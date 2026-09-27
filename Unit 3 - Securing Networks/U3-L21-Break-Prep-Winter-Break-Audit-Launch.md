# U3 L21: Break Prep — Winter Break Device Audit Launch (Dec 18, Fri — PAPER DAY, HALF DAY)

**Dismissal is 12:30.** We start and end on schedule. This is a working half day, not a free period.

**Learning Objectives:**
- 4.1.A Identify the attack surface of a device the student actually owns and name one vulnerability class per device
- 4.1.D Distinguish the malware types that target a personally owned device and state the control that blocks each
- 4.2.A Evaluate the authentication posture of a personal account and explain what an attacker gains by defeating it
- 4.3.A Identify one hardening or patching gap on a personally owned device and the residual risk after the fix

**Materials:** Printed device audit packet ([GDoc](https://docs.google.com/document/d/1o6FlZDoGBoWmAas4Iviac3bH99ny-OJR6HjO0eu7E8s/edit) — copy only, attach view-only in Classroom, never export a PDF), completed sample audit (2 pages, teacher's own phone and laptop), the four Unit 4 malware cards printed as a reference bank, Unit 4 study guide (start it over break), timer

**No computers for the break work.** This assignment is paper only — the printed packet, a pen, and your own devices, but not for the write-up. No GitHub, no submissions, no tech during Winter Break. If you want to note your phone's OS version or check a settings screen, that is fine, but the audit is by hand.

---

## Activities

1. **Attendance and check-in (3 min):** Confirm who is present on the half day and who will be here Monday. Note absences against the return-day tracker — students missing the launch are missing the due-date explanation, so give them the packet before they go.

2. **Hook (5 min):** "Someone gets into your phone. Not by guessing the passcode — by getting you to install an app, or by abusing a setting you forgot was on." Take two or three answers, then push: **"What did you give away, and which one of your accounts would that reach first?"** A stolen phone is a Unit 4 problem, not a Unit 3 problem, and the whole unit is in that exchange.

3. **Direct instruction — the device audit, requirement by requirement (14 min):** Walk the checklist line by line on the board. Do not hand out the packet until the last item. For each requirement, state the attack surface it targets and one control that would close it.

   - **Device inventory (4.1.A)** — every device the student owns that touches a network: phone, laptop, tablet, watch, TV, printer, router, a family member's device on the same home network. For each, the OS, the model, and the last time it was updated. The inventory is the whole document; the analysis hangs off it.
   - **Attack surface, per device (4.1.A, 4.1.B)** — what is actually exposed. A phone is an encrypted, patched, sandboxed device with a huge amount of data on it — and that data is the surface. A router is a small computer on the internet with an admin panel nobody has visited since 2019. Make them say the surface out loud, not just name the device.
   - **Malware targeting (4.1.D)** — virus, worm, trojan, ransomware, spyware, adware. For each device, which one is actually plausible, and which would be blocked by the control already in place. Most personal devices have app-store review and platform signing; say so, and then say why that is not sufficient against a trojan.
   - **Authentication (4.2.A, 4.2.B)** — for the three accounts that matter most, the password, whether it is reused, whether it lives in the device password manager or in a document or a notebook. Then MFA: which accounts have it, which do not, and which do not and could. Reuse is the finding that recurs — push on what a single breached site hands the attacker.
   - **Hardening, patching, encryption (4.3)** — automatic updates on or off, screen lock timeout, encryption at rest, remote wipe enabled, a device lost in a taxi versus a device stolen from a house. Ask which of those two is the one the settings actually change.
   - **Risk line (2.1.E, revisited)** — every finding gets a likelihood and an impact. "Old router" is an observation; "old router, 2019 firmware, admin panel reachable from tenant Wi-Fi, likelihood medium, impact high, residual after patching is low" is an assessment.
   - **Treatment line (2.1.F)** — every finding also gets a treatment: avoid, transfer, mitigate, or accept, with one sentence of reasoning. Accepting a risk is a legitimate answer; accepting it *without writing the sentence* is not. Replacing a five-year-old router is often the correct treatment and it costs money — that is a real finding, and saying so out loud is part of the exercise.
   - **Taiwan addendum A — shared building network (2.4.B, carried forward):** in a Taiwanese apartment building the home network boundary is the building, not the apartment. Each student records **one risk from shared building network infrastructure** and the evidence that would reveal it. Accepted answers include: a single unmanaged building switch, one flat VLAN with no segmentation between tenants, a management interface reachable from tenant Wi-Fi, shared Wi-Fi with a default or published key, or an unmonitored building-level firewall handing off to the street. Note the overlap: the router in this inventory is often not the student's to patch.
   - **Taiwan addendum B — devices and typhoon season (2.3.C, carried forward):** each student records **one device-resilience gap** relevant to typhoon and flood season, and what it would break. Accepted answers include: a phone or laptop left charging in a ground-floor unit, a router or NAS shelf below floor level, no surge protection on the network gear, a UPS that protects the computer but not the router, a device that is enrolled in remote wipe but not in a backup, or an outdoor access point or camera that goes dark in a brownout.

4. **Sample audit walkthrough (10 min):** Distribute the packet. Then project the two-page completed sample — the teacher's own phone and laptop, with a router past end of support, one account on a reused password with no MFA, one that is the only thing standing between a thief and every photo on the device, and a laptop on a UPS that protects the machine but leaves it cut off from the internet. Read it aloud, front to back, and narrate the reasoning in the margin: why this is 4.1.A and not 4.1.D, why the likelihood on the router is medium and not high, why the treatment on the MFA gap is mitigate rather than avoid.

   Make the standard explicit before students leave: **describe, assess, treat, evidence.** Four lines minimum per finding. A finding with no evidence line is an opinion, and opinions do not earn credit.

5. **Due date, format, and the break itself (5 min):**
   - **Due:** the first class back — **Monday, Jan 4.** It comes back as a graded HW quiz at the start of the day, so bring it physically, not a photo.
   - **Length:** 2–4 pages, hand-written. One page minimum per addendum.
   - **Bring:** the packet, plus a two-sentence answer to each of the two Taiwan addenda.
   - **The graded thing is the reasoning, not the device.** A student who finds a serious flaw on a cheap phone and treats it well outscores a student who finds nothing on new hardware.

   Then the break logistics, and be specific because it is long: **Winter Break runs Friday Dec 18 (dismiss 12:30) through Sunday Jan 3. That is sixteen days** — twice as long as Fall Break. Classes resume **Monday, Jan 4.** Midterms are Jan 18–21, no class, and **Term 3 begins Jan 22** with Unit 4 continuing straight through 4.2 authentication and 4.3 hardening. The Dec 15–17 Unit 4 lessons, including the Stuxnet case study, are what the break sits in the middle of — do not let them fade.

6. **Open Q&A (5 min):** Remaining time on questions. Take questions about the checklist, about what counts as acceptable evidence, and about the two addenda — the addenda are the part students most often get wrong.

**Homework (due Mon Jan 4, brought to class — graded HW quiz that day):** Complete the Winter Break device audit, 2–4 pages, by hand. Both Taiwan addenda included. Nothing else — no devices, no computers, no tech for this course over the break. A quiet re-read of 4.1–4.2 is fine and encouraged; the grader is the audit.

**Differentiation / ELL support:** The packet is fillable as a table, so a student can record findings as structured rows instead of prose. A one-page bank of likelihood/impact phrasings and a treatment-selection table are provided for students who find the risk vocabulary harder than the observation work. A printed reference card of the six malware types with the control that blocks each removes the recall burden so the time goes to analysis. Students with no personal devices of their own — or who share one family phone — may audit a shared or household device plus a building common-area network, and may write the authentication section for a parent or sibling's account with that person's permission. For the two addenda, give a worked example of each so the required specificity is clear.
