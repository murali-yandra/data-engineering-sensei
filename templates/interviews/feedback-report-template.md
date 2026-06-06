# Feedback Report Template

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
data-engineering-sensei/templates/interviews/feedback-report-template.md
```

Purpose:

```text
Create detailed feedback reports after drills, rounds, mocks, project reviews, resume reviews, and roadmap assessments.
```


## 1. Feedback Report Master Prompt

```text
You are my Data Engineering Sensei feedback mentor.

Create a strict feedback report for my latest answer/session.

Rules:
1. Score from 0 to 5.
2. Be direct and practical.
3. Separate strengths from weaknesses.
4. Explain why each weakness matters in interviews.
5. Give corrected answer or corrected approach.
6. Assign repair drills.
7. Identify which progress files must be updated.
8. Do not say I did well unless evidence supports it.
9. Do not give vague motivation.
10. End with next 3 actions.
```


## 2. Feedback Score Scale

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


## 3. Universal Feedback Format

```text
# Feedback Report

Session:
Topic:
Date:
Target role:
Score:
Verdict:

## What Was Good
...

## What Was Missing
...

## Interview Risk
...

## Corrected Answer / Better Approach
...

## Weaknesses Added
...

## Repair Plan
...

## Retest Plan
...

## Next 3 Actions
...

## Files To Update
...
```


## 4. Feedback Severity Levels

```text
Critical:
will likely fail interview

High:
seriously hurts score

Medium:
noticeable improvement needed

Low:
polish issue
```

Feedback rule:

```text
Every Critical or High issue must create a WEAKNESS_REGISTER.md entry and NEXT_STEPS.md repair task.
```


## 5. SQL Feedback

Evaluate:

- grain correctness
- join correctness
- aggregation
- window function
- dedupe logic
- NULL/date handling
- performance

Feedback prompt:

```text
Give feedback for this area.
For each issue:
1. what happened
2. why it matters
3. severity
4. repair action
5. retest method
```


## 6. Python Feedback

Evaluate:

- correctness
- data structures
- edge cases
- readability
- error handling
- logging
- testing

Feedback prompt:

```text
Give feedback for this area.
For each issue:
1. what happened
2. why it matters
3. severity
4. repair action
5. retest method
```


## 7. DSA Feedback

Evaluate:

- pattern recognition
- brute force
- optimized approach
- code
- dry run
- complexity

Feedback prompt:

```text
Give feedback for this area.
For each issue:
1. what happened
2. why it matters
3. severity
4. repair action
5. retest method
```


## 8. System Design Feedback

Evaluate:

- requirements
- architecture
- data model
- processing
- idempotency
- DQ
- monitoring
- security
- cost
- trade-offs

Feedback prompt:

```text
Give feedback for this area.
For each issue:
1. what happened
2. why it matters
3. severity
4. repair action
5. retest method
```


## 9. Project Feedback

Evaluate:

- problem clarity
- architecture
- data model
- pipeline flow
- evidence
- security
- testing
- impact

Feedback prompt:

```text
Give feedback for this area.
For each issue:
1. what happened
2. why it matters
3. severity
4. repair action
5. retest method
```


## 10. Communication Feedback

Evaluate:

- structure
- clarity
- conciseness
- confidence
- examples
- follow-up handling
- summary

Feedback prompt:

```text
Give feedback for this area.
For each issue:
1. what happened
2. why it matters
3. severity
4. repair action
5. retest method
```


## 11. Resume/GitHub Feedback

Evaluate:

- role alignment
- evidence
- metrics
- project proof
- README clarity
- defensibility

Feedback prompt:

```text
Give feedback for this area.
For each issue:
1. what happened
2. why it matters
3. severity
4. repair action
5. retest method
```


## 12. Weakness Entry Generator

```text
Create weakness entry:

Weakness ID:
Area:
Topic:
Severity:
Evidence:
Why it matters:
Repair task:
Retest:
Target score:
Related file:
```


## 13. Repair Plan Generator

```text
Create repair plan:

Weakness:
Current score:
Target score:
Time box:
Drill 1:
Drill 2:
Drill 3:
Retest:
Pass condition:
Files to update:
```


## 14. Feedback Report Examples

Example verdicts:

```text
Score 2/5:
You know the terms, but the answer is not interview-ready because it lacks structure, examples, and failure handling.

Score 3/5:
Usable foundation, but you missed important production details. Needs repair before real interviews.

Score 4/5:
Interview-ready for this level. Minor polish remains.

Score 5/5:
Strong answer. You handled requirements, trade-offs, edge cases, and follow-ups.
```


## 15. Feedback Progress Update

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


## 16. Final Feedback Rule

```text
Feedback must create action.
If there is no repair task, retest, or next step, the feedback is incomplete.
```
