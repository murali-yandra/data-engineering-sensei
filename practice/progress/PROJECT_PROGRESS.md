# Project Progress

Generated: 2026-06-06

Path:

```text
data-engineering-sensei/practice/progress/PROJECT_PROGRESS.md
```

This file tracks **project evidence and project interview readiness** for Data Engineering Sensei.

Primary project:

```text
Personal Finance Tracking Platform
```

This file should help the candidate turn project work into:

```text
interview answers
resume bullets
GitHub README improvements
architecture explanations
system design examples
portfolio proof
job application evidence
```

Current status:

```text
Initial PROJECT_PROGRESS.md generated.
Project deep-dive assessment has not started yet.
Known project details are recorded as starting context.
```

Core rule:

```text
A project is interview-ready only when the candidate can explain problem, architecture, data model, trade-offs, failures, testing, and impact.
```


## 1. Purpose

`PROJECT_PROGRESS.md` exists to track project work as interview evidence.

It should store:

```text
project goals
features
architecture
tech stack
data model
pipeline flow
API design
data quality
security
testing
deployment
CI/CD
known gaps
resume bullets
GitHub README status
mock interview scores
```

Use this file when:

```text
candidate completes a project milestone
candidate prepares project deep dive
candidate improves README
candidate creates resume bullets
candidate adds architecture diagram
candidate receives project feedback
candidate needs proof for applications
```

Strict rule:

```text
Do not claim project strength without evidence.
```


## 2. Relationship With Other Progress Files

| File | How it connects |
|---|---|
| `CURRENT_STATE.md` | summarizes active project state |
| `ROADMAP_PROGRESS.md` | tracks project deep-dive phase completion |
| `NEXT_STEPS.md` | stores next project tasks |
| `SESSION_LOG.md` | records project sessions |
| `WEAKNESS_REGISTER.md` | stores project explanation weaknesses |
| `RESUME_STATE.md` | converts project evidence into resume bullets |
| `GITHUB_PORTFOLIO_STATE.md` | tracks README/repo/demo readiness |
| `MOCK_INTERVIEW_HISTORY.md` | stores project mock scores |

Update rule:

```text
If project evidence improves, update PROJECT_PROGRESS.md.
If it affects resume, update RESUME_STATE.md.
If it affects GitHub, update GITHUB_PORTFOLIO_STATE.md.
If it reveals weakness, update WEAKNESS_REGISTER.md.
```


## 3. Main Project Snapshot

```yaml
project_name: "Personal Finance Tracking Platform"
project_type: "Data engineering / backend data product"
status: "Sprint 0 completed, Sprint 1 authentication/user management in progress"
interview_readiness_score: 0
github_readiness_score: 0
resume_readiness_score: 0
deep_dive_status: "not_started"
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
SMS-based transaction ingestion
automated expense tracking
merchant learning engine
merchant normalization
transaction categorization
account and balance reconciliation
Telegram bot notifications and corrections
AI-assisted categorization
user-feedback learning engine
authentication/user management in progress
```

Current project positioning:

```text
A personal finance data platform that ingests transaction messages, normalizes merchants, categorizes expenses, reconciles accounts, and supports user corrections through Telegram and AI-assisted workflows.
```


## 4. Project Interview Pitch

Current draft pitch:

```text
I am building a personal finance tracking platform that ingests transaction messages, normalizes merchant names, categorizes expenses, reconciles balances across accounts, and lets users correct transactions through a Telegram bot. The backend uses FastAPI, PostgreSQL, SQLModel, Alembic, Docker, GitHub Actions, and an AI-assisted categorization flow using Ollama.
```

Pitch improvement checklist:

```text
clear problem
clear user
clear data flow
clear technical ownership
clear business value
clear measurable impact
```

2-minute pitch template:

```text
Problem:
What user pain does it solve?

Solution:
What did I build?

Architecture:
How data moves through the system.

Technical depth:
Key design decisions and trade-offs.

Impact:
What it improves or proves.

Next:
What I am adding next.
```

Task:

```text
Run project deep dive and score the 2-minute pitch.
```


## 5. Project Requirements

Functional requirements to document:

```text
ingest SMS transaction data
parse transaction fields
normalize merchant names
categorize transactions
track accounts and balances
reconcile transactions against account balances
allow user corrections
send Telegram notifications
learn from user feedback
support authentication and user management
provide transaction history and summaries
```

Non-functional requirements to document:

```text
data correctness
idempotent ingestion
security and authentication
PII protection
auditability
error handling
logging
database migrations
deployment reproducibility
CI/CD checks
scalability for multiple users
```

Prompt:

```text
Ask me requirements questions for my finance tracker project one by one.
Convert my answers into functional and non-functional requirements.
```


## 6. Architecture Tracker

Current architecture needs to be explained clearly.

Expected architecture flow:

```text
SMS / transaction source
    ↓
ingestion/parsing layer
    ↓
FastAPI backend
    ↓
PostgreSQL database
    ↓
merchant normalization + categorization
    ↓
account/balance reconciliation
    ↓
Telegram bot notifications/corrections
    ↓
feedback learning loop
    ↓
reporting/insights layer
```

Architecture questions to answer:

```text
Where does transaction data come from?
How is duplicate ingestion avoided?
How are merchants normalized?
How are categories assigned?
How are user corrections stored?
How does feedback improve future categorization?
How is account reconciliation handled?
How does Telegram integrate?
How are migrations handled?
How is the app deployed?
How are errors logged?
```

Evidence needed:

```text
architecture diagram
README architecture section
API flow examples
database schema
sample transaction flow
```


## 7. Data Model Tracker

Database entities to confirm:

```text
users
accounts
transactions
merchants
merchant_aliases
categories
transaction_categories
classification_feedback
balance_snapshots
telegram_users
audit_logs
```

Data model questions:

```text
What is the primary key for transactions?
How are duplicate transactions detected?
How is merchant alias linked to canonical merchant?
How are categories stored?
How is feedback stored?
How are accounts connected to users?
How are balances reconciled?
What fields are sensitive?
What tables need audit columns?
```

Data model evidence checklist:

```text
ERD or text schema
table purpose descriptions
primary keys and foreign keys
unique constraints
indexes
migration files
sample rows
```

Current status:

```text
not reviewed
```


## 8. Data Pipeline Flow

Project pipeline flow should be documented.

Possible flow:

```text
1. Receive transaction message.
2. Parse amount, merchant, date, account, type.
3. Validate required fields.
4. Deduplicate transaction.
5. Normalize merchant.
6. Categorize transaction.
7. Save transaction.
8. Update account/balance state.
9. Send Telegram notification.
10. Accept correction from user.
11. Store feedback.
12. Improve future classification.
```

Pipeline design questions:

```text
Is ingestion batch, event-driven, or API-triggered?
What happens if parsing fails?
What happens if Telegram call fails?
What happens if categorization confidence is low?
What happens if user correction conflicts with prediction?
How are retries handled?
How are duplicate messages handled?
```

Interview target:

```text
Candidate should explain this flow clearly in under 3 minutes.
```


## 9. Feature Progress Tracker

| Feature | Status | Evidence | Interview Value |
|---|---|---|---|
| SMS transaction ingestion | in_progress / unknown | needs proof | ingestion pipeline |
| Transaction parsing | unknown | needs proof | data extraction |
| Merchant normalization | planned/known | needs proof | data cleaning |
| Categorization | planned/known | needs proof | ML/rules/data logic |
| Feedback learning | planned/known | needs proof | iterative data product |
| Account reconciliation | planned/known | needs proof | data quality |
| Telegram bot notifications | planned/known | needs proof | user interaction |
| Telegram corrections | planned/known | needs proof | feedback loop |
| Authentication/user management | in_progress | Sprint 1 | security |
| Alembic migrations | known stack | needs proof | production DB practice |
| Docker setup | known stack | needs proof | deployment |
| GitHub Actions | known stack | needs proof | CI/CD |

Status values:

```text
planned
in_progress
implemented
tested
documented
interview_ready
blocked
```


## 10. Data Quality And Reconciliation

This is a high-value interview area.

Project should explain:

```text
duplicate transaction detection
required field validation
amount/date validation
merchant normalization quality
category confidence checks
user correction audit
account balance reconciliation
missing transaction detection
failed parse quarantine
manual review queue if needed
```

Possible DQ checks:

```text
transaction amount is not null
transaction date is valid
account_id exists
merchant text exists
category exists or marked uncategorized
duplicate transaction fingerprint not already processed
balance snapshot difference explained by transactions
```

Interview line:

```text
I treated user corrections and reconciliation as data quality feedback loops, not just UI features.
```

Evidence needed:

```text
validation rules
tests
schema constraints
reconciliation logic
audit fields
example correction flow
```


## 11. Security And Privacy

The project likely handles sensitive financial data.

Security topics to explain:

```text
authentication
authorization
user-level data isolation
password/token handling
Telegram user linking
PII and financial data protection
secrets management
database access control
audit logging
input validation
```

Sensitive data examples:

```text
transaction messages
account names
merchant history
spending behavior
Telegram identifiers
user profile data
```

Interview risk:

```text
If the candidate cannot explain security, this project may look risky.
```

Required evidence:

```text
auth design
user table
access control checks
environment variables
no secrets in repo
README security note
```


## 12. Testing And CI/CD

Testing areas:

```text
unit tests for parsing
unit tests for merchant normalization
unit tests for categorization
unit tests for reconciliation
API tests
database migration tests
Telegram bot handler tests
error-handling tests
```

CI/CD areas:

```text
GitHub Actions workflow
lint/test steps
Docker build
migration check
environment configuration
```

Interview explanation:

```text
I used tests and CI/CD to make sure changes to parsing, categorization, and database schema do not break the transaction pipeline.
```

Current status:

```text
not verified
```

Task:

```text
Collect actual testing and CI/CD evidence from repo before claiming this strongly.
```


## 13. Deployment And Operations

Deployment topics to document:

```text
Docker setup
environment variables
database migrations
startup command
logging
error handling
health checks
backup strategy
monitoring plan
```

Operational failure cases:

```text
message parsing fails
database migration fails
duplicate transaction arrives
Telegram API fails
AI categorization fails
database unavailable
bad user correction
balance mismatch
```

Interview target:

```text
Candidate can explain how the system behaves when things fail.
```


## 14. Project Deep-Dive Scorecard

Use 0 to 5 scale.

| Area | Score | Status | Notes |
|---|---:|---|---|
| Problem explanation | 0 | not_tested | needs mock |
| Requirements | 0 | not_tested | needs mock |
| Architecture | 0 | not_tested | needs diagram/explanation |
| Data model | 0 | not_tested | needs schema review |
| Pipeline flow | 0 | not_tested | needs mock |
| Data quality | 0 | not_tested | needs evidence |
| Security | 0 | not_tested | needs auth explanation |
| Testing | 0 | not_tested | needs proof |
| Deployment | 0 | not_tested | needs proof |
| Trade-offs | 0 | not_tested | needs mock |
| Resume value | 0 | not_tested | needs bullets |
| GitHub readiness | 0 | not_tested | needs README review |

Pass condition:

```text
overall project deep-dive score >= 4/5
```


## 15. Resume Bullet Bank

Draft bullets must be evidence-backed.

Draft bullet 1:

```text
Built a personal finance tracking backend using FastAPI and PostgreSQL to ingest transaction data, normalize merchants, categorize expenses, and support account reconciliation workflows.
```

Draft bullet 2:

```text
Designed a merchant normalization and feedback-learning flow to improve transaction categorization using user corrections from a Telegram bot.
```

Draft bullet 3:

```text
Implemented production-style backend practices using SQLModel, Alembic migrations, Docker, and GitHub Actions for repeatable setup and database change management.
```

Evidence needed before final resume use:

```text
actual implemented status
number of APIs/tables
tests
sample transaction flow
accuracy or manual effort improvement
deployment proof
screenshots/demo
GitHub link
```

Rule:

```text
Do not add metrics unless the candidate can prove them.
```


## 16. GitHub README Checklist

Main project README should include:

```text
project overview
problem statement
features
architecture diagram
tech stack
database schema
setup instructions
environment variables example
Docker instructions
API examples
Telegram bot flow
sample transaction flow
testing instructions
migration instructions
roadmap
screenshots/demo if available
known limitations
```

Current status:

```text
not reviewed
```

Next task:

```text
Review finance tracker README and score it from 0 to 5.
```


## 17. Project Mock Interview Questions

Use these for project deep dive.

```text
1. Explain your project in 2 minutes.
2. What problem does it solve?
3. Why did you choose FastAPI?
4. Why PostgreSQL?
5. Explain your database schema.
6. How do transactions enter the system?
7. How do you detect duplicates?
8. How do you normalize merchants?
9. How does categorization work?
10. How does user feedback improve categorization?
11. How does account reconciliation work?
12. How does the Telegram bot interact with backend?
13. How do you handle failed parsing?
14. How do you handle failed Telegram messages?
15. How do you protect user financial data?
16. What tests did you write?
17. How do migrations work?
18. How would you scale this to many users?
19. What trade-offs did you make?
20. What would you improve next?
```

Mock target:

```text
Candidate should answer each with structure and evidence.
```


## 18. Project Weakness Tracker

| Weakness ID | Area | Weakness | Severity | Status | Repair |
|---|---|---|---|---|---|
| PRJ-W001 | Deep dive | Project not yet mock-tested | High | open | Run project deep dive |
| PRJ-W002 | Evidence | Metrics/evidence missing | High | open | collect project proof |
| PRJ-W003 | README | README not reviewed | Medium | open | review GitHub README |
| PRJ-W004 | Architecture | diagram/explanation not verified | Medium | open | create architecture section |
| PRJ-W005 | Security | auth/privacy explanation not tested | High | open | explain Sprint 1 auth design |

If weakness affects overall readiness:

```text
also update WEAKNESS_REGISTER.md
```


## 19. Project Milestone Plan

Recommended milestone order:

```text
1. Confirm current implemented features.
2. Write 2-minute project pitch.
3. Document architecture.
4. Document database schema.
5. Document transaction pipeline flow.
6. Document data quality and reconciliation.
7. Document security/authentication.
8. Document tests and CI/CD.
9. Improve README.
10. Create resume bullets.
11. Run project deep-dive mock.
12. Retest weak sections.
```

Immediate next project task:

```text
Run project deep-dive-mode and answer the first 5 questions.
```


## 20. Machine-Readable Project State

Keep this YAML-style block synchronized.

```yaml
project_progress_version: "1.0"
last_updated: "YYYY-MM-DD"
main_project: "Personal Finance Tracking Platform"
project_status: "sprint_1_auth_user_management_in_progress"
deep_dive_status: "not_started"
project_scores:
  problem_explanation: 0
  architecture: 0
  data_model: 0
  pipeline_flow: 0
  data_quality: 0
  security: 0
  testing: 0
  deployment: 0
  tradeoffs: 0
  resume_value: 0
  github_readiness: 0
known_stack:
  - "FastAPI"
  - "PostgreSQL"
  - "SQLModel"
  - "Alembic"
  - "Docker"
  - "GitHub Actions"
  - "Ollama"
  - "Telegram Bot API"
known_features:
  - "SMS transaction ingestion"
  - "merchant normalization"
  - "transaction categorization"
  - "account reconciliation"
  - "Telegram corrections"
  - "AI-assisted categorization"
active_project_weaknesses:
  - "project not yet mock-tested"
  - "metrics/evidence missing"
  - "README not reviewed"
next_project_action: "Run project deep dive and collect evidence."
related_files:
  current_state: "practice/progress/CURRENT_STATE.md"
  roadmap_progress: "practice/progress/ROADMAP_PROGRESS.md"
  next_steps: "practice/progress/NEXT_STEPS.md"
  weakness_register: "practice/progress/WEAKNESS_REGISTER.md"
  resume_state: "practice/progress/RESUME_STATE.md"
  github_portfolio_state: "practice/progress/GITHUB_PORTFOLIO_STATE.md"
```


## 21. Project Update Prompt

Use this prompt after project work:

```text
Update PROJECT_PROGRESS.md.

Project:
Personal Finance Tracking Platform

Completed:
<what changed>

Evidence:
<commit/file/API/schema/test/demo>

Interview value:
<how this helps interviews>

Resume value:
<possible bullet>

GitHub value:
<README/demo/setup improvement>

Weakness found:
<weakness>

Next project task:
<task>

Also update:
CURRENT_STATE.md
ROADMAP_PROGRESS.md
NEXT_STEPS.md
WEAKNESS_REGISTER.md if weakness found
RESUME_STATE.md if resume bullet created
GITHUB_PORTFOLIO_STATE.md if README/repo changed
SESSION_LOG.md
```


## 22. Final Summary

`PROJECT_PROGRESS.md` turns project work into job evidence.

It tracks:

```text
project features
architecture
data model
pipeline flow
data quality
security
testing
deployment
CI/CD
resume bullets
GitHub readiness
mock questions
weaknesses
next milestones
```

Current truth:

```text
The Personal Finance Tracking Platform is the main portfolio project.
It has useful Data Engineering interview potential.
But it is not yet deep-dive tested and needs stronger evidence.
```

Final rule:

```text
A project is valuable for interviews only if the candidate can explain and defend it clearly.
```
