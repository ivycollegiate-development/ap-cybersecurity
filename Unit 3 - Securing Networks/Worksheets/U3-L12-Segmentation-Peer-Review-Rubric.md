# U3 L12: Peer Review — Segmentation Findings Rubric

**Date:** Dec 1 (Tue) — PAPER DAY
**Reviews:** U3 L10 GitHub Lab: Network Segmentation Sim (Nov 27)

---

## Instructions
Swap your Friday lab report with a partner. Evaluate their work using this rubric. Write one "glow" (strength) and one "grow" (area for improvement). Submit completed rubric with both names.

---

## Reviewer Info

| Field | Your Info |
|-------|-----------|
| **Your Name** | |
| **Partner's Name** | |
| **Date** | Dec 1 |

---

## Rubric: Segmentation Lab Report Evaluation

### Section 1: Completeness (All Required Segments Present?)

| Criterion | Yes / Partial / No | Evidence in Report |
|-----------|---------------------|---------------------|
| VLAN 10 (Staff) created | | |
| VLAN 20 (Students) created | | |
| DMZ with web server + email server | | |
| Guest VLAN isolated from internal file server | | |
| IoT camera VLAN (extension) | | |
| Water utility OT VLAN (extension) | | |

**Completeness Score: ____ / 6**

---

### Section 2: Evidence Quality (Screenshots + Reasoning)

| Criterion | Yes / Partial / No | Notes |
|-----------|---------------------|-------|
| Screenshots show VLAN configuration | | |
| Screenshots show firewall rules between segments | | |
| Screenshots verify same-VLAN traffic flows | | |
| Screenshots verify cross-VLAN traffic blocked | | |
| Screenshots show inter-VLAN routing through firewall | | |
| Each screenshot has a caption explaining what it proves | | |

**Evidence Score: ____ / 6**

---

### Section 3: Security Soundness (Blast Radius Limited?)

| Criterion | Yes / Partial / No | Explanation |
|-----------|---------------------|-------------|
| Guest VLAN cannot reach internal file server | | |
| IoT cameras in own VLAN (no internet route) | | |
| DMZ servers accessible from internet but not internal network | | |
| Staff/Student VLANs separated (no direct access) | | |
| Water utility OT VLAN has NO internet route (CISA fix) | | |
| Design follows least-privilege principle | | |

**Security Score: ____ / 6**

---

### Section 4: Executive Summary (3-Sentence Requirement)

| Criterion | Yes / No | Notes |
|-----------|----------|-------|
| Exactly 3 sentences | | |
| Addresses ICA IT audience | | |
| Identifies top 2–3 segmentation priorities | | |
| Uses correct terminology (VLAN, DMZ, blast radius, least privilege) | | |

**Executive Summary Score: ____ / 4**

---

## Glow & Grow (Required)

### Glow (What they did well — be specific):

### Grow (One concrete improvement — be specific):

---

## Overall Assessment

**Total Score: ____ / 22**

**Would this segmentation design effectively protect ICA's network?**
- [ ] Yes, with minor tweaks
- [ ] Mostly, but has significant gaps
- [ ] No, major redesign needed

**Reviewer Signature:** _________________________

**Partner Signature (acknowledging feedback):** _________________________

---

## Homework (Due 20:30)

1. **Revise your lab report** based on peer feedback. Resubmit via GitHub Classroom if changes are substantial.
2. **Read CED excerpt on 3.3 Zero Trust** (1 page — provided separately).
3. **Prep for U3 L13:** Tomorrow we'll apply Zero Trust principles to the school network diagram from U3 L11.