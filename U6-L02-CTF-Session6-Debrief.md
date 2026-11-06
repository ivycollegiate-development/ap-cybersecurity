# U6-L02: CTF Session 6 Debrief — Network Forensics

**AP Cybersecurity — ICA 2026-27**  
**Date**: May 7, 2027 (Fri) | **Period**: 123 | **Duration**: 50 min  
**Type**: Post-AP CTF Debrief | **Format**: Walkthrough + Packet Analysis

---

## Learning Objectives

By the end of this lesson, students will be able to:
1. **Reconstruct** the CTF Session 6 network forensics challenge attack chain
2. **Apply** Wireshark/tshark filters to extract IOCs from PCAP
3. **Correlate** network artifacts with MITRE ATT&CK techniques
4. **Document** findings in portfolio-ready format

---

## Prerequisites

- CTF Session 6 completed (Saturday May 8 or prior)
- Wireshark/tshark installed (Codespaces or local)
- Session 6 PCAP file: `ctf-session6.pcap` (distributed via Classroom)

---

## Materials

- `ctf-session6.pcap` — network capture with: C2 beaconing, DNS tunneling, lateral movement
- Wireshark/tshark cheat sheet (distributed)
- `Portfolio-Template.md` Section 3 (Implementation Evidence) — for documentation model
- MITRE ATT&CK Navigator (https://mitre-attack.github.io/attack-navigator/)

---

## Lesson Flow

| Time | Activity | Details |
|------|----------|---------|
| 0-5 | **Context** | "CTFs aren't just games — they're interview prep. Every challenge = a portfolio artifact if documented." |
| 5-20 | **Guided Walkthrough** (15 min) | Teacher leads analysis of `ctf-session6.pcap`:<br>1. **Overview**: `tshark -r ctf-session6.pcap -q -z io,phs` — protocol hierarchy<br>2. **DNS Tunneling**: `tshark -r ctf-session6.pcap -Y "dns.qry.name.len > 50" -T fields -e dns.qry.name \| sort -u`<br>3. **C2 Beaconing**: `tshark -r ctf-session6.pcap -Y "http" -T fields -e frame.time -e ip.src -e ip.dst -e http.host -e http.request.uri \| head -30`<br>4. **Lateral Movement**: `tshark -r ctf-session6.pcap -Y "smb || smb2" -T fields -e ip.src -e ip.dst -e smb2.cmd` |
| 20-35 | **Student Analysis** (15 min) | In pairs, students answer on shared doc:<br>1. **Initial Access**: What technique? (TA0001) — Evidence?<br>2. **Command & Control**: Protocol? Domain pattern? (TA0011)<br>3. **Lateral Movement**: Service used? Accounts? (TA0008)<br>4. **Exfiltration**: Data volume? Encryption? (TA0010)<br>5. **Detection**: What Suricata/Zeek rules would fire? |
| 35-45 | **MITRE Mapping** (10 min) | Each pair adds their findings to class MITRE ATT&CK Navigator layer (shared link). Teacher highlights: T1071.004 (DNS), T1021.002 (SMB), T1567.002 (Exfil to Cloud) |
| 45-50 | **Portfolio Connection** | "Document this like Portfolio Section 3: problem → analysis → evidence → MITRE mapping. Save your tshark commands and output as `ctf-session6-analysis.md` in your portfolio repo." |

---

## Teacher Notes

- **PCAP source**: Generated from CTFd challenge or custom (malware-traffic-analysis.net style)
- **Codespaces**: Ensure `tshark` works in devcontainer (installed via Dockerfile)
- **Differentiation**: Provide pre-run tshark output for students who struggle with CLI
- **Time**: If short, skip lateral movement deep-dive; focus on DNS+C2

---

## Differentiation

| Need | Adjustment |
|------|------------|
| CLI Novice | Provide tshark command bank; focus on interpretation not syntax |
| Advanced | Add: "Write a Suricata rule for the DNS tunneling" or "Extract file from HTTP stream" |
| Visual Learner | Use Wireshark GUI for walkthrough; show "Follow HTTP/TCP Stream" |

---

## Assessment

**Formative**: Pair analysis doc collected — checks for MITRE technique accuracy and evidence citation.

---

## Homework / Next Steps

- **Save**: `ctf-session6-analysis.md` to portfolio repo (create `ctf/` folder)
- **Read**: Portfolio-Template.md Section 3 (Implementation Evidence) — note structure
- **Prep**: U6-L03 (May 10) — bring capstone repo URL, threat model, and GitHub profile link

---

*U6-L02 — CTF Session 6 Debrief — Network Forensics — May 7, 2027*