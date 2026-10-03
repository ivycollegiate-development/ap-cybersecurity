# U2 L8: Physical Attack Case Studies (Oct 9, Fri — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on physical attack methods (tailgating, piggybacking, shoulder surfing, cloning), plus 1 on detection points.

**Learning Objectives:**
- 2.2.A Identify the physical attack method used in a real incident
- 2.2.C Identify the vulnerability the attacker exploited and why the existing control did not stop it
- 2.3.A Recommend the specific control that would have prevented or limited the incident

**Materials:** Slides, four case briefs (see Links below), case analysis worksheet ([GDoc](https://docs.google.com/document/d/1IvJePzgR30GGa2j8JkJy6509BQjy9wbZ868UJAs3qUs/edit)), projector

---

## Activities

1. **Framing (3 min):** Four incidents, four different organizations, four different decades. You are not being asked to summarize them. You are answering the same three questions about each one, and those three questions are the format of a scored AP Cybersecurity FRQ question. Announce that now so the groups write accordingly.

2. **Jigsaw (22 min):** Groups of 3–4, one case per group. The four:
   - **RSA SecurID, 2011** — an outsourced contractor's credentials, an APT campaign, and the eventual replacement of every deployed token. The physical story is a contractor with legitimate access and no verification of what that access was for.
   - **Snowden, 2013** — a trusted insider with legitimate badge access, credential abuse, and mass exfiltration. The access was real at every step. Nothing triggered an alarm.
   - **Stuxnet** — a worm that arrived on a USB drive inside a contractor's laptop, crossed an air gap by being carried, and targeted industrial control software. The physical vector was four USB sticks and one maintenance contract.
   - **Taichung fab incident** — a realistic composite drawn from Taiwan's own reporting on fab water, power, and typhoon response, plus a trade-press account of a contractor entering a process area without a proper escort. Use the brief in the repo, not outside sources.

   Each group answers, in writing, on the worksheet:
   - **Attack method** — name the physical vector specifically. Not "social engineering" but "unverified contractor admitted by badge escort at a side door." Be exact; vagueness costs points.
   - **Vulnerability exploited** — the weakness in the *system*, not in the person. Snowden was not careless; the system assumed a cleared insider behaved. RSA's contractor access was administered but not scoped. Stuxnet exploited a control that was designed for data, on a network that was designed to be isolated, physically.
   - **Control that would have stopped it** — specific, and ideally one that does not rely on the attacker being smarter or the insider being good. A control that depends on perfect human behavior is a weak answer, and you should say so if you propose one.

   Groups should also note: was there a *detection* control in place at all, and what would have caught it?

3. **Share-outs (15 min):** **2 minutes per group, strictly timed.** Method, vulnerability, control — in that order, no narration of the story. The class listens for the next two groups and must be able to name a control from group 1 that contradicts or covers group 2. This is a listening task, not a wait task.

4. **Debrief (5 min):** Which controls recur across the four cases? The answer students should arrive at, and the one that is worth pressing if they do not:
   - **Scoped access and least privilege** — access held, but narrowed to what the role actually needs, and time-bounded. RSA and Snowden both turn on access that was too broad or too casually granted.
   - **Independent verification of identity and authority** — a badge proves who you are, not why you are here. Stuxnet crossed an air gap because a device was carried in by someone with a legitimate reason to carry it in.
   - **Monitoring of access, not just authentication** — each of these involved valid credentials used validly. Detection controls that watch for *pattern* (unusual volume, unusual hours, unusual destinations) are what would have caught any of them.
   - **The physical layer is upstream of all of it.** No amount of network segmentation, in Stuxnet's case, mattered — the attacker started inside the boundary by being carried in.

   Close on this: every one of these four organizations had a security program. In each case the control that failed was one nobody had written down as a requirement.

## Case briefs

| Case | Brief |
| ---- | ----- |
| RSA SecurID, 2011 | https://docs.google.com/document/d/1-n-z1wJ7CTkXTZzhPsPdkTBqpO6OkZcnOA45lW9Q1t8/edit |
| Snowden, 2013 | https://docs.google.com/document/d/1g54vPIR7OSqb0CdECxUzqMjZwwk8RyA05uLhJ6KSZ50/edit |
| Stuxnet | https://docs.google.com/document/d/1Mh-tCBWW6JjHmPCZSAKkyzZxAw8jOGqXuvTTknvx6tQ/edit |
| Taichung water utility | https://docs.google.com/document/d/1-uQYEU9FZI32nvqE5z5ubYq_SAB9R0TMM4X0ss0oDs0/edit |

**Homework (due Mon 20:30 — Tuesday quiz):** Write a 150-word response: pick one of the four cases and describe the single most cost-effective control you would have added, with a cost estimate. Quiz is on the three FRQ questions — method, vulnerability, control.

**Differentiation / ELL support:** Each case brief is a one-page summary at roughly a 9th-grade reading level, with the key facts bolded and the timeline given as a bulleted list rather than prose — the chronology is the hardest part of Stuxnet and the briefs pre-extract it. The worksheet is a three-row table matching the three FRQ questions, so structure carries the organization and students fill in reasoning. Groups may split the four cases into pairs within the group if that helps, but the share-out is still one voice per case. A vocabulary card for the terms in the briefs (air gap, APT, exfiltration, OT/ICS, insider) is on the back table. Students who finish early should draft the Monday homework during class.
