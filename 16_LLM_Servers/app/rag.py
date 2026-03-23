"""Retrieval-Augmented Generation (RAG) utilities and tool.

This module builds an in-memory RAG pipeline that:
- Loads PDF documents from `RAG_DATA_DIR` (default: "data").
- Splits documents into chunks using a token-aware splitter.
- Embeds chunks and generates answers via Fireworks AI or OpenAI (provider-selectable).
- Stores vectors in an in-memory Qdrant store.
- Exposes a LangChain Tool `retrieve_information` that retrieves relevant
  context and generates a response constrained to that context.
"""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Annotated, TypedDict

import tiktoken
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langgraph.graph import START, StateGraph


def _tiktoken_len(text: str) -> int:
    """Return token length using tiktoken; used for chunk length measurement."""
    tokens = tiktoken.encoding_for_model("gpt-4o").encode(text)
    return len(tokens)


class _RAGState(TypedDict):
    """State schema for the simple two-step RAG graph: retrieve then generate."""

    question: str
    context: list[Document]
    response: str


def _build_rag_graph(data_dir: str, provider: str = "fireworks"):
    """Construct and compile a minimal RAG graph.
    Args:
        data_dir: directory containing the PDF documents
        provider: provider to use for the embeddings and generation model
    Steps:
    1) Load PDFs from `data_dir` recursively (best-effort).
    2) Split documents into token-aware chunks.
    3) Create embeddings and an in-memory Qdrant vector store retriever.
    4) Define a chat prompt and generation model.
    5) Wire a two-node graph: retrieve -> generate.
    """
    # Load PDFs from data directory (recursive)
    try:
        directory_loader = DirectoryLoader(
            data_dir, glob="**/*.pdf", loader_cls=PyMuPDFLoader
        )
        documents = directory_loader.load()
    except Exception:
        documents = []

    # Split documents
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=750, chunk_overlap=0, length_function=_tiktoken_len
    )
    chunks = text_splitter.split_documents(documents) if documents else []

    # Embeddings and vector store (in-memory Qdrant)
    if provider == "fireworks":
        embedding_model = OpenAIEmbeddings(
            model=os.environ.get("FIREWORKS_EMBEDDING_MODEL", "accounts/fireworks/models/qwen3-embedding-8b"),
            openai_api_key=os.environ["FIREWORKS_API_KEY"],
            openai_api_base="https://api.fireworks.ai/inference/v1",
            check_embedding_ctx_length=False,
            dimensions=4096,
        )
    elif provider == "openai":
        embedding_model = OpenAIEmbeddings(
            model=os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
            openai_api_key=os.environ["OPENAI_API_KEY"],
        )
    qdrant_vectorstore = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embedding_model,
        location=":memory:",
        collection_name="rag_collection",
    )
    retriever = qdrant_vectorstore.as_retriever()

    # Prompt and model
    human_template = (
        "\n#CONTEXT:\n{context}\n\nQUERY:\n{query}\n\n"
        "Use the provided context to answer the user query. "
        "Only use the provided context to answer the query. If you do not know the answer, or it's not contained in the provided context respond with \"I don't know\""
    )
    chat_prompt = ChatPromptTemplate.from_messages([("human", human_template)])
    if provider == "fireworks":
        generator_llm = ChatOpenAI(
            model=os.environ.get("FIREWORKS_CHAT_MODEL", "accounts/fireworks/models/gpt-oss-20b"),
            openai_api_key=os.environ["FIREWORKS_API_KEY"],
            openai_api_base="https://api.fireworks.ai/inference/v1",
        )
    elif provider == "openai":
        generator_llm = ChatOpenAI(
            model=os.environ.get("OPENAI_CHAT_MODEL", "gpt-4.1-mini"),
            openai_api_key=os.environ["OPENAI_API_KEY"],
        )

    def retrieve(state: _RAGState) -> _RAGState:
        retrieved_docs = retriever.invoke(state["question"]) if retriever else []
        return {"context": retrieved_docs}  # type: ignore

    def generate(state: _RAGState) -> _RAGState:
        generator_chain = chat_prompt | generator_llm | StrOutputParser()
        response_text = generator_chain.invoke(
            {"query": state["question"], "context": state.get("context", [])}
        )
        return {"response": response_text}  # type: ignore

    graph_builder = StateGraph(_RAGState)
    graph_builder = graph_builder.add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    return graph_builder.compile()


@lru_cache(maxsize=2)
def _get_rag_graph(provider: str = "fireworks"):
    """Return a cached compiled RAG graph built from RAG_DATA_DIR."""
    data_dir = os.environ.get("RAG_DATA_DIR", "data")
    return _build_rag_graph(data_dir, provider)


@tool
def retrieve_information(
    query: Annotated[str, "query to ask the retrieve information tool"],
):
    """Use Retrieval Augmented Generation to retrieve information about feline health, including life stage care, nutrition, vaccinations, parasite control, behavior, diagnostics, and veterinary guidelines for cats."""
    graph = _get_rag_graph()
    result = graph.invoke({"question": query})
    # Prefer returning the response string if available
    if isinstance(result, dict) and "response" in result:
        return result["response"]
    return result


def run_rag_pipeline(question: str, provider: str = "fireworks") -> dict:
    """Run the RAG pipeline and return contexts + answer for RAGAS evaluation.

    Args:
        question: The user question.
        provider: "fireworks" or "openai".

    Returns:
        Dict with "contexts" (list of retrieved doc strings) and "answer" (generated response).
    """
    graph = _get_rag_graph(provider)
    config = {
        "tags": [f"provider:{provider}"],
        "metadata": {"provider": provider},
        "run_name": f"rag-{provider}",
    }
    result = graph.invoke({"question": question}, config=config)

    contexts = []
    if isinstance(result, dict) and "context" in result:
        for doc in result["context"]:
            if hasattr(doc, "page_content"):
                contexts.append(doc.page_content)
            elif isinstance(doc, str):
                contexts.append(doc)

    answer = ""
    if isinstance(result, dict) and "response" in result:
        answer = result["response"]

    return {"contexts": contexts, "answer": answer}