# FRQ Practice Set 3 — Device Security Analysis (Set C)

**AP Cybersecurity — ICA 2026-27**  
**Format**: Device Security Analysis FRQ (matches official AP exam)  
**Time**: 50 minutes  
**Date**: Apr 27, 2027  
**Points**: 14

---

## Scenario: Kubernetes Cluster Node Compromise

You are investigating a Kubernetes worker node (`k8s-worker-3`, IP: 10.0.20.15) in a production cluster. The cluster runs Kubernetes 1.28 with containerd runtime. At 22:15 UTC, the CSPM tool detected a "privileged container" running on this node. You have collected the following artifacts:

---

### Source 1: Network Policy (Calico) for Namespace `production`

```yaml
apiVersion: projectcalico.org/v3
kind: NetworkPolicy
metadata:
  name: production-default-deny
  namespace: production
spec:
  selector: all()
  types:
  - Ingress
  - Egress
  ingress:
  - action: Allow
    protocol: TCP
    destination:
      ports: [8080, 8443]
    source:
      namespaceSelector: ingress-nginx
  - action: Allow
    protocol: TCP
    destination:
      ports: [9090]
    source:
      namespaceSelector: monitoring
  egress:
  - action: Allow
    protocol: TCP
    destination:
      ports: [53, 443]
      selector: 'k8s-app == "coredns"'
  - action: Allow
    protocol: UDP
    destination:
      ports: [53]
      selector: 'k8s-app == "coredns"'
  - action: Allow
    protocol: TCP
    destination:
      ports: [443]
      namespaceSelector: external-apis
```

---

### Source 2: Container List (`crictl ps -a` collected 22:20 UTC)

```
CONTAINER           IMAGE               CREATED              STATE      NAME                      ATTEMPT  POD ID
a1b2c3d4e5f6        nginx:1.25          2 hours ago          Running    nginx-prod                0        p1
f2e3d4c5b6a7        myapp:latest        2 hours ago          Running    app-prod                  0        p1
9a8b7c6d5e4f        alpine:latest       15 minutes ago       Running    suspicious-sidecar        0        p2
b3c4d5e6f7a8        busybox:latest      15 minutes ago       Running    attacker-shell            0        p2
```

---

### Source 3: Pod Details (`kubectl get pod -n production p2 -o yaml`)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: p2
  namespace: production
  labels:
    app: debug-tools
  annotations:
    kubernetes.io/psp: privileged-psp
spec:
  serviceAccountName: cluster-admin-sa
  containers:
  - name: suspicious-sidecar
    image: alpine:latest
    command: ["sleep", "3600"]
    securityContext:
      privileged: true
      capabilities:
        add: ["SYS_ADMIN", "CAP_DAC_OVERRIDE", "CAP_SYS_PTRACE"]
    volumeMounts:
    - name: host-root
      mountPath: /host
  - name: attacker-shell
    image: busybox:latest
    command: ["sh", "-c", "while true; do sleep 30; done"]
    securityContext:
      privileged: true
  volumes:
  - name: host-root
    hostPath:
      path: /
      type: Directory
  nodeName: k8s-worker-3
```

---

### Source 4: Audit Log (`/var/log/audit/audit.log` on k8s-worker-3, 22:10–22:20 UTC)

```
type=SYSCALL msg=audit(1679437800.123:4567): arch=c000003e syscall=257 success=yes exit=3 a0=ffffff9c a1=7ffeefbff5b0 a2=90800 a3=0 items=2 ppid=1234 pid=9999 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=(none) ses=4294967295 comm="nsenter" exe="/usr/bin/nsenter" key="container_escape"
type=SYSCALL msg=audit(1679437800.124:4568): arch=c000003e syscall=257 success=yes exit=4 a0=ffffff9c a1=7ffeefbff5c0 a2=90800 a3=0 items=2 ppid=1234 pid=9999 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 egid=0 fsgid=0 tty=(none) ses=4294967295 comm="nsenter" exe="/usr/bin/nsenter" key="container_escape"
type=SYSCALL msg=audit(1679437800.125:4569): arch=c000003e syscall=2 success=yes exit=5 a0=3 a1=7ffeefbff5d0 a2=0 a3=0 items=1 ppid=9999 pid=10000 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=(none) ses=4294967295 comm="cat" exe="/usr/bin/cat" key="sensitive_file"
type=SYSCALL msg=audit(1679437800.126:4570): arch=c000003e syscall=2 success=yes exit=6 a0=3 a1=7ffeefbff5e0 a2=0 a3=0 items=1 ppid=9999 pid=10001 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=(none) ses=4294967295 comm="cat" exe="/usr/bin/cat" key="sensitive_file"
```

---

### Source 5: RBAC Configuration (ClusterRoleBinding)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cluster-admin-binding
subjects:
- kind: ServiceAccount
  name: cluster-admin-sa
  namespace: production
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: rbac.authorization.k8i.io/v1
kind: Role
metadata:
  name: pod-creator
  namespace: production
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["create", "get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: dev-pod-creator
  namespace: production
subjects:
- kind: User
  name: devuser
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-creator
  apiGroup: rbac.authorization.k8s.io
```

---

## Questions

### Part A (3 points)
**Analyze the Pod specification** (Source 3). Identify **three security misconfigurations** that violate Kubernetes security best practices. For each, explain the **risk** it introduces.

### Part B (3 points)
**Examine the NetworkPolicy** (Source 1). The suspicious pod (p2) has containers with `hostNetwork: false` (default). Can this pod **initiate outbound connections** to:
1. `k8s-worker-1` (10.0.20.10) on port 22 (SSH)?
2. An external API at `api.example.com` (port 443)?
3. The Kubernetes API server (10.0.0.1:6443)?
For each, answer **Yes/No** and cite the **specific policy rule** that allows or denies.

### Part C (3 points)
**Interpret the audit log** (Source 4). The `nsenter` commands (syscall 257 = openat) were executed by PID 9999. What **container escape technique** does this represent? What **MITRE ATT&CK technique** (Tactic + Technique ID)? The subsequent `cat` commands (PIDs 10000, 10001) accessed files with `key="sensitive_file"`. Which **host files** were likely targeted?

### Part D (3 points)
**Evaluate the RBAC configuration** (Source 5). The pod uses `serviceAccountName: cluster-admin-sa` which is bound to `cluster-admin` ClusterRole. A developer (`devuser`) has a RoleBinding to `pod-creator` Role in the `production` namespace. Explain **how the attacker** (who compromised `devuser` credentials) **escalated privileges** to create this privileged pod. What **principle of least privilege** was violated?

### Part E (2 points)
The **Pod Security Policy (PSP)** annotation shows `kubernetes.io/psp: privileged-psp`. PSPs are **deprecated in Kubernetes 1.25** and **removed in 1.28**. What **replacement mechanism** should be used in Kubernetes 1.28 to enforce equivalent restrictions? Name the **Kubernetes API resource** and the **enforcement mode** that would have prevented this pod from being admitted.

---

## Scoring Rubric (14 Points)

| Part | Points | Key Elements |
|------|--------|--------------|
| A | 3 | 1) `privileged: true` + hostPath `/` mount → full host access, container escape trivial. 2) `serviceAccountName: cluster-admin-sa` with cluster-admin → full cluster control. 3) `capabilities.add: [SYS_ADMIN, CAP_DAC_OVERRIDE, CAP_SYS_PTRACE]` → dangerous capabilities (mount, bypass DAC, ptrace). 4) PSP `privileged-psp` allows all of above. |
| B | 3 | 1) NO — Egress only allows DNS (53), HTTPS (443) to coredns/external-apis. SSH (22) not allowed. 2) YES — Egress allows TCP 443 to `namespaceSelector: external-apis` (if api.example.com in that namespace). 3) NO — API server (6443) not in any egress rule. |
| C | 3 | Technique: Container Escape via `nsenter` → entering host namespaces from privileged container. MITRE: T1611 (Escape to Host) — Privilege Escalation tactic. `cat` with `sensitive_file` key → likely `/etc/shadow`, `/etc/passwd`, `/root/.ssh/id_rsa`, `/var/lib/kubelet/pki/`. |
| D | 3 | devuser has `pod-creator` Role (create pods in production). Pod spec uses `cluster-admin-sa` ServiceAccount. Attacker creates pod spec referencing that SA → pod runs with cluster-admin privileges. Violation: SA with cluster-admin should NOT be in production namespace; devuser should not be able to specify arbitrary SAs (needs `impersonate` verb on SA). |
| E | 2 | Replacement: **Pod Security Admission (PSA)** — built-in admission controller. API resource: `PodSecurityPolicy` → replaced by `Namespace labels`: `pod-security.kubernetes.io/enforce: restricted` (or `baseline`). Enforcement mode: `enforce` (block), `audit` (log), `warn` (user-facing). `restricted` profile blocks privileged, hostPath, dangerous capabilities. |

---

*FRQ Practice Set 3 — Administered Apr 27, 2027 — Upload to qsec_ap_review/frq-practice/*