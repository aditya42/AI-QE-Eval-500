# Evaluation Guide

## 1. Generate the model response
Run the candidate model on the `input` field only.

## 2. Score each rubric criterion
Score every criterion from 0 to 4.

### 0
Incorrect, unsafe, irrelevant, or absent.

### 1
Touches the topic but misses major requirements.

### 2
Partially correct with meaningful omissions.

### 3
Strong answer with only minor gaps.

### 4
Expert-level answer: correct, complete, risk-aware, and well-scoped.

## 3. Compute weighted score
For criterion score `s` and weight `w`:

`weighted contribution = (s / 4) * w * 4`

The record score is the sum of all weighted contributions.

## 4. Passing threshold
Default: `>= 3.0 / 4.0`

## 5. Aggregate reporting
Recommended:
- Macro average across all records
- Average per category
- Pass rate per category
- Average by difficulty
- Average by risk
- Error counts by `failure_category`

## 6. Human adjudication
Use a human reviewer when:
- evaluator scores differ by >1 point on any criterion;
- the reference is underspecified;
- the candidate gives a valid alternative solution;
- safety or production-risk claims are disputed.

## 7. Avoid invalid evaluation practices
Do not reward verbosity by itself.
Do not require hidden chain-of-thought.
Do not treat the reference as a string-matching gold answer.
Do not collapse all QE capabilities into one pass/fail metric.
