# AP Cybersecurity — Course Materials

**🇹🇼 Taiwan-context convention (approved Aug 26, 2026):** roughly 1-in-3 🎯 Cyber Attack of the Day warm-ups should feature Taiwan-relevant incidents (government agency attacks, semiconductor-sector targeting, Chinese-language phishing campaigns). Bias recurring current-events selections the same way.

> **Canonical source of truth (since Aug 23, 2026).** The AP Cybersecurity
> markdown masters live in this private repo. Version-controlled via git.
> Production surfaces — the syllabus gdoc/PDF, per-unit "Detailed Lesson
> Plans" Google Docs, worksheet GDocs, .docx twins, answer keys — are generated
> FROM these files and live in the school Drive under
> `2026 Fall Semester/AP_Cybersecurity/`.
> To regenerate a Google Doc from a unit's .md, use
> `scripts/rebuild-md-gdoc.py` from the `ap-cyber-curriculum` skill.

## Folder Structure

```
ap-cybersecurity/                  # THIS REPO (was AP_Cybersecurity/ on Drive)
├── README.md                      # This navigation map
├── Pacing-Calendar.md             # Full-year date-by-date schedule (source of truth)
├── Unit 1 - Introduction to Security/
│   ├── Unit-1-Lesson-Plans.md     # 18 periods (12 tech + 3 paper + 3 study-hall), 5 topics, 3 GitHub labs, test
│   └── Worksheets/                # Unit 1 worksheet .md sources (P4-P14)
├── Unit 2 - Securing Spaces/
│   └── Unit-2-Lesson-Plans.md
├── Unit 3 - Securing Networks/
│   └── Unit-3-Lesson-Plans.md
├── Unit 4 - Securing Devices/
│   └── Unit-4-Lesson-Plans.md
└── Unit 5 - Securing Applications and Data/
    ├── Unit-5-Lesson-Plans.md
    └── Cold-Card-Case-Study-Worksheet.md
```

**Not in this repo (stay on Drive as Google-native files):** syllabus gdoc/PDF,
CED PDF, `Pacing Guides/*.xlsx`, lesson-plan .docx twins, worksheet/rubric GDocs,
answer-key GDocs, "Detailed Lesson Plans" review gdocs.

## Quick Reference

| Unit | Topics | Periods | Status |
|------|--------|---------|--------|
| 1 — Introduction to Security | 1.1-1.5 (5) | 18 (15 APSI + 3 study-hall) | Done |
| 2 — Securing Spaces | 2.1-2.4 (4) | 23 + test week | Done |
| 3 — Securing Networks | 3.1-3.5 (5) | 20 (compressed) | Done |
| 4 — Securing Devices | 4.1-4.4 (4) | 23 | Done |
| 5 — Securing Applications & Data | 5.1-5.6 (6) | 30 | Done |

**Total: ~119 instructional periods** (vs CED 110 recommended). CED-aligned, with break assignments and course-wide review.

## Course Model

- **Tech days (Mon/Wed/Fri):** Direct instruction + GitHub labs in Codespaces
- **Paper days (Tue/Thu):** No computers — case studies, peer review, FRQ walk-throughs, pre-lab prep, sprints, synthesis
- **⚡ Graded HW Quiz:** every class period opens with a 5-10 min quiz on prev night HW (due 20:30)
- **📝 Unit Tests:** Units 1-5, paper-based, ~45 min
- **🧘 Study-Hall/Prep (Unit 1 only):** 3 Tue/Thu slots — quick review + student work time on upcoming due assignments
- **Break assignments** at every natural boundary (Fall Break, Winter Break, CNY, Spring Break)

## Assessment Map

| Type | What | When | Weight |
|------|------|------|--------|
| **Unit tests (📝)** | 5 paper-based tests, ~45 min | End of each unit | Quizzes/Assessments 25% |
| **⚡ HW quizzes** | 5-10 min graded quiz every class | Daily, opens each class | Quizzes/Assessments 25% |
| **GitHub labs** | Auto-graded via Classroom + Actions | 3-5 labs per unit | Labs 30% |
| **Capstone project** | Multi-day project | Unit 5 tail (Mar 23-31) | Projects 20% |
| **Full practice exam** | Timed, self-keyed over Spring Break | Apr 1 (before break) | Diagnostic for AP review |
| **Midterm** | School-wide exam | Jan | 10% | (no school final — AP exam May 5, 2027) |
| **Formative** | Exit tickets, Mock MCQ Sprints, FRQ walk-throughs, peer review, pre-lab worksheets | Throughout | Ungraded feedback |

## Unit 1 Lab Needs (low-infrastructure — no VMs required)

| Lab | Repo | Tools |
|-----|------|-------|
| Phishing Classification (P2) | `apcyber-u1-phishing-samples` | Codespaces, GitHub Issues |
| Password Strength Analyzer (P6) | `apcyber-u1-password-strength-lab` | Codespaces, cracker script, GitHub Actions |
| AI-Powered Code Review (P14) | `apcyber-u1-vulnerable-code-lab` | Codespaces, CodeQL, AI tool (Claude/ChatGPT) |

## Source Materials

- **CED** (official): `ap-cybersecurity-course-and-exam-description.pdf` (192 pages)
- **APSI Pacing Guides:** Desktop/APSI/ (authoritative period-by-period structure)
- **ICA Calendar:** Term 1 Aug 31, Fall Break Oct 30, Term 2 Nov 9, Winter Break Dec 18, Term 3 Jan 4, CNY Feb 3-14, Spring Break Apr 2, Review Apr 12, AP exam Wed May 5, 2027

## GitHub

Org: `ivycollegiate-development`. All labs use GitHub Classroom + Codespaces + Actions for auto-validation. Student workflow: fork → Codespaces → commit → PR → auto-grade.
