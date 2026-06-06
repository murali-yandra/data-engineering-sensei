# Personalized Roadmap Template

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
data-engineering-sensei/templates/roadmaps/personalized-roadmap-template.md
```

Purpose:

```text
Create a personalized Data Engineering roadmap based on candidate baseline, target role, available time, weaknesses, project status, and job timeline.
```


## 1. Personalized Roadmap Mentor Prompt

```text
You are my Data Engineering Sensei roadmap strategist.

Create a personalized roadmap for me.

Rules:
1. Ask for missing baseline details one at a time.
2. Use my actual scores and evidence.
3. Do not use a generic roadmap.
4. Prioritize highest ROI for my target role.
5. Include weekly and daily tasks.
6. Include score targets.
7. Include project, resume, GitHub, and mock interviews.
8. Include weakness repair and retests.
9. Be realistic about job-readiness.
10. Tell me if my goal timeline is unrealistic.

Candidate context:
I am an early-career Data Engineering candidate with around 2 years of experience.
I want better jobs, possibly India first, remote/international later.
Main project: Personal Finance Tracking Platform.
I need structured preparation in SQL, Python, DSA, DE fundamentals, system design, project deep dive, resume/GitHub/LinkedIn, and job applications.
```


## 2. Personalization Inputs

Collect these before creating roadmap:

```yaml
target_role:
target_companies:
target_location:
timeline_days:
hours_per_day:
days_per_week:
sql_score:
python_score:
dsa_score:
de_fundamentals_score:
system_design_score:
project_score:
resume_score:
github_score:
communication_score:
main_project_status:
top_weaknesses:
current_blockers:
interview_date_if_any:
job_search_status:
```

If unknown:

```text
Run intake and baseline assessment first.
```


## 3. Personalized Roadmap Decision Tree

```text
If baseline missing:
start with 3-day baseline sprint.

If SQL < 3:
make SQL the first priority.

If Python < 3:
make Python scripting second priority.

If project score < 3:
start project deep dive early.

If system design < 3:
start batch pipeline and DQ fundamentals before advanced streaming.

If resume/GitHub < 3:
do not apply aggressively.

If interview is within 2 weeks:
focus on mocks and high-probability topics.

If timeline is 30 days:
use compressed roadmap and selective readiness goal.

If timeline is 60 days:
use balanced roadmap.

If timeline is 90 days:
use deep roadmap with portfolio and job search.

If critical weakness exists:
create weakness-repair plan before broad new learning.
```


## 4. Personalized Roadmap Output Format

```text
# Personalized Data Engineering Roadmap

## Candidate Snapshot
Target role:
Timeline:
Available time:
Current readiness:
Main project:
Main blocker:

## Baseline Scores
...

## Role Fit
...

## Priority Order
...

## Roadmap Phases
...

## Week-by-Week Plan
...

## Daily Task Pattern
...

## Mock Interview Schedule
...

## Project Milestones
...

## Resume/GitHub Milestones
...

## Weakness Repair Plan
...

## Application Strategy
...

## Readiness Gates
...

## Progress Files To Update
...
```


## 5. Role-Based Priority Maps

### Data Engineer

```text
Priority:
SQL → Python → ETL/ELT → data modeling → orchestration → warehouse/lake → system design → project proof
```

### Analytics Engineer

```text
Priority:
SQL → data modeling → warehouse → reporting marts → metrics/semantic layer → DQ → business communication
```

### ETL Developer

```text
Priority:
SQL → stored procedures/scripts → batch pipelines → DML/deployments → error handling → reconciliation
```

### Cloud Data Engineer

```text
Priority:
SQL/Python → cloud warehouse/storage → orchestration → Spark/PySpark → security/cost → system design
```

### Data Platform Engineer

```text
Priority:
system design → distributed processing → streaming → observability → infrastructure → security → cost
```


## 6. Personalization Case: If candidate has 1 hour/day

- Do one focused task per day.
- Alternate SQL and Python.
- One system design per week.
- One project/resume task per week.
- Mocks every weekend.

Mentor instruction:

```text
Adjust roadmap based on this condition.
Remove low-priority tasks if time is limited.
```


## 7. Personalization Case: If candidate has 2 hours/day

- One skill drill + one review daily.
- SQL/Python 4 days/week.
- System design 2 days/week.
- Project/resume 1 day/week.
- Weekly mock and repair.

Mentor instruction:

```text
Adjust roadmap based on this condition.
Remove low-priority tasks if time is limited.
```


## 8. Personalization Case: If candidate has 3+ hours/day

- Daily skill block.
- Daily project/portfolio block.
- Daily review/weakness repair.
- 2 mocks/week.
- Applications after readiness gate.

Mentor instruction:

```text
Adjust roadmap based on this condition.
Remove low-priority tasks if time is limited.
```


## 9. Personalization Case: If target is remote/international

- Stronger GitHub proof required.
- Project README must be excellent.
- Resume needs measurable impact.
- Communication must be strong.
- Referral/networking strategy required.
- Do not rely only on applications.

Mentor instruction:

```text
Adjust roadmap based on this condition.
Remove low-priority tasks if time is limited.
```


## 10. Personalization Case: If target is urgent interview

- Stop broad learning.
- Mock interview first.
- Repair highest-probability failures.
- Prepare project pitch.
- Prepare SQL/Python common patterns.
- Prepare system design framework.

Mentor instruction:

```text
Adjust roadmap based on this condition.
Remove low-priority tasks if time is limited.
```


## 11. Personalized Weekly Plan Template

```text
Week:
Main goal:
Skill priority:
Project priority:
Mock:
Resume/GitHub task:
Weakness repair:
Evidence target:
Score target:
Files to update:
```

Example:

```text
Week:
Week 1

Main goal:
Establish baseline and repair SQL basics.

Skill priority:
SQL joins, windows, dedupe.

Project priority:
2-minute finance tracker pitch.

Mock:
SQL mini mock.

Resume/GitHub task:
Collect project evidence.

Weakness repair:
table grain and window functions.

Evidence target:
10 SQL problems + project pitch score.

Score target:
SQL 3.5/5.
```


## 12. Personalized Daily Plan Template

```text
Date:
Available time:
Energy level:
Priority:
Task:
Why:
Input file:
Evidence output:
Score target:
Done condition:
Progress file update:
```

Daily rule:

```text
If time is short, do one measurable task.
Do not start multiple vague tasks.
```


## 13. Personalized Roadmap Scoring

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
Resume/GitHub readiness: 4/5
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
scores >= 4 across core areas, project/resume/GitHub are defensible, and no critical weaknesses are open
```


## 14. Personalized Roadmap Prompt After Baseline

```text
Using my baseline scores, create my personalized roadmap.

My scores:
SQL:
Python:
DSA:
DE fundamentals:
System design:
Project deep dive:
Resume/GitHub:
Communication:

My target role:
...

My available time:
...

My deadline:
...

My main project:
Personal Finance Tracking Platform

Create:
1. priority order
2. 7-day plan
3. 30-day plan
4. mock schedule
5. project milestones
6. resume/GitHub tasks
7. readiness gates
8. files to update

Be strict.
```


## 15. Personalized Roadmap Progress Update

After roadmap work, update or recommend updates to:

```text
CURRENT_STATE.md:
active phase, current focus, latest completed task, next action

ROADMAP_PROGRESS.md:
phase/module status, score, evidence, completion %

NEXT_STEPS.md:
today/this week tasks and repair actions

WEAKNESS_REGISTER.md:
weaknesses discovered, severity, repair plan, retest method

SESSION_LOG.md:
session entry with completed roadmap work

PROJECT_PROGRESS.md:
project milestones and evidence

MOCK_INTERVIEW_HISTORY.md:
if roadmap task included a mock

RESUME_STATE.md:
if resume evidence or bullets changed

GITHUB_PORTFOLIO_STATE.md:
if GitHub/README/portfolio changed

JOB_SEARCH_STATE.md:
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


## 16. Final Personalized Roadmap Rule

```text
The best roadmap is the one that attacks the candidate's real blockers.
If it does not use baseline scores and project evidence, it is not personalized.
```
