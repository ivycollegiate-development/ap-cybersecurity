# Lab 5.5 Capstone Extension — WAF, Secure Coding & Log Analysis Engine

**Base Lab**: `ap-cyber-u5-l5-waf-secure-coding`  
**Core Skills**: 5.5.A, 5.5.B, 5.5.C, 5.6.A, 5.6.B, 3.4.A, 3.4.B, 3.4.C

---

## Extension Requirements (TODO)

Implement **at least 3** of the following:

- [ ] **Custom WAF Rules Engine**: ModSecurity-compatible rule language with Lua/JS scripting
- [ ] **SAST Integration**: AST-based static analysis for common vulns (SQLi, XSS, path traversal)
- [ ] **Log Anomaly Detection**: ML/statistical detection of anomalous patterns in access/error logs
- [ ] **Attack Classification**: Auto-classify log entries by ATT&CK technique / OWASP category
- [ ] **Real-time Alerting**: Webhook/Slack/Email alerts with deduplication and escalation
- [ ] **Log Enrichment**: GeoIP, ASN, threat intel (AbuseIPDB, AlienVault OTX) enrichment
- [ ] **Compliance Reporting**: Generate PCI-DSS / SOC2 / HIPAA relevant log reports

**Minimum Viable Extension**: WAF rules engine + SAST scanner + log anomaly detection + alerting

---

## Suggested Architecture

```
capstone/
├── waf/
│   ├── __init__.py
│   ├── rule_engine.py      # Rule parsing, evaluation, actions
│   ├── rules/              # Built-in rule sets
│   │   ├── owasp_crs.yaml
│   │   ├── custom.yaml
│   │   └── lua_scripts/
│   └── middleware.py       # Framework integration (Flask/FastAPI/ASGI)
├── sast/
│   ├── __init__.py
│   ├── analyzer.py         # AST visitor for Python/JS
│   ├── rules/              # Vulnerability patterns
│   │   ├── python_rules.yaml
│   │   └── js_rules.yaml
│   └── reporter.py         # SARIF / HTML output
├── logs/
│   ├── __init__.py
│   ├── parser.py           # Multi-format log parser (nginx, apache, json, syslog)
│   ├── enricher.py         # GeoIP, ASN, threat intel
│   ├── anomaly.py          # Statistical/ML anomaly detection
│   ├── classifier.py       # ATT&CK / OWASP classification
│   └── alerting.py         # Alert manager with dedup/escalation
├── tests/
│   ├── test_waf.py
│   ├── test_sast.py
│   └── test_logs.py
├── .github/
│   └── workflows/
│       └── capstone-ci.yml
└── requirements.txt
```

---

## Starter Stubs (in `src/stubs/`)

```python
# waf/rule_engine.py
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any, Callable
import re

class Action(Enum):
    ALLOW = "allow"
    DENY = "deny"
    LOG = "log"
    REDIRECT = "redirect"
    CAPTCHA = "captcha"
    RATE_LIMIT = "rate_limit"

class Operator(Enum):
    EQ = "eq"
    NE = "ne"
    REGEX = "rx"
    CONTAINS = "contains"
    STARTS_WITH = "starts_with"
    ENDS_WITH = "ends_with"
    GT = "gt"
    LT = "lt"
    IN = "in"
    IP_MATCH = "ip_match"

@dataclass
class Condition:
    variable: str      # e.g., "REQUEST_HEADERS:User-Agent", "ARGS:id", "IP:SRC"
    operator: Operator
    value: Any
    negation: bool = False

@dataclass
class Rule:
    id: str
    phase: int         # 1=request headers, 2=request body, 3=response headers, 4=response body, 5=logging
    conditions: List[Condition]
    actions: List[Action]
    action_params: Dict[str, Any] = None  # e.g., {"redirect_url": "/blocked", "rate_limit": "10/min"}
    msg: str = ""
    severity: str = "Medium"  # Critical, High, Medium, Low, Info
    tags: List[str] = None
    enabled: bool = True

@dataclass
class Transaction:
    """Represents a single HTTP transaction for rule evaluation."""
    request_headers: Dict[str, str]
    request_body: str
    request_method: str
    request_uri: str
    request_args: Dict[str, List[str]]  # Query params
    source_ip: str
    response_headers: Dict[str, str] = None
    response_body: str = None
    response_status: int = None

class WAFRuleEngine:
    def __init__(self):
        self.rules: List[Rule] = []
        self.variable_extractors: Dict[str, Callable[[Transaction], Any]] = self._build_extractors()
    
    def _build_extractors(self) -> Dict[str, Callable]:
        """Map variable names to extraction functions."""
        return {
            "REQUEST_HEADERS": lambda tx, name: tx.request_headers.get(name, ""),
            "REQUEST_HEADERS:": lambda tx, name: tx.request_headers.get(name, ""),
            "ARGS": lambda tx, name: tx.request_args.get(name, [""])[0],
            "ARGS:": lambda tx, name: tx.request_args.get(name, [""])[0],
            "REQUEST_METHOD": lambda tx, _: tx.request_method,
            "REQUEST_URI": lambda tx, _: tx.request_uri,
            "REQUEST_BODY": lambda tx, _: tx.request_body,
            "IP:SRC": lambda tx, _: tx.source_ip,
            "RESPONSE_STATUS": lambda tx, _: str(tx.response_status) if tx.response_status else "",
            # Add more...
        }
    
    def load_rules(self, rules: List[Rule]):
        """Load rules, sort by phase then by id."""
        self.rules = sorted(rules, key=lambda r: (r.phase, r.id))
    
    def load_rules_from_yaml(self, yaml_path: str):
        """Parse YAML rule file (ModSecurity-compatible subset)."""
        # TODO: Parse YAML, create Rule objects
        raise NotImplementedError
    
    def evaluate(self, transaction: Transaction) -> List[Rule]:
        """Evaluate all rules against transaction. Return matched rules."""
        matched = []
        for rule in self.rules:
            if not rule.enabled:
                continue
            if self._match_rule(rule, transaction):
                matched.append(rule)
        return matched
    
    def _match_rule(self, rule: Rule, tx: Transaction) -> bool:
        """All conditions must match (AND logic)."""
        for cond in rule.conditions:
            if not self._match_condition(cond, tx):
                return False
        return True
    
    def _match_condition(self, cond: Condition, tx: Transaction) -> bool:
        # TODO: Extract variable value, apply operator, handle negation
        raise NotImplementedError
    
    def apply_actions(self, matched_rules: List[Rule], tx: Transaction) -> Dict[str, Any]:
        """Execute actions. Return decision: allow/deny/redirect/etc."""
        # Priority: DENY > REDIRECT > CAPTCHA > RATE_LIMIT > LOG > ALLOW
        for rule in matched_rules:
            for action in rule.actions:
                if action == Action.DENY:
                    return {"action": "deny", "rule": rule.id, "msg": rule.msg}
                # ... handle other actions
        return {"action": "allow"}

# waf/middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse, RedirectResponse

class WAFMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, engine: WAFRuleEngine):
        super().__init__(app)
        self.engine = engine
    
    async def dispatch(self, request: Request, call_next):
        # Build transaction
        tx = Transaction(
            request_headers=dict(request.headers),
            request_body=await request.body(),
            request_method=request.method,
            request_uri=str(request.url),
            request_args=dict(request.query_params),
            source_ip=request.client.host if request.client else "unknown",
        )
        
        # Evaluate
        matched = self.engine.evaluate(tx)
        decision = self.engine.apply_actions(matched, tx)
        
        if decision["action"] == "deny":
            return JSONResponse({"error": "Request blocked by WAF", "rule": decision["rule"]}, status_code=403)
        elif decision["action"] == "redirect":
            return RedirectResponse(url=decision.get("redirect_url", "/blocked"))
        
        # Continue
        response = await call_next(request)
        
        # Evaluate response phase rules
        tx.response_headers = dict(response.headers)
        tx.response_body = b""  # Would need body capture
        tx.response_status = response.status_code
        matched_resp = self.engine.evaluate(tx)
        # ... handle response actions
        
        return response
```

```python
# sast/analyzer.py
import ast
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Finding:
    file: str
    line: int
    column: int
    rule_id: str
    message: str
    severity: str  # Critical, High, Medium, Low, Info
    cwe: str
    owasp: str
    code_snippet: str

class PythonASTAnalyzer(ast.NodeVisitor):
    def __init__(self, rules: List[Dict]):
        self.rules = rules
        self.findings: List[Finding] = []
        self.current_file = ""
        self.source_lines = []
    
    def analyze_file(self, file_path: str) -> List[Finding]:
        with open(file_path, 'r') as f:
            source = f.read()
        self.current_file = file_path
        self.source_lines = source.splitlines()
        tree = ast.parse(source, filename=file_path)
        self.visit(tree)
        return self.findings
    
    def visit_Call(self, node: ast.Call):
        # Check for dangerous function calls
        # subprocess.call with shell=True
        # eval, exec
        # sqlite3 execute with string formatting
        # requests with verify=False
        # etc.
        for rule in self.rules:
            if self._matches_rule(node, rule):
                self._add_finding(node, rule)
        self.generic_visit(node)
    
    def _matches_rule(self, node: ast.Call, rule: Dict) -> bool:
        # TODO: Match function name, arguments, context
        raise NotImplementedError
    
    def _add_finding(self, node: ast.Call, rule: Dict):
        line = node.lineno
        snippet = self.source_lines[line-1] if line <= len(self.source_lines) else ""
        self.findings.append(Finding(
            file=self.current_file,
            line=line,
            column=node.col_offset,
            rule_id=rule["id"],
            message=rule["message"],
            severity=rule["severity"],
            cwe=rule.get("cwe", ""),
            owasp=rule.get("owasp", ""),
            code_snippet=snippet.strip()
        ))

class SASTScanner:
    def __init__(self, rules_dir: str):
        self.python_rules = self._load_rules(f"{rules_dir}/python_rules.yaml")
        self.js_rules = self._load_rules(f"{rules_dir}/js_rules.yaml")
    
    def _load_rules(self, path: str) -> List[Dict]:
        # TODO: Load YAML rules
        raise NotImplementedError
    
    def scan(self, path: str) -> List[Finding]:
        """Scan file or directory."""
        # TODO: Recurse directory, dispatch to appropriate analyzer
        raise NotImplementedError
    
    def generate_sarif(self, findings: List[Finding]) -> dict:
        """Generate SARIF 2.1.0 output for GitHub Code Scanning."""
        # TODO: Map findings to SARIF format
        raise NotImplementedError
```

```python
# logs/anomaly.py
import numpy as np
from collections import Counter
from datetime import datetime, timedelta
from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: datetime
    source_ip: str
    method: str
    uri: str
    status: int
    bytes_sent: int
    user_agent: str
    extra: dict

@dataclass
class Anomaly:
    timestamp: datetime
    type: str  # "volume", "rate", "geo", "status", "user_agent", "payload"
    severity: str
    description: str
    affected_ips: List[str]
    sample_entries: List[LogEntry]

class LogAnomalyDetector:
    def __init__(self, window_minutes: int = 10):
        self.window_minutes = window_minutes
        self.baseline = {}  # Learned normal behavior
    
    def train(self, entries: List[LogEntry]):
        """Learn baseline from historical data."""
        # TODO: Calculate baseline stats per IP, per URI, per hour, etc.
        # Request rate per IP/minute
        # Status code distribution
        # URI access patterns
        # User agent diversity
        # Geographic distribution
        raise NotImplementedError
    
    def detect(self, entries: List[LogEntry]) -> List[Anomaly]:
        """Detect anomalies in recent window."""
        anomalies = []
        
        # Volume spike per IP
        anomalies.extend(self._detect_volume_spike(entries))
        
        # Unusual status codes (5xx spike, 404 scan)
        anomalies.extend(self._detect_status_anomaly(entries))
        
        # Geographic impossibility (same IP, distant locations quickly)
        anomalies.extend(self._detect_geo_impossible(entries))
        
        # New user agents / automated tools
        anomalies.extend(self._detect_ua_anomaly(entries))
        
        # Payload anomalies (SQLi, XSS patterns in args)
        anomalies.extend(self._detect_payload_anomaly(entries))
        
        return anomalies
    
    def _detect_volume_spike(self, entries: List[LogEntry]) -> List[Anomaly]:
        # Count requests per IP in window
        ip_counts = Counter(e.source_ip for e in entries)
        threshold = self.baseline.get("max_req_per_ip_per_window", 100)
        for ip, count in ip_counts.items():
            if count > threshold * 3:  # 3x baseline
                yield Anomaly(...)
    
    def _detect_status_anomaly(self, entries: List[LogEntry]) -> List[Anomaly]:
        # 5xx rate > 5%, or 404 rate > 20%
        raise NotImplementedError
    
    def _detect_geo_impossible(self, entries: List[LogEntry]) -> List[Anomaly]:
        # Requires GeoIP enrichment first
        raise NotImplementedError
```

```python
# logs/alerting.py
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Callable
import time
import hashlib

class AlertSeverity(Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class Alert:
    id: str
    timestamp: float
    severity: AlertSeverity
    title: str
    description: str
    source: str  # "waf", "sast", "logs"
    tags: List[str]
    deduplication_key: str
    count: int = 1
    first_seen: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)

class AlertManager:
    def __init__(self, dedup_window_seconds: int = 300):
        self.dedup_window = dedup_window_seconds
        self.alerts: Dict[str, Alert] = {}  # dedup_key -> Alert
        self.handlers: List[Callable[[Alert], None]] = []
    
    def add_handler(self, handler: Callable[[Alert], None]):
        self.handlers.append(handler)
    
    def fire(self, severity: AlertSeverity, title: str, description: str, 
             source: str, tags: List[str], dedup_key: str = None):
        if dedup_key is None:
            dedup_key = hashlib.md5(f"{source}:{title}".encode()).hexdigest()[:16]
        
        now = time.time()
        if dedup_key in self.alerts:
            alert = self.alerts[dedup_key]
            if now - alert.last_seen < self.dedup_window:
                alert.count += 1
                alert.last_seen = now
                return  # Suppressed
            # Window expired, fire new alert
        
        alert = Alert(
            id=hashlib.md5(f"{now}:{title}".encode()).hexdigest()[:12],
            timestamp=now,
            severity=severity,
            title=title,
            description=description,
            source=source,
            tags=tags,
            deduplication_key=dedup_key,
        )
        self.alerts[dedup_key] = alert
        
        for handler in self.handlers:
            try:
                handler(alert)
            except Exception:
                pass  # Log but don't crash
    
    # Built-in handlers
    @staticmethod
    def webhook_handler(url: str, secret: str = None):
        def handler(alert: Alert):
            import requests, hmac, hashlib
            payload = {"alert": alert.__dict__}
            headers = {"Content-Type": "application/json"}
            if secret:
                sig = hmac.new(secret.encode(), str(payload).encode(), hashlib.sha256).hexdigest()
                headers["X-Signature"] = sig
            requests.post(url, json=payload, headers=headers, timeout=5)
        return handler
    
    @staticmethod
    def slack_handler(webhook_url: str):
        def handler(alert: Alert):
            color = {"critical": "danger", "high": "warning", "medium": "#ffcc00", "low": "good", "info": "#439FE0"}
            payload = {
                "attachaches": [{
                    "color": color.get(alert.severity.value, "#439FE0"),
                    "title": f"[{alert.severity.value.upper()}] {alert.title}",
                    "text": alert.description,
                    "fields": [
                        {"title": "Source", "value": alert.source, "short": True},
                        {"title": "Count", "value": str(alert.count), "short": True},
                    ],
                    "footer": f"Tags: {', '.join(alert.tags)}"
                }]
            }
            requests.post(webhook_url, json=payload, timeout=5)
        return handler
```

---

## Test Scaffolding

```python
# test_waf.py
import pytest
from capstone.waf.rule_engine import WAFRuleEngine, Rule, Condition, Action, Operator, Transaction

class TestWAFRuleEngine:
    @pytest.fixture
    def engine(self):
        e = WAFRuleEngine()
        e.load_rules([
            Rule(id="sql-1", phase=2, conditions=[
                Condition(variable="ARGS:id", operator=Operator.REGEX, value=r"(?i)(union|select|insert|delete)")
            ], actions=[Action.DENY], msg="SQL Injection attempt"),
            Rule(id="rate-1", phase=1, conditions=[
                Condition(variable="IP:SRC", operator=Operator.IN, value=["192.168.1.100"])
            ], actions=[Action.RATE_LIMIT], action_params={"rate_limit": "10/min"}),
        ])
        return e
    
    def test_sql_injection_blocked(self, engine):
        tx = Transaction(
            request_headers={}, request_body="", request_method="GET",
            request_uri="/api/user", request_args={"id": ["1 UNION SELECT * FROM users"]},
            source_ip="10.0.0.1"
        )
        matched = engine.evaluate(tx)
        decision = engine.apply_actions(matched, tx)
        assert decision["action"] == "deny"
        assert "sql-1" in decision["rule"]
    
    def test_rate_limit_tagged(self, engine):
        tx = Transaction(
            request_headers={}, request_body="", request_method="GET",
            request_uri="/api/user", request_args={"id": ["1"]},
            source_ip="192.168.1.100"
        )
        matched = engine.evaluate(tx)
        # Check rate limit action would apply
        assert any(r.id == "rate-1" for r in matched)

# test_sast.py
import pytest
import tempfile
from capstone.sast.analyzer import SASTScanner, PythonASTAnalyzer

class TestSASTScanner:
    @pytest.fixture
    def scanner(self):
        return SASTScanner("capstone/sast/rules")
    
    def test_detects_sql_injection(self, scanner):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write('''
import sqlite3
conn = sqlite3.connect("test.db")
user_id = input("Enter ID: ")
cursor = conn.execute(f"SELECT * FROM users WHERE id = {user_id}")
''')
            f.flush()
            findings = scanner.scan(f.name)
            assert any("SQL" in f.message or "CWE-89" in f.cwe for f in findings)
    
    def test_detects_command_injection(self, scanner):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write('''
import subprocess
user_input = input("File: ")
subprocess.call(f"cat {user_input}", shell=True)
''')
            f.flush()
            findings = scanner.scan(f.name)
            assert any("command injection" in f.message.lower() or "CWE-78" in f.cwe for f in findings)

# test_logs.py
import pytest
from datetime import datetime, timedelta
from capstone.logs.anomaly import LogAnomalyDetector, LogEntry

class TestLogAnomalyDetector:
    @pytest.fixture
    def detector(self):
        d = LogAnomalyDetector(window_minutes=10)
        # Train with normal traffic
        normal = [
            LogEntry(datetime.now() - timedelta(minutes=i), "10.0.0.1", "GET", "/api/health", 200, 100, "Mozilla/5.0", {})
            for i in range(100)
        ]
        d.train(normal)
        return d
    
    def test_volume_spike(self, detector):
        now = datetime.now()
        spike = [
            LogEntry(now, "192.168.1.50", "GET", "/admin", 200, 100, "curl/7.68", {})
            for _ in range(500)  # Way above baseline
        ]
        anomalies = detector.detect(spike)
        assert any(a.type == "volume" for a in anomalies)
```

---

## CI Workflow

```yaml
name: Capstone CI

on:
  push:
    branches: [capstone]
  pull_request:
    branches: [main, capstone]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8 bandit pyyaml requests geoip2
      - name: Lint
        run: flake8 capstone/
      - name: Security scan
        run: bandit -r capstone/ || true
      - name: Tests
        run: pytest tests/ -v --cov=capstone --cov-report=term-missing
      - name: SAST self-scan
        run: python -m capstone.sast.analyzer capstone/ --format sarif --output sast-results.sarif || true
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: sast-results.sarif
```

---

## Requirements

```
pyyaml>=6.0
requests>=2.31.0
geoip2>=4.7.0
numpy>=1.24.0
scikit-learn>=1.3.0  # Optional for ML anomaly detection
starlette>=0.27.0
uvicorn>=0.23.0
pytest>=7.4.0
pytest-cov>=4.1.0
flake8>=6.0.0
bandit>=1.7.0
```

---

## Grading Notes

| Feature | Points (of 40) |
|---------|----------------|
| WAF rule engine (ModSecurity subset) | 12 |
| SAST analyzer (Python + JS) | 10 |
| Log anomaly detection + enrichment | 8 |
| Alerting with dedup/escalation | 5 |
| Code quality, tests, CI, SARIF | 5 |

**Bonus**: Real-time streaming (Kafka/Redis), ML-based anomaly, ATT&CK mapping, compliance reports