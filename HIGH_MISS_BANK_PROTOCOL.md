# High-Miss Bank Extraction Protocol — AP Cybersecurity

**Extraction Date**: Mar 29, 2027 (after unit tests graded, before Spring Break)  
**Supplement Date**: Apr 11–16, 2027 (from practice exam self-scoring)  
**Teacher Review Gate**: 3-day buffer after each stage before packet upload

---

## Stage 1: Mar 29 — Unit Test High-Miss Bank (30 items)

### Data Source Requirements
- Unit test results must be queryable from:
  - Google Classroom grade export, OR
  - Teacher gradebook (Google Sheets), OR
  - Manual entry from graded tests
- Each item must have: question text, correct answer, student responses per class, LO code

### Extraction Process

```bash
# Option A: Automated (if gradebook queryable)
python3 scripts/extract_high_miss_bank.py \
  --source classroom \
  --course-id 856028522807 \
  --unit-tests "U1-Test,U2-Test,U3-Test,U4-Test,U5-Test" \
  --threshold 0.60 \
  --output high_miss_bank_stage1.csv

# Option B: Manual (if automated unavailable)
# Teacher fills: scripts/high_miss_bank_template.csv with:
# question_id,unit,lo_code,question_text,correct_answer,total_students,correct_count,miss_rate
```

### Selection Criteria
1. **Miss rate ≥ 60%** across all sections (primary filter)
2. **LO coverage**: At least 2 items per Unit (1–5), balanced across Topics
3. **Difficulty spread**: Mix of conceptual, application, analysis
4. **No duplicates**: Deduplicate by LO code + concept
5. **Total**: Exactly 30 items (6 per unit average)

### Output Format (`high_miss_bank_stage1.csv`)
| question_id | unit | lo_code | question_text | correct_answer | miss_rate | distractor_analysis |
|-------------|------|---------|---------------|----------------|-----------|---------------------|
| HM-001 | 1 | 1.2.A | ... | B | 0.72 | A: confusion with..., C: ... |
| HM-002 | 1 | 1.3.B | ... | A | 0.68 | ... |

### Teacher Review (Mar 29–31, 30 min)
- Verify LO codes match Course Curriculum Framework
- Confirm distractor analysis accuracy
- Approve 30-item bank for packet building
- **Sign-off required** before packet generation

---

## Stage 2: Apr 11–16 — Practice Exam Supplement

### Trigger
- Practice exam administered Apr 1
- Self-scoring due Apr 11 (Spring Break)
- Error analysis worksheets collected Apr 11

### Supplement Process (Pre-Defined Protocol)

| Date | Action | Owner |
|------|--------|-------|
| **Apr 11** | Export practice exam scores + error analysis from Classroom/Forms | Teacher |
| **Apr 12** | Run supplement script: identifies top-missed practice exam items not in Stage 1 bank | Teacher/Script |
| **Apr 12–13** | Teacher review (30 min): validate new items, confirm LO codes, check duplicates | Teacher |
| **Apr 14** | Merge Stage 1 + Supplement → Final 30-item High-Miss Bank | Teacher |
| **Apr 16** | Upload final bank to Drive; regenerate 5 Unit Review Packets | Teacher |

### Supplement Script Logic
```python
# scripts/supplement_high_miss_bank.py
# Input: practice_exam_results.csv, high_miss_bank_stage1.csv
# Output: high_miss_bank_final.csv (still 30 items, best of both sources)

# 1. Calculate miss rates for all 60 practice exam MCQs
# 2. Filter: miss_rate >= 50% AND lo_code not already in Stage 1
# 3. Rank by miss_rate descending
# 4. For each LO code in Stage 1 with miss_rate < 65%, consider replacement
# 5. Maintain exactly 30 items, balanced across Units 1–5
# 6. Output: final 30 items with source tag (stage1/stage2)
```

### Teacher Review Checklist (Apr 12–13, 30 min)
- [ ] All new items have valid LO codes (Unit.Topic.Letter format)
- [ ] No duplicate concepts across Stage 1 + Supplement
- [ ] Unit balance maintained (5–7 items per unit)
- [ ] Distractor analysis provided for new items
- [ ] Final count = 30 items

---

## Fallback Protocol (If Miss-Rate Data Unavailable)

**Trigger**: Unit test results not queryable from gradebook/Classroom by Mar 28

### Option A: Teacher-Curated Bank (Preferred)
Teacher selects 30 MCQs based on:
- Known difficult concepts from instruction
- Historical student struggle areas
- LO coverage map (ensure all 5 units represented)
- Mix of recall, application, analysis

### Option B: Full Unit Test Bank
Use ALL MCQs from all 5 unit tests as the "bank"
- Build review packets covering all test items
- Less targeted but comprehensive
- Teacher annotates "high priority" items for students

### Documentation
Record which fallback used in `HIGH_MISS_BANK_LOG.md`:
```markdown
# High-Miss Bank Log
**Date**: 2027-03-29
**Method**: [Automated / Teacher-Curated / Full Test Bank]
**Source**: [Classroom Export / Gradebook / Manual]
**Items**: 30
**Units Covered**: 1:6, 2:6, 3:6, 4:6, 5:6
**Teacher Sign-off**: _________________________
```

---

## Packet Generation (After Final Bank Approved)

### 5 Unit Review Packets
Each packet contains:
1. **High-Miss Items** (6–7 questions from bank for that unit)
2. **LO Mapping Table** — each question → LO code → Course Curriculum Framework reference
3. **Distractor Analysis** — why each wrong answer is tempting
4. **Mini-Lesson** — 1-page concept refresher for top 2 missed LOs
5. **Practice Set** — 5 new items (similar concept, different context)
6. **Self-Check** — Answer key with explanations

### Naming Convention
- `U1-Review-Packet-High-Miss.md`
- `U2-Review-Packet-High-Miss.md`
- `U3-Review-Packet-High-Miss.md`
- `U4-Review-Packet-High-Miss.md`
- `U5-Review-Packet-High-Miss.md`

### Upload Location
Google Drive: `qsec_ap_review` folder → `review-packets/` subfolder

---

## Quality Gates

| Gate | When | Criteria |
|------|------|----------|
| Stage 1 Approval | Mar 31 | 30 items, valid LO codes, distractor analysis, teacher sign-off |
| Stage 2 Approval | Apr 16 | Final 30 items, no duplicates, balanced units, teacher sign-off |
| Packet Upload | Apr 19 | All 5 packets generated, formatted, uploaded to Drive |

---

## Scripts to Create

| Script | Purpose | Location |
|--------|---------|----------|
| `extract_high_miss_bank.py` | Stage 1 extraction from gradebook | `/scripts/` |
| `supplement_high_miss_bank.py` | Stage 2 merge with practice exam | `/scripts/` |
| `generate_review_packets.py` | Build 5 packets from final bank | `/scripts/` |
| `high_miss_bank_template.csv` | Manual entry template | `/scripts/` |

---

*Protocol version 1.0 — Aligned to Pacing Calendar, Course Curriculum Framework*

---

## Packet Templates (Detailed)

### Template: Unit Review Packet (`U#-Review-Packet-High-Miss.md`)

```markdown
# Unit # Review Packet — High-Miss Bank Items

**AP Cybersecurity — ICA 2026-27**  
**Unit**: # — [Unit Name]  
**Source**: High-Miss Bank (Stage 1: Mar 29, Stage 2: Apr 11–16)  
**Target**: AP Exam Review — May 5, 2027

---

## High-Miss Items (6–7 Questions)

### HM-XXX | LO #.X.X | Miss Rate: XX%
**Question**: [Full question text]

A) [Option A]  
B) [Option B]  
C) [Option C]  
D) [Option D]  
E) [Option E — for multi-select only]

**Correct Answer**: [Letter(s)]  
**Distractor Analysis**:  
- [Option A]: Why it's tempting / what misconception it targets  
- [Option B]: ...  
- [Option C]: ...  
- [Option D]: ...  
- [Option E]: ...  

**Key Concept**: [One-sentence exam-ready summary]

---

## LO Mapping Table

| Item | LO Code | Framework Reference | Concept Category |
|------|---------|---------------------|------------------|
| HM-XXX | #.X.X | Unit # Topic X.X | [Category] |

---

## Mini-Lesson: Top 2 Missed LOs

### LO #.X.X — [Concept Name] (Miss Rate XX%)

[2-3 paragraph concept refresher with:
- Core definition
- Key formula/rule/process
- Common misconception & correction
- Exam tip / "watch for" language
- Quick reference table if applicable]

---

### LO #.X.X — [Concept Name] (Miss Rate XX%)

[Same structure as above]

---

## Practice Set (5 New Items)

### P# | LO #.X.X
**Question**: [New question testing same LO, different context]

[Options]

**Answer**: [Letter]  
**Explanation**: [Why correct, why distractors wrong]

---

## Self-Check Answer Key

| Item | Answer | LO | Explanation |
|------|--------|-----|-------------|
| HM-XXX | [Letter] | #.X.X | [1-line rationale] |

---

## Study Plan Template

| LO Code | Concept | Current Mastery (1-5) | Review Action | Target Date |
|---------|---------|----------------------|---------------|-------------|
| #.X.X | [Concept] | ___ | [Specific action] | Apr XX |

---

*Packet generated from High-Miss Bank — Upload to qsec_ap_review/review-packets/*
```

---

## Grading Integration

### High-Miss Bank → Review Packet → AP Exam Prep Flow

```
Unit Tests (Mar) → Stage 1 Bank (30 items) → 5 Unit Packets (Apr 12-19)
                                      ↓
Practice Exam (Apr 1) → Self-Score (Apr 2-11) → Error Analysis (Apr 11)
                                      ↓
                              Stage 2 Supplement (Apr 11-16)
                                      ↓
                              Final 30-Item Bank → Regenerate Packets (Apr 16)
                                      ↓
                              5 Packets + 3 FRQ Sets + CLI Fluency (Apr 19-May 2)
                                      ↓
                              Mock Exam (May 2) → AP Exam (May 5)
```

### Gradebook Integration

| Assessment | Weight | Data Source | Integration Point |
|------------|--------|-------------|-------------------|
| Unit Tests | Formative | Classroom/Gradebook | Stage 1 extraction (Mar 29) |
| Practice Exam | Quiz (25%) | Classroom Forms | Stage 2 supplement (Apr 11-16) |
| Review Packets | Participation (5%) | Completion check | Apr 19-May 4 |
| FRQ Practice | Formative | Teacher scoring | Apr 20/22/27 |
| CLI Fluency | Formative | Auto-grader CSV | Apr 28 |
| Mock Exam | Formative | Teacher scoring | May 2 |

### Participation Incentive (5% of Participation = 5/25 pts)

| Activity | Points | Verification |
|----------|--------|--------------|
| Complete all 5 review packets | 2/5 | Teacher check (Apr 19) |
| Complete all 3 FRQ practice sets | 2/5 | Submitted & scored (Apr 27) |
| Complete CLI Fluency Check | 1/5 | Auto-grader CSV (Apr 28) |
| **Total** | **5/5** | |

### Teacher Scoring Workflow

1. **Review Packets** (Apr 12-19): Quick scan for completion → 2 pts
2. **FRQ Sets** (Apr 20/22/27): Score with rubric (14 pts each) → feedback → 2 pts
3. **CLI Fluency** (Apr 28): Import CSV → verify ≥ 7/10 → 1 pt
4. **Mock Exam** (May 2): Full score → predictive composite → formative only

---

## Scripts (Implementation Templates)

### `/scripts/extract_high_miss_bank.py`

```python
#!/usr/bin/env python3
"""
Stage 1: Extract High-Miss Bank from Unit Test Results
Usage: python3 extract_high_miss_bank.py --source classroom --course-id 856028522807 --threshold 0.60
"""

import argparse
import csv
import json
from pathlib import Path

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--source", choices=["classroom", "sheets", "manual"], required=True)
    p.add_argument("--course-id", type=str)
    p.add_argument("--unit-tests", type=str, help="Comma-separated test names")
    p.add_argument("--threshold", type=float, default=0.60)
    p.add_argument("--output", type=str, default="high_miss_bank_stage1.csv")
    p.add_argument("--creds", type=str, help="Path to Google credentials")
    return p.parse_args()

def fetch_from_classroom(course_id, test_names, creds_path):
    """Use Google Classroom API to get student submissions for unit tests"""
    # TODO: Implement Classroom API calls
    # Return list of dicts: {question_id, unit, lo_code, question_text, correct_answer, student_responses}
    pass

def fetch_from_sheets(sheet_id, creds_path):
    """Read unit test results from teacher Google Sheet"""
    # TODO: Implement Sheets API calls
    pass

def load_manual(template_path):
    """Load from teacher-filled CSV template"""
    with open(template_path) as f:
        return list(csv.DictReader(f))

def calculate_miss_rates(items):
    """Add miss_rate field to each item"""
    for item in items:
        total = int(item.get("total_students", 0))
        correct = int(item.get("correct_count", 0))
        item["miss_rate"] = round(1 - correct/total, 3) if total > 0 else 0
    return items

def select_top_items(items, threshold, max_per_unit=7):
    """Filter by threshold, balance across units, dedupe by LO"""
    # Filter
    filtered = [i for i in items if i["miss_rate"] >= threshold]
    
    # Group by unit
    by_unit = {}
    for item in filtered:
        by_unit.setdefault(item["unit"], []).append(item)
    
    # Sort each unit by miss_rate desc
    for unit in by_unit:
        by_unit[unit].sort(key=lambda x: x["miss_rate"], reverse=True)
    
    # Select top N per unit, dedupe LO codes
    selected = []
    seen_los = set()
    for unit in sorted(by_unit.keys()):
        for item in by_unit[unit]:
            if item["lo_code"] not in seen_los and len([s for s in selected if s["unit"]==unit]) < max_per_unit:
                selected.append(item)
                seen_los.add(item["lo_code"])
    
    return selected

def main():
    args = parse_args()
    
    if args.source == "classroom":
        items = fetch_from_classroom(args.course_id, args.unit_tests.split(","), args.creds)
    elif args.source == "sheets":
        items = fetch_from_sheets(args.sheet_id, args.creds)
    else:
        items = load_manual("high_miss_bank_template.csv")
    
    items = calculate_miss_rates(items)
    selected = select_top_items(items, args.threshold)
    
    # Write output
    fieldnames = ["question_id", "unit", "lo_code", "question_text", "correct_answer", "miss_rate", "distractor_analysis"]
    with open(args.output, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i, item in enumerate(selected, 1):
            item["question_id"] = f"HM-{i:03d}"
            writer.writerow({k: item.get(k, "") for k in fieldnames})
    
    print(f"Selected {len(selected)} items → {args.output}")
    print("Unit distribution:", {u: len([s for s in selected if s["unit"]==u]) for u in set(s["unit"] for s in selected)})

if __name__ == "__main__":
    main()
```

---

### `/scripts/supplement_high_miss_bank.py`

```python
#!/usr/bin/env python3
"""
Stage 2: Supplement High-Miss Bank with Practice Exam Data
Usage: python3 supplement_high_miss_bank.py --practice-exam results.csv --stage1 bank.csv --output final.csv
"""

import argparse
import csv
from pathlib import Path

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--practice-exam", type=str, required=True, help="Practice exam results CSV")
    p.add_argument("--stage1", type=str, required=True, help="Stage 1 bank CSV")
    p.add_argument("--output", type=str, default="high_miss_bank_final.csv")
    p.add_argument("--min-miss-rate", type=float, default=0.50)
    return p.parse_args()

def load_bank(path):
    with open(path) as f:
        return list(csv.DictReader(f))

def load_practice_exam(path):
    """Returns dict: lo_code -> {miss_rate, question_data}"""
    # Practice exam results should have per-question miss rates
    # Expected columns: question_id, lo_code, question_text, correct_answer, miss_rate, distractor_analysis
    with open(path) as f:
        return {row["lo_code"]: row for row in csv.DictReader(f)}

def merge_banks(stage1_items, practice_data, min_miss_rate):
    """Merge Stage 1 + Practice Exam, keep best 30 items"""
    stage1_by_lo = {item["lo_code"]: item for item in stage1_items}
    
    # Find practice exam items that are better than Stage 1 items
    candidates = []
    for lo_code, pe_item in practice_data.items():
        pe_miss = float(pe_item.get("miss_rate", 0))
        if pe_miss < min_miss_rate:
            continue
        
        if lo_code in stage1_by_lo:
            s1_miss = float(stage1_by_lo[lo_code].get("miss_rate", 0))
            if pe_miss > s1_miss:
                # Practice exam item is harder - candidate for replacement
                candidates.append(("replace", lo_code, pe_item, pe_miss - s1_miss))
        else:
            # New LO not in Stage 1
            candidates.append(("new", lo_code, pe_item, pe_miss))
    
    # Sort by improvement/new miss rate descending
    candidates.sort(key=lambda x: x[3], reverse=True)
    
    # Build final bank
    final_items = list(stage1_items)
    final_los = set(stage1_by_lo.keys())
    unit_counts = {}
    for item in final_items:
        unit_counts[item["unit"]] = unit_counts.get(item["unit"], 0) + 1
    
    for action, lo_code, item, score in candidates:
        if len(final_items) >= 30:
            break
        
        unit = item["unit"]
        if unit_counts.get(unit, 0) >= 7:  # Max 7 per unit
            continue
        
        if action == "replace":
            # Replace the Stage 1 item
            final_items = [i for i in final_items if i["lo_code"] != lo_code]
            final_items.append({**item, "source": "stage2", "improvement": score})
            unit_counts[unit] = unit_counts.get(unit, 0)  # Same unit count
        elif action == "new":
            final_items.append({**item, "source": "stage2"})
            unit_counts[unit] = unit_counts.get(unit, 0) + 1
        
        final_los.add(lo_code)
    
    # If still under 30, fill from Stage 1 items not yet included
    if len(final_items) < 30:
        for item in stage1_items:
            if item["lo_code"] not in final_los and len(final_items) < 30:
                final_items.append({**item, "source": "stage1"})
                final_los.add(item["lo_code"])
    
    # Renumber
    for i, item in enumerate(final_items, 1):
        item["question_id"] = f"HM-{i:03d}"
    
    return final_items

def main():
    args = parse_args()
    
    stage1 = load_bank(args.stage1)
    practice = load_practice_exam(args.practice_exam)
    
    final = merge_banks(stage1, practice, args.min_miss_rate)
    
    fieldnames = ["question_id", "unit", "lo_code", "question_text", "correct_answer", "miss_rate", "distractor_analysis", "source"]
    with open(args.output, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(final)
    
    print(f"Final bank: {len(final)} items → {args.output}")
    print("Sources:", {s: len([i for i in final if i.get("source")==s]) for s in set(i.get("source") for i in final)})
    print("Units:", {u: len([i for i in final if i["unit"]==u]) for u in sorted(set(i["unit"] for i in final))})

if __name__ == "__main__":
    main()
```

---

### `/scripts/generate_review_packets.py`

```python
#!/usr/bin/env python3
"""
Generate 5 Unit Review Packets from Final High-Miss Bank
Usage: python3 generate_review_packets.py --bank high_miss_bank_final.csv --template packet_template.md --output-dir packets/
"""

import argparse
import csv
import re
from pathlib import Path
from string import Template

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--bank", type=str, required=True)
    p.add_argument("--template", type=str, default="packet_template.md")
    p.add_argument("--output-dir", type=str, default="review_packets")
    return p.parse_args()

def load_bank(path):
    with open(path) as f:
        return list(csv.DictReader(f))

def load_template(path):
    with open(path) as f:
        return Template(f.read())

def group_by_unit(items):
    by_unit = {}
    for item in items:
        by_unit.setdefault(item["unit"], []).append(item)
    return by_unit

def build_lo_mapping_table(items):
    rows = []
    for item in items:
        rows.append(f"| {item['question_id']} | {item['lo_code']} | Unit {item['unit']} Topic {item['lo_code'].split('.')[1]}.{item['lo_code'].split('.')[2]} | [Category] |")
    return "\n".join(rows)

def build_distractor_analysis(items):
    sections = []
    for item in items:
        sections.append(f"### {item['question_id']} | LO {item['lo_code']} | Miss Rate: {float(item['miss_rate'])*100:.0f}%\n\n**Question**: {item['question_text']}\n\n**Correct Answer**: {item['correct_answer']}\n\n**Distractor Analysis**:\n{item.get('distractor_analysis', '[Add analysis]')}\n\n**Key Concept**: [Add one-sentence summary]\n")
    return "\n---\n".join(sections)

def build_answer_key(items):
    rows = []
    for item in items:
        rows.append(f"| {item['question_id']} | {item['correct_answer']} | {item['lo_code']} | [Explanation] |")
    return "\n".join(rows)

def build_study_plan(items):
    rows = []
    for item in items:
        rows.append(f"| {item['lo_code']} | [Concept] | ___ | [Review action] | Apr XX |")
    return "\n".join(rows)

def main():
    args = parse_args()
    
    bank = load_bank(args.bank)
    template = load_template(args.template)
    
    by_unit = group_by_unit(bank)
    
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    unit_names = {
        "1": "Foundations of Cybersecurity",
        "2": "Network Security",
        "3": "Cryptography",
        "4": "System Security",
        "5": "Application Security"
    }
    
    for unit_num in sorted(by_unit.keys(), key=int):
        items = by_unit[unit_num]
        
        content = template.substitute(
            unit_num=unit_num,
            unit_name=unit_names.get(unit_num, f"Unit {unit_num}"),
            high_miss_items=build_distractor_analysis(items),
            lo_mapping_table=build_lo_mapping_table(items),
            answer_key=build_answer_key(items),
            study_plan=build_study_plan(items)
        )
        
        output_path = output_dir / f"U{unit_num}-Review-Packet-High-Miss.md"
        output_path.write_text(content)
        print(f"Generated: {output_path}")
    
    print(f"All 5 packets written to {output_dir}/")

if __name__ == "__main__":
    main()
```

---

### `/scripts/high_miss_bank_template.csv`

```csv
question_id,unit,lo_code,question_text,correct_answer,total_students,correct_count,miss_rate,distractor_analysis
HM-001,1,1.1.A,"Which threat actor type is most likely to target intellectual property for competitive advantage?",B,24,8,0.667,"A: Script kiddies lack sophistication; C: Hacktivists seek publicity; D: Insiders have access but different motive"
HM-002,1,1.2.A,"In the CIA triad, which property ensures data is not modified without authorization?",B,24,10,0.583,"A: Confidentiality = unauthorized access; C: Availability = accessible when needed; D: Non-repudiation = cannot deny action"
HM-003,2,2.1.C,"During a TCP NULL scan, what response indicates an open port?",B,24,6,0.75,"A: RST = closed; C: No response = open|filtered; D: SYN/ACK = not applicable to NULL scan"
HM-004,3,3.3.A,"The security of Diffie-Hellman key exchange relies on the hardness of which mathematical problem?",C,24,7,0.708,"A: Factorization = RSA; B: ECDLP = ECC; D: Knapsack = Merkle-Hellman (broken)"
HM-005,4,4.3.A,"ASLR (Address Space Layout Randomization) primarily mitigates which exploit technique?",C,24,9,0.625,"A: Buffer overflow = DEP/NX; B: Format string = input validation; D: ROP = combined with DEP"
HM-006,5,5.1.C,"Which OWASP Top 10 2021 category includes SQL Injection, Command Injection, and LDAP Injection?",B,24,5,0.792,"A: A01 Broken Access Control = authz flaws; C: A04 Insecure Design = missing controls; D: A06 Vulnerable Components = known CVEs"
```

---

## High-Miss Bank Log Template

```markdown
# High-Miss Bank Log — AP Cybersecurity 2026-27

## Stage 1: Mar 29, 2027
**Method**: [Automated / Teacher-Curated / Full Test Bank]  
**Source**: [Classroom Export / Gradebook / Manual Entry]  
**Items Selected**: 30  
**Unit Distribution**: 1:6, 2:6, 3:6, 4:6, 5:6  
**LO Codes Covered**: [List all 30 LO codes]  
**Threshold Used**: Miss rate ≥ 60%  
**Teacher Review**: 30 min (Mar 29-31)  
**Sign-off**: _________________________ (Date: __________)  

## Stage 2: Apr 11–16, 2027
**Practice Exam Data Source**: [Classroom Forms / Manual Entry]  
**Supplement Items Considered**: [Number]  
**Items Replaced**: [Number] / **New Items Added**: [Number]  
**Final Bank Count**: 30  
**Final Unit Distribution**: 1:X, 2:X, 3:X, 4:X, 5:X  
**Teacher Review**: 30 min (Apr 12-13)  
**Sign-off**: _________________________ (Date: __________)  

## Packet Generation: Apr 16, 2027
**Packets Generated**: 5 (U1-U5)  
**Upload Location**: qsec_ap_review/review-packets/  
**Teacher Review Gate**: 3-day buffer (Apr 16-19)  
**Final Upload**: Apr 19  

## Participation Tracking
| Student | U1 Packet | U2 Packet | U3 Packet | U4 Packet | U5 Packet | FRQ Set A | FRQ Set B | FRQ Set C | CLI Fluency | Total (5) |
|---------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-------------|-----------|
| [Name]  | ☐         | ☐         | ☐         | ☐         | ☐         | ☐         | ☐         | ☐         | ☐           | 0         |
```

---

*Protocol version 1.1 — Complete with Stage 2, templates, grading integration, scripts*