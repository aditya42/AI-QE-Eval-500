#!/usr/bin/env python3
"""
Minimal rubric scorer skeleton.
Plug your model/evaluator outputs into `scores` as criterion->0..4.
"""
def weighted_score(record, scores):
    total = 0.0
    for criterion in record["rubric"]["criteria"]:
        name = criterion["name"]
        weight = criterion["weight"]
        total += (scores[name] / 4.0) * weight * 4.0
    return round(total, 3)

def passes(record, scores):
    return weighted_score(record, scores) >= record["rubric"]["passing_score"]
