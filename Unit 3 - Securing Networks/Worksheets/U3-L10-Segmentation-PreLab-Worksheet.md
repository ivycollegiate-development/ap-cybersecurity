# U3 L10: Pre-Lab — Network Segmentation Sim Prep Worksheet

**Date:** Nov 27 (Fri) — TECH DAY (pre-lab on paper, lab on computer)
**Prepares for:** U3 L10 GitHub Lab: Network Segmentation Sim (same period)

---

## Instructions
Complete this worksheet **before** starting the lab. Review VLAN concepts from pre-reading. Submit at end of class.

---

## Section 1: VLAN Concepts Review (Pre-Reading Check)

| Concept | Definition | Key Detail |
|---------|------------|------------|
| VLAN | | |
| VLAN ID Range | | 1–4094 |
| Default VLAN | | VLAN 1 (cannot be deleted) |
| Access Port | | |
| Trunk Port | | |
| Inter-VLAN Routing | | Requires Layer 3 device (router/firewall) |
| Native VLAN | | Untagged traffic on trunk |

---

## Section 2: Segmentation Design Predictions

**The lab asks you to design a network for a small business. Predict the answers before you start.**

### Business Requirements:
- Web server (public)
- Email server (public)
- Internal file server (private)
- 20 employee PCs
- 10 IoT cameras
- Guest Wi-Fi

### Your Predictions:

| Segment | VLAN ID | Purpose | Should It Have Internet Access? |
|---------|---------|---------|----------------------------------|
| DMZ | | Public-facing servers | Yes (restricted) |
| Staff | | Employee PCs | Yes (via firewall) |
| Guest | | Visitor Wi-Fi | Yes (captive portal only) |
| IoT | | Cameras/sensors | **NO** (critical) |
| Management | | Switch/firewall mgmt | No (out-of-band) |

**Why must the IoT VLAN have NO internet route? (Connect to CISA water-system hack fix):**

---

## Section 3: Lab Checklist (Use During Lab)

**Check off each step as you complete it in the Codespaces simulator.**

- [ ] Fork repo → Codespaces launches
- [ ] Create VLAN 10 (Staff) — access ports for employee PCs
- [ ] Create VLAN 20 (Students/Guest) — access ports for guest Wi-Fi
- [ ] Create DMZ VLAN — place web server + email server
- [ ] Verify same-VLAN traffic flows (ping test)
- [ ] Verify cross-VLAN traffic blocked (ping test)
- [ ] Add inter-VLAN routing through firewall
- [ ] Configure firewall rules: allow DMZ→internet (80/443), block DMZ→internal
- [ ] Configure firewall rules: allow Staff→DMZ (80/443), block Staff→IoT
- [ ] Configure firewall rules: block Guest→all internal VLANs
- [ ] Block IoT VLAN from internet (critical — CISA fix)
- [ ] Capture screenshots as evidence for each verification
- [ ] Submit via GitHub Classroom

---

## Section 4: Homework Questions (Due Sun 20:30 — Monday Quiz)

**Answer in 2–3 sentences each.**

1. **What happens to broadcast traffic when you segment a network with VLANs?**

2. **Why is it critical to protect IoT devices in their own VLAN with NO internet route?**

3. **In the lab, you placed the web server and email server in a DMZ. Why not put them in the Staff VLAN?**

---

## Section 5: Vocab Flashcard Set 3 Reminder

**Terms from U3 L6 (Risk Assessment) — review for Monday's quiz:**
- likelihood
- impact
- risk matrix
- risk register
- mitigation
- residual risk
- risk appetite
- qualitative vs quantitative assessment