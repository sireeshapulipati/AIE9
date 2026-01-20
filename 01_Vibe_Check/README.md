<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](https://github.com/AI-Maker-Space/AIE9/blob/main/00_Docs/Session_Sheets/01_Vibe%20Check.md) | Coming Soon! | Coming Soon! | You are here! | Coming Soon! | Coming Soon! |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested: How the app responds to unrelated question. It accurately explained what OOP is with an example, even though this is not related to the domain/function of the app - which is Mental coach. This surprised me. As an user, I would expect the app to refuse to answer this unrelated question and direct me to its core competence. The response is not formatted well, just a block of text.
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: Correctly prompts the user to provide the paragraph, when it's missing. It also asks for any focus for summarization - themes, arguments, action items. This is really good, guiding the user to clarify the expectations.
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: It took some time (longer than the previous responses) to produce the output. The story was weird, but interesting. A robot's frienship with a lighthouse. The story was within the word limit mentioned, which is good.
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: Does it do the math correctly? It does. provides answer with equations and as a sentence. Also adds something extra - Nice and tidy!
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: Asks for the paragraph; and also for constraints - length limit, level of formality, region-specific English. It proactively says it can provide 2 versions - moderately formal and highly formal. Also provides a list of tips it can apply. Which is all cool!

#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer: Yes, the answers appear correct and are useful

---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: Help me think through the pros and cons of doing Master's. degree in AI
   - Result: Great question. A Master’s in AI can be a powerful catalyst, but it’s not the only path. Here’s a balanced way to think it through. Potential upsides - Structured, rigorous foundation: Deep math (linear algebra, probability), core ML, optimization, systems—skills that outlast tool churn. - Research exposure: Access to labs, publications, conferences, and strong letters of recommendation (especially if you might do a PhD later). - Brand and network: Faculty, peers, alumni, and recruiting pipelines can open doors you can’t easily get solo. - Projects with resources: Compute credits, datasets, industry-sponsored capstones, and mentorship. - Career switching signal: For non-CS backgrounds, a Master’s can credibly reset your trajectory. - Internships and recruiting windows: University channels, career fairs, and internships that often convert to offers. - Focus and accountability: Deadlines and structure can accelerate mastery. - Immigration/relocation enabler: For some countries, student status can be a practical pathway (confirm specifics with an advisor). Potential downsides - Cost and opportunity cost: Tuition + living + lost salary during study can be substantial. - Rapidly evolving tools: Some course content may lag industry; you’ll still need ongoing self-learning. - Time and stress: Intense workload; less time for earning, family, or side projects. - Not strictly required: Many AI/ML and AI-adjacent roles hire strong engineers without a Master’s. - Specialization risk: Over-focusing on a niche that may not match job openings where you want to live. - Admissions and prerequisites: Math/programming gaps can make the ramp-up tough if not prepared. Who tends to benefit most - Aspiring researchers or future PhD candidates. - Career switchers who need a strong technical signal and structured path. - Engineers aiming for roles that value research depth (applied scientist, research engineer) or top-tier labs. - People who thrive in academic environments and want access to faculty, labs, and compute. Who may not need it (or not now) - Strong software/data engineers already shipping ML features and accumulating a solid portfolio. - Founders/operators focused on rapid product cycles using foundation-model tooling where speed and product sense dominate. - Those who can get similar outcomes via employer-sponsored projects, AI residencies, or apprenticeships. Alternatives and hybrids - Self-study + portfolio: fast.ai, CS229/CS231n, DeepLearning.AI, Hands-On ML; implement classic papers; open-source contributions; Kaggle or real-world datasets. - Work-first path: Join a company with ML teams, then pivot internally while building experience. - Certificates/micro-masters: Lower cost/time, enough to break into MLOps, LLM app dev, or data-centric roles. - Part-time/online Master’s: Reduce opportunity cost while working. - AI residencies/fellowships or RA roles: Especially good if research is your goal. How to evaluate programs - Faculty and labs: Whose work genuinely excites you? Do they take Master’s students into their groups? - Curriculum freshness: Modern deep learning, LLMs, ML systems, data-centric AI, MLOps, responsible AI. - Industry links: Capstones with companies, internships, alumni at places you want to work. - Placement outcomes: Roles, sectors, locations; ask for recent data and talk to alumni. - Compute and data access: GPUs, cloud credits, engineering support. - Format fit: Thesis vs coursework; in-person vs online; full vs part-time. - Support: Career services, immigration advising, mental health resources, funding options (TA/RA/scholarships). A quick ROI frame - Total cost of attendance = tuition + fees + living + relocation + interest minus any funding. - Opportunity cost = salary you’d otherwise earn during the program. - Expected uplift = (post-degree salary – current salary) × probability of landing your target role. - Break-even years ≈ (total cost + opportunity cost) / expected annual uplift. - Stress-test: What if uplift is smaller or takes 12–18 months post-graduation? If-then heuristics - If you want to do research or keep a PhD option open, a strong thesis Master’s is often worth it. - If you mainly want to build and deploy AI features quickly, a portfolio plus strong SWE/MLOps skills may be faster. - If you lack core math/ML foundations and struggle to stay consistent solo, the structure of a Master’s helps. - If finances are tight and you can learn on the job, consider delaying or doing part-time/online. Practical next steps - Do a 6–8 week “pilot”: take a rigorous ML course, reproduce a paper, and ship a small end-to-end project. This tests fit before committing. - Informational interviews: Speak with 5+ alumni from programs you’re considering and 5 professionals in roles you want. Ask what actually moved the needle. - Gap analysis: Compare target job descriptions to your skills; note gaps in math, systems, data engineering, or domain expertise. - Build one substantive project: Preferably with real users/data and clear business or research impact. - Financial plan: Map costs, funding options, and a conservative ROI; decide your break-even tolerance. - Shortlist programs: 3–5 that match your goals; verify faculty availability and capstone options. I can tailor this much better with a bit of context. Could you share: - Your current background (degree, years of experience, main skills). - Your target roles (e.g., applied scientist, ML engineer, AI researcher, AI product). - Whether you’re open to research/thesis and possibly a PhD later. - Constraints around time, location, visa, and finances. - Your timeline and urgency to switch or level up. - One or two companies or problems that genuinely excite you.
2. Prompt: What can I cook with paneer in fridge.
   - Result: Nice choice—paneer is super versatile. Pick something that matches your energy and what you’ve got on hand. Quick (10–15 min) - Paneer Bhurji (scrambled paneer) - Sauté onion, green chili, and garlic in a little oil. - Add tomatoes, turmeric, chili powder, cumin, salt; cook 2–3 min. - Crumble in paneer; stir 2–3 min. Finish with garam masala and lemon. - Great with toast, roti, or in a wrap. - Chili Paneer (dry, no batter) - Sear paneer cubes in a little oil; set aside. - Stir-fry garlic, onion, bell pepper; add soy sauce, vinegar, chili sauce, pinch of sugar. - Toss paneer back in; finish with pepper/scallions. - Paneer Wrap/Quesadilla - Use leftover bhurji or spiced paneer. - Fill tortilla/roti with paneer and veggies/cheese; toast till crisp. Comforting curries (15–25 min) - Quick Palak Paneer - Blend spinach (fresh or thawed frozen) with a splash of water. - Temper cumin in oil, add garlic, onion, then tomato, turmeric, coriander, chili. - Stir in spinach purée, simmer 3–4 min; add paneer, salt, splash of cream or yogurt. - Easy Matar Paneer - Fry onion + ginger-garlic; add tomato, turmeric, coriander, garam masala. - Add water, frozen peas, simmer 5 min; add paneer, finish with kasuri methi (if you have it). - Paneer Butter Masala (creamier) - Sauté onion, tomato, cashews (optional) with spices; blend smooth. - Simmer with butter, a little cream; add paneer and a pinch of sugar. Grill/oven/air-fryer (15–20 min) - Paneer Tikka - Marinade: yogurt, ginger-garlic, lemon, turmeric, chili, garam masala, salt, oil. - Toss paneer + peppers/onion; skewer or spread; broil/air-fry till charred edges. Lemon to finish. Fusion and bowls (10–20 min) - Paneer Fried Rice - Sauté garlic and mixed veggies; add leftover rice, soy sauce, pepper, a splash of vinegar. - Stir in browned paneer; finish with sesame oil. - Quick Salad Bowl - Pan-sear paneer; toss with greens, cucumber, tomato, onion. - Dress with lemon + olive oil + salt + chaat masala (or cumin + pepper). Tips - Press paneer with paper towels before frying; it browns better. - If it smells sour or feels slimy, skip it. - No cream? Use milk + a bit of butter or cashew paste. What do you have on hand (onion, tomato, spinach, peppers, peas, yogurt, tortillas/rice?) and how much time do you want to spend? I can tailor one of these to exactly what you’ve got.
3. Prompt: Help me plan a birthday surprise for my best friend who lives close to me.
   - Result: Love this—let’s make it memorable and low-stress for you. Here are a few solid surprise concepts you can choose from, plus a simple timeline and scripts. Pick one and I’ll tailor it to your friend’s vibe, budget, and timing. Five flexible surprise ideas 1) The “Favorite Things” Day (simple, heartfelt) - Morning: Drop their favorite coffee/pastry at their door with a handwritten note and a balloon. - Afternoon: Picnic at a nearby park or living-room picnic if weather’s bad. Add a mini photo album or memory jar. - Evening: Small gathering at your place with their favorite takeout, cake, and a custom playlist. 2) At-Home Pop-Up Theme (works for introverts) - Get them out for 60–90 minutes (coffee run, errand) while you transform their space or yours (theme ideas: cozy speakeasy, cottagecore, game lounge). - Decor: String lights, a banner, a few themed touches, and a photo garland. - Activity: A short “toast circle,” a game, or a DIY dessert bar. 3) Progressive Mini-Surprise Walk (fun, light movement) - Plan a short walking route (3–5 stops) near you: a friend waiting with flowers, a coffee pickup, a street musician or curated playlist moment, a surprise guest at the park, then cake at the final stop. - Works great for 2–6 guests joining along the route. 4) Backyard/Outdoor Movie Night - Projector + sheet, blankets, fairy lights. - Pre-movie “trailer” of your photos together, then their favorite film. - Snack board, popcorn bar, warm drinks. Rain plan: same setup indoors. 5) Mini Scavenger Hunt to a Final Reveal - 4–6 clues tied to inside jokes and favorite spots, ending at a decorated space with friends. - Keep clues easy; focus on nostalgia and laughs. Personal touches that land - Memory jar: friends add short notes (“A favorite memory with you…”). - “Soundtrack of You” playlist. - Small custom cake topper or photo cake. - A framed photo or mini scrapbook of the last year. - A “coupon” booklet (coffee dates, rides, dog-sitting, movie night). Simple timeline - 1 week out: Pick a plan, quietly confirm 2–6 key people, order cake/balloons, reserve projector or picnic kit. - 3–4 days out: Buy decor/snacks, prep playlist, write clues/notes, confirm weather backup. - Day before: Pre-stage decor kit, charge speakers/phones, chill drinks, prep servingware. - Day of: Quick tidy/decor, pick up cake/flowers, do a test run (music/lighting), breathe. Quick checklists - Essentials: cake, candles + lighter, knife/plates/napkins, drinks/ice, trash bags, phone chargers, playlist speaker. - Decor: banner, balloons, string lights, one focal piece (photo garland or flowers). - Comfort: extra seating/blankets, bug spray if outdoors. - Safety/considerations: dietary needs, allergies, neighbor quiet hours, weather backup. Easy cover stories (pick one) - “Want to try that new coffee spot? My treat.” (leads to decorated space on return) - “I found a short walking route with a surprise view. Up for a mini adventure?” - “Help me taste-test snacks for a ‘movie night’?” (actually their movie night) Budget notes (rough) - Low: $40–$100 (homemade treats, DIY decor, memory jar). - Mid: $100–$250 (takeout, cake, projector rental or a few themed items). - Higher: $250+ (catered bites, custom cake, professional photos). To tailor this perfectly, share: - Indoors or outdoors? Any weather constraints. - Guest count (just you, a few close friends, or 8–12?). - Their vibe: cozy/quiet vs social/energetic. - Favorite foods/drinks, music, and any no-gos (diet, allergies). - Timing (date, time window, prep time you have). - Budget range. You’ve got this. Pick the idea that feels easiest and most “them,” and I’ll turn it into a precise checklist, budget, and text templates for invites and decoy messages.

#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer: These are generic responses, not specifically rooted in my preferences (understandbly). However, they are useful as they are often comprehensive, and different options are provided as well. It would have been great, if it asked me clarifying questions first and then answered, using that information.

---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: What's the current stock price of Shopify
   - Result: I don’t have live market data access. To see the current price of Shopify, check: - Ticker: SHOP (NYSE) or SHOP.TO (TSX) - Your broker app, or sites like Google Finance, Yahoo Finance (quote/SHOP), TradingView, or Bloomberg (SHOP:US) Note that premarket/after-hours prices can differ from the regular session. If you share the price you see, I can help you interpret the move or set up calm, practical alert levels so you’re not glued to the ticker.
2. Prompt: How many meetings do I have this week?
   - Result: I can’t see your calendar, so I don’t know yet. But I can help you get the number fast. Pick one: - Tell me which calendar you use (Google Calendar, Outlook desktop/web, Apple Calendar) and what you count as a “meeting” (e.g., exclude holds/all‑day events?), and I’ll give step‑by‑step instructions. - Paste your week’s events (an agenda/schedule view works best) and I’ll count and summarize them for you. - DIY quick steps: - Google Calendar (web): switch to “Schedule” view, hide Tasks/Reminders/Birthdays in the left panel, then scan Monday–Sunday and count entries that have guests or a conferencing link. - Outlook desktop: open Calendar, View > Change View > List, filter for “This Week” and you’ll see a count of items in the status bar; exclude all‑day holds if needed. - Apple Calendar (Mac): View > Show List, select this week’s dates in the mini‑calendar, then count listed events. If you’re asking because the week feels packed, tell me roughly how many you saw and I can help you triage (what to decline, shorten, or batch) and protect some focus time.

#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer: It does not have access to any tools (Calendar, Web Search, API calls etc.) or any real-time data.

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_
Updated the system prompt to:
- Require GitHub-flavored Markdown responses
- Use headings, subheadings, bullet lists, numbered lists, and short paragraphs
- Handle unrelated questions: decline to answer, state the system's purpose/expertise, and provide 3-5 example mental health questions

##### Results:
1. _Comment here how the change(s) impacted the vibe check of your system_
2. When an related question is asked, it doesn't answer it. rather states its purpose, gives reasons why it it's not answering my question, gives me example questions to ask; 
3. When I prompted with "What can I cook with milk and bread?", in addition to the above content, it also provided related mental health response - "If meal planning feels overwhelming....", which I find very interesting. Maybe because the system prompt includes - you are a supportive mental coach??
4. The responses are well formatted and easy to read; not a wall of text like earlier
5. It did answer the "help me think through pros and cons.." questions though. Is it really related to its scope? - stress, motivation, habits, confidence. Hmm!


## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.
