# Capstone Demo Rubric — 3-Minute Presentation (35 pts)

**Student**: _________________________  
**Lab**: _________________________  
**Date**: Mar 31, 2027  
**Evaluator**: _________________________

---

## Scoring Breakdown

| Component | Weight | Points | Score |
|-----------|--------|--------|-------|
| 1. Problem Statement | 5 | 5 | ____ |
| 2. Threat Model Highlights | 5 | 5 | ____ |
| 3. Live Demonstration | 15 | 15 | ____ |
| 4. Code Walkthrough | 5 | 5 | ____ |
| 5. Q&A | 5 | 5 | ____ |
| **Total** | **100%** | **35** | **____** |

---

## Detailed Criteria

### 1. Problem Statement (5 pts) — ~30 seconds
| Level | Description | Points |
|-------|-------------|--------|
| **Exceeds** | Clear, concise, compelling. Explains *what* was extended, *why* it matters to security, and *who* benefits. Connects to real-world impact. | 5 |
| **Meets** | States what was extended and why. Context provided but could be sharper. | 4 |
| **Approaches** | Vague or incomplete. Missing "why it matters" or security relevance. | 2–3 |
| **Below** | Unclear what was done or why. No security context. | 0–1 |

**Key Elements to Cover**:
- Which Unit 5 lab was extended
- Specific feature/capability added
- Security problem it addresses
- One-sentence real-world relevance

---

### 2. Threat Model Highlights (5 pts) — ~30 seconds
| Level | Description | Points |
|-------|-------------|--------|
| **Exceeds** | Presents top 2 risks with STRIDE categories. Clearly links each risk to a specific mitigation in the implementation. Shows risk prioritization thinking. | 5 |
| **Meets** | Identifies 2 risks with mitigations. Connection to implementation clear. | 4 |
| **Approaches** | Lists risks but mitigations generic or missing. STRIDE categories not used. | 2–3 |
| **Below** | No threat model reference, or risks/mitigations don't match. | 0–1 |

**Key Elements to Cover**:
- Top 2 risks (by risk score)
- STRIDE category for each
- Specific mitigation implemented (not just "we fixed it")

---

### 3. Live Demonstration (15 pts) — ~90 seconds
| Level | Description | Points |
|-------|-------------|--------|
| **Exceeds** | Flawless demo. Shows core extension features working. Handles edge case or error gracefully. Visual/output clear. Timing perfect. | 14–15 |
| **Meets** | Core features work. Minor hiccup recovered quickly. Output visible. Within time. | 11–13 |
| **Approaches** | Partial demo. Major feature fails or not shown. Significant fumbling. Over/under time. | 6–10 |
| **Below** | Demo fails completely. No working features shown. | 0–5 |

**What to Demonstrate** (choose 2–3 key features):
- [ ] New functionality in action (API call, UI flow, CLI command)
- [ ] Security control working (block attack, validate input, enforce policy)
- [ ] Before/after comparison (vulnerable → mitigated)
- [ ] Test output showing coverage (pytest, curl, browser)
- [ ] Log/audit output showing detection

**Setup Requirements**:
- Codespaces ready *before* presentation slot
- Screen shared, terminal/editor visible
- Backup: recorded 60-sec video if live fails

---

### 4. Code Walkthrough (5 pts) — ~30 seconds
| Level | Description | Points |
|-------|-------------|--------|
| **Exceeds** | Highlights 1–2 key implementation decisions. Explains *why* chosen (security, performance, maintainability). References specific files/functions. | 5 |
| **Meets** | Shows key code. Explains what it does. Some reasoning provided. | 4 |
| **Approaches** | Scrolls through code without focus. Minimal explanation. | 2–3 |
| **Below** | No code shown, or cannot explain own code. | 0–1 |

**Suggested Focus Areas**:
- Input validation / sanitization function
- Authentication/authorization check
- Cryptographic implementation (key handling, encryption)
- Threat mitigation code (rate limiter, WAF rule, audit logger)
- Test case demonstrating security property

---

### 5. Q&A (5 pts) — ~1 minute
| Level | Description | Points |
|-------|-------------|--------|
| **Exceeds** | Answers confidently and accurately. Admits uncertainty honestly. Connects answers to threat model / course concepts. | 5 |
| **Meets** | Answers correctly. May need brief pause. Covers core concepts. | 4 |
| **Approaches** | Partial answers. Some confusion on concepts. | 2–3 |
| **Below** | Unable to answer basic questions about own work. | 0–1 |

**Common Questions**:
- "How would this scale to production?"
- "What happens if [mitigation] fails?"
- "How does this map to [Unit X LO]?"
- "What would you do with more time?"
- "How did you test [edge case]?"

---

## Timing Penalties

| Violation | Penalty |
|-----------|---------|
| Demo > 3:30 (hard stop at 4:00) | -3 pts |
| Demo < 2:00 | -2 pts |
| Not ready at assigned slot | -5 pts (reschedule to Apr 2) |
| No screen share / Codespaces not loaded | -5 pts |

---

## Light Option Adjustment

If student opted into Light Option (threat model + pseudocode + test plan):
- **Live Demonstration** → **Design Walkthrough** (15 pts): Walk through pseudocode, test plan, threat model
- **Code Walkthrough** → **Pseudocode Walkthrough** (5 pts): Explain key algorithms/logic
- Maximum demo score: 35 pts (same weight)
- Maximum total capstone: 60/100

---

## Evaluator Notes

______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________

**Final Score**: ____ / 35

**Evaluator Signature**: _________________________ **Date**: _______________