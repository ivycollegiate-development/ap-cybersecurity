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
                 check_fn=None, expected_files: list | None = None) -> dict:
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