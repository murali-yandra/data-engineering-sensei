# Templates Index

<!-- BEGIN LIBRARY ROLE -->
> **Library role: hub.** Entry point for every output format Data Engineering Sensei produces.
>
> Open the template that matches what you are about to write, then follow its structure.
<!-- END LIBRARY ROLE -->

Consistent output shape is not cosmetic. A candidate compares this week's review against
last week's to see whether they are actually improving - and they can only do that if both
reviews have the same sections in the same order. Improvising a new format each time hides
progress and regression alike.

Pick by what you are producing.

## Assessment and intake

| File | Use when |
|---|---|
| `templates/assessment/intake-questionnaire.md` | Running the full intake for a roadmap or assessment request |
| `templates/assessment/skill-level-assessment-template.md` | Writing the diagnosis after intake |
| `templates/assessment/candidate-profile-template.md` | Recording a candidate's durable profile |

## Roadmaps

| File | Use when |
|---|---|
| `templates/roadmaps/personalized-roadmap-template.md` | Default - any roadmap built from a real intake |
| `templates/roadmaps/30-day-roadmap-template.md` | Interview is under ~5 weeks out |
| `templates/roadmaps/60-day-roadmap-template.md` | Roughly two months of runway |
| `templates/roadmaps/90-day-roadmap-template.md` | A full quarter, or a career switch |
| `templates/roadmaps/weakness-repair-plan-template.md` | Repairing one diagnosed weakness |

## Reviews

| File | Use when |
|---|---|
| `templates/reviews/sql-review-template.md` | Reviewing a query |
| `templates/reviews/code-review-template.md` | Reviewing Python or a DSA solution |
| `templates/reviews/pipeline-review-template.md` | Reviewing a pipeline or system design |
| `templates/reviews/project-review-template.md` | Reviewing a project story or resume bullet |

## Mock interview rounds

| File | Use when |
|---|---|
| `templates/interviews/mock-interview-template.md` | Running a full multi-round loop |
| `templates/interviews/sql-round-template.md` | A SQL round |
| `templates/interviews/python-round-template.md` | A Python round |
| `templates/interviews/dsa-round-template.md` | A coding/DSA screen |
| `templates/interviews/system-design-round-template.md` | A design round |
| `templates/interviews/project-deep-dive-round-template.md` | A project defense round |
| `templates/interviews/feedback-report-template.md` | The written report after a round |
| `templates/interview-feedback/mock-interview-feedback-template.md` | Scored feedback on a single mock |

## Answer frameworks

Give these to the candidate as the structure to answer *with* - they are for the candidate's
own use under pressure, not just for your write-up.

| File | Use when |
|---|---|
| `templates/answer-frameworks/sql-answer-framework.md` | Teaching how to approach a SQL question before writing SQL |
| `templates/answer-frameworks/python-answer-framework.md` | Teaching how to approach a Python problem |
| `templates/answer-frameworks/system-design-answer-framework.md` | Teaching the requirements-first design sequence |

## Worked solutions

Use when writing out a model answer the candidate will study.

| File | Use when |
|---|---|
| `templates/solutions/sql-solution-template.md` | A model SQL solution |
| `templates/solutions/python-solution-template.md` | A model Python solution |
| `templates/solutions/dsa-solution-template.md` | A model DSA solution with complexity |
| `templates/solutions/system-design-solution-template.md` | A model system design answer |
| `templates/solutions/project-explanation-template.md` | A model project explanation |

## Progress

| File | Use when |
|---|---|
| `templates/progress/session-summary-template.md` | Closing out a session |

Progress files themselves live in `progress/` and are maintained by
`scripts/update_progress.py` rather than by hand.
