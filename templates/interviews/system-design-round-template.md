# System Design Round Template

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
data-engineering-sensei/templates/interviews/system-design-round-template.md
```

Purpose:

```text
Run Data Engineering system design rounds.
Focus on requirements, architecture, data modeling, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```


## 1. System Design Mentor Master Prompt

```text
You are my Data Engineering Sensei system design interviewer.

Run a strict Data Engineering system design round.

Rules:
1. Give one design prompt.
2. Let me ask clarifying questions first.
3. Do not give the architecture before I try.
4. Force requirements-first thinking.
5. Make me define sources, consumers, SLA, scale, data model, processing, quality, monitoring, security, cost, and trade-offs.
6. Interrupt if I jump directly to tools.
7. Ask follow-ups on idempotency, backfills, late data, failures, data quality, and monitoring.
8. Score from 0 to 5.
9. Add weaknesses and repair tasks.
10. End with a corrected strong answer.
```


## 2. Scoring Rubric

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


## 3. Required System Design Framework

```text
1. Clarify business problem.
2. Identify consumers.
3. Identify sources.
4. Define SLA/freshness.
5. Estimate scale.
6. Define data contracts/schema.
7. Draw architecture.
8. Define storage layers.
9. Define data model.
10. Define processing strategy.
11. Define idempotency.
12. Define backfills/replay.
13. Define late data handling.
14. Define data quality.
15. Define monitoring/alerting.
16. Define security/PII.
17. Define cost controls.
18. Explain trade-offs.
19. Summarize.
```

Score cap:

```text
If no data quality: max 3
If no monitoring: max 3
If no idempotency: max 3.5
If no trade-offs: max 3
If tools before requirements: max 3
```


## 4. System Design Round Structure

```text
Duration:
45 to 60 minutes

0-5 min:
candidate asks clarifying questions

5-15 min:
high-level architecture

15-30 min:
deep dive into data model and processing

30-40 min:
reliability, DQ, monitoring, security, cost

40-50 min:
follow-ups and trade-offs

50-60 min:
feedback and repair plan
```


## 5. High-ROI Prompts

```text
Design a batch pipeline for daily orders.
Design a data warehouse for e-commerce.
Design a data quality framework.
Design a reporting pipeline for executive KPIs.
Design a CDC pipeline from PostgreSQL to warehouse.
Design a data lake with bronze/silver/gold.
Design event ingestion for clickstream.
Design a realtime fraud detection pipeline.
Design customer 360 pipeline.
Design finance reporting with reconciliation.
```


## 6. Batch Pipeline Cases

### Case 1: Design a daily batch pipeline from OLTP orders to warehouse.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 2: Design an incremental pipeline with late arriving records.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 3: Design a backfill-safe pipeline for 2 years of history.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```


## 7. Data Warehouse Cases

### Case 1: Design an e-commerce warehouse.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 2: Design sales reporting warehouse with facts and dimensions.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 3: Design customer 360 warehouse.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```


## 8. Data Quality Framework Cases

### Case 1: Design a DQ framework for critical tables.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 2: Design quality gates before publishing reports.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 3: Design reconciliation for finance metrics.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```


## 9. CDC Pipeline Cases

### Case 1: Design CDC from PostgreSQL to BigQuery/Snowflake.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 2: Handle inserts, updates, deletes, and schema changes.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 3: Design replay for CDC failures.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```


## 10. Data Lake Cases

### Case 1: Design bronze/silver/gold lake architecture.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 2: Design data lake file layout and partitioning.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 3: Handle schema evolution and compaction.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```


## 11. Reporting Pipeline Cases

### Case 1: Design daily sales dashboard pipeline.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 2: Design executive KPI reporting pipeline.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 3: Design partner export reporting pipeline.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```


## 12. Event And Realtime Cases

### Case 1: Design clickstream event ingestion.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 2: Design realtime dashboard pipeline.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```

### Case 3: Design realtime fraud alerting pipeline.

Mentor prompt:

```text
Design this system.
First ask clarifying questions.
Then propose architecture.
Then deep dive into data model, processing, quality, reliability, monitoring, security, cost, and trade-offs.
```

Follow-ups to ask:

```text
How do you make it idempotent?
How do you handle late data?
How do you backfill?
How do you validate output?
How do you monitor freshness?
How do you handle schema changes?
How do you control cost?
What are the trade-offs?
```

Scoring focus:

```text
requirements
architecture
data model
processing
data quality
reliability
monitoring
security
cost
trade-offs
communication
```


## 13. System Design Feedback Template

```text
System Design Feedback

Prompt:
Score:
Pass/fail:

What was good:
...

Missing critical areas:
- requirements:
- scale/SLA:
- architecture:
- data model:
- processing:
- idempotency:
- backfills:
- late data:
- data quality:
- monitoring:
- security:
- cost:
- trade-offs:

Corrected strong design:
...

Weakness ID:
...

Repair drill:
...

Retest case:
...
```


## 14. System Design Progress Update

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


## 15. System Design Final Mentor Rule

```text
Never accept a tool-list system design.
A strong Data Engineering design must explain correctness, recovery, quality, monitoring, and trade-offs.
```
