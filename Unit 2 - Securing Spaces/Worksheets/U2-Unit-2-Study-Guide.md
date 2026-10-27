# Unit 2 Study Guide — Securing Spaces

**Name:** _________________________  **Class:** AP Cybersecurity

---

## How to Use This Guide

1. **After every Mock MCQ Sprint** (Oct 27, Nov 11, and any practice), file every miss in the tracking tables below.
2. **File guessed-right answers too** — if you weren't sure, you don't own the objective.
3. **Before the Unit 2 Test (Nov 13)**, this guide is your personalized review plan. Every row with a tally > 0 is a topic you must re-study.
4. **Bring this to every review day** (Nov 9–12). The re-teach board tells you which objectives are the class priorities; your guide tells you *your* priorities.

---

## 2.1 — Cyberattack Phases & Risk Management

| Objective | Description | Miss Tally | Notes / Key Concepts to Review |
|-----------|-------------|------------|--------------------------------|
| 2.1.A | Reconnaissance — information gathering (passive/active) | | |
| 2.1.B | Initial Access — gaining a foothold (phishing, exploits, valid accounts) | | |
| 2.1.C | Lateral Movement — pivoting, privilege escalation, credential dumping | | |
| 2.1.D | Exfiltration / Impact — data theft, encryption, destruction | | |
| 2.1.E | Risk Assessment — Likelihood × Impact matrix, inherent vs. residual risk | | |
| 2.1.F | Risk Treatment — Avoid / Transfer / Mitigate / Accept (with examples) | | |

---

## 2.2 — Physical Vulnerabilities & Attacks

| Objective | Description | Miss Tally | Notes / Key Concepts to Review |
|-----------|-------------|------------|--------------------------------|
| 2.2.A | Physical attack vectors — tailgating, lock bypass, device theft, dumpster diving | | |
| 2.2.B | Physical vulnerabilities — unsecured doors, poor lighting, exposed cabling, no mantraps | | |
| 2.2.C | Environmental threats — fire, flood, power loss, HVAC failure, temperature/humidity | | |

---

## 2.3 — Protecting Physical Spaces

| Objective | Description | Miss Tally | Notes / Key Concepts to Review |
|-----------|-------------|------------|--------------------------------|
| 2.3.A | Perimeter & Building layer controls — fences, lighting, CCTV, guards, reception, badges | | |
| 2.3.B | Room layer controls — server room locks, **environmental controls** (HVAC, fire suppression, humidity), motion sensors, cable management | | |
| 2.3.C | Rack/Asset layer controls — cable locks, port locks, asset tags, mantraps, biometric access | | |

---

## 2.4 — Detecting Physical Attacks

| Objective | Description | Miss Tally | Notes / Key Concepts to Review |
|-----------|-------------|------------|--------------------------------|
| 2.4.A | Log sources — badge logs, guard patrol logs, CCTV, visitor logs, sensor alerts | | |
| 2.4.B | Correlation & anomaly detection — off-hours access, impossible travel, missing patrols, CCTV gaps, multi-source correlation | | |
| 2.4.C | Alerting & response — alert design (thresholds, enrichment), escalation, incident documentation | | |

---

## Personal Review Priority (Fill In After Each Sprint)

| Sprint Date | Top 3 Objective Codes I Missed Most | Action (re-read, lab redo, peer explain, office hours) |
|-------------|--------------------------------------|--------------------------------------------------------|
| Oct 27 (P21) | 1. __________  2. __________  3. __________ | |
| Nov 11 (P27) | 1. __________  2. __________  3. __________ | |
| Practice / Other | 1. __________  2. __________  3. __________ | |

---

## Key Terms Quick Reference

| Term | Definition | Objective |
|------|------------|-----------|
| Inherent Risk | Risk before any controls applied | 2.1.E |
| Residual Risk | Risk after controls applied | 2.1.E |
| Defense in Depth | Layered security: Perimeter → Building → Room → Rack | 2.3.A–C |
| Mantrap | Two-door interlock with authentication on both sides | 2.3.C |
| Tailgating | Following an authorized person through a secured door | 2.2.A |
| Piggybacking | Authorized person knowingly lets unauthorized person in | 2.2.A |
| CCTV Gap | Time window where camera footage is missing | 2.4.B |
| Correlation | Linking multiple log sources to detect anomalies | 2.4.B |

---

## Mini-Project Reference (Oct 20–22)

**Scenario:** Design a physical security program for a 3-story office building with server room, reception, and shared tenant spaces.

**Your Design Deliverables:**
- [ ] Threat model (adversary types, entry points, assets)
- [ ] Control selection per layer (perimeter, building, room, rack)
- [ ] Detection plan (log sources, correlation rules, alert thresholds)
- [ ] Budget with justification (cost vs. risk reduction)

**Review Criteria (used for peer review & synthesis):**
1. **Coverage** — All 4 layers addressed with specific controls
2. **Detection** — At least 3 correlation rules with log sources named
3. **Budget realism** — Costs researched, risk reduction quantified
4. **Trade-offs** — Explicit accept/mitigate/transfer decisions documented

---

## Fall Break Assignment (Assigned Oct 29, Due Nov 9)

**Physical Security Audit — Home Exercise (paper only, no tech)**

1. **Shared Infrastructure Risk** — In your apartment/building, identify ONE shared-infrastructure risk (e.g., shared network closet, common hallway CCTV, building-wide access control). Describe the risk and one mitigation.
2. **Weather Resilience Gap** — Identify ONE typhoon/flood physical resilience gap (e.g., server room on ground floor, no flood sensors, single power feed). Describe the gap and one mitigation.

**Format:** One page, handwritten or typed. Collected Nov 9 (first class back). Graded as homework quiz.