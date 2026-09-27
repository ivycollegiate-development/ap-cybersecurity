# U2 L5: Risk Management Options (Oct 6, Tue — PAPER DAY)

**⚡ HW Quiz (5 min):** 3 MCQ on defense in depth functions, plus 1 on residual risk from your own matrix.

**Learning Objectives:**
- 2.1.F Explain and compare the four risk treatment options — avoid, transfer, mitigate, accept
- 2.1.E Justify a treatment choice for a specific scenario using likelihood, impact, and cost

**Materials:** Slides, treatment-options reference sheet, six costed scenario handouts ([GDoc](https://docs.google.com/document/d/1Gw3Xa60zTpQIgZik17NBuQK-FMhtpDHg6X52PBNix2M/edit)), exit ticket slip

**No computers today.** Paper day — the scenario work happens on the handout.

---

## Activities

1. **Hook (5 min):** "Your shared apartment building's front door lock fails. A locksmith quotes $50 to fix it. A thief breaks into a neighbor's apartment two weeks later and takes about $10,000 of laptop, jewelry, and cash. Is the lock worth it?" Take a vote, then push: the answer is obviously yes, so why do people skip it? Because the $50 buys insurance against something that may never happen, and $50 spent on a concert feels real while $50 of insurance feels like nothing. That is the whole problem risk treatment exists to solve.

2. **Direct instruction (15 min):**
   - **Avoid** — change the plan so the risk cannot occur. Stop shipping physical product, move the server off-site, cancel the service entirely. Works only if the activity is genuinely optional.
   - **Transfer** — hand the financial consequence to someone else. Cyber insurance, an SLA with penalties, outsourcing to a managed provider. **You still own the risk; you have moved the cost.** Say that out loud — students routinely answer "transfer" when they mean "delegate."
   - **Mitigate** — reduce likelihood or impact with controls. Locks, badges, MFA, training. The default answer for most items in a risk register.
   - **Accept** — consciously do nothing, and either absorb the cost or fund a contingency. Accept with a plan is a decision. Accept by ignoring it is a failure, and that is what the register is supposed to expose.
   - **Cost versus exposure:** the $50K question. You are not choosing the cheapest control; you are choosing the treatment where control cost is proportionate to expected loss (likelihood × impact). A $50,000 fire-suppression system for a $200 asset is bad. A $20 lock for a $50,000 server room is good.
   - Note that treatments combine. Transfer the financial risk *and* mitigate the physical risk is common and defensible.

3. **Activity — six costed scenarios (20 min):** Work the handout. For each scenario, pick a treatment, name a specific control if you chose mitigate, and justify it in two sentences referencing likelihood, impact, and cost.

   The six:
   1. Taichung fab — cleanroom wafer scrap with 2024 process data left in an open corridor outside the fab. Value of the data: $2M. Scrap is disposed of next week or not at all.
   2. Apartment building — 40 doors, no visitor log, one known break-in this year. $15K in losses last year. $6,000 for a full lock and intercom upgrade.
   3. Small clinic — off-site backup tapes in the same closet as the servers. Fire destroys both. $3,000 for off-site storage.
   4. Student records — a single shared admin account, no MFA, four staff use it daily. $40K to implement individual accounts with MFA.
   5. Cafeteria card system — vendor says a breach exposes roughly 8,000 card numbers. Vendor offers $500,000 liability cap. Redeploying to a different vendor costs $20,000 up front plus a term of lost transactions.
   6. School building — a roof leak above the server closet is fixed for $800. A flood happened four years ago. The servers are on the bottom shelf.

   Push groups past the obvious answer. Scenario 5 looks like transfer until you notice the cap is below the exposure. Scenario 6 looks like mitigate but the honest call may be accept-and-plan if the roof is the building department's decision, not the school's.

4. **Exit ticket (5 min):** "A risk has low likelihood and catastrophic impact. Name a treatment, name a control, and explain why you did not pick a different one." Collect on paper. This exact reasoning appears on the Unit 2 test.

**Homework (due Wed 20:30 — Thursday quiz):** Read CED 2.1.F and be ready to build a risk register tomorrow. Bring your six scenario justifications — Wednesday's lab reuses this vocabulary.

**Differentiation / ELL support:** Provide a partially completed handout with scenarios 1 and 2 already treated as worked examples so the task starts from imitation rather than blank page. The transfer-versus-delegate distinction is the hard one; a printed two-column card contrasting the two is on the front desk. Students may write the justification orally to a partner before writing it.
