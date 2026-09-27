# U2 L22: Break Prep — Fall Break Audit Launch (Oct 29, Thu — PAPER DAY)

**⚡ HW Quiz (5 min):** 5 MCQ on the Unit 2 synthesis program (Oct 28) — which control layer closes a given physical gap, and the difference between a detective and a corrective control.

**Learning Objectives:**
- 2.2.A Identify tailgating and piggybacking risks in a real entry sequence and propose a control
- 2.2.C Explain how social engineering is used at the door, and at a badge reader
- 2.3.A Evaluate locks and access controls in a building the student actually uses
- 2.3.C Assess environmental and monitoring gaps against typhoon and flood seasons
- 2.4.A Identify what a badge or access log would and would not have recorded for a physical entry event

**Materials:** Printed audit packet ([GDoc](https://docs.google.com/document/d/1FallBreakAuditSheet)), completed sample audit (2 pages, teacher's own apartment), physical security slides, requirement checklist board, Unit 2 study guide (start it today)

**No computers for the break work.** This assignment is paper only — notebook or the printed packet, pen, and your own eyes. No GitHub, no submissions, no tech during Fall Break. If you want to photograph your building, that is fine, but the write-up is by hand.

---

## Activities

1. **Hook (5 min):** "You just let someone in your building without checking. Explain exactly what is wrong with that." Take two or three answers, then push on the second question: **"How would anyone else know you'd done it?"** That is the whole unit in one exchange — the vulnerability and the detection failure are the same event.

2. **Direct instruction — the audit, requirement by requirement (12 min):** Walk the checklist line by line on the board. Do not hand out the packet until the last item. For each requirement, state the vulnerability it targets and one control that would close it.

   - **Perimeter and door** — who can reach the door unchallenged? Single door, no mantrap. Note the gap between "the door is locked" and "the door admits only people who belong here."
   - **Access control** — keypad code, fob, card, guard, intercom, or nothing. Ask: how are codes distributed, changed, and revoked? Who holds a copy right now?
   - **Tailgating exposure (2.2.A)** — count how many people enter behind one badgeholder during a normal evening. Then ask what the badge log records. It records one event. The building saw four.
   - **Shoulder surfing and door social engineering (2.2.B, 2.2.C)** — a propped door, an unverified "I'm here to fix the router," a delivery held open for a neighbor. Note that 2.2.C attacks the *person* at the door, which is why training and mantraps are the controls, not a stronger lock.
   - **Cloning and lock picking (2.2.C)** — proximity cards and magnetic stripes are copyable; a tubular pin tumbler is pickable in seconds by anyone who watches a YouTube video. Push the class past "get a better lock": the answer is a layer, not a cylinder.
   - **Surveillance (2.3.B)** — is there CCTV? Camera placement matters more than camera count: does it cover the entry, or the parking lot?
   - **Environmental and monitoring (2.3.C)** — lighting, signage, landscaping that limits sightlines, fire doors that are wedged open, and a log that nobody reviews.
   - **Taiwan addendum A — shared building network (2.4.B):** every apartment in a Taiwanese building is usually on the same building switch and often the same ISP handoff, so the "home network" boundary is much wider than the apartment door. One student must record **one risk from shared building network infrastructure** and name the evidence that would reveal it. Accepted answers include: a single unmanaged building switch, one flat VLAN with no segmentation between tenants, a management interface reachable from tenant Wi-Fi, shared Wi-Fi with a default or published key, or an unmonitored building-level firewall handing off to the street.
   - **Taiwan addendum B — typhoon and flood season (2.3.C):** each student records **one physical-resilience gap** relevant to typhoon and flood season, and what it would break. Accepted answers include: entry doors and lobby glass facing wind-driven rain, ground-floor equipment on the power, a server or NAS shelf below floor level, no backup power for badge readers and network gear, a single roof drain path, water ingress reaching a power strip, or loose exterior fixtures.
   - **Risk line (2.1.E)** — every finding gets a likelihood and an impact, not just a description. "Unlocked side gate" is an observation; "unlocked side gate, likelihood medium, impact high, residual after control is low" is an assessment.
   - **Treatment line (2.1.F)** — every finding also gets a treatment: avoid, transfer, mitigate, or accept, with one sentence of reasoning. Accepting a risk is a legitimate answer; accepting it *without writing the sentence* is not.

3. **Sample audit walkthrough (15 min):** Distribute the packet. Then project the two-page completed sample — the teacher's own apartment building, photographed on foot, with a real mantrap problem, a keypad code that has not changed in two years, one camera pointed at the wrong thing, and a second-floor switch closet that floods. Read it aloud, front to back, and narrate the reasoning in the margin: why this is 2.2.A and not 2.2.C, why the likelihood is medium and not high, why the treatment on the switch closet is avoid rather than mitigate.

   Make the standard explicit before students leave: **describe, assess, treat, evidence.** Four lines minimum per finding. A finding with no evidence line is an opinion, and opinions do not earn credit.

4. **Due date, format, and Unit 2 recap (8 min):**
   - **Due:** the first class back — **Monday, Nov 9.** It comes back as a graded HW quiz at the start of the day, so bring it physically, not a photo.
   - **Length:** 2–4 pages, hand-written. One page minimum per addendum.
   - **Bring:** the packet, plus a two-sentence answer to each of the two Taiwan addenda.
   - **The graded thing is the reasoning, not the building.** A student who finds a serious flaw in a modest building and treats it well outscores a student who finds nothing at a gated complex.

   Then the unit recap, brisk: 2.1 attack phases and risk, 2.2 physical vulnerabilities, 2.3 protections, 2.4 detection. Do not re-teach — flag that Nov 9 through Nov 12 is four straight review days and the test is **Friday, Nov 13**, and that the first three of those days are driven by what the class's own audits found.

5. **Open Q&A (5 min):** Remaining time on questions. Take questions about the checklist, about what counts as acceptable evidence, and about the two addenda — the addenda are the part students most often get wrong.

**Homework (due Mon Nov 9, brought to class — graded HW quiz that day):** Complete the Fall Break physical security audit, 2–4 pages, by hand. Both Taiwan addenda included. Read the first CED excerpt of Unit 3 (Securing Networks) — a quiet read only; you are not expected to know it yet.

**Differentiation / ELL support:** The packet is fillable as a table, so a student can record findings as structured rows instead of prose. A one-page bank of likelihood/impact phrasings and a treatment-selection table are provided for students who find the risk vocabulary harder than the observation work. Students who cannot photograph or revisit their building may audit a shared common area (lobby, mailroom, bike room, stairwell) instead — the vulnerability categories are identical. For the two addenda, give a worked example of each so the required specificity is clear.