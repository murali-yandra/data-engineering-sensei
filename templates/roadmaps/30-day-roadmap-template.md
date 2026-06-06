# 30-Day Roadmap Template

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

Important templates already created:
templates/assessment/*
templates/interviews/*
templates/reviews/*

Strict readiness rule:
Generated files are preparation material only.
Interview readiness requires baseline assessment, scored practice, mock interviews, weakness repair, retest evidence, and portfolio/resume proof.
```

Path:

```text
data-engineering-sensei/templates/roadmaps/30-day-roadmap-template.md
```

Purpose:

```text
Create a focused 30-day Data Engineering interview-readiness sprint.
This roadmap is for fast baseline, repair, and proof-building.
```

Best use:

```text
Use when candidate has limited time and needs a realistic push toward interview readiness.
Use after intake or baseline assessment.
```


## 1. 30-Day Roadmap Mentor Prompt

```text
You are my Data Engineering Sensei roadmap mentor.

Create a strict 30-day roadmap for me.

Use my context:
- I am an early-career data professional with around 2 years of experience.
- I am targeting Data Engineer / Analytics Engineer / ETL Developer roles.
- My main project is Primary Portfolio Data Project.
- I need SQL, Python, DSA patterns, DE fundamentals, system design, project deep dive, resume/public portfolio, and mock interview preparation.
- I want no-sugarcoating guidance.
- I prefer visual, structured, practical learning.

Rules:
1. Do not create a generic roadmap.
2. First use my baseline scores if available.
3. If baseline scores are missing, start with baseline assessment.
4. Focus on highest ROI for Data Engineering jobs.
5. Include daily tasks.
6. Include evidence output for every day.
7. Include mock interviews.
8. Include weakness repair and retests.
9. Include project/resume/public portfolio work.
10. Tell me exactly which progress files to update.

Make the roadmap realistic.
If 30 days is not enough for full readiness, say that clearly.
```


## 2. 30-Day Roadmap Scoring And Gates

Use this 0 to 5 scale:

```text
0 = not assessed / no evidence
1 = beginner; knows words but cannot apply
2 = basic; can do simple cases but fails follow-ups
3 = usable with support; partial interview readiness
4 = interview-ready for target level
5 = strong; can teach, defend trade-offs, and handle deep follow-ups
```

Default pass marks:

```text
SQL: 4/5
Python: 4/5
DSA: 3.5/5 for most Data Engineering roles
Data Engineering fundamentals: 4/5
System design: 4/5
Project deep dive: 4/5
Resume/public portfolio readiness: 4/5
Communication: 3.5/5
```

Readiness verdicts:

```text
not_ready:
baseline missing or core score below target

partially_ready:
some core areas pass but project/system design/resume still weak

selectively_ready:
can apply to limited roles matching current strengths

interview_ready:
core scores meet target and mocks are passing

strong_candidate:
scores >= 4 across core areas, project/resume/public portfolio are defensible, and no critical weaknesses are open
```


## 3. 30-Day Roadmap Principles

Core roadmap rules:

```text
1. Do not mark anything complete only because a file was generated.
2. Mark complete only when there is evidence.
3. Evidence can be solved problems, code, mock scores, project proof, resume bullets, public portfolio updates, or retest results.
4. If score is below target, create a weakness and repair task.
5. If a weakness is repaired, retest before marking it repaired.
6. Keep tasks small, time-boxed, and measurable.
7. Prefer SQL, Python, project depth, and core system design before advanced topics.
8. Do not start aggressive job applications before readiness gates are met.
```

High-ROI preparation order for this candidate:

```text
1. Baseline assessment
2. SQL interview readiness
3. Python data scripting
4. Data Engineering fundamentals
5. Batch pipeline + data warehouse + data quality system design
6. Primary Portfolio Data Project deep dive
7. Resume/public portfolio evidence
8. Mock interview loop
9. Targeted job applications
```


## 4. 30-Day Roadmap Overview

The 30-day roadmap is divided into 4 weeks:

```text
Week 1:
Baseline + SQL/Python foundations

Week 2:
Data Engineering fundamentals + SQL/Python repair

Week 3:
System design + project deep dive

Week 4:
Mock interviews + resume/public portfolio polish + application readiness check
```

Expected result after 30 days:

```text
Best case:
Candidate becomes selectively ready for junior/early-mid Data Engineering or Analytics Engineering roles.

Realistic case:
Candidate has clear scores, repaired top weaknesses, stronger project explanation, and can begin selective applications.

Not realistic if starting from weak baseline:
Full FAANG-level readiness in 30 days.
```


## 5. Required Inputs Before Starting

Before generating the personalized 30-day roadmap, collect:

```text
SQL score
Python score
DSA score
DE fundamentals score
System design score
Project deep-dive score
Resume/public portfolio score
Communication score
available hours per day
target roles
target companies/location
main project status
biggest blockers
```

If scores are missing:

```text
Day 1 must be baseline assessment.
```


## 6. Week 1: Baseline, SQL, Python

| Day | Task | Evidence Output | Progress Files |
|---|---|---|---|
| Day 1 | Run full baseline assessment | scores across SQL, Python, DSA, DE fundamentals, system design, project, resume/public portfolio | CANDIDATE_PROFILE, CURRENT_STATE, ROADMAP_PROGRESS, NEXT_STEPS, WEAKNESS_REGISTER |
| Day 2 | SQL joins + aggregation baseline drill | 5 solved SQL problems + score | SESSION_LOG, WEAKNESS_REGISTER, NEXT_STEPS |
| Day 3 | SQL CTEs + window functions | 5 solved SQL problems + mistakes | SESSION_LOG, WEAKNESS_REGISTER |
| Day 4 | Python CSV/JSON processing drill | 1 working script + review | SESSION_LOG, WEAKNESS_REGISTER |
| Day 5 | Python API processing + error handling | 1 working API/pagination script | SESSION_LOG, WEAKNESS_REGISTER |
| Day 6 | DSA hashmap + sliding window patterns | 5 problems + pattern score | SESSION_LOG, WEAKNESS_REGISTER |
| Day 7 | Weekly review + retest weakest SQL/Python topic | weekly score update + next week tasks | ROADMAP_PROGRESS, NEXT_STEPS |


Daily rule:

```text
Each day must produce evidence.
If no evidence was produced, the task is not complete.
```


## 7. Week 2: DE Fundamentals And Core Repair

| Day | Task | Evidence Output | Progress Files |
|---|---|---|---|
| Day 8 | ETL vs ELT, batch vs streaming, warehouse vs lake | 3 interview explanations scored | SESSION_LOG |
| Day 9 | Idempotency, backfills, partitioning | 3 production-style explanations scored | WEAKNESS_REGISTER |
| Day 10 | Data quality fundamentals | DQ checks for sample pipeline | SESSION_LOG |
| Day 11 | Airflow/orchestration basics | DAG explanation + failure/retry answer | SESSION_LOG |
| Day 12 | SQL business case: reporting/revenue/funnel | 2 business SQL problems | WEAKNESS_REGISTER |
| Day 13 | Python pandas basics or scripting repair | 1 transformation script | SESSION_LOG |
| Day 14 | Week 2 mock: SQL + DE fundamentals | mock score + repair plan | MOCK_INTERVIEW_HISTORY, WEAKNESS_REGISTER |


Daily rule:

```text
Each day must produce evidence.
If no evidence was produced, the task is not complete.
```


## 8. Week 3: System Design And Project Deep Dive

| Day | Task | Evidence Output | Progress Files |
|---|---|---|---|
| Day 15 | Batch pipeline system design | 45-minute mock + score | MOCK_INTERVIEW_HISTORY, WEAKNESS_REGISTER |
| Day 16 | Data warehouse design | schema/grain/fact-dim design | SESSION_LOG |
| Day 17 | Data quality framework design | DQ framework answer + score | MOCK_INTERVIEW_HISTORY |
| Day 18 | Reporting pipeline design | metrics/grain/reconciliation design | SESSION_LOG |
| Day 19 | Portfolio project project pitch | 2-minute + 5-minute project explanation scored | PROJECT_PROGRESS |
| Day 20 | Portfolio project architecture + database deep dive | architecture + schema explanation | PROJECT_PROGRESS |
| Day 21 | Week 3 review + system design retest | score update + active weaknesses | ROADMAP_PROGRESS, NEXT_STEPS |


Daily rule:

```text
Each day must produce evidence.
If no evidence was produced, the task is not complete.
```


## 9. Week 4: Mock Loop, Resume, public portfolio, Job Readiness

| Day | Task | Evidence Output | Progress Files |
|---|---|---|---|
| Day 22 | Project deep-dive mock | project score + resume evidence | PROJECT_PROGRESS, MOCK_INTERVIEW_HISTORY |
| Day 23 | Resume bullet generation | 3-5 evidence-backed bullets | RESUME_STATE |
| Day 24 | public portfolio README review/improvement | README checklist + next fixes | PORTFOLIO_READINESS |
| Day 25 | SQL mock retest | timed SQL score | MOCK_INTERVIEW_HISTORY |
| Day 26 | Python mock retest | timed Python score | MOCK_INTERVIEW_HISTORY |
| Day 27 | System design mock retest | batch/DQ/warehouse score | MOCK_INTERVIEW_HISTORY |
| Day 28 | Mixed mock interview | overall readiness score | MOCK_INTERVIEW_HISTORY, ROADMAP_PROGRESS |
| Day 29 | Repair top 3 remaining weaknesses | repair evidence + retest plan | WEAKNESS_REGISTER, NEXT_STEPS |
| Day 30 | Final 30-day review + application readiness verdict | readiness verdict + next 30/60 days | CURRENT_STATE, ROADMAP_PROGRESS, NEXT_STEPS |


Daily rule:

```text
Each day must produce evidence.
If no evidence was produced, the task is not complete.
```


## 10. 30-Day Daily Session Prompt

Use this each day:

```text
You are my Data Engineering Sensei mentor.

Use my 30-day roadmap.
Today is Day <number>.
Start today's task.

Before starting, tell me:
1. today's goal
2. why it matters for Data Engineering interviews
3. what evidence we need
4. what score target we are aiming for
5. which progress files will be updated

Then run the session.
Ask one question/task at a time.
Score me strictly.
End with feedback, weakness updates, and next action.
```


## 11. 30-Day Weekly Review Prompt

```text
Review my 30-day roadmap progress for this week.

Tell me:
1. tasks completed
2. evidence produced
3. scores improved
4. weaknesses added
5. weaknesses repaired
6. blockers
7. whether I am on track
8. next week's priority
9. progress files to update

Be strict.
Do not count reading or file generation as skill mastery.
```


## 12. 30-Day Exit Criteria

Candidate passes the 30-day sprint only if:

```text
baseline scores are known
SQL score improved or >= 4
Python score improved or >= 3.5/4
at least one system design case scored
project pitch and architecture are scored
top weaknesses are recorded
resume/project bullets are improved
mock interview history exists
next roadmap is clear
```

Candidate is application-ready only if:

```text
SQL >= 4
Python >= 3.5
system design >= 3.5
project deep dive >= 4
resume/public portfolio >= 3.5
communication >= 3.5
no critical weakness open
```


## 13. 30-Day Roadmap Output Template

```text
# 30-Day Roadmap

Candidate:
Target role:
Available time:
Current readiness:
Main blocker:

## Week 1
...

## Week 2
...

## Week 3
...

## Week 4
...

## Score Targets
...

## Evidence Targets
...

## Mock Interview Schedule
...

## Project Milestones
...

## Resume/public portfolio Milestones
...

## Final Readiness Gate
...
```


## 14. 30-Day Progress Update

After roadmap work, update or recommend updates to:

```text
progress/CURRENT_STATE.md:
active phase, current focus, latest completed task, next action

progress/ROADMAP_PROGRESS.md:
phase/module status, score, evidence, completion %

progress/NEXT_STEPS.md:
today/this week tasks and repair actions

progress/WEAKNESS_REGISTER.md:
weaknesses discovered, severity, repair plan, retest method

progress/SESSION_LOG.md:
session entry with completed roadmap work

progress/PROJECT_PROGRESS.md:
project milestones and evidence

progress/MOCK_INTERVIEW_HISTORY.md:
if roadmap task included a mock

progress/RESUME_STATE.md:
if resume evidence or bullets changed

progress/PORTFOLIO_READINESS.md:
if public portfolio/README/portfolio changed

progress/JOB_SEARCH_READINESS.md:
if applications/referrals/interviews started
```

Roadmap output must end with:

```text
Files to update:
- ...

Next 3 actions:
1.
2.
3.
```


## 15. Final 30-Day Rule

```text
A 30-day roadmap is for focused improvement, not magic.
If baseline is weak, the goal is selective readiness and clear repair path, not fake confidence.
```
