# Project Deep Dive Round Template

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

Strict readiness rule:
Generated files are preparation material only. Interview readiness requires attempted answers, scores, feedback, weakness repair, and retest evidence.
```

Path:

```text
data-engineering-sensei/templates/interviews/project-deep-dive-round-template.md
```

Purpose:

```text
Run a strict project deep-dive interview round, especially for the Primary Portfolio Data Project.
```


## 1. Project Deep Dive Mentor Master Prompt

```text
You are my Data Engineering Sensei project interviewer.

Run a strict project deep-dive round for my Primary Portfolio Data Project.

Rules:
1. Ask one question at a time.
2. Do not accept tool-list answers.
3. Force me to explain problem, architecture, data model, pipeline flow, data quality, security, failures, tests, deployment, trade-offs, and impact.
4. Ask follow-ups like a real interviewer.
5. Score each answer from 0 to 5.
6. Convert strong answers into resume/public portfolio evidence.
7. Add weaknesses when I cannot defend a claim.
8. Do not invent project metrics.
9. Ask for proof before accepting resume bullets.
```


## 2. Project Context

```text
Project:
Primary Portfolio Data Project

Stack:
candidate-provided implementation stack only
source system or raw data source
ingestion layer
storage, warehouse, lakehouse, or database
transformation and modeling layer
orchestration or scheduling if implemented
tests and data quality checks
CI/CD, Docker, monitoring, or deployment if implemented
reporting, dashboard, API, or downstream consumer if relevant

Features:
source ingestion
validation and quarantine
staging and transformations
analytics model or serving output
deduplication and idempotency
data quality checks
reconciliation where applicable
orchestration, monitoring, and backfill/replay
public portfolio documentation
resume and interview evidence
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

### Question 3: Where does the backend or service layer fit?

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

### Question 4: Where does your storage or warehouse layer fit?

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

### Question 5: Where does user-facing notification or feedback channel fit?

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

### Question 2: How do source, staging, final model, quality, and serving tables relate?

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

### Question 2: How do you parse or ingest raw source data?

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

### Question 4: How do you standardize, enrich, or map raw values?

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


## 10. Optional Automation, AI, And Feedback Loop

### Question 1: Where does optional automation, AI, or feedback fit if implemented?

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

### Question 4: How do you handle identity, access, or ownership for user-facing outputs?

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

### Question 2: How do schema changes or migrations work in your project?

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

### Question 4: What does CI/CD workflows check?

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

### Question 4: Why did you choose your storage, database, warehouse, or lakehouse technology?

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


## 14. Resume And public portfolio Evidence

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

public portfolio value:
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
progress/CURRENT_STATE.md:
latest round, score, active weakness, next action

progress/ROADMAP_PROGRESS.md:
module status, score, evidence, gate changes

progress/NEXT_STEPS.md:
repair tasks and next round

progress/WEAKNESS_REGISTER.md:
new weakness, severity, repair plan, retest method

progress/SESSION_LOG.md:
session entry with round details

progress/MOCK_INTERVIEW_HISTORY.md:
round type, topic, score, pass/fail, feedback, retest date

progress/PROJECT_PROGRESS.md:
only if project evidence was discussed

progress/RESUME_STATE.md:
only if resume bullets/evidence were discussed
```


## 18. Project Final Mentor Rule

```text
A project is useful only if the candidate can defend it.
Do not allow exaggerated claims.
Convert real project evidence into interview stories and resume bullets.
```
