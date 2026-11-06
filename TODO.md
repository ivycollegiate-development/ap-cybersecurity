# Capstone Extension TODO Checklist

**Lab**: [Lab Name]  
**Student**: _________________________  
**Repo**: _________________________  
**Branch**: `capstone` (create from `capstone-starter`)

---

## Week 1: Mar 29 (Work Day 1)

### Morning (Threat Modeling)
- [ ] Clone `capstone-starter` branch
- [ ] Review `README_CAPSTONE.md` for lab-specific requirements
- [ ] Complete **THREAT_MODEL.md** using template
  - [ ] System architecture diagram
  - [ ] Asset inventory
  - [ ] STRIDE analysis (min 8 threats)
  - [ ] Risk prioritization (top 3)
- [ ] Commit: `feat: threat model complete`

### Afternoon (Repo Setup + Design)
- [ ] Explore starter stubs in `src/stubs/`
- [ ] Design data structures and interfaces
- [ ] Write `PSEUDOCODE.md` (required for Light Option; recommended for all)
- [ ] Plan implementation tasks for Mar 30
- [ ] Commit: `docs: pseudocode and design notes`

---

## Week 2: Mar 30 (Work Day 2)

### Morning (Core Implementation)
- [ ] Implement core functionality (per lab requirements)
  - Lab 1: Recon scanner + auth tester
  - Lab 2: RuBAC engine + audit logger
  - Lab 3: AEAD + file encryption
  - Lab 4: CA + cert lifecycle
  - Lab 5: WAF engine + SAST analyzer
- [ ] Write unit tests as you go (TDD encouraged)
- [ ] Commit frequently with descriptive messages

### Afternoon (Integration + Testing)
- [ ] Integrate components
- [ ] Run full test suite: `pytest tests/ -v`
- [ ] Fix failing tests
- [ ] Run security scan: `bandit -r capstone/`
- [ ] Fix any HIGH/CRITICAL findings
- [ ] Commit: `feat: core implementation complete`

---

## Week 3: Mar 31 (Work Day 3 — Morning)

### Final Polish (Before 10:00 AM)
- [ ] Complete all TODO items in `README_CAPSTONE.md`
- [ ] Run full CI locally: lint, test, security scan
- [ ] Generate coverage report: `pytest --cov=capstone --cov-report=term-missing`
- [ ] Verify coverage ≥ 80%
- [ ] Update `THREAT_MODEL.md` if implementation changed design
- [ ] Prepare demo script (3 min max)

### Demo Prep
- [ ] Test Codespaces environment loads correctly
- [ ] Prepare demo data (sample logs, test files, etc.)
- [ ] Practice 3-minute demo with timer
- [ ] Record 60-second backup video (phone/capture) in case of technical issues
- [ ] Push final commits to `capstone` branch

---

## Demo Time: Mar 31 (Class)

- [ ] Join class, screen share ready
- [ ] Present 3-minute demo
- [ ] Answer Q&A (1 min)

---

## Post-Demo: Apr 2 (Buffer)

- [ ] Address any judge feedback (if requested)
- [ ] Ensure all files pushed to `capstone` branch
- [ ] Verify `THREAT_MODEL.md`, `PSEUDOCODE.md` (if Light), `TEST_PLAN.md` (if Light) present

---

## Definition of Done (Full Option)

- [ ] `THREAT_MODEL.md` complete and accurate
- [ ] Implementation meets minimum requirements (3+ features)
- [ ] All tests pass (`pytest tests/ -v`)
- [ ] Coverage ≥ 80%
- [ ] No HIGH/CRITICAL bandit findings
- [ ] CI passes (lint, test, security)
- [ ] `capstone/` branch up to date
- [ ] Demo delivered successfully

## Definition of Done (Light Option)

- [ ] `THREAT_MODEL.md` complete
- [ ] `PSEUDOCODE.md` with 3–5 core algorithms
- [ ] `TEST_PLAN.md` with 15+ test cases (5+ security)
- [ ] Design walkthrough delivered

---

## Emergency Contacts

- Technical issues: #ap-cyber-capstone Slack / GitHub Discussions
- Lab readiness problems: Email teacher immediately
- Light Option declaration: Email by Mar 26, 23:59
- Codespaces not loading: Use local Docker / Replit backup

---

## Notes

______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________