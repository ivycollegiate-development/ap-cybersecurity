# Portfolio Rubric — AP Cybersecurity Capstone

**ICA 2026-27** | **Total**: 100 pts | **Weight**: 20% of course grade (Projects category)

---

## Scoring Philosophy

This rubric evaluates the **capstone project portfolio** as a cohesive demonstration of cybersecurity competency. It is distinct from the capstone project implementation rubric (40 pts implementation + 25 pts threat model + 35 pts demo = 100 pts capstone). The portfolio packages the capstone for external audiences (college, employers) and adds reflection, presentation, and career-readiness dimensions.

**Portfolio completion + GitHub portfolio = 5% of Participation grade (5/25 pts)**

---

## Rubric Dimensions

| Dimension | Weight | Points | Description |
|-----------|--------|--------|-------------|
| **1. Threat Model Quality** | 20% | 20 pts | STRIDE completeness, mitigations mapped to code, residual risk documented |
| **2. Implementation Evidence** | 25% | 25 pts | Code quality, security controls, test coverage, CI/CD integration |
| **3. Documentation & Communication** | 20% | 20 pts | README, API docs, runbook, architecture diagrams, executive summary |
| **4. Presentation & Demo** | 15% | 15 pts | 3-min technical talk, live demo, Q&A handling, slide design |
| **5. Reflection & Growth** | 10% | 10 pts | Honest self-assessment, LO mapping, next steps, skills articulation |
| **6. Career Readiness** | 10% | 10 pts | GitHub profile polish, LinkedIn-ready artifacts, credential awareness |

---

## Detailed Scoring

### 1. Threat Model Quality (20 pts)

| Score | Criteria |
|-------|----------|
| **18-20 (Exemplary)** | Complete STRIDE across all trust boundaries; each threat → specific code mitigation; residual risks justified with business context; architecture diagram professional (draw.io/Mermaid); threat model versioned with code |
| **14-17 (Proficient)** | STRIDE covers major boundaries; most threats have mitigations; some residual risks undocumented; diagram clear but minor gaps; versioned |
| **10-13 (Developing)** | STRIDE incomplete (missing categories/boundaries); mitigations generic ("input validation"); residual risks not addressed; diagram missing or hand-drawn only |
| **0-9 (Beginning)** | No threat model or minimal (checklist only); no threat-to-code traceability; no diagram |

**Evidence**: `threat-model/stride-analysis.md`, `threat-model/mitigations.md`, `threat-model/architecture.drawio`

---

### 2. Implementation Evidence (25 pts)

| Score | Criteria |
|-------|----------|
| **23-25 (Exemplary)** | All planned features delivered; code follows secure patterns (parameterized queries, least privilege, fail-safe defaults); 90%+ test coverage (unit + integration + security); CI/CD with security gates (SAST, dependency scan, container scan); zero critical findings in CI |
| **18-22 (Proficient)** | Core features delivered; minor security pattern gaps; 75%+ test coverage; CI with basic security checks; <3 medium findings |
| **12-17 (Developing)** | Partial feature delivery; notable security anti-patterns (string concat SQL, hardcoded secrets); <60% coverage; CI missing security gates |
| **0-11 (Beginning)** | Minimal implementation; major vulnerabilities; no tests; no CI |

**Evidence**: `src/`, `tests/`, `.github/workflows/`, CI artifacts, dependency scan reports

---

### 3. Documentation & Communication (20 pts)

| Score | Criteria |
|-------|----------|
| **18-20 (Exemplary)** | README: problem, architecture, quickstart, API, deployment, contributing; API docs (OpenAPI/Swagger); runbook for ops; architecture diagram + data flow; executive summary for non-technical audience; all docs in repo, rendered |
| **14-17 (Proficient)** | README covers basics; API docs exist; runbook partial; diagrams present; executive summary adequate |
| **10-13 (Developing)** | README minimal; API docs missing or outdated; no runbook; diagrams incomplete |
| **0-9 (Beginning)** | No meaningful documentation; only code comments |

**Evidence**: `README.md`, `docs/api.md`, `docs/deployment.md`, `docs/runbook.md`, `demo/architecture.drawio`

---

### 4. Presentation & Demo (15 pts)

| Score | Criteria |
|-------|----------|
| **14-15 (Exemplary)** | 3-min talk: clear problem → approach → result; live demo works flawlessly; handles Q&A with depth; slides visual (not text-heavy); time management perfect |
| **11-13 (Proficient)** | Talk covers required elements; demo works with minor hiccups; Q&A adequate; slides functional; time ±30 sec |
| **7-10 (Developing)** | Talk missing elements; demo fragile or pre-recorded only; Q&A struggles; slides text-heavy; time off by >1 min |
| **0-6 (Beginning)** | No live demo; talk reads slides; cannot answer basic questions; over/under time significantly |

**Evidence**: `demo/demo.mp4`, `demo/slides.pdf`, live presentation (U6-L13)

---

### 5. Reflection & Growth (10 pts)

| Score | Criteria |
|-------|----------|
| **9-10 (Exemplary)** | Honest about failures; specific LO codes mapped to growth; concrete next steps (not "learn more"); articulates transferable skills; connects to career path |
| **7-8 (Proficient)** | Acknowledges challenges; LO mapping present; next steps somewhat vague; skills articulated |
| **5-6 (Developing)** | Surface-level reflection; LO mapping incomplete; next steps generic ("keep coding") |
| **0-4 (Beginning)** | No reflection or purely descriptive; no LO mapping; no next steps |

**Evidence**: Portfolio Section 6 (Reflection), Portfolio Section 8 (LO Mapping)

---

### 6. Career Readiness (10 pts)

| Score | Criteria |
|-------|----------|
| **9-10 (Exemplary)** | GitHub profile: pinned repos, bio, contribution graph; LinkedIn-ready project descriptions; cert/degree research documented (Portfolio-Template Section 7); tailored resume bullet points for this project |
| **7-8 (Proficient)** | GitHub profile functional; project descriptions clear; some career research; resume bullets drafted |
| **5-6 (Developing)** | GitHub bare minimum; project descriptions minimal; career research absent |
| **0-4 (Beginning)** | No GitHub profile polish; no career artifacts |

**Evidence**: GitHub profile, `Portfolio-Template.md` Section 7, resume bullets (U6-L04/L05 artifacts)

---

## Grade Boundaries

| Total Score | Letter | Proficiency | Participation Credit (5 pts) |
|-------------|--------|-------------|------------------------------|
| 90-100 | A | Exemplary | 5/5 (full) |
| 80-89 | B | Proficient | 4/5 |
| 70-79 | C | Developing | 3/5 |
| 60-69 | D | Beginning | 2/5 |
| <60 | F | Insufficient | 0/5 |

**Note**: Portfolio score is **formative** for Participation. Capstone project score (separate 100-pt rubric) determines the **Projects 20%** summative grade.

---

## Teacher Scoring Workflow (U6-L13)

1. **Pre-session** (May 26-27): Review GitHub repos, threat models, documentation
2. **Presentation day** (May 28): Score Dimensions 4 live, confirm 1-3, 5-6 from artifacts
3. **Post-session** (May 28-29): Finalize scores, write feedback, enter Participation points
4. **Feedback delivery**: Return scored rubric + written feedback via Google Classroom by Jun 2

---

## Calibration Anchors (for teacher consistency)

| Anchor | Description | Expected Score |
|--------|-------------|----------------|
| **Exemplary** | Student built custom WAF rules engine with 0 critical findings, 95% test coverage, professional docs, articulate 3-min talk, clear career plan | 92 |
| **Proficient** | Student extended Lab 3 (crypto) with key rotation, 80% coverage, good docs, demo works, knows next certs | 83 |
| **Developing** | Student did Light Option (threat model + pseudocode), partial implementation, basic docs, demo pre-recorded | 71 |
| **Beginning** | Minimal capstone, no threat model, broken demo, no reflection | 45 |

---

## Light Option Scoring (if applicable)

Students who declared Light Option (CAPSTONE_LIGHT_OPTION.md) are scored on adjusted scale:

| Dimension | Standard Weight | Light Option Weight |
|-----------|-----------------|---------------------|
| Threat Model | 20% | 35% |
| Implementation | 25% | 10% (pseudocode quality) |
| Documentation | 20% | 20% |
| Presentation | 15% | 15% |
| Reflection | 10% | 10% |
| Career Readiness | 10% | 10% |

**Max portfolio score for Light Option**: 60/100 → maps to Participation credit proportionally (max 3/5 pts)

---

*Rubric version 1.0 — Aligned with Capstone-Spec.md, CAPSTONE_LIGHT_OPTION.md, Course-Syllabus.md*