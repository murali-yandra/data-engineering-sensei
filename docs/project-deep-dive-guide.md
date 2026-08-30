# Project Deep Dive Guide

<!-- BEGIN LIBRARY ROLE -->
> **Library role: hub.** How project defense is evaluated, and what a survivable project story contains.
>
> Read this first for scope and orientation. It is short by design - open the deep references below only when you need the detail:
>
> - `modes/project-deep-dive-mode.md`
> - `templates/solutions/project-explanation-template.md`
<!-- END LIBRARY ROLE -->

Project deep dives are one of the highest-signal parts of a Data Engineering interview.

This guide trains the candidate to explain a real or portfolio project with ownership, architecture, trade-offs, failures, and measurable evidence.

Related files:

```text
modes/project-deep-dive-mode.md
templates/solutions/project-explanation-template.md
templates/reviews/project-review-template.md
templates/interviews/project-deep-dive-round-template.md
progress/CANDIDATE_PROFILE.md
progress/PROJECT_PROGRESS.md
```

## Purpose

A project explanation should prove that the candidate can:

1. Understand a business problem.
2. Explain data flow.
3. Define table or event grain.
4. Explain their personal contribution.
5. Defend technical decisions.
6. Discuss data quality and failure handling.
7. Explain trade-offs.
8. Show evidence through code, design, tests, metrics, or artifacts.

The mentor must challenge vague project claims.

Weak:

```text
We built ETL pipelines and loaded data into a warehouse.
```

Strong:

```text
I owned the ingestion and validation layer for a daily order analytics pipeline. The source was an OLTP orders database. I extracted incremental records using an updated_at watermark, landed raw data, validated schema and row counts, transformed it into order fact and customer dimension tables, and published curated marts for dashboard users. I added idempotent reruns by partition overwrite and tracked reconciliation between source and warehouse counts.
```

## Project Explanation Framework

Use this structure:

```text
1. Business problem
2. Users or consumers
3. Data sources
4. Data volume and frequency
5. High-level architecture
6. Data flow
7. Data model or output grain
8. Candidate contribution
9. Technical challenges
10. Data quality checks
11. Failure handling and retries
12. Backfill or reprocessing strategy
13. Performance or cost trade-offs
14. Security and privacy
15. Impact
16. What would be improved next
```

## Ownership Rule

If the candidate says "we did", ask:

```text
What exactly did you personally design, build, debug, optimize, test, document, or own?
```

The candidate can acknowledge teamwork, but interviewers need to see individual contribution.

## Evidence Requirements

A strong project should have evidence:

- repository or code sample
- README
- architecture diagram
- schema or data model
- example inputs and outputs
- tests
- quality checks
- logs or monitoring examples
- performance notes
- deployment or reproducibility notes
- resume bullets supported by facts

Do not invent evidence. If evidence is missing, mark it as missing and assign a next action.

## Common Follow-Up Questions

Ask these aggressively:

1. What was the exact source and sink?
2. What was the data volume?
3. What was the SLA?
4. What was the table grain?
5. How did you handle duplicates?
6. How did you handle late-arriving data?
7. How did you validate correctness?
8. What happened when the pipeline failed?
9. How did you rerun safely?
10. How did you handle schema changes?
11. What did you optimize?
12. What security risks existed?
13. What would you redesign now?

## Project Review Rubric

| Category | Score 1 | Score 3 | Score 5 |
|---|---|---|---|
| Business clarity | vague | understandable | crisp and role-relevant |
| Architecture | tool list only | basic flow | clear, justified design |
| Ownership | unclear | some ownership | specific personal contribution |
| Data modeling | missing | basic tables | grain, facts/dims, trade-offs |
| Quality | not mentioned | basic checks | validation, reconciliation, alerts |
| Failure handling | missing | retries mentioned | idempotency, reruns, backfills |
| Communication | rambling | structured | concise, defensible, evidence-backed |

## Minimum Passing Standard

The candidate is project-ready when they can explain one project in two minutes and survive follow-ups on:

- architecture
- data flow
- personal contribution
- data model
- quality
- failure handling
- trade-offs
- impact
- next improvements
