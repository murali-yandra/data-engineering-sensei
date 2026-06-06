# Project Review Template

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

Review philosophy:
Reviews are not only for finding mistakes.
Reviews should improve interview readiness, production thinking, resume evidence, public portfolio quality, and mentor feedback accuracy.

Strict readiness rule:
Generated files are preparation material only.
Readiness requires reviewed work, scored feedback, weakness repair, and retest evidence.
```

Path:

```text
data-engineering-sensei/templates/reviews/project-review-template.md
```

Purpose:

```text
Review the candidate's project as a portfolio, resume, public portfolio, and interview asset.
Primary project context is Primary Portfolio Data Project.
```


## 1. Project Review Master Prompt

```text
You are my Data Engineering Sensei project reviewer.

Review my project strictly for Data Engineering job readiness.

Rules:
1. Do not accept tool-list explanation.
2. Review problem, requirements, architecture, data model, pipeline flow, DQ, security, testing, deployment, README, resume value, and interview defensibility.
3. Score each section from 0 to 5.
4. Identify what is strong, weak, missing, or exaggerated.
5. Ask for evidence before accepting claims.
6. Convert real evidence into resume bullets.
7. Tell me what to improve in public portfolio README.
8. Add project weaknesses and next tasks.
9. Do not invent metrics or implementation status.
10. Be direct and practical.

Use my main project:
Primary Portfolio Data Project with Use only the stack the candidate provides; otherwise mark unknown.
```


## 2. Project Review Rubric

Use this 0 to 5 scale:

```text
0 = not reviewed / no evidence
1 = very weak; major gaps
2 = basic; works only in simple cases
3 = usable with support; has important gaps
4 = interview-ready / production-aware for target level
5 = strong; clean, defensible, scalable, and can handle follow-ups
```

Default review verdicts:

```text
0-1.9:
not acceptable; major repair needed

2.0-2.9:
basic but not interview-ready

3.0-3.4:
usable but weak under follow-up

3.5-3.9:
near-ready but needs targeted repair

4.0-4.4:
interview-ready for candidate level

4.5-5.0:
strong and portfolio/resume-ready
```

Automatic score caps:

```text
No evidence: max 2
Tool names without reasoning: max 2.5
No tests: max 3.5
No error handling: max 3.5
No data quality thinking in data code/pipeline: max 3
No monitoring/recovery in pipeline: max 3
No security/PII discussion in project: max 3.5
No README/setup proof for portfolio project: max 3.5
Cannot defend design in follow-up: max 3.5
Claims impact without evidence: max 2.5
```


## 3. Project Review Input Template

Collect:

```text
Project name:
public portfolio link:
README available:
Current status:
Implemented features:
Planned features:
Tech stack:
Architecture:
Database schema:
Tests:
Deployment:
Demo/screenshots:
Resume bullets:
Known blockers:
```

Ask if missing:

```text
What is actually implemented today?
What is only planned?
What evidence can you show?
```


## 4. Project Review Output Format

```text
# Project Review

Project:
Overall score:
Portfolio verdict:
Resume verdict:
Interview verdict:

## One-Line Positioning
...

## Strengths
...

## Weaknesses
...

## Missing Evidence
...

## Architecture Review
...

## Data Model Review
...

## Pipeline/Data Flow Review
...

## Data Quality Review
...

## Security Review
...

## Testing/Deployment Review
...

## README/public portfolio Review
...

## Resume Bullet Review
...

## Interview Questions You Must Handle
...

## Priority Fixes
...

## Files To Update
...
```


## 5. Primary Portfolio Data Project Context

Known context:

```text
Problem:
Operational analytics is difficult because raw events or transactions need ingestion, validation, cleanup, enrichment, correction workflows, and reconciliation.

Possible value:
Turns raw source data into reliable analytics-ready outputs with validation, transformation, modeling, quality checks, reconciliation, and documented serving.

Tech:
candidate-provided ingestion or service layer
candidate-provided storage or warehouse
transformation and modeling code
orchestration or scheduling if implemented
tests and data quality checks
Docker or reproducible setup if implemented
CI/CD workflows if implemented
monitoring, docs, and public portfolio artifacts
```

Review warning:

```text
Only mark a feature strong if implemented or clearly evidenced.
Do not let planned features become resume claims.
```


## 6. Problem And Positioning Review

### Check 1: Is the problem clear?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: Is the user clear?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: Is the project relevant to Data Engineering?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: Can the candidate explain business value?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: Is the scope realistic?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 7. Architecture Review

### Check 1: Is the architecture understandable?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: Is data flow clear from source to output?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: Are components separated properly?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: Are trade-offs explained?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: Can the architecture be drawn?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 8. Data Model Review

### Check 1: Are entities clear?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: Are relationships clear?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: Are keys and constraints defined?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: Are indexes considered?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: Are audit fields considered?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 9. Pipeline Flow Review

### Check 1: How does transaction ingestion work?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: How are messages parsed?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: How are duplicates prevented?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: How is raw data standardized or enriched?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: How are categories assigned?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 6: How are corrections captured?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 10. Data Quality Review

### Check 1: Are required fields validated?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: Are bad records handled?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: Is reconciliation defined?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: Are user corrections auditable?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: Are DQ checks testable?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 11. Security Review

### Check 1: Is authentication explained?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: Is user-level isolation enforced?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: Are secrets protected?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: Is financial data treated as sensitive?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: Are logs safe?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 12. Testing And Deployment Review

### Check 1: Are tests present?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: Can app run from README?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: Are migrations documented?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: Is Docker setup clear?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: Does CI run useful checks?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 13. README And Portfolio Review

### Check 1: Does README explain problem?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: Does README show architecture?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: Does README provide setup?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: Does README show sample flow?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: Does README include roadmap and limitations?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 14. Resume Evidence Review

### Check 1: Are bullets evidence-backed?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 2: Can candidate defend each bullet?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 3: Are metrics real?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 4: Does bullet show Data Engineering value?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```

### Check 5: Does bullet avoid exaggeration?

Review instruction:

```text
Evaluate this honestly.
Ask for proof if needed.
Give score and repair action.
```

Interview impact:

```text
If weak, candidate may fail project deep-dive follow-ups.
```


## 15. Project Scorecard

| Area | Score | Evidence | Status |
|---|---:|---|---|
| Problem clarity | 0 | not reviewed | not_started |
| Architecture | 0 | not reviewed | not_started |
| Data model | 0 | not reviewed | not_started |
| Pipeline flow | 0 | not reviewed | not_started |
| Data quality | 0 | not reviewed | not_started |
| Security | 0 | not reviewed | not_started |
| Testing | 0 | not reviewed | not_started |
| Deployment | 0 | not reviewed | not_started |
| README | 0 | not reviewed | not_started |
| Resume value | 0 | not reviewed | not_started |
| Interview defense | 0 | not reviewed | not_started |


## 16. Project Review Findings Template

```text
Finding:
README does not show architecture.

Severity:
High

Impact:
Recruiter/interviewer cannot understand project depth quickly.

Fix:
Add architecture section with:
source -> ingestion layer -> storage or warehouse -> transformations -> data quality checks -> serving/reporting layer.

Evidence needed:
diagram or ASCII architecture + explanation.
```


## 17. Resume Bullet Validation

For each project bullet:

```text
Bullet:
Evidence:
Implemented or planned:
Can defend in interview:
Metric available:
Risk of exaggeration:
Improved bullet:
```

Rule:

```text
If feature is planned but not implemented, do not write it as completed.
```


## 18. Project Review Progress Update

After every review, update or recommend updates to:

```text
progress/CURRENT_STATE.md:
latest review result, score, active weakness, next action

progress/ROADMAP_PROGRESS.md:
affected module status, evidence, readiness gate impact

progress/NEXT_STEPS.md:
repair tasks and retest tasks

progress/WEAKNESS_REGISTER.md:
new weakness, severity, repair plan, retest method

progress/SESSION_LOG.md:
review session entry

progress/PROJECT_PROGRESS.md:
if project/code/pipeline evidence changed

progress/RESUME_STATE.md:
if a resume bullet or evidence changed

progress/PORTFOLIO_READINESS.md:
if repo/README/portfolio readiness changed
```

Review output must end with:

```text
Files to update:
- ...
Next 3 actions:
1.
2.
3.
```


## 19. Final Project Review Rule

```text
A project becomes job evidence only when it is understandable, defensible, documented, and connected to the target role.
```
