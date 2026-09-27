# U6 L09: Ethics and the Law — PIPL, and Where It Differs (May 18, Tue — P130)

**Date:** Tue May 18, 2027
**Unit:** 6 — Post-Exam and Portfolio
**Period:** P130
**Gradebook category:** Participation
**LOs:** 1.C (analyse regulatory constraints) · 4.A (consider the human and organisational context) · 3.D (detection and reporting obligations)

**Materials:** Comparison notes template, primary legal texts (read online, not from summaries), your capstone compliance section, the four-line incident note structure

**📄 PAPER DAY. No new technical content — this is judgement, and judgement is what the exam and the job both test.**

**The framing for the whole lesson, and it is the important part:** you will be tempted to memorise statute sections. Don't. **Statute changes, and memorised section numbers go stale.** What does not go stale is the *shape* of the reasoning: identify the data, identify who is responsible for it, identify the obligation, identify the trigger, identify the clock. Learn the shape, verify the specifics from the primary text, and you will be right in a country you have never visited.

---

## PART 1 — THE SHAPE OF A REGULATORY ANSWER (10 min)

**The structure. Use it for every legal question you meet, in any jurisdiction, for the rest of your career:**

1. **What data is in scope?** Identify the category — personal data, sensitive data, health data, financial data, credentials, telemetry. *The scope determines whether the law applies at all.* A great many bad compliance answers start by not doing this step.
2. **Who is responsible?** Name the role, not the company. Data controller, processor, organisation, employer, service provider. **The obligation attaches to a role, and roles are assigned — that is why an organisation's governance document is the first thing you look at.**
3. **What is the obligation?** Notify the authority, notify the affected individuals, obtain consent, record the processing, secure the data, honour a subject's request, restrict transfers.
4. **What triggers it?** A breach, a new purpose, a cross-border transfer, a subject request, an acquisition. *Triggers are the part people miss* — an obligation with no trigger never fires.
5. **What is the clock?** Any deadline, and what the deadline runs from. **A deadline with no stated start point is not a deadline** — knowing the start point is the mark of someone who has read a real policy.
6. **What is the practical consequence?** What must you actually do, operationally, on day one?

**Write all six on the card. This is the artifact.** Every specific figure in this lesson is an *example* of the shape at work, and the examples are here so you can see the shape filled in — not so you can memorise them.

## PART 2 — TAIWAN'S DATA-PROTECTION FRAMEWORK, VERIFIED FROM THE PRIMARY TEXT (14 min)

**Method, and this is the graded part: go to the primary legal text, not to a summary, not to a blog, not to my description.** Summaries of data-protection law are frequently wrong in exactly the details that matter, and a professional who cannot find the primary text is a professional with a liability problem.

**Go to the primary text of Taiwan's Personal Data Protection Act (PIPL).** Work through it and fill in the six-part shape:

- ☐ **Scope (1):** What counts as personal data under the Act? Does it include some categories the GDPR would treat differently? **Note anything that is defined broadly here.**
- ☐ **Responsible party (2):** Which role carries the obligations, and how is that role assigned in practice? How does that differ from an organisation that is simply the employer?
- ☐ **Obligations (3):** List the duties — security measures, notification on a data incident, purpose limitation, retention. **Read the operative language, do not paraphrase from memory.**
- ☐ **Triggers (4):** What event starts the clock? A confirmed breach? A suspected one? Awareness of what, exactly? **This is the detail that separates a real answer from a plausible one.**
- ☐ **The clock (5):** What is the deadline for notifying the competent authority? What is the deadline for notifying affected individuals? **Write the number and cite the provision you found it in.** Note: cross-border transfer of personal data outside Taiwan is itself a regulated activity with its own conditions — find that provision, because it is a genuinely distinctive feature of a local framework and it is very relevant to a Taiwanese candidate.
- ☐ **Consequence (6):** What must you actually do operationally, in the first hours?

**Write the citations.** A page of notes with no provision references is not research, it is recollection.

**And one thing to be careful about, because students get this wrong every year:** the exact thresholds, deadlines, and definitions in this law have been subject to amendment and to related statutes and implementing rules. **If the primary text and a secondary summary disagree, the primary text wins, and saying so in your notes is worth more than being right by accident.**

## PART 3 — WHERE IT DIFFERS FROM THE US, STRUCTURALLY (14 min)

**Not a list of differences — a set of structural contrasts.** This is the framing that generalises.

**Contrast 1 — the constitutional frame.**
The US has a patchwork: no single federal general data-protection statute of the kind PIPL is, instead sectoral and state-level regimes — state breach-notification statutes, sector-specific rules for health and financial data, and distinct regimes for different data types. Taiwan's is a single general statute applying broadly across sectors, administered by a competent authority.

**The consequence for you, and this is the real lesson:** *the same incident triggers a different set of obligations, on a different clock, to a different recipient, depending on where the organisation and the affected individuals are.* A global company cannot have one data-protection posture. If you are ever asked — in an interview, in a portfolio, in an incident — **"whose law applies?"** is the first question, and asking it is the mark of someone who has thought about it.

**Contrast 2 — the trigger and the audience.**
US state breach-notification regimes are generally triggered by **unauthorised acquisition of, or access to, personal information** of a defined category, and route primarily to **affected individuals** and to the state attorney general, with thresholds varying by state and by data type. PIPL's structure is built around the **data controller's obligations** and routes notifications to **the competent authority** as well as to affected individuals, with a shorter and more prescriptive clock.

**Say this carefully and without overclaiming:** the structural difference is *where the duty sits and who receives the notification.* That is a real, checkable contrast, and it is enough for the comparison. **Do not assert specific deadlines for the US side without checking a specific state's statute** — state law varies and that variation is itself the point of contrast 1.

**Contrast 3 — enforcement and the role of the individual.**
The frameworks differ in how much weight they give to individual rights and to regulator-driven enforcement. **Look this up and cite it.** This is where careful reading pays off and where a confidently wrong statement is most embarrassing.

**Contrast 4 — the workplace and employee context.**
Different rules apply to monitoring, to employee data, and to workplace devices. In a security role you will be the person who implements these, so the contrast is operational, not theoretical.

**The deliverable, and this is the artifact:** a **one-page comparison** — a real table, not a list — with the six-part shape as rows and Taiwan and the US as columns, every cell either cited or marked `not verified`. **The empty cells are the point.** A comparison that has filled in every cell without checking the primary sources is not thorough; it is confident, and those are different things.

## PART 4 — APPLY IT: THE FOUR-LINE INCIDENT NOTE (7 min)

**The capstone exercise, and it is the same structure you used on May 3 and again on May 6. It is now yours.**

Scenario: a Taiwanese online retailer suffers an incident in which customer personal data may have been exposed. **Write the four lines:**

1. **Which topic owned the failure** — the control that was missing or misconfigured.
2. **Which control would have detected it, how much sooner, and from what source.**
3. **What obligation was triggered, owed to whom, on what clock** — using the six-part shape, and naming the framework that actually applies.
4. **The single cheapest change that would have reduced the impact.**

**Then the hard follow-up, and it is the one that separates a compliance answer from a compliance *understanding*:** *what would change if the affected customers were mostly outside Taiwan?* **"Whose law applies" just became a live question**, and the fact that you can ask it puts you ahead of most candidates.

## 🇹🇼 TAIWAN CONTEXT

**3-minute brief.** One current TWNCERT or iThome item involving personal data, and the four-line note applied to it.

**The portfolio point, and it is genuinely strong:** you can now write a short piece titled something like *"What a Taiwan-based security engineer knows that a US-based one does not."* The argument is not that other frameworks are worse — it is that they are **different**, and that operating across both requires asking whose law applies before you decide what to do. **That is a genuine professional advantage and it is one you can evidence in writing by Friday.**

**One caution, because the failure mode is real and it is a credibility failure:** do not turn a comparative legal lesson into advocacy about which system is better. The professional claim is *"the frameworks differ structurally in where the duty sits and who receives notification, and I can work in both."* The personal claim is *"one is better"* and it is not supported, it is not professional, and in an interview it marks you as someone who has an opinion instead of an analysis.

## CLOSE (2 min)

Collect the six-part card, the one-page comparison, and the four-line note.

**Next: Wed May 19, P131 — Session 8 debrief: OWASP Juice Shop findings.** **Saturday May 22 is the CTF session itself**; this is where you prepare, and the web app writeup is the deliverable. **Then May 20–25 is thesis week — no school, nothing scheduled — and portfolio build day 2 is Wednesday May 26.** You are working with one week of slack in the middle; use it deliberately rather than discovering it late.

## TURN IN —

1. **The six-part regulatory shape card**, with a filled-in example under each part.
2. **The Taiwan PIPL research notes**, in the six-part shape, **with provision citations for every specific figure and every number written down with the source and the date you read it.** Unsourced numbers are the failure I am looking for.
3. **The one-page Taiwan-versus-US comparison table.** Six-part shape as rows, jurisdictions as columns, **every cell cited or marked `not verified`.** The `not verified` cells must be genuine — I want to see where you stopped and did not guess.
4. **The four-line incident note** plus the answer to *"what would change if the affected customers were mostly outside Taiwan?"*
