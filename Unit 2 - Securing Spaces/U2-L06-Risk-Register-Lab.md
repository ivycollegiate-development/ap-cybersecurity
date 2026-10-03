# U2 L6: Risk Register Lab (Oct 7, Wed — TECH DAY)

**⚡ HW Quiz (5 min):** 4 MCQ on risk treatment options, including two that test transfer vs. delegate.

**Learning Objectives:**
- 2.1.E Score a risk using likelihood and impact, and compute inherent and residual risk
- 2.1.F Propose a control for a scored risk and recompute residual risk
- 2.1.E Build a risk register that a third party could act on

**Materials:** Slides, risk register template ([GDoc](https://docs.google.com/document/d/10MbSe4Af18mXFv7EoqaxsAG9JM2q_i7p1dJtH8xXTYI/edit)), scenario brief (written on the register template, top section), projector for the gallery walk

---

## Activities

1. **Walk through the template (8 min):** Eight columns, and what each one is actually for.

   - **Asset** — the thing with value. Be specific: "Etch tool controller software on Line 3," not "computers." A vague asset produces a vague risk.
   - **Vulnerability** — the weakness that would be exploited. Not the threat. "Sends unencrypted data" is a vulnerability; "hacker" is not.
   - **Likelihood** — probability in a given year, as a 1–5 number with a written reason. The reason is the part that gets challenged in the gallery walk.
   - **Impact** — 1–5, in whatever units matter: NT$ lost, wafers scrapped, days of downtime, records exposed.
   - **Inherent Risk** — likelihood × impact, before any control. The arithmetic is not the hard part; choosing the numbers is.
   - **Proposed Control** — the specific control, with its cost and who installs it. "Better security" is not a control. "Install badge readers at both stairwell doors, NT$180,000, facilities team, 6 weeks" is.
   - **Residual Risk** — likelihood × impact *after* the control. A control that changes only one axis is the normal case; say which one and why.
   - **Owner** — a named person or role, not "IT." The register is a list of promises, and promises need names.

   Note the shape: a risk whose residual risk is identical to its inherent risk means either the control does nothing or the group did not do the arithmetic.

2. **Lab — build the register (25 min):** Groups of 3–4. Scenario: a Taiwanese semiconductor fab in Taichung, 3,000 employees, three process lines, an office building and a fab building sharing a perimeter fence.

   Build a register of **8 or more assets**. Spread them — do not let a group submit eight variations of the same server. A workable spread includes fab process equipment and its control software, recipe files, cleanroom suits and tracking, the employee badge system, the perimeter fence and gate, the shipping and receiving dock, the fab's OT/IT network segment, the EHS and chemical systems, the roof and flood exposure, the fab's IP and R&D drawings, the cafeteria and shuttle.

   For each: score it, propose one control, and compute residual risk. Every group will be asked to defend at least two of their scores.

   Use your homework justifications from yesterday where they apply — the treatment vocabulary is the same.

3. **Gallery walk and cross-review (7 min):** Registers posted in order. Each group reads **two** other registers and leaves written feedback on sticky notes addressing: (a) one score you think is wrong and why, (b) one control you think does not actually reduce that risk, (c) one asset missing that the group should have considered.

   The second question is where the real learning is. A control that does not touch the named vulnerability does not reduce the risk, and this is the most common error in the room.

4. **Close (5 min):** Two groups read out the asset the other groups missed most often. Cross-check against the template columns.

   **Rubric (20 points):**
   - Assets — 4 pts. 8+ assets, genuinely distinct, named specifically.
   - Scores — 4 pts. Likelihood and impact each carry a written reason; inherent risk arithmetic is correct.
   - Controls — 6 pts. Specific, costed, addressed to the named vulnerability rather than to the asset in general. "Turn on MFA" scores 1; "MFA on fab OT jump hosts via a separate RADIUS server, NT$600,000, 10 weeks" scores 3.
   - Residual risk — 4 pts. Recomputed correctly, with the affected axis identified and the control's limits stated honestly. 2 pts if residual equals inherent with no explanation.
   - A 2 pt deduction applies to any group whose register has fewer than 8 rows.

**Homework (due Thu 20:30 — Friday quiz):** Bring your cross-review sticky notes. Read the four case study briefs for tomorrow's jigsaw. Quiz is on the register columns and the meaning of residual risk.

**Differentiation / ELL support:** The template is a sheet, not a form — students type the column headings in first so the structure is fixed and the thinking goes into content. Provide a second pre-scored example row (a fab server) for students who need one worked before the blank. Groups of two are acceptable; a group of two simply produces 8 assets with a single named owner each. The likelihood 1–5 scale with written descriptors is on the reference sheet at the back of the room. Camera access for the gallery walk is provided by the projector screenshot, so nobody has to physically stand at another table.
