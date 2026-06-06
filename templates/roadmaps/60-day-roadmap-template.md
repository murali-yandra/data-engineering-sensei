# 60-Day Roadmap Template

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
data-engineering-sensei/templates/roadmaps/60-day-roadmap-template.md
```

Purpose:

```text
Create a realistic 60-day roadmap for Data Engineering interview readiness.
This is better than the 30-day roadmap when the candidate needs both fundamentals and portfolio improvement.
```


## 1. 60-Day Roadmap Mentor Prompt

```text
You are my Data Engineering Sensei roadmap mentor.

Create a strict 60-day roadmap.

Use my context:
I am targeting Data Engineering roles with around 2 years of experience.
I need SQL, Python, DSA patterns, DE fundamentals, system design, project deep dive, resume/public portfolio, and mock interview readiness.
My main project is Primary Portfolio Data Project.

Rules:
1. Start with baseline if missing.
2. Divide the plan into 8 weeks.
3. Include weekly score targets.
4. Include practice, mocks, project work, and resume/public portfolio work.
5. Include weakness repair weeks.
6. Include retests.
7. Include application readiness gate at the end.
8. Be realistic and strict.
```


## 2. 60-Day Scoring And Gates

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


## 3. 60-Day Roadmap Principles

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


## 4. 60-Day Roadmap Overview

The 60-day roadmap is divided into 8 weeks:

```text
Week 1:
Baseline + setup + priority map

Week 2:
SQL foundation

Week 3:
Python data scripting + DSA basics

Week 4:
Data Engineering fundamentals

Week 5:
Data modeling + warehouse + reporting

Week 6:
Pipeline system design

Week 7:
Project deep dive + resume/public portfolio

Week 8:
Mock interview loop + application readiness
```

Expected result:

```text
Candidate should be much closer to real interview readiness than in a 30-day sprint.
Selective applications can start if score gates are met.
```


## 5. Week 1: Baseline And Plan

- Run intake and skill-level assessment.
- Record scores in progress/CANDIDATE_PROFILE.md.
- Create active weaknesses in progress/WEAKNESS_REGISTER.md.
- Set roadmap module statuses.
- Create NEXT_STEPS for Week 2.
- Run a short SQL baseline and Python baseline.
- Output: baseline score table, top 5 weaknesses, 60-day task plan.

Weekly evidence required:

```text
At least one score, one weakness update, one session log, and one next-step update.
```


## 6. Week 2: SQL Foundation

- Joins and aggregations.
- CTEs and subqueries.
- Window functions.
- Deduplication.
- Business SQL cases.
- Query optimization basics.
- End-week SQL mock.
- Output: 25 SQL problems, 1 SQL mock score, repair tasks.

Weekly evidence required:

```text
At least one score, one weakness update, one session log, and one next-step update.
```


## 7. Week 3: Python Data Scripting And DSA Basics

- Python functions, dict/list/set.
- CSV and JSON processing.
- API pagination.
- Error handling and logging.
- Pandas basics.
- DSA hashmap, two pointers, sliding window.
- End-week Python mock.
- Output: 3 scripts, 10 DSA problems, Python score.

Weekly evidence required:

```text
At least one score, one weakness update, one session log, and one next-step update.
```


## 8. Week 4: Data Engineering Fundamentals

- ETL vs ELT.
- Batch vs streaming.
- Warehouse vs lake vs lakehouse.
- Partitioning, file formats, storage layout.
- Idempotency, backfills, schema evolution.
- Orchestration and Airflow DAGs.
- Data quality and monitoring.
- Output: 10 scored concept explanations, fundamentals mock.

Weekly evidence required:

```text
At least one score, one weakness update, one session log, and one next-step update.
```


## 9. Week 5: Data Modeling, Warehouse, Reporting

- Facts and dimensions.
- Table grain.
- SCD Type 1 and Type 2.
- Late-arriving facts/dimensions.
- Data warehouse design.
- Reporting pipeline design.
- Metric definitions and semantic layer.
- Output: warehouse design mock + reporting pipeline mock.

Weekly evidence required:

```text
At least one score, one weakness update, one session log, and one next-step update.
```


## 10. Week 6: Pipeline System Design

- Batch pipeline design.
- CDC pipeline design.
- Data lake design.
- Data quality framework.
- Event ingestion basics.
- Realtime pipeline basics.
- Monitoring, security, cost, trade-offs.
- Output: 3 system design mocks, active repair plan.

Weekly evidence required:

```text
At least one score, one weakness update, one session log, and one next-step update.
```


## 11. Week 7: Project Deep Dive And Portfolio

- Primary Portfolio Data Project 2-minute pitch.
- Architecture explanation.
- Database schema explanation.
- Transaction ingestion flow.
- Merchant normalization/categorization/feedback loop.
- Security/authentication explanation.
- Testing/deployment explanation.
- README and resume bullet improvement.
- Output: project score, public portfolio/README plan, 3-5 resume bullets.

Weekly evidence required:

```text
At least one score, one weakness update, one session log, and one next-step update.
```


## 12. Week 8: Mock Interviews And Application Readiness

- SQL mock retest.
- Python mock retest.
- System design mock retest.
- Project deep-dive mock.
- Behavioral mock.
- Resume/public portfolio final review.
- Application readiness verdict.
- Output: readiness gate decision, next 30 days, application strategy.

Weekly evidence required:

```text
At least one score, one weakness update, one session log, and one next-step update.
```


## 13. 60-Day Weekly Score Targets

| Week | SQL | Python | DSA | DE Fundamentals | System Design | Project | Resume/public portfolio |
|---|---:|---:|---:|---:|---:|---:|---:|
| Week 1 | baseline | baseline | baseline | baseline | baseline | baseline | baseline |
| Week 2 | 3.5 | 0 | 0 | 0 | 0 | 0 | 0 |
| Week 3 | 3.5 | 3.5 | 2.5 | 0 | 0 | 0 | 0 |
| Week 4 | 3.5 | 3.5 | 2.5 | 3.5 | 0 | 0 | 0 |
| Week 5 | 4 | 3.5 | 3 | 3.5 | 3.5 | 0 | 0 |
| Week 6 | 4 | 3.5 | 3 | 4 | 3.5 | 0 | 0 |
| Week 7 | 4 | 3.5 | 3 | 4 | 3.5 | 3.5 | 3 |
| Week 8 | 4 | 4 | 3.5 | 4 | 4 | 4 | 4 |

Note:

```text
These are targets, not fake scores.
Only update scores with evidence.
```


## 14. 60-Day Mock Schedule

```text
Week 1:
baseline mini mocks

Week 2:
SQL mock

Week 3:
Python mock

Week 4:
DE fundamentals mock

Week 5:
data warehouse/reporting mock

Week 6:
pipeline system design mock

Week 7:
project deep-dive mock

Week 8:
full mixed mock + retests
```


## 15. 60-Day Roadmap Prompt For Daily Execution

```text
Use my 60-day roadmap.
Tell me today's task, expected evidence, and scoring target.
Run the task.
Score me.
Update weaknesses and next steps.
Do not move to the next topic until today's evidence exists.
```


## 16. 60-Day Exit Criteria

Candidate passes the 60-day roadmap if:

```text
SQL >= 4
Python >= 4 or at least 3.5 with clear repair path
DSA >= 3.5
DE fundamentals >= 4
System design >= 4 in core cases
Project deep dive >= 4
Resume/public portfolio >= 4
Communication >= 3.5
No critical weakness open
```

If not passed:

```text
Create 30-day weakness repair roadmap.
```


## 17. 60-Day Progress Update

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


## 18. Final 60-Day Rule

```text
The 60-day roadmap should produce measurable readiness, not just learning notes.
If mock scores are not improving, switch from content learning to weakness repair.
```
