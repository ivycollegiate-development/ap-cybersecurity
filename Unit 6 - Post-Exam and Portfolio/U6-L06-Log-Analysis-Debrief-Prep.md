# U6 L06: CTF Session 7 Debrief Prep — Log Analysis Sprint (May 13, Thu — P127)

**Date:** Thu May 13, 2027
**Unit:** 6 — Post-Exam and Portfolio
**Period:** P127
**Gradebook category:** Participation
**LOs:** 3.A–3.D (Detect Attacks) · 4.B (document findings for a non-specialist)

**Materials:** Your Saturday session notes (Session 6, May 8 — network forensics), the log analysis method card, the writeup template, a clean sheet

**📄 PAPER DAY. This is a preparation day, and the distinction matters.**

**Saturday May 15 is CTF Session 7 — the log analysis sprint.** The session runs; nothing about it changes. But the writeup — the artifact that goes in your portfolio and that you will talk about on May 28 — is produced **after** the session, and it is produced better if you know now what a strong writeup of a log analysis actually contains.

**So today is not the debrief. Today is the template.** On Monday May 19 you will write the real one, with real findings from a session that has not happened yet.

---

## PART 1 — WHY LOG ANALYSIS IS THE MOST EMPLOYABLE THING YOU DO (10 min)

Say this without hedging, because it is true and it is the through-line of your portfolio.

**Most of security is judgement about evidence.** Logs are the rawest evidence there is: an append-only record of what actually happened, written by a machine that did not know it was being watched. The skill of turning that into a defensible narrative — *here is the attack, here is the timeline, here is the evidence for each step* — is **the** core analyst skill. SOC tier one does it daily. An IR analyst does it during an incident. A pentester does it to prove what they found. A GRC person does it to prove a control worked or did not.

**And it is the hardest thing to fake.** Anyone can claim they understand access controls. To claim you have traced an attack through a log, a reader can look and see whether your timeline holds together.

**The portfolio implication, and this is the point of the session series:** a log analysis writeup with a *defensible timeline* is worth more in an interview than any certificate. It is evidence of the exact thing the Credential Ladder says employers screen for — thinking, shown.

## PART 2 — THE METHOD, REBUILT FROM SCRATCH (16 min)

Log analysis is not a bag of tricks. It is a procedure, and the procedure is what goes in the writeup. Rebuild it cold, from memory, and write it down — **this is the template you will fill on Monday.**

**Step 1 — Establish the baseline before you look for anything.**
What does normal look like in this environment? Volume, timing, source distribution, status-code mix, user-agent patterns, which accounts are usually active. **You cannot find a deviation before you know the norm, and skipping this step is the single most common way a log analysis goes wrong** — including in professional writeups. It is also the step that produces false positives if you skip it.

**Step 2 — Sort events into phases.**
Reconnaissance → exploitation → post-exploitation → (impact or exfiltration). Most log analysis has a *shape*: something appears, then something is attempted repeatedly, then something succeeds. **Your writeup's central claim is the shape, not any individual line.**

**Step 3 — Cite the specific field, every time.**
Not "there were lots of failed logins." *The 401 responses in the `status` field, from a single source, across a contiguous window in the timestamp field.* A finding without a field-level citation is an opinion. You learned this in the Apr 29 tool fluency check and it is the same rule.

**Step 4 — Build the timeline and make it survive scrutiny.**
Earliest evidence, then each subsequent step, each with its cited field. **Then ask: what would have to be true for this to be a false positive, and can I rule that out?** An authorised scan, a health check, a misconfigured client, a proxy — these are the standard benign explanations, and naming them is what separates an analyst from someone pattern-matching.

**Step 5 — State the confidence and the limits.**
What you can evidence, what you infer, and what you cannot determine from the logs at all. **The limits paragraph is the most credibility-building paragraph in the whole writeup** and it is the one everyone deletes.

**Step 6 — Recommend, specifically.**
What would have prevented it, what would have detected it earlier, and what would have improved the logging so the next analyst has more to work with. The third one is the one people forget and it is the one that shows you think about the *system*, not just the incident.

**Write all six steps on the card. Take it home. This is your Monday template.**

## PART 3 — THE WRITEUP SHAPE (12 min)

A portfolio-grade writeup of a log analysis sprint. **One to two pages. This is the actual structure, and the headings are the deliverable:**

1. **The question.** What you were asked to find. One or two sentences. *(Almost nobody writes this and it is what makes a reader able to follow everything after it.)*
2. **The data.** What the logs were, where they came from, the time window, the volume, and — critically — **what the logs could not tell you.** The baseline you established in step 1.
3. **The method.** The steps you took, in order, so a reader could reproduce your work. **Reproducibility is the whole ballgame** — a finding nobody can follow is a claim.
4. **The findings.** Each one: what, the exact field or line as evidence, and the confidence. Number them.
5. **The timeline.** The reconstructed sequence, with the benign explanations you considered and ruled out — or did not.
6. **The limits.** What the data cannot support.
7. **The recommendations.** Prevention, earlier detection, better logging.
8. **What I got wrong first.** The failed attempts, and what each one taught you. **The highest-value section in the document, and the one every writeup I have ever read skips.**

**Section 8 is not optional.** A portfolio where everything worked first time teaches a reader that the writer either got lucky or is not telling the truth. A portfolio that shows a wrong turn and the correction is the most credible artifact you can produce — and it is exactly what the Saturday session format already asks for.

**Also: length.** One to two pages. A ten-page log analysis is a worse portfolio artifact than a two-page one, because nobody reads past page three. **Cut the noise and keep the method.**

## PART 4 — PREPARE THE SPACECRAFT FOR SATURDAY (7 min)

Practical preparation, ten minutes, and it makes Saturday more productive:

- ☐ Re-read your own notes from Session 6 (May 8, network forensics) and list the *specific questions you could not answer then.* Those are the questions to bring to Saturday. **A debrief is worth more when it starts from a real unanswered question.**
- ☐ Note the two log-analysis skills you found hardest on Saturday. Those are the two you will write the strongest parts of the writeup about.
- ☐ Open your portfolio repo and create the folder for the Session 7 writeup now, with a stub README. Setting up the structure beforehand means Saturday's output goes straight in rather than waiting for you to organise it.

## 🇹🇼 TAIWAN CONTEXT

**3-minute brief, on real log sources.**

**Question:** *if you were analysing logs from a Taiwanese organisation, which sources would you want, and which would you expect to be missing?*

Think it through properly, because this is a real professional skill — knowing what you cannot see is most of analysis:

- **Network perimeter logs, web server logs, authentication logs, endpoint telemetry, DNS logs, firewall logs, VPN logs, and cloud control-plane logs** are the sources an analyst actually lives in. Each has a different blind spot — DNS logs see names but not content; authentication logs see success and failure but not intent; web logs see requests but not what happened behind them.
- **For a Taiwanese organisation specifically:** do they log in a central SIEM, or on the device? Are logs retained long enough to investigate an incident that happened weeks ago — retention is a real and common failure, and it is a finding. Are logs in local time or UTC, and is daylight-saving relevant where relevant? **Timestamp normalisation is a genuine trap and a real cause of missed incidents.**
- **The local regulatory dimension:** where personal data is involved, what does the organisation's obligations mean for retention, access to logs, and who may read them? Under Taiwan's data-protection framework, personal data in logs is still personal data.

**The portfolio line this produces, and it is a good one:** *"I know what the evidence will not show before I start looking."* That is a senior-sounding sentence and you will be able to say it truthfully, because you have written the limits paragraph by hand.

## CLOSE (2 min)

Hand in the six-step method card with the eight writeup headings. **This is the template. On Monday you fill it in.**

**Next: Fri May 14, P128 — portfolio build day 1, the capstone writeup.** The first of three build days and the one with a real deadline attached. Bring the method card and your career memo; both will inform the capstone writeup.

## TURN IN —

1. **The six-step log analysis method card**, written from memory in your own words, with a one-line example of the *specific-field citation* rule in each of the finding and timeline steps.
2. **The eight writeup headings**, with two or three sentences under each saying what goes in that section. Under "What I got wrong first," say specifically what you will record — because if you do not decide now, in the moment, you will forget.
3. **Session 6 open questions** — the things you could not answer on May 8, listed. These are the questions you bring to Saturday.
