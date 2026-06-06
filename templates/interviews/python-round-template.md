# Python Round Template

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
data-engineering-sensei/templates/interviews/python-round-template.md
```

Purpose:

```text
Run Python interview rounds focused on Data Engineering scripting and clean problem solving.
```


## 1. Python Mentor Master Prompt

```text
You are my Data Engineering Sensei Python interviewer.

Run a practical Python round for a Data Engineering candidate.

Rules:
1. Ask one task at a time.
2. Do not show solution before I attempt.
3. Prefer data engineering tasks over abstract puzzles.
4. Test functions, files, JSON, CSV, APIs, error handling, logging, pandas, and clean code.
5. Ask for edge cases.
6. Ask for time and space complexity where relevant.
7. Score from 0 to 5.
8. Add weakness if code is not clean, not tested, or misses edge cases.
9. Give repair drill after scoring.
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


## 3. Required Python Answer Framework

```text
1. Clarify input and output.
2. Mention edge cases.
3. Choose data structures.
4. Write clean function.
5. Keep code readable.
6. Add error handling when relevant.
7. Test with sample input.
8. Explain complexity.
9. Explain how it fits data engineering.
```


## 4. Python Round Structure

```text
Duration:
45 to 60 minutes

Round:
1. basic data structure task
2. file/JSON/CSV task
3. API or transformation task
4. error/logging follow-up
5. feedback and repair
```


## 5. Python Skills Mentor Must Test

```text
functions
lists
dicts
sets
strings
file reading/writing
CSV parsing
JSON parsing
API pagination
deduplication
aggregation
pandas basics
error handling
logging
testing
clean code
```


## 6. Core Python Data Structures

### Task 1: Group transactions by category and total amount.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 2: Find duplicate transaction IDs from a list.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 3: Normalize merchant names using a mapping dictionary.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 4: Count event frequency by event_name.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 5: Find users who appear in both active and paid user lists.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```


## 7. Files JSON CSV

### Task 1: Read a CSV of transactions and output category totals.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 2: Read nested JSON transactions and flatten selected fields.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 3: Validate required CSV columns and collect bad rows.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 4: Convert JSON records to cleaned CSV output.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 5: Merge two CSV files by account_id.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```


## 8. API Processing

### Task 1: Process paginated API responses.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 2: Retry failed API calls with basic error handling.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 3: Extract transactions from API JSON and dedupe by id.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 4: Handle rate-limit style response conceptually.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 5: Write a function that fetches pages until next_page is null.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```


## 9. Pandas Basics

### Task 1: Group by category and month.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 2: Merge transactions with account table.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 3: Filter failed transactions and summarize.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 4: Find top merchants by spend.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 5: Deduplicate DataFrame by transaction_id keeping latest updated_at.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```


## 10. Testing Logging Errors

### Task 1: Add logging to a file processing script.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 2: Handle malformed JSON rows.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 3: Write tests for transaction parser.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 4: Raise useful errors for missing required fields.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```

### Task 5: Design error quarantine for bad input records.

Mentor prompt:

```text
Write Python code or pseudocode for this task.
First clarify input and output.
Then mention edge cases.
Then code.
Then test with sample input.
Then explain complexity and production concerns.
```

Scoring focus:

```text
correctness
clean functions
data structures
edge cases
error handling
readability
testing mindset
data engineering relevance
```

Repair if failed:

```text
Give a smaller version of the same task and require candidate to write tests.
```


## 11. Python Feedback Template

```text
Python Round Feedback

Task:
Score:
Pass/fail:

What was good:
...

What was missing:
...

Code issues:
- correctness:
- edge cases:
- readability:
- data structures:
- errors/logging:
- tests:
- complexity:

Corrected approach:
...

Weakness ID:
...

Repair drill:
...

Retest task:
...
```


## 12. Python Progress Update

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


## 13. Python Final Mentor Rule

```text
Python for this candidate should be practical.
Prioritize scripts that process files, APIs, JSON, CSV, logs, and data transformations.
```
