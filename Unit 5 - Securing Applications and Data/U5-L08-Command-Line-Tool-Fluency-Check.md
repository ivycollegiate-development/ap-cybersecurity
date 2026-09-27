# U5 L08: Command-Line and Tool Fluency Check (Apr 29, Thu — P118)

**Date:** Thu Apr 29, 2027
**Unit:** 5 — Securing Applications and Data (AP Exam Review stretch)
**Period:** P118
**Gradebook category:** Unit Tests
**LOs:** 3.D (interpret tool output correctly) · 2.D (apply a control in the tool) — *the hands-on material*

**Materials:** Laptops or the Mac Mini Codespaces terminal, the check packet, the Octal Conversion Card (reference, permitted), the pre-printed command sheet

**TECH DAY. This is a skill check, not a review lecture.**

> **The premise, and it is the reason this day exists:** you can score well on multiple-choice and still lose points on any item that requires you to *use* a tool — read a permission string, interpret a config, convert an octal mode, trace a log line, check a hash. Those items reward fluency, and fluency is not fixed by reading about it. Today you practise the hand.

**Honesty rule, non-negotiable, and it applies to this file as much as to your work:** every value in this packet is one you compute yourself, in front of me. If a result is not what you expected, that is a finding — write what actually happened, not what the sheet suggested. Inventing an output loses the point and teaches you nothing.

---

## PART 1 — READ THE ARTIFACT, NAME THE TOOL (8 min)

Five artifacts on screen. For each, in writing, in 60 seconds:

1. What tool produced this, and what is the artifact called?
2. What question is this tool's output normally used to answer?
3. What is the *first* field or line you would look at, and why that one?

**Examples of the artifact families you have met this year, all of which can appear:** a filesystem permission listing; a hash computed from a file; a network capture opened in a packet analyser; a web server access log; a certificate chain; a firewall rule set; an encrypted file and its ciphertext; a signature verification result.

**The transferable skill, and it is the whole lesson:** every tool in security answers one narrow question. Someone fluent with tools is not someone who knows many tools; it is someone who knows, for each tool, **what question it answers and what it cannot tell you.** `ls -l` tells you the permission bits. It does not tell you who is behind the connection. Knowing the boundary is what stops you over-reading an artifact.

## PART 2 — FLUENCY DRILLS, TIMED (24 min)

Six stations, four minutes each. Same workstation, move when the timer goes. **Answers are written, not typed into a form — a wrong value you computed is recoverable; a value you guessed is not.**

**Station 1 — Permission strings to octal.**
Given a symbolic listing such as `-rwxr-x---`, produce the octal mode. Then the reverse: given an octal mode, produce the symbolic form. You have done this in Unit 5's `chmod` lab; this is the exam version, cold.
- The reference card is available. **First do it without it, then check.** A correct answer you found by looking is not the same as a correct answer you produced.
- The subtraction that matters: each of the three triples contributes 4 for read, 2 for write, 1 for execute. Make yourself say that out loud, not just remember it.

**Station 2 — Hash a file and say what it proves.**
Compute the SHA-256 of the file provided. Then answer, in writing:
- What does this value prove about the file *as it exists right now*?
- What does it **not** prove? (Two things at minimum: it says nothing about *who* produced the file, and nothing about whether the *content* is benign — an attacker can hash a malicious file perfectly.)
- What would you need in addition to conclude "this file is trustworthy"?

**The lesson:** a hash is an integrity check against change, not a verdict about trustworthiness. Saying the second thing is the scored part.

**Station 3 — Read a log and find the timeline.**
Given a server access log excerpt:
- Sort the events into reconnaissance / exploitation / post-exploitation where the evidence supports it.
- Cite the **specific field** that supports each classification. If you cannot cite a field, you are guessing, and you should mark it as unknown rather than assert it.
- State the earliest timestamp you can *evidence*, and say what the evidence is.

**The lesson:** a timeline claim without a cited field is an opinion. This is the habit from Wednesday, now on live data.

**Station 4 — Inspect a certificate chain.**
Given a certificate and its issuer:
- Name the fields you would read first and what each one tells you.
- State what the chain of trust is doing and what breaks it.
- Say what an expired certificate and an untrusted issuer each mean, and how they differ.

**The lesson:** read the *dates* and the *issuer*, in that order. Almost every certificate question is a dates-and-issuer question.

**Station 5 — Encrypt, then verify, then break it.**
Using OpenSSL, on the provided file: encrypt it, decrypt it, and confirm the round trip. Then modify the ciphertext by a single character and attempt decryption again.
- Record **what actually happened**, character by character, and what the tool reported.
- The teaching point: authenticated modes (such as GCM) are *designed* to fail loudly on tampering, and the point of the lab is to see the failure rather than be told about it.
- Then answer: what does successful decryption of a tampered ciphertext under an unauthenticated mode tell you about whether the plaintext is trustworthy?

**Do not predict the output before you run it. Run it, then write what happened.** If your ciphertext decrypted to readable garbage, that *is* the result and it is the most instructive one on this page.

**Station 6 — Read a config for a security defect.**
Given a configuration excerpt:
- Name the artifact and the technology.
- List every setting you would question, and for each, say **what risk the setting creates** and **what a safer value would be.**
- Then, separately, mark which of your questions you can verify from the file alone and which need information the file does not contain.

**The lesson, and it is the one senior candidates most often miss:** confidently stating a defect you cannot support from the artifact is the fastest way to lose a point. "I would want to check whether…" is a better sentence than an assertion you cannot back.

## PART 3 — HONEST ERROR LEDGER (8 min)

For every station where your first answer was wrong, write one line:

> *I wrote ______ because ______. The correct procedure is ______.*

**This is the most valuable artifact you will produce this week** and it feeds directly into Monday's and Tuesday's sweeps. Be specific about the *reason*, because the reason is the transferable part: a wrong octal conversion is arithmetic, a wrong octal conversion because you read `-` as "no permission" when it means "regular file" is a misread, and only one of those two will show up again under a different question.

**I will look at this ledger, not the scores.** A bad day on the stations with an honest ledger is a good day. A good day on the stations with an empty ledger is not.

## 🇹🇼 TAIWAN CONTEXT

**3-minute brief, tool-shaped.** Take the certificate artifact from Station 4 and read it as a real one: a Taiwanese online service presenting a certificate to your browser.

**Questions (2 min, out loud, no writing):**
- What does a valid certificate *not* tell you about the site behind it?
- If the site is a financial service, whose problem is the certificate, and whose is the browser's?
- Does any of that change if the site is a hospital or a government service? Why would the answer to the last question be yes?

**The point that transfers to the exam:** a valid HTTPS connection is evidence of *encryption and identity as asserted by that certificate*. It is not evidence that the site is legitimate, safe, or that the organisation behind it is who it claims. Scenario questions about "a site is using HTTPS, so it is secure" are testing exactly this. Do not let a green padlock decide an item for you.

## CLOSE (5 min)

**Next:** Fri Apr 30, P119 — **Full topic sweep, part 1.** This is the first of the two broad sweeps across every unit, built from your error ledger. Bring the ledger.

## TURN IN —

1. **Six station worksheets**, with real terminal output pasted or transcribed **exactly as the tool produced it.** If a value could not be produced, write why — "command unavailable in this environment" is a correct and acceptable answer; a plausible-looking invented value is not.
2. **Honest error ledger**, one line per wrong first answer, with the *reason* named and the correct procedure stated.
3. **One-sentence answer to each Station 2 sub-question** and the Station 5 "what does successful decryption of tampered ciphertext mean" question. These two are the conceptual core and I grade them as writing, not as tool use.
