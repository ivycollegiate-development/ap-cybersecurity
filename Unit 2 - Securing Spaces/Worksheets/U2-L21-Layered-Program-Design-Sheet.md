# U2 L21: Layered Physical Security Program Design Sheet (Front) + Fall Break Audit Checklist (Back)

**Name(s):** _________________________________________  **Date:** Oct 28  **Period:** P22

---

## Scenario: Your Home / Building

Your home / apartment building / dorm is the site. Each of you audits a different real location. The threat model is yours — what's worth protecting, who wants in, what the building already does, and what it doesn't.

**Threat model shift:** Articulate how your home's risk profile changes when viewed through Unit 2 lenses.

**Taiwan-specific context:** Shared building network infrastructure in local apartments/offices, plus typhoon/flood physical resilience — you must address both.

---

## Design Instructions

Design a **layered physical security program** across six zones. For every control you add:

1. **Name the specific control** (e.g., "Mantrap at server room entry", "Badge reader + PIN at clean-room door", "Doorbell camera at apartment entry", "Flood sensor under NAS shelf")
2. **Justify it by naming the Unit 2 Learning Objective it satisfies** — write the **objective code** in the second column
3. **A control with no objective code does not go on the sheet**

**Objective Code Reference Strip:**

| 2.1.A Recon | 2.1.B Initial Access | 2.1.C Lateral Movement | 2.1.D Exfiltration | 2.1.E Risk Assessment | 2.1.F Risk Treatment |
| 2.2.A Physical Attack Vectors | 2.2.B Physical Vulnerabilities | 2.2.C Environmental Threats |
| 2.3.A Perimeter/Building | 2.3.B Room Layer (env. controls) | 2.3.C Rack/Asset Layer |
| 2.4.A Log Sources | 2.4.B Correlation & Anomaly Detection | 2.4.C Alerting & Response |

---

## Zone 1: PERIMETER (Building exterior, property line, parking, lobby entrance, shared building envelope)

| Control | Unit 2 LO Code |
|---------|----------------|
|         |                |
|         |                |
|         |                |
|         |                |

---

## Zone 2: ENTRY CONTROL (Building entry — guard, intercom, keypad, fob; apartment/room door; tailgating exposure)

| Control | Unit 2 LO Code |
|---------|----------------|
|         |                |
|         |                |
|         |                |
|         |                |

---

## Zone 3: INTERIOR ZONES (Rooms, network gear closet, NAS/server shelf, work-from-home desk)

| Control | Unit 2 LO Code |
|---------|----------------|
|         |                |
|         |                |
|         |                |
|         |                |

---

## Zone 4: MONITORING (Building CCTV, hallway cameras, doorbell cam, smart sensors, environmental sensors)

| Control | Unit 2 LO Code |
|---------|----------------|
|         |                |
|         |                |
|         |                |
|         |                |

---

## Zone 5: DETECTION (Badge/access logs, doorbell events, router logs, sensor alerts, guard patrol logs)

| Control | Unit 2 LO Code |
|---------|----------------|
|         |                |
|         |                |
|         |                |
|         |                |

---

## Zone 6: RESPONSE (Who you call, escalation path, landlord/management contact, personal incident log, named owner + action)

| Control | Unit 2 LO Code |
|---------|----------------|
|         |                |
|         |                |
|         |                |
|         |                |

---

## Teacher Prompts (for reference — not for student copy)

- If a student's entry control is a **keypad code**, ask: which physical attack does the keypad do nothing about? → **2.2.A tailgating, 2.2.C shoulder surfing**
- If their monitoring is a **doorbell camera**, ask: what does the camera not generate? → **2.4.A — cameras are not logs; the badge/access log is where the correlation of 2.4.B comes from**
- If their response is **"call the landlord"**, ask: **who is the named owner and what is the specific action?**
- Local texture to use: **typhoon/flood resilience** for gear closet & ground-floor equipment (2.3.C), **shared lobby** where one entrance serves multiple households, **building network infrastructure** (shared switch, flat VLAN, management interface reachable from tenant Wi-Fi) as an access path nobody in the unit owns (2.4.B)

---

## Gap Hunt (Class Activity — after peer cross-check)

**Which Unit 2 learning objective did NO student cover?** ________________________________________

That gap is the first item on the re-teach board for Nov 9.

---

# ═══════════════════════════════════════════
# REVERSE SIDE: FALL BREAK AUDIT CHECKLIST
# ═══════════════════════════════════════════

## U2 Fall Break Physical Security Audit — Checklist

**Name:** _________________________  **Building:** _________________________  **Unit/Floor:** _______

**Instructions:** Complete this checklist during Fall Break. For each finding, you must write **four lines minimum**: Description → Likelihood → Impact → Treatment + Reasoning → Evidence. A finding with no evidence line is an opinion and earns no credit. Attach additional pages if needed. Due **Nov 9** (brought to class, handwritten).

---

### 1. Perimeter & Door
| Finding | Likelihood (L/M/H) | Impact (L/M/H) | Treatment (Avoid/Transfer/Mitigate/Accept + Reasoning) | Evidence (what you saw / photographed / log shows) |
|---------|-------------------|----------------|--------------------------------------------------------|-----------------------------------------------------|
|         |                   |                |                                                        |                                                     |
|         |                   |                |                                                        |                                                     |

**LO Codes Targeted:** 2.2.A, 2.2.B, 2.3.A

---

### 2. Access Control
| Finding | Likelihood | Impact | Treatment + Reasoning | Evidence |
|---------|------------|--------|----------------------|----------|
|         |            |        |                      |          |
|         |            |        |                      |          |

**How are codes/fobs distributed, changed, revoked? Who holds a copy now?** ________________________________________

**LO Codes Targeted:** 2.2.A, 2.2.C, 2.3.A

---

### 3. Tailgating Exposure (2.2.A)
| Finding | Likelihood | Impact | Treatment + Reasoning | Evidence |
|---------|------------|--------|----------------------|----------|
|         |            |        |                      |          |

**Count:** How many people enter behind one badgeholder/resident in 10 min at peak? ______  **What does the log record?** ______

**LO Codes Targeted:** 2.2.A, 2.4.A

---

### 4. Shoulder Surfing & Door Social Engineering (2.2.B, 2.2.C)
| Finding | Likelihood | Impact | Treatment + Reasoning | Evidence |
|---------|------------|--------|----------------------|----------|
|         |            |        |                      |          |
|         |            |        |                      |          |

**Propped door? Unverified "router repair"? Delivery held open?** ________________________________________

**LO Codes Targeted:** 2.2.B, 2.2.C

---

### 5. Cloning & Lock Picking (2.2.C)
| Finding | Likelihood | Impact | Treatment + Reasoning | Evidence |
|---------|------------|--------|----------------------|----------|
|         |            |        |                      |          |

**Proximity cards? Magnetic stripe? Tubular pin tumbler?** ________________________________________

**LO Codes Targeted:** 2.2.C

---

### 6. Surveillance (2.3.B)
| Finding | Likelihood | Impact | Treatment + Reasoning | Evidence |
|---------|------------|--------|----------------------|----------|
|         |            |        |                      |          |

**CCTV placement: entry or parking lot? Doorbell cam field of view?** ________________________________________

**LO Codes Targeted:** 2.3.B, 2.4.A

---

### 7. Environmental & Monitoring (2.3.C)
| Finding | Likelihood | Impact | Treatment + Reasoning | Evidence |
|---------|------------|--------|----------------------|----------|
|         |            |        |                      |          |
|         |            |        |                      |          |

**Lighting, signage, landscaping sightlines, fire doors wedged open, log nobody reviews** ________________________________________

**LO Codes Targeted:** 2.3.C, 2.4.A

---

### 8. Taiwan Addendum A — Shared Building Network Risk (2.4.B)
**One risk from shared building network infrastructure:** ________________________________________
_________________________________________________________________________________________

**Evidence that would reveal it:** ________________________________________
_________________________________________________________________________________________

*Accepted answers: single unmanaged building switch, flat VLAN no segmentation, management interface reachable from tenant Wi-Fi, shared Wi-Fi default/published key, unmonitored building firewall handoff*

---

### 9. Taiwan Addendum B — Typhoon/Flood Resilience Gap (2.3.C)
**One physical-resilience gap relevant to typhoon/flood:** ________________________________________
_________________________________________________________________________________________

**What it would break:** ________________________________________
_________________________________________________________________________________________

*Accepted answers: entry doors/lobby glass facing wind-driven rain, ground-floor equipment on the power, server/NAS shelf below floor level, no backup power for badge readers/network gear, single roof drain path, water ingress reaching power strip, loose exterior fixtures*

---

### 10. Risk & Treatment Summary (2.1.E, 2.1.F)
| Top 3 Findings | Inherent Risk (L×I) | Residual Risk (after control) | Treatment Decision + One-Sentence Reasoning |
|----------------|---------------------|-------------------------------|---------------------------------------------|
| 1.             |                     |                               |                                             |
| 2.             |                     |                               |                                             |
| 3.             |                     |                               |                                             |

---

**Standard:** Describe → Assess → Treat → Evidence. Four lines minimum per finding. Opinions without evidence = no credit.