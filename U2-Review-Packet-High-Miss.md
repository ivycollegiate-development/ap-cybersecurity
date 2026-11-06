# Unit 2 Review Packet — High-Miss Bank Items

**AP Cybersecurity — ICA 2026-27**  
**Unit**: 2 — Network Security  
**Source**: High-Miss Bank (Stage 1: Mar 29, Stage 2: Apr 11–16)  
**Target**: AP Exam Review — May 5, 2027

---

## High-Miss Items (6 Questions)

### HM-007 | LO 2.1.C | Miss Rate: 78%
**Question**: Which **TCP flag combination** in a port scan indicates a **NULL scan** (no flags set)?

A) SYN  
B) SYN, ACK  
C) FIN, URG, PSH  
D) No flags set  

**Correct Answer**: D  
**Distractor Analysis**:  
- A: SYN scan (half-open)  
- B: SYN/ACK response from open port  
- C: XMAS scan (FIN+URG+PSH)  
**Key Concept**: NULL scan = no TCP flags. Used to bypass simple firewall rules that only block SYN.

---

### HM-008 | LO 2.2.B | Miss Rate: 71%
**Question**: A network administrator configures a **stateful firewall** rule allowing outbound HTTPS. An internal user initiates HTTPS to external server. The return traffic is allowed because:

A) The firewall has a rule allowing inbound port 443  
B) The firewall tracks connection state in its state table  
C) The return traffic uses a different port  
D) HTTPS uses UDP which is stateless  

**Correct Answer**: B  
**Distractor Analysis**:  
- Stateful firewall: allows return traffic for ESTABLISHED connections without explicit inbound rule  
- A: Not needed for stateful firewall  
- C: Return traffic uses ephemeral source port, but state table matches it  
- D: HTTPS uses TCP (stateful), not UDP  
**Key Concept**: Stateful inspection = connection tracking. "Established, related" traffic auto-allowed.

---

### HM-009 | LO 2.3.D | Miss Rate: 82%
**Question**: Which **DNS record type** is used to delegate a subdomain to another nameserver?

A) A  
B) CNAME  
C) NS  
D) MX  

**Correct Answer**: C  
**Distractor Analysis**:  
- A: Maps domain to IPv4 address  
- B: Alias to another domain name  
- D: Mail exchanger (email routing)  
**Key Concept**: NS (Name Server) record delegates authority. Critical for subdomain takeover attacks if misconfigured.

---

### HM-010 | LO 2.4.A | Miss Rate: 69%
**Question**: An attacker performs **ARP poisoning** on a local network. Which layer of the OSI model does this attack target?

A) Layer 1 — Physical  
B) Layer 2 — Data Link  
C) Layer 3 — Network  
D) Layer 4 — Transport  

**Correct Answer**: B  
**Distractor Analysis**:  
- ARP operates at Layer 2 (Data Link), mapping IP (L3) to MAC (L2)  
- ARP poisoning = sending fake ARP replies to associate attacker MAC with victim IP  
**Key Concept**: ARP is L2 protocol. Mitigation: Dynamic ARP Inspection (DAI), static ARP entries, VPN.

---

### HM-011 | LO 2.5.C | Miss Rate: 64%
**Question**: Which **WPA3** feature prevents offline dictionary attacks on captured handshakes?

A) AES-CCMP encryption  
B) Simultaneous Authentication of Equals (SAE)  
C) Protected Management Frames (PMF)  
D) 192-bit security suite  

**Correct Answer**: B  
**Distractor Analysis**:  
- SAE (Dragonfly handshake) replaces WPA2's 4-way handshake. Uses zero-knowledge proof — no password hash transmitted.  
- A: Encryption, not authentication  
- C: PMF protects management frames (deauth), not handshake  
- D: Enterprise/optional, not the anti-dictionary feature  
**Key Concept**: WPA3-Personal uses SAE. WPA2-Personal vulnerable to KRACK/offline cracking.

---

### HM-012 | LO 2.6.B | Miss Rate: 59%
**Question**: A **VPN** using IPsec in **tunnel mode** encrypts:

A) Only the payload (data)  
B) The entire original IP packet (header + payload)  
C) Only the TCP/UDP header  
D) The IP header but not payload  

**Correct Answer**: B  
**Distractor Analysis**:  
- Tunnel mode: encapsulates entire original packet (new IP header + ESP + original IP header + payload)  
- Transport mode: only payload + transport header (original IP header stays)  
**Key Concept**: Tunnel mode = site-to-site VPN, full packet encryption. Transport mode = end-to-end host communication.

---

## LO Mapping Table

| Item | LO Code | Framework Reference | Concept Category |
|------|---------|---------------------|------------------|
| HM-007 | 2.1.C | Unit 2 Topic 1.C | TCP/IP / Port Scanning |
| HM-008 | 2.2.B | Unit 2 Topic 2.B | Stateful Firewall |
| HM-009 | 2.3.D | Unit 2 Topic 3.D | DNS / Subdomain Delegation |
| HM-010 | 2.4.A | Unit 2 Topic 4.A | ARP / Layer 2 Attacks |
| HM-011 | 2.5.C | Unit 2 Topic 5.C | Wireless / WPA3 |
| HM-012 | 2.6.B | Unit 2 Topic 6.B | VPN / IPsec Modes |

---

## Mini-Lesson: Top 2 Missed LOs

### LO 2.3.D — DNS Subdomain Delegation & NS Records (Miss Rate 82%)

**DNS Hierarchy & Delegation**:
```
Root (.) → .com → example.com → sub.example.com
                ↓                    ↓
           NS: a.gtld-servers.net   NS: ns1.sub.example.com
```

**NS Record Purpose**: Delegates authority for a zone to specific nameservers.

**Subdomain Takeover Risk**:
1. Org creates `app.example.com` → NS records point to `cloud.provider.com`
2. Service discontinued, DNS record NOT removed
3. Attacker claims `cloud.provider.com` subdomain
4. Attacker serves content on `app.example.com`

**Prevention**:
- Monitor for dangling NS/CNAME records
- Automate DNS cleanup with infrastructure changes
- Use `dig +trace` to verify delegation chain

**Record Types Quick Reference**:
| Type | Purpose | Example |
|------|---------|---------|
| A | IPv4 address | `example.com → 192.0.2.1` |
| AAAA | IPv6 address | `example.com → 2001:db8::1` |
| CNAME | Alias | `www → example.com` |
| **NS** | **Delegation** | **`sub → ns1.sub.example.com`** |
| MX | Mail server | `example.com → mail.example.com` |
| TXT | Arbitrary text | SPF, DKIM, verification |
| SOA | Start of Authority | Zone admin, serial, timers |

---

### LO 2.1.C — TCP Flag Combinations & Scan Types (Miss Rate 78%)

**TCP Flags** (in order): `URG, ACK, PSH, RST, SYN, FIN`

| Scan Type | Flags Set | Purpose | Detection |
|-----------|-----------|---------|-----------|
| **SYN** | SYN | Half-open, stealthy | Common, logged |
| **NULL** | **None** | Bypass SYN-only filters | Easy to detect (abnormal) |
| **FIN** | FIN | Bypass some firewalls | RFC 793: closed→RST, open→drop |
| **XMAS** | FIN, URG, PSH | "Light up like XMAS tree" | Same as FIN |
| **ACK** | ACK | Map firewall rules | Stateful firewalls block |
| **SYN/ACK** | SYN, ACK | Rare, confuse simple IDS | Anomalous |

**RFC 793 Response Logic**:
| Port State | SYN Scan | NULL/FIN/XMAS Scan |
|------------|----------|-------------------|
| **Open** | SYN/ACK | **No response** (drop) |
| **Closed** | RST | **RST** |
| **Filtered** | No response / ICMP | No response / ICMP |

**Key Insight**: NULL/FIN/XMAS scans differentiate open vs closed by **presence/absence of RST**. Open ports drop the packet (per RFC), closed ports respond RST.

**Nmap Commands**:
```bash
nmap -sS target      # SYN scan (default, requires root)
nmap -sN target      # NULL scan
nmap -sF target      # FIN scan
nmap -sX target      # XMAS scan
nmap -sA target      # ACK scan
```

---

## Practice Set (5 New Items)

### P6 | LO 2.1.A
**Question**: The **three-way handshake** establishes a TCP connection. What is the correct sequence?

A) SYN → SYN/ACK → ACK  
B) SYN → ACK → SYN/ACK  
C) SYN/ACK → SYN → ACK  
D) ACK → SYN → SYN/ACK  
**Answer**: A — Client SYN, Server SYN/ACK, Client ACK.

### P7 | LO 2.2.A
**Question**: A **stateless firewall** (packet filter) makes decisions based on:

A) Connection state table  
B) Individual packet headers only  
C) Application-layer content  
D) User identity  
**Answer**: B — Stateless = each packet evaluated in isolation (5-tuple: src/dst IP, src/dst port, protocol).

### P8 | LO 2.4.B
**Question**: **DHCP snooping** on a switch prevents which attack?

A) ARP poisoning  
B) Rogue DHCP server  
C) VLAN hopping  
D) MAC flooding  
**Answer**: B — DHCP snooping trusts only designated DHCP server ports, drops DHCP responses from untrusted ports.

### P9 | LO 2.5.A
**Question**: **WPA2-Personal** uses which authentication method?

A) 802.1X / RADIUS  
B) Pre-Shared Key (PSK)  
C) SAE (Dragonfly)  
D) Certificate-based  
**Answer**: B — WPA2-Personal = PSK. WPA2-Enterprise = 802.1X. WPA3-Personal = SAE.

### P10 | LO 2.6.A
**Question**: **SSL/TLS** operates at which OSI layer?

A) Layer 4 — Transport  
B) Layer 5 — Session  
C) Layer 6 — Presentation  
D) Layer 7 — Application  
**Answer**: C — TLS = Presentation layer (encryption, compression). Often said "between transport and application."

---

## Self-Check Answer Key

| Item | Answer | LO | Explanation |
|------|--------|-----|-------------|
| HM-007 | D | 2.1.C | NULL scan = no flags |
| HM-008 | B | 2.2.B | Stateful = connection tracking |
| HM-009 | C | 2.3.D | NS = delegation |
| HM-010 | B | 2.4.A | ARP = Layer 2 |
| HM-011 | B | 2.5.C | SAE = anti-dictionary |
| HM-012 | B | 2.6.B | Tunnel mode = full packet |
| P6 | A | 2.1.A | SYN → SYN/ACK → ACK |
| P7 | B | 2.2.A | Stateless = per-packet |
| P8 | B | 2.4.B | DHCP snooping = rogue DHCP |
| P9 | B | 2.5.A | WPA2-Personal = PSK |
| P10 | C | 2.6.A | TLS = Presentation (L6) |

---

## Study Plan Template

| LO Code | Concept | Current Mastery (1-5) | Review Action | Target Date |
|---------|---------|----------------------|---------------|-------------|
| 2.3.D | DNS Delegation / NS | ___ | Mini-lesson, dig practice | Apr 20 |
| 2.1.C | TCP Scan Types | ___ | Mini-lesson, nmap flags | Apr 20 |
| 2.2.B | Stateful Firewall | ___ | Practice rule scenarios | Apr 21 |
| 2.5.C | WPA3 SAE | ___ | Compare WPA2 vs WPA3 | Apr 21 |
| 2.4.A | ARP Poisoning | ___ | Layer 2 attack summary | Apr 22 |
| 2.6.B | IPsec Modes | ___ | Tunnel vs Transport table | Apr 22 |

---

*Packet generated from High-Miss Bank — Upload to qsec_ap_review/review-packets/*