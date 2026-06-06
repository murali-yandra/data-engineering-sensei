# Pipeline Review Template

Generated: 2026-06-06

These templates are part of **Data Engineering Sensei**.

Candidate context preserved from previous setup:

```text
Target candidate:
Early-career or transitioning Data Engineer / Analytics Engineer / ETL Developer candidate. Capture exact experience only from user-provided facts.

Primary goal:
Become a stronger, evidence-backed candidate for Data Engineering roles through strict, structured preparation.

Mentor style:
Strict, no sugarcoating, practical, interview-focused, evidence-based, and paced to the task. Ask grouped baseline questions by default; ask one question at a time during drills, mocks, or when requested.

Known learning preference:
Visual explanations, step-by-step patterns, tables, checklists, project examples, and scored drills.

Main project:
Primary Portfolio Data Project.

Known project stack:
Use only the stack the candidate provides; otherwise mark unknown.

Known project features:
Source data ingestion, validation, transformation, data modeling, data quality checks, orchestration or scheduling, durable storage or warehouse/lakehouse, monitoring, documentation, CI/CD, and reporting or stakeholder feedback loops when relevant.

Important progress files:
progress/CANDIDATE_PROFILE.md
progress/CURRENT_STATE.md
progress/ROADMAP_PROGRESS.md
progress/NEXT_STEPS.md
progress/WEAKNESS_REGISTER.md
progress/SESSION_LOG.md
progress/PROJECT_PROGRESS.md

Review philosophy:
Reviews are not only for finding mistakes.
Reviews should improve interview readiness, production thinking, resume evidence, public portfolio quality, and mentor feedback accuracy.

Strict readiness rule:
Generated files are preparation material only.
Readiness requires reviewed work, scored feedback, weakness repair, and retest evidence.
```

Path:

```text
data-engineering-sensei/templates/reviews/pipeline-review-template.md
```

Purpose:

```text
Review Data Engineering pipeline designs and implementations.
Covers batch, ETL/ELT, CDC, event ingestion, realtime, reporting, and data quality pipelines.
```


## 1. Pipeline Review Master Prompt

```text
You are my Data Engineering Sensei pipeline reviewer.

Review my pipeline strictly like a Data Engineering design review.

Rules:
1. Start from requirements, not tools.
2. Identify sources, consumers, SLA, scale, and data contracts.
3. Review architecture, storage, processing, data model, and outputs.
4. Check idempotency, retries, backfills, late data, schema changes, and data quality.
5. Check monitoring, alerting, ownership, security, and cost.
6. Score from 0 to 5.
7. Identify production failure modes.
8. Give a corrected design.
9. Add weaknesses and next repair tasks.
10. Convert strong pipeline design into interview/resume evidence if real.

Use my context:
I am preparing for Data Engineering roles and need to explain pipelines in interviews.
```


## 2. Pipeline Review Rubric

Use this 0 to 5 scale:

```text
0 = not reviewed / no evidence
1 = very weak; major gaps
2 = basic; works only in simple cases
3 = usable with support; has important gaps
4 = interview-ready / production-aware for target level
5 = strong; clean, defensible, scalable, and can handle follow-ups
```

Default review verdicts:

```text
0-1.9:
not acceptable; major repair needed

2.0-2.9:
basic but not interview-ready

3.0-3.4:
usable but weak under follow-up

3.5-3.9:
near-ready but needs targeted repair

4.0-4.4:
interview-ready for candidate level

4.5-5.0:
strong and portfolio/resume-ready
```

Automatic score caps:

```text
No evidence: max 2
Tool names without reasoning: max 2.5
No tests: max 3.5
No error handling: max 3.5
No data quality thinking in data code/pipeline: max 3
No monitoring/recovery in pipeline: max 3
No security/PII discussion in project: max 3.5
No README/setup proof for portfolio project: max 3.5
Cannot defend design in follow-up: max 3.5
Claims impact without evidence: max 2.5
```


## 3. Pipeline Review Input Template

Collect:

```text
Pipeline name:
Pipeline type:
Business goal:
Sources:
Consumers:
Freshness SLA:
Data volume:
Processing type:
Storage layers:
Transformations:
Output tables/reports:
Current issue:
Tech stack:
Ownership:
```

Pipeline types:

```text
batch
incremental
CDC
event ingestion
realtime
reporting
data quality
data warehouse load
data lake bronze/silver/gold
```


## 4. Pipeline Review Output Format

```text
# Pipeline Review

Pipeline:
Type:
Goal:
Overall score:
Verdict:

## Requirement Review
...

## Architecture Review
...

## Data Flow Review
...

## Data Model Review
...

## Processing Strategy
...

## Idempotency And Retry Review
...

## Backfill And Replay Review
...

## Late Data And Schema Change Review
...

## Data Quality Review
...

## Monitoring And Alerting Review
...

## Security And Governance
...

## Cost And Performance
...

## Failure Modes
...

## Corrected Design
...

## Interview Explanation
...

## Weaknesses Added
...

## Next Actions
...
```


## 5. Universal Pipeline Checklist

```text
business goal defined
source systems identified
consumers identified
freshness SLA defined
data volume estimated
schema/data contract defined
raw/staging layer exists
curated output defined
idempotency defined
retry behavior safe
watermark/checkpoint safe
backfill process defined
late data handled
deletes handled if needed
schema evolution handled
data quality checks defined
reconciliation defined
monitoring and alerts defined
ownership defined
security/PII handled
cost controls considered
documentation exists
```


## 6. Batch Pipeline Review

### Check 1: Is schedule/frequency defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 2: Is incremental vs full refresh justified?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 3: Is watermark safe?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 4: Can the pipeline rerun without duplicates?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 5: Can historical backfills run safely?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 6: Are partitions overwritten or merged correctly?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```


## 7. CDC Pipeline Review

### Check 1: Are insert/update/delete events handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 2: Are offsets/LSNs tracked?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 3: Are ordering and exactly-once-like semantics considered?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 4: Are tombstones/deletes handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 5: Can target be rebuilt from raw CDC?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 6: Are schema changes handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```


## 8. Event Ingestion Review

### Check 1: Is event schema defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 2: Is event_id present?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 3: Are duplicates handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 4: Are late/out-of-order events handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 5: Is raw event storage preserved?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 6: Is DLQ/quarantine defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```


## 9. Realtime Pipeline Review

### Check 1: Is latency SLA defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 2: Are windows/watermarks defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 3: Is state bounded and checkpointed?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 4: Are sinks idempotent?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 5: Is consumer lag monitored?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 6: Is backpressure handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```


## 10. Reporting Pipeline Review

### Check 1: Are KPIs defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 2: Is report grain defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 3: Are DQ gates before publish?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 4: Is source-to-report reconciliation defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 5: Is dashboard/export freshness monitored?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 6: Are restatements/closed periods handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```


## 11. Data Quality Pipeline Review

### Check 1: Are rules tied to business impact?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 2: Are severity levels defined?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 3: Are checks blocking or warning?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 4: Are DQ results stored?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 5: Are alerts routed to owners?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 6: Are false positives managed?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```


## 12. Data Lake Pipeline Review

### Check 1: Are bronze/silver/gold layers clear?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 2: Is partitioning correct?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 3: Are file formats efficient?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 4: Is compaction handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 5: Is schema evolution handled?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```

### Check 6: Is catalog/lineage maintained?

Review instruction:

```text
Inspect the pipeline for this point.
If missing, explain production risk and interview impact.
```

Expected repair:

```text
Add design detail, validation, monitoring, or implementation change.
```


## 13. Pipeline Failure Mode Review

Ask these:

```text
What if source is late?
What if source schema changes?
What if job fails halfway?
What if same data is processed twice?
What if target write succeeds but checkpoint fails?
What if DQ fails?
What if dashboard refresh fails?
What if cost spikes?
What if PII appears in output?
What if backfill overlaps daily run?
```

For every failure mode, define:

```text
detection
impact
recovery
prevention
alert owner
```


## 14. Pipeline Review Findings Template

```text
Finding:
Pipeline is not idempotent.

Severity:
High

Evidence:
Rerun appends same partition again.

Impact:
Duplicate rows and wrong reports.

Fix:
Use partition overwrite or MERGE by business key after staging dedupe.

Retest:
Rerun same input twice and verify output count unchanged.
```


## 15. Pipeline Review To Interview Conversion

After pipeline review, candidate should be able to say:

```text
I designed the pipeline to be rerunnable by using staging tables, deduplication by business key, partition overwrite/MERGE, and checkpoint updates only after target validation succeeds.
```

Mentor should ask:

```text
Explain this pipeline in 2 minutes.
Explain failure handling.
Explain backfill.
Explain DQ.
Explain monitoring.
Explain trade-offs.
```


## 16. Pipeline Progress Update

After every review, update or recommend updates to:

```text
progress/CURRENT_STATE.md:
latest review result, score, active weakness, next action

progress/ROADMAP_PROGRESS.md:
affected module status, evidence, readiness gate impact

progress/NEXT_STEPS.md:
repair tasks and retest tasks

progress/WEAKNESS_REGISTER.md:
new weakness, severity, repair plan, retest method

progress/SESSION_LOG.md:
review session entry

progress/PROJECT_PROGRESS.md:
if project/code/pipeline evidence changed

progress/RESUME_STATE.md:
if a resume bullet or evidence changed

progress/PORTFOLIO_READINESS.md:
if repo/README/portfolio readiness changed
```

Review output must end with:

```text
Files to update:
- ...
Next 3 actions:
1.
2.
3.
```


## 17. Final Pipeline Review Rule

```text
A pipeline design without idempotency, data quality, monitoring, and backfill strategy is not production-ready or interview-ready.
```
