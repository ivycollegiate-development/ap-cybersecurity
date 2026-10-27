# U2 L20: Mock MCQ Sprint — Unit 2 Review (Oct 27) — TEACHER ANSWER KEY

**For teacher use only — do not distribute before sprint.**

---

## Answer Key with CED Rationales

### Question 1 — Cyberattack Phases (2.1.A)
**Correct: A. Reconnaissance**

**CED Rationale:** The four phases of a cyberattack (2.1.A–2.1.D) are: **Reconnaissance** → Initial Access → Lateral Movement → Exfiltration/Impact. Reconnaissance is the preparatory phase where adversaries gather intelligence: network topology, open ports, running services, employee information, technology stack. This informs the choice of exploit in Initial Access.

**Why the others are wrong:**
- **B. Initial Access** — Gaining a foothold (phishing, exploit, stolen creds). Comes *after* reconnaissance.
- **C. Lateral Movement** — Moving through the network after initial access. Requires prior access.
- **D. Exfiltration** — Removing data. Final phase, not preparatory.

---

### Question 2 — Risk Assessment (2.1.E)
**Correct: C. High**

**CED Rationale:** Risk = Likelihood × Impact. Standard 3×3 or 5×5 matrix:
- Medium Likelihood × Critical Impact = **High** inherent risk
- Residual risk (after controls) would be lower — e.g., adding fire suppression reduces likelihood or impact.

**Why the others are wrong:**
- **A. Low** — Would require Low likelihood (e.g., Rare × Minor)
- **B. Medium** — Would require Low×Critical, Medium×High, or High×Medium
- **D. Critical** — Would require High likelihood × Critical impact

---

### Question 3 — Physical Vulnerabilities (2.2.B)
**Correct: C. A locked door held open by a doorstop for ventilation**

**CED Rationale:** Physical vulnerabilities (2.2.A–2.2.C) include unsecured entry points, piggybacking/tailgating enablers, and environmental weaknesses. A doorstop on a secured door (C) **defeats the control entirely** — it creates an open path for anyone to enter without credentials, enabling tailgating by design.

**Why the others are wrong:**
- **A.** A proximity reader *logs* entries but doesn't prevent tailgating if an authorized user holds the door — it's a detection/audit control, not a preventive one.
- **B.** A mantrap with dual biometrics is a **strong preventive control** (2.3.C), not a vulnerability.
- **D.** A visitor sign-in sheet is an administrative/procedural control (2.3.A), not a physical vulnerability.

---

### Question 4 — Protecting Physical Spaces (2.3.B)
**Correct: C. Room layer**

**CED Rationale:** Defense-in-depth physical layers (2.3.A–2.3.C):
- **Perimeter** (A) — Fences, lighting, bollards, CCTV outside
- **Building** (B) — Lobby access, reception, badge readers at entrance, guards
- **Room** (C) — Server room door locks, **environmental controls** (HVAC, fire suppression, humidity), motion sensors inside the room
- **Rack/Asset** (D) — Cable locks, port locks, asset tags on individual equipment

Environmental controls protect the *room* environment where equipment operates.

---

### Question 5 — Detecting Physical Attacks (2.4.B)
**Correct: A. Badge log correlation with shift schedules**

**CED Rationale:** Detection methods (2.4.A–2.4.C) include log analysis, sensor alerts, and correlation. The scenario gives three data sources:
1. Badge log: Employee #4421 at 02:14 AM
2. Guard patrol: No check 01:00–03:00
3. CCTV: 4-min gap 02:12–02:16

**Badge log correlation with shift schedules (A)** directly identifies the *who* and *when* anomaly — an employee accessing a secure area 6 hours before shift start. This is the primary detection signal.

**Why the others are less direct:**
- **B. Guard patrol variance** — Confirms no human witnessed it, but doesn't identify the actor
- **C. CCTV gap** — Corroborates the time window but the gap *missed* the event; it's a detection failure, not a detection
- **D. Visitor log** — Irrelevant; this is an employee badge, not a visitor

---

## Re-Teach Board Tracking

Record the **objective codes** of the most-missed items. These codes drive the Nov 9–12 review block:

| Objective Code | Topic | Tally of Misses |
|----------------|-------|-----------------|
| 2.1.A–D | Cyberattack Phases | |
| 2.1.E | Risk Assessment (L×I matrix) | |
| 2.1.F | Risk Treatment (avoid/transfer/mitigate/accept) | |
| 2.2.A–C | Physical Vulnerabilities & Attacks | |
| 2.3.A–C | Protecting Physical Spaces (layers, controls) | |
| 2.4.A–C | Detecting Physical Attacks (logs, sensors, correlation) | |

**Instructions:** After peer-grading, have students call out their misses by objective code. Tally above. The top 3–4 codes become the focus for Nov 9 (Review Day 1), Nov 10 (Review Day 2), Nov 11 (Mock MCQ Sprint 2), Nov 12 (Review Day 4).