# U5 L06: FRQ Round 2 — The Six Most Common Scoring Misses (Apr 27, Tue — P116)

**Date:** Tue Apr 27, 2027
**Unit:** 5 — Securing Applications and Data (AP Exam Review stretch)
**Period:** P116
**Gradebook category:** Unit Tests
**LOs:** 2.D · 3.D · 4.A–4.C (written technical communication under rubric scoring)

**Materials:** The six-miss reference sheet (distributed in advance), a fresh performance-task packet, pencils, timers, rubric projection, the named misconceptions you wrote on Monday

**📄 PAPER DAY. This is the last time we write a long response before the exam.** Friday's tool day and the sweeps are content and hands-on. After today, your exam writing is done in practice — so write well.

---

## PART 1 — THE SIX MISSES (14 min)

These are the failure patterns that cost the most points across both of our practice rounds, in both MC and free-response. Read each one, then apply it to the **named misconception you wrote on Monday.** The six are the same every year because the failures are structural, not topical.

**1. The category answer instead of the specific one.**
*"Use encryption"* scores zero. *"Use AES-256-GCM with a per-record IV, keys held in a KMS/HSM rather than in application config"* scores. The rubric names nouns. Write nouns.

**2. The right control in the wrong layer.**
Item asks for a *network* control, answer is a *host* control, and the rubric marks it wrong. Before answering, name the layer: network / host / application / data / physical / people. Ask what layer the item is asking about.

**3. The missed sub-part.**
A three-part item with a two-part answer loses a third of the available points. **Re-read the item's final line before you stop writing.** The last sub-part is the one students skip, and it is often the cheapest.

**4. The diagnosis without the remediation.**
Naming the vulnerability earns half. The rubric wants the fix in the same or next sentence. If you diagnose, remediate. Always.

**5. The prevention answer where detection was asked.**
(and the reverse) Preventive controls block; detective controls observe and alert; responsive controls act after. If the item says "how would you *detect*," a firewall answer is wrong even though the firewall is a real control.

**6. The absolute where the item wanted a comparison.**
*"Encryption is more secure than ACLs"* is meaningless. *"ACLs control *who* reaches a resource; encryption controls *what* is readable if the resource or its storage is obtained"* is a real answer with points in it. When the item gives you a scenario with two things in it, it wants the relationship between them, not a verdict.

**Also, the one that costs the most total points and appears nowhere on a list: the blank.** Leaving a sub-part empty is a guaranteed zero. An imperfect answer is frequently a partial point. Never leave a sub-part blank — if you are out of time, write the control name and the reason, badly, and stop.

## PART 2 — TIMED PERFORMANCE TASK, ROUND 2 (22 min)

**Same conditions as last week, deliberately.** 22 minutes. Notes closed. Commit before you can revise. Called at 15 / 10 / 5 / 1.

**One change:** this packet's artifact is harder to classify. You will not be handed the topic — you will be handed the situation and have to determine which topics apply. That is what the real thing is like, and classifying is a scored skill.

**While you write, watch for the six.** You will hit at least two of them. When you do, name it in the margin — a one-word tag like `SPECIFIC` or `LAYER`. The tags are how you learn which ones you personally still do.

## PART 3 — SELF-SCORE AND DIAGNOSE (6 min)

Grade yourself against the rubric. Then, instead of a vague note, **tag every unearned point with the number of the miss above** (1–6, or `blank`).

**Produce the histogram.** Which numbers are your personal pattern?

Say the diagnostic rule plainly: **the miss you commit most is the one to fix this weekend, and it is worth more than re-reading a topic you already know.** A student who tags all six of their losses as `3 — missed sub-part` has a five-minute fix that is worth more than three hours of cryptography review. A student tagged `1` and `2` needs to change *how they write*, not *what they know*.

Compare histograms with your neighbour. Two people with different histograms should swap their two worst tags and read the reference sheet entries for each other before Monday.

## 🇹🇼 TAIWAN CONTEXT

**3-minute brief.** One real Taiwan data incident, framed as an exam item.

**Write the response first, then we compare.** This is the exercise: *here is a scenario with a breach of personal data at a Taiwanese online retailer. It asks you to (a) name the likely vulnerability class, (b) name a control that would have prevented it, (c) name a control that would have detected it, and (d) name one legal notification obligation and who it is owed to.*

**What to notice in your own answer:**
- Did (b) and (c) come out as *different* controls? If they came out the same, you have miss 5.
- Was (b) specific enough? If it read "better security," you have miss 1.
- Is (d) a noun and an obligation, or a general statement about privacy law? If the latter, you have miss 1 again.

The Taiwan-specific part of (d) that the rubric cares about: under PIPL the obligations sit on the **data controller** — notifying the competent authority, and notifying affected individuals where their rights are at risk. A US-framed answer would instead route through state breach-notification statutes or, for health data, HIPAA-style rules. **Name the framework, then name the obligation.** That ordering is the point.

## CLOSE (3 min)

**Next:** Wed Apr 28, P117 — Targeted review, **second-weakest topic**. Bring your histogram and your two worst tags; we will re-teach against the misses you personally made, not the ones the class made.

## TURN IN —

1. **Timed performance task packet, round 2.** Practice score, not a test grade.
2. **Tagged rubric self-score with the miss histogram** (count of each of the six, plus `blank`). Your two worst tags named explicitly, and — one sentence — *the specific change you will make to your writing to fix that tag*. That sentence is the deliverable; the histogram is only how you found it.
