# Roadmap Progress

Generated: 2026-06-06

Path:

```text
data-engineering-sensei/practice/progress/ROADMAP_PROGRESS.md
```

This file tracks the candidate's **Data Engineering Sensei roadmap progress**.

It is used to know:

```text
which roadmap phase is active
which modules are completed
which modules are not started
which modules are blocked
which modules need retest
which scores were achieved
which files were used
which evidence proves progress
which next milestone should be completed
```

This file is not the same as `CURRENT_STATE.md`.

```text
CURRENT_STATE.md = current live snapshot.
ROADMAP_PROGRESS.md = long-term roadmap and module completion tracker.
```

Current status:

```text
Initial ROADMAP_PROGRESS.md generated.
Roadmap progress is not yet baselined.
Most modules are marked not_started until assessment/practice evidence is added.
```

Important rule:

```text
Do not mark a module complete only because a guide file was generated.
Mark a module complete only when the candidate has practiced, scored, and shown evidence.
```


## 1. Purpose Of This File

`ROADMAP_PROGRESS.md` is the long-term progress tracker for the Data Engineering Sensei skill.

It should track progress across:

```text
repo setup
profile assessment
SQL
Python
DSA
data engineering fundamentals
data modeling
ETL/ELT
orchestration
Spark/PySpark
cloud data platforms
data warehouse
data lake
CDC
data quality
event ingestion
realtime pipelines
reporting pipelines
project deep dives
mock interviews
resume/GitHub/LinkedIn
job application readiness
```

The AI mentor should use this file to decide:

```text
what has already been completed
what must be practiced next
what should not be repeated
what has weak score evidence
what is blocked
what phase should be unlocked next
```

Strict rule:

```text
A generated learning file is only preparation material.
A completed roadmap milestone requires candidate performance evidence.
```


## 2. Relationship With Other Progress Files

Use this file with other progress files.

| File | Responsibility |
|---|---|
| `practice/progress/CANDIDATE_PROFILE.md` | long-term candidate profile, goals, strengths, risks, target roles |
| `practice/progress/CURRENT_STATE.md` | live active snapshot and next session state |
| `practice/progress/ROADMAP_PROGRESS.md` | roadmap phases, module completion, milestones, gates |
| `practice/progress/NEXT_STEPS.md` | immediate task queue |
| `practice/progress/SESSION_LOG.md` | detailed chronological session history |
| `practice/progress/WEAKNESS_REGISTER.md` | weaknesses and repair evidence |
| `practice/progress/MOCK_INTERVIEW_HISTORY.md` | mock interview scores and feedback |
| `practice/progress/PROJECT_PROGRESS.md` | project milestones and evidence |
| `practice/progress/RESUME_STATE.md` | resume bullets and readiness |
| `practice/progress/GITHUB_PORTFOLIO_STATE.md` | GitHub and portfolio readiness |
| `practice/progress/JOB_SEARCH_STATE.md` | applications, referrals, interview pipeline |

Roadmap update rule:

```text
When ROADMAP_PROGRESS.md changes:
1. update CURRENT_STATE.md summary
2. update NEXT_STEPS.md if next tasks change
3. update WEAKNESS_REGISTER.md if a roadmap block is caused by weakness
4. update MOCK_INTERVIEW_HISTORY.md if score came from mock
5. update CANDIDATE_PROFILE.md if long-term score/readiness changed
```


## 3. Roadmap Status Values

Use only these status values.

```text
not_started:
candidate has not started the topic

in_progress:
candidate has started but has not passed the exit criteria

blocked:
candidate cannot progress because prerequisite or weakness is blocking

needs_retest:
candidate practiced but needs a retest before completion

completed:
candidate passed exit criteria with evidence

skipped:
topic intentionally skipped with reason

archived:
old module replaced by better module or no longer relevant
```

Completion rule:

```text
completed = score evidence + practice evidence + mentor approval
```

Do not use vague status labels like:

```text
done
okay
good
almost
learned
reviewed
```


## 4. Score Scale

Use the same 0 to 5 score scale everywhere.

```text
0 = not assessed
1 = beginner
2 = basic
3 = usable with support
4 = interview-ready
5 = strong / can teach
```

Roadmap completion scoring:

```text
0-2.9:
not complete

3.0-3.4:
basic progress, needs more practice

3.5-3.9:
usable but not fully strong

4.0-4.4:
interview-ready for target level

4.5-5.0:
strong, can handle follow-ups
```

Default pass mark:

```text
4/5 for interview readiness modules
3.5/5 for early baseline unlocks
```

Strict rule:

```text
If the candidate cannot explain the topic aloud under interview pressure, the module is not complete.
```


## 5. Current Roadmap Overview

Current roadmap phase:

```text
Phase 0:
Repo and skill structure generation.
```

Roadmap overview:

| Phase | Name | Status | Completion % | Exit Criteria |
|---|---|---|---:|---|
| Phase 0 | Setup and skill repository | in_progress | 80 | core files and progress files generated |
| Phase 1 | Profile baseline assessment | not_started | 0 | baseline scores recorded |
| Phase 2 | SQL + Python + DSA foundation | not_started | 0 | core drills passed |
| Phase 3 | Data engineering fundamentals | not_started | 0 | fundamentals mock passed |
| Phase 4 | Data modeling + warehouse/lake | not_started | 0 | modeling and warehouse cases passed |
| Phase 5 | Pipeline system design | not_started | 0 | batch/CDC/DQ/reporting cases passed |
| Phase 6 | Project deep dive | not_started | 0 | main project explained at 4/5 |
| Phase 7 | Mock interview loop | not_started | 0 | repeated passing mock scores |
| Phase 8 | Resume/GitHub/LinkedIn polish | not_started | 0 | career assets ready |
| Phase 9 | Job search execution | not_started | 0 | applications/referrals tracked |

Prompt to update:

```text
When a phase changes, update:
1. status
2. completion %
3. exit criteria status
4. evidence
5. next milestone
```


## 6. Phase 0: Setup And Skill Repository

Purpose:

```text
Build the Data Engineering Sensei skill repository and learning structure.
```

Status:

```text
in_progress
```

Generated core files:

```text
SKILL.md
README.md
CONTRIBUTING.md
CHANGELOG.md
```

Generated docs files:

```text
docs/assessment-rubric.md
docs/cloud-data-platforms-guide.md
docs/communication-rubric.md
docs/data-engineering-fundamentals.md
docs/data-engineering-interview-roadmap.md
docs/data-modeling-guide.md
docs/data-warehouse-guide.md
docs/dsa-for-data-engineers.md
docs/error-handling-playbook.md
docs/etl-elt-pipelines-guide.md
docs/faang-interview-standards.md
docs/leetcode-practice-map.md
docs/orchestration-airflow-guide.md
docs/python-interview-guide.md
docs/spark-pyspark-guide.md
docs/sql-interview-guide.md
docs/system-design-guide.md
```

Generated mode files:

```text
modes/data-engineering-fundamentals-mode.md
modes/dsa-drill-mode.md
modes/feedback-mode.md
modes/hint-mode.md
modes/interview-mode.md
modes/pattern-mapper-mode.md
modes/profile-assessment-mode.md
modes/project-deep-dive-mode.md
modes/python-drill-mode.md
modes/review-mode.md
modes/roadmap-mode.md
modes/sql-drill-mode.md
modes/system-design-mode.md
modes/tutor-mode.md
modes/weakness-repair-mode.md
```

Generated practice files:

```text
practice/dsa/arrays-strings.md
practice/dsa/bfs-dfs-basics.md
practice/dsa/hashmaps.md
practice/dsa/heap-top-k.md
practice/dsa/intervals.md
practice/dsa/sorting-binary-search.md
practice/dsa/stack-queue.md
practice/dsa/two-pointers-sliding-window.md

practice/python/api-processing.md
practice/python/data-scripting.md
practice/python/files-json-csv.md
practice/python/fundamentals.md
practice/python/pandas-basics.md
practice/python/testing-logging-errors.md

practice/sql/business-sql-cases.md
practice/sql/ctes-subqueries.md
practice/sql/deduplication.md
practice/sql/gaps-and-islands.md
practice/sql/joins.md
practice/sql/query-optimization.md
practice/sql/window-functions.md

practice/system-design/batch-pipeline.md
practice/system-design/cdc-pipeline.md
practice/system-design/data-lake.md
practice/system-design/data-quality-framework.md
practice/system-design/data-warehouse.md
practice/system-design/event-ingestion.md
practice/system-design/realtime-pipeline.md
practice/system-design/reporting-pipeline.md
```

Generated progress files:

```text
practice/progress/CANDIDATE_PROFILE.md
practice/progress/CURRENT_STATE.md
practice/progress/ROADMAP_PROGRESS.md
```

Known path correction:

```text
practice/python/api-processing.md is the correct path.
Do not keep api-processing.md under practice/dsa.
```

Remaining recommended progress files:

```text
practice/progress/NEXT_STEPS.md
practice/progress/SESSION_LOG.md
practice/progress/WEAKNESS_REGISTER.md
practice/progress/MOCK_INTERVIEW_HISTORY.md
practice/progress/PROJECT_PROGRESS.md
practice/progress/RESUME_STATE.md
practice/progress/GITHUB_PORTFOLIO_STATE.md
practice/progress/JOB_SEARCH_STATE.md
```

Exit criteria:

```text
core repo files generated
main docs generated
practice modules generated
progress tracking files generated
candidate ready to begin baseline assessment
```

Current exit status:

```text
not complete
```


## 7. Phase 1: Profile Baseline Assessment

Purpose:

```text
Assess the candidate's current level before starting structured practice.
```

Status:

```text
not_started
```

Assessment files/modes:

```text
modes/profile-assessment-mode.md
docs/assessment-rubric.md
docs/communication-rubric.md
practice/progress/CANDIDATE_PROFILE.md
practice/progress/CURRENT_STATE.md
```

Baseline areas:

| Area | Status | Score | Evidence |
|---|---|---:|---|
| SQL | not_started | 0 | none |
| Python | not_started | 0 | none |
| DSA | not_started | 0 | none |
| DE fundamentals | not_started | 0 | none |
| Data modeling | not_started | 0 | none |
| System design | not_started | 0 | none |
| Project deep dive | not_started | 0 | none |
| Communication | not_started | 0 | none |
| Resume/GitHub | not_started | 0 | none |

Exit criteria:

```text
baseline scores recorded
top 5 weaknesses identified
current target role confirmed
first 30-day plan created
NEXT_STEPS.md updated
WEAKNESS_REGISTER.md initialized
```

Recommended prompt:

```text
Run my Data Engineering Sensei profile baseline assessment.
Ask me one question at a time.
Assess SQL, Python, DSA, DE fundamentals, system design, project explanation, resume, and communication.
Score each area from 0 to 5.
Update ROADMAP_PROGRESS.md, CURRENT_STATE.md, and WEAKNESS_REGISTER.md.
```


## 8. Phase 2: SQL Foundation And Interview Readiness

Purpose:

```text
Make SQL interview-ready for Data Engineering roles.
```

Status:

```text
not_started
```

Required modules:

| Module | File | Status | Score | Evidence |
|---|---|---|---:|---|
| Joins | `practice/sql/joins.md` | not_started | 0 | none |
| CTEs and subqueries | `practice/sql/ctes-subqueries.md` | not_started | 0 | none |
| Window functions | `practice/sql/window-functions.md` | not_started | 0 | none |
| Deduplication | `practice/sql/deduplication.md` | not_started | 0 | none |
| Gaps and islands | `practice/sql/gaps-and-islands.md` | not_started | 0 | none |
| Query optimization | `practice/sql/query-optimization.md` | not_started | 0 | none |
| Business SQL cases | `practice/sql/business-sql-cases.md` | not_started | 0 | none |

Completion evidence required:

```text
at least 25 SQL problems completed
at least 5 business SQL cases completed
one timed SQL mock completed
score >= 4/5 in SQL mock
candidate can explain grain and joins clearly
candidate avoids DISTINCT as a band-aid
candidate can explain window functions
```

Exit criteria:

```text
SQL score >= 4/5
no critical SQL weakness open
candidate can solve medium SQL interview problem in 20-30 minutes
```

Recommended first drill:

```text
Start with joins + aggregation baseline.
Then move to window functions and deduplication.
```


## 9. Phase 3: Python Foundation And Data Scripting

Purpose:

```text
Make Python strong enough for data engineering scripts and interviews.
```

Status:

```text
not_started
```

Required modules:

| Module | File | Status | Score | Evidence |
|---|---|---|---:|---|
| Fundamentals | `practice/python/fundamentals.md` | not_started | 0 | none |
| Data scripting | `practice/python/data-scripting.md` | not_started | 0 | none |
| Files JSON CSV | `practice/python/files-json-csv.md` | not_started | 0 | none |
| API processing | `practice/python/api-processing.md` | not_started | 0 | none |
| Pandas basics | `practice/python/pandas-basics.md` | not_started | 0 | none |
| Testing logging errors | `practice/python/testing-logging-errors.md` | not_started | 0 | none |

Completion evidence required:

```text
at least 10 Python drills completed
at least 3 file/API processing scripts completed
one timed Python mock completed
score >= 4/5 in Python scripting mock
candidate uses clean functions
candidate handles errors and edge cases
candidate explains complexity when relevant
```

Exit criteria:

```text
Python score >= 4/5
candidate can write data processing script with CSV/JSON/API input
candidate can explain code clearly
```

Recommended first drill:

```text
Start with CSV/JSON file processing, then API pagination and error handling.
```


## 10. Phase 4: DSA For Data Engineers

Purpose:

```text
Learn practical DSA patterns needed for Data Engineering interviews.
```

Status:

```text
not_started
```

Required modules:

| Module | File | Status | Score | Evidence |
|---|---|---|---:|---|
| Arrays and strings | `practice/dsa/arrays-strings.md` | not_started | 0 | none |
| Hashmaps | `practice/dsa/hashmaps.md` | not_started | 0 | none |
| Two pointers/sliding window | `practice/dsa/two-pointers-sliding-window.md` | not_started | 0 | none |
| Stack and queue | `practice/dsa/stack-queue.md` | not_started | 0 | none |
| Sorting and binary search | `practice/dsa/sorting-binary-search.md` | not_started | 0 | none |
| Intervals | `practice/dsa/intervals.md` | not_started | 0 | none |
| Heap/top K | `practice/dsa/heap-top-k.md` | not_started | 0 | none |
| BFS/DFS basics | `practice/dsa/bfs-dfs-basics.md` | not_started | 0 | none |

Completion evidence required:

```text
at least 30 DSA problems completed
candidate can identify pattern within 2-3 minutes
candidate can solve common easy/medium problems
candidate can explain brute force and optimized approach
```

Exit criteria:

```text
DSA score >= 3.5/5 for Data Engineering role target
no critical hashmap/sliding-window weakness open
```

Important rule:

```text
Do not over-prioritize advanced DSA before SQL, Python, project depth, and DE system design.
```


## 11. Phase 5: Data Engineering Fundamentals

Purpose:

```text
Build strong explanations for core Data Engineering concepts.
```

Status:

```text
not_started
```

Required modules:

| Module | File | Status | Score | Evidence |
|---|---|---|---:|---|
| DE fundamentals | `docs/data-engineering-fundamentals.md` | not_started | 0 | none |
| ETL/ELT | `docs/etl-elt-pipelines-guide.md` | not_started | 0 | none |
| Data warehouse basics | `docs/data-warehouse-guide.md` | not_started | 0 | none |
| Data modeling | `docs/data-modeling-guide.md` | not_started | 0 | none |
| Orchestration | `docs/orchestration-airflow-guide.md` | not_started | 0 | none |
| Cloud platforms | `docs/cloud-data-platforms-guide.md` | not_started | 0 | none |
| Spark/PySpark | `docs/spark-pyspark-guide.md` | not_started | 0 | none |
| Error handling | `docs/error-handling-playbook.md` | not_started | 0 | none |

Completion evidence required:

```text
candidate can answer common DE fundamentals in 60-120 seconds
candidate can give practical examples
candidate can explain trade-offs
candidate can connect fundamentals to project work
```

Exit criteria:

```text
DE fundamentals mock score >= 4/5
candidate can explain batch vs streaming, ETL vs ELT, warehouse vs lake, orchestration, DQ, partitioning, idempotency, and backfills
```


## 12. Phase 6: Data Modeling And Warehouse Readiness

Purpose:

```text
Make candidate strong in dimensional modeling, warehouses, reporting marts, and analytical design.
```

Status:

```text
not_started
```

Required modules:

| Module | File | Status | Score | Evidence |
|---|---|---|---:|---|
| Data modeling guide | `docs/data-modeling-guide.md` | not_started | 0 | none |
| Data warehouse guide | `docs/data-warehouse-guide.md` | not_started | 0 | none |
| Data warehouse system design | `practice/system-design/data-warehouse.md` | not_started | 0 | none |
| Reporting pipeline | `practice/system-design/reporting-pipeline.md` | not_started | 0 | none |
| SQL business cases | `practice/sql/business-sql-cases.md` | not_started | 0 | none |

Must master:

```text
table grain
facts
dimensions
star schema
snowflake schema
SCD Type 1
SCD Type 2
late-arriving facts
late-arriving dimensions
reporting marts
semantic layer
metric definitions
source-to-report reconciliation
```

Exit criteria:

```text
data warehouse design case score >= 4/5
candidate defines grain before tables
candidate avoids fact-to-fact join explosion
candidate handles SCD and late data
```


## 13. Phase 7: Pipeline System Design

Purpose:

```text
Prepare for Data Engineering system design interviews.
```

Status:

```text
not_started
```

Required system design cases:

| Case | File | Status | Score | Evidence |
|---|---|---|---:|---|
| Batch pipeline | `practice/system-design/batch-pipeline.md` | not_started | 0 | none |
| CDC pipeline | `practice/system-design/cdc-pipeline.md` | not_started | 0 | none |
| Data lake | `practice/system-design/data-lake.md` | not_started | 0 | none |
| Data quality framework | `practice/system-design/data-quality-framework.md` | not_started | 0 | none |
| Data warehouse | `practice/system-design/data-warehouse.md` | not_started | 0 | none |
| Event ingestion | `practice/system-design/event-ingestion.md` | not_started | 0 | none |
| Realtime pipeline | `practice/system-design/realtime-pipeline.md` | not_started | 0 | none |
| Reporting pipeline | `practice/system-design/reporting-pipeline.md` | not_started | 0 | none |

Completion evidence required:

```text
at least 5 full system design mocks completed
at least 3 cases scored >= 4/5
batch pipeline scored >= 4/5
data warehouse scored >= 4/5
data quality framework scored >= 4/5
candidate uses requirements-first framework
candidate explains trade-offs and failure handling
```

Exit criteria:

```text
system design average >= 4/5 across core cases
no critical missing patterns:
- idempotency
- backfills
- data quality
- monitoring
- security
- cost
- late data
```


## 14. Phase 8: Project Deep Dive

Purpose:

```text
Make the candidate's main project interview-ready.
```

Status:

```text
not_started
```

Main project:

```text
Personal Finance Tracking Platform
```

Known stack:

```text
FastAPI
PostgreSQL
SQLModel
Alembic
Docker
GitHub Actions
Ollama
Telegram Bot API
```

Known features:

```text
SMS transaction ingestion
automated expense tracking
merchant normalization
merchant learning engine
transaction categorization
account and balance reconciliation
Telegram bot notifications and corrections
AI-assisted categorization
feedback learning engine
```

Project modules to assess:

| Area | Status | Score | Evidence |
|---|---|---:|---|
| One-line explanation | not_started | 0 | none |
| Business problem | not_started | 0 | none |
| Architecture | not_started | 0 | none |
| Database design | not_started | 0 | none |
| API design | not_started | 0 | none |
| Data pipeline flow | not_started | 0 | none |
| Data quality/reconciliation | not_started | 0 | none |
| Security/authentication | not_started | 0 | none |
| Deployment/CI/CD | not_started | 0 | none |
| Testing | not_started | 0 | none |
| Failure handling | not_started | 0 | none |
| Scaling/trade-offs | not_started | 0 | none |
| Resume story | not_started | 0 | none |

Exit criteria:

```text
project deep dive score >= 4/5
candidate can explain project in 2 minutes, 5 minutes, and 20 minutes
candidate has architecture diagram or clear architecture explanation
candidate can defend design choices
candidate can connect project to target Data Engineer role
```


## 15. Phase 9: Mock Interview Loop

Purpose:

```text
Convert learning into interview performance.
```

Status:

```text
not_started
```

Mock interview types:

| Mock Type | Status | Latest Score | Required Pass Score |
|---|---|---:|---:|
| SQL mock | not_started | 0 | 4 |
| Python mock | not_started | 0 | 4 |
| DSA mock | not_started | 0 | 3.5 |
| DE fundamentals mock | not_started | 0 | 4 |
| System design mock | not_started | 0 | 4 |
| Project deep dive mock | not_started | 0 | 4 |
| Behavioral mock | not_started | 0 | 3.5 |
| Resume screen mock | not_started | 0 | 4 |

Mock completion rule:

```text
A mock counts only if:
1. candidate answers under time pressure
2. mentor gives score
3. weaknesses are recorded
4. repair action is assigned
5. retest happens if score < pass mark
```

Exit criteria:

```text
3 consecutive passing mocks across SQL/Python/System Design/Project
no critical weakness open
candidate can handle follow-up questions
```


## 16. Phase 10: Career Asset Readiness

Purpose:

```text
Prepare resume, GitHub, LinkedIn, and portfolio for applications.
```

Status:

```text
not_started
```

Career asset tracker:

| Asset | Status | Score | Evidence |
|---|---|---:|---|
| Resume | not_started | 0 | none |
| GitHub profile README | in_progress | 0 | needs review |
| Main project README | not_started | 0 | none |
| Project architecture diagram | not_started | 0 | none |
| LinkedIn headline/about | in_progress | 0 | needs review |
| Portfolio proof | not_started | 0 | none |
| Resume bullets with metrics | not_started | 0 | none |

Exit criteria:

```text
resume score >= 4/5
GitHub portfolio score >= 4/5
LinkedIn score >= 3.5/5
main project has strong README
project can be demoed or explained clearly
```

Strict rule:

```text
Do not apply aggressively with vague project bullets and weak GitHub proof.
```


## 17. Phase 11: Job Search Execution

Purpose:

```text
Track active job applications, referrals, interviews, and outcomes.
```

Status:

```text
not_started
```

Start condition:

```text
Only start aggressive applications after job application readiness gate is passed.
```

Application readiness gate:

| Area | Required Score | Current Score | Status |
|---|---:|---:|---|
| SQL | 4 | 0 | not_ready |
| Python | 3.5 | 0 | not_ready |
| System design | 3.5 | 0 | not_ready |
| Project deep dive | 4 | 0 | not_ready |
| Resume | 4 | 0 | not_ready |
| GitHub | 3.5 | 0 | not_ready |
| Communication | 3.5 | 0 | not_ready |

Target roles:

```text
Data Engineer
Analytics Engineer
ETL Developer
Cloud Data Engineer
BI/Data Warehouse Engineer
```

Target strategy:

```text
India first
remote later
international after stronger proof
```

Exit criteria:

```text
applications tracked
referrals tracked
interview feedback recorded
weaknesses repaired after each rejection/mock
offer strategy prepared
```


## 18. Module Completion Template

Use this template when updating a module.

```text
Module:
File:
Started on:
Completed on:
Status:
Score:
Evidence:
Problems completed:
Mock completed:
Main weaknesses:
Repair actions:
Retest needed:
Next module:
Mentor approval:
```

Example:

```text
Module:
SQL window functions

File:
practice/sql/window-functions.md

Started on:
2026-06-10

Completed on:
2026-06-12

Status:
needs_retest

Score:
3.5/5

Evidence:
Solved 8 window problems, but struggled with running totals and ranking tie cases.

Main weaknesses:
frame clauses and tie handling

Repair actions:
practice 5 additional ranking and running total problems

Retest needed:
yes
```


## 19. Roadmap Update Prompt

Use this prompt after completing any roadmap work:

```text
Update ROADMAP_PROGRESS.md.

Completed:
<module/topic>

Evidence:
<problems solved / mock score / file generated / project milestone>

Score:
<0-5>

Status:
not_started / in_progress / blocked / needs_retest / completed

Weakness found:
<weakness if any>

Next module:
<next module>

Also tell me whether CURRENT_STATE.md, NEXT_STEPS.md, WEAKNESS_REGISTER.md, MOCK_INTERVIEW_HISTORY.md, or CANDIDATE_PROFILE.md should be updated.
```


## 20. Baseline Assessment Update Prompt

Use this prompt after baseline assessment:

```text
Update ROADMAP_PROGRESS.md after baseline assessment.

Scores:
SQL:
Python:
DSA:
DE fundamentals:
Data modeling:
System design:
Project deep dive:
Communication:
Resume/GitHub:

Top strengths:
1.
2.
3.

Top weaknesses:
1.
2.
3.
4.
5.

Recommended roadmap phase:
<phase>

Next 7 days:
<tasks>

Also update:
CURRENT_STATE.md
CANDIDATE_PROFILE.md
NEXT_STEPS.md
WEAKNESS_REGISTER.md
```


## 21. Mock Interview Roadmap Update Prompt

Use this after a mock interview:

```text
Update roadmap progress from mock interview.

Mock type:
SQL / Python / DSA / System Design / Project / Behavioral

Topic:
<topic>

Score:
<0-5>

Pass:
yes/no

Roadmap module affected:
<module>

Status update:
<not_started/in_progress/blocked/needs_retest/completed>

Evidence:
<summary>

Weakness:
<weakness>

Repair:
<repair drill>

Retest:
<date or condition>

Also update:
MOCK_INTERVIEW_HISTORY.md
WEAKNESS_REGISTER.md
CURRENT_STATE.md
NEXT_STEPS.md
```


## 22. Project Roadmap Update Prompt

Use this after project progress:

```text
Update ROADMAP_PROGRESS.md for project deep dive.

Project:
<project name>

Milestone:
<architecture/API/database/testing/deployment/resume bullet/demo>

Status:
<status>

Evidence:
<commit/file/link/explanation>

Interview score:
<0-5 if tested>

Resume value:
<possible bullet>

Next project milestone:
<task>

Also update:
PROJECT_PROGRESS.md
RESUME_STATE.md if resume evidence exists
CURRENT_STATE.md
NEXT_STEPS.md
```


## 23. Weakness Blocking Roadmap Rule

A weakness can block roadmap completion.

Blockers should be recorded when:

```text
candidate repeatedly fails same pattern
mock score is below pass mark
candidate cannot explain concept aloud
candidate cannot apply concept to project
candidate misses critical system design requirement
candidate gives tool-only answer
candidate cannot defend resume/project claim
```

Common blocking weaknesses:

```text
SQL grain confusion
weak window functions
Python file/API handling weakness
DSA pattern recognition weakness
system design starts with tools
missing idempotency
missing data quality
missing monitoring
weak project explanation
no measurable impact
unclear communication
```

Blocker update:

```text
If a blocker exists:
1. mark module as blocked
2. add blocker to WEAKNESS_REGISTER.md
3. add repair task to NEXT_STEPS.md
4. update CURRENT_STATE.md
```


## 24. Evidence Standards

Roadmap progress needs evidence.

Strong evidence:

```text
solved problem set
mock interview score
project commit
architecture explanation
resume bullet with metric
successful retest
documented feedback
mentor-approved answer
```

Weak evidence:

```text
read guide only
watched video only
generated file only
said "I understand"
copied solution
tool list without explanation
```

Completion evidence examples:

```text
SQL:
Solved 10 window-function problems and passed timed mock with 4/5.

Python:
Built API pagination script with error handling and logging.

System design:
Designed batch pipeline in 45 minutes and scored 4/5.

Project:
Explained finance tracker architecture and trade-offs with score 4/5.

Resume:
Created 5 evidence-backed bullets reviewed at 4/5.
```

Strict rule:

```text
Learning material generated does not equal interview readiness.
```


## 25. Roadmap Gates

Use roadmap gates to decide if candidate can move forward.

### Gate A: Baseline Known

Required:

```text
all major baseline scores recorded
top weaknesses identified
next steps created
```

Status:

```text
not_passed
```

### Gate B: Core Skills Ready

Required:

```text
SQL >= 4
Python >= 3.5
DSA >= 3
DE fundamentals >= 3.5
```

Status:

```text
not_passed
```

### Gate C: System Design Ready

Required:

```text
batch pipeline >= 4
data warehouse >= 4
data quality framework >= 4
one advanced case >= 3.5
```

Status:

```text
not_passed
```

### Gate D: Project Ready

Required:

```text
main project deep dive >= 4
architecture clearly explained
resume bullets created
GitHub README strong
```

Status:

```text
not_passed
```

### Gate E: Application Ready

Required:

```text
resume >= 4
GitHub >= 3.5
communication >= 3.5
no critical weaknesses open
```

Status:

```text
not_passed
```


## 26. Current Recommended Sequence

Recommended sequence from current state:

```text
1. Finish remaining progress tracking files.
2. Run profile baseline assessment.
3. Run SQL baseline.
4. Run Python baseline.
5. Start SQL + Python core improvement.
6. Run first batch pipeline system design mock.
7. Run finance tracker project deep dive.
8. Repair top weaknesses.
9. Create resume bullets from project/work evidence.
10. Start regular mock interview loop.
```

Why this sequence:

```text
The repository content is mostly generated.
But candidate performance evidence is missing.
Baseline assessment must happen before serious roadmap completion can be marked.
```

Current next file after this:

```text
practice/progress/NEXT_STEPS.md
```


## 27. SQL Roadmap Detail

SQL learning order:

```text
1. joins
2. aggregations
3. CTEs/subqueries
4. window functions
5. deduplication
6. date logic
7. gaps and islands
8. query optimization
9. business SQL cases
10. timed mocks
```

SQL milestone tracker:

| Milestone | Status | Evidence |
|---|---|---|
| Can explain join types | not_started | none |
| Can identify table grain | not_started | none |
| Can write CTE-based queries | not_started | none |
| Can use ROW_NUMBER/RANK | not_started | none |
| Can solve top N per group | not_started | none |
| Can dedupe correctly | not_started | none |
| Can solve gaps/islands basics | not_started | none |
| Can discuss indexes/execution basics | not_started | none |
| Can solve business case SQL | not_started | none |
| Passed SQL mock | not_started | none |


## 28. Python Roadmap Detail

Python learning order:

```text
1. syntax and functions
2. lists/dicts/sets
3. strings
4. files
5. JSON/CSV
6. API processing
7. error handling
8. logging
9. pandas basics
10. tests and clean scripts
```

Python milestone tracker:

| Milestone | Status | Evidence |
|---|---|---|
| Can write clean functions | not_started | none |
| Can use dict/set for data tasks | not_started | none |
| Can parse CSV | not_started | none |
| Can parse JSON | not_started | none |
| Can process paginated API | not_started | none |
| Can handle exceptions | not_started | none |
| Can add logging | not_started | none |
| Can use pandas basics | not_started | none |
| Can write reusable data script | not_started | none |
| Passed Python mock | not_started | none |


## 29. DSA Roadmap Detail

DSA learning order:

```text
1. arrays and strings
2. hashmaps
3. two pointers
4. sliding window
5. stack and queue
6. sorting and binary search
7. intervals
8. heap/top K
9. BFS/DFS basics
10. mixed pattern mock
```

DSA milestone tracker:

| Milestone | Status | Evidence |
|---|---|---|
| Recognizes hashmap pattern | not_started | none |
| Recognizes two pointer pattern | not_started | none |
| Recognizes sliding window pattern | not_started | none |
| Can solve stack basics | not_started | none |
| Can use binary search | not_started | none |
| Can merge intervals | not_started | none |
| Can solve top K | not_started | none |
| Can do BFS/DFS basics | not_started | none |
| Passed DSA pattern mock | not_started | none |


## 30. System Design Roadmap Detail

System design learning order:

```text
1. batch pipeline
2. data warehouse
3. data quality framework
4. reporting pipeline
5. data lake
6. CDC pipeline
7. event ingestion
8. realtime pipeline
```

System design milestone tracker:

| Milestone | Status | Evidence |
|---|---|---|
| Can clarify requirements | not_started | none |
| Can estimate scale/SLA | not_started | none |
| Can draw architecture | not_started | none |
| Can discuss data model | not_started | none |
| Can discuss idempotency | not_started | none |
| Can discuss backfills | not_started | none |
| Can discuss data quality | not_started | none |
| Can discuss monitoring | not_started | none |
| Can discuss security | not_started | none |
| Can discuss cost | not_started | none |
| Passed batch pipeline mock | not_started | none |
| Passed warehouse mock | not_started | none |
| Passed DQ mock | not_started | none |


## 31. Project Roadmap Detail

Main project roadmap:

```text
Project:
Personal Finance Tracking Platform
```

Project milestone tracker:

| Milestone | Status | Evidence |
|---|---|---|
| One-line pitch | not_started | none |
| Problem statement | not_started | none |
| Requirements | not_started | none |
| Architecture | not_started | none |
| Database schema | not_started | none |
| API design | not_started | none |
| Data ingestion flow | not_started | none |
| Merchant normalization logic | not_started | none |
| Categorization logic | not_started | none |
| Reconciliation logic | not_started | none |
| Telegram bot flow | not_started | none |
| AI/Ollama integration | not_started | none |
| Authentication/user management | in_progress | Sprint 1 in progress |
| Testing | not_started | none |
| CI/CD | not_started | none |
| Docker setup | not_started | none |
| Failure handling | not_started | none |
| Monitoring/logging | not_started | none |
| Resume bullets | not_started | none |
| Project deep-dive mock | not_started | none |

Exit criteria:

```text
Project can be explained strongly and defended under follow-up questions.
```


## 32. Resume And Portfolio Roadmap Detail

Resume/GitHub/LinkedIn roadmap:

| Milestone | Status | Evidence |
|---|---|---|
| Resume summary improved | not_started | none |
| Work experience bullets improved | not_started | none |
| Project bullets improved | not_started | none |
| Skills section cleaned | not_started | none |
| GitHub profile README updated | in_progress | profile README already exists |
| Main project README improved | not_started | none |
| Architecture diagram added | not_started | none |
| LinkedIn headline updated | in_progress | needs final review |
| LinkedIn about section updated | not_started | none |
| Portfolio proof ready | not_started | none |

Exit criteria:

```text
Resume and GitHub support the same story:
early-career Data Engineer with SQL, Python, ETL/ELT, warehouse, and strong project evidence.
```


## 33. Monthly Roadmap Review

Use this monthly.

```text
Month:
Current phase:
Phases completed:
Modules completed:
Scores improved:
Weaknesses repaired:
New blockers:
Project milestones:
Resume/GitHub updates:
Mocks completed:
Application activity:
Next month focus:
```

Monthly score table:

| Area | Start Score | End Score | Improvement | Evidence |
|---|---:|---:|---:|---|
| SQL | 0 | 0 | 0 | none |
| Python | 0 | 0 | 0 | none |
| DSA | 0 | 0 | 0 | none |
| DE fundamentals | 0 | 0 | 0 | none |
| System design | 0 | 0 | 0 | none |
| Project | 0 | 0 | 0 | none |
| Communication | 0 | 0 | 0 | none |
| Resume/GitHub | 0 | 0 | 0 | none |
```

Rule:

```text
If a month passes with no score improvement or evidence, the roadmap is not being executed.
```


## 34. Weekly Roadmap Review

Use this weekly.

```text
Week:
Main focus:
Completed:
Not completed:
Best evidence:
Worst weakness:
Repair action:
Next week tasks:
```

Weekly checklist:

| Task | Target | Actual | Status |
|---|---:|---:|---|
| SQL problems | 5 | 0 | not_started |
| Python drills | 3 | 0 | not_started |
| DSA problems | 3 | 0 | not_started |
| DE concept explanations | 2 | 0 | not_started |
| System design practice | 1 | 0 | not_started |
| Project improvement | 1 | 0 | not_started |
| Mock interview | 1 | 0 | not_started |
| Resume/GitHub improvement | 1 | 0 | not_started |

Weekly pass condition:

```text
At least one measurable skill output and one evidence artifact must be created.
```


## 35. Roadmap Completion Rules

A roadmap module can be marked complete only when:

```text
candidate practiced the module
candidate produced evidence
candidate scored at or above pass mark
candidate can explain the concept aloud
candidate can handle at least one follow-up
mentor approves completion
```

A roadmap module should stay in progress when:

```text
guide was only read
candidate solved only easy examples
candidate needed heavy hints
candidate cannot explain trade-offs
candidate has not been timed
```

A roadmap module should be marked needs_retest when:

```text
candidate improved but no retest happened
candidate scored 3.0 to 3.9
candidate solved practice but failed mock
```

A roadmap module should be blocked when:

```text
prerequisite is weak
candidate repeatedly fails
project evidence missing
communication blocks explanation
```


## 36. Roadmap Anti-Cheating Rules

Do not inflate progress.

Invalid completion reasons:

```text
file generated
guide downloaded
topic read once
candidate says "I know this"
AI gave solution
copied answer
watched tutorial
no timed attempt
no score
no evidence
```

Valid completion reasons:

```text
candidate solved problems independently
candidate passed mock interview
candidate explained project clearly
candidate produced working code
candidate defended design choices
candidate repaired weakness and retested
```

Strict mentor rule:

```text
The roadmap exists to measure readiness, not to make the candidate feel productive.
```


## 37. Current Machine-Readable Roadmap State

Keep this block synchronized.

```yaml
roadmap_version: "1.0"
last_updated: "YYYY-MM-DD"
current_phase: "phase_0_setup_and_skill_repository"
current_phase_status: "in_progress"
next_phase: "phase_1_profile_baseline_assessment"
latest_generated_file: "practice/progress/ROADMAP_PROGRESS.md"
latest_zip_name: "data-engineering-sensei-with-roadmap-progress.zip"

phase_status:
  phase_0_setup: "in_progress"
  phase_1_profile_baseline: "not_started"
  phase_2_sql_python_dsa: "not_started"
  phase_3_de_fundamentals: "not_started"
  phase_4_modeling_warehouse_lake: "not_started"
  phase_5_pipeline_system_design: "not_started"
  phase_6_project_deep_dive: "not_started"
  phase_7_mock_interview_loop: "not_started"
  phase_8_career_assets: "not_started"
  phase_9_job_search: "not_started"

readiness_gates:
  baseline_known: "not_passed"
  core_skills_ready: "not_passed"
  system_design_ready: "not_passed"
  project_ready: "not_passed"
  application_ready: "not_passed"

current_scores:
  sql: 0
  python: 0
  dsa: 0
  de_fundamentals: 0
  system_design: 0
  project_deep_dive: 0
  communication: 0
  resume_github: 0

next_best_action:
  - "Generate practice/progress/NEXT_STEPS.md"
  - "Generate practice/progress/SESSION_LOG.md"
  - "Run baseline assessment"
```


## 38. Roadmap Mentor Instructions

The AI mentor must use ROADMAP_PROGRESS.md as the long-term map.

Before starting a session, check:

```text
current phase
active module
module status
last score
blocking weakness
next required evidence
```

After a session, update:

```text
module status
score
evidence
weaknesses
next milestone
related files
```

Mentor must be strict:

```text
Do not mark complete without evidence.
Do not skip baseline assessment.
Do not let candidate jump to job search before readiness gates.
Do not let generated files count as skill mastery.
Do not accept vague answers without retest.
```

Mentor feedback after roadmap update:

```text
Roadmap status:
Evidence added:
Score:
Module status:
Next milestone:
Files to update next:
```


## 39. Next Roadmap Actions

Immediate roadmap actions:

```text
1. Generate practice/progress/NEXT_STEPS.md.
2. Generate practice/progress/SESSION_LOG.md.
3. Generate practice/progress/WEAKNESS_REGISTER.md.
4. Generate practice/progress/MOCK_INTERVIEW_HISTORY.md.
5. Generate practice/progress/PROJECT_PROGRESS.md.
6. Run baseline profile assessment.
7. Start SQL baseline drill.
8. Start Python baseline drill.
9. Start batch pipeline system design mock.
10. Start finance tracker project deep dive.
```

First actual learning action after file generation:

```text
Run profile baseline assessment.
```

Prompt:

```text
Start Phase 1 profile baseline assessment for Data Engineering Sensei.
Ask one question at a time.
Score strictly.
Update ROADMAP_PROGRESS.md and CURRENT_STATE.md after the assessment.
```


## 40. Final Summary

`ROADMAP_PROGRESS.md` is the long-term roadmap tracker for Data Engineering Sensei.

It tracks:

```text
phases
modules
scores
status
evidence
weaknesses
roadmap gates
next milestones
career readiness
```

Current truth:

```text
The skill repository is mostly generated.
Progress tracking is being created.
Actual interview readiness is not yet baselined.
No module should be marked complete until performance evidence exists.
```

Current next milestone:

```text
Finish remaining progress files, then run baseline assessment.
```

Final rule:

```text
Roadmap progress must be earned through practice, scoring, evidence, and retesting.
```
