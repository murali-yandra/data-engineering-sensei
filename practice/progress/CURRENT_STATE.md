# Current State

Generated: 2026-06-06

Path:

```text
data-engineering-sensei/practice/progress/CURRENT_STATE.md
```

This file is the **live progress snapshot** for Data Engineering Sensei.

It should store the candidate's current learning state from the day they started learning with AI.

This is not a resume.
This is not a motivational journal.
This is not a final profile.

This is the current operating memory for the AI mentor.

It should answer:

```text
Where is the candidate right now?
What has the candidate already generated?
What has the candidate already learned?
What is currently in progress?
What is blocked?
What should the next AI session continue from?
What files contain long-term user details?
What files should be updated after this file changes?
```

Current status:

```text
Initial CURRENT_STATE.md created.
This file is currently filled with prompts, templates, and instructions for how to store progress.
Actual progress should be added by the AI mentor after each learning session.
```

Important rule:

```text
Update this file at the end of every meaningful AI learning session.
```


## 1. Purpose Of This File

The purpose of `CURRENT_STATE.md` is to store the candidate's **active learning state**.

It should help any AI mentor continue from the last session without asking the same questions again.

This file should store:

```text
current roadmap phase
current active topic
current skill scores
current open weaknesses
current completed files
current generated artifacts
current project status
current mock interview status
current next action
current blockers
current session summary
```

This file should not replace:

```text
CANDIDATE_PROFILE.md
ROADMAP_PROGRESS.md
NEXT_STEPS.md
mock interview feedback files
resume files
project README files
```

Use this file as the quick-start state before a learning session.

The AI mentor should read this file and know:

```text
what to continue
what not to repeat
what to test next
what weakness to repair
which progress file to update
```


## 2. Current State vs Other Progress Files

Use this map to avoid storing the same information everywhere.

| File | Purpose | Store Here? |
|---|---|---|
| `practice/progress/CANDIDATE_PROFILE.md` | Long-term candidate profile, goals, skills, strengths, risks, target roles | Stable user details |
| `practice/progress/CURRENT_STATE.md` | Live current progress snapshot | Current session state |
| `practice/progress/ROADMAP_PROGRESS.md` | Roadmap milestone completion tracking | Topic/module progress |
| `practice/progress/NEXT_STEPS.md` | Immediate task queue | Actionable next tasks |
| `practice/progress/MOCK_INTERVIEW_HISTORY.md` | Mock interview scores and feedback | Mock history |
| `practice/progress/WEAKNESS_REGISTER.md` | Weaknesses, severity, repair plans | Deep weakness tracking |
| `practice/progress/SESSION_LOG.md` | Chronological session notes | Detailed session-by-session log |
| `practice/progress/PROJECT_PROGRESS.md` | Project milestones and evidence | Project-specific state |
| `practice/progress/JOB_SEARCH_STATE.md` | Applications, referrals, interview pipeline | Job search status |
| `practice/progress/RESUME_STATE.md` | Resume bullets and evidence | Resume readiness |
| `practice/progress/GITHUB_PORTFOLIO_STATE.md` | GitHub project/readme/profile readiness | Portfolio readiness |

Current file responsibility:

```text
CURRENT_STATE.md should summarize the latest state and point to the detailed file where deeper information lives.
```

Example:

```text
Current weakness:
Window functions are weak.

Detailed tracking:
See practice/progress/WEAKNESS_REGISTER.md

Current next action:
Practice 10 window function problems.

Detailed task:
See practice/progress/NEXT_STEPS.md
```


## 3. AI Mentor Update Rule

At the end of every meaningful learning session, the AI mentor should update this file.

Meaningful session examples:

```text
completed a SQL drill
completed a Python drill
completed a DSA pattern
completed a system design case
generated a new guide file
updated resume/project profile
finished a mock interview
created a roadmap
discovered a weakness
repaired a weakness
made a job-search decision
```

Do not update for:

```text
small casual questions
one-line definitions
temporary unrelated questions
non-career chat
```

End-of-session update prompt:

```text
Update CURRENT_STATE.md with:
1. today's date
2. session topic
3. what was completed
4. what was learned
5. current score if tested
6. active weakness discovered
7. next recommended action
8. files created or changed
9. which progress file should also be updated
```


## 4. What To Store In CURRENT_STATE.md

Store only active, current, useful information.

Store:

```text
current learning phase
current topic
current active mode
latest completed session
latest score
latest weakness
current blocker
next action
active project focus
latest generated files
latest practice files completed
current interview readiness snapshot
current resume/GitHub/LinkedIn readiness
current job search readiness
```

Do not store:

```text
passwords
API keys
private tokens
exact sensitive personal details
temporary emotions
random unrelated facts
unverified claims
old details that are no longer useful
large duplicate notes already stored elsewhere
```

Use this file to make the next AI session efficient:

```text
When the candidate says "continue", the mentor should use CURRENT_STATE.md first.
```


## 5. Current Learning Start Record

Use this section to record when the candidate started structured AI learning.

```yaml
ai_learning_started_on: "YYYY-MM-DD"
skill_name: "Data Engineering Sensei"
current_phase: "initial skill/repo construction"
current_focus: "building skill files and progress tracking structure"
mentor_style: "strict, job-focused, no sugarcoating"
primary_goal: "become interview-ready for Data Engineering roles"
target_level: "strong junior to early mid-level"
```

Prompt to update this section:

```text
AI mentor, update the learning start record if the candidate gives a real start date or changes the main goal.
Do not invent dates.
If unknown, keep YYYY-MM-DD.
```


## 6. Current Active Snapshot

This section should always show the latest active state.

```yaml
last_updated: "YYYY-MM-DD"
current_mode: "repo-generation / roadmap / SQL drill / Python drill / DSA drill / system-design / mock-interview / project-deep-dive / resume-review"
current_topic: "Update this"
current_module: "Update this"
current_file_being_worked_on: "Update this"
latest_completed_file: "Update this"
latest_completed_session: "Update this"
current_blocker: "None / Update this"
next_best_action: "Update this"
```

Prompt to update:

```text
AI mentor, replace this active snapshot with the latest true state.
Keep it short.
Detailed logs should go into SESSION_LOG.md.
```


## 7. Current Repo Generation State

This section tracks which Data Engineering Sensei files have been generated.

Current known generated files:

```text
SKILL.md
README.md
CONTRIBUTING.md
CHANGELOG.md
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
practice/progress/CANDIDATE_PROFILE.md
practice/progress/CURRENT_STATE.md
```

Known path correction:

```text
api-processing.md should be under:
practice/python/api-processing.md

Not under:
practice/dsa/api-processing.md
```

Prompt to update:

```text
When a new file is generated, add it to this list.
When a wrong path is found, add a path correction note.
When a file is regenerated or replaced, mark it with the latest generated date.
```


## 8. Current Generated ZIP State

Use this to track latest ZIP artifact generated by AI.

```yaml
latest_zip_name: "data-engineering-sensei-with-current-state.zip"
latest_zip_contains_up_to: "practice/progress/CURRENT_STATE.md"
previous_zip_name: "data-engineering-sensei-with-candidate-profile.zip"
artifact_location_note: "Generated in ChatGPT sandbox during file creation session"
```

Prompt to update:

```text
AI mentor, when a new ZIP is generated, update latest_zip_name, latest_zip_contains_up_to, and previous_zip_name.
```

Important:

```text
The ZIP file is an artifact delivery format.
The repository source of truth should be the actual folder/file structure after user downloads or commits it.
```


## 9. Current Roadmap State

This is a short summary only.

Detailed roadmap tracking should live in:

```text
practice/progress/ROADMAP_PROGRESS.md
```

Current roadmap phase:

```text
Phase 0:
Build Data Engineering Sensei skill/repo structure.

Phase 1:
Profile assessment and baseline scoring.

Phase 2:
SQL + Python + DE fundamentals strengthening.

Phase 3:
System design and project deep dive.

Phase 4:
Mock interviews and weakness repair.

Phase 5:
Resume/GitHub/LinkedIn/job application execution.
```

Current phase status:

```yaml
phase_0_repo_generation: "in_progress"
phase_1_profile_assessment: "not_started"
phase_2_core_skills: "not_started"
phase_3_system_design_project: "not_started"
phase_4_mock_interviews: "not_started"
phase_5_job_applications: "not_started"
```

Prompt to update:

```text
When a roadmap phase changes, update this summary and also update ROADMAP_PROGRESS.md.
```


## 10. Current Skill Scores Snapshot

This is a short score snapshot.

Detailed score history should live in:

```text
practice/progress/CANDIDATE_PROFILE.md
practice/progress/MOCK_INTERVIEW_HISTORY.md
practice/progress/ROADMAP_PROGRESS.md
```

Use 0 to 5 scale:

```text
0 = not assessed
1 = beginner
2 = basic
3 = usable with support
4 = interview-ready
5 = strong
```

Current scores:

| Area | Current Score | Last Assessed | Evidence |
|---|---:|---|---|
| SQL | 0 | Not assessed | Needs baseline |
| Python | 0 | Not assessed | Needs baseline |
| DSA | 0 | Not assessed | Needs baseline |
| Data Engineering Fundamentals | 0 | Not assessed | Needs baseline |
| Data Modeling | 0 | Not assessed | Needs baseline |
| System Design | 0 | Not assessed | Needs baseline |
| Project Deep Dive | 0 | Not assessed | Needs baseline |
| Resume Readiness | 0 | Not assessed | Needs baseline |
| Communication | 0 | Not assessed | Needs baseline |

Prompt to update:

```text
After every assessment or mock interview:
1. update the score
2. add last assessed date
3. add evidence
4. update weakness if score is below target
```


## 11. Current Active Weaknesses Snapshot

This is a short active weakness snapshot.

Detailed weakness tracking should live in:

```text
practice/progress/WEAKNESS_REGISTER.md
practice/progress/CANDIDATE_PROFILE.md
```

Current active weaknesses:

| Area | Weakness | Severity | Current Repair Action | Status |
|---|---|---|---|---|
| SQL | Not baselined yet | Unknown | Run SQL assessment | Open |
| Python | Not baselined yet | Unknown | Run Python assessment | Open |
| DSA | Not baselined yet | Unknown | Run DSA pattern assessment | Open |
| System Design | Not baselined yet | Unknown | Run batch pipeline mock | Open |
| Project Deep Dive | Not baselined yet | Unknown | Run finance tracker deep dive | Open |
| Communication | Not baselined yet | Unknown | Run mock explanation | Open |

Prompt to update:

```text
When a weakness is discovered, add it here only if it is actively blocking current progress.
For full details, update WEAKNESS_REGISTER.md.
When repaired, mark it as repaired and remove from active list only after retest.
```


## 12. Current Next Steps Snapshot

This is the short task queue.

Detailed task tracking should live in:

```text
practice/progress/NEXT_STEPS.md
```

Current recommended next steps:

```text
1. Generate remaining progress files:
   - ROADMAP_PROGRESS.md
   - NEXT_STEPS.md
   - MOCK_INTERVIEW_HISTORY.md
   - WEAKNESS_REGISTER.md
   - SESSION_LOG.md
   - PROJECT_PROGRESS.md

2. Run baseline profile assessment.

3. Run SQL baseline assessment.

4. Run Python baseline assessment.

5. Run first system design mock:
   - batch pipeline

6. Start project deep dive for Personal Finance Tracking Platform.

7. Convert project evidence into resume bullets.
```

Prompt to update:

```text
After each session, write only 3 to 7 immediate next actions here.
Move detailed task planning to NEXT_STEPS.md.
```


## 13. Current Session Log Summary

This section should contain only the latest few sessions.

Full session history should live in:

```text
practice/progress/SESSION_LOG.md
```

Latest sessions:

| Date | Session Type | Completed | Result | Next Action |
|---|---|---|---|---|
| YYYY-MM-DD | Repo generation | Created CURRENT_STATE.md | Progress tracking file added | Generate ROADMAP_PROGRESS.md |
| YYYY-MM-DD | Repo generation | Created CANDIDATE_PROFILE.md | Candidate profile template added | Start baseline assessment |

Prompt to update:

```text
Add the latest session here.
Keep only the latest 5 to 10 rows.
Move full details to SESSION_LOG.md.
```


## 14. What To Store After Each AI Learning Session

After every AI learning session, store these details:

```text
date
topic
mode
files used
files created/changed
concepts learned
problems solved
score if assessed
mistakes made
weaknesses discovered
feedback received
next action
progress file updates needed
```

Session update template:

```text
## Session Update

Date:
Mode:
Topic:
Started from:
Completed:
Files touched:
Score:
What improved:
Mistakes:
Weakness added:
Next action:
Progress files to update:
```

Example:

```text
Date:
2026-06-06

Mode:
system-design

Topic:
batch pipeline

Completed:
Mock interview attempt 1

Score:
2.5/5

What improved:
Candidate understood raw/staging/curated layers.

Mistakes:
Missed idempotency, late data, and monitoring.

Weakness added:
System design reliability patterns.

Next action:
Practice batch-pipeline.md sections on idempotency and backfills.

Progress files to update:
CURRENT_STATE.md
WEAKNESS_REGISTER.md
MOCK_INTERVIEW_HISTORY.md
NEXT_STEPS.md
```


## 15. Prompt: Continue From Current State

Use this prompt at the beginning of a new AI session:

```text
You are my Data Engineering Sensei mentor.

Read my CURRENT_STATE.md first.
Then continue from my latest active state.

Do not restart from basics unless the current state says I need it.
Tell me:
1. where I currently am
2. what I completed last
3. what my active weakness is
4. what I should do next
5. which file should be updated after this session

Then start the next drill or lesson.
Be strict and job-focused.
```


## 16. Prompt: End Session And Update Progress

Use this prompt at the end of a session:

```text
Update my Data Engineering Sensei progress.

Update CURRENT_STATE.md with:
1. date
2. session mode
3. topic
4. what was completed
5. score if any
6. concepts learned
7. weaknesses found
8. next action
9. files created/updated
10. other progress files that should also be updated

Also tell me whether ROADMAP_PROGRESS.md, NEXT_STEPS.md, MOCK_INTERVIEW_HISTORY.md, WEAKNESS_REGISTER.md, or CANDIDATE_PROFILE.md should be updated.
```


## 17. Prompt: Store New Learning Progress

Use this when the candidate learns a concept:

```text
Store this learning progress in CURRENT_STATE.md.

Concept learned:
<concept>

Evidence:
<problem solved / explanation given / file completed>

Current confidence:
<0-5>

Still weak in:
<weakness>

Next practice:
<specific drill>

Also tell me if this should update ROADMAP_PROGRESS.md or WEAKNESS_REGISTER.md.
```

Example:

```text
Concept learned:
SQL window functions: ROW_NUMBER, RANK, SUM OVER.

Evidence:
Solved 5 top-N-per-group problems.

Current confidence:
3/5

Still weak in:
gaps and islands.

Next practice:
practice/sql/gaps-and-islands.md
```


## 18. Prompt: Store File Generation Progress

Use this when a new skill file is generated:

```text
Update CURRENT_STATE.md because a new file was generated.

File path:
<data-engineering-sensei/...>

Purpose:
<why this file exists>

Status:
generated / updated / corrected path / replaced

Related files:
<other files connected to this>

Next file to generate:
<next file>
```

Example:

```text
File path:
data-engineering-sensei/practice/system-design/reporting-pipeline.md

Purpose:
System design practice for reporting pipelines.

Status:
generated

Related files:
batch-pipeline.md
data-warehouse.md
data-quality-framework.md

Next file to generate:
practice/progress/CANDIDATE_PROFILE.md
```


## 19. Prompt: Store Mock Interview Progress

Use this after every mock interview:

```text
Store this mock interview result.

Mode:
SQL / Python / DSA / System Design / Project Deep Dive / Behavioral

Topic:
<topic>

Score:
<0-5>

Pass/Fail:
<pass or fail>

What was good:
<points>

What was missing:
<points>

Main weakness:
<weakness>

Repair drill:
<specific file/section/problem set>

Retest date:
<date>

Update:
CURRENT_STATE.md
MOCK_INTERVIEW_HISTORY.md
WEAKNESS_REGISTER.md
NEXT_STEPS.md
```


## 20. Prompt: Store Project Progress

Use this when project progress changes:

```text
Update my current state for project progress.

Project:
<project name>

Completed:
<what changed>

Technical evidence:
<commit/file/API/schema/test>

Interview value:
<how this helps job interviews>

Resume value:
<possible bullet>

Current blocker:
<blocker if any>

Next project task:
<task>

Update:
CURRENT_STATE.md
PROJECT_PROGRESS.md
RESUME_STATE.md if resume evidence was created
```


## 21. Prompt: Store Resume/GitHub/LinkedIn Progress

Use this when career assets change:

```text
Update my current state for career asset progress.

Asset:
Resume / GitHub / LinkedIn / Portfolio

Completed:
<what was improved>

Evidence:
<link/file/section>

Current readiness score:
<0-5>

Remaining gap:
<gap>

Next action:
<action>

Update:
CURRENT_STATE.md
RESUME_STATE.md or GITHUB_PORTFOLIO_STATE.md or JOB_SEARCH_STATE.md
```


## 22. Prompt: Store Weakness Repair Progress

Use this when working on a weakness:

```text
Update weakness repair progress.

Weakness:
<weakness>

Old score:
<score>

Repair work completed:
<drills/problems/session>

Retest result:
<score or pending>

Status:
open / improving / repaired / needs retest

Next action:
<action>

Update:
CURRENT_STATE.md
WEAKNESS_REGISTER.md
NEXT_STEPS.md
```

Rule:

```text
Do not mark a weakness repaired without retest evidence.
```


## 23. Prompt: Store Job Search Progress

Use this when job search starts.

```text
Update my job search current state.

Target role:
<role>

Target location:
<location>

Company/type:
<company or type>

Application status:
not applied / applied / referral requested / recruiter call / interview / rejected / offer

Resume version:
<version>

Notes:
<important notes>

Next action:
<action>

Update:
CURRENT_STATE.md
JOB_SEARCH_STATE.md
NEXT_STEPS.md
```

Current job search state:

```text
Not active yet.
Preparation and portfolio building are still priority.
```


## 24. Current File Dependency Map

When CURRENT_STATE.md changes, check if these files also need updates.

| Trigger | Also Update |
|---|---|
| Candidate goal changes | CANDIDATE_PROFILE.md |
| Current score changes | CANDIDATE_PROFILE.md, ROADMAP_PROGRESS.md |
| Roadmap phase changes | ROADMAP_PROGRESS.md |
| New immediate task appears | NEXT_STEPS.md |
| Mock interview completed | MOCK_INTERVIEW_HISTORY.md, WEAKNESS_REGISTER.md |
| Weakness discovered | WEAKNESS_REGISTER.md, NEXT_STEPS.md |
| Weakness repaired | WEAKNESS_REGISTER.md, ROADMAP_PROGRESS.md |
| Project milestone completed | PROJECT_PROGRESS.md, RESUME_STATE.md |
| Resume bullet created | RESUME_STATE.md |
| GitHub repo improved | GITHUB_PORTFOLIO_STATE.md |
| Job application sent | JOB_SEARCH_STATE.md |
| New guide file generated | CURRENT_STATE.md, ROADMAP_PROGRESS.md |
| New session completed | SESSION_LOG.md |

Prompt:

```text
AI mentor, after updating CURRENT_STATE.md, tell me exactly which other progress files need updates and why.
```


## 25. Current Topic Focus

Current topic focus:

```yaml
primary_focus: "building Data Engineering Sensei skill repository"
secondary_focus: "progress tracking system"
next_learning_focus: "baseline assessment after progress files are complete"
```

Active system design files recently generated:

```text
batch-pipeline.md
cdc-pipeline.md
data-lake.md
data-quality-framework.md
data-warehouse.md
event-ingestion.md
realtime-pipeline.md
reporting-pipeline.md
```

Active progress files recently generated:

```text
CANDIDATE_PROFILE.md
CURRENT_STATE.md
```

Prompt to update:

```text
When the candidate switches from repo generation to learning/practice, update primary_focus and next_learning_focus.
```


## 26. Current Baseline Assessment Status

Baseline assessment status:

| Assessment | Status | Score | Next Action |
|---|---|---:|---|
| Profile assessment | Not started | 0 | Run profile assessment mode |
| SQL baseline | Not started | 0 | Run SQL drill mode |
| Python baseline | Not started | 0 | Run Python drill mode |
| DSA baseline | Not started | 0 | Run DSA drill mode |
| DE fundamentals | Not started | 0 | Run fundamentals mode |
| System design baseline | Not started | 0 | Run batch pipeline mock |
| Project deep dive | Not started | 0 | Run project deep dive mode |
| Communication baseline | Not started | 0 | Run interview mode |

Prompt to update:

```text
After each baseline assessment, update the status, score, and next action.
Also update CANDIDATE_PROFILE.md and ROADMAP_PROGRESS.md.
```


## 27. Current Learning Evidence

Use this section to store short evidence only.

Detailed evidence should go into:

```text
practice/progress/PROJECT_PROGRESS.md
practice/progress/RESUME_STATE.md
practice/progress/SESSION_LOG.md
```

Current evidence:

```text
Built/generated a large Data Engineering Sensei skill structure.
Generated multiple system design guides.
Generated DSA, SQL, Python, and mode files.
Generated candidate profile progress file.
Currently generating live progress tracking file.
```

Evidence to collect next:

```text
SQL drill scores
Python drill outputs
DSA solved problems
system design mock scores
project architecture diagram
finance tracker README
resume bullets
GitHub commits
mock interview feedback
```

Prompt to update:

```text
Add only strong evidence here.
Do not add vague claims like "learned SQL" without proof.
```


## 28. Current Interview Readiness Summary

Current interview readiness:

```text
Not yet interview-ready.
The skill repository and tracking system are still being built.
Baseline assessments have not yet been completed.
```

Current strongest readiness areas:

```text
learning consistency
project-building intention
data engineering role clarity
repo/skill structure creation
```

Current weakest readiness areas:

```text
not yet assessed
mock interview evidence missing
resume evidence not finalized
project deep-dive not tested
SQL/Python/DSA scores not known
system design delivery not tested
```

Next readiness move:

```text
complete progress tracking files, then run baseline assessment.
```


## 29. Current Communication State

Communication status:

```text
Not yet formally assessed.
```

Known desired mentor style:

```text
strict
clear
practical
job-focused
no sugarcoating
visual where useful
structured with tables/checklists
```

Communication behaviors to train:

```text
answer in frameworks
clarify requirements first
avoid tool-only answers
define grain in data questions
explain trade-offs
summarize clearly
use evidence
```

Prompt to update:

```text
After each mock interview, update this section with communication score and recurring issues.
```


## 30. Current Project State

Detailed project tracking should live in:

```text
practice/progress/PROJECT_PROGRESS.md
```

Current main project:

```text
Personal Finance Tracking Platform
```

Known current project details:

```text
FastAPI
PostgreSQL
SQLModel
Alembic
Docker
GitHub Actions
Ollama
Telegram Bot API
SMS-based transaction ingestion
merchant normalization
categorization
account reconciliation
Telegram corrections
AI-assisted transaction categorization
```

Current project status:

```text
Sprint 0 completed.
Sprint 1 authentication/user management in progress.
Project deep-dive not yet tested.
```

Next project action:

```text
Run project-deep-dive-mode on Personal Finance Tracking Platform.
Create architecture explanation.
Create resume bullets with evidence.
```


## 31. Current Resume/GitHub/LinkedIn State

Detailed files should be:

```text
practice/progress/RESUME_STATE.md
practice/progress/GITHUB_PORTFOLIO_STATE.md
practice/progress/JOB_SEARCH_STATE.md
```

Current resume state:

```text
Needs evidence-driven bullets.
Needs project impact and measurable details.
```

Current GitHub state:

```text
Data Engineering Sensei repo/skill structure is being generated.
Finance tracker project should be made portfolio-ready.
Profile README/bio has been discussed previously.
```

Current LinkedIn state:

```text
Needs clear data engineering positioning and project proof.
```

Next action:

```text
After baseline and project deep dive, update resume bullets and GitHub README.
```


## 32. Current Job Search State

Current job search status:

```text
Preparation phase.
Not recommended to aggressively apply yet.
```

Current target roles:

```text
Data Engineer
Analytics Engineer
ETL Developer
Cloud Data Engineer
BI/Data Warehouse Engineer
```

Current target markets:

```text
India first
remote later
international after stronger proof
```

Job search gate:

```text
Start serious applications after:
SQL >= 4/5
Python >= 3.5/5
System design >= 3.5/5
Project deep dive >= 4/5
Resume >= 4/5
GitHub portfolio presentable
```

Prompt to update:

```text
When the candidate starts applying, update CURRENT_STATE.md and JOB_SEARCH_STATE.md.
```


## 33. Current Open Decisions

Use this section for decisions not finalized yet.

Current open decisions:

| Decision | Options | Current Leaning | Needed Evidence |
|---|---|---|---|
| First interview focus | SQL / Python / System Design | SQL + Python baseline first | Baseline scores |
| Main project for resume | Finance tracker / other | Finance tracker | Project readiness review |
| Target role priority | DE / AE / ETL | Data Engineer | Resume and skills |
| Cloud platform focus | GCP / AWS / Azure | Not decided | Job target analysis |
| DSA depth | light / medium / heavy | medium-light for DE | Interview target |

Prompt to update:

```text
When a decision is made, record the decision, reason, and date.
```


## 34. Current Blockers

Current blockers:

```text
baseline scores missing
progress files not fully generated
project deep-dive not tested
resume evidence not finalized
GitHub portfolio not fully packaged
mock interview history empty
```

Blocker update template:

```text
Blocker:
Why it blocks progress:
Severity:
Owner:
Next action:
Due date:
Status:
```

Prompt to update:

```text
Keep only active blockers here.
Move resolved blockers to SESSION_LOG.md or ROADMAP_PROGRESS.md.
```


## 35. Current Recommended Next File Generation Order

Recommended next progress files:

```text
1. ROADMAP_PROGRESS.md
2. NEXT_STEPS.md
3. SESSION_LOG.md
4. WEAKNESS_REGISTER.md
5. MOCK_INTERVIEW_HISTORY.md
6. PROJECT_PROGRESS.md
7. RESUME_STATE.md
8. GITHUB_PORTFOLIO_STATE.md
9. JOB_SEARCH_STATE.md
```

Why:

```text
ROADMAP_PROGRESS.md tracks long-term module completion.
NEXT_STEPS.md gives immediate task queue.
SESSION_LOG.md stores full chronological learning history.
WEAKNESS_REGISTER.md stores repair work.
MOCK_INTERVIEW_HISTORY.md stores scores and feedback.
PROJECT_PROGRESS.md stores portfolio evidence.
RESUME_STATE.md turns evidence into bullets.
GITHUB_PORTFOLIO_STATE.md tracks portfolio readiness.
JOB_SEARCH_STATE.md starts when applications begin.
```

Prompt:

```text
Continue generating the next progress file in this order unless the candidate asks for a different file.
```


## 36. Current State Update Checklist

Before saving an update to CURRENT_STATE.md, check:

```text
Is the update current?
Is it useful for the next AI session?
Is it short enough?
Is detailed information stored in the right file?
Does it avoid sensitive/private data?
Does it mention the next action?
Does it mention the related progress files?
Does it remove outdated state?
```

After saving, answer:

```text
Updated CURRENT_STATE.md.
Also update:
- <file>: <reason>
Next action:
- <action>
```


## 37. Current State Compact Summary

This section should be easy to read quickly.

```text
Current phase:
Building Data Engineering Sensei skill/repo and progress tracking system.

Latest completed:
CANDIDATE_PROFILE.md generated.

Current file:
CURRENT_STATE.md generated as live progress tracker.

Current skill status:
No baseline assessments completed yet.

Current project:
Personal Finance Tracking Platform is main portfolio project but not yet deep-dive tested.

Current next action:
Generate ROADMAP_PROGRESS.md and NEXT_STEPS.md, then run baseline assessment.

Current warning:
Do not start aggressive job applications until scores and portfolio evidence improve.
```

Prompt to update:

```text
Always keep this compact summary updated.
This should be the fastest section for an AI mentor to read.
```


## 38. Machine-Readable Current State

Use this YAML-style block for AI parsing.

```yaml
current_state_version: "1.0"
last_updated: "YYYY-MM-DD"
skill_name: "Data Engineering Sensei"
current_phase: "repo_generation"
current_focus: "progress_tracking_files"
latest_completed:
  - "practice/progress/CANDIDATE_PROFILE.md"
  - "practice/progress/CURRENT_STATE.md"
active_file: "practice/progress/CURRENT_STATE.md"
next_files:
  - "practice/progress/ROADMAP_PROGRESS.md"
  - "practice/progress/NEXT_STEPS.md"
  - "practice/progress/SESSION_LOG.md"
baseline_assessments:
  sql: "not_started"
  python: "not_started"
  dsa: "not_started"
  fundamentals: "not_started"
  system_design: "not_started"
  project_deep_dive: "not_started"
main_project: "Personal Finance Tracking Platform"
job_search_status: "preparation"
active_blockers:
  - "baseline scores missing"
  - "mock history empty"
  - "project deep dive not tested"
next_best_action: "Generate ROADMAP_PROGRESS.md, then NEXT_STEPS.md, then run baseline assessment."
related_progress_files:
  candidate_profile: "practice/progress/CANDIDATE_PROFILE.md"
  current_state: "practice/progress/CURRENT_STATE.md"
  roadmap_progress: "practice/progress/ROADMAP_PROGRESS.md"
  next_steps: "practice/progress/NEXT_STEPS.md"
  session_log: "practice/progress/SESSION_LOG.md"
  weakness_register: "practice/progress/WEAKNESS_REGISTER.md"
  mock_interview_history: "practice/progress/MOCK_INTERVIEW_HISTORY.md"
```

Prompt to update:

```text
AI mentor, keep this YAML block synchronized with the human-readable sections.
```


## 39. Final Instruction For AI Mentor

When using this file, the AI mentor must:

```text
1. Read compact summary.
2. Read machine-readable current state.
3. Check active blockers.
4. Check current next steps.
5. Continue from the latest active file or topic.
6. Avoid repeating completed generation.
7. Update this file after meaningful progress.
8. Tell the candidate which related progress files need updates.
```

The mentor must not:

```text
treat this file as final truth forever
store unnecessary sensitive details
duplicate full content from other progress files
skip baseline assessments
skip weakness repair
jump to job applications too early
```

Core rule:

```text
CURRENT_STATE.md is the active control panel for the candidate's learning journey.
```


## 40. Final Summary

This file stores the candidate's current AI-learning state for Data Engineering Sensei.

It should always make the next session easier.

It stores:

```text
current phase
current focus
latest completed work
current generated files
current scores
current weaknesses
current blockers
current next steps
current related progress files
current project/job readiness summary
prompts for updating progress
```

It points to other files for details:

```text
CANDIDATE_PROFILE.md:
long-term candidate profile

ROADMAP_PROGRESS.md:
module completion

NEXT_STEPS.md:
immediate tasks

SESSION_LOG.md:
full session history

WEAKNESS_REGISTER.md:
weakness repair

MOCK_INTERVIEW_HISTORY.md:
mock scores

PROJECT_PROGRESS.md:
portfolio evidence

RESUME_STATE.md:
resume bullets and readiness

GITHUB_PORTFOLIO_STATE.md:
GitHub portfolio status

JOB_SEARCH_STATE.md:
applications and interview pipeline
```

Final rule:

```text
Every time the candidate learns, practices, builds, gets feedback, or changes direction, CURRENT_STATE.md should be updated first, then the relevant detailed progress file should be updated.
```
