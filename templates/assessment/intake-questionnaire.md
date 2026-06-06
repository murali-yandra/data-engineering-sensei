# Intake Questionnaire

Generated: 2026-06-06

Path:

```text
data-engineering-sensei/templates/assessment/intake-questionnaire.md
```

Purpose:

```text
This questionnaire is used by the Data Engineering Sensei AI mentor to collect candidate details before creating the roadmap and assessment plan.
```

Important:

```text
The AI mentor should ask the required baseline questions in one block by default.
Use one-question-at-a-time intake only when the candidate explicitly asks for a conversational intake or when the candidate is overwhelmed.
```

This questionnaire is designed for a candidate preparing for Data Engineering roles with:

```text
SQL
Python
DSA patterns
ETL/ELT
data modeling
data warehouse
data lake
orchestration
Spark/PySpark
cloud
system design
project deep dive
resume/public portfolio/professional profile
job search
```


## 1. AI Mentor Intake Prompt

Use this prompt to start the intake.

```text
You are my Data Engineering Sensei mentor.

Run my intake questionnaire for Data Engineering job preparation.

Rules:
1. Ask the required baseline questions in one message.
2. Wait for my answers before creating the roadmap.
3. If my answer is vague, ask only the missing critical follow-up.
4. Do not assume or invent details.
5. At the end, summarize my profile.
6. Give me a realistic readiness verdict.
7. Create a first roadmap.
8. Tell me which progress files need updates.

Use the context that I am preparing for Data Engineering roles and want strict, practical, no-sugarcoating guidance.

Collect details about:
- current role and experience
- target role
- target location
- skills
- projects
- SQL/Python/DSA level
- data engineering fundamentals
- system design
- resume/public portfolio/professional profile
- job search
- time availability
- blockers
- learning preferences

After intake, update:
progress/CANDIDATE_PROFILE.md
progress/CURRENT_STATE.md
progress/ROADMAP_PROGRESS.md
progress/NEXT_STEPS.md
progress/WEAKNESS_REGISTER.md if weaknesses are clear
progress/PROJECT_PROGRESS.md if project details are given
progress/RESUME_STATE.md if resume details are given
```


## 2. Intake Flow

The intake should follow this order:

```text
1. identity and role context
2. target job goal
3. experience and work history
4. current skill self-rating
5. SQL assessment context
6. Python assessment context
7. DSA assessment context
8. data engineering fundamentals
9. system design exposure
10. project portfolio
11. resume/public portfolio/professional profile
12. job search status
13. constraints and availability
14. learning preferences
15. final summary and next steps
```

Mentor rule:

```text
Ask the baseline assessment in one block.
If the candidate requests a conversational intake, ask one section at a time.
If the candidate is impatient, ask only the highest-impact questions first.
```


## 3. Identity And Current Role

### Q1. What is your current job title and what work do you actually do day to day?

Why this matters:

```text
Clarify real experience vs title.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. How many years of professional experience do you have?

Why this matters:

```text
Set target level.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Optional Q3. Which technologies do you use at work?

Why this matters:

```text
Identify real evidence when tool-specific project or resume alignment is needed.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Do you work mostly with SQL, Python, pipelines, reports, dashboards, cloud, or something else?

Why this matters:

```text
Map experience to DE roles.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. What are the strongest tasks you have done professionally?

Why this matters:

```text
Resume evidence.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. What are the weakest tasks you avoid or struggle with?

Why this matters:

```text
Weakness register.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 4. Target Role And Goal

### Q1. What exact role are you targeting first: Data Engineer, Analytics Engineer, ETL Developer, Cloud Data Engineer, or BI/Data Warehouse Engineer?

Why this matters:

```text
Role focus.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Are you targeting local market, remote, target market, target market, or other international roles?

Why this matters:

```text
Job strategy.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. What is your timeline: 1 month, 3 months, 6 months, or longer?

Why this matters:

```text
Roadmap pacing.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. What role target or compensation expectations, if relevant and voluntarily shared are you expecting, if you want to share?

Why this matters:

```text
Reality check.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Are you willing to relocate or only remote?

Why this matters:

```text
Search strategy.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. What companies or company types are you aiming for?

Why this matters:

```text
Interview difficulty.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 5. Work Experience Evidence

### Q1. Describe one real data task you completed at work.

Why this matters:

```text
Evidence bank.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Have you written SQL queries, stored procedures, or reports in production?

Why this matters:

```text
SQL proof.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Have you worked on ETL/ELT pipelines?

Why this matters:

```text
Pipeline proof.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Have you deployed scripts or database changes through any release process?

Why this matters:

```text
DevOps proof.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Have you debugged a production data issue?

Why this matters:

```text
Behavioral/story proof.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. Do you know any measurable impact from your work?

Why this matters:

```text
Resume metrics.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 6. SQL Intake

### Q1. Rate your SQL from 0 to 5 and explain why.

Why this matters:

```text
Self-rating plus evidence.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Can you write joins confidently?

Why this matters:

```text
Basic SQL.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Can you use CTEs and subqueries?

Why this matters:

```text
Intermediate SQL.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Can you use window functions like ROW_NUMBER, RANK, SUM OVER?

Why this matters:

```text
Advanced SQL.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Can you solve deduplication problems?

Why this matters:

```text
DE SQL pattern.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. Can you explain query optimization basics?

Why this matters:

```text
Performance.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Optional Q7. Which SQL database do you use most: SQL Server, PostgreSQL, MySQL, BigQuery, Snowflake, etc.?

Why this matters:

```text
Dialect context.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 7. Python Intake

### Q1. Rate your Python from 0 to 5 and explain why.

Why this matters:

```text
Self-rating plus evidence.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Can you write functions without help?

Why this matters:

```text
Basics.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Can you process CSV/JSON files?

Why this matters:

```text
Data scripting.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Can you call APIs and handle pagination?

Why this matters:

```text
DE Python.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Can you use pandas for filtering, grouping, and merging?

Why this matters:

```text
Analytics scripting.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. Can you add logging and error handling?

Why this matters:

```text
Production readiness.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q7. Have you written tests for Python code?

Why this matters:

```text
Quality.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 8. DSA Intake

### Q1. Rate your DSA from 0 to 5 and explain why.

Why this matters:

```text
Self-rating.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Which patterns do you know: hashmap, two pointers, sliding window, stack, binary search, heap, BFS/DFS?

Why this matters:

```text
Pattern map.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Have you solved LeetCode easy/medium problems?

Why this matters:

```text
Evidence.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Do you struggle more with coding, pattern recognition, or explanation?

Why this matters:

```text
Repair direction.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. How much DSA does your target company require?

Why this matters:

```text
Priority setting.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 9. Data Engineering Fundamentals Intake

### Q1. Can you explain ETL vs ELT?

Why this matters:

```text
Fundamentals.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Can you explain batch vs streaming?

Why this matters:

```text
Fundamentals.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Can you explain data warehouse vs data lake vs lakehouse?

Why this matters:

```text
Storage concepts.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Can you explain partitioning and why it matters?

Why this matters:

```text
Performance.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Can you explain idempotency in pipelines?

Why this matters:

```text
Production reliability.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. Can you explain backfills?

Why this matters:

```text
Production reliability.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q7. Can you explain data quality checks?

Why this matters:

```text
DQ readiness.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q8. Can you explain orchestration and DAGs?

Why this matters:

```text
Airflow readiness.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 10. System Design Intake

### Q1. Have you ever designed a data pipeline in an interview style?

Why this matters:

```text
Baseline.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Can you design a batch pipeline?

Why this matters:

```text
Core DE design.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Can you design a data warehouse?

Why this matters:

```text
Warehouse readiness.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Can you design a data quality framework?

Why this matters:

```text
DQ readiness.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Can you design a CDC pipeline?

Why this matters:

```text
Advanced pipeline.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. Can you design event ingestion or realtime pipeline?

Why this matters:

```text
Streaming readiness.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q7. What do you usually miss in design answers: requirements, scale, data model, DQ, monitoring, security, cost, trade-offs?

Why this matters:

```text
Weakness mapping.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 11. Project Portfolio Intake

### Q1. What is your main project for interviews?

Why this matters:

```text
Project focus.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. What problem does the project solve?

Why this matters:

```text
Problem clarity.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. What is the tech stack?

Why this matters:

```text
Stack evidence.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. What features are completed?

Why this matters:

```text
Status.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. What is still in progress?

Why this matters:

```text
Reality check.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. Can you explain the architecture?

Why this matters:

```text
Deep dive.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q7. Can you explain the database schema?

Why this matters:

```text
Data modeling.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q8. Can you explain failure handling?

Why this matters:

```text
Production thinking.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q9. Can you explain security?

Why this matters:

```text
Risk.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q10. Can you show public portfolio, README, screenshots, tests, or demo?

Why this matters:

```text
Portfolio proof.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 12. Resume/public portfolio/professional profile Intake

### Q1. Do you already have a resume for Data Engineering roles?

Why this matters:

```text
Resume status.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Do your resume bullets have measurable impact?

Why this matters:

```text
Evidence.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Do you have public portfolio projects that are ready to show recruiters?

Why this matters:

```text
public portfolio status.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Does your main project README explain setup, architecture, and features?

Why this matters:

```text
README quality.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Does your professional profile clearly say Data Engineer/Data Engineering focus?

Why this matters:

```text
professional profile positioning.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q6. Do you post or comment about tech/data engineering?

Why this matters:

```text
Visibility.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 13. Constraints And Availability

### Q1. How many hours per day can you study or practice?

Why this matters:

```text
Roadmap realism.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. How many days per week can you commit?

Why this matters:

```text
Schedule.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Do you prefer morning, evening, or weekend study?

Why this matters:

```text
Planning.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. What blocks your consistency?

Why this matters:

```text
Risk.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Do you need a 30-day, 60-day, or 6-month plan?

Why this matters:

```text
Plan horizon.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 14. Learning Preferences

### Q1. Do you prefer visual explanations, examples, drills, or mock interviews?

Why this matters:

```text
Teaching style.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q2. Do you want strict scoring after every answer?

Why this matters:

```text
Feedback mode.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q3. Do you want one question at a time?

Why this matters:

```text
Interaction style.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q4. Do you prefer links when visuals cannot be shown?

Why this matters:

```text
Resource style.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```

### Q5. Do you want direct no-sugarcoating reality checks?

Why this matters:

```text
Tone.
```

Expected answer format:

```text
Answer:
Evidence:
Confidence:
Blocker:
```

AI mentor follow-up rule:

```text
If the answer is vague, ask for one concrete example or evidence.
```


## 15. Fast Intake Version

Use this when the candidate wants a shorter intake.

```text
Ask me only these 10 questions first:

1. What role are you targeting first?
2. How many years of experience do you have?
3. What do you do in your current job day to day?
4. Rate SQL from 0 to 5 with evidence.
5. Rate Python from 0 to 5 with evidence.
6. Rate DSA from 0 to 5 with evidence.
7. What is your main project and current status?
8. What system design topics can you explain?
9. Is your resume/public portfolio ready?
10. How many hours per week can you practice?

After I answer, give:
- realistic readiness verdict
- top 5 weaknesses
- next 7-day plan
- files to update
```


## 16. Intake Scoring Rules

After intake, score the candidate only where evidence exists.

```text
0 = not assessed
1 = beginner
2 = basic
3 = usable with support
4 = interview-ready
5 = strong
```

Do not score from confidence alone.

Evidence examples:

```text
SQL:
solved query, work task, mock answer

Python:
script, code, project module, mock answer

System design:
structured design answer, mock score

Project:
clear explanation, repo, README, architecture, working code

Resume:
evidence-backed bullets and defensible claims
```

AI mentor prompt:

```text
Based on my intake answers, score only the areas where you have enough evidence.
For missing evidence, mark "not assessed".
Do not inflate scores.
```


## 17. Intake Summary Output Template

At the end of intake, output:

```text
# Intake Summary

## Candidate Snapshot
...

## Target Role
...

## Current Evidence
...

## Skill Scores
...

## Strengths
...

## Risks
...

## Missing Information
...

## Immediate Next Steps
...

## Recommended Roadmap Phase
...

## Files To Update
...
```

Final verdict format:

```text
Current readiness:
not_ready / partially_ready / interview_ready

Reason:
...

Fastest improvement path:
...
```


## 18. Intake-to-Progress File Mapping

Use this mapping after intake.

| Intake Result | Update File |
|---|---|
| stable personal/career details | `progress/CANDIDATE_PROFILE.md` |
| current phase and latest state | `progress/CURRENT_STATE.md` |
| roadmap phase and skill module status | `progress/ROADMAP_PROGRESS.md` |
| immediate tasks | `progress/NEXT_STEPS.md` |
| weakness discovered | `progress/WEAKNESS_REGISTER.md` |
| project evidence | `progress/PROJECT_PROGRESS.md` |
| session details | `progress/SESSION_LOG.md` |
| mock score | `progress/MOCK_INTERVIEW_HISTORY.md` |
| resume bullets/evidence | `progress/RESUME_STATE.md` |
| public portfolio/portfolio status | `progress/PORTFOLIO_READINESS.md` |
| applications/interviews | `progress/JOB_SEARCH_READINESS.md` |

AI mentor prompt:

```text
After intake, tell me exactly which files should be updated and why.
```


## 19. No-Sugarcoating Reality Check Prompt

Use this after intake.

```text
Based on my intake answers, give me a no-sugarcoating reality check.

Tell me:
1. what roles I can realistically target now
2. what roles are too early for me
3. what will fail me in interviews
4. what I should stop wasting time on
5. what I should focus on for the next 30 days
6. whether my main project is strong enough
7. whether my resume/public portfolio is ready
8. what score I need before applying aggressively

Be direct but practical.
Give percentages only if they are rough estimates and explain uncertainty.
```


## 20. Final Intake Rule

The intake is complete only when the mentor can answer:

```text
Who is the candidate?
What role is the candidate targeting?
What evidence exists?
What is not assessed?
What are the top risks?
What should be done next?
Which files must be updated?
```

Final rule:

```text
Do not start a generic roadmap before intake.
Use intake to personalize the roadmap.
```
