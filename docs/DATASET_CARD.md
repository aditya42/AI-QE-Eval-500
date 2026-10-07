# Dataset Card — AI-QE-Eval-500

## Summary
AI-QE-Eval-500 is a 500-case benchmark for evaluating LLM and AI-agent performance on software Quality Engineering tasks.

## Motivation
The dataset targets a gap between generic coding benchmarks and the reasoning work performed by senior QA/QE/SDET engineers.

## Data sources
Version 1.0 is synthetic and authored from common QE task patterns. It contains no production credentials, customer records, proprietary tickets, or personal data.

## Categories
- Requirement analysis
- Test generation
- Debugging
- Root-cause analysis
- Automation review
- API testing
- Risk assessment

## Annotation model
Each record contains:
- prompt/input
- expected capability
- reference answer guidance
- weighted rubric
- risk level
- failure category
- tags and metadata

## Risks and limitations
- Synthetic cases may be cleaner than real production incidents.
- References are guidance, not the only valid answer.
- LLM-as-judge scoring can be biased.
- Domain coverage is broad rather than exhaustive.
- English-only in v1.0.
- No private chain-of-thought should be requested or required for scoring.

## Recommended reporting
Report:
- overall weighted score
- category-level score
- pass rate
- failure-category distribution
- model/version
- evaluator/version
- temperature / decoding parameters
- number of repeated runs

## Versioning
Semantic dataset versions are recommended:
- 1.0.x: typo/metadata fixes
- 1.x: new compatible cases or annotations
- 2.0: schema-breaking changes
