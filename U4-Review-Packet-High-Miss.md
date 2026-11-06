# Unit 4 Review Packet — High-Miss Bank Items

**AP Cybersecurity — ICA 2026-27**  
**Unit**: 4 — System Security  
**Source**: High-Miss Bank (Stage 1: Mar 29, Stage 2: Apr 11–16)  
**Target**: AP Exam Review — May 5, 2027

---

## High-Miss Items (6 Questions)

### HM-019 | LO 4.1.B | Miss Rate: 74%
**Question**: Which **Windows security feature** uses virtualization-based security (VBS) to isolate secrets (like NTLM hashes, Kerberos tickets) from the normal OS?

A) Windows Defender Credential Guard  
B) Windows Defender Application Guard  
C) Windows Defender Exploit Guard  
D) Windows Defender Application Control  

**Correct Answer**: A  
**Distractor Analysis**:  
- Credential Guard = VBS isolation for secrets (LSASS protection)  
- Application Guard = isolate untrusted apps (Edge/Office) in container  
- Exploit Guard = exploit mitigations (ASLR, CFG, etc.)  
- Application Control = code integrity (whitelisting)  
**Key Concept**: Credential Guard = "Virtual Secure Mode" isolates LSASS. Requires TPM 2.0, UEFI, Windows 10/11 Enterprise.

---

### HM-020 | LO 4.2.C | Miss Rate: 70%
**Question**: In **Linux**, which file stores **hashed passwords** for local users (readable only by root)?

A) /etc/passwd  
B) /etc/shadow  
C) /etc/gshadow  
D) /etc/security/passwd  

**Correct Answer**: B  
**Distractor Analysis**:  
- /etc/passwd = user info (world-readable), passwords = 'x' placeholder  
- /etc/shadow = actual hashes (root-only), aging info  
- /etc/gshadow = group passwords  
**Key Concept**: Shadow file = /etc/shadow. Hash format: $id$salt$hash (id: 1=MD5, 5=SHA-256, 6=SHA-512, y=yescrypt).

---

### HM-021 | LO 4.3.A | Miss Rate: 77%
**Question**: **Address Space Layout Randomization (ASLR)** randomizes the memory layout of which areas?

A) Stack, heap, libraries, executable base  
B) Only stack and heap  
C) Only shared libraries  
D) Kernel memory only  

**Correct Answer**: A  
**Distractor Analysis**:  
- Full ASLR = stack + heap + libraries (shared objects) + executable base + VDSO  
- B: Incomplete (missing libraries, executable)  
- C: Incomplete  
- D: KASLR is separate (kernel ASLR)  
**Key Concept**: ASLR defeats ROP/JOP by making addresses unpredictable. Entropy matters: 64-bit = more entropy than 32-bit.

---

### HM-022 | LO 4.4.B | Miss Rate: 66%
**Question**: A **buffer overflow** vulnerability allows an attacker to overwrite the **return address** on the stack. Which mitigation makes this exploit unreliable by randomizing stack addresses?

A) Stack Canaries  
B) ASLR  
C) DEP/NX (Non-Executable Stack)  
D) Control Flow Guard (CFG)  

**Correct Answer**: B  
**Distractor Analysis**:  
- ASLR = randomizes stack base → attacker can't predict return address location  
- Canaries = detect overwrite before return (different mechanism)  
- DEP/NX = prevents executing shellcode on stack (but ROP still works)  
- CFG = validates indirect call targets (Windows)  
**Key Concept**: ASLR + DEP + Canaries = defense in depth. None alone is sufficient.

---

### HM-023 | LO 4.5.C | Miss Rate: 61%
**Question**: Which **Linux capability** allows a process to bypass all permission checks (read/write/execute) on files?

A) CAP_DAC_OVERRIDE  
B) CAP_SYS_ADMIN  
C) CAP_NET_RAW  
D) CAP_CHOWN  

**Correct Answer**: A  
**Distractor Analysis**:  
- CAP_DAC_OVERRIDE = bypass Discretionary Access Control (read/write/execute checks)  
- CAP_SYS_ADMIN = "superpower" capability (mount, namespace, etc.) — broader but not specifically DAC  
- CAP_NET_RAW = raw sockets  
- CAP_CHOWN = change file ownership  
**Key Concept**: Capabilities split root privileges. CAP_DAC_OVERRIDE = "ignore file permissions." Dangerous if granted.

---

### HM-024 | LO 4.6.A | Miss Rate: 57%
**Question**: **SELinux** operates in which mode when it **logs violations but does not enforce** policy?

A) Enforcing  
B) Permissive  
C) Disabled  
D) Targeted  

**Correct Answer**: B  
**Distractor Analysis**:  
- Enforcing = block + log  
- Permissive = log only (audit mode) — used for policy development  
- Disabled = no SELinux at all  
- Targeted = policy type (not mode), protects targeted daemons  
**Key Concept**: Modes: Enforcing/Permissive/Disabled. Types: Targeted/MLS. Permissive = debug mode.

---

## LO Mapping Table

| Item | LO Code | Framework Reference | Concept Category |
|------|---------|---------------------|------------------|
| HM-019 | 4.1.B | Unit 4 Topic 1.B | Windows / Credential Guard / VBS |
| HM-020 | 4.2.C | Unit 4 Topic 2.C | Linux / Shadow File |
| HM-021 | 4.3.A | Unit 4 Topic 3.A | ASLR / Memory Protection |
| HM-022 | 4.4.B | Unit 4 Topic 4.B | Buffer Overflow / ASLR Mitigation |
| HM-023 | 4.5.C | Unit 4 Topic 5.C | Linux Capabilities |
| HM-024 | 4.6.A | Unit 4 Topic 6.A | SELinux Modes |

---

## Mini-Lesson: Top 2 Missed LOs

### LO 4.3.A — ASLR (Address Space Layout Randomization) (Miss Rate 77%)

**What ASLR Randomizes**:
```
┌─────────────────────────────────────────┐
│           High Memory                    │
├─────────────────────────────────────────┤
│  Stack (random offset)                  │
├─────────────────────────────────────────┤
│  Memory Mapping Segment (libs, mmap)    │  ← Shared libraries randomized
├─────────────────────────────────────────┤
│  Heap (random offset)                   │
├─────────────────────────────────────────┤
│  BSS / Data                             │
├─────────────────────────────────────────┤
│  Executable Base (PIE)                  │  ← Position Independent Executable
├─────────────────────────────────────────┤
│           Low Memory                     │
```

**Entropy** (bits of randomness):
| Architecture | Stack | Heap | Libraries | Executable (PIE) |
|--------------|-------|------|-----------|------------------|
| 32-bit | 8-16 | 8-16 | 8-16 | 8-16 |
| 64-bit | 28-32 | 28-32 | 28-32 | 28-32 |

**Bypass Techniques** (for awareness):
- Information leaks (format string, read primitives) to disclose addresses
- Partial overwrites (lower bytes only)
- JIT spraying (heap spraying)
- Relative addressing (PIE bypass)

**Mitigations Combined**:
| Mitigation | What It Stops | Bypassed By |
|------------|---------------|-------------|
| ASLR | Predictable addresses | Info leaks |
| DEP/NX | Code execution on stack/heap | ROP/JOP |
| Stack Canaries | Stack smashing detection | Info leaks, non-linear overflows |
| CFG/CET | Indirect call validation | ROP with valid gadgets |

**Exam Tip**: ASLR = randomization. DEP/NX = non-executable memory. Canaries = stack cookie. They work TOGETHER.

---

### LO 4.1.B — Windows Credential Guard & VBS (Miss Rate 74%)

**Virtualization-Based Security (VBS)**:
- Uses Hyper-V hypervisor to create **Virtual Secure Mode (VSM)**
- Isolated memory region that even kernel (Ring 0) cannot access
- Runs **Trustlets** (small, signed code modules)

**Credential Guard**:
```
┌─────────────────────────────────────────────────────────────┐
│                        Normal OS (Ring 0)                    │
│  LSASS (stubs) → RPC → VSM                                   │
└──────────────────────────────────┬──────────────────────────┘
                                   │ Hypercall
┌──────────────────────────────────▼──────────────────────────┐
│              Virtual Secure Mode (VSM)                       │
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │  Isolated LSASS │  │   Key Protection │                   │
│  │  (NTLM, Kerb)   │  │   (TPM-backed)   │                   │
│  └─────────────────┘  └─────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

**What It Protects**:
- NTLM password hashes
- Kerberos tickets (TGTs, service tickets)
- Credential Manager secrets
- Domain credentials

**Requirements**:
- Windows 10/11 Enterprise or Education
- TPM 2.0
- UEFI with Secure Boot
- Virtualization enabled in BIOS
- Hyper-V feature installed

**Related Features**:
| Feature | Purpose | Uses VBS? |
|---------|---------|-----------|
| Credential Guard | Protect secrets | Yes |
| HVCI (Hypervisor-Protected Code Integrity) | Kernel code integrity | Yes |
| Application Guard | Isolate untrusted apps | Yes |
| Exploit Guard | Exploit mitigations | No (user-mode) |

---

## Practice Set (5 New Items)

### P16 | LO 4.1.A
**Question**: **User Account Control (UAC)** in Windows primarily mitigates:

A) Remote code execution  
B) Privilege escalation by malware  
C) Network sniffing  
D) Phishing attacks  
**Answer**: B — UAC = prompt for elevation. Prevents silent admin privilege use.

### P17 | LO 4.2.A
**Question**: The **root** user in Linux has UID:

A) 0  
B) 1  
C) 1000  
D) 65535  
**Answer**: A — UID 0 = root. All permission checks bypassed for UID 0.

### P18 | LO 4.3.B
**Question**: **DEP (Data Execution Prevention)** / **NX (No-Execute)** bit prevents:

A) Buffer overflow from occurring  
B) Code execution on stack/heap  
C) ASLR from being bypassed  
D) Return address overwrite  
**Answer**: B — NX = marks memory pages non-executable. Stops shellcode on stack. ROP bypasses.

### P19 | LO 4.4.A
**Question**: **Format string vulnerability** occurs when:

A) User input passed directly as format string to printf()  
B) Buffer overflow in sprintf()  
C) Integer overflow in format parsing  
D) Uninitialized format string  
**Answer**: A — printf(user_input) allows %n to write arbitrary memory, %s to read.

### P20 | LO 4.6.B
**Question**: **AppArmor** differs from SELinux in that it:

A) Uses path-based profiles (not labels)  
B) Requires MLS (Multi-Level Security)  
C) Only works on Red Hat systems  
D) Cannot be disabled  
**Answer**: A — AppArmor = path-based, simpler. SELinux = label-based, more granular.

---

## Self-Check Answer Key

| Item | Answer | LO | Explanation |
|------|--------|-----|-------------|
| HM-019 | A | 4.1.B | Credential Guard = VBS for secrets |
| HM-020 | B | 4.2.C | /etc/shadow = hashed passwords |
| HM-021 | A | 4.3.A | ASLR = stack, heap, libs, exe |
| HM-022 | B | 4.4.B | ASLR randomizes stack address |
| HM-023 | A | 4.5.C | CAP_DAC_OVERRIDE = bypass DAC |
| HM-024 | B | 4.6.A | Permissive = log only |
| P16 | B | 4.1.A | UAC = privilege escalation mitigation |
| P17 | A | 4.2.A | Root UID = 0 |
| P18 | B | 4.3.B | DEP/NX = non-executable stack |
| P19 | A | 4.4.A | Format string = user input as format |
| P20 | A | 4.6.B | AppArmor = path-based |

---

## Study Plan Template

| LO Code | Concept | Current Mastery (1-5) | Review Action | Target Date |
|---------|---------|----------------------|---------------|-------------|
| 4.3.A | ASLR Details | ___ | Mini-lesson, entropy table | Apr 20 |
| 4.1.B | Credential Guard / VBS | ___ | Mini-lesson, architecture diagram | Apr 20 |
| 4.4.B | Buffer Overflow + ASLR | ___ | ROP chain concept, mitigations | Apr 21 |
| 4.2.C | Linux Shadow File | ___ | Hash format $id$salt$hash | Apr 21 |
| 4.5.C | Linux Capabilities | ___ | CAP_DAC_OVERRIDE vs SYS_ADMIN | Apr 22 |
| 4.6.A | SELinux Modes | ___ | Enforcing/Permissive/Disabled | Apr 22 |

---

*Packet generated from High-Miss Bank — Upload to qsec_ap_review/review-packets/*