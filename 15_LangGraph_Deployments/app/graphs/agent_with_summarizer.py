"""An agent graph with a post-response TL;DR summarizer.

After the agent responds, a summarizer node condenses the response to 1-2 sentences
and prepends it as "TL;DR:" at the beginning of the final output.
"""
from __future__ import annotations

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage

from app.state import MessagesState
from app.models import get_chat_model
from app.tools import get_tool_belt


def _build_model_with_tools():
    """Return a chat model instance bound to the current tool belt."""
    model = get_chat_model()
    return model.bind_tools(get_tool_belt())


def call_model(state: MessagesState) -> dict:
    """Invoke the model with the accumulated messages and append its response."""
    model = _build_model_with_tools()
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}


def route_to_action_or_summarizer(state: MessagesState):
    """Decide whether to execute tools or run the summarizer."""
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "action"
    return "summarizer"


_summarizer_prompt = ChatPromptTemplate.from_template(
    "Condense the following response into exactly 1-2 concise sentences. "
    "Preserve the key information.\n\n"
    "Response:\n{response}"
)


def summarizer_node(state: MessagesState) -> dict:
    """Add a TL;DR (1-2 sentence summary) at the beginning of the agent's response."""
    last_message = state["messages"][-1]
    original_content = getattr(last_message, "content", "") or ""

    if not original_content.strip():
        return {"messages": [AIMessage(content=original_content)]}

    model = get_chat_model(model_name="gpt-4.1-mini")
    summary = (_summarizer_prompt | model).invoke({"response": original_content})
    tldr = summary.content.strip() if hasattr(summary, "content") else str(summary)

    enhanced_content = f"TL;DR: {tldr}\n\n{original_content}"
    return {"messages": [AIMessage(content=enhanced_content)]}


def build_graph():
    """Build an agent graph with a TL;DR summarizer node."""
    graph = StateGraph(MessagesState)
    tool_node = ToolNode(get_tool_belt())
    graph.add_node("agent", call_model)
    graph.add_node("action", tool_node)
    graph.add_node("summarizer", summarizer_node)
    graph.add_edge(START, "agent")
    graph.add_conditional_edges(
        "agent",
        route_to_action_or_summarizer,
        {"action": "action", "summarizer": "summarizer"},
    )
    graph.add_edge("action", "agent")
    graph.add_edge("summarizer", END)
    return graph


graph = build_graph().compile()
