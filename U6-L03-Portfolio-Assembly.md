# U6-L03: Portfolio Assembly — What a Cybersecurity Portfolio Actually Is

**AP Cybersecurity — ICA 2026-27**  
**Date**: May 10, 2027 (Mon) | **Period**: 124 | **Duration**: 50 min  
**Type**: Portfolio Build | **Format**: Workshop + GitHub Setup

---

## Learning Objectives

By the end of this lesson, students will be able to:
1. **Define** the components of a hireable cybersecurity portfolio
2. **Initialize** a professional GitHub profile and portfolio repository
3. **Structure** capstone project for external audiences (employers, admissions)
4. **Begin** populating Portfolio-Template.md with capstone evidence

---

## Prerequisites

- Capstone project completed (Mar 31 presentation done)
- GitHub account (ivycollegiate-development org access)
- `Portfolio-Template.md` read (Sections 1-3, 7-8)
- Capstone repo URL, threat model files, demo recording

---

## Materials

- `Portfolio-Template.md` (reference)
- `Portfolio-Rubric.md` (scoring guide)
- GitHub profile checklist (handout)
- Example portfolio repos (teacher-curated list)

---

## Lesson Flow

| Time | Activity | Details |
|------|----------|---------|
| 0-5 | **Why Portfolio?** | "Your capstone proved you can *do* the work. Your portfolio proves you can *communicate* it. Employers spend 30 sec scanning GitHub." Show 2 examples: strong vs weak. |
| 5-15 | **GitHub Profile Polish** (10 min) | Students update live:<br>1. **Profile README** (`github.com/username/username`) — bio, skills, certs target, capstone link<br>2. **Pinned repos** — capstone + 2 best (CTF writeup, tool, lab extension)<br>3. **Bio** — "Aspiring [Role] | AP Cybersecurity Capstone: [Project] | Security+ (target Oct 2027)"<br>4. **Social links** — LinkedIn, portfolio site if any |
| 15-30 | **Portfolio Repo Creation** (15 min) | Create `username-portfolio` repo (public):<br>1. `README.md` ← Portfolio-Template.md Section 1 (Executive Summary) + badges<br>2. `PORTFOLIO.md` ← Full Portfolio-Template.md (to fill progressively)<br>3. `threat-model/` ← Copy from capstone repo<br>4. `demo/` ← Demo recording, slides<br>5. `ctf/` ← CTF Session 6 analysis (from U6-L02)<br>6. `docs/` ← API docs, runbook, architecture diagrams<br>7. `.github/workflows/portfolio.yml` — CI: markdown lint, link check |
| 30-40 | **Capstone Integration** (10 min) | Students copy/paste into `PORTFOLIO.md`:<br>- Threat model summary (Section 2)<br>- Implementation table (Section 3.2)<br>- Security controls table (Section 3.3)<br>- Test results summary (Section 4)<br>- LO mapping (Section 8) — use Course Curriculum Framework |
| 40-45 | **Peer Quick-Review** (5 min) | Swap repos with partner. Check: repo public? README renders? Capstone link works? Threat model folder exists? |
| 45-50 | **Commit & Push** | `git add . && git commit -m "Init portfolio with capstone" && git push`<br>Teacher verifies: all repos accessible, PORTFOLIO.md has content |

---

## Teacher Notes

- **GitHub org**: Students use personal accounts (not ivycollegiate-development) for portfolio
- **Privacy**: Repos must be public for portfolio value — confirm no secrets in capstone code
- **Time pressure**: This is setup only; content filling continues U6-L07, U6-L11
- **Rubric reference**: Portfolio-Rubric.md Dimensions 3 (Documentation) and 6 (Career Readiness)

---

## Differentiation

| Need | Adjustment |
|------|------------|
| Git Novice | Pre-made repo template (GitHub template repo); teacher assists with push |
| Advanced | Add: GitHub Pages deployment for portfolio site; custom domain |
| No Capstone (Light Option) | Use threat model + pseudocode + test plan as "project" — same structure |

---

## Assessment

**Formative**: Portfolio repo URL submitted via Classroom — teacher checks: public, README, PORTFOLIO.md started, threat-model/ folder present.

---

## Homework / Next Steps

- **Complete**: Portfolio-Template.md Sections 1, 2, 3, 8 in PORTFOLIO.md — due U6-L07 (May 14)
- **Read**: Career-Path-Research.md Parts 1-3 (Roles, Certs, Education) — due U6-L04 (May 11)
- **Polish**: GitHub profile (bio, pinned, README) — due U6-L04

---

*U6-L03 — Portfolio Assembly — May 10, 2027*