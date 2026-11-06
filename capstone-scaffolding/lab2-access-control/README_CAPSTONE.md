# Lab 5.2 Capstone Extension — Access Control Policy Engine

**Base Lab**: `ap-cyber-u5-l2-access-control`  
**Core Skills**: 2.3.A, 2.3.B, 5.2.A, 5.2.B, 5.2.C, 5.2.D

---

## Extension Requirements (TODO)

Implement **at least 3** of the following:

- [ ] **RuBAC Engine**: Rule-based access control with time, location, device, risk-score conditions
- [ ] **ABAC Policy Evaluator**: Attribute-based access control with XACML-like policy language
- [ ] **Audit Logger**: Tamper-evident audit trail for all access decisions (append-only, signed)
- [ ] **Policy Simulator**: "What-if" analysis — test policy changes against historical requests
- [ ] **Anomaly Detection**: ML/statistical detection of unusual access patterns (impossible travel, off-hours)
- [ ] **Break-Glass Procedure**: Emergency access with approval workflow, time-boxed, fully audited
- [ ] **Policy-as-Code CI**: Validate policies on PR; deploy to OPA/Gatekeeper on merge

**Minimum Viable Extension**: RuBAC engine + audit logger + policy simulator + CI validation

---

## Suggested Architecture

```
capstone/
├── access_control/
│   ├── __init__.py
│   ├── models.py           # Policy, Rule, Subject, Resource, Action, Context
│   ├── rubac_engine.py     # Rule evaluation engine
│   ├── abac_evaluator.py   # ABAC policy evaluation (subset of XACML)
│   ├── audit_logger.py     # Signed, append-only audit log
│   ├── simulator.py        # Policy simulation against request history
│   └── anomaly_detector.py # Statistical anomaly detection
├── tests/
│   ├── test_rubac.py
│   ├── test_abac.py
│   └── test_audit.py
├── policies/
│   ├── example_rubac.yaml
│   └── example_abac.yaml
├── .github/
│   └── workflows/
│       └── capstone-ci.yml
└── requirements.txt
```

---

## Starter Stubs (in `src/stubs/`)

```python
# models.py
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any, List, Optional
from datetime import datetime

class Effect(Enum):
    PERMIT = "Permit"
    DENY = "Deny"
    NOT_APPLICABLE = "NotApplicable"

@dataclass
class Subject:
    id: str
    attributes: Dict[str, Any]  # role, department, clearance, device_id, etc.

@dataclass
class Resource:
    id: str
    type: str
    attributes: Dict[str, Any]  # classification, owner, sensitivity, etc.

@dataclass
class Action:
    id: str
    name: str  # read, write, delete, admin

@dataclass
class Context:
    timestamp: datetime
    ip_address: str
    location: Optional[str] = None
    device_fingerprint: Optional[str] = None
    risk_score: float = 0.0
    custom: Dict[str, Any] = None

@dataclass
class Request:
    subject: Subject
    resource: Resource
    action: Action
    context: Context

@dataclass
class Decision:
    effect: Effect
    policy_id: str
    rule_id: Optional[str]
    obligations: List[str]  # e.g., ["log", "notify", "require_mfa"]
    explanation: str

@dataclass
class AuditEntry:
    request: Request
    decision: Decision
    signature: str  # HMAC of entry for tamper evidence
    timestamp: datetime
```

```python
# rubac_engine.py
class RuBACEngine:
    def __init__(self, policies: List[Policy]):
        self.policies = policies
    
    def evaluate(self, request: Request) -> Decision:
        """Evaluate request against all policies. First matching rule wins."""
        # TODO: Implement rule evaluation with condition matching
        # Conditions: time windows, IP ranges, geo, risk score thresholds, etc.
        raise NotImplementedError
    
    def add_policy(self, policy: Policy):
        self.policies.append(policy)
    
    def explain(self, request: Request) -> List[str]:
        """Return human-readable explanation of why decision was made."""
        raise NotImplementedError

# abac_evaluator.py
class ABACEvaluator:
    def __init__(self, policy_store: PolicyStore):
        self.policy_store = policy_store
    
    def evaluate(self, request: Request) -> Decision:
        """Evaluate XACML-like policy: Target + Rule + Condition."""
        # TODO: Implement attribute matching, function evaluation (string-equal, regex, etc.)
        raise NotImplementedError

# audit_logger.py
import hmac
import hashlib
import json

class AuditLogger:
    def __init__(self, secret_key: bytes, log_path: str):
        self.secret_key = secret_key
        self.log_path = log_path
        self._verify_chain()
    
    def log(self, entry: AuditEntry) -> str:
        """Append entry with HMAC signature. Return entry ID."""
        # TODO: Serialize, sign, append. Verify chain integrity on read.
        raise NotImplementedError
    
    def verify_chain(self) -> bool:
        """Verify entire log chain integrity."""
        raise NotImplementedError
    
    def query(self, filters: Dict) -> List[AuditEntry]:
        """Query audit log with filters (subject, resource, time range, effect)."""
        raise NotImplementedError

# simulator.py
class PolicySimulator:
    def __init__(self, engine: RuBACEngine, request_history: List[Request]):
        self.engine = engine
        self.history = request_history
    
    def simulate(self, new_policies: List[Policy]) -> SimulationReport:
        """Re-evaluate historical requests against proposed policies."""
        # TODO: Compare old vs new decisions. Identify breaking changes.
        raise NotImplementedError
    
    def find_conflicts(self, policies: List[Policy]) -> List[Conflict]:
        """Detect contradictory rules within policy set."""
        raise NotImplementedError
```

---

## Test Scaffolding (in `tests/`)

```python
# test_rubac.py
import pytest
from datetime import datetime, time
from capstone.access_control.rubac_engine import RuBACEngine
from capstone.access_control.models import *

class TestRuBACEngine:
    @pytest.fixture
    def engine(self):
        return RuBACEngine([])
    
    def test_time_based_rule(self, engine):
        # Rule: allow 9-17 on weekdays
        policy = Policy(rules=[
            Rule(condition="context.timestamp.time() >= 9:00 and <= 17:00 and context.timestamp.weekday() < 5",
                 effect=Effect.PERMIT)
        ])
        engine.add_policy(policy)
        
        req = Request(
            subject=Subject(id="user1", attributes={"role": "employee"}),
            resource=Resource(id="doc1", type="document", attributes={}),
            action=Action(id="read", name="read"),
            context=Context(timestamp=datetime(2024, 1, 15, 10, 0))  # Monday 10am
        )
        decision = engine.evaluate(req)
        assert decision.effect == Effect.PERMIT
    
    def test_deny_outside_hours(self, engine):
        # Same policy, but 8pm
        req = Request(
            subject=Subject(id="user1", attributes={"role": "employee"}),
            resource=Resource(id="doc1", type="document", attributes={}),
            action=Action(id="read", name="read"),
            context=Context(timestamp=datetime(2024, 1, 15, 20, 0))
        )
        decision = engine.evaluate(req)
        assert decision.effect == Effect.DENY

# test_audit.py
import pytest
from capstone.access_control.audit_logger import AuditLogger
from capstone.access_control.models import *

class TestAuditLogger:
    @pytest.fixture
    def logger(self, tmp_path):
        return AuditLogger(b"test-secret", str(tmp_path / "audit.log"))
    
    def test_log_and_verify(self, logger):
        entry = AuditEntry(
            request=Request(...),  # minimal valid request
            decision=Decision(effect=Effect.PERMIT, policy_id="p1", rule_id="r1", obligations=[], explanation="test"),
            signature="",  # will be set by logger
            timestamp=datetime.now()
        )
        entry_id = logger.log(entry)
        assert entry_id
        assert logger.verify_chain()
    
    def test_tamper_detection(self, logger):
        logger.log(valid_entry)
        # Corrupt log file
        with open(logger.log_path, 'a') as f:
            f.write("corrupted")
        assert not logger.verify_chain()
```

---

## Example Policy Files (`policies/`)

```yaml
# example_rubac.yaml
policies:
  - id: "corporate-data-access"
    description: "Access to corporate documents during business hours from managed devices"
    rules:
      - id: "business-hours-managed-device"
        condition: |
          context.timestamp.time() >= "09:00" and 
          context.timestamp.time() <= "17:00" and
          context.timestamp.weekday() < 5 and
          subject.attributes.device_managed == true
        effect: "Permit"
        obligations: ["log", "watermark"]
      - id: "deny-all-other"
        condition: "true"
        effect: "Deny"
        obligations: ["log", "alert"]
```

```yaml
# example_abac.yaml
policy:
  target:
    subject:
      attribute: "role"
      match: "employee"
    resource:
      attribute: "classification"
      match: "internal"
  rules:
    - effect: "Permit"
      condition:
        function: "and"
        args:
          - function: "time-in-range"
            args: ["09:00", "17:00"]
          - function: "string-equals"
            args: ["subject.attributes.department", "resource.attributes.owner_dept"]
      obligations: ["log"]
    - effect: "Deny"
```

---

## CI Workflow (`.github/workflows/capstone-ci.yml`)

```yaml
name: Capstone CI

on:
  push:
    branches: [capstone]
  pull_request:
    branches: [main, capstone]

jobs:
  lint-test-policy-validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8 bandit pyyaml
      - name: Lint
        run: flake8 capstone/ --max-line-length=100
      - name: Security scan
        run: bandit -r capstone/ || true
      - name: Validate policy syntax
        run: python -c "import yaml; [yaml.safe_load(open(f)) for f in ['policies/example_rubac.yaml', 'policies/example_abac.yaml']]"
      - name: Run tests
        run: pytest tests/ -v --cov=capstone --cov-report=term-missing
      - name: Policy conflict check
        run: python -m capstone.access_control.simulator --check-conflicts policies/
```

---

## Requirements

```
pyyaml>=6.0
cryptography>=41.0.0
pytest>=7.4.0
pytest-cov>=4.1.0
flake8>=6.0.0
bandit>=1.7.0
```

---

## Grading Notes

| Feature | Points (of 40) |
|---------|----------------|
| RuBAC engine with time/geo/device conditions | 12 |
| ABAC evaluator (subset XACML) | 10 |
| Tamper-evident audit logger | 8 |
| Policy simulator / conflict detection | 5 |
| Code quality, tests, CI | 5 |

**Bonus**: Anomaly detection, break-glass workflow, OPA integration