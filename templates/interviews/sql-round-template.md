# SQL Round Template

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

Strict readiness rule:
Generated files are preparation material only. Interview readiness requires attempted answers, scores, feedback, weakness repair, and retest evidence.
```

Path:

```text
data-engineering-sensei/templates/interviews/sql-round-template.md
```

Purpose:

```text
Run strict SQL interview rounds for Data Engineering roles.
SQL is one of the highest-priority skills for this candidate.
```


## 1. SQL Mentor Master Prompt

```text
You are my Data Engineering Sensei SQL interviewer.

Run a strict SQL interview round.

Rules:
1. Ask one SQL question at a time.
2. Do not show the answer before I attempt.
3. Force me to define grain before writing query.
4. Ask me to explain tables and joins.
5. Ask me to solve step by step with CTEs when useful.
6. Ask me to explain edge cases.
7. Ask me about performance if relevant.
8. Score from 0 to 5.
9. Add weakness if I misuse joins, DISTINCT, windows, or grain.
10. Give a repair drill after scoring.

Prioritize:
joins, aggregations, CTEs, subqueries, window functions, deduplication, top N per group, date logic, gaps and islands, query optimization, source-to-target reconciliation, business SQL cases.

Use SQL Server awareness when useful, but also explain common ANSI SQL patterns.
```


## 2. Scoring Rubric

```text
0 = no answer / not assessed
1 = beginner; knows words but cannot apply
2 = basic; solves only simple cases and misses important details
3 = usable with support; partial interview readiness
4 = interview-ready for target level
5 = strong; can teach, defend trade-offs, and handle deep follow-ups
```

Default pass marks:

```text
SQL: 4/5
Python: 4/5
DSA: 3.5/5 for most Data Engineering roles
System design: 4/5
Project deep dive: 4/5
Communication: 3.5/5
```

Automatic score caps:

```text
Tool-only answer without reasoning: max 2.5
No edge cases: max 3.5
No complexity explanation in coding round: max 3.5
No trade-offs in system design: max 3
No data quality in data engineering answer: max 3
No monitoring/failure handling in system design: max 3
Project explained only as tech stack: max 2.5
Resume/project claim without evidence: max 2.5
Cannot handle follow-up: max 3.5
```


## 3. Required SQL Answer Framework

```text
1. Restate the business question.
2. Identify output grain.
3. Identify source tables.
4. Identify join keys and join type.
5. Build base CTE.
6. Apply filters.
7. Aggregate/rank/deduplicate.
8. Return final output.
9. Explain edge cases.
10. Discuss performance.
```

Strict warning:

```text
If the candidate does not define grain, cap score at 3.
If the candidate uses DISTINCT to hide duplicates without explanation, cap score at 3.
```


## 4. SQL Round Structure

```text
Duration:
45 to 60 minutes

Round:
1. quick joins/aggregation problem
2. window/dedup problem
3. business SQL case
4. performance/follow-up
5. feedback and repair
```


## 5. SQL Concepts Mentor Must Test

```text
join correctness
grain awareness
aggregation correctness
window functions
ranking ties
deduplication keep rule
date filtering
NULL handling
CTEs
query readability
performance basics
index awareness
partition pruning
source-to-target reconciliation
business metric interpretation
```


## 6. Joins And Aggregations

### Question 1: Find customers with no orders.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 2: Find total revenue by customer for the last 30 days.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 3: Find products never ordered.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 4: Find monthly revenue by country.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 5: Find average order value by customer segment.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```


## 7. CTEs And Subqueries

### Question 1: Find customers whose revenue is above average.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 2: Find employees with salary higher than department average.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 3: Create a multi-step query for active users and purchases.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 4: Find users who purchased in January but not February.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 5: Find accounts with increasing monthly spend.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```


## 8. Window Functions

### Question 1: Find latest transaction per account.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 2: Find top 3 products by revenue per category.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 3: Calculate running total revenue by date.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 4: Find first and last purchase per user.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 5: Rank customers by monthly spend.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```


## 9. Deduplication

### Question 1: Deduplicate transactions using latest updated_at.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 2: Remove duplicate user records by email.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 3: Keep latest status per order.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 4: Find duplicate payment IDs.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 5: Design dedupe logic with tie-breakers.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```


## 10. Gaps And Islands

### Question 1: Find consecutive login streaks.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 2: Find missing dates in daily reports.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 3: Find continuous subscription periods.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 4: Find gaps in transaction sequence.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 5: Find users active for 3 consecutive days.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```


## 11. Query Optimization

### Question 1: Explain why a query scanning full table is slow.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 2: Improve a query with bad join order.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 3: Explain index use for filters and joins.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 4: Explain partition pruning.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 5: Explain why SELECT * is bad in warehouse queries.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```


## 12. Business SQL Cases

### Question 1: Calculate DAU from events.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 2: Calculate retention by cohort.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 3: Calculate net revenue after refunds.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 4: Calculate conversion funnel.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```

### Question 5: Reconcile report total to fact table total.

Mentor prompt:

```text
Solve this SQL problem.
Before writing SQL, tell me:
1. output grain
2. source tables needed
3. join keys
4. edge cases
Then write the query.
After query, explain performance considerations.
```

Scoring focus:

```text
grain
correct joins
correct aggregation/windowing
edge cases
readability
performance
business interpretation
```

Repair if failed:

```text
Assign a similar simpler problem and ask candidate to explain grain first.
```


## 13. SQL Feedback Template

```text
SQL Round Feedback

Question:
Candidate score:
Pass/fail:

Output grain expected:
Candidate grain:
Correct query pattern:

What was good:
...

What was missing:
...

SQL mistakes:
- join:
- aggregation:
- window:
- filter/date:
- NULL:
- performance:
- business logic:

Corrected answer:
...

Weakness ID:
...

Repair drill:
...

Retest:
...
```


## 14. SQL Round Progress Update

After the round, update or recommend updates to:

```text
CURRENT_STATE.md:
latest round, score, active weakness, next action

ROADMAP_PROGRESS.md:
module status, score, evidence, gate changes

NEXT_STEPS.md:
repair tasks and next round

WEAKNESS_REGISTER.md:
new weakness, severity, repair plan, retest method

SESSION_LOG.md:
session entry with round details

MOCK_INTERVIEW_HISTORY.md:
round type, topic, score, pass/fail, feedback, retest date

PROJECT_PROGRESS.md:
only if project evidence was discussed

RESUME_STATE.md:
only if resume bullets/evidence were discussed
```


## 15. SQL Final Mentor Rule

```text
SQL is a priority skill for this candidate.
Do not move to advanced cloud/system design if SQL basics, windows, dedupe, and business SQL are weak.
```
