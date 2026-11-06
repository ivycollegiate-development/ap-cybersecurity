# CLI Fluency Check — 10 Tasks Specification

**AP Cybersecurity — ICA 2026-27**  
**Assessment Date**: Apr 28, 2027 (Single 50-minute session)  
**Environment**: GitHub Codespaces (custom Docker image) — validated by Apr 7  
**Fallback**: Replit / Gitpod with `install-tools.sh`  
**Scoring**: Automated grader (`CLI-Check-Grader.py`) → CSV submitted via Classroom  
**Weight**: Part of AP Review Sprint (formative, prepares for AP Exam practical skills)

---

## 10 CLI Tasks (5 minutes each)

| Task | Category | Description | LO Mapping |
|------|----------|-------------|------------|
| **1** | Network Recon | Use `nmap` to scan target, identify open ports, services, OS | 2.1.C, 3.4.A |
| **2** | Traffic Analysis | Use `tcpdump`/`wireshark-cli` to extract HTTP hosts, count unique IPs | 2.2.A, 3.4.B |
| **3** | Log Analysis | Use `grep`/`awk`/`jq` to parse auth logs, find failed SSH by IP | 4.6.B, 5.6.C |
| **4** | File Forensics | Use `find`/`stat`/`file`/`strings` to locate suspicious files, extract IOCs | 4.4.A, 3.1.A |
| **5** | Crypto Operations | Use `openssl` to generate keys, create CSR, verify cert chain | 3.2.A, 3.5.B |
| **6** | Hash & Verify | Use `sha256sum`/`gpg` to verify file integrity, detect tampering | 3.1.C, 3.4.A |
| **7** | Process & Memory | Use `ps`/`lsof`/`netstat`/`ss` to find suspicious processes, connections | 4.3.A, 4.4.B |
| **8** | Script Automation | Write Bash/Python one-liner to automate multi-step check | 5.5.C, 3.4.C |
| **9** | Container Inspection | Use `docker`/`crictl` to inspect container, find privileged mounts | 4.5.A, 5.4.C |
| **10** | Git & Secrets | Use `git`/`trufflehog`/`gitleaks` to find committed secrets in repo | 5.1.A, 5.5.B |

---

## Task Details

### Task 1: Network Reconnaissance (nmap)
**Target**: `scanme.nmap.org` (or local target `10.0.10.0/24`)
**Commands**:
```bash
# TCP SYN scan, service detection, OS detection, top 1000 ports
nmap -sS -sV -O --top-ports 1000 scanme.nmap.org

# Save output in grepable format
nmap -sS -sV -O --top-ports 1000 -oG nmap_results.gnmap scanme.nmap.org
```
**Expected Output**: Parse grepable format for open ports, service names, versions.

**Grading**: Grader runs nmap, checks output file exists, parses for required fields.

---

### Task 2: Traffic Analysis (tcpdump/tshark)
**Input**: Provided PCAP file `traffic.pcap` (HTTP + DNS traffic)
**Commands**:
```bash
# Extract HTTP Host headers
tshark -r traffic.pcap -Y "http.request" -T fields -e http.host | sort -u

# Count unique source IPs
tshark -r traffic.pcap -T fields -e ip.src | sort -u | wc -l

# Find DNS queries for suspicious domains
tshark -r traffic.pcap -Y "dns.qry.name contains \"malicious\"" -T fields -e dns.qry.name
```
**Expected Output**: Text files with extracted data.

---

### Task 3: Log Analysis (grep/awk/jq)
**Input**: `auth.log` (JSON format) or traditional syslog
**Commands**:
```bash
# Count failed SSH attempts per IP (JSON)
jq -r 'select(.message | contains("Failed password")) | .source_ip' auth.json | sort | uniq -c | sort -rn

# Or traditional format
grep "Failed password" auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn

# Find successful logins after failures (brute force indicator)
grep "Accepted password" auth.log | awk '{print $1,$2,$3,$9,$11}' > accepted.log
```
**Expected Output**: Ranked list of attacking IPs.

---

### Task 4: File Forensics (find/stat/file/strings)
**Target**: Directory `/investigation` with mixed files
**Commands**:
```bash
# Find files modified in last 24h, larger than 1MB
find /investigation -type f -mtime -1 -size +1M -exec ls -lh {} \;

# Identify file types (magic bytes)
file /investigation/* | grep -v "ASCII\|text"

# Extract strings from binary
strings /investigation/suspicious.bin | grep -E "http|IP|password|key" | head -20

# Check for hidden files
find /investigation -name ".*" -type f
```
**Expected Output**: List of suspicious files with IOCs.

---

### Task 5: Crypto Operations (openssl)
**Commands**:
```bash
# Generate RSA key pair
openssl genrsa -out private.key 2048

# Extract public key
openssl rsa -in private.key -pubout -out public.key

# Create CSR
openssl req -new -key private.key -out request.csr -subj "/CN=test.example.com/O=ICA/C=US"

# Verify certificate chain
openssl verify -CAfile ca.crt server.crt

# Check certificate details
openssl x509 -in server.crt -text -noout
```
**Expected Output**: Valid key pair, CSR, verification result.

---

### Task 6: Hash & Verify (sha256sum/gpg)
**Input**: File `artifact.img` and signature `artifact.img.sig`
**Commands**:
```bash
# Generate SHA256 hash
sha256sum artifact.img > artifact.sha256

# Verify against known good hash
echo "expected_hash  artifact.img" | sha256sum -c

# Verify GPG signature
gpg --verify artifact.img.sig artifact.img

# Create detached signature
gpg --armor --detach-sign artifact.img
```
**Expected Output**: Hash match/fail, signature valid/invalid.

---

### Task 7: Process & Memory (ps/lsof/netstat/ss)
**Commands**:
```bash
# Find processes listening on network ports
ss -tlnp | grep LISTEN

# Find process with suspicious network connection
lsof -i -P | grep ESTABLISHED

# Check for processes running from /tmp or /var/tmp
ps aux | awk '$11 ~ /^\/tmp/ || $11 ~ /^\/var\/tmp/'

# Find processes with deleted executables
ls -l /proc/*/exe 2>/dev/null | grep deleted
```
**Expected Output**: List of anomalous processes.

---

### Task 8: Script Automation (Bash/Python one-liner)
**Challenge**: Write a one-liner that:
1. Scans `/var/log` for `.log` files
2. Counts lines containing "ERROR" or "CRITICAL" in last hour
3. Outputs: `filename:count` sorted by count descending

**Bash Solution**:
```bash
find /var/log -name "*.log" -exec sh -c 'c=$(grep -c -E "ERROR|CRITICAL" "$1"); [ $c -gt 0 ] && echo "$1:$c"' _ {} \; | sort -t: -k2 -rn
```

**Python Solution**:
```python
python3 -c "import os,re,glob,time; now=time.time(); print('\n'.join(sorted([f'{f}:{sum(1 for l in open(f) if re.search(r\"ERROR|CRITICAL\",l) and (now-os.path.getmtime(f))<3600)}' for f in glob.glob('/var/log/**/*.log', recursive=True)], key=lambda x: -int(x.split(':')[1]))) if int(x.split(':')[1])>0)"
```

---

### Task 9: Container Inspection (docker/crictl)
**Commands**:
```bash
# List all containers (including stopped)
crictl ps -a

# Inspect specific container for privileged config
crictl inspect <container_id> | jq '.info.config.security_context'

# Check for hostPath mounts
crictl inspect <container_id> | jq '.info.config.mounts[] | select(.host_path)'

# View container processes
crictl exec <container_id> ps aux
```
**Expected Output**: Identification of privileged container with host mount.

---

### Task 10: Git & Secrets (git/trufflehog/gitleaks)
**Commands**:
```bash
# Clone repo
git clone https://github.com/example/repo.git
cd repo

# Scan for secrets with trufflehog
trufflehog git file://. --json > trufflehog_results.json

# Or gitleaks
gitleaks detect --source . --report-format json --report-path gitleaks_results.json

# Check git history for removed secrets
git log --all --full-history --oneline -- "*secret*" "*password*" "*key*"
```
**Expected Output**: JSON report with detected secrets.

---

## Environment Specification

### Primary: GitHub Codespaces (Custom Docker Image)

**Dockerfile** (in repo at `.devcontainer/Dockerfile`):
```dockerfile
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Install security tools
RUN apt-get update && apt-get install -y \
    nmap \
    tcpdump \
    tshark \
    wireshark-common \
    jq \
    openssl \
    gnupg2 \
    docker.io \
    containerd \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python tools
RUN pip3 install --no-cache-dir trufflehog gitleaks

# Install crictl (for Kubernetes)
RUN VERSION="v1.28.0" && \
    wget -q https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz && \
    tar -xzf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin && \
    rm crictl-$VERSION-linux-amd64.tar.gz

# Set up non-root user
USER codespace
```

**devcontainer.json**:
```json
{
  "name": "AP Cybersecurity CLI Fluency",
  "build": { "dockerfile": "Dockerfile" },
  "customizations": {
    "vscode": {
      "extensions": ["ms-vscode-remote.remote-containers"]
    }
  },
  "remoteUser": "codespace",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:1": {}
  }
}
```

### Fallback: Replit / Gitpod

**install-tools.sh**:
```bash
#!/bin/bash
set -e

# Replit: uses nix, Gitpod: uses apt
if command -v nix-env &> /dev/null; then
    # Replit - use nix
    nix-env -iA nixpkgs.nmap nixpkgs.tcpdump nixpkgs.wireshark-cli nixpkgs.jq nixpkgs.openssl nixpkgs.gnupg nixpkgs.docker nixpkgs.git nixpkgs.python3 nixpkgs.pip
    pip install trufflehog gitleaks
else
    # Gitpod / Ubuntu-based
    sudo apt-get update && sudo apt-get install -y \
        nmap tcpdump tshark jq openssl gnupg2 docker.io git python3-pip
    pip3 install trufflehog gitleaks
    
    # crictl
    VERSION="v1.28.0"
    wget -q https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
    sudo tar -xzf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
    rm crictl-$VERSION-linux-amd64.tar.gz
fi

echo "Tools installed. Verifying..."
nmap --version | head -1
tcpdump --version | head -1
tshark -v | head -1
jq --version
openssl version
gpg --version
docker --version
crictl version
trufflehog --version
gitleaks version
```

---

## Automated Grader: `CLI-Check-Grader.py`

```python
#!/usr/bin/env python3
"""
CLI Fluency Check Automated Grader
Runs in student's Codespace, executes 10 tasks, outputs CSV for Classroom submission.
"""

import subprocess
import json
import csv
import os
import sys
import hashlib
from pathlib import Path
from datetime import datetime

class CLIGrader:
    def __init__(self, student_id: str, output_dir: str = "."):
        self.student_id = student_id
        self.output_dir = Path(output_dir)
        self.results = []
        self.start_time = datetime.now()
    
    def run_task(self, task_num: int, cmd: str, timeout: int = 60, 
                 check_fn=None, expected_files: list = None) -> dict:
        """Run a single task, return result dict."""
        result = {
            "task": task_num,
            "command": cmd,
            "status": "FAIL",
            "score": 0,
            "max_score": 1,
            "output": "",
            "error": "",
            "duration_sec": 0
        }
        
        start = datetime.now()
        try:
            proc = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=timeout,
                cwd=self.output_dir
            )
            result["output"] = proc.stdout
            result["error"] = proc.stderr
            result["duration_sec"] = (datetime.now() - start).total_seconds()
            
            if proc.returncode == 0:
                if check_fn:
                    passed, details = check_fn(proc.stdout, self.output_dir)
                    result["status"] = "PASS" if passed else "FAIL"
                    result["score"] = 1 if passed else 0
                    result["output"] = details
                elif expected_files:
                    missing = [f for f in expected_files if not Path(f).exists()]
                    result["status"] = "PASS" if not missing else "FAIL"
                    result["score"] = 1 if not missing else 0
                    result["output"] = f"Files: {', '.join(expected_files)}" + (f" Missing: {missing}" if missing else "")
                else:
                    result["status"] = "PASS"
                    result["score"] = 1
            else:
                result["status"] = "FAIL"
                result["score"] = 0
                
        except subprocess.TimeoutExpired:
            result["error"] = f"Timeout after {timeout}s"
        except Exception as e:
            result["error"] = str(e)
        
        self.results.append(result)
        return result
    
    def grade_all(self):
        """Run all 10 tasks."""
        tasks = [
            # Task 1: Network Recon
            (1, "nmap -sS -sV -O --top-ports 100 -oG nmap_results.gnmap scanme.nmap.org",
             120, lambda out, d: (Path("nmap_results.gnmap").exists() and "Ports:" in Path("nmap_results.gnmap").read_text(), "nmap output saved")),
            
            # Task 2: Traffic Analysis (uses provided pcap)
            (2, "tshark -r traffic.pcap -Y 'http.request' -T fields -e http.host | sort -u > http_hosts.txt",
             60, lambda out, d: (Path("http_hosts.txt").exists() and len(Path("http_hosts.txt").read_text().strip().split()) > 0, "HTTP hosts extracted")),
            
            # Task 3: Log Analysis
            (3, "jq -r 'select(.message | contains(\"Failed password\")) | .source_ip' auth.json | sort | uniq -c | sort -rn > ssh_failures.txt",
             60, lambda out, d: (Path("ssh_failures.txt").exists() and len(Path("ssh_failures.txt").read_text().strip().split()) > 0, "SSH failures parsed")),
            
            # Task 4: File Forensics
            (4, "find /investigation -type f -mtime -1 -size +1M -exec ls -lh {} \\; > large_files.txt 2>/dev/null; file /investigation/* | grep -v 'ASCII\\|text' > binary_files.txt 2>/dev/null",
             60, lambda out, d: (Path("large_files.txt").exists() or Path("binary_files.txt").exists(), "Forensics output saved")),
            
            # Task 5: Crypto Operations
            (5, "openssl genrsa -out private.key 2048 && openssl rsa -in private.key -pubout -out public.key && openssl req -new -key private.key -out request.csr -subj '/CN=test.example.com/O=ICA/C=US'",
             60, lambda out, d: (Path("private.key").exists() and Path("public.key").exists() and Path("request.csr").exists(), "Keys and CSR generated")),
            
            # Task 6: Hash & Verify
            (6, "echo 'test content' > artifact.img && sha256sum artifact.img > artifact.sha256 && gpg --batch --yes --passphrase '' --pinentry-mode loopback --quick-generate-key 'test@test.com' default default never 2>/dev/null && gpg --armor --detach-sign artifact.img",
             60, lambda out, d: (Path("artifact.sha256").exists() and Path("artifact.img.asc").exists(), "Hash and signature created")),
            
            # Task 7: Process & Memory
            (7, "ss -tlnp > listeners.txt 2>/dev/null; lsof -i -P | grep ESTABLISHED > established.txt 2>/dev/null; ls -l /proc/*/exe 2>/dev/null | grep deleted > deleted_exe.txt 2>/dev/null",
             30, lambda out, d: (Path("listeners.txt").exists() and Path("established.txt").exists(), "Process/network output saved")),
            
            # Task 8: Script Automation
            (8, "find /var/log -name '*.log' -exec sh -c 'c=$(grep -c -E \"ERROR|CRITICAL\" \"$1\" 2>/dev/null); [ $c -gt 0 ] && echo \"$1:$c\"' _ {} \\; 2>/dev/null | sort -t: -k2 -rn > error_counts.txt",
             30, lambda out, d: (Path("error_counts.txt").exists(), "Error counts generated")),
            
            # Task 9: Container Inspection
            (9, "crictl ps -a > containers.txt 2>/dev/null; crictl inspect $(crictl ps -q | head -1) 2>/dev/null | jq '.info.config.security_context' > security_context.json 2>/dev/null",
             30, lambda out, d: (Path("containers.txt").exists(), "Container info saved")),
            
            # Task 10: Git & Secrets
            (10, "git clone --depth 1 https://github.com/trufflesecurity/test_keys.git repo_test 2>/dev/null && trufflehog git file://repo_test --json > secrets.json 2>/dev/null",
             60, lambda out, d: (Path("secrets.json").exists() and len(Path("secrets.json").read_text().strip()) > 2, "Secrets scan completed")),
        ]
        
        for task in tasks:
            self.run_task(*task)
        
        return self.results
    
    def export_csv(self):
        """Export results to CSV for Classroom submission."""
        timestamp = self.start_time.strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"cli_fluency_{self.student_id}_{timestamp}.csv"
        
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                "student_id", "task", "status", "score", "max_score", 
                "command", "output", "error", "duration_sec", "timestamp"
            ])
            writer.writeheader()
            for r in self.results:
                row = {"student_id": self.student_id, "timestamp": self.start_time.isoformat()}
                row.update(r)
                writer.writerow(row)
        
        # Also create summary
        total_score = sum(r["score"] for r in self.results)
        max_score = sum(r["max_score"] for r in self.results)
        summary = {
            "student_id": self.student_id,
            "total_score": total_score,
            "max_score": max_score,
            "percentage": round(total_score / max_score * 100, 1) if max_score > 0 else 0,
            "completed_at": datetime.now().isoformat(),
            "task_details": self.results
        }
        
        summary_file = self.output_dir / f"cli_fluency_{self.student_id}_{timestamp}_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        return filename, summary_file

def main():
    student_id = os.environ.get("STUDENT_ID", "unknown")
    grader = CLIGrader(student_id)
    print(f"Starting CLI Fluency Check for {student_id}...")
    grader.grade_all()
    csv_file, json_file = grader.export_csv()
    print(f"Results saved to {csv_file} and {json_file}")
    
    # Print summary
    total = sum(r["score"] for r in grader.results)
    print(f"\nScore: {total}/10")
    for r in grader.results:
        print(f"  Task {r['task']}: {r['status']} ({r['score']}/1)")

if __name__ == "__main__":
    main()
```

---

## Teacher Validation (Apr 7 Deadline)

**Validation Checklist** (run in reference Codespace):
- [ ] All 10 tasks complete without error
- [ ] Each task produces expected output files
- [ ] Grader correctly scores PASS/FAIL
- [ ] CSV output format matches Classroom import spec
- [ ] Execution time < 40 minutes (leaves 10 min buffer)
- [ ] Network access works for nmap/trufflehog tasks
- [ ] Docker-in-Docker works for crictl task
- [ ] GPG key generation works in container

**Validation Command**:
```bash
# In teacher's reference Codespace
STUDENT_ID=VALIDATION_REF python3 CLI-Check-Grader.py
# Verify output CSV has 10 rows, all PASS
```

---

## Classroom Submission Format

**CSV Columns**:
| student_id | task | status | score | max_score | command | output | error | duration_sec | timestamp |

**Import to Google Classroom**:
1. Create assignment "CLI Fluency Check — Apr 28"
2. Attach CSV as "Students edit file" → NO, use "Make a copy for each student"
3. Students run grader, CSV auto-generated in workspace
4. Students attach CSV to assignment

**Alternative**: GitHub Classroom Autograding
- Create `.github/classroom/autograding.json` with test cases
- Each task = separate autograding test
- Runs on push to `cli-fluency` branch

---

## Scoring & Feedback

| Score | Proficiency |
|-------|-------------|
| 10/10 | Expert — Ready for AP Exam practical |
| 8-9/10 | Proficient — Minor gaps |
| 6-7/10 | Developing — Needs practice |
| <6/10 | Beginning — Remediation required |

**Feedback delivered**: Auto-generated summary JSON + CSV attached to Classroom assignment.

---

*CLI Fluency Check Specification — Administered Apr 28, 2027 — Upload to qsec_ap_review/cli-fluency/*