# U6-L06: Log Analysis Debrief Prep

**AP Cybersecurity — ICA 2026-27**  
**Date**: May 13, 2027 (Thu) | **Period**: 127 | **Duration**: 50 min  
**Type**: Skill Reinforcement | **Format**: Lab + Portfolio Artifact Creation

---

## Learning Objectives

By the end of this lesson, students will be able to:
1. **Execute** structured log analysis using grep, awk, jq, and SIEM queries
2. **Correlate** multi-source logs (auth, firewall, application, audit) to reconstruct incidents
3. **Produce** a portfolio-ready log analysis writeup with timeline, IOCs, and MITRE mapping
4. **Connect** log analysis skills to capstone logging implementation (LO 5.6)

---

## Prerequisites

- Unit 5 Lab 5 (WAF/Log Analysis) completed
- CLI Fluency Check (Apr 28) — Task 3: Log Analysis
- `ctf-session6.pcap` analysis (U6-L02) — network-to-log correlation
- Investigation dataset: `/investigation/` (from Codespaces devcontainer)

---

## Materials

- Investigation dataset (pre-loaded in Codespaces): `app.log`, `auth.json`, `firewall.log`, `audit.log`
- `Portfolio-Template.md` Section 3.4 (Testing & Validation) — for artifact documentation model
- Log analysis cheat sheet: grep/awk/jq patterns, Splunk/Elastic query syntax
- MITRE ATT&CK reference: T1059, T1069, T1110, T1548, T1003

---

## Lesson Flow

| Time | Activity | Details |
|------|----------|---------|
| 0-5 | **Context** | "Logs are the receipts. Your capstone implemented structured logging (LO 5.6). Now: prove you can *read* them. This = portfolio artifact + interview prep." |
| 5-20 | **Guided Lab: Multi-Source Correlation** (15 min) | Teacher leads in Codespaces (projected):<br>1. **Auth brute force**: `jq 'select(.message | contains("Failed password")) | .source_ip' auth.json \| sort \| uniq -c \| sort -rn`<br>2. **Firewall correlation**: `grep "192.168.1.100" firewall.log \| head -20`<br>3. **Process execution**: `grep "execve.*uid=0" audit.log`<br>4. **Timeline build**: Combine timestamps → attack chain narrative |
| 20-35 | **Independent Analysis** (15 min) | Students analyze dataset to answer:<br>1. **Initial compromise**: When? Vector? Evidence?<br>2. **Privilege escalation**: Technique? MITRE ID?<br>3. **Persistence**: Mechanism? Cron? Service? Registry?<br>4. **Lateral movement**: Target? Protocol?<br>5. **Exfiltration**: Data? Volume? Encryption?<br>6. **Detection gaps**: What logs *missing*? What rules *needed*?<br>Write findings in `log-analysis-debrief.md` (portfolio `ctf/` folder) |
| 35-45 | **Portfolio Artifact Polish** (10 min) | Structure `log-analysis-debrief.md`:<br>```markdown<br># Log Analysis Debrief — [Scenario Name]<br>## Scenario<br>[1-paragraph context]<br>## Timeline<br>[Table: Timestamp | Source | Event | MITRE Technique]<br>## IOCs<br>[IPs, hashes, domains, usernames]<br>## Detection Rules Proposed<br>[Suricata/Elastic/Splunk queries]<br>## Capstone Connection<br>[How my capstone logging would/could detect this]<br>``` |
| 45-50 | **Commit & Reflect** | `git add ctf/log-analysis-debrief.md && git commit -m "Add log analysis debrief artifact" && git push`<br>Exit: "One log source you wish you had in this scenario." |

---

## Teacher Notes

- **Dataset**: Use Codespaces `/investigation/` (auth.json, app.log, firewall.log, audit.log from devcontainer Dockerfile)
- **Codespaces**: Ensure all students have devcontainer running; fallback to Replit/Gitpod with install-tools.sh
- **Time**: If short, provide pre-extracted IOCs; focus on correlation narrative
- **Capstone link**: Explicitly connect to Lab 5 (WAF/Log Analysis) and LO 5.6.A-C

---

## Differentiation

| Need | Adjustment |
|------|------------|
| CLI Weak | Provide pre-run command outputs; focus on interpretation |
| Advanced | Add: "Write Elastic Watcher alert for brute force pattern" or "Create Sigma rule" |
| Visual | Use Kibana/Grafana if deployed; show dashboard creation |

---

## Assessment

**Formative**: `log-analysis-debrief.md` in portfolio repo — teacher checks: timeline structure, MITRE IDs correct, capstone connection explicit.

---

## Homework / Next Steps

- **Polish**: `log-analysis-debrief.md` — add detection rules, capstone connection — due U6-L07 (May 14)
- **Portfolio**: Continue PORTFOLIO.md Sections 1-3, 8 — due U6-L07
- **Read**: Portfolio-Rubric.md Dimensions 2, 3 (Implementation Evidence, Documentation) — self-score draft

---

*U6-L06 — Log Analysis Debrief Prep — May 13, 2027*