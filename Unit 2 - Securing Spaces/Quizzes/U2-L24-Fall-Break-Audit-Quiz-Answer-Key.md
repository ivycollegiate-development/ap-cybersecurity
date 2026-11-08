# U2 L24 — Fall Break Audit Quiz — ANSWER KEY

**Teacher only. Never shared with students and never attached to a Classroom assignment.**

**Total: 10 points** — Part A 5 × 1 pt, Part B 3 × 1 pt, Part C 2 × 1 pt.

**Objectives tested:** 2.2.A (Q1, Q5), 2.2.B (Q2), 2.2.C (Q3, Q4), 2.1.E (Q6–Q8), 2.1.F (Q9–Q10).

**Scoring (from the quiz instructions):**
- **Part A (Q1–Q5) — 1 pt each:** 0.5 for the correct category code, 0.5 for the attack it enables. No point for the code alone or the attack alone.
- **Q6, Q7 — 1 pt each:** for Q6, 0.5 for each rating **with** its reason — an unreasoned rating scores zero. For Q7, the finding plus a plausible "what happens next" chain.
- **Q8 — 1 pt:** all three lines correct = 1; two of three = 0.5.
- **Q9, Q10 — 1 pt each:** 0.5 for the treatment, 0.5 for the justification. Correct treatment with no justification scores 0.5.

---

## Part A — Classify the vulnerability (Q1–Q5)

| Q | Finding | Category | Attack it enables | Accept also |
|---|---|---|---|---|
| 1 | F1 — propped fire-exit door, no alarm, no camera | **2.2.A** | Unauthorized entry through the open door — tailgating / piggybacking (walking in behind staff) into the corridor that reaches the switch closet and records room | "unauthorized entry", "piggybacking", "walk-in through a held/propped door" |
| 2 | F2 — keypad and reception monitors face the lobby queue | **2.2.B** | Shoulder surfing — observing the PIN (and on-screen data) and replaying it to enter without a badge | "PIN observation", "watching the code being typed" |
| 3 | F3 — contractors released in with no work-order check | **2.2.C** | Social engineering at the door — pretexting / impersonating a delivery or service worker to be admitted | "pretexting", "impersonation at the door", "confidence trick" |
| 4 | F4 — concealed long-range reader cloned the badge | **2.2.C** | Credential cloning — the badge is copied wirelessly and the duplicate opens the same doors | "badge cloning", "RFID skimming", "card cloning" (not "lock picking") |
| 5 | F5 — turnstile held open, anti-passback alarm silenced | **2.2.A** | Tailgating / piggybacking — several people on one badge event, with the alarm that would catch it disabled | "tailgating", "one badge, many people" |

**Watch for:** Q4 marked 2.2.A. Cloning copies the credential; it is not following someone through. This is the item most likely to split the class, and it feeds Monday's re-teach.

---

## Part B — Likelihood and impact (Q6–Q8)

**Q6 — F1, the propped fire-exit door. 1 pt (0.5 per reasoned rating).**

- **Likelihood: High.** The door is wedged open *all day*, there is no door-prop alarm, and no camera on that side. Nothing detects or interrupts the path, so exposure is continuous — not occasional.
- **Impact: High.** The corridor behind it runs to the ground-floor switch closet and the records room. Reaching the switch closet means the network; reaching the records room means the records.

Accept Medium likelihood only if the reason names a real constraint (for example, the door is only propped while the floor is staffed). A rating with no reason scores zero, per the instructions.

**Q7 — the highest-impact finding. 1 pt.**

**Model answer — F1.** Chain: propped door → walk in unobserved → corridor → **switch closet** (network access: shut down or tap the network) and **records room** (records theft) → from the network, lateral movement and exfiltration.

A defensible alternative is **F4**: the cloned badge proved persistent — it opened the same doors *eleven days later* — so the attacker retains repeatable, credential-level access that survives a perimeter fix. Award the point for **any single finding plus a plausible "what happens next" chain**. Do not award for naming a finding with no chain.

**Q8 — inherent vs residual. 1 pt.**

- **Inherent risk:** High likelihood / High impact — the original rating, before the wedge is removed and the alarm installed.
- **Residual risk:** Medium likelihood / High impact — the rating that remains after the control.
- **What the control changed:** the **likelihood** half of the pair. Removing the wedge and adding a door-prop alarm reduces the *chance* of entry; it does nothing to the *consequence* once someone is inside. Impact stays High.

---

## Part C — Treatment (Q9–Q10)

**Q9 — F3, contractors admitted with no work-order check. 1 pt.**

- **Treatment: Mitigate.** 0.5
- **Justification:** deliveries must still get in, so the goal is not to stop contractor access but to add the missing verification step — check the work order and confirm the expected arrival before releasing the door. This lowers likelihood without blocking the docks. 0.5

Accept **Avoid** only if the justification is that contractor access is removed entirely (escorted hand-off at the dock, no door release) — that eliminates the exposure rather than reducing it. Do not accept **Transfer** or **Accept** here.

**Q10 — F2, the keypad PIN visible to the lobby queue. 1 pt.**

- **Treatment: Mitigate.** 0.5
- **Control that addresses the mechanism:** the mechanism is *observation of the PIN*, so the fix must break the line of sight — a privacy shield on the keypad and repositioning the keypad and the reception monitors out of the queue's view. Changing the PIN, or the keypad brand, does not address it. 0.5

Accept **Avoid** only where the justification is that the keypad is replaced by a credential with no visible input (for example, a card reader or a phone credential). Do not accept **Accept**.

---

## Diagnostic use

Per the lesson plan, the three lowest-confidence items drive the rest of the week's review. Sort the collected quizzes before Period 6 decides the focus:

- **Q1 / Q5 (2.2.A)** — entry-sequence control, not locks. Re-teach Tuesday if the class missed either.
- **Q2 / Q10 (2.2.B, 2.1.F)** — keypad position as a design failure, and treatment matching the mechanism.
- **Q4 (2.2.C)** — cloning vs. following; the category-split item.
- **Q8 (2.1.E)** — inherent vs residual and which half the control moved.

No names on the board at any point — the debrief is anonymized.
