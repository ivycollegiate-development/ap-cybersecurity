# U2 L15 Mini-Project — Teacher Answer Key (TSMC Subcontractor Scenario)

**For teacher use only — not distributed to students**  
**Unit 2: Securing Spaces | Mini-Project Day 1 (Design) → Day 2 (Peer Review) → Day 3 (Presentations)**

---

## Scenario Summary (from GDoc: 1wC7delxjsSL8mR1jAqj-81Fce4w0sLZGWGoGiILBrU4)

| Element | Detail |
|---------|--------|
| **Role** | Security Director, TSMC subcontractor in Taichung |
| **Business** | Specialty chemicals for semiconductor fabrication |
| **Budget** | NT$2,000,000 / year (hard ceiling) |
| **Buildings** | Office (2F), Clean Room (1F + mezzanine), Chemical Storage (separate) |
| **Staff** | 200 employees, 3 shifts |
| **Assets** | Client chip designs (IP), chemical formulas, clean room environment, employee safety |
| **Current Controls** | Basic key locks, 1 CCTV at front desk, password-protected Wi-Fi |
| **Critical Constraint** | Typhoon/flood season — availability & integrity, not just security |
| **Deliverable** | Individual 7-slide Google Slides deck + cost table under NT$2M |

---

## Expected Top 3 Threats (Slide 1) — Strong Responses

| Rank | Threat | Why It Fits This Facility | CED LO Trace |
|------|--------|---------------------------|--------------|
| 1 | **IP Theft via Physical Access** (tailgating, cloned badge, social engineering at server room/IP vault) | Chip designs = high-value target; shared lobby + 3 shifts = extended attack surface; current controls = key locks only | 2.2.A, 2.2.C, 2.3.A, 2.4.A–C |
| 2 | **Typhoon/Flood Disruption to Clean Room & Chemical Storage** (flooding, power loss, HVAC failure, contamination) | Ground-floor clean room + chemical storage in typhoon zone; single roof drain; UPS on floor; availability = integrity for semiconductor supply chain | 2.3.C |
| 3 | **Insider Threat / Credential Misuse** (shared badges, contractor access, after-hours entry, shoulder surfing) | 200 people / 3 shifts = high credential exposure; cleaning/maintenance contractors; no badge log review; shared-credential trap from L13 lab | 2.2.A, 2.2.B, 2.2.C, 2.4.A–C |

**Acceptable alternatives** (if justified): Industrial espionage via wireless, supply chain tampering at chemical delivery, ransomware via physical USB drop.  
**Weak threats** (deduct): Generic "hacking," "malware," "data breach" without physical vector.

---

## Slide-by-Slide Strong Response Benchmarks

### Slide 2 — Perimeter + Entry Controls
| Required Element | Strong Response | Weak Response |
|------------------|-----------------|---------------|
| Boundary definition | Per-building fence line + mantrap at each entry; Office/clean room/chem storage each have dedicated perimeter | "Fence around campus" (too vague; buildings have different risk profiles) |
| Reader scoping | Office: all staff badges. Clean Room: fab staff + maintenance only (scope changed by security dir only). Chem Storage: hazmat-certified + security escort required. | "Badges for everyone" or no scoping |
| Visitor policy | All visitors: pre-registered, photo ID, escorted, badge expires at end of visit. Deliveries: receiving bay only, inspected, logged. | "Sign in at front desk" |
| Delivery handling | Dedicated receiving bay with CCTV, X-ray/scanner for chem storage deliveries, chain-of-custody log | Not addressed |

### Slide 3 — Interior Controls
| Required Element | Strong Response | Weak Response |
|------------------|-----------------|---------------|
| Corridor/stairwell control | Clean room corridors: badge readers at zone transitions. Stairwells: alarmed doors (fire code compliant), badge required for re-entry. Office: standard badge readers. | "Locks on doors" |
| Alarmed vs. locked | Server room/IP vault: alarmed + badge + door contact. Chemical storage: alarmed + dual-auth badge. Office interior: locked only. | All doors same treatment |
| Auditor-acceptable records | Badge logs with timestamp, location, badge ID, door state (forced/held open). Retained 90 days, exported monthly for audit. | "Logs exist" |

### Slide 4 — Server Room / IP Vault Controls (Critical Slide)
| Required Element | Strong Response | Weak Response |
|------------------|-----------------|---------------|
| Location risk | Ground floor = flood risk. **Rack elevation + flood barrier + leak sensors + UPS elevated**. IP vault inside server room = dual perimeter. | No flood mitigation |
| Access scope | Only: Security Dir, IT Lead, Vendor Escalation (pre-approved). **Two-person rule for vendor access**. Scope changes logged, approved by Security Dir. | "IT staff" |
| Door contact + tamper | Magnetic door contact + vibration sensor on frame + cabinet tamper switches. All alert to monitoring station. | "Badge reader" only |
| Power/HVAC failure | UPS (elevated) → generator auto-start → environmental monitoring alerts facilities lead + security. Graceful shutdown script for IP vault systems. | "UPS" only |

### Slide 5 — Policies + Detection Methods
| Required Element | Strong Response | Weak Response |
|------------------|-----------------|---------------|
| Visitor escort | Printed policy: escort required at all times, visitor badge color-coded, escort logs name/time/purpose. | "Visitors escorted" |
| Badge issue/return | HR onboarding → badge issued, scope set, photo logged. Termination → badge revoked < 1 hour, return verified, exit audit. | "HR handles it" |
| Contractor onboarding | Pre-vetted list, time-limited badges, scope-restricted, daily check-in/out, sponsor required. | "Contractors get badges" |
| Tailgating prohibition | Posted at every mantrap, enforced by sensors, disciplinary policy referenced. | Not addressed |
| After-hours access | Pre-approved list only, badge + PIN, logged, alert to night-shift security officer. | "Badge works 24/7" |
| Camera placement justified | **Per camera**: "Covers clean room entry mantrap — detects tailgating (2.2.A)." "Covers chem storage delivery bay — verifies chain of custody." | "Cameras at all doors" |
| Badge-log alerting thresholds | 1. Shared badge: same badge >2 entries in 60 sec → alert night-shift security. 2. Tailgating burst: >3 entries on 1 badge in 5 min → alert + camera review. 3. Failed-then-success: 3+ fails then success in 10 min → alert + verify identity. 4. After-hours: any server room/IP vault/chem storage entry 22:00–06:00 → page night-shift security, verify in 10 min, dispatch if not confirmed. | "Alert on weird stuff" |
| Retention period | Badge logs: 90 days hot, 1 year cold. Video: 30 days (storage cost in budget). | "Forever" or not stated |
| Out-of-hours recipient | **Named role**: Night-Shift Security Officer (contracted guard service, 22:00–06:00). Backup: Facilities Lead (on-call). | "Security team" |

### Slide 6 — Defense-in-Depth Rationale
| Strong Response | Weak Response |
|-----------------|---------------|
| **Layer 1 (Perimeter)**: Mantrap + fence delays adversary → buys time for detection. **Layer 2 (Entry)**: Badge scoping limits who reaches interior → reduces attack surface. **Layer 3 (Interior)**: Alarmed doors + zone segmentation contains lateral movement. **Layer 4 (Server Room)**: Dual-auth + tamper + environmental = detection even if preventive fails. **Layer 5 (Detection)**: Badge-log thresholds + cameras + named responder = detective controls that work at 3 AM. **Layer 6 (Policy)**: Visitor escort + badge lifecycle + contractor mgmt = administrative controls that make technical controls effective. **All layers trace to Top 3 Threats.** | List of purchases with prices. No explanation of how layers interact. |

### Slide 7 — Budget Breakdown (Sample Strong Plan, Under NT$2M)

| Line Item | Qty | Unit Cost (NT$) | Total (NT$) | What It Defends | Threat (from Slide 1) |
|-----------|-----|-----------------|-------------|-----------------|----------------------|
| Door reader + controller (HID iCLASS SE) | 18 | 18,000 | 324,000 | All building entries, server room, chem storage, clean room zones | 1, 3 |
| Electric strike / maglock retrofit | 18 | 12,000 | 216,000 | Door hardware for reader control | 1, 3 |
| CCTV camera (outdoor, IP, IR, vandal-resistant) | 12 | 22,000 | 264,000 | Perimeter fence, delivery bays, rooftop drainage | 1, 2 |
| CCTV camera (indoor, dome, WDR) | 16 | 15,000 | 240,000 | Mantraps, corridors, server room, chem storage interior | 1, 3 |
| NVR + storage (32-ch, 30-day retention, RAID) | 1 | 180,000 | 180,000 | Video recording for all cameras | 1, 3 |
| Badge printer + cards (DTC1250e + 500 cards) | 1 | 95,000 | 95,000 | Credential issuance, visitor badges, contractor badges | 3 |
| Door contact / sensor (magnetic + vibration) | 22 | 3,500 | 77,000 | Server room, IP vault, chem storage, clean room zones | 1 |
| Water leak sensors (rope + point) | 10 | 4,200 | 42,000 | Server room (raised floor), chem storage, clean room | 2 |
| Power monitoring (PDU + UPS SNMP) | 6 | 8,500 | 51,000 | Server room, NVR, badge controllers, network gear | 2 |
| Flood barrier (modular, 60cm deployable) | 1 set | 120,000 | 120,000 | Chemical storage building, clean room entry | 2 |
| Rack elevation kit (seismic-rated, 30cm) | 4 | 18,000 | 72,000 | Server room racks, IP vault equipment | 2 |
| UPS (elevated, 10kVA, SNMP, generator start) | 2 | 150,000 | 300,000 | Server room + IP vault power continuity | 2 |
| Guard service (contracted, night shift 22:00–06:00) | 365 nights | 1,800/night | 657,000 | Out-of-hours response, escort, patrol | 1, 3 |
| Signage, lanyards, procedures (printed, laminated) | 1 lot | 25,000 | 25,000 | Policy visibility, visitor management | 3 |
| Contingency (5%) | — | — | 100,500 | Unforeseen price variance, scope adjustment | — |
| **TOTAL** | | | **2,763,500** | **OVER BUDGET — MUST TRIM** | |

**Budget Trim Example (to get under NT$2M):**
- Reduce guard service to 200 nights (peak typhoon + high-risk periods): -292,000
- Reduce outdoor cameras to 8: -88,000
- Use existing NVR + add 2 drives: -120,000
- Phase flood barrier: chem storage only year 1: -60,000
- **Revised Total: ~NT$1,993,500** ✓

**Key teaching point:** Students **must** show trade-offs. A plan that fits budget by cutting critical controls (e.g., no night guard, no flood barrier) is weaker than one that cuts quantity but keeps coverage and documents residual risk acceptance.

---

## Grading Rubric Alignment (Peer Review → Presentation → Test)

| Rubric Row (Peer Review, 40 pts) | Presentation Rubric (12 pts) | Test Weight |
|----------------------------------|------------------------------|-------------|
| 1. Layer coverage (6) | Threat Model (4) | 2.3.A, 2.3.B, 2.3.C |
| 2. Defense in depth real (6) | Layered Controls (4) | 2.3.A–C, 2.4.A–C |
| 3. Server room treatment (6) | Layered Controls (4) | 2.3.A, 2.3.C, 2.4.C |
| 4. Cost realism (6) | — | 2.1.F (resource allocation) |
| 5. Value for money (4) | Justification (4) | 2.1.E, 2.1.F |
| 6. Detection quality (5) | Justification (4) | 2.4.A–C |
| 7. Policies & auditability (3) | Threat Model (4) | 2.3.A, 2.3.C |
| 8. Shared-surface realism (2) | — | 2.2.A, 2.3.B |
| 9. Clarity (2) | — | Communication |

---

## Common Student Gaps (Flag During Circulation)

| Gap | Why It Matters | Redirect Question |
|-----|----------------|-------------------|
| **No server room / IP vault section** | Highest-value asset, most testable LO | "Where are the chip designs stored? What happens if that room floods at 3 AM?" |
| **Empty cost table** | Cannot evaluate trade-offs; fails peer review criterion 4 | "How do you know you're under budget if you haven't priced anything?" |
| **Cameras without purpose** | Fails 2.3.B, 2.4.B, peer review criterion 6 | "This camera — what attack does it detect? What threshold triggers on its feed?" |
| **No named out-of-hours recipient** | Fails 2.4.C, peer review criterion 6 | "It's 3 AM. The alert fires. Who wakes up? What do they do?" |
| **Budget adds up but no threat trace** | Fails peer review criterion 5, Slide 6 rationale | "This NT$300K UPS — which of your top 3 threats does it reduce?" |
| **Shared lobby ignored** | Misses 2.2.A, 2.3.A, 2.4.B (building switch, shared VLAN) | "The lobby guard works for the landlord. Four tenants. How do you control who reaches your door?" |
| **Typhoon = only "water"** | Misses power loss, HVAC, wind damage, supply chain | "Power's out for 18 hours. HVAC down. Clean room humidity hits 80%. What fails first?" |

---

## Peer Review Day (L16) — Teacher Quick-Reference

| Reviewer Must Do | Author Must Do |
|------------------|----------------|
| Score all 9 criteria on printed rubric | Read feedback, pick 2–3 highest-value fixes |
| Write specific feedback for any criterion < 60% | Note disagreements with reasoning on slide |
| Calibrate scores as a class (5 min) | Keep cost table closed — no new spend without cuts |
| Return rubric + deck to author | Show revised deck with reviewer comments visible |

**Most common peer review misses:** Criterion 6 (detection quality — missing named recipient), Criterion 3 (server room — no power/HVAC failure plan), Criterion 8 (shared surface — lobby/building network).

---

## Presentation Day (L17) — Scoring Focus

| Rubric Row | 4 = Mastery | 2 = Typical Student |
|------------|-------------|---------------------|
| Threat Model | Assets + specific attacks tracing to shared lobby, 3-shift ops, typhoon | Assets listed, attacks generic ("theft," "hacking") |
| Layered Controls | Preventive + detective + corrective named; can explain failure cascade | Prevention only; "cameras and locks" |
| Justification | Every control: risk reduced + LO code + likelihood/impact effect | Controls listed, rationale vague, no LO codes |

---

## Unit 2 Test Connections (Nov 13)

| Test Item Type | Mini-Project Link |
|----------------|-------------------|
| "Design controls for a facility with shared lobby and 3 shifts" | Direct transfer — they've done it |
| "A badge log shows X; video shows Y. What is the finding?" | L13 lab + L15 Slide 5 thresholds + L18 FRQ Part (d) |
| "Calculate ALE for flood risk; choose treatment" | L5 risk mgmt + L15 budget trade-offs + L18 FRQ Part (b) |
| "Name a detective control for server room access" | L15 Slide 5 thresholds + L16 peer review criterion 6 |

---

## Files to Prepare (Teacher Only)

| File | Location | Purpose |
|------|----------|---------|
| `U2-L15-Mini-Project-Design.md` | Repo | Lesson plan |
| `U2-L16-Mini-Project-Peer-Review.md` | Repo | Peer review rubric + protocol |
| `U2-L17-Mini-Project-Presentations.md` | Repo | Presentation rubric + protocol |
| `U2-L18-FRQ-Packet.md` | Repo | FRQ practice (uses this scenario) |
| `U2-L15-Teacher-Answer-Key.md` | **This file** | Grading benchmark, budget samples, gap radar |
| **Google Sheet (this content)** | **Teacher-only Drive folder** | Sortable, filterable, shareable with co-teachers |

---

## Converting to Google Sheet

1. Copy this markdown content
2. In Google Sheets: **File → Import → Paste values** (or use `md2gdoc.py` equivalent for Sheets)
3. Suggested tabs:
   - **Scenario & Threats**
   - **Slide Benchmarks** (one tab per slide or consolidated)
   - **Sample Budget** (with formulas for trim scenarios)
   - **Rubric Alignment**
   - **Gap Radar** (circulation checklist)
   - **Test Connections**

**Sharing:** Restrict to `pjones@ivycollegiate.org` + any co-teachers. **Do not share with students.**

---

*Last updated: Oct 20, 2026 | For 2026-27 AP Cybersecurity (Fall Term)*