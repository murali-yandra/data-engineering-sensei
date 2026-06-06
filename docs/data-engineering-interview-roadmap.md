# Data Engineering Interview Roadmap

Generated: 2026-06-06

This file defines how **Data Engineering Sensei** should create and use interview-preparation roadmaps.

The roadmap is not a generic study calendar. It must be personalized based on:

- candidate experience
- current role
- interview timeline
- target companies/countries if provided
- skill ratings
- weakest areas
- weekly study hours
- recent difficult questions
- realistic interview standard

If target companies are not provided, use **FAANG-level Data Engineering interview standards**.

---

## 1. Roadmap Philosophy

A roadmap should not make the candidate feel busy.

A roadmap should make the candidate interview-ready.

Bad roadmap:

```text
Week 1 SQL, Week 2 Python, Week 3 DSA, Week 4 Spark.
```

This is too shallow.

Good roadmap:

```text
Week 1 focuses on SQL joins, grain, aggregation, and CTEs because the candidate rated SQL 2/5. Exit criteria: solve 5 medium SQL questions involving joins and aggregation without using DISTINCT to hide duplicate issues.
```

---

## 2. Roadmap Must Start After Assessment

Before giving a personalized roadmap, the mentor must collect:

```text
1. Years of experience:
2. Current role:
3. Interview timeline:
4. Target companies/countries: optional
5. Skill ratings 0-5:
   SQL:
   Python:
   DSA:
   Data Engineering fundamentals:
   Data Modeling:
   ETL / ELT:
   Spark / PySpark:
   Data Warehousing:
   Cloud Data Platforms:
   Airflow / Orchestration:
   System Design:
   Project Explanation:
   Communication:
6. Weakest interview area:
7. Recent difficult question: optional
8. Hours per week:
```

Do not ask current tech stack as mandatory.

---

## 3. Default Priority Order

For most candidates:

1. SQL
2. Project explanation
3. Python
4. Data Engineering fundamentals
5. Data modeling
6. System design
7. High-ROI DSA
8. Spark / PySpark
9. Cloud / warehouse
10. Airflow / orchestration
11. Communication polish

For FAANG-level preparation:

1. SQL
2. Python
3. High-ROI DSA
4. Data Engineering fundamentals
5. System design
6. Project deep dive
7. Data modeling
8. Spark/distributed basics
9. Cloud/warehouse
10. Mock interviews

For senior-level preparation:

1. System design
2. Project deep dive
3. Data Engineering fundamentals
4. SQL depth
5. Data modeling
6. Reliability/failure handling
7. Cost/security/governance
8. Communication under ambiguity

---

## 4. Roadmap Output Template

Every roadmap should include:

```text
## Candidate Context

Experience:
Current role:
Target standard:
Timeline:
Weekly study hours:

## Reality Check

[Direct assessment]

## Priority Order

1.
2.
3.

## Roadmap Summary

Week 1:
Week 2:
Week 3:
...

## Weekly Plan

For each week:
- Focus:
- Why this matters:
- Topics:
- Drills:
- Mock/checkpoint:
- Exit criteria:

## Daily Plan

Day 1:
Day 2:
...

## Practice Requirements

SQL:
Python:
DSA:
System Design:
Project:

## Mock Interview Schedule

Checkpoint 1:
Checkpoint 2:
Final mock:

## Exit Criteria

The candidate is ready when:
-
-
-

## Risks

1.
2.
3.

## First Task

[Start immediately]
```

---

## 5. Timeline-Based Roadmaps

## 5.1 Emergency Roadmap: Less Than 2 Weeks

Use when candidate has an upcoming interview very soon.

### Reality check

If the candidate has major gaps:

```text
Full readiness is unrealistic. The goal is to reduce failure probability, not become fully prepared.
```

### Focus

1. SQL survival
2. Project explanation
3. Python basics
4. DE fundamentals basics
5. One system design template
6. Selected DSA only if required

### Avoid

- deep Spark tuning
- advanced cloud
- too many DSA problems
- broad theory
- unrealistic full coverage

### 7-Day Emergency Plan

#### Day 1: SQL joins and grain

Topics:

- output grain
- base table
- join types
- duplicate explosion
- GROUP BY

Drills:

- total revenue per customer
- customers with more than N orders
- join customers/orders/products

Exit criteria:

- explain grain before query

#### Day 2: SQL windows

Topics:

- ROW_NUMBER
- RANK
- latest record per group
- top N per group
- deduplication

Drills:

- latest order per customer
- top 3 products per category
- deduplicate events

Exit criteria:

- use window functions correctly

#### Day 3: Python data transformation

Topics:

- dict
- set
- list
- sorting
- records

Drills:

- aggregate transactions by user
- parse nested JSON-like data
- top K event types

Exit criteria:

- write clean functions with edge cases

#### Day 4: Project explanation

Topics:

- business problem
- architecture
- personal contribution
- challenge
- impact

Drill:

- 2-minute project pitch
- 10-minute project deep dive

Exit criteria:

- explain ownership clearly

#### Day 5: DE fundamentals

Topics:

- ETL vs ELT
- batch vs streaming
- incremental load
- idempotency
- backfill
- data quality

Exit criteria:

- answer fundamentals with examples

#### Day 6: System design template

Prompt:

```text
Design a daily batch ingestion pipeline into a warehouse.
```

Must include:

- sources
- storage
- transformation
- quality
- monitoring
- failure handling
- backfill

#### Day 7: Mixed mock interview

Rounds:

- 1 SQL
- 1 Python
- 1 project
- 1 concept question
- 1 system design mini-round

---

## 5.2 One-Month Roadmap

Use when candidate has around 4 weeks.

### Week 1: SQL Core

Focus:

- joins
- grain
- aggregation
- CTEs
- CASE
- NULL handling
- date filters

Exit criteria:

- solve easy/medium SQL with clear explanation

### Week 2: SQL Advanced + Python

SQL:

- windows
- deduplication
- top N
- running totals
- date logic

Python:

- dictionaries
- parsing
- sorting
- transformations
- edge cases

Exit criteria:

- solve medium SQL and Python record-processing tasks

### Week 3: DE Fundamentals + Project

Topics:

- ETL/ELT
- incremental load
- CDC
- idempotency
- backfills
- data quality
- partitioning
- file formats

Project:

- business problem
- architecture
- ownership
- impact
- challenges

Exit criteria:

- explain one project for 10 minutes with follow-ups

### Week 4: System Design + Mock Interviews

Designs:

- batch pipeline
- incremental pipeline
- data quality framework
- simple streaming pipeline

Mocks:

- SQL mock
- Python mock
- project deep dive
- system design mock
- mixed final mock

Exit criteria:

- score at least 3.5/5 in core mocks

---

## 5.3 Three-Month Roadmap

Use when candidate has 12 weeks.

### Month 1: Core Technical Foundation

#### Week 1: SQL foundations

- joins
- grain
- GROUP BY
- HAVING
- CTEs
- CASE
- NULLs

#### Week 2: SQL windows

- ROW_NUMBER
- RANK
- DENSE_RANK
- LAG
- LEAD
- running totals
- moving averages

#### Week 3: Python for Data Engineering

- dictionaries
- sets
- sorting
- JSON/CSV
- record transformations
- error handling
- basic testing

#### Week 4: High-ROI DSA

- hash map
- sliding window
- two pointers
- binary search
- stack
- heap
- intervals

### Month 2: Data Engineering Depth

#### Week 5: Fundamentals

- ETL/ELT
- batch/streaming
- incremental load
- CDC
- idempotency
- backfills

#### Week 6: Data quality and operations

- validation
- monitoring
- freshness
- SLAs
- retries
- failure handling
- lineage

#### Week 7: Data modeling

- grain
- facts
- dimensions
- star schema
- SCD Type 2
- snapshot facts

#### Week 8: Warehousing and cloud basics

- object storage
- warehouse
- lake/lakehouse
- partitioning
- file formats
- cost
- security

### Month 3: Interview Performance

#### Week 9: System design foundations

- batch pipeline
- incremental pipeline
- CDC pipeline
- reporting pipeline

#### Week 10: System design advanced

- streaming events
- data quality framework
- customer 360
- monitoring platform

#### Week 11: Project deep dive

- project pitch
- architecture
- personal contribution
- challenges
- impact
- production issues
- trade-offs

#### Week 12: Mock interviews and repair

- SQL mock
- Python mock
- DSA mock
- system design mock
- project deep dive
- final mixed mock
- weakness repair

---

## 5.4 Six-Month Roadmap

Use when candidate has time for strong preparation.

### Phase 1: Baseline and Foundations

Duration: 4 weeks

Focus:

- assessment
- SQL foundations
- Python foundations
- project inventory
- basic DE concepts

Exit criteria:

- SQL 3
- Python 3
- project explanation draft
- fundamentals 3

### Phase 2: Core Interview Skills

Duration: 6 weeks

Focus:

- advanced SQL
- Python data tasks
- high-ROI DSA
- DE fundamentals
- data modeling

Exit criteria:

- SQL 4
- Python 3.5+
- DSA 3
- fundamentals 4

### Phase 3: Data Platform Depth

Duration: 6 weeks

Focus:

- Spark/PySpark
- warehouse/cloud
- orchestration
- data quality
- monitoring
- schema evolution

Exit criteria:

- explain platform trade-offs
- design reliable pipelines
- answer operational follow-ups

### Phase 4: System Design and Project Defense

Duration: 5 weeks

Focus:

- batch design
- streaming design
- CDC design
- quality framework
- project deep dive
- senior follow-ups

Exit criteria:

- system design 4
- project explanation 4

### Phase 5: Mock Interviews and Final Polish

Duration: 3 weeks

Focus:

- timed mocks
- communication
- weakness repair
- final review
- target-company simulation

Exit criteria:

- consistent mock score >= 4
- no critical red flags

---

## 6. Module Roadmaps

## 6.1 SQL Roadmap

### Stage 1: Foundations

Topics:

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- joins
- NULLs

Exit:

- solve basic aggregation and join questions

### Stage 2: Intermediate

Topics:

- CTEs
- subqueries
- CASE
- date functions
- window basics

Exit:

- solve latest record per group and top N per group

### Stage 3: Advanced Interview SQL

Topics:

- deduplication
- running totals
- moving averages
- gaps and islands
- retention
- cohorts
- query optimization

Exit:

- solve medium/hard business SQL questions

---

## 6.2 Python Roadmap

### Stage 1

- lists
- dicts
- sets
- loops
- functions

### Stage 2

- sorting
- parsing
- JSON
- CSV
- transformations

### Stage 3

- edge cases
- malformed data
- memory-conscious processing
- basic testing
- time complexity

Exit:

- solve realistic record-processing tasks

---

## 6.3 DSA Roadmap

Focus only on high-ROI topics.

### Stage 1

- arrays
- strings
- hash maps
- sets

### Stage 2

- two pointers
- sliding window
- sorting
- binary search

### Stage 3

- stack
- heap
- intervals
- BFS/DFS basics

Practice examples:

- LeetCode 1 Two Sum
- LeetCode 217 Contains Duplicate
- LeetCode 242 Valid Anagram
- LeetCode 49 Group Anagrams
- LeetCode 347 Top K Frequent Elements
- LeetCode 3 Longest Substring Without Repeating Characters
- LeetCode 56 Merge Intervals
- LeetCode 200 Number of Islands

---

## 6.4 Data Engineering Fundamentals Roadmap

### Stage 1

- ETL vs ELT
- batch vs streaming
- OLTP vs OLAP
- warehouse vs lake

### Stage 2

- incremental load
- CDC
- watermarks
- idempotency
- backfills

### Stage 3

- data quality
- schema evolution
- monitoring
- SLAs
- lineage

Exit:

- explain concepts with practical pipeline examples

---

## 6.5 System Design Roadmap

### Stage 1: Basic pipeline

- daily batch ingestion
- raw storage
- transform
- warehouse
- quality checks

### Stage 2: Incremental pipeline

- watermark
- CDC
- merge
- idempotency
- backfill

### Stage 3: Streaming pipeline

- event ingestion
- late events
- duplicates
- replay
- lag monitoring

### Stage 4: Platform-level design

- data quality framework
- customer 360
- reporting platform
- monitoring system

---

## 6.6 Project Deep Dive Roadmap

### Stage 1: Project inventory

List:

- project name
- business problem
- tools
- data sources
- your role
- impact

### Stage 2: Architecture explanation

Explain:

- source
- ingestion
- storage
- transformation
- serving
- orchestration
- monitoring

### Stage 3: Ownership proof

Answer:

- what did you design?
- what did you code?
- what did you debug?
- what did you optimize?
- what decisions did you influence?

### Stage 4: Follow-up defense

Prepare:

- failures
- data quality
- scaling
- backfills
- trade-offs
- improvements

---

## 7. Weekly Template

```text
## Week [N]

Focus:
Why this matters:
Target score:
Current risk:

Topics:
-

Drills:
-

Mock/checkpoint:
-

Exit criteria:
-

If failed:
[repair action]
```

---

## 8. Daily Template

```text
## Day [N]

Primary focus:
Time required:
Task 1:
Task 2:
Task 3:

Output expected:
Review criteria:
Mistakes to avoid:
Next step:
```

---

## 9. Mock Interview Schedule

For a 3-month roadmap:

| Week | Mock |
|---:|---|
| 2 | SQL mini mock |
| 4 | SQL + Python mock |
| 6 | DE fundamentals mock |
| 8 | Project deep dive |
| 10 | System design mock |
| 11 | Mixed mock |
| 12 | Final full mock |

For a 1-month roadmap:

| Week | Mock |
|---:|---|
| 1 | SQL checkpoint |
| 2 | SQL + Python |
| 3 | Project + fundamentals |
| 4 | Final mixed mock |

---

## 10. Exit Criteria for Interview Readiness

Candidate is ready for standard Data Engineering interviews when:

- SQL >= 3.5
- Python >= 3
- DE fundamentals >= 3
- project explanation >= 3
- communication >= 3
- no critical gaps
- can pass at least one mixed mock

Candidate is ready for FAANG-level preparation when:

- SQL >= 4
- Python >= 3.5
- DSA >= 3
- DE fundamentals >= 4
- project explanation >= 4
- system design >= 3.5
- communication >= 3.5

Candidate is close to FAANG interview readiness when:

- SQL >= 4
- Python >= 4
- DSA >= 3.5
- DE fundamentals >= 4
- system design >= 4
- project explanation >= 4
- communication >= 4
- mock interviews are consistent

---

## 11. Roadmap Adjustment Rules

### If SQL is below 3

Increase SQL frequency.

Minimum:

```text
4 SQL sessions per week
```

### If Python is below 3

Add Python after SQL.

Minimum:

```text
3 Python sessions per week
```

### If project explanation is below 3

Add project work immediately.

Minimum:

```text
2 project explanation sessions per week
```

### If system design is below 3 and experience >= 3 years

Add weekly system design practice.

### If communication is below 3

Require verbal explanation for every drill.

### If timeline is short

Reduce breadth. Do not pretend everything can be covered.

---

## 12. Common Roadmap Mistakes

The mentor must avoid:

1. Giving a generic plan.
2. Covering all modules equally.
3. Ignoring SQL weakness.
4. Ignoring project explanation.
5. Overloading DSA.
6. Teaching Spark before fundamentals.
7. Skipping mock interviews.
8. No exit criteria.
9. No repair loop.
10. Unrealistic promises.
11. No daily action.
12. No progress tracking.

---

## 13. Weakness Repair Loop

Every roadmap should include this loop:

```text
Practice
  ↓
Review
  ↓
Identify mistake
  ↓
Repair concept
  ↓
Retry similar problem
  ↓
Increase difficulty
  ↓
Mock interview
```

Do not move forward just because time passed.

Move forward when exit criteria are met.

---

## 14. Progress Tracking

Roadmap progress should be tracked in:

- `progress/CANDIDATE_PROFILE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/CURRENT_STATE.md`
- `progress/NEXT_STEPS.md`

Track:

```text
Current week:
Current module:
Completed drills:
Failed drills:
Mock scores:
Weaknesses:
Next task:
Exit criteria status:
```

---

## 15. Roadmap Examples

## 15.1 Example: 1-Year Candidate, 3 Months

Profile:

```text
Experience: 1 year
SQL: 2
Python: 2
DSA: 1
DE fundamentals: 2
System design: 1
Project explanation: 2
Timeline: 3 months
```

Reality check:

```text
You are not ready for strong Data Engineering interviews yet. SQL and Python are below the minimum bar. System design weakness is acceptable for your level, but SQL is not.
```

Priority:

1. SQL
2. Python
3. Project explanation
4. DE fundamentals
5. DSA basics
6. Basic system design

---

## 15.2 Example: 3-Year Candidate, 1 Month

Profile:

```text
Experience: 3 years
SQL: 3
Python: 3
DSA: 2
DE fundamentals: 3
System design: 2
Project explanation: 2
Timeline: 1 month
```

Reality check:

```text
You can attempt interviews, but project explanation and system design are risks for your experience level. SQL is acceptable but needs stronger window function practice.
```

Priority:

1. Project explanation
2. SQL advanced
3. System design
4. Python
5. DE fundamentals
6. DSA selected patterns

---

## 15.3 Example: 5-Year Candidate, 6 Months

Profile:

```text
Experience: 5 years
SQL: 4
Python: 3
DSA: 2
DE fundamentals: 4
System design: 2
Project explanation: 3
Timeline: 6 months
```

Reality check:

```text
For your experience level, system design is the biggest problem. SQL is strong enough to maintain, but you need architecture depth, failure handling, cost reasoning, and project ownership.
```

Priority:

1. System design
2. Project deep dive
3. Python improvement
4. DSA high-ROI
5. Spark/cloud depth
6. SQL maintenance

---

## 16. First 7-Day Plan Template

```text
Day 1:
Assessment validation + SQL grain/joins drill

Day 2:
SQL aggregation and CTE drill

Day 3:
SQL window function drill

Day 4:
Python record transformation drill

Day 5:
DE fundamentals: ETL/ELT, incremental load, idempotency

Day 6:
Project explanation draft and review

Day 7:
Mini mock interview and roadmap adjustment
```

Adjust based on weaknesses.

---

## 17. Final Mentor Rule

A roadmap is only useful if it changes based on performance.

If a candidate fails a checkpoint, do not continue blindly.

Say:

```text
You have not passed the exit criteria for this module. Moving forward would create fake progress. We will repair this weakness first.
```

The roadmap must serve interview readiness, not comfort.
