# U5 L02: FRQ / Performance Task Practice, Timed (Apr 20, Tue — P112)

**Date:** Tue Apr 20, 2027
**Unit:** 5 — Securing Applications and Data (AP Exam Review stretch)
**Period:** P112
**Gradebook category:** Unit Tests
**LOs:** 2.D (mitigate, in a written design) · 3.D (detect, from an artifact) · 4.A–4.C (collaborate and communicate a technical position)

**Materials:** Printed performance-task packet (distributed in advance), pencils, timers visible to the whole room, your own remediation card from L01, the rubric projection

**PAPER DAY. Closed notes, timed, silent.** Today is the last comfortable opportunity to practice a long response before the exam. Wednesday's targeted review and the final sweep both assume you already know how to write under a clock.

---

## PART 1 — HOW THE FREE-RESPONSE IS ACTUALLY SCORED (5 min)

Project this and read it aloud. It is the same logic every year, and almost nobody internalizes it.

**The rubric is a checklist of observable things.** Not "understands risk assessment" — that is not gradeable. It is closer to:

- *Identifies the injection type from the given artifact (1 pt)*
- *Names a specific control, not a category (1 pt)*
- *Ties the control to the specific vulnerability it addresses (1 pt)*

Three consequences, and they are the whole lesson:

1. **Every sub-part is scored independently.** You can lose part (a) and keep part (b). Never abandon a part because you fumbled the one before it.
2. **Specificity is what separates points.** "Improve security" is zero. "Use parameterized queries / prepared statements instead of string concatenation" is the point. The rubric rewards the noun.
3. **A wrong answer in the right category still earns.** If part (c) asks for a mitigation and you write a real, correctly-categorized mitigation, you get the point even if part (a) was wrong. Do not let a cascade failure eat the rest of the response.

Put on the board: **address every sub-part, name a specific control, connect it to the artifact.**

## PART 2 — TIMED PERFORMANCE TASK (30 min)

**Conditions, stated exactly:**
- 30 minutes on the clock, timed by me, not by a phone.
- No notes, no study guides, no remediation card visible. Put it face-down in your bag.
- One packet, distributed now. **Do not open it until I say go.**
- Write in the packet. Do not draft on loose paper.
- I will call 20 / 10 / 5 / 1 remaining. Those are real. When I call 1, you should be writing your last line, not starting one.

**Before you start, read the packet's front page.** The performance tasks in this course always carry a scenario paragraph, then several numbered parts. Read the scenario, then read all the parts, then start writing — that ordering alone is worth points, because part (a) usually tells you what part (b) is about.

**While you write, I am watching for three things and will say nothing until time:**
- Do you answer the part you are on, or the part you are comfortable with?
- Do you write a control, or a category of control?
- Do you leave anything blank?

**After:** collect the packets at the buzzer. No second pass. That is the point.

## PART 3 — SELF-SCORE AGAINST THE RUBRIC (8 min)

Get your packet back. Grade it yourself against the printed rubric, point by point. **Be honest — this is the only diagnostic you get before the exam.**

Then, for every point you did not earn, write one line:

> I lost this point because ________.

Not "I didn't know the content." Specific: "I wrote 'use encryption' when the rubric wanted the named mode and the key-management answer." "I left (c) blank because I ran out of time and (c) was the easiest one." "I answered the risk-treatment question with a detection control."

Then compute the number that matters: **points lost per sub-part.** If you lost points evenly, you have a coverage problem and the sweeps will fix it. If you lost them all in the last two parts, you have a *pacing* problem, and that is fixed by a habit, not by more review. Say which one you have out loud to your seat partner.

## 🇹🇼 TAIWAN CONTEXT

**3-minute brief.** Pull a real Taiwan incident narrative you have already used this year — the e-commerce platform breach we analyzed in Unit 5, or a TWNCERT advisory.

**The question, and it is the exam question:** *if this happened to a Taiwanese e-commerce platform, what would the notification timeline have been?*

Nobody needs to memorise a statute to answer a performance task. What you need is the shape:

- Taiwanese personal-data law (**PIPL**, the Personal Data Protection Act, in force since 2015 and amended since) puts obligations on the **data controller** when personal data is compromised: notify the competent authority, notify affected individuals where there is a risk to their rights, and record the incident.
- A US framing under state breach-notification law and HIPAA-style rules is different in structure — different trigger, different clock, different audience.

**Point to make:** on an exam, a compliance sub-part usually wants *who must be told, in what order, and why*. Say it in those terms. The statute name is the noun; the reasoning is the point.

**Ask (1 min):** name one step in that timeline that a technical control would have made unnecessary.

## CLOSE (2 min)

Tomorrow is the first targeted day — built around weak topic 1, which is on the re-teach board from Monday. Bring the line you wrote about what you lost and why.

**Next:** Thu Apr 22, P113 — Targeted review, weak topic 1, part 1. Bring every Unit note for that topic and your Unit 1–5 study guides. This is a content day, not a writing day.

## TURN IN —

1. **Timed performance task packet (30 min, in-packet responses).** Graded with the rubric; the score is recorded as a **practice score**, not a test grade.
2. **Points-lost ledger.** One line per unearned point: *point lost because ___*. Plus your read of whether your loss pattern is coverage or pacing. This is the artifact I use to build the FRQ round 2 on Tuesday.
