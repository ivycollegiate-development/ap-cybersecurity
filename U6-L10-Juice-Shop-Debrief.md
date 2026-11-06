# U6-L10: OWASP Juice Shop Debrief Prep

**AP Cybersecurity — ICA 2026-27**  
**Date**: May 19, 2027 (Wed) | **Period**: 131 | **Duration**: 50 min  
**Type**: Skill Reinforcement | **Format**: Lab Walkthrough + Portfolio Artifact

---

## Learning Objectives

By the end of this lesson, students will be able to:
1. **Reconstruct** the OWASP Juice Shop vulnerabilities exploited in capstone Lab 1
2. **Map** each vulnerability to OWASP Top 10 2021 categories and CWE IDs
3. **Document** fix verification with before/after evidence for portfolio
4. **Connect** Juice Shop findings to capstone threat model (Lab 1 extension)

---

## Prerequisites

- Capstone Lab 1 (Juice Shop) completed — threat model + extension implemented
- Unit 5 LO 5.1 (OWASP Top 10), LO 5.5 (WAF/Secure Coding)
- Juice Shop instance accessible (Codespaces or local Docker)
- Capstone Lab 1 repo with fixes

---

## Materials

- OWASP Juice Shop running instance (per student or shared)
- Capstone Lab 1 threat model (`threat-model/stride-analysis.md`)
- Vulnerability documentation template (portfolio `ctf/juice-shop-debrief.md`)
- OWASP Top 10 2021 / CWE mapping reference

---

## Lesson Flow

| Time | Activity | Details |
|------|----------|---------|
| 0-5 | **Context** | "Juice Shop is the *intentionally vulnerable* app. Your capstone extended it. Now: prove you understand *why* each vuln existed and *how* your fix works. This = interview gold." |
| 5-20 | **Guided Walkthrough: Top 5 Juice Shop Vulns** (15 min) | Teacher demonstrates (students follow in Codespaces):<br>1. **A03:2021 Injection** — SQLi in login (`' OR 1=1--`) → CWE-89<br>2. **A01:2021 Broken Access Control** — IDOR in `/rest/user/orders` → CWE-639<br>3. **A04:2021 Insecure Design** — Missing rate limit on password reset → CWE-307<br>4. **A05:2021 Security Misconfiguration** — Exposed `/api/Users` with admin hash → CWE-200<br>5. **A06:2021 Vulnerable Components** — Outdated `sanitize-html` → CWE-1104<br><br>For each: **Reproduce** → **Identify root cause** → **Show capstone fix** → **Verify fix fails exploit** |
| 20-35 | **Student Documentation** (15 min) | Students complete `juice-shop-debrief.md` in portfolio `ctf/`:<br>```markdown<br># Juice Shop Vulnerability Debrief<br>## Vulnerabilities Exploited (Capstone Lab 1)<br>| # | OWASP Cat | CWE | Endpoint | Payload | Root Cause | Capstone Fix | Verification |<br>|---|---|---|---|---|---|---|---|<br>| 1 | A03 | CWE-89 | /rest/user/login | ' OR 1=1-- | String concat | Parameterized query | Unit test + SAST clean |<br>...<br>## Threat Model Traceability<br>[Link each fix to STRIDE threat ID from capstone threat model]<br>## WAF Rules Added<br>[ModSecurity rules from capstone Lab 5 extension]<br>## Lessons for Portfolio<br>[What this teaches about secure SDLC — for interviews] | |
| 35-45 | **Fix Verification Lab** (10 min) | Students run verification in Codespaces:<br>1. `npm test` — capstone unit tests pass<br>2. `npm run sast` — Semgrep/Bandit: 0 critical findings<br>3. `docker run -t owasp/juice-shop` + `zap-baseline.py` — ZAP scan: previous vulns gone<br>4. Screenshot results → add to `juice-shop-debrief.md` |
| 45-50 | **Commit & Connect** | `git add ctf/juice-shop-debrief.md && git commit -m "Add Juice Shop debrief with fix verification" && git push`<br>Exit: "One Juice Shop vuln you *didn't* fix — why? Scope? Time? Complexity?" |

---

## Teacher Notes

- **Juice Shop version**: Use v15.x (current stable) — matches capstone Lab 1 baseline
- **Codespaces**: Pre-load Juice Shop in devcontainer or provide `docker-compose.yml`
- **Capstone Lab 1 extension**: Should have addressed at least 3 of the above; Light Option = threat model only
- **Portfolio value**: This artifact shows: vuln knowledge + fix implementation + verification + threat modeling traceability

---

## Differentiation

| Need | Adjustment |
|------|------------|
| Lab 1 Not Chosen | Use Lab 1 as case study; apply same template to chosen lab (Lab 2-5) |
| Light Option | Document threat model findings for Juice Shop; pseudocode fixes; no verification |
| Advanced | Add: "Create custom Semgrep rule for one vuln pattern" or "Write Nuclei template" |

---

## Assessment

**Formative**: `juice-shop-debrief.md` committed — teacher checks: OWASP/CWE mapping accuracy, fix traceability to threat model, verification evidence.

---

## Homework / Next Steps

- **Polish**: `juice-shop-debrief.md` — ensure all capstone Lab 1 fixes documented — due U6-L11
- **Portfolio**: Continue Sections 5, 6, 7 — due U6-L11 (May 26)
- **Practice**: 3-min talk — incorporate Juice Shop story — U6-L13 (May 28)
- **Read**: Portfolio-Rubric.md Dimension 2 (Implementation Evidence) — self-score Juice Shop section

---

*U6-L10 — OWASP Juice Shop Debrief Prep — May 19, 2027*