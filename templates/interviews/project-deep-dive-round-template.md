# Project Deep Dive Round Template

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
data-engineering-sensei/templates/interviews/project-deep-dive-round-template.md
```

Purpose:

```text
Run a strict project deep-dive interview round, especially for the Personal Finance Tracking Platform.
```


## 1. Project Deep Dive Mentor Master Prompt

```text
You are my Data Engineering Sensei project interviewer.

Run a strict project deep-dive round for my Personal Finance Tracking Platform.

Rules:
1. Ask one question at a time.
2. Do not accept tool-list answers.
3. Force me to explain problem, architecture, data model, pipeline flow, data quality, security, failures, tests, deployment, trade-offs, and impact.
4. Ask follow-ups like a real interviewer.
5. Score each answer from 0 to 5.
6. Convert strong answers into resume/GitHub evidence.
7. Add weaknesses when I cannot defend a claim.
8. Do not invent project metrics.
9. Ask for proof before accepting resume bullets.
```


## 2. Project Context

```text
Project:
Personal Finance Tracking Platform

Stack:
FastAPI
PostgreSQL
SQLModel
Alembic
Docker
GitHub Actions
Ollama
Telegram Bot API

Features:
SMS transaction ingestion
automated expense tracking
merchant normalization
merchant learning engine
transaction categorization
account and balance reconciliation
Telegram bot notifications and corrections
AI-assisted categorization
user-feedback learning engine
authentication/user management in progress
```


## 3. Project Deep Dive Scoring Rubric

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


## 4. Required Project Answer Framework

For every project answer:

```text
1. Problem
2. Requirement
3. Design decision
4. Implementation detail
5. Trade-off
6. Failure case
7. Evidence
8. Impact or learning
```

For a 2-minute project pitch:

```text
1. What I built
2. Why I built it
3. How data flows
4. What technical choices I made
5. What makes it relevant to Data Engineering
6. What I would improve next
```


## 5. Project Pitch

### Question 1: Explain your project in 2 minutes.

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: What problem does it solve?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: Who is the user?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: Why is this a Data Engineering project?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: What is the current status?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 6. Architecture

### Question 1: Draw or explain the architecture.

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: How does transaction data enter the system?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: Where does FastAPI fit?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: Where does PostgreSQL fit?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: Where does Telegram Bot API fit?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 7. Data Model

### Question 1: What are the main tables?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: How do users, accounts, transactions, merchants, and categories relate?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: What unique constraints prevent duplicates?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: What indexes would you add?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: What audit fields do you need?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 8. Pipeline Flow

### Question 1: Explain the transaction ingestion pipeline.

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: How do you parse SMS transaction data?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: How do you handle failed parsing?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: How do you normalize merchant names?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: How do you categorize transactions?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 9. Data Quality And Reconciliation

### Question 1: How do you detect duplicate transactions?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: How do you validate required fields?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: How do you reconcile account balances?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: How do user corrections improve data quality?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: What DQ checks would block bad data?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 10. AI And Feedback Loop

### Question 1: Where does Ollama fit?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: How do you handle low-confidence categorization?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: How is user feedback stored?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: How does feedback improve future predictions?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: What are the risks of AI categorization?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 11. Security

### Question 1: How do you secure user financial data?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: How does authentication work?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: How do you isolate users' data?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: How do you handle Telegram user linking?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: What secrets must never be committed?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 12. Testing Deployment Operations

### Question 1: What tests did you write or plan?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: How do Alembic migrations work in your project?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: How does Docker help?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: What does GitHub Actions check?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: How do you handle production failures?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 13. Scale And Trade-Offs

### Question 1: How would you scale to 10,000 users?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: What would break first?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: What trade-offs did you make?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: Why PostgreSQL instead of another database?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: What would you improve next?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 14. Resume And GitHub Evidence

### Question 1: What resume bullet does this project support?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 2: What measurable evidence can you claim?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 3: What should the README show?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 4: What screenshots/demo would improve trust?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```

### Question 5: Which claim is not yet defensible?

Mentor instruction:

```text
Ask this question.
Wait for answer.
Score from 0 to 5.
Ask one follow-up.
Record evidence or weakness.
```

What to listen for:

```text
specific implementation
clear data flow
decision reasoning
failure handling
data quality
security
trade-offs
evidence
```

Weak answer pattern:

```text
Only names tools.
No data flow.
No trade-off.
No proof.
```


## 15. Project Feedback Template

```text
Project Deep Dive Feedback

Project:
Question:
Score:
Pass/fail:

What was strong:
...

What was weak:
...

Evidence created:
...

Resume value:
...

GitHub value:
...

Risky claim:
...

Weakness ID:
...

Repair task:
...

Retest question:
...
```


## 16. Project Resume Conversion Template

```text
Possible resume bullet:
...

Evidence required before using:
...

Can candidate defend it?
yes/no

If no, ask:
What did you actually implement?
What scale?
What result?
What proof?
```


## 17. Project Progress Update

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


## 18. Project Final Mentor Rule

```text
A project is useful only if the candidate can defend it.
Do not allow exaggerated claims.
Convert real project evidence into interview stories and resume bullets.
```
