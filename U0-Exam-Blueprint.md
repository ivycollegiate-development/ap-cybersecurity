# U0-Exam-Blueprint.md — AP Cybersecurity Practice Exam Blueprint

**Course**: AP Cybersecurity (ICA 2026-27)  
**Source**: Course Curriculum Framework (derived from College Board CED, Effective Fall 2026)  
**Exam Date**: April 1, 2027 (in-class administration)  
**Self-Scoring Window**: April 2–11, 2027 (Spring Break)  
**Error Analysis Due**: April 11, 2027  
**Format**: Matches official AP Cybersecurity Exam exactly

---

## Exam Structure (Official Format)

| Section | Questions | Weight | Time | Format |
|---------|-----------|--------|------|--------|
| I: Multiple-Choice | 60 | 70% | 80 min | 40 single-select + 20 multi-select |
| II: Free-Response | 1 (5 parts) | 30% | 50 min | Device Security Analysis performance task |
| **Total** | **61 items** | **100%** | **130 min** | |

---

## Section I: Multiple-Choice (60 Questions, 80 min)

### Unit Distribution (Validated Against CED)

| Unit | Topics | MCQ Count | % of MC | Skill Category Focus |
|------|--------|-----------|---------|---------------------|
| 1: Introduction to Security | 1.1–1.5 | 6 | 10% | 1 (Analyze Risk) |
| 2: Securing Spaces | 2.1–2.4 | 13 | 22% | 1, 2 |
| 3: Securing Networks | 3.1–3.5 | 10 | 17% | 2 (Mitigate Risk), 3 (Detect) |
| 4: Securing Devices | 4.1–4.4 | 11 | 18% | 1, 2, 3 |
| 5: Securing Applications & Data | 5.1–5.6 | 13 | 22% | 2, 3 |
| **Total** | | **60** | **100%** | |

*Distribution derived from CED class periods and topic density; validated against official sample question LO mapping.*

### Question Type Breakdown

| Type | Count | Format |
|------|-------|--------|
| Single-Select | 40 | 4 options (A–D), one correct |
| Multi-Select | 20 | "Select all that apply — 5 options, variable correct count" |

### Skill Category Distribution (Target)

| Skill Category | Code | Target % | MCQ Count |
|----------------|------|----------|-----------|
| Analyze Risk | 1.A–1.D | 30% | 18 |
| Mitigate Risk | 2.A–2.D | 35% | 21 |
| Detect Attacks | 3.A–3.D | 35% | 21 |

*All within CED 25–40% ranges.*

### LO Coverage Requirements

- Every topic (1.1–5.6) must have ≥1 MCQ
- Each LO code (`Unit.Topic.Letter`) tagged on its question
- No duplicate LO codes across MCQs (max 1 per LO)
- Multi-select questions tag multiple LOs where appropriate

---

## Section II: Free-Response (1 Question, 5 Parts, 50 min)

### Task: Device Security Analysis (Performance Task)

**Modeled on official CED sample** — students analyze a single device using multiple simulated sources.

### Sources Provided (5 sources, ~2–3 pages each)

| Source | Type | Content |
|--------|------|---------|
| Source 1 | Firewall Configuration | Rule table: Action, Source, Destination, Direction, Port, Protocol |
| Source 2 | Network Application Log | Process execution logs (sudo, apt, systemctl, ufw, ss, journalctl) |
| Source 3 | Authentication Log | SSH/FTP login attempts, sudo sessions, UFW blocks, cron jobs |
| Source 4 | Web Server Access Log | HTTP requests (GET/POST), IPs, user agents, paths, status codes |
| Source 5 | File System Permissions | `ls -la` output showing ownership, permissions, timestamps |

### Parts (A–E) — 14 Points Total

| Part | Task Verb | Focus | Points | LO/Skill Tags |
|------|-----------|-------|--------|---------------|
| A | Identify | Identify security issues from firewall rules | 2 | 3.4.A, 3.4.C, 2.A |
| B | Explain | Explain evidence of attacks from auth logs | 3 | 4.4.A, 3.D, 1.C |
| C | Describe | Describe impact of permission/config changes | 3 | 5.2.C, 5.2.D, 2.B |
| D | Determine | Determine how firewall rules affect traffic | 3 | 3.4.B, 3.4.D, 2.C |
| E | Write | Write a command to mitigate a detected issue | 3 | 5.5.A, 2.D, 3.B |

### Scoring Guidelines

- Each part has explicit rubric with evidence citation requirements
- Students must cite specific source lines (e.g., "Source 3, lines 3–7")
- Partial credit for correct reasoning with incomplete evidence
- Total: 14 points → scaled to 30% of exam score

---

## Administration Logistics

| Event | Date | Details |
|-------|------|---------|
| In-class administration | Apr 1, 2027 | 130 min (8:00–10:10 AM), proctored |
| Optional self-scoring session | Apr 1, 2027 | 30 min after exam (MCQ only, exemplars provided) |
| Self-scoring window | Apr 2–11, 2027 | Spring Break; students score MCQ + FRQ at home |
| Error Analysis due | Apr 11, 2027 | 5 missed MCQs + 3 weak FRQ topics with justifications |
| Teacher FRQ spot-check | Apr 10–11, 2027 | 50% of FRQ self-scores verified before high-miss bank compilation |

---

## Materials to Produce

| File | Purpose | Naming |
|------|---------|--------|
| U0-Exam-MCQ.md | 60 MCQs with LO tags, answer key, distractor analysis | Student version |
| U0-Exam-FRQ.md | Device Security Analysis task (5 sources, 5 parts) | Student version |
| U0-Exam-Student-Packet.md | Combined exam packet (instructions, MCQ, FRQ, answer sheets) | Student version |
| U0-Exam-MCQ-Key.md | Answer key with distractor analysis for all 60 MCQs | Teacher only |
| U0-Exam-FRQ-Key.md | FRQ scoring rubric with sample responses, point breakdown | Teacher only |
| U0-Exam-Error-Analysis.md | Worksheet: 5 MCQ + 3 FRQ weaknesses, justifications | Student version |
| U0-Exam-Teacher-Key.md | Combined teacher key + administration notes | Teacher only |

---

## Grade Weight (Per Course-Syllabus.md)

| Category | Weight | Points | Practice Exam Contribution |
|----------|--------|--------|---------------------------|
| Quizzes/Assessments | 25% | 125 pts | **60 pts raw** (scaled to quiz weight) |

*60 raw points = 1 pt per MCQ + 14 pt FRQ scaled to 60-pt total*

---

## Quality Gates (Pre-Upload)

- [ ] Course Curriculum Framework approved (this document)
- [ ] MC weight distribution validated against CED (discrepancy >2% → adjust)
- [ ] All 60 MCQs LO-tagged, no duplicates, distractor analysis complete
- [ ] FRQ modeled on official Device Security Analysis, 5 parts, 14 pts
- [ ] Multi-select format verified: "Select all that apply — 5 options, variable correct count"
- [ ] Internal peer-review pilot: 10 MCQs (2/unit) reviewed by Mr. Chen (CS Dept.) Mar 20
- [ ] Teacher review checkpoint: 3-day buffer after Task 1.3 completion
- [ ] Alternate reviewer: Department Head (name TBD) as backup

---

## File Locations

- **Local (markdown source)**: `/Users/pauljonessr/Projects/ap-cybersecurity/`
- **Google Drive**: `qsec_practice` folder (ID captured at creation, `drive_index_generator.py` updated)
- **GitHub**: `ivycollegiate-development` org (if applicable)

---

*Blueprint approved for development. Proceed to Task 1.2: Write 60 MCQs with Internal Peer-Review Pilot.*