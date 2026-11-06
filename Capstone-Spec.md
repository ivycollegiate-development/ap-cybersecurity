# Capstone Project Specification — AP Cybersecurity (ICA 2026-27)

**Course**: AP Cybersecurity  
**Unit**: Capstone (Post-Unit 5)  
**Weight**: 20% of course grade (100 pts, Projects category)  
**Timeline**: 3 work days (Mar 29–31), Presentations Mar 31, Buffer Apr 2  
**Teacher Review Gate**: 3-day buffer after spec approval before Drive upload

---

## Overview

Extend **ONE** Unit 5 lab to demonstrate applied cybersecurity skills. You will:
1. Select a lab and define a meaningful extension
2. Create a threat model for your extension
3. Implement the extension (or submit Light Option deliverables)
4. Present a 3-minute demo on Mar 31

---

## Unit 5 Lab Options (Choose ONE)

| Lab | Repo (ivycollegiate-development) | Core Topic | Extension Ideas |
|-----|----------------------------------|------------|-----------------|
| **5.1** | `ap-cyber-u5-l1-juice-shop-recon` | Recon/OSINT, App Vulns | Automate recon pipeline; add auth bypass testing; integrate with CI |
| **5.2** | `ap-cyber-u5-l2-access-control` | Managerial & Access Controls | Implement RuBAC/ABAC policies; add audit logging; simulate insider threat |
| **5.3** | `ap-cyber-u5-l3-symmetric-crypto` | Symmetric Encryption | Build file encryption tool; add key rotation; implement authenticated encryption |
| **5.4** | `ap-cyber-u5-l4-pki-simulation` | PKI & Digital Signatures | Create mini-CA; automate cert lifecycle; add OCSP/CRL checking |
| **5.5** | `ap-cyber-u5-l5-waf-secure-coding` | WAF, Secure Coding, Log Analysis | Custom WAF rules; SAST integration; anomaly detection in logs |

**All 5 repos have pre-built starter branches with TODOs — tested in Codespaces by Mar 24.**

---

## Deliverables (Due Mar 31, 8:00 AM)

### Required for All Students
1. **Threat Model Document** (`THREAT_MODEL.md`) — 25 pts
2. **Implementation** (code in lab repo, `capstone/` branch) — 40 pts
3. **3-Minute Demo** (live in class Mar 31) — 35 pts

### Light Option (if implementation fails)
If your lab fails Codespaces readiness check or you cannot complete implementation:
- Submit **detailed threat model** + **pseudocode** + **test plan** — 60/100 pts max
- Still present 3-min demo (walk through threat model & design)
- Must notify teacher by **Mar 26** to opt into Light Option

---

## Threat Model Requirements (25 pts)

Use the **STRIDE** framework. Document must include:

| Section | Requirements | Points |
|---------|--------------|--------|
| **System Overview** | Architecture diagram (ASCII/text), data flows, trust boundaries | 5 |
| **Asset Inventory** | Data assets, components, external dependencies | 3 |
| **STRIDE Analysis** | Table with Threat, STRIDE category, Likelihood (H/M/L), Impact (H/M/L), Mitigation | 12 |
| **Risk Prioritization** | Top 3 risks with justification, residual risk after mitigations | 5 |

**Template**: See `THREAT_MODEL_TEMPLATE.md` (provided)

---

## Implementation Requirements (40 pts)

| Criterion | Exceeds (40) | Meets (30) | Approaches (20) | Below (10) |
|-----------|--------------|------------|-----------------|------------|
| **Functionality** | Extension works fully; handles edge cases | Core features work; minor bugs | Partial implementation; major gaps | Minimal/no working code |
| **Code Quality** | Clean, modular, documented, follows style guide | Readable; some docs; minor style issues | Inconsistent; sparse comments | Disorganized; no comments |
| **Security Practices** | Input validation, least privilege, secure defaults, no hardcoded secrets | Basic validation; no obvious flaws | Some validation gaps | Significant vulnerabilities |
| **Testing** | Unit + integration tests; CI passing; coverage >80% | Basic tests; CI passing | Few tests; CI issues | No tests |
| **Git Hygiene** | Logical commits, clear messages, `capstone/` branch, PR-ready | Clean history; branch used | Messy commits; branch issues | No branch; commit to main |

---

## Demo Requirements (35 pts)

**Format**: 3 minutes live demo + 1 min Q&A (strict timing)

| Component | Points | Details |
|-----------|--------|---------|
| **Problem Statement** | 5 | What you extended, why it matters (30 sec) |
| **Threat Model Highlights** | 5 | Top 2 risks + mitigations (30 sec) |
| **Live Demonstration** | 15 | Working extension; show key features (90 sec) |
| **Code Walkthrough** | 5 | Key implementation decisions (30 sec) |
| **Q&A** | 5 | Answer questions on design, security, testing | |

**Demo Day**: Mar 31, during class. Order randomized. Screen share from Codespaces or local.

---

## Rubric Summary (100 pts)

| Component | Weight | Points |
|-----------|--------|--------|
| Threat Model | 25% | 25 |
| Implementation | 40% | 40 |
| Demo & Communication | 35% | 35 |
| **Total** | **100%** | **100** |

**Course Grade Impact**: 100 pts → 20% of 500 pts total (Projects category)

---

## Milestones & Checkpoints

| Date | Milestone |
|------|-----------|
| **Mar 24** | Lab readiness confirmed (all 5 repos tested in Codespaces) |
| **Mar 26** | Light Option declaration deadline (if needed) |
| **Mar 29** | Work Day 1: Threat model draft + repo setup |
| **Mar 30** | Work Day 2: Implementation + testing |
| **Mar 31** | Work Day 3 (AM): Finalize + rehearse demo |
| **Mar 31** | **Presentations (class time)** |
| **Apr 2** | Buffer day (late submissions, makeups) |
| **Apr 3** | Teacher grading complete |

---

## Scaffolding Provided (by Mar 24)

Each lab repo will have a `capstone-starter/` branch with:

```
capstone-starter/
├── TODO.md              # Extension requirements checklist
├── THREAT_MODEL_TEMPLATE.md
├── src/
│   └── stubs/           # Pre-built function/class stubs with docstrings
├── tests/
│   └── test_stubs.py    # Test scaffolding (pytest)
├── .github/
│   └── workflows/
│       └── ci.yml       # CI pipeline (lint, test, security scan)
└── README_CAPSTONE.md   # Lab-specific extension guidance
```

**Languages**: Python (primary), JavaScript/TypeScript (Juice Shop lab)

---

## Academic Integrity

- Work must be your own. Collaboration allowed on threat modeling discussions only.
- Code must be written during the 3 work days (Mar 29–31).
- Pre-existing code: only the provided `capstone-starter/` stubs.
- Cite any external libraries/sources in `THREAT_MODEL.md`.
- Violations → 0 on capstone + referral per ICA policy.

---

## Backup Option: Mini-Juice-Shop

If **all 5 labs fail** Codespaces readiness by Mar 24:
- Teacher provides `mini-juice-shop` repo (3 pre-seeded vulns: SQLi, XSS, broken auth)
- Same deliverables, same timeline, same rubric
- Announced Mar 24 if triggered

---

## Questions?

- Lab selection: Confirm with teacher by Mar 26
- Technical issues: Post in #ap-cyber-capstone Slack/GitHub Discussions
- Light Option: Email teacher by Mar 26

---

*Spec version 1.0 — Aligned to Course Curriculum Framework Units 5.1–5.6, Skills 1.A–3.D*