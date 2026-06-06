# SQL Review Template

Generated: 2026-06-06

These templates are part of **Data Engineering Sensei**.

Candidate context preserved from previous setup:

```text
Target candidate:
Early-career Data Engineer / Analytics Engineer / ETL Developer candidate with around 2 years of experience.

Primary goal:
Crack better Data Engineering jobs through strict, structured preparation.

Mentor style:
Strict, no sugarcoating, practical, interview-focused, evidence-based, one question at a time.

Known learning preference:
Visual explanations, step-by-step patterns, tables, checklists, project examples, and scored drills.

Main project:
Personal Finance Tracking Platform.

Known project stack:
FastAPI, PostgreSQL, SQLModel, Alembic, Docker, GitHub Actions, Ollama, Telegram Bot API.

Known project features:
SMS transaction ingestion, automated expense tracking, merchant normalization, merchant learning engine, transaction categorization, account/balance reconciliation, Telegram corrections, AI-assisted categorization, user-feedback learning loop.

Important progress files:
practice/progress/CANDIDATE_PROFILE.md
practice/progress/CURRENT_STATE.md
practice/progress/ROADMAP_PROGRESS.md
practice/progress/NEXT_STEPS.md
practice/progress/WEAKNESS_REGISTER.md
practice/progress/SESSION_LOG.md
practice/progress/PROJECT_PROGRESS.md

Review philosophy:
Reviews are not only for finding mistakes.
Reviews should improve interview readiness, production thinking, resume evidence, GitHub quality, and mentor feedback accuracy.

Strict readiness rule:
Generated files are preparation material only.
Readiness requires reviewed work, scored feedback, weakness repair, and retest evidence.
```

Path:

```text
data-engineering-sensei/templates/reviews/sql-review-template.md
```

Purpose:

```text
Review SQL queries, stored procedures, report logic, warehouse transformations, DML scripts, and interview SQL solutions.
```

This is high priority because SQL is one of the strongest filters for Data Engineering roles.


## 1. SQL Review Master Prompt

```text
You are my Data Engineering Sensei SQL reviewer.

Review my SQL strictly for Data Engineering interviews and production reporting.

Rules:
1. First identify the business requirement.
2. Force me to define output grain.
3. Review joins, filters, aggregations, windows, deduplication, and date logic.
4. Check if the query can duplicate or drop rows.
5. Check if DISTINCT is hiding a modeling problem.
6. Check performance and readability.
7. Check SQL Server syntax if relevant.
8. Score from 0 to 5.
9. Explain what would fail in an interview.
10. Give corrected SQL or corrected pattern.
11. Add weaknesses and repair tasks when needed.

Use my context:
I have SQL Server/stored procedure exposure and need to become interview-ready in SQL for Data Engineering roles.
```


## 2. SQL Review Rubric

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


## 3. SQL Review Input Template

Collect:

```text
SQL query:
Database:
Business requirement:
Input tables:
Expected output:
Expected grain:
Known issue:
Data volume:
Performance concern:
```

If expected grain is missing, ask:

```text
What should one output row represent?
```


## 4. SQL Review Output Format

```text
# SQL Review

Requirement:
Database/dialect:
Expected grain:
Detected grain:
Overall score:
Verdict:

## Query Summary
...

## Correctness Issues
...

## Grain And Join Review
...

## Aggregation/Window Review
...

## Date/NULL/Edge Case Review
...

## Performance Review
...

## Readability Review
...

## Corrected Query
...

## Interview Explanation
...

## Weaknesses Added
...

## Repair Drill
...

## Files To Update
...
```


## 5. SQL Review Checklist

```text
business requirement clear
output grain defined
source tables correct
join type correct
join keys correct
filters correct
date range correct
aggregation correct
window function correct
dedupe keep rule clear
NULLs handled
duplicates avoided
metrics defined
query readable
CTEs useful
performance considered
indexes/partitioning considered
SQL dialect correct
```


## 6. Grain Review

### Check 1: What does one output row represent?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 2: Do joins preserve that grain?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 3: Does aggregation match that grain?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 4: Could fact-to-fact joins multiply rows?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 5: Is there a primary/natural key for output?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```


## 7. Join Review

### Check 1: Are join keys correct?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 2: Is join type correct?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 3: Can left join become inner join because of WHERE filter?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 4: Are many-to-many joins controlled?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 5: Are unmatched records expected?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```


## 8. Aggregation Review

### Check 1: Are GROUP BY columns correct?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 2: Are metrics summed/averaged at correct level?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 3: Is COUNT vs COUNT DISTINCT correct?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 4: Are duplicates affecting totals?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 5: Are denominators safe from zero?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```


## 9. Window Function Review

### Check 1: Is PARTITION BY correct?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 2: Is ORDER BY deterministic?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 3: Are ties handled?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 4: Is frame clause needed?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 5: Is ROW_NUMBER/RANK/DENSE_RANK chosen correctly?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```


## 10. Deduplication Review

### Check 1: What is the duplicate key?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 2: What is the keep rule?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 3: What is the tie-breaker?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 4: Is latest updated_at enough?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 5: Is source timestamp reliable?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```


## 11. Date Logic Review

### Check 1: Is date range inclusive/exclusive correct?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 2: Is timezone/business date considered?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 3: Is month/week grouping correct?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 4: Are late-arriving records handled?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 5: Is load_date confused with event_date?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```


## 12. Performance Review

### Check 1: Are filters pushed early?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 2: Are unnecessary columns selected?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 3: Are indexes useful?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 4: Are partitions pruned?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 5: Are repeated subqueries avoidable?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 6: Is SELECT * avoided?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```

### Check 7: Can CTE/materialization help?

Review instruction:

```text
Inspect the SQL for this issue.
If there is a problem, explain the failure mode and give corrected pattern.
```

Interview risk:

```text
A candidate who misses this may produce wrong business numbers.
```


## 13. Common SQL Review Findings

```text
Finding:
Output grain is not defined.

Impact:
The query may produce duplicated or aggregated-at-wrong-level results.

Fix:
Define one row per <entity/date/etc> and align joins/aggregation to that grain.
```

```text
Finding:
DISTINCT is used to hide duplicates.

Impact:
May hide a bad join and silently drop valid rows.

Fix:
Find duplicate source and deduplicate with ROW_NUMBER using a clear keep rule.
```

```text
Finding:
LEFT JOIN filter in WHERE turns query into INNER JOIN.

Impact:
Rows without matches are accidentally dropped.

Fix:
Move right-table filters into JOIN condition or explicitly handle NULL.
```


## 14. SQL Stored Procedure Review

For SQL Server stored procedures, also check:

```text
parameters
transaction handling
error handling TRY/CATCH
idempotency
DML safety
temp table usage
indexes on temp tables if large
NOCOUNT usage if applicable
deployment variables
SQLCMD :r path usage if script-based
environment-specific values
rollback strategy
```

Mentor prompt:

```text
Review this stored procedure for correctness, maintainability, deployment safety, and interview explanation.
```


## 15. SQL Review Progress Update

After every review, update or recommend updates to:

```text
CURRENT_STATE.md:
latest review result, score, active weakness, next action

ROADMAP_PROGRESS.md:
affected module status, evidence, readiness gate impact

NEXT_STEPS.md:
repair tasks and retest tasks

WEAKNESS_REGISTER.md:
new weakness, severity, repair plan, retest method

SESSION_LOG.md:
review session entry

PROJECT_PROGRESS.md:
if project/code/pipeline evidence changed

RESUME_STATE.md:
if a resume bullet or evidence changed

GITHUB_PORTFOLIO_STATE.md:
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


## 16. Final SQL Review Rule

```text
SQL review must protect correctness first.
A fast query that returns wrong numbers is a failed query.
```
