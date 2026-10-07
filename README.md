# AI-QE-Eval-500

**AI-QE-Eval-500** is a public evaluation dataset for measuring how well LLMs and AI agents perform software Quality Engineering tasks.

It contains **500 evaluation cases** spanning requirement analysis, test design, debugging, root-cause analysis, automation review, API testing, and release-risk assessment.

## Dataset composition

| Category | Cases |
|---|---:|
| Requirement analysis | 100 |
| Test generation | 100 |
| Debugging | 75 |
| Root-cause analysis | 75 |
| Automation review | 50 |
| API testing | 50 |
| Risk assessment | 50 |
| **Total** | **500** |

## Why this dataset exists

Most software-engineering benchmarks emphasize code generation. Quality Engineering requires a different set of capabilities:

- requirements reasoning
- testability analysis
- risk-based test design
- fault isolation
- root-cause reasoning
- automation architecture judgment
- API quality validation
- release-risk assessment

AI-QE-Eval-500 provides a structured benchmark for those capabilities.

## Record format

```json
{
  "id": "AIQE-0001",
  "category": "requirement_analysis",
  "task_type": "analysis",
  "difficulty": "easy",
  "input": "...",
  "expected_capability": "...",
  "reference": "...",
  "rubric": {
    "scoring_scale": "0-4",
    "criteria": [
      {
        "name": "gap_detection",
        "weight": 0.30,
        "description": "..."
      }
    ],
    "passing_score": 3.0
  },
  "risk": "LOW",
  "failure_category": "REQUIREMENT_AMBIGUITY",
  "tags": ["...", "..."],
  "metadata": {
    "source": "synthetic",
    "version": "1.0",
    "language": "en"
  },
  "fingerprint": "..."
}
```

## Suggested evaluation protocol

Evaluate model responses criterion-by-criterion on a **0-4 scale**.

- **0** — incorrect / missing
- **1** — weak, materially incomplete
- **2** — partially correct
- **3** — strong, minor omissions
- **4** — expert-level

Compute the weighted rubric score and treat **3.0/4.0** as the default passing threshold.

For more reliable benchmarking, use:
1. deterministic model settings where possible;
2. two independent evaluators or one evaluator + human adjudication;
3. per-category scores, not only one global score;
4. failure-category analysis;
5. repeated runs for variance-sensitive models.

## Splits

The repo includes deterministic category-preserving splits:

- `data/splits/train.jsonl`
- `data/splits/dev.jsonl`
- `data/splits/test.jsonl`

These are intended for evaluator development and benchmark iteration. If comparing models publicly, report the exact commit/version used.

## Validation

```bash
python scripts/validate_dataset.py
```

## Example benchmark dimensions

- Requirement understanding
- Completeness
- Edge-case awareness
- Correctness of test or RCA logic
- Evidence discipline
- Risk prioritization
- Test maintainability
- API semantic coverage
- Hallucination / unsupported assumptions

## Repository structure

```text
ai-qe-eval-500/
├── data/
│   ├── ai-qe-eval-500.json
│   ├── ai-qe-eval-500.jsonl
│   └── splits/
├── schemas/
│   └── record.schema.json
├── scripts/
│   ├── validate_dataset.py
│   └── score_example.py
├── docs/
│   ├── DATASET_CARD.md
│   └── EVALUATION_GUIDE.md
├── examples/
│   └── sample_records.json
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Intended use

Good uses:
- LLM evaluation for Quality Engineering
- model regression testing
- evaluator/judge experiments
- agent benchmarking
- prompt/model comparison
- QE-oriented research
- interview/demo portfolio work

Not intended for:
- certifying a model as production-safe by itself
- replacing security testing
- replacing domain-specific human review
- making employment decisions about individuals

## Limitations

Version 1.0 is predominantly **synthetic**. That makes the dataset reproducible and safe to publish, but it does not fully represent production incidents, proprietary systems, or all QE domains. Future releases should add expert-reviewed real-world cases, multilingual examples, mobile/device testing, performance engineering, security, and agentic multi-step tasks.

## License

MIT for repository code and dataset artifacts. See `LICENSE`.

## Citation

If you publish this dataset, add your name and repository URL here:

```bibtex
@dataset{ai_qe_eval_500_2026,
  title={AI-QE-Eval-500: A Quality Engineering Evaluation Dataset for LLMs and AI Agents},
  year={2026},
  publisher={GitHub},
  version={1.0}
}
```
