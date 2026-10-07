#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "ai-qe-eval-500.jsonl"

EXPECTED = {
    "requirement_analysis": 100,
    "test_generation": 100,
    "debugging": 75,
    "root_cause_analysis": 75,
    "automation_review": 50,
    "api_testing": 50,
    "risk_assessment": 50,
}

def validate():
    rows = [json.loads(line) for line in DATA.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == 500, f"Expected 500 rows, got {len(rows)}"
    assert len({r["id"] for r in rows}) == 500, "Duplicate IDs detected"
    assert len({r["fingerprint"] for r in rows}) == 500, "Duplicate fingerprints detected"

    counts = Counter(r["category"] for r in rows)
    assert counts == Counter(EXPECTED), f"Category mismatch: {counts}"

    for r in rows:
        for key in ["input", "expected_capability", "reference", "rubric", "risk", "failure_category"]:
            assert r.get(key), f"{r['id']} missing {key}"
        weight_sum = sum(c["weight"] for c in r["rubric"]["criteria"])
        assert abs(weight_sum - 1.0) < 1e-9, f"{r['id']} rubric weights sum to {weight_sum}"

    print("Validation passed.")
    print(f"Records: {len(rows)}")
    for category in EXPECTED:
        print(f"{category}: {counts[category]}")

if __name__ == "__main__":
    validate()
