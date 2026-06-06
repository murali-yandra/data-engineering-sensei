# Weakness Register

Generated: 2026-06-06

Path:

```text
data-engineering-sensei/practice/progress/WEAKNESS_REGISTER.md
```

This file tracks the candidate's **active and historical weaknesses** for Data Engineering Sensei.

It is used to store:

```text
what weakness was found
where it was found
how serious it is
what evidence proves it exists
what repair drill is assigned
when it should be retested
whether it is still blocking progress
```

This file is not a place for vague self-criticism.

It is a repair tracker.

Core rule:

```text
A weakness is not repaired until retested with evidence.
```

Current status:

```text
Initial weakness register generated.
Candidate has not completed baseline assessment yet.
Most weaknesses are provisional until tested.
```


## 1. Purpose

The weakness register exists to prevent repeating the same mistakes.

The AI mentor should update this file when:

```text
candidate fails a drill
candidate scores below target in a mock
candidate gives vague project explanation
candidate misses a critical system design requirement
candidate cannot solve a common SQL/Python/DSA pattern
candidate makes the same mistake repeatedly
candidate has a resume/project claim that cannot be defended
```

Use it to decide:

```text
what to repair next
what blocks roadmap progress
what should be retested
what should be added to NEXT_STEPS.md
what should be tracked in ROADMAP_PROGRESS.md
```

Strict rule:

```text
Do not hide weaknesses.
Make them specific, measurable, and repairable.
```


## 2. Relationship With Other Progress Files

| File | How it connects |
|---|---|
| `CURRENT_STATE.md` | stores only the active top weaknesses |
| `ROADMAP_PROGRESS.md` | marks roadmap modules blocked by weaknesses |
| `NEXT_STEPS.md` | stores repair tasks for active weaknesses |
| `SESSION_LOG.md` | records when weakness was discovered or repaired |
| `MOCK_INTERVIEW_HISTORY.md` | provides mock evidence for weakness |
| `CANDIDATE_PROFILE.md` | stores long-term risk areas |
| `PROJECT_PROGRESS.md` | stores project-specific weaknesses |
| `RESUME_STATE.md` | stores resume-evidence weaknesses |

Update rule:

```text
If a weakness is added here, also add the repair task to NEXT_STEPS.md.
If a weakness blocks a roadmap module, also update ROADMAP_PROGRESS.md.
If a weakness was discovered in a mock, also update MOCK_INTERVIEW_HISTORY.md.
If a weakness is currently active, summarize it in CURRENT_STATE.md.
```


## 3. Weakness Status Values

Use only these status values:

```text
open:
weakness exists and repair has not started

repairing:
candidate is actively working on repair

needs_retest:
repair work done but not yet proven

repaired:
candidate passed retest and weakness is no longer active

blocked:
cannot repair because prerequisite is missing

archived:
old weakness no longer relevant but kept for history
```

Do not use vague statuses:

```text
better
almost fixed
okay
improved
done maybe
```

Completion rule:

```text
repaired = retest score >= target + mentor approval + evidence recorded
```


## 4. Severity Levels

Use these severity levels:

```text
Critical:
will likely fail interview or block job readiness

High:
will hurt interview score seriously

Medium:
noticeable weakness but repairable with focused practice

Low:
small improvement area

Unknown:
not assessed yet
```

Severity examples:

```text
Critical:
cannot define table grain in SQL/warehouse/reporting questions

High:
misses idempotency and monitoring in system design

Medium:
needs cleaner Python error handling

Low:
minor communication polish issue
```

Rule:

```text
Critical and High weaknesses should always appear in NEXT_STEPS.md.
```


## 5. Weakness Entry Template

Use this format for every weakness.

```text
Weakness ID:
Area:
Topic:
Severity:
Status:
Found on:
Found in:
Evidence:
Why it matters:
Repair plan:
Repair file:
Practice target:
Retest method:
Retest date:
Target score:
Current score:
Owner:
Related roadmap module:
Related progress files:
Notes:
```

Example:

```text
Weakness ID:
WR-SD-001

Area:
System Design

Topic:
Idempotency and retry handling

Severity:
High

Status:
open

Found in:
Batch pipeline mock

Evidence:
Candidate described pipeline steps but did not explain safe reruns, duplicate prevention, or watermark commit timing.

Why it matters:
Data pipelines fail in production; interviewers expect recovery and idempotency.

Repair plan:
Study batch-pipeline.md idempotency sections and design 2 retry-safe pipelines.

Retest method:
45-minute batch pipeline mock

Target score:
4/5
```


## 6. Current Active Weaknesses

These are initial placeholders until baseline assessment is completed.

| Weakness ID | Area | Topic | Severity | Status | Evidence | Repair Action |
|---|---|---|---|---|---|---|
| WR-BASE-001 | Overall | Baseline not completed | Critical | open | No baseline scores yet | Run profile baseline assessment |
| WR-SQL-001 | SQL | SQL skill not baselined | Unknown | open | No SQL mock yet | Run SQL baseline |
| WR-PY-001 | Python | Python scripting not baselined | Unknown | open | No Python mock yet | Run Python baseline |
| WR-DSA-001 | DSA | DSA pattern ability not baselined | Unknown | open | No DSA mock yet | Run DSA baseline |
| WR-SD-001 | System Design | System design delivery not baselined | Unknown | open | No system design mock yet | Run batch pipeline mock |
| WR-PRJ-001 | Project | Main project deep dive not tested | High | open | No project mock yet | Run finance tracker deep dive |
| WR-COMM-001 | Communication | Interview communication not scored | Unknown | open | No communication mock yet | Run mock interview |

Rule:

```text
Replace placeholders with real weaknesses after baseline assessment.
```


## 8. SQL Weakness Categories

- table grain confusion
- wrong join type
- fact-to-fact join duplication
- overusing DISTINCT to hide bugs
- weak CTE decomposition
- window function confusion
- ranking ties not handled
- deduplication keep-rule missing
- date filtering mistakes
- gaps and islands weakness
- query optimization vocabulary weak
- SQL Server syntax gaps

Prompt:

```text
If one of these appears in a session, create a weakness entry with evidence and repair task.
```


## 9. Python Weakness Categories

- unclear function structure
- weak list/dict/set usage
- file parsing errors
- JSON/CSV edge cases missed
- API pagination not handled
- exceptions not handled
- logging missing
- pandas merge/groupby weak
- code not tested with edge cases
- overcomplicating simple scripts

Prompt:

```text
If one of these appears in a session, create a weakness entry with evidence and repair task.
```


## 10. DSA Weakness Categories

- pattern recognition slow
- hashmap frequency logic weak
- two pointer condition confusion
- sliding window shrink logic weak
- stack use cases unclear
- binary search boundary errors
- interval merge logic weak
- heap/top K pattern unclear
- BFS/DFS traversal basics weak
- time complexity explanation weak

Prompt:

```text
If one of these appears in a session, create a weakness entry with evidence and repair task.
```


## 11. Data Engineering Fundamentals Weakness Categories

- ETL vs ELT explanation weak
- batch vs streaming trade-off weak
- data lake vs warehouse vs lakehouse confusion
- partitioning strategy weak
- file format trade-offs weak
- orchestration/DAG concepts weak
- idempotency/backfill explanation weak
- data quality gates weak
- schema evolution weak
- CDC concepts weak
- monitoring/alerting weak
- cost/security ignored

Prompt:

```text
If one of these appears in a session, create a weakness entry with evidence and repair task.
```


## 12. System Design Weakness Categories

- jumps to tools before requirements
- does not define sources/consumers
- does not estimate scale/SLA
- does not define storage layers
- does not define data model
- misses idempotency
- misses backfills/replay
- misses late data
- misses data quality
- misses monitoring
- misses security/PII
- misses cost trade-offs
- weak final summary

Prompt:

```text
If one of these appears in a session, create a weakness entry with evidence and repair task.
```


## 13. Project Deep Dive Weakness Categories

- project explained as tool list
- business problem unclear
- architecture unclear
- data model unclear
- pipeline flow unclear
- trade-offs missing
- failure handling missing
- data quality/reconciliation missing
- security/authentication weak
- testing/deployment weak
- impact not measurable
- resume bullet not defensible

Prompt:

```text
If one of these appears in a session, create a weakness entry with evidence and repair task.
```


## 14. Communication Weakness Categories

- answer too long
- answer too vague
- not structured
- no examples
- no trade-offs
- does not clarify requirements
- does not summarize
- low confidence
- uses buzzwords without proof
- cannot handle follow-ups

Prompt:

```text
If one of these appears in a session, create a weakness entry with evidence and repair task.
```


## 15. Resume/GitHub Weakness Categories

- bullets lack impact
- claims not backed by project evidence
- skills too broad
- README unclear
- setup instructions missing
- architecture diagram missing
- project status unclear
- no measurable proof
- portfolio story inconsistent

Prompt:

```text
If one of these appears in a session, create a weakness entry with evidence and repair task.
```


## 15. Repair Cycle

Every weakness must follow this cycle:

```text
1. Detect weakness.
2. Record evidence.
3. Assign severity.
4. Add repair task.
5. Practice targeted drills.
6. Retest under pressure.
7. Mark repaired only if retest passes.
8. Update roadmap and current state.
```

Repair cycle prompt:

```text
Repair weakness <Weakness ID>.
Give me:
1. short explanation of what I am missing
2. 3 examples
3. 5 practice drills
4. one retest question
5. scoring rubric
```

Rule:

```text
Never repair a weakness with passive reading only.
```


## 16. Retest Rules

Retest is required when:

```text
score was below pass mark
weakness severity is Critical or High
candidate needed heavy hints
candidate failed to explain clearly
candidate practiced but has not proven improvement
```

Retest methods:

```text
timed SQL problem
Python script task
DSA pattern problem
system design mini-mock
full mock interview
project deep-dive follow-up
resume bullet defense
```

Retest pass criteria:

```text
target score reached
answer given with less help
mistake not repeated
candidate can explain why old answer was weak
```

Do not mark repaired if:

```text
candidate only read solution
candidate needed same hint again
candidate cannot explain concept aloud
candidate passed easy case but failed realistic case
```


## 17. Weakness-To-Next-Steps Mapping

When weakness is added, create a next step.

| Weakness Type | Next Step Example |
|---|---|
| SQL window weak | Solve 5 window function problems |
| Python API weak | Write API pagination script |
| DSA hashmap weak | Solve 5 hashmap frequency problems |
| System design idempotency weak | Redesign batch pipeline with retry-safe writes |
| Data quality weak | Design DQ gates for reporting pipeline |
| Project explanation weak | Practice 2-minute project pitch |
| Resume evidence weak | Add metric/evidence to 3 bullets |
| Communication weak | Answer same question in 90 seconds |

Prompt:

```text
Create a NEXT_STEPS.md repair task for Weakness ID <id>.
The task must be concrete, time-boxed, and produce evidence.
```


## 18. Weakness Review Schedule

Review weaknesses:

```text
daily:
active Critical/High weaknesses

weekly:
all open and repairing weaknesses

monthly:
archived/repaired weaknesses and roadmap patterns
```

Weekly review prompt:

```text
Review my WEAKNESS_REGISTER.md.
Show:
1. top 5 active weaknesses
2. blockers
3. repair tasks for this week
4. retests due
5. weaknesses that can be archived
```

Monthly review prompt:

```text
Show weakness trends from this month.
Which weaknesses repeated?
Which were repaired?
Which still block job readiness?
```


## 19. Weakness Summary Dashboard

Current dashboard:

| Metric | Value |
|---|---:|
| Critical open weaknesses | 1 |
| High open weaknesses | 1 |
| Medium open weaknesses | 0 |
| Low open weaknesses | 0 |
| Unknown open weaknesses | 5 |
| Weaknesses in repair | 0 |
| Weaknesses needing retest | 0 |
| Repaired weaknesses | 0 |

Update rule:

```text
Update this dashboard after adding, repairing, or archiving weaknesses.
```


## 20. Machine-Readable Weakness State

Keep this YAML-style block synchronized.

```yaml
weakness_register_version: "1.0"
last_updated: "YYYY-MM-DD"
active_critical:
  - "WR-BASE-001"
active_high:
  - "WR-PRJ-001"
active_unknown:
  - "WR-SQL-001"
  - "WR-PY-001"
  - "WR-DSA-001"
  - "WR-SD-001"
  - "WR-COMM-001"
needs_retest: []
repaired: []
next_repair_action: "Run baseline assessment and replace placeholders with real weaknesses."
related_files:
  current_state: "practice/progress/CURRENT_STATE.md"
  roadmap_progress: "practice/progress/ROADMAP_PROGRESS.md"
  next_steps: "practice/progress/NEXT_STEPS.md"
  session_log: "practice/progress/SESSION_LOG.md"
  mock_history: "practice/progress/MOCK_INTERVIEW_HISTORY.md"
```


## 21. Final Summary

This file is the repair engine for Data Engineering Sensei.

It stores:

```text
weaknesses
evidence
severity
repair plans
retest rules
status
blocking impact
related progress updates
```

Current truth:

```text
Real weaknesses are not yet known because baseline assessment has not started.
Initial placeholders exist so the mentor knows what to assess first.
```

Final rule:

```text
The candidate improves only when weaknesses are named, repaired, and retested.
```
