# U3 L19: Synthesis + Current Event — Build Your Own Network Defense Plan

**Date:** Dec 10 (Thu) — PAPER DAY
**Synthesizes:** 3.1–3.5 | **Current Event:** Teacher-selected recent incident (printed)

---

## Instructions
Work in groups of 3–4. Design a defense-in-depth network for the scenario below. Document with a network diagram + defense rationale. Swap with another group for critique. Then analyze the current event article.

---

## Part 1: Scenario — Ecosoft Electronics (Hsinchu Science Park)

> **You are the IT security team for Ecosoft Electronics, a 50-person embedded-chip company in Hsinchu Science Park.**
>
> **Assets:**
> - 40 workstations (engineering + admin)
> - 1 web server (public-facing, customer portal)
> - 1 internal file server (R&D — **most sensitive**, chip designs)
> - 1 dev server (CI/CD, build artifacts)
> - 20 IoT sensors on factory floor (environmental monitoring)
> - Guest Wi-Fi (visitors, vendors)
>
> **Budget:** One managed switch, one firewall/NGFW, one wireless AP.
>
> **Design a defense-in-depth network.**

---

## Part 2: Design Phase (15 min)

### A. VLAN Segmentation with Justification

| VLAN ID | Name | Assets Placed Here | Justification (CED LO) |
|---------|------|-------------------|------------------------|
| 10 | | | |
| 20 | | | |
| 30 | | | |
| 40 | | | |
| 50 | | | |

**DMZ Placement:** Which server(s) go in the DMZ? Why?

**Zero Trust Principle Applied:** How does your design implement "never trust, always verify"?

---

### B. Firewall ACLs Between Segments

**List key firewall rules (source → destination, port, action, logging). Order matters — specific first.**

| # | Source | Destination | Port/Protocol | Action | Log? | Purpose |
|---|--------|-------------|---------------|--------|------|---------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | (Implicit Deny) | Any | Any | Any | Deny | Yes | Default deny |

---

### C. Wireless Security Configuration

| Setting | Value | CED LO Reference |
|---------|-------|------------------|
| Encryption | | 3.2.C |
| Authentication | | 3.2.C |
| SSID Broadcast | | 3.2.C |
| Guest Network Isolation | | 3.2.A |
| RADIUS / 802.1X | | 3.2.C |

---

### D. NIDS Placement

**Where do you place NIDS sensors? (Check all that apply)**
- [ ] Internet ↔ Firewall (WAN side)
- [ ] Firewall ↔ DMZ
- [ ] Firewall ↔ Internal VLANs
- [ ] Switch SPAN port on core switch
- [ ] Other: _______________

**What traffic patterns will each sensor monitor?**

---

### E. Managerial Controls

| Control | Description | CED LO |
|---------|-------------|--------|
| Acceptable Use Policy (key points) | | 3.2.A |
| Guest Network Policy | | 3.2.A |
| Incident Response Trigger (NIDS alert → action) | | 3.5.B |

---

## Part 3: Network Diagram (Sketch or Describe)

```
[Draw your network diagram here — include:
- Internet
- Firewall/NGFW
- Managed Switch
- Wireless AP
- VLANs (10, 20, 30, 40, 50)
- DMZ
- All 6 asset groups
- NIDS sensor locations
- Traffic flow arrows with port numbers]
```

---

## Part 4: Defense Rationale (3–4 sentences per pillar)

**VLAN Segmentation:**

**Firewall Rules:**

**Wireless Security:**

**NIDS Placement & SIEM Correlation:**

**Managerial Controls:**

---

## Part 5: Pair-Critique (10 min)

**Swap with another group. Identify at least 3 weaknesses or missing controls.**

| Weakness / Missing Control | Why It Matters | Suggested Fix |
|----------------------------|----------------|---------------|
| 1. | | |
| 2. | | |
| 3. | | |

**Critiquer Names:** _________________________________

---

## Part 6: Current Event Analysis (10 min)

**Article Title:** _________________________________
**Source/Date:** _________________________________

### Map to CED Framework

| Stage | What Happened in the Incident | CED Topic |
|-------|-------------------------------|-----------|
| Vulnerability | | |
| Exploit | | |
| Impact | | |

### Which Ecosoft Controls Would Have Stopped This?

| Ecosoft Control | Would It Help? (Yes/Partial/No) | Explanation |
|-----------------|----------------------------------|-------------|
| VLAN Segmentation | | |
| Firewall ACLs | | |
| Wireless Security | | |
| NIDS/SIEM | | |
| Managerial Controls | | |

---

## Homework (Due 20:30)

**Revise your design based on peer feedback.** Submit revised diagram + rationale tomorrow.

**Tomorrow (Dec 11):** U3 L20 GitHub Lab: Network Scanning Detection Lab — final lab of Unit 3.