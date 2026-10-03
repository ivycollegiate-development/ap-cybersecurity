# U2 L15: Mini-Project Day 1 — Defense-in-Depth Design (Oct 20, Tue — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on defense in depth: layers, functions, and what a detective control contributes that a preventive one cannot.

**Learning Objectives:**
- 2.3.A Design a layered physical access control plan (perimeter, entry, interior, server room) with cost justification
- 2.3.B Specify surveillance coverage and retention policy for the scenario
- 2.3.C Include environmental and monitoring controls appropriate to the site
- 2.4.C Define detection and alerting for each layer of the plan

**Materials:** Slides, scenario brief ([GDoc](https://docs.google.com/document/d/1wC7delxjsSL8mR1jAqj-81Fce4w0sLZGWGoGiILBrU4/edit)), Google Slides template (team deck), cost table sheet, role assignment board, projector

---

## Activities

1. **Scenario brief and framing (7 min):** Read the brief aloud and let the reality of it land before anyone opens a slide deck.

   **You are the security director for a TSMC subcontractor in Taichung.** You have **NT$2,000,000** to secure the facility for one year. The building is a leased industrial office block in a Taichung science park: three floors, roughly 40 staff, a ground-floor server closet that also serves the office LAN, a shared bike area, a loading bay used by a contract courier, and a shared apartment-building network cabinet one block away that half your staff also touch. You report to a customer audit annually. Get it wrong and the customer relationship is at risk; get it right and the audit is a formality.

   Name the constraints out loud, because they are the whole problem:
   - A fixed budget with real prices. Every camera and reader has a cost and the total must land under NT$2M.
   - An **audit** requirement. Controls that cannot produce a record are worth less here, because the auditor is the customer.
   - **Shared surfaces you do not control** — the bike area, the courier, the apartment cabinet. You cannot lock down what is not yours; you have to monitor and detect.
   - **Typhoon and flood season.** A server closet on a ground floor is an availability and integrity problem before it is a security one, and the plan has to survive it.
   - Only about 8 hours of staffed coverage on weekdays. Anything that needs a human to notice has to fit inside those hours, and this connects directly to the 3 AM argument from two weeks ago.

   Deliverable: a **Google Slides deck** presenting the plan, built in a 4-person team.

2. **Role assignments (5 min):** Assign in the room, not by preference. Write the four roles on the board with what each owns:
   - **Layer Lead — Perimeter & Entry.** Fence, approach, main doors, visitor process, reception, bike area, courier bay.
   - **Layer Lead — Interior & Server Room.** Corridor and stairwell control, the server closet, badge scopes, environmental and flood controls.
   - **Detection & Monitoring Lead.** Cameras and placement logic, badge log alerting thresholds, retention policy, who receives a 3 AM alert.
   - **Budget & Compliance Lead.** The cost table, the audit trail, and the policy documents. Owns the constraint that the numbers work.

   Each role must produce a visible section of the deck. Note for the Detection Lead: the hardest question in this scenario is not which camera, it is who is awake to receive the alarm. Have them answer it before they place a single camera.

3. **Design work — build the plan (26 min):** Groups build in Google Slides. Use the six required sections as slide headers; the deck grows as the plan grows.

   - **Perimeter.** What defines the boundary, who can cross it freely, what is shared with a neighbour or the street. The bike area and the courier bay are the hard ones — the site is not fully controlled and the design has to acknowledge that.
   - **Entry.** Doors, readers, scope, visitor sign-in and escort policy, delivery handling. A reader is a *scoping* decision: which badges open which doors, and who can change a scope. Note the shared-credential trap from the audit lab — an unlogged shared code undoes all of it.
   - **Interior.** Corridor and stairwell control, which doors are alarmed, what is alarmed vs. merely locked, and which of those produces a record an auditor will accept.
   - **Server room.** The ground-floor closet is the crown jewel and the worst-placed asset on the site. Address location risk (flood), access scope, door contact, tamper detection, and what happens to a power or HVAC failure. Ask: who can open this door, and how would we know if someone who should not opened it?
   - **Policies.** Visitor escort, badge issue and return, contractor onboarding and badge deactivation, clean-desk in the server area, tailgating prohibition, after-hours access. Every policy needs an owner and a review cycle, or it is a document rather than a control.
   - **Detection.** Cameras with placement justified against a purpose, badge log alerting thresholds, retention period, and the named recipient for an out-of-hours alert. Tie each threshold to something from the lab: shared badge, tailgating burst, failed-then-success, after-hours entry.

4. **Cost table (5 min):** The Budget & Compliance Lead builds the cost table live while the others design. Use realistic Taichung figures and make every line defensible:

   | Line item | Qty | Unit cost (NT$) | Total (NT$) | What it defends | Layer |
   |---|---|---|---|---|---|
   | Door reader + controller | | | | | |
   | Electric strike / maglock retrofit | | | | | |
   | CCTV camera (indoor / outdoor) | | | | | |
   | NVR + storage (retention target) | | | | | |
   | Badge printer + cards | | | | | |
   | Door contact / sensor | | | | | |
   | Water leak + power monitoring | | | | | |
   | Flood barrier / rack elevation | | | | | |
   | Guard service (contracted hours) | | | | | |
   | Signage, lanyards, procedures | | | | | |
   | Contingency | | | | | |

   Hard rules: the total must come in **under NT$2,000,000**, every line must name what it defends, and contingency is not a place to hide an unaffordable camera. If a group cannot afford a control, that is a legitimate and interesting answer — *which* layer absorbs the risk, and how the residual risk is accepted and documented. A 3% contingency line is normal; a 20% one is a plan that did not add up.

5. **End-of-period check (2 min):** Before students leave, each group shows the teacher two things:
   - The **design draft** — the layered plan, on the slide or whiteboard, in enough detail that a stranger could spot the gap.
   - The **deck skeleton** — the six section headers exist, with the cost table started, even if the content is thin.

   Flag any group that has no server room section or an empty cost table. Those are the two that collapse tomorrow. Any unassigned or drifted role is reassigned now, not at 8:10 tomorrow morning.

**Homework (due Wed 20:30 — Wednesday quiz):** Finish the deck. Every section must have real content and a complete cost table under NT$2M. Bring the deck to class tomorrow ready to swap for peer review — you will be reviewing someone else's plan, and you will want yours to survive the same reading.

**Differentiation / ELL support:** The role structure gives every student one owned section, which is the main scaffold — nobody is left deciding where to start. The cost table is pre-filled with line items and a Total row formula, so the work is estimating, not formatting. A worked cost example for one control is on the deck template slide. Provide the six section headers as a pre-made Google Slides layout so groups spend the period on content. The flood and typhoon item is a genuine differentiator: students who have seen flooding in Taichung lead that section, and for others it is a concrete scenario to reason about rather than an abstraction. Students who need support can present the deck and have a partner handle the cost table verbally — but the numbers still have to be right.