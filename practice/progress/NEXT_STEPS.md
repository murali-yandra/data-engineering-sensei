# Next Steps

Generated: 2026-06-06

Path:

```text
data-engineering-sensei/practice/progress/NEXT_STEPS.md
```

This file is the **active task queue** for Data Engineering Sensei.

It tells the AI mentor and candidate:

```text
what to do next
what is urgent
what is blocked
what should be done today
what should be done this week
what should be done after file generation
what progress files must be updated
what learning session should start next
```

This file is different from:

```text
CURRENT_STATE.md:
current live snapshot

ROADMAP_PROGRESS.md:
long-term roadmap status

NEXT_STEPS.md:
immediate executable task queue
```

Current status:

```text
Initial NEXT_STEPS.md generated.
The candidate is still in repo/progress-file generation phase.
No baseline assessment has been completed yet.
```

Important rule:

```text
NEXT_STEPS.md should never become a huge wishlist.
It should show the smallest useful next actions that move the candidate toward interview readiness.
```


## 1. Purpose Of This File

`NEXT_STEPS.md` exists to prevent random learning.

It should answer:

```text
What exactly should I do next?
Why should I do it?
Which file should I use?
How long should it take?
What output should be produced?
What progress file should be updated after it?
```

The AI mentor should use this file when the candidate says:

```text
what next?
continue
what should I do now?
start today's task
give me next drill
update my progress
```

The candidate should use this file to avoid:

```text
topic hopping
repeating completed work
starting job applications too early
over-learning theory without practice
building random files without assessment
ignoring weaknesses
```

Core principle:

```text
Every next step must create either skill, evidence, feedback, or readiness.
```


## 2. Relationship With Other Progress Files

Use this file with the other progress files.

| File | Role |
|---|---|
| `practice/progress/CURRENT_STATE.md` | says where the candidate is right now |
| `practice/progress/ROADMAP_PROGRESS.md` | says where the candidate is on the long-term roadmap |
| `practice/progress/NEXT_STEPS.md` | says what to do next |
| `practice/progress/SESSION_LOG.md` | records what actually happened |
| `practice/progress/WEAKNESS_REGISTER.md` | stores weaknesses and repair actions |
| `practice/progress/MOCK_INTERVIEW_HISTORY.md` | stores mock scores |
| `practice/progress/PROJECT_PROGRESS.md` | stores project milestones |
| `practice/progress/RESUME_STATE.md` | stores resume tasks and bullet evidence |
| `practice/progress/GITHUB_PORTFOLIO_STATE.md` | stores GitHub/portfolio tasks |
| `practice/progress/JOB_SEARCH_STATE.md` | stores application/referral/interview tasks |

Update rules:

```text
If a task is completed:
update NEXT_STEPS.md and SESSION_LOG.md.

If a task changes current state:
update CURRENT_STATE.md.

If a task changes roadmap phase or score:
update ROADMAP_PROGRESS.md.

If a task discovers weakness:
update WEAKNESS_REGISTER.md.

If a task is a mock:
update MOCK_INTERVIEW_HISTORY.md.

If a task creates project evidence:
update PROJECT_PROGRESS.md and maybe RESUME_STATE.md.

If a task affects job search:
update JOB_SEARCH_STATE.md.
```


## 3. Task Status Values

Use only these task statuses:

```text
todo:
task is ready to start

in_progress:
task has started but is not complete

blocked:
task cannot start until another task is done

waiting:
task needs user input, external action, or review

done:
task completed with evidence

dropped:
task intentionally removed with reason

replaced:
task replaced by a better task
```

Do not use vague labels:

```text
maybe
soon
almost
kind of done
reviewed
learned
okay
```

Completion rule:

```text
A task is done only when the output exists.
```

Examples:

```text
Bad:
Study SQL.

Good:
Solve 5 joins + aggregation problems from practice/sql/joins.md and score answers.
```


## 4. Priority Levels

Use priority levels to decide what happens first.

```text
P0:
urgent blocker. Must do before anything else.

P1:
high priority. Should be done next.

P2:
normal priority. Useful but not blocking.

P3:
optional or later. Do not distract from core readiness.
```

Current priority logic:

```text
P0:
finish progress file structure and run baseline assessment

P1:
SQL baseline, Python baseline, batch pipeline mock, project deep dive

P2:
DSA baseline, GitHub/resume improvements, more system design cases

P3:
advanced cloud, advanced DSA, international applications, extra projects
```

Rule:

```text
If a P3 task distracts from a P0/P1 task, postpone it.
```


## 5. Task Format

Every task should use this format:

```text
Task ID:
Priority:
Status:
Task:
Why:
Input file:
Output:
Time box:
Success criteria:
After completion update:
```

Example:

```text
Task ID:
NS-001

Priority:
P0

Status:
todo

Task:
Generate practice/progress/SESSION_LOG.md.

Why:
The repo needs a chronological learning history file before serious practice starts.

Input file:
CURRENT_STATE.md and ROADMAP_PROGRESS.md

Output:
SESSION_LOG.md generated and added to latest ZIP.

Time box:
30-45 minutes

Success criteria:
File exists, has templates for session logging, and ZIP is updated.

After completion update:
CURRENT_STATE.md
ROADMAP_PROGRESS.md
NEXT_STEPS.md
```


## 6. Current Immediate Task Queue

These are the current highest-priority tasks.

| Task ID | Priority | Status | Task | Output |
|---|---|---|---|---|
| NS-001 | P0 | done | Generate `practice/progress/NEXT_STEPS.md` | This file |
| NS-002 | P0 | todo | Generate `practice/progress/SESSION_LOG.md` | chronological session log |
| NS-003 | P0 | todo | Generate `practice/progress/WEAKNESS_REGISTER.md` | weakness tracking file |
| NS-004 | P0 | todo | Generate `practice/progress/MOCK_INTERVIEW_HISTORY.md` | mock score history |
| NS-005 | P1 | todo | Generate `practice/progress/PROJECT_PROGRESS.md` | project evidence tracker |
| NS-006 | P1 | todo | Generate `practice/progress/RESUME_STATE.md` | resume readiness tracker |
| NS-007 | P1 | todo | Generate `practice/progress/GITHUB_PORTFOLIO_STATE.md` | GitHub portfolio tracker |
| NS-008 | P2 | todo | Generate `practice/progress/JOB_SEARCH_STATE.md` | job search tracker |
| NS-009 | P0 | blocked | Run profile baseline assessment | scores + weaknesses |
| NS-010 | P1 | blocked | Run SQL baseline assessment | SQL score |
| NS-011 | P1 | blocked | Run Python baseline assessment | Python score |
| NS-012 | P1 | blocked | Run batch pipeline system design mock | system design score |
| NS-013 | P1 | blocked | Run finance tracker project deep dive | project readiness score |

Blocked reason:

```text
Baseline and practice tasks should start after core progress files are generated.
```

Next task after this file:

```text
Generate practice/progress/SESSION_LOG.md.
```


## 7. Current File Generation Tasks

The candidate is currently generating progress files.

### NS-002

```text
Task:
Generate practice/progress/SESSION_LOG.md

Priority:
P0

Status:
todo

Why:
Need a chronological record of learning sessions, file generation, drills, mocks, scores, and progress updates.

Output:
SESSION_LOG.md with templates and initial entries.

Success criteria:
Can store date, mode, topic, completed work, score, weakness, next action, and related files.
```

### NS-003

```text
Task:
Generate practice/progress/WEAKNESS_REGISTER.md

Priority:
P0

Status:
todo

Why:
Need one place to store weaknesses, severity, repair plan, retest evidence, and status.

Output:
WEAKNESS_REGISTER.md

Success criteria:
Can track weakness ID, area, severity, evidence, repair task, retest score, and status.
```

### NS-004

```text
Task:
Generate practice/progress/MOCK_INTERVIEW_HISTORY.md

Priority:
P0

Status:
todo

Why:
Need a history of mock interviews with scores and feedback.

Output:
MOCK_INTERVIEW_HISTORY.md

Success criteria:
Can store mock type, topic, score, pass/fail, feedback, weakness, repair action, and retest date.
```

### NS-005

```text
Task:
Generate practice/progress/PROJECT_PROGRESS.md

Priority:
P1

Status:
todo

Why:
Need to track the Personal Finance Tracking Platform and portfolio evidence.

Output:
PROJECT_PROGRESS.md

Success criteria:
Tracks features, architecture, commits, README, interview explanation, resume evidence, and blockers.
```


## 8. Current Learning Tasks After File Generation

After the progress files are generated, start learning/practice in this order.

| Order | Task | File/Mode | Output |
|---:|---|---|---|
| 1 | Run profile baseline assessment | `modes/profile-assessment-mode.md` | baseline scores |
| 2 | Run SQL baseline | `modes/sql-drill-mode.md` | SQL weakness map |
| 3 | Run Python baseline | `modes/python-drill-mode.md` | Python weakness map |
| 4 | Run DE fundamentals baseline | `modes/data-engineering-fundamentals-mode.md` | fundamentals score |
| 5 | Run first system design mock | `practice/system-design/batch-pipeline.md` | system design score |
| 6 | Run project deep dive | `modes/project-deep-dive-mode.md` | project readiness score |
| 7 | Update roadmap and next steps | progress files | repair plan |

Rule:

```text
Do not spend weeks reading guides before baseline assessment.
Baseline first, then targeted repair.
```


## 9. Today's Recommended Next Action

Recommended next action:

```text
Generate practice/progress/SESSION_LOG.md.
```

Why:

```text
The repository already has CANDIDATE_PROFILE.md, CURRENT_STATE.md, ROADMAP_PROGRESS.md, and NEXT_STEPS.md.
The next missing foundation file is SESSION_LOG.md.
It will record all future learning sessions and prevent progress loss.
```

Prompt to use:

```text
Generate practice/progress/SESSION_LOG.md for Data Engineering Sensei.
It should store chronological AI learning sessions, file generation sessions, drills, mock interviews, scores, weaknesses, next actions, and which progress files were updated.
Fill it with prompts and templates for now because actual learning has not started yet.
```

After generation, update:

```text
CURRENT_STATE.md
ROADMAP_PROGRESS.md
NEXT_STEPS.md
```


## 10. This Week's Recommended Plan

Current week plan while still in setup phase:

| Day | Task | Output |
|---|---|---|
| Day 1 | Generate remaining progress files | progress structure complete |
| Day 2 | Run profile baseline assessment | baseline scorecard |
| Day 3 | Run SQL baseline | SQL weakness map |
| Day 4 | Run Python baseline | Python weakness map |
| Day 5 | Run batch pipeline mock | system design baseline |
| Day 6 | Run finance tracker project deep dive | project score |
| Day 7 | Update roadmap + next 30-day plan | repair plan |

Minimum outcome by end of week:

```text
baseline scores known
top 5 weaknesses identified
next 7-day repair plan created
main project deep-dive gaps known
```


## 11. First 10 Learning Tasks

Once setup files are done, execute these tasks.

### Task 1

```text
Run profile assessment.
Output:
baseline score table and top weaknesses.
```

### Task 2

```text
Solve 5 SQL joins/aggregation questions.
Output:
score and mistakes.
```

### Task 3

```text
Solve 5 SQL window function questions.
Output:
window weakness map.
```

### Task 4

```text
Write Python CSV + JSON processing script.
Output:
working script and feedback.
```

### Task 5

```text
Write Python API pagination script.
Output:
working script with error handling.
```

### Task 6

```text
Practice hashmap DSA pattern with 5 problems.
Output:
pattern recognition score.
```

### Task 7

```text
Explain ETL vs ELT, batch vs streaming, warehouse vs lake.
Output:
DE fundamentals score.
```

### Task 8

```text
Design batch pipeline in mock interview style.
Output:
system design score and feedback.
```

### Task 9

```text
Explain Personal Finance Tracking Platform in 2 minutes.
Output:
project pitch score.
```

### Task 10

```text
Create 3 resume bullets from project/work evidence.
Output:
resume bullet score.
```


## 12. Daily Task Template

Use this for daily planning.

```text
Date:
Main focus:
Available time:
Energy level:
Task 1:
Task 2:
Task 3:
Expected output:
Progress file to update:
```

Example:

```text
Date:
2026-06-06

Main focus:
SQL baseline

Available time:
60 minutes

Task 1:
Solve 3 join questions.

Task 2:
Solve 2 aggregation questions.

Task 3:
Review mistakes and update weakness register.

Expected output:
SQL baseline mini-score.

Progress file to update:
CURRENT_STATE.md
NEXT_STEPS.md
WEAKNESS_REGISTER.md
SESSION_LOG.md
```

Daily rule:

```text
Do one measurable thing, not five half-started things.
```


## 13. Weekly Task Template

Use this for weekly planning.

```text
Week:
Main goal:
Skill focus:
Project focus:
Mock interview:
Resume/GitHub task:
Weakness to repair:
Success criteria:
```

Example:

```text
Week:
Week 1

Main goal:
Get baseline scores.

Skill focus:
SQL + Python baseline.

Project focus:
Finance tracker 2-minute explanation.

Mock interview:
Batch pipeline system design.

Resume/GitHub task:
Draft project README outline.

Weakness to repair:
Unknown until baseline.

Success criteria:
At least 5 scores recorded and top 5 weaknesses identified.
```

Weekly rule:

```text
A week is successful only if it creates evidence.
```


## 14. Task Completion Checklist

Before marking a task done, check:

```text
Was the task actually completed?
Is there an output?
Was there a score if it was practice?
Was feedback captured?
Were weaknesses recorded?
Was next action assigned?
Were related progress files updated?
```

Task is not done if:

```text
candidate only read material
candidate only generated a file but did not use it
candidate watched a video
candidate copied answer
candidate says "understood" without evidence
```

Completion note template:

```text
Completed:
Evidence:
Score:
Weakness:
Next:
Files updated:
```


## 15. Next Step Decision Rules

Use these rules to choose next steps.

### If baseline is missing

```text
Do baseline assessment first.
```

### If SQL score < 4

```text
Prioritize SQL drills.
```

### If Python score < 3.5

```text
Prioritize Python data scripting.
```

### If project explanation score < 4

```text
Prioritize project deep dive and resume evidence.
```

### If system design score < 3.5

```text
Prioritize batch pipeline, data warehouse, and data quality framework.
```

### If communication score < 3.5

```text
Prioritize mock interviews and structured explanation practice.
```

### If resume score < 4

```text
Prioritize evidence-backed bullets and GitHub proof.
```

### If all core scores >= target

```text
Start job application execution and mock interview maintenance.
```


## 16. Baseline Assessment Next Steps

Baseline assessment should produce:

```text
SQL score
Python score
DSA score
DE fundamentals score
system design score
project deep-dive score
communication score
resume/GitHub score
top strengths
top weaknesses
first 7-day repair plan
```

Baseline task:

```text
Task ID:
NS-009

Priority:
P0

Status:
blocked until progress files are generated

Task:
Run profile baseline assessment.

Input:
CANDIDATE_PROFILE.md
CURRENT_STATE.md
ROADMAP_PROGRESS.md

Output:
baseline scorecard and weakness map

Success criteria:
At least 8 areas scored from 0 to 5.
Top 5 weaknesses recorded.
Next 7 days of tasks created.
```

Prompt:

```text
Start my Data Engineering Sensei baseline assessment.
Ask one question at a time.
Score strictly from 0 to 5.
Do not give answers first.
After the assessment, update CURRENT_STATE.md, ROADMAP_PROGRESS.md, NEXT_STEPS.md, and WEAKNESS_REGISTER.md.
```


## 17. SQL Next Steps

SQL priority:

```text
1. joins
2. aggregations
3. CTEs
4. window functions
5. deduplication
6. business cases
7. query optimization
```

Immediate SQL tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| SQL-001 | P1 | blocked | SQL baseline assessment | score recorded |
| SQL-002 | P1 | todo after baseline | 5 joins problems | 4/5 accuracy |
| SQL-003 | P1 | todo after baseline | 5 window function problems | can explain ROW_NUMBER/RANK/SUM OVER |
| SQL-004 | P2 | todo after baseline | 3 dedupe problems | no DISTINCT misuse |
| SQL-005 | P2 | todo after baseline | 2 business SQL cases | correct grain |

Prompt:

```text
Start SQL baseline for Data Engineering interviews.
Ask me one SQL problem at a time.
Focus on joins, aggregation, CTEs, windows, and deduplication.
Score my answer and update NEXT_STEPS.md with repair tasks.
```


## 18. Python Next Steps

Python priority:

```text
1. functions and data structures
2. files
3. JSON/CSV
4. API processing
5. error handling
6. logging
7. pandas basics
8. testing
```

Immediate Python tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| PY-001 | P1 | blocked | Python baseline assessment | score recorded |
| PY-002 | P1 | todo after baseline | CSV/JSON parsing script | clean reusable function |
| PY-003 | P1 | todo after baseline | API pagination script | handles pagination/errors |
| PY-004 | P2 | todo after baseline | logging + exceptions drill | clean error handling |
| PY-005 | P2 | todo after baseline | pandas basics drill | groupby/filter/merge |

Prompt:

```text
Start Python data engineering baseline.
Give me one practical script task at a time.
Focus on files, JSON, CSV, API processing, error handling, and clean functions.
Score my solution and update NEXT_STEPS.md with repair tasks.
```


## 19. DSA Next Steps

DSA priority for Data Engineering:

```text
1. hashmaps
2. arrays/strings
3. two pointers
4. sliding window
5. stack/queue
6. binary search
7. intervals
8. heap/top K
9. BFS/DFS basics
```

Immediate DSA tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| DSA-001 | P2 | blocked | DSA pattern baseline | score recorded |
| DSA-002 | P2 | todo after baseline | hashmap pattern drill | identify pattern fast |
| DSA-003 | P2 | todo after baseline | two pointer drill | explain optimized approach |
| DSA-004 | P2 | todo after baseline | sliding window drill | window logic correct |
| DSA-005 | P3 | todo later | mixed easy/medium set | 70%+ independent |

Rule:

```text
DSA should not block SQL/Python/project/system design unless the target company heavily tests DSA.
```


## 20. DE Fundamentals Next Steps

Fundamentals priority:

```text
ETL vs ELT
batch vs streaming
warehouse vs lake vs lakehouse
partitioning
orchestration
DAGs
idempotency
backfills
data quality
schema evolution
CDC
monitoring
security
cost
```

Immediate tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| DE-001 | P1 | blocked | Fundamentals baseline | score recorded |
| DE-002 | P1 | todo after baseline | Explain ETL vs ELT | 90-second answer |
| DE-003 | P1 | todo after baseline | Explain batch vs streaming | example-based answer |
| DE-004 | P1 | todo after baseline | Explain idempotency/backfills | practical pipeline answer |
| DE-005 | P2 | todo after baseline | Explain DQ and monitoring | production-ready answer |

Prompt:

```text
Test my Data Engineering fundamentals.
Ask me short interview questions one by one.
Score each answer and give corrected answer after I respond.
```


## 21. System Design Next Steps

System design priority:

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

Immediate tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| SD-001 | P1 | blocked | Batch pipeline mock | score recorded |
| SD-002 | P1 | todo after baseline | Data warehouse mock | score >= 3.5 first attempt |
| SD-003 | P1 | todo after baseline | DQ framework mock | covers rules/gates/alerts |
| SD-004 | P2 | todo after baseline | Reporting pipeline mock | metrics/grain/reconciliation |
| SD-005 | P2 | todo later | CDC pipeline mock | handles offsets/deletes/replay |

System design answer structure:

```text
requirements
sources
consumers
scale
SLA
architecture
data model
processing
quality
failure handling
monitoring
security
cost
trade-offs
summary
```

Prompt:

```text
Start a Data Engineering system design mock.
Topic: batch pipeline.
Ask clarifying questions first, then let me design.
Score me strictly from 0 to 5.
```


## 22. Project Deep Dive Next Steps

Main project:

```text
Personal Finance Tracking Platform
```

Immediate project tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| PRJ-001 | P1 | blocked | 2-minute project explanation | score recorded |
| PRJ-002 | P1 | todo after baseline | architecture explanation | clear source → API → DB → bot flow |
| PRJ-003 | P1 | todo after baseline | database model explanation | entities and relationships clear |
| PRJ-004 | P1 | todo after baseline | data quality/reconciliation explanation | production thinking shown |
| PRJ-005 | P2 | todo after baseline | resume bullets | 3 strong bullets |
| PRJ-006 | P2 | todo after baseline | GitHub README update | project proof improved |

Project explanation checklist:

```text
problem
user
requirements
architecture
data model
pipeline flow
trade-offs
failure handling
data quality
security
deployment
impact
future improvements
```

Prompt:

```text
Start project deep dive for my Personal Finance Tracking Platform.
Ask me one question at a time.
Score my answer.
Help me turn strong answers into resume and GitHub evidence.
```


## 23. Resume Next Steps

Resume tasks should start after project evidence is clearer.

Immediate resume tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| RES-001 | P2 | blocked | collect project evidence | evidence bank updated |
| RES-002 | P2 | blocked | create 3 project bullets | defensible bullets |
| RES-003 | P2 | blocked | improve SQL/work bullets | impact clearer |
| RES-004 | P2 | blocked | align skills to target role | no irrelevant clutter |
| RES-005 | P2 | blocked | resume mock screen | score >= 4 |

Bullet formula:

```text
Action + technical work + scale/context + measurable/business result
```

Prompt:

```text
Help me create evidence-backed resume bullets for my data engineering project and work experience.
Ask me for missing metrics instead of inventing them.
```


## 24. GitHub Portfolio Next Steps

GitHub tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| GH-001 | P2 | todo | Ensure repo structure is clean | no wrong paths |
| GH-002 | P2 | blocked | improve profile README | clear DE positioning |
| GH-003 | P2 | blocked | improve finance tracker README | setup + architecture + features |
| GH-004 | P2 | blocked | add architecture diagram | visually clear |
| GH-005 | P3 | todo later | add demo/screenshots | proof improved |

GitHub quality checklist:

```text
clear README
setup instructions
architecture
schema
API examples
Docker instructions
tests
CI/CD
roadmap
meaningful commits
```

Prompt:

```text
Review my GitHub portfolio for Data Engineering roles.
Score it from 0 to 5.
Give me the next 5 improvements in priority order.
```


## 25. Job Search Next Steps

Current job search state:

```text
not active
preparation phase
```

Do not start aggressive job applications until:

```text
SQL >= 4
Python >= 3.5
System design >= 3.5
Project deep dive >= 4
Resume >= 4
GitHub >= 3.5
Communication >= 3.5
```

Future job-search tasks:

| Task ID | Priority | Status | Task | Success Criteria |
|---|---|---|---|---|
| JOB-001 | P3 | blocked | define target role list | role focus clear |
| JOB-002 | P3 | blocked | create company list | 30 companies |
| JOB-003 | P3 | blocked | create referral message | ready to send |
| JOB-004 | P3 | blocked | application tracker | job search state updated |
| JOB-005 | P3 | blocked | apply selectively | feedback loop active |

Rule:

```text
Preparation without applications is incomplete.
Applications without readiness waste opportunities.
```


## 26. Blocked Tasks

Current blocked tasks:

| Task | Blocked By | Unblock Condition |
|---|---|---|
| Baseline assessment | remaining progress files | SESSION_LOG, WEAKNESS_REGISTER, MOCK_INTERVIEW_HISTORY generated |
| SQL baseline | profile baseline not run | profile baseline completed |
| Python baseline | profile baseline not run | profile baseline completed |
| System design mock | baseline not run | initial profile known |
| Project deep dive | progress structure incomplete | PROJECT_PROGRESS file generated |
| Resume bullet work | project evidence missing | project deep dive completed |
| Job applications | readiness gate not passed | core scores improved |

Prompt:

```text
Show me my blocked tasks and tell me the fastest unblock path.
```


## 27. Active Risks In Next Steps

Current risks:

```text
generating many files but not practicing
marking roadmap complete without scores
starting job search before proof
jumping to advanced topics before baseline
not updating progress files after sessions
not creating resume evidence from project
over-focusing on DSA at the cost of SQL/Python/DE design
```

Risk controls:

```text
baseline assessment first
strict scoring
weekly evidence review
weakness register
mock interview loop
resume proof checks
small next steps only
```

Mentor warning:

```text
If the candidate keeps generating content but avoids baseline mocks, stop file generation and run assessment.
```


## 28. Next Steps Update Prompt

Use this prompt to update NEXT_STEPS.md:

```text
Update NEXT_STEPS.md.

Completed task:
<task>

Evidence:
<file/problem/mock score/output>

Current blockers:
<blockers>

New task:
<task>

Priority:
P0/P1/P2/P3

Status:
todo/in_progress/blocked/waiting/done/dropped/replaced

Next 3 actions:
1.
2.
3.

Also update:
CURRENT_STATE.md
ROADMAP_PROGRESS.md
SESSION_LOG.md
WEAKNESS_REGISTER.md if needed
MOCK_INTERVIEW_HISTORY.md if needed
```


## 29. Session Start Prompt Using NEXT_STEPS.md

Use this prompt at the start of a work session:

```text
You are my Data Engineering Sensei mentor.

Read NEXT_STEPS.md, CURRENT_STATE.md, and ROADMAP_PROGRESS.md.
Tell me:
1. the current highest-priority task
2. why it matters
3. what output we need
4. which file we will use
5. how long the task should take
6. what progress files we will update after

Then start the task immediately.
```


## 30. Session End Prompt Using NEXT_STEPS.md

Use this prompt at the end of a work session:

```text
End this Data Engineering Sensei session.

Update NEXT_STEPS.md:
1. mark completed task status
2. add evidence
3. add next task
4. update blockers
5. update priority queue

Also update:
CURRENT_STATE.md
ROADMAP_PROGRESS.md
SESSION_LOG.md
WEAKNESS_REGISTER.md if a weakness appeared
MOCK_INTERVIEW_HISTORY.md if it was a mock
PROJECT_PROGRESS.md if project evidence was created
RESUME_STATE.md if resume evidence was created
```


## 31. Small Task Examples

Good next-step examples:

```text
Solve 5 SQL join questions and score mistakes.
Write one Python script that reads JSON and outputs cleaned CSV.
Explain ETL vs ELT in 90 seconds and get scored.
Design batch pipeline for 30 minutes and receive feedback.
Explain finance tracker project in 2 minutes.
Create 3 resume bullets with evidence.
Update GitHub README setup section.
Repair window function weakness with 5 problems.
Retest batch pipeline after studying idempotency.
```

Bad next-step examples:

```text
Learn SQL.
Study Python.
Improve resume.
Prepare for jobs.
Understand system design.
Read everything.
Apply abroad.
Build more projects.
```

Rule:

```text
A good next step is concrete, time-boxed, and produces evidence.
```


## 32. Time-Box Rules

Use time boxes to prevent endless work.

Recommended time boxes:

```text
quick definition:
10 minutes

single drill:
20-30 minutes

SQL/Python problem set:
45-60 minutes

system design mock:
45 minutes

project deep dive:
45-60 minutes

resume/GitHub review:
45 minutes

weekly review:
30 minutes
```

If time is short:

```text
do one focused task
do not start a large vague task
```

If task exceeds time box:

```text
record blocker
assign next action
do not pretend it is complete
```


## 33. Done Definition By Task Type

### File generation task is done when:

```text
file exists
path is correct
content matches purpose
ZIP updated
CURRENT_STATE/ROADMAP/NEXT_STEPS updated
```

### Drill task is done when:

```text
problem attempted
answer reviewed
score assigned
mistakes recorded
repair task assigned if needed
```

### Mock task is done when:

```text
mock completed under time pressure
score assigned
feedback recorded
weakness updated
retest action assigned
```

### Project task is done when:

```text
project evidence exists
explanation reviewed
interview value clear
resume/GitHub value identified
```

### Resume task is done when:

```text
bullet is evidence-backed
claim can be defended
review score assigned
```


## 34. Current Next 3 Actions

Current next 3 actions:

```text
1. Generate practice/progress/SESSION_LOG.md.
2. Generate practice/progress/WEAKNESS_REGISTER.md.
3. Generate practice/progress/MOCK_INTERVIEW_HISTORY.md.
```

After those:

```text
4. Generate PROJECT_PROGRESS.md.
5. Run profile baseline assessment.
6. Run SQL baseline assessment.
```

Do not skip to:

```text
job applications
advanced DSA
advanced cloud
new unrelated projects
```


## 35. Current Compact Task Board

Compact task board:

| Priority | Task | Status |
|---|---|---|
| P0 | Generate NEXT_STEPS.md | done |
| P0 | Generate SESSION_LOG.md | todo |
| P0 | Generate WEAKNESS_REGISTER.md | todo |
| P0 | Generate MOCK_INTERVIEW_HISTORY.md | todo |
| P1 | Generate PROJECT_PROGRESS.md | todo |
| P1 | Generate RESUME_STATE.md | todo |
| P1 | Run baseline assessment | blocked |
| P1 | Run SQL baseline | blocked |
| P1 | Run Python baseline | blocked |
| P1 | Run batch pipeline mock | blocked |
| P1 | Run finance tracker deep dive | blocked |

Update rule:

```text
Keep this compact board short.
Detailed task history belongs in SESSION_LOG.md.
```


## 36. Machine-Readable Next Steps

Keep this YAML-style block synchronized.

```yaml
next_steps_version: "1.0"
last_updated: "YYYY-MM-DD"
current_highest_priority: "Generate practice/progress/SESSION_LOG.md"
current_phase: "progress_file_generation"
task_board:
  NS-001:
    priority: "P0"
    status: "done"
    task: "Generate practice/progress/NEXT_STEPS.md"
  NS-002:
    priority: "P0"
    status: "todo"
    task: "Generate practice/progress/SESSION_LOG.md"
  NS-003:
    priority: "P0"
    status: "todo"
    task: "Generate practice/progress/WEAKNESS_REGISTER.md"
  NS-004:
    priority: "P0"
    status: "todo"
    task: "Generate practice/progress/MOCK_INTERVIEW_HISTORY.md"
  NS-005:
    priority: "P1"
    status: "todo"
    task: "Generate practice/progress/PROJECT_PROGRESS.md"
  NS-006:
    priority: "P1"
    status: "todo"
    task: "Generate practice/progress/RESUME_STATE.md"
  NS-007:
    priority: "P1"
    status: "todo"
    task: "Generate practice/progress/GITHUB_PORTFOLIO_STATE.md"
  NS-008:
    priority: "P2"
    status: "todo"
    task: "Generate practice/progress/JOB_SEARCH_STATE.md"
  NS-009:
    priority: "P0"
    status: "blocked"
    task: "Run profile baseline assessment"
blocked_by:
  - "progress tracking files not fully generated"
next_3_actions:
  - "Generate SESSION_LOG.md"
  - "Generate WEAKNESS_REGISTER.md"
  - "Generate MOCK_INTERVIEW_HISTORY.md"
files_to_update_after_next_task:
  - "CURRENT_STATE.md"
  - "ROADMAP_PROGRESS.md"
  - "NEXT_STEPS.md"
```


## 37. Mentor Instructions For NEXT_STEPS.md

The AI mentor must use this file to choose the next action.

Before starting:

```text
read compact task board
read machine-readable next steps
check blockers
choose highest P0/P1 todo task
state why it matters
start task
```

After finishing:

```text
mark task done
add evidence
add next task
update blockers
update related progress files
```

Mentor must not:

```text
create random new tasks
ignore blocked status
skip baseline assessment
mark practice complete without score
let candidate avoid weaknesses
recommend job applications before readiness
```

Mentor response format:

```text
Current next task:
Why:
Output:
Time box:
Start:
```


## 38. Candidate Instructions

The candidate should use this file like a command center.

When opening the repo, ask:

```text
What is my current P0 task?
What output should I create?
What file should I update after?
```

Candidate should avoid:

```text
working without a task ID
starting too many tasks
skipping progress updates
doing only reading
avoiding mock tests
ignoring weak areas
```

Candidate should ask the mentor:

```text
Start my current highest-priority task from NEXT_STEPS.md.
```

Or:

```text
Show my next 3 actions from NEXT_STEPS.md and start the first one.
```


## 39. Next File To Generate

Next file:

```text
practice/progress/SESSION_LOG.md
```

Reason:

```text
The repo needs a chronological log before real practice starts.
Session logs will preserve what happened during:
- file generation
- drills
- mocks
- project reviews
- resume updates
- weakness repair
```

Prompt:

```text
Generate practice/progress/SESSION_LOG.md for Data Engineering Sensei.
It should store chronological learning sessions, file generation sessions, drills, mock interviews, scores, weaknesses, next actions, and related progress file updates.
For now, fill it with templates, examples, and instructions because actual learning has not started yet.
```

After generating it, update this task:

```text
NS-002 status = done
next task = NS-003 Generate WEAKNESS_REGISTER.md
```


## 40. Final Summary

`NEXT_STEPS.md` is the immediate execution plan for Data Engineering Sensei.

It tracks:

```text
highest-priority tasks
blocked tasks
today's action
weekly plan
file generation tasks
baseline assessment tasks
skill practice tasks
project tasks
resume/GitHub tasks
job search tasks
task status
task priority
update prompts
```

Current truth:

```text
The candidate is still in setup/progress-file generation phase.
The next task is SESSION_LOG.md.
Actual baseline assessment has not started yet.
No learning module should be marked complete until there is score evidence.
```

Final rule:

```text
Always do the next smallest evidence-producing task.
```
