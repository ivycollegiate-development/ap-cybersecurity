# U5 L10: Full Topic Sweep, Part 2 — Units 4–5 (May 3, Mon — P120)

**Date:** Mon May 3, 2027
**Unit:** 5 — Securing Applications and Data (AP Exam Review stretch)
**Period:** P120
**Gradebook category:** Unit Tests
**LOs:** all four skills, Units 4–5 · 1.A–1.D, 2.A–2.D, 3.A–3.D, 4.A–4.D

**Materials:** Friday's sweep sheet and triage, all Unit 4–5 study guides, today's sweep question set, pencils, timer

**The last content day before the exam.** Same rules as Friday, same discipline, and today it covers the two units closest to the practice-exam material, so the hits should be sharper.

**Tomorrow is the final review and exam logistics. Wednesday is the exam.** Today is the last day anything new can be learned — which means today is the day for *recalibration*, not for new content.

---

## PART 1 — UNIT 4 SWEEP (14 min)

**Unit 4 — Securing Devices.** What counts as a device and where the attack surface is; device vulnerability classes; malware taxonomy (virus, worm, trojan, ransomware, spyware, adware) and the control that stops each; authentication factors and where MFA genuinely helps versus where it is bypassed; certificate-based and token authentication; hardening, patching, and encryption at rest; endpoint detection and response; host IDS.

**Watch for, and I will ask cold:**
- **Malware taxonomy.** Virus needs a host, worm self-propagates, trojan masquerades, ransomware encrypts for payment, spyware observes silently. If you mix up worm and virus you lose points on every item in that family, and it is pure recall — free points, freely lost.
- **Authentication.** Factor vs authentication vs authorisation vs accounting. If an item says "this proves *who* they are," it is authentication; "what they may do" is authorisation. Read the verb.
- **MFA's honest limit.** MFA defeats credential theft and replay well; it does not defeat malware on the device, and it does not defeat a session that has already been established. An item offering "enable MFA" as the fix for a malware problem is a distractor, and it is a popular one.
- **Hardening versus patching.** Hardening reduces the surface; patching closes known holes. A device fully patched but running unnecessary services is still exposed, and an item saying "install updates" as the answer to an unnecessary-service finding is wrong.
- **Encryption at rest** versus in transit versus in use. The Cold Card case in Unit 5 is the anchor for the third: a key generated badly is broken at the source, and no later control recovers it.

## PART 2 — UNIT 5 SWEEP (14 min)

**Unit 5 — Securing Applications and Data.** Application vulnerability classes — SQL injection, XSS, CSRF, buffer overflow, path traversal, insecure deserialization; access control models (DAC, MAC, RBAC, RuBAC/ABAC) and least privilege; symmetric and asymmetric cryptography and when each is used; hashing and salting; PKI, the chain of trust, and digital signatures; secure SDLC and code review; SAST versus DAST; WAF versus RASP; data classification and DLP; audit logging and detection of attacks on data.

**Watch for — this is the unit with the most distractor traps in the course:**
- **Vulnerability class identification from an artifact.** The item gives you a snippet or a log line and asks you to name the class. Name the class *first*, then justify from the artifact. If you justify before naming, you drift.
- **The same class of input, different names.** A stored XSS and a reflected XSS differ in *where the payload is stored*, not in what the payload does. Same for in-band versus blind injection: the difference is whether results come back in the response, not whether the query is malicious.
- **Cryptography selection.** Symmetric for bulk data with a shared secret; asymmetric for key exchange, signatures, and cases where the two parties do not already share a secret; hashing for integrity and verification with no secret. If an item mixes two of these, say which one the requirement actually implies.
- **Digital signature properties.** A signature provides authenticity and integrity. It does **not** provide confidentiality — signing a document does not hide it. That distinction is worth a point every time it appears.
- **WAF versus RASP.** Network-side inspection versus in-application, context-aware, runtime enforcement. If an item asks for something a signature-based WAF structurally cannot see — because it is inside an encrypted session, or because it requires application semantics — the answer is not a better WAF rule.
- **Access control models.** Say the word that defines each: DAC the *owner* decides; MAC the *system* decides via labels; RBAC permissions attach to *roles*; RuBAC/ABAC decisions depend on *rules and context*. The defining word is the discriminator, and distractors are built by swapping the defining word.
- **Least privilege.** An item offering an answer that grants more access than the task requires is wrong even if it is a real control. Least privilege is a *minimality* requirement, and that is what the item is testing.

## PART 3 — COLD TRIAGE, BOTH SWEEPS (10 min)

Lay Friday's triage beside today's. Fill in the combined picture:

| | Blanks | Guesses | Sure & right |
|---|---|---|---|
| **Unit 1** | | | |
| **Unit 2** | | | |
| **Unit 3** | | | |
| **Unit 4** | | | |
| **Unit 5** | | | |

Then the two questions that decide tomorrow:

1. **What is my single worst cell?** Not my worst unit — my worst *cell*. One topic, one specific gap. Tomorrow's final review is built around it.
2. **What is my best cell?** Name it. The point of this is that a student who knows what they are secure in does not waste tomorrow re-reading it, and instead protects the points they already own.

**Say the honest version out loud to your seat partner:** are you a student who loses points on recall, on reasoning, on artifact reading, or on writing? They have different last-day fixes. Recall is fixed by tonight. Reasoning is not fixable in one night. Artifact reading and writing are fixable by habit, starting tomorrow morning.

## 🇹🇼 TAIWAN CONTEXT

**3-minute brief, the capstone of the block.** We have asked a Taiwan question every day for eleven days. The final one is the one worth remembering.

**Take a real incident affecting a Taiwanese organisation — semiconductor, e-commerce, healthcare, or government — and answer the capstone question, in writing, in four lines:**

1. **Which unit topic owned the failure?** (The control that was missing or misconfigured.)
2. **Which unit topic would have detected it, and how much sooner?** Name the detection source — log, sensor, monitor, endpoint.
3. **What legal or regulatory obligation was triggered, and owed to whom?** (For personal data in Taiwan, PIPL obligations sit on the data controller, and route to the competent authority and to affected individuals. For other sectors and other jurisdictions the framework differs — name the one that actually applies rather than the one you remember best.)
4. **What is the single cheapest change that would have reduced the impact?**

**Why this is the right note to end on:** the four lines are the shape of a good answer to almost any scenario item on this exam. Own the failure, own the detection, own the obligation, own the cheapest control. Write them in the CED's vocabulary, not in the vocabulary of the news story.

## CLOSE (4 min)

Collect the sweeps and the combined triage. Set out tomorrow's two behaviour cards and your worst-cell note on your desk tonight.

**Next:** Tue May 4, P121 — **Final review and exam logistics.** The last period before the exam. Nothing new; the last day is for confidence, logistics, and the two or three things you personally have to carry into the room on Wednesday.

## TURN IN —

1. **Unit 4 and Unit 5 sweep sheets**, with the `sure` / `guess` / `blank` mark on every answer.
2. **Combined five-unit triage table**, plus your single worst cell and your single best cell, named.
3. **The four-line Taiwan capstone answer.** Written, not discussed. This is the last substantial piece of writing before the exam and it is worth doing properly — the four-line structure is exactly the free-response structure.
