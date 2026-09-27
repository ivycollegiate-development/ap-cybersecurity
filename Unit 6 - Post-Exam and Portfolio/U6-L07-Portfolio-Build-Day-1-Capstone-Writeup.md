# U6 L07: Portfolio Build Day 1 — The Capstone Writeup (May 14, Fri — P128)

**Date:** Fri May 14, 2027
**Unit:** 6 — Post-Exam and Portfolio
**Period:** P128
**Gradebook category:** Participation
**LOs:** 4.A–4.C (Collaborate and communicate) · 2.D (mitigate, in writing) · 1.C (revise against a standard)

**Materials:** Laptops, your portfolio repo, your portfolio structure from May 10, your career memo from May 12, the capstone materials, the writeup standard below

**Graded as: Final Projects.** 🔨 **BUILD DAY 1 OF 3.**

**Build days are working days.** The lesson content is the standard below and the demonstration. The rest of the period is your writing. If you finish early, you start the next piece — do not treat finishing early as permission to stop.

**The schedule, so you can see what you are working toward:**

| Day | Date | Build target |
|-----|------|--------------|
| **Build 1** | **Fri May 14** | **Capstone writeup — working draft** |
| Build 2 | Wed May 26 | Polish, README, screenshots — near-final |
| Peer review | Thu May 27 | Reviewed and revised |
| **Present** | **Fri May 28** | 5-minute portfolio presentation |

**Note the gap: May 20–25 is thesis week and there is no school.** That is deliberate. It means this Friday and then May 26 are the two working days you have, and the thesis week is yours to use or to waste. **Plan accordingly — if the capstone needs four hours and you only have two, find that out today, not on May 26.**

---

## PART 1 — THE CAPSTONE, AND WHY IT IS THE BEST THING YOU OWN (10 min)

The capstone — a cybersecurity team hired by a Taiwan critical infrastructure operator, defending a chosen sector against a modelled advanced persistent threat — produced a threat model, a layered architecture, a control mapping, and a compliance analysis. **As a slide deck, it is decent. As a portfolio piece, it is currently weak, and the reason is instructive.**

A deck is made to be presented. A portfolio piece is made to be **read, alone, by a stranger who has never heard you speak.** Those are different products, and the conversion is the work of today.

**The three things a deck has and a portfolio piece must not:**
- ☐ **The narrator.** In a deck, you supply the argument by talking. In a document, every claim must carry its own evidence.
- ☐ **The abbreviations.** Your team knew what your notation meant. A stranger does not. Every acronym expanded on first use.
- ☐ **The assumed context.** The scenario you were handed. A stranger needs it restated in two sentences.

**The two things a portfolio piece needs and a deck usually lacks:**
- ☐ **The reasoning between the control and the threat.** A diagram showing a WAF in front of an app tells a reader nothing. *"A WAF was placed at the application boundary because threat T3 targets the application layer directly, and the specific mitigation for T3 in the threat model was input validation at the app rather than network-level filtering"* tells a reader everything — it demonstrates that the architecture came from analysis and not from a template.
- ☐ **The honest limitation.** What the design does not cover, what you would do next, and what you got wrong. **This is the section that converts an assignment into a portfolio piece**, because it demonstrates exactly the judgement the Credential Ladder says employers screen for.

## PART 2 — THE PORTFOLIO-PIECE STANDARD (12 min)

**Write your capstone piece to this standard. It is the standard for every featured piece in your portfolio, not just this one.**

**Length: 700–1,000 words.** Not 400 (too thin to show thinking) and not 3,000 (nobody reads it).

**Structure — six sections, in this order:**

**1. The situation (2–3 sentences).** Restate the scenario for a stranger: sector, the threat, the scope of the engagement. No assumed context.

**2. The question I was answering (2–3 sentences).** What was actually being asked. Almost nobody writes this and it is what lets a reader follow everything after it.

**3. The analysis (25% of the piece).** Threat model, risk reasoning, and the decisions that followed from them. **Show the reasoning, not just the conclusion.** The sentence "we chose X because Y" is worth ten times the sentence "we chose X."

**4. The design (25%).** The architecture and controls, as text with a diagram. **For every control: the threat it addresses, and the reasoning that connected them.** This is where the third thing from Part 1 goes.

**5. What I would do differently (20%).** The limitations section. Three to five specific things:
- ☐ A gap in the design you can now name.
- ☐ A control you included that you are not sure earns its place — and why.
- ☐ A threat you modelled badly in retrospect.
- ☐ A control you omitted that you would add with more time.
- ☐ Something about the *process* — the method that would have produced a better design.

**This section is not a humblebrag and it is not an apology.** It is a demonstration that you can evaluate your own work, which is the hardest professional skill and the one nobody can fake.

**6. The artefacts (the rest).** Links to the deck, the diagrams, the risk register. **Do not embed everything** — a portfolio piece that embeds fifteen artefacts is a portfolio piece nobody finishes.

**House style, carried over from the year:**
- Speaker is **"I"** — never the teacher by name, and never "the teacher." *"I built," "I argued," "I was wrong about."* This is a portfolio; the voice is yours.
- Specific over general. *"Parameterized queries" beats "secure coding."* *"A WAF with rules matching the UNION SELECT pattern observed in T3"* beats "a WAF."
- **Every claim traceable to something in the capstone.** Do not assert a finding you did not produce.
- If you are going to describe a real incident or a real tool's behaviour, **verify it or do not assert it.** Describe what you observed, not what you expect would have happened.

## PART 3 — BUILD TIME (18 min)

**Write the draft. Not an outline — a draft.** I would rather read four rough paragraphs than a perfect plan.

**Start here, in this order, and do not skip forward:**
1. Section 5 first. *What I would do differently.* It is the hardest to write, it is the highest-value section, and writing it first makes sections 1–4 easier because you know where you are being honest.
2. Then section 3, the analysis.
3. Then section 4, the design with the control-to-threat reasoning.
4. Then sections 1, 2, and 6, which are quick once the middle exists.

**Working rules:**
- ☐ Write in the repo, in a file, committed as you go. **Commit history is itself portfolio evidence** — a document with ten commits tells a story a single commit does not.
- ☐ Set a 20-minute timer on the first draft and **do not edit while writing it.** Editing and drafting at the same time is how you end up with a polished version of an empty argument.
- ☐ If you are stuck on a section, write the question at the top of the file and move to another section. Come back.

**What to do when you finish early, and this is a real instruction:**
- ☐ Start the README for your portfolio repo. You need one for May 26; starting it now means May 26 is polish rather than construction.
- ☐ Or start section 5 of a *second* featured piece.
- ☐ Or re-read your career memo and revise it now that you have written three pages of actual prose — you will see things in it you did not see on Tuesday.

## PART 4 — THE STRESS TEST (5 min)

**One question, asked to two people at your table, and answered honestly:**

> *"I read this and I concluded ____. Do you actually support that, or did I fill it in?"*

This is the whole method of technical writing compressed into one move. A reader will always infer a conclusion from your evidence, and the gap between the conclusion you drew and the conclusion you wanted them to draw is where miscommunication lives. **Ask the question, find out, and fix it.** Every unclear sentence in a portfolio piece is a place where the reader filled in something you did not intend.

## 🇹🇼 TAIWAN CONTEXT

**The capstone was Taiwan-specific, and that is the point — not the decoration.**

**For the portfolio, write the local context as a *design constraint*, not as colour.** The difference matters enormously and it is the difference between a candidate who has been to a place and a candidate who understands it.

- **Not this:** "We chose a semiconductor fab, which is a critical industry in Taiwan."
- **This:** "We chose semiconductor manufacturing because the concentration of advanced fabrication capability in this region makes it a high-value target, which changes the threat model in two specific ways: the adversary's objective is likely operational disruption rather than data theft, and the tolerable downtime is measured in hours rather than days, which rules out controls that require a maintenance window."

**That second version demonstrates three things in one sentence: you understand the local context, you know how it propagates into a design decision, and you can reject an option based on a stated constraint.** That is a professional sentence. This is where a Taiwanese candidate beats a candidate who chose a generic sector.

**Second-order point worth putting in the piece:** the compliance mapping in the capstone. Locally, personal-data obligations and sector-specific regulation shape what a design is allowed to do, and a reader who works in this region will immediately recognise a candidate who can speak to that. **Say what the obligation is, who it is owed to, and how it constrained the design** — same three-part structure as the Unit 5 PIPL work, and it is the structure that keeps earning points.

## CLOSE (2 min)

Commit the draft, even if it is rough. **A committed rough draft on May 14 is worth more than a perfect draft in your head on May 26.**

**Next: Mon May 17, P129 — Talking about your own work: the 3-minute technical talk.** You will present on May 28, and the gap between a written piece and a spoken one is the whole lesson. **Wed May 18: ethics and law, PIPL versus the US.** **Thu May 19: Session 8 debrief, OWASP Juice Shop.** Then thesis week, then build day 2 on May 26.

## TURN IN —

1. **Capstone portfolio piece, working draft, 700–1,000 words, all six sections, committed to the repo.** Sections 3, 4, and 5 must be substantially complete. A draft missing section 5 is the most common way to fail this and I will send it back.
2. **Commit history showing at least three commits** with meaningful messages. This is evidence of iteration and it is worth points.
3. **One paragraph, in the file, listing the honest limits of the piece itself** — what you simplified, what you cut and why, and what you would need to do to make this production-quality. **Meta-honesty about your own document is a portfolio skill**, and it costs you five minutes.
