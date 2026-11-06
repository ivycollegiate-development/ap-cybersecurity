# FRQ Practice Set 2 — Device Security Analysis (Set B)

**AP Cybersecurity — ICA 2026-27**  
**Format**: Device Security Analysis FRQ (matches official AP exam)  
**Time**: 50 minutes  
**Date**: Apr 22, 2027  
**Points**: 14

---

## Scenario: Suspicious Windows Workstation

You are investigating a Windows 11 Enterprise workstation (`WKS-DEV-07`, IP: 10.0.10.45) used by a software developer. The EDR agent alerted on "PowerShell encoded command execution" at 14:22 UTC. You have collected the following artifacts:

---

### Source 1: Windows Firewall Configuration (Export)

```
Profile: Domain, Private, Public
State: ON
Inbound: Block (default)
Outbound: Allow (default)

Inbound Rules (Enabled):
- Rule: "Allow ICMPv4-In" | Action: Allow | Protocol: ICMPv4 | Direction: Inbound
- Rule: "Remote Desktop (TCP-In)" | Action: Allow | Protocol: TCP | Local Port: 3389 | Remote IP: 10.0.1.0/24
- Rule: "WinRM-HTTP-In-TCP" | Action: Allow | Protocol: TCP | Local Port: 5985 | Remote IP: 10.0.1.0/24
- Rule: "Custom: Dev Tools" | Action: Allow | Protocol: TCP | Local Port: 3000,8080,8888 | Remote IP: Any

Outbound Rules (Enabled):
- Rule: "Block Telemetry" | Action: Block | Remote IP: 13.107.0.0/16, 40.77.0.0/16
- Rule: "Allow Windows Update" | Action: Allow | Remote IP: Windows Update GPO
- Rule: "Custom: Dev Outbound" | Action: Allow | Protocol: TCP | Remote Port: 80,443,22,4433 | Remote IP: Any
```

---

### Source 2: Netstat Output (`netstat -ano` collected 14:25 UTC)

```
Proto  Local Address    Foreign Address    State       PID
TCP    0.0.0.0:135      0.0.0.0:0          LISTENING   984
TCP    0.0.0.0:445      0.0.0.0:0          LISTENING   4
TCP    0.0.0.0:3389     0.0.0.0:0          LISTENING   1236
TCP    0.0.0.0:5985     0.0.0.0:0          LISTENING   4
TCP    0.0.0.0:3000     0.0.0.0:0          LISTENING   4521
TCP    0.0.0.0:8080     0.0.0.0:0          LISTENING   4521
TCP    10.0.10.45:3389  10.0.1.50:52134    ESTABLISHED 1236
TCP    10.0.10.45:50234  185.220.101.45:80  ESTABLISHED 7892
TCP    10.0.10.45:50235  185.220.101.45:443 ESTABLISHED 7892
TCP    10.0.10.45:50236  10.0.10.20:445     ESTABLISHED 4
TCP    10.0.10.45:50237  192.168.1.100:4444 ESTABLISHED 7892
UDP    0.0.0.0:5355     *:*                               984
UDP    0.0.0.0:5353     *:*                               4521
```

---

### Source 3: Process List (`tasklist /v` collected 14:25 UTC)

```
Image Name                   PID Session Name    Session#    Mem Usage  Status    User Name
System                         4  Services         0          1,234 KB  Running   NT AUTHORITY\SYSTEM
svchost.exe                  984  Services         0            234 KB  Running   NT AUTHORITY\SYSTEM
lsass.exe                   1024  Services         0          5,678 KB  Running   NT AUTHORITY\SYSTEM
winlogon.exe                1156  Console         1          3,456 KB  Running   NT AUTHORITY\SYSTEM
explorer.exe                2341  Console         1         89,234 KB  Running   DOMAIN\devuser
chrome.exe                  3421  Console         1        234,567 KB  Running   DOMAIN\devuser
code.exe                    4521  Console         1        456,789 KB  Running   DOMAIN\devuser
powershell.exe              7892  Console         1         45,678 KB  Running   DOMAIN\devuser
cmd.exe                     7893  Console         1          12,345 KB  Running   DOMAIN\devuser
```

---

### Source 4: Security Event Log (Event IDs 4688, 4624, 4672 — 14:15–14:30 UTC)

```
Event 4688 (Process Creation):
  Time: 14:22:15
  New Process: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
  Command Line: powershell.exe -nop -w hidden -enc JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAA...
  Creator Process: C:\Windows\System32\cmd.exe (PID 7893)
  Process ID: 7892
  Account: DOMAIN\devuser

Event 4624 (Logon):
  Time: 14:20:10
  Account: DOMAIN\devuser
  Logon Type: 2 (Interactive)
  Source IP: 10.0.10.45

Event 4672 (Special Logon):
  Time: 14:20:10
  Account: DOMAIN\devuser
  Privileges: SeDebugPrivilege, SeImpersonatePrivilege, SeAssignPrimaryTokenPrivilege
```

---

### Source 5: AppLocker Configuration (Effective Policy)

```
AppLocker Policy: Enforced

Executable Rules:
- Allow: Everyone | Path: C:\Windows\* (signed)
- Allow: Everyone | Path: C:\Program Files\* (signed)
- Allow: DOMAIN\Developers | Path: C:\DevTools\* (any)
- Deny: Everyone | Path: C:\Temp\* (any)
- Deny: Everyone | Path: C:\Users\*\AppData\Local\Temp\* (any)

Script Rules (PowerShell):
- Allow: Everyone | Path: C:\Windows\System32\WindowsPowerShell\v1.0\* (signed)
- Allow: DOMAIN\Developers | Publisher: Microsoft (any version)
- Deny: Everyone | File Hash: SHA256 of known malicious scripts
```

---

## Questions

### Part A (3 points)
**Identify the suspicious outbound connections** in Source 2 (netstat). Provide the **local ports**, **remote IPs and ports**, **PID**, and **process name**. Explain why the connection to **192.168.1.100:4444** is anomalous given the network context.

### Part B (3 points)
**Analyze the PowerShell command line** in Source 4 (Event 4688). The `-enc` parameter contains a Base64-encoded command. What **MITRE ATT&CK technique** does this represent (Tactic + Technique ID + Sub-technique)? What is the **purpose of `-nop -w hidden`**?

### Part C (3 points)
**Evaluate the AppLocker policy** (Source 5) against the observed activity. The PowerShell process (PID 7892) was allowed to execute. Which **specific rule** permitted this? Was the **script content** evaluated by AppLocker? Explain why AppLocker **did not prevent** this attack.

### Part D (3 points)
The firewall (Source 1) has a **"Custom: Dev Outbound"** rule allowing TCP 80, 443, 22, 4433 to any destination. The suspicious connection uses **port 80 and 443 to 185.220.101.45**, and **port 4444 to 192.168.1.100**. Propose **two specific firewall modifications** that would block the malicious connections while preserving developer productivity. For each, state the **trade-off**.

### Part E (2 points)
The **Security Event Log** shows Event 4672 (Special Logon) with privileges including `SeDebugPrivilege`. What does this privilege allow? How does it relate to the **threat actor's ability to inject code** into other processes?

---

## Scoring Rubric (14 Points)

| Part | Points | Key Elements |
|------|--------|--------------|
| A | 3 | Local ports 50234, 50235, 50237; Remote 185.220.101.45:80/443 and 192.168.1.100:4444; PID 7892 (powershell.exe). 192.168.1.100 is RFC1918 (internal) but not in corporate 10.0.0.0/8 → suspicious lateral movement or C2. |
| B | 3 | Technique: T1059.001 (Command and Scripting Interpreter: PowerShell) — Execution tactic. Base64 encoding = obfuscation (T1027.010). `-nop` = No Profile (faster, bypasses profile scripts). `-w hidden` = WindowStyle Hidden (no visible window). |
| C | 3 | Rule: "Allow: Everyone | Path: C:\Windows\System32\WindowsPowerShell\v1.0\* (signed)" — allows powershell.exe binary. AppLocker script rules apply to .ps1 FILES, not encoded commands passed to powershell.exe. The -enc payload is not a file, so script rules don't evaluate it. |
| D | 3 | 1) Restrict "Dev Outbound" to corporate IP ranges (10.0.0.0/8, approved cloud CIDRs). Trade-off: developers can't access arbitrary GitHub/npm/GitLab without allowlist updates. 2) Add explicit block for RFC1918 outbound (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) except approved internal services. Trade-off: may break legitimate dev tools connecting to local services. |
| E | 2 | SeDebugPrivilege = allows process to attach debugger to any process (including SYSTEM), read/write memory, inject code (CreateRemoteThread, WriteProcessMemory). Used for credential theft (lsass.exe), process injection, bypassing PPL. |

---

*FRQ Practice Set 2 — Administered Apr 22, 2027 — Upload to qsec_ap_review/frq-practice/*