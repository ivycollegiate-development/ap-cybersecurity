# U2 L15: Mini-Project Day 1 — Defense-in-Depth Design (Oct 20, Tue — TECH DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on defense in depth: layers, functions, and what a detective control contributes that a preventive one cannot.

**Learning Objectives:**
- 2.3.A Design a layered physical access control plan (perimeter, entry, interior, server room) with cost justification
- 2.3.B Specify surveillance coverage and retention policy for the scenario
- 2.3.C Include environmental and monitoring controls appropriate to the site
- 2.4.C Define detection and alerting for each layer of the plan

**Materials:** Scenario brief ([GDoc](https://docs.google.com/document/d/1wC7delxjsSL8mR1jAqj-81Fce4w0sLZGWGoGiILBrU4/edit)) — students create their **own** Google Slides deck (7 slides) from scratch; projector.

---

## Activities

1. **Scenario brief and framing (7 min):** Read the brief aloud and let the reality of it land before anyone opens a slide deck.

   **You are the security director for a TSMC subcontractor in Taichung.** The company manufactures specialty chemicals used in semiconductor fabrication. **NT$2,000,000** budget for one year. The facility:
   - **3 buildings:** Office (2 floors), Clean Room (1 floor + mezzanine), Chemical Storage (separate building)
   - **200 employees, 3 shifts**
   - **Assets to protect:** client chip designs (IP), chemical formulas, clean room environment, employee safety
   - **Current controls:** basic key locks, one CCTV camera at front desk, password-protected Wi-Fi
   - **Typhoon season:** Taichung sits in typhoon/flood territory — the plan must keep the facility available and its assets protected through a typhoon event (flooding, power loss, wind damage are availability/integrity problems, not just security ones).

   Name the constraints out loud, because they are the whole problem:
   - A fixed budget with real prices. Every camera and reader has a cost and the total must land under NT$2M.
   - **Typhoon and flood season.** A chemical storage building and a clean room are availability and integrity problems before they are security ones, and the plan has to survive the weather.
   - **3 shifts, 200 people.** Anything that needs a human to notice has to work when only the night shift is present, and this connects directly to the 3 AM argument from two weeks ago.

   Deliverable: each student builds **their own Google Slides deck — 7 slides**. This is deliberately not a group project: no role split, no shared deck. The class's three independent plans for the same facility will diverge in budget decisions, and that divergence is the most useful thing that happens this week. (If the class were larger, students could compare in larger sets, but the individual-design model stays.)

2. **Individual plan framing (5 min):** Every student owns the whole plan. Write the seven required slides on the board and what each one is really asking:
   - **Slide 1 — Title + Threat Model.** Top 3 threats to *this* facility. Everything else in the deck must trace back to these three.
   - **Slide 2 — Perimeter + Entry controls (with costs).** What defines each building's boundary, who can cross it freely, reader scoping (which badges open which doors, who can change a scope), visitor sign-in and escort policy, delivery handling.
   - **Slide 3 — Interior controls (with costs).** Corridor and stairwell control, which doors are alarmed vs. merely locked, which of those produces a record an auditor will accept.
   - **Slide 4 — Server Room / IP Vault controls (with costs).** Address location risk, access scope, door contact, tamper detection, and what happens on power or HVAC failure. Ask: who can open this door, and how would we know if someone who should not opened it?
   - **Slide 5 — Policies + Detection methods (with costs).** Visitor escort, badge issue/return, contractor onboarding and deactivation, tailgating prohibition, after-hours access; cameras with placement justified against a purpose, badge-log alerting thresholds, retention period, and the named recipient for an out-of-hours alert. Tie each threshold to the lab: shared badge, tailgating burst, failed-then-success, after-hours entry.
   - **Slide 6 — Defense-in-Depth rationale.** How the layers actually work together — not a list of purchases. A camera nobody watches is not detection.
   - **Slide 7 — Budget breakdown + total.** Must stay **under NT$2,000,000**.

   Remind them of the shared-credential trap from the audit lab — an unlogged shared code undoes all of it.

3. **Design work — build the plan (26 min):** Students build their own deck in Google Slides using the seven required slides as headers. Circulate with the two questions that separate a strong plan from a shopping list:
   - *"Who is awake to receive the alarm?"* The hardest question is not which camera, it is who answers the 3 AM alert on the night shift. Have them answer it before they place a single camera.
   - *"Which threat does this spend defend?"* Every control must trace to one of the top 3 threats from Slide 1.

4. **Cost table (5 min):** Each student builds the budget breakdown (Slide 7) with realistic Taichung figures and every line defensible:

   | Line item | Qty | Unit cost (NT$) | Total (NT$) | What it defends | Threat (from Slide 1) |
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

   Hard rules: the total must come in **under NT$2,000,000**, every line must name what it defends and which threat it traces to. If a student cannot afford a control, that is a legitimate and interesting answer — *which* layer absorbs the risk, and how the residual risk is accepted and documented. A 3% contingency line is normal; a 20% one is a plan that did not add up.

5. **End-of-period check (2 min):** Before students leave, each shows the teacher two things:
   - The **design draft** — the layered plan, in enough detail that a stranger could spot the gap.
   - The **deck skeleton** — the seven slide headers exist, with the cost table started, even if the content is thin.

   Flag any student who has no server room / IP vault section or an empty cost table. Those are the two that collapse on peer-review day.

**Homework (due Wed 20:30 — Wednesday quiz):** Finish the deck. **Post it to the Google Classroom assignment** (turn it in there) in addition to keeping it in your own Drive folder. Every slide must have real content and a complete cost table under NT$2M. Bring the deck to class ready for peer review — both classmates will review it against the same four criteria you will use on their decks (coverage, budget realism, layering, threat alignment — every score must cite a specific slide and a specific reason, and each reviewer must also write one thing to add and one thing to cut, with reasons).

**Looking ahead:** U2 L16 is peer review — every student reviews both classmates' decks, then writes an author response (which criticism accepted, which rejected and on what grounds, what is changing — graded). U2 L17 is presentations to the class, with questions from the floor counting toward the rubric, and the three plans' divergent budget decisions as the closing comparison.

**Differentiation / ELL support:** Every student owns all seven slides, which is the main scaffold — nobody is left deciding where to start; the seven headers give the structure. The cost table is pre-filled with line items, so the work is estimating, not formatting. The typhoon and flood item is a genuine differentiator: students who have seen flooding in Taichung will lead with those controls, and for others it is a concrete scenario to reason about rather than an abstraction. Students who need support can present verbally while a printed cost table carries the numbers — but the numbers still have to be right. On peer-review day, the strictest scaffold is the citation rule: no score without a slide reference.
