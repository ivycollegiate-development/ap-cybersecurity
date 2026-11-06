# U2 L25 — FRQ Practice: Model Answer and Scoring Notes — ANSWER KEY

**Teacher only. Never shared with students and never attached to a Classroom assignment.**
Read aloud in class; students self-score against the rubric a second time while it is read.

---

## Model answer (read-aloud text)

**Finding 1 — the keypad entry door (2.2.B, shoulder surfing).**
The single entry door uses a keypad PIN, and the keypad is mounted so the code is visible to anyone standing in the lobby queue. **Likelihood: High** — residents report unknown people entering several times in the past month, a shared code entered in view of others is observed routinely, and there is no second factor to defeat. **Impact: High** — one observed code gives unrestricted, unlogged entry to every resident floor and to the ground-floor switch closet, and there is no camera on the corridor behind the door to reconstruct what happened afterwards.

**Treatment: mitigate.** Move the keypad out of the queue's sightline and add a privacy shield, then pair the keypad with a second, independent control — a door-position sensor that alerts on held-open doors and a camera covering the interior corridor. This does not remove the risk; it reduces both the chance the code is observed and the value of the code once it is.

**Finding 2 — the unmonitored approach and no per-person record (2.2.A, tailgating).**
The CCTV covers the parking entrance but not the entry door's approach path, the keypad produces no per-person record at all — one shared code admits any number of people — and the staff badge log records a single badge event regardless of how many people follow through behind it. **Likelihood: High** — the audit of the class's own buildings found entry-sequence failure more often than any lock weakness, and this scenario has both halves of it. **Impact: High** — an intruder is inside an occupied residential building with access to the switch closet, and the only record is a single staff badge event.

**Treatment: mitigate.** Add a camera whose field of view covers the approach path and the door face together, and pair the entry door with a control that counts people — an anti-tailgating sensor, or a camera-count-versus-credential-count mismatch alert. (Several people passing through one opening produce a single door-position event, so a door-position sensor alone cannot catch a second person.) The point is that the building gains a record of *how many* people entered, which is the fact the current control cannot produce.

**The two conditions that lose the most points:**
The switch closet is on the ground floor. Treated as a security problem alone, that is a locked door. Treated correctly, it is also an **environmental** problem: in Taichung's typhoon season a ground-floor closet is below the water line of a blocked drain or a loading-dock inflow, so the equipment should be raised above the expected flood level, with a water-leak sensor that alerts and a secondary drain path. **Typhoon and flood resilience is a Unit 2 control (2.3.C), not an aside.** If the building shares a network with its neighbours — a common unmanaged switch or a management console reachable from tenant Wi-Fi — that flat shared infrastructure is a **2.3** risk worth naming, because it means the building's own controls are not the whole boundary.

---

## Scoring guidance

| Criterion | Points | Full credit looks like |
|---|---|---|
| Two physical vulnerabilities, correctly categorised (2.2.A / 2.2.B / 2.2.C) | 2 | Both named and both labelled with the right CED code. 1 pt for two named but only one categorised, or one named and categorised. |
| Likelihood + impact per finding, with a one-sentence reason | 2 | Four ratings present (two per finding), each with a reason that references the mechanism. A rating with no reason scores zero for that rating. |
| Two correct treatments, justified | 4 | 2 pts per finding: treatment named (1) + justification tied to the mechanism (1). Naming a treatment with no justification scores 1 of 2. |
| Ground-floor switch closet + a Taiwan condition | 2 | 1 pt for treating the closet as an environmental (flood) as well as access problem; 1 pt for naming the typhoon/flood condition or the shared-building-network risk as a real risk, not a footnote. |

**Common ways to lose points**
- Answering a broader question than the one asked — redesigning the whole building instead of assessing two findings.
- Naming a vulnerability without its CED category.
- Giving a treatment with no justification, or a justification that restates the treatment ("mitigate it by mitigating").
- Treating the switch closet as only a locked door, missing the environmental half.
- Recommending more than two treatments when the prompt asks for two — a third treatment costs time and earns nothing.

---

## Item notes for the delta conversation

The two findings in the model answer map to the class's own Fall Break audit categories. If a student's paper is weak on 2.2.A (tailgating) but strong on 2.2.C (cloning and door social engineering), that is the same split the L24 audit debrief surfaced — and it is the split to target in Wednesday's sprint.
