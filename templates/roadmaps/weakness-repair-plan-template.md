# Weakness Repair Plan Template

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
data-engineering-sensei/templates/roadmaps/weakness-repair-plan-template.md
```

Purpose:

```text
Create targeted repair plans for weaknesses discovered during assessment, drills, mocks, project reviews, SQL reviews, code reviews, or system design rounds.
```

This template is the most important roadmap when candidate is stuck or repeating mistakes.


## 1. Weakness Repair Mentor Prompt

```text
You are my Data Engineering Sensei weakness repair mentor.

Create a strict weakness repair plan.

Rules:
1. Use the weakness evidence, not vague feelings.
2. Identify root cause.
3. Explain why this weakness matters in interviews.
4. Create targeted drills.
5. Set retest conditions.
6. Do not mark repaired without retest.
7. Update progress/WEAKNESS_REGISTER.md and progress/NEXT_STEPS.md.
8. Keep repair focused and time-boxed.
9. Do not switch topics until critical weakness is repaired.
10. Be direct and practical.

Use my context:
I am preparing for Data Engineering roles.
My highest ROI areas are SQL, Python, DE fundamentals, system design, and project deep dive.
```


## 2. Weakness Repair Scoring

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


## 3. Weakness Entry Input

Collect:

```text
Weakness ID:
Area:
Topic:
Current score:
Target score:
Evidence:
Where found:
Severity:
Why it matters:
Related files:
Deadline:
```

If evidence is missing:

```text
Run assessment or mock first.
```


## 4. Weakness Repair Output Format

```text
# Weakness Repair Plan

Weakness ID:
Area:
Topic:
Severity:
Current score:
Target score:
Status:

## Evidence
...

## Root Cause
...

## Why It Matters
...

## Repair Strategy
...

## Drill Plan
...

## Study Material
...

## Retest Plan
...

## Pass Criteria
...

## Files To Update
...

## Next 3 Actions
...
```


## 5. Repair Cycle

```text
1. Name weakness.
2. Record evidence.
3. Identify root cause.
4. Explain correct concept.
5. Practice small drills.
6. Practice realistic drill.
7. Retest under pressure.
8. Mark repaired only if retest passes.
9. Update progress files.
```

Rule:

```text
Passive reading does not repair a weakness.
```


## 6. Repair Plan: SQL Grain Weakness

- Explain what one output row represents for 5 queries.
- Identify source table grain for 5 tables.
- Rewrite 3 queries that duplicate rows.
- Explain why DISTINCT is not a fix.
- Retest with a business SQL case.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 7. Repair Plan: SQL Window Function Weakness

- Practice ROW_NUMBER vs RANK vs DENSE_RANK.
- Solve latest-row-per-group problems.
- Solve top-N-per-group problems.
- Solve running total problems.
- Retest with 2 timed window queries.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 8. Repair Plan: Python File/API Weakness

- Write CSV parser with bad-row handling.
- Write JSON flattener.
- Write API pagination function.
- Add retry/error handling/logging.
- Retest with a complete data script.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 9. Repair Plan: DSA Pattern Recognition Weakness

- Create pattern flashcards.
- Solve 5 hashmap problems.
- Solve 5 sliding window problems.
- Explain pattern before coding.
- Retest with unseen easy/medium problem.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 10. Repair Plan: DE Fundamentals Weakness

- Answer ETL vs ELT in 90 seconds.
- Answer batch vs streaming with example.
- Explain warehouse vs lake vs lakehouse.
- Explain idempotency/backfills.
- Retest with fundamentals mock.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 11. Repair Plan: System Design Tool-First Weakness

- Practice requirements-first opening.
- Design without naming tools for first 5 minutes.
- Use framework: requirements → sources → consumers → SLA → architecture.
- Retest with batch pipeline design.
- Score based on structure and completeness.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 12. Repair Plan: Idempotency/Backfill Weakness

- Explain idempotency with example.
- Design rerunnable batch pipeline.
- Design safe backfill by partition.
- Explain duplicate prevention.
- Retest with pipeline failure scenario.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 13. Repair Plan: Data Quality Weakness

- List DQ checks for transaction pipeline.
- Design DQ gates for reporting pipeline.
- Explain severity levels.
- Explain reconciliation.
- Retest with DQ framework design.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 14. Repair Plan: Monitoring Weakness

- Define freshness metrics.
- Define row-count and volume alerts.
- Define DLQ/failed records alerts.
- Define dashboard/report SLA alerts.
- Retest with pipeline monitoring follow-up.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 15. Repair Plan: Project Explanation Weakness

- Write 2-minute pitch.
- Explain architecture in ASCII.
- Explain data model.
- Explain DQ/security/failure handling.
- Retest with project deep-dive mock.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 16. Repair Plan: Resume Evidence Weakness

- Pick one project bullet.
- List evidence for it.
- Remove unsupported claims.
- Add measurable proof if available.
- Retest by defending bullet in mock.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 17. Repair Plan: Communication Weakness

- Answer in 90 seconds.
- Use structure: point → example → trade-off → summary.
- Record and score answer.
- Practice follow-ups.
- Retest with behavioral/project question.

Repair done condition:

```text
Candidate passes retest at or above target score.
```

Progress files:

```text
progress/WEAKNESS_REGISTER.md
progress/NEXT_STEPS.md
progress/SESSION_LOG.md
progress/ROADMAP_PROGRESS.md
progress/CURRENT_STATE.md
```


## 18. 3-Day Weakness Repair Sprint

Use for small or medium weakness.

```text
Day 1:
Understand weakness and solve 3 guided drills.

Day 2:
Solve 5 independent drills.

Day 3:
Retest under time pressure and update status.
```

Pass condition:

```text
retest score >= target
mistake not repeated
candidate can explain correction
```


## 19. 7-Day Weakness Repair Sprint

Use for high or critical weakness.

```text
Day 1:
Root cause and corrected concept.

Day 2:
Basic drills.

Day 3:
Intermediate drills.

Day 4:
Realistic interview problem.

Day 5:
Apply to project/system design.

Day 6:
Mock retest.

Day 7:
Review, update progress files, and decide next weakness.
```


## 20. Weakness Repair Task Template

```text
Task ID:
Weakness ID:
Priority:
Status:
Task:
Why:
Input file:
Drill:
Time box:
Success criteria:
Retest:
Files to update:
```


## 21. Weakness Retest Template

```text
Retest for Weakness ID:
Date:
Original score:
Target score:
Retest question:
Candidate answer:
New score:
Pass/fail:
What improved:
What still failed:
Status update:
Next action:
```

Rule:

```text
If retest fails, keep weakness open or repairing.
Do not mark repaired.
```


## 22. Weakness Repair Review Prompt

```text
Review my active weaknesses.

For each weakness:
1. severity
2. current score
3. root cause
4. repair task
5. retest method
6. whether it blocks job readiness

Then choose the top 3 weaknesses to repair this week.
Be strict.
```


## 23. Weakness Repair Progress Update

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


## 24. Final Weakness Repair Rule

```text
The roadmap is only as strong as the weakness repair loop.
If the same mistake repeats, stop broad learning and repair the weakness.
```
