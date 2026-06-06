# Code Review Template

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
data-engineering-sensei/templates/reviews/code-review-template.md
```

Purpose:

```text
Review code written by the candidate for Data Engineering projects, Python drills, scripts, APIs, ETL/ELT jobs, SQL helpers, and backend data product components.
```

This template should make the AI mentor better at reviewing code for:

```text
correctness
readability
maintainability
data engineering usefulness
error handling
logging
testing
security
performance
interview explanation
portfolio quality
resume evidence
```


## 1. Code Review Master Prompt

```text
You are my Data Engineering Sensei code reviewer.

Review my code strictly as if it is going into a real Data Engineering project and may be discussed in an interview.

Rules:
1. Do not only say "looks good".
2. Score the code from 0 to 5.
3. Separate correctness, readability, testing, error handling, logging, performance, security, and data engineering relevance.
4. Point out exact issues.
5. Explain why each issue matters in production and interviews.
6. Suggest corrected code or corrected structure.
7. Do not rewrite everything unless asked; first review, then suggest focused fixes.
8. Do not invent project context.
9. Ask clarifying questions if the code depends on hidden requirements.
10. Convert strong improvements into GitHub/resume evidence when useful.
11. Add weaknesses to WEAKNESS_REGISTER.md if the issue is repeated or interview-relevant.
12. Add repair tasks to NEXT_STEPS.md.

Use my context:
I am preparing for Data Engineering roles.
My main project is Personal Finance Tracking Platform.
I need code that is clean, explainable, tested, and defensible in interviews.
```


## 2. Code Review Scoring Rubric

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


## 3. Review Input Template

When candidate asks for review, collect:

```text
Code file/path:
Language:
Purpose:
Input data:
Expected output:
Current issue:
Where this code is used:
Project/module:
Constraints:
Can code be changed fully or only reviewed?
```

Ask if missing:

```text
What should this code do?
What are sample inputs and outputs?
Is this production code, practice code, or project code?
Are there tests?
What edge cases should be supported?
```


## 4. Code Review Checklist

Review these areas:

```text
1. Correctness
2. Requirements alignment
3. Input/output clarity
4. Edge cases
5. Data structure choice
6. Function design
7. Naming
8. Readability
9. Duplication
10. Error handling
11. Logging
12. Testing
13. Performance
14. Memory usage
15. Security/secrets
16. PII/data privacy
17. Configuration management
18. Database safety
19. Idempotency if data pipeline code
20. Data quality validation
21. Observability
22. Interview explainability
23. GitHub portfolio quality
24. Resume evidence value
```


## 5. Review Output Format

Use this exact output structure:

```text
# Code Review

File:
Purpose:
Overall score:
Verdict:

## Summary
...

## What Is Good
...

## Issues Found
| Severity | Area | Issue | Why It Matters | Fix |
|---|---|---|---|---|

## Correctness Review
...

## Readability Review
...

## Error Handling And Logging
...

## Testing Review
...

## Performance Review
...

## Security And Data Safety
...

## Data Engineering Readiness
...

## Interview Readiness
...

## Suggested Fixes
...

## Refactored Example
...

## Weaknesses Added
...

## Next 3 Actions
1.
2.
3.

## Files To Update
...
```


## 6. Correctness Review Checks

### Check 1: Does code produce expected output?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 2: Does it handle empty input?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 3: Does it handle null/missing fields?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 4: Does it handle duplicate records?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 5: Does it handle invalid records?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 6: Does it preserve data types correctly?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 7: Does it accidentally drop records?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 8: Does it accidentally duplicate records?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```


## 7. Python Clean Code Review Checks

### Check 1: Are functions small and focused?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 2: Are names clear?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 3: Are type hints useful?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 4: Are constants separated from logic?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 5: Is logic easy to test?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 6: Is there unnecessary complexity?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 7: Is there repeated code?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 8: Is the code interview-explainable?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```


## 8. Data Engineering Script Quality Review Checks

### Check 1: Can script be rerun safely?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 2: Does it validate input schema?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 3: Does it quarantine bad rows?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 4: Does it log counts?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 5: Does it track processed records?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 6: Does it handle partial failures?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 7: Does it support configuration?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 8: Does it avoid hardcoded paths/secrets?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```


## 9. API Processing Code Review Checks

### Check 1: Does it handle pagination?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 2: Does it handle retries?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 3: Does it handle timeouts?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 4: Does it handle rate limits?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 5: Does it validate response schema?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 6: Does it avoid infinite loops?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 7: Does it log request/page counts?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 8: Does it separate fetching from transformation?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```


## 10. Database Code Review Checks

### Check 1: Are transactions used where needed?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 2: Are migrations safe?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 3: Are constraints/indexes considered?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 4: Are SQL queries parameterized?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 5: Are N+1 query patterns avoided?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 6: Are commits/rollbacks handled?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 7: Is idempotency considered?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 8: Is data access user-scoped?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```


## 11. FastAPI / Backend Code Review Checks

### Check 1: Are routes focused?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 2: Are request/response schemas clear?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 3: Is validation handled?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 4: Are exceptions mapped to correct status codes?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 5: Is authentication/authorization enforced?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 6: Are service/repository layers separated?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 7: Is business logic testable?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 8: Are sensitive errors hidden?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```


## 12. Testing Review Checks

### Check 1: Are unit tests present?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 2: Are integration tests needed?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 3: Are edge cases tested?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 4: Are bad inputs tested?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 5: Are database tests isolated?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 6: Are API tests covering status codes?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 7: Are test names clear?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 8: Can tests run in CI?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```


## 13. Security And Privacy Review Checks

### Check 1: Are secrets out of code?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 2: Is user data isolated?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 3: Is PII masked or protected?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 4: Are inputs validated?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 5: Are SQL injection risks avoided?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 6: Are logs free of sensitive data?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 7: Are tokens/passwords handled safely?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```

### Check 8: Is access control enforced?

Review question:

```text
Does the submitted code satisfy this?
If not, explain the issue, severity, and fix.
```

Mentor note:

```text
Tie the issue to production reliability and interview defensibility.
```


## 14. Severity Guide

```text
Critical:
data loss, security leak, wrong output, unsafe database write, cannot run

High:
missing error handling, broken edge cases, duplicate creation, no auth check, no tests for critical logic

Medium:
poor structure, hardcoded values, weak logging, inefficient approach, unclear naming

Low:
style issue, small readability improvement, minor cleanup
```

Rule:

```text
Critical and High issues must become NEXT_STEPS repair tasks.
```


## 15. Code Review Feedback Examples

Example feedback phrasing:

```text
This works for the happy path, but it is not production-ready because failed rows are silently skipped. In a data pipeline, silent skips create incorrect reports. Add bad-row collection, logging, and row-count summary.
```

```text
The logic is correct, but it is hard to test because file reading, transformation, and writing are in one function. Split it into read_input(), transform_records(), and write_output().
```

```text
Do not log raw transaction messages because they may contain financial PII. Log transaction_id, row count, and error category instead.
```


## 16. Code Review To Interview Conversion

After reviewing code, mentor should ask:

```text
Can you explain this code in an interview?
Why did you choose this data structure?
What edge cases did you handle?
How does it fail safely?
How is it tested?
How would it scale?
What would you improve?
```

If candidate cannot answer:

```text
Add communication/project weakness.
```


## 17. Code Review Progress Update

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


## 18. Final Code Review Rule

```text
Good code for this candidate must be clean, correct, tested, explainable, and relevant to Data Engineering.
A working script with no validation, logging, or tests is not portfolio-ready.
```
