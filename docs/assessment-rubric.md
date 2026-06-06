# Assessment Rubric for Data Engineering Sensei

Generated: 2026-06-06

This file defines how **Data Engineering Sensei** should assess a candidate for Data Engineering interview readiness.

The rubric is intentionally strict. The goal is not to make the candidate feel good. The goal is to identify the truth about their current interview readiness and give a precise repair path.

This rubric should be used by:

- `SKILL.md`
- `modes/profile-assessment-mode.md`
- `modes/roadmap-mode.md`
- `modes/review-mode.md`
- `modes/interview-mode.md`
- `modes/weakness-repair-mode.md`
- `templates/interview-feedback/mock-interview-feedback-template.md`
- `progress/CANDIDATE_PROFILE.md`
- `progress/ROADMAP_PROGRESS.md`

---

## 1. Purpose

The purpose of this rubric is to classify the candidate across the skills required for Data Engineering interviews.

The mentor should use this rubric to answer:

1. What level is the candidate currently at?
2. What interview rounds are they likely to pass?
3. What interview rounds are they likely to fail?
4. What topics are urgent?
5. What topics can wait?
6. What is the candidate’s realistic readiness level?
7. What should be trained first?
8. What is the exit criteria for improvement?

---

## 2. Assessment Philosophy

### 2.1 Be Honest

Do not inflate scores.

A candidate who knows definitions but cannot answer follow-ups is not interview-ready.

A candidate who can write code but cannot explain trade-offs is not interview-ready for stronger companies.

A candidate who can name tools but cannot design a failure-safe pipeline is not system-design ready.

### 2.2 Judge by Interview Performance

Assess based on what the candidate can do under interview conditions:

- Can they clarify requirements?
- Can they explain their approach?
- Can they solve accurately?
- Can they handle edge cases?
- Can they reason about performance?
- Can they recover after mistakes?
- Can they answer follow-ups?
- Can they explain project ownership?

Do not assess only based on what the candidate claims.

### 2.3 Use Experience-Level Expectations

The same answer can be acceptable for a fresher and weak for a 5-year candidate.

Example:

```text
A beginner not knowing CDC deeply is acceptable.
A 4-year Data Engineer not knowing CDC, incremental load, and idempotency is a serious risk.
```

### 2.4 Prioritize Interview-Critical Areas

For most Data Engineering interviews, the highest priority areas are:

1. SQL
2. Python
3. Data Engineering fundamentals
4. Project explanation
5. System design
6. High-ROI DSA
7. Data modeling
8. Spark / PySpark
9. Warehousing / Cloud
10. Airflow / Orchestration

The exact order can change based on experience, target company, and timeline.

---

## 3. Candidate Intake Fields

The assessment should start with this information:

```text
1. Years of experience in Data Engineering or related data roles:
2. Current role:
3. Interview timeline:
4. Target companies or countries: optional
5. Skill ratings from 0 to 5:
   - SQL
   - Python
   - DSA
   - Data Engineering fundamentals
   - Data Modeling
   - ETL / ELT Pipelines
   - Spark / PySpark
   - Data Warehousing
   - Cloud Data Platforms
   - Airflow / Orchestration
   - Data Engineering System Design
   - Project Explanation
   - Communication
6. Weakest interview area:
7. Recent difficult interview question: optional
8. Hours per week available for study:
```

Do not require current tech stack during intake.

Target companies/countries are optional. If missing, use FAANG-level Data Engineering interview standards.

---

## 4. Global 0-5 Skill Scale

Use this scale for every module.

| Score | Label | Meaning |
|---:|---|---|
| 0 | No knowledge | Cannot explain or solve even basic questions |
| 1 | Beginner | Knows a few terms but cannot answer interview follow-ups |
| 2 | Basic | Can answer simple questions but not reliably interview-ready |
| 3 | Developing | Can handle some medium questions with gaps |
| 4 | Interview-ready | Can pass many standard interviews in this area |
| 5 | Strong | Can handle difficult follow-ups and explain trade-offs clearly |

---

## 5. Score Meaning by Interview Risk

### Score 0

The candidate has no usable interview knowledge in this area.

Expected behavior:

- start from fundamentals
- avoid advanced drills
- do not schedule mock interviews in this module yet
- give beginner roadmap

Interview risk:

```text
Critical
```

### Score 1

The candidate has surface-level familiarity.

Expected behavior:

- teach definitions
- use simple examples
- ask basic explanation checks
- correct misconceptions early

Interview risk:

```text
Very high
```

### Score 2

The candidate has basic knowledge but is not reliable.

Expected behavior:

- drill easy to medium problems
- review explanations
- force edge cases
- build pattern recognition

Interview risk:

```text
High
```

### Score 3

The candidate can perform with support but has gaps.

Expected behavior:

- drill medium problems
- add follow-ups
- increase pressure
- identify weak subtopics

Interview risk:

```text
Moderate
```

### Score 4

The candidate is ready for many standard interviews.

Expected behavior:

- polish speed and communication
- run mock interviews
- train follow-up handling
- target advanced weak spots

Interview risk:

```text
Low to moderate
```

### Score 5

The candidate is strong.

Expected behavior:

- use hard follow-ups
- simulate senior-level ambiguity
- test trade-offs and edge cases
- maintain sharpness

Interview risk:

```text
Low
```

---

## 6. Experience Bands

| Years of Experience | Level |
|---:|---|
| 0 - 1 | Beginner / Entry-Level |
| 1 - 2 | Junior Data Engineer |
| 2 - 4 | Mid-Level Data Engineer |
| 4 - 7 | Experienced Data Engineer |
| 7+ | Senior Data Engineer |

---

## 7. Experience-Level Expectations

## 7.1 Beginner / Entry-Level Candidate

Expected baseline:

- SQL basics
- Python basics
- basic DSA patterns
- basic ETL understanding
- simple project explanation
- willingness to learn

Not expected:

- deep system design
- advanced Spark tuning
- complex warehouse architecture
- production ownership

Strict feedback rule:

```text
Be direct, but do not judge them against senior standards.
```

Minimum interview target:

```text
Entry-level Data Engineer / Data Analyst Engineer / Junior Data Engineer
```

---

## 7.2 Junior Data Engineer Candidate

Expected baseline:

- joins, aggregation, CTEs
- basic window functions
- Python dictionaries/lists/sets
- simple data transformations
- basic ETL/ELT concepts
- simple pipeline explanation
- easy/medium DSA patterns

Weaknesses that are serious:

- cannot write joins
- cannot explain GROUP BY
- cannot use dictionaries in Python
- cannot explain their own project
- no understanding of incremental load

Minimum interview target:

```text
Junior Data Engineer roles and some standard Data Engineer I roles
```

---

## 7.3 Mid-Level Data Engineer Candidate

Expected baseline:

- strong SQL including windows
- Python data processing
- high-ROI DSA easy/medium
- ETL/ELT trade-offs
- data modeling basics
- Spark basics if in job description
- project ownership
- basic system design

Weaknesses that are serious:

- SQL below 3
- project explanation below 3
- cannot explain incremental load
- cannot discuss failure handling
- cannot design a batch pipeline
- cannot reason about duplicates or data quality

Minimum interview target:

```text
Data Engineer II / Mid-Level Data Engineer roles
```

---

## 7.4 Experienced Data Engineer Candidate

Expected baseline:

- advanced SQL
- strong Python
- production pipeline reasoning
- data modeling
- Spark/distributed basics
- warehouse/cloud reasoning
- orchestration
- data quality
- monitoring
- system design
- strong project ownership

Weaknesses that are serious:

- cannot explain architecture trade-offs
- cannot discuss monitoring/failure/backfill
- weak SQL
- weak project ownership
- tool listing without reasoning
- cannot explain scaling or cost

Minimum interview target:

```text
Senior-ish Data Engineer roles, Data Engineer III, platform-oriented roles
```

---

## 7.5 Senior Data Engineer Candidate

Expected baseline:

- ambiguous requirement handling
- architecture leadership
- cross-team trade-offs
- platform thinking
- governance
- reliability
- cost optimization
- mentoring
- deep incident/project stories
- strong system design

Weaknesses that are serious:

- no ownership examples
- cannot design under ambiguity
- cannot defend trade-offs
- cannot explain governance/security basics
- cannot reason about reliability and scale
- weak communication

Minimum interview target:

```text
Senior Data Engineer / Staff-track preparation depending on depth
```

---

## 8. Readiness Verdicts

Use one final verdict after assessment.

| Verdict | Meaning |
|---|---|
| Not interview-ready | Major gaps in core areas |
| Partially interview-ready | Can attempt interviews but likely to fail stronger rounds |
| Interview-ready for standard companies | Can pass many normal DE interviews |
| FAANG-prep ready | Strong foundation, needs pressure testing and tough drills |
| FAANG-interview ready | Strong across SQL, Python, DSA, DE concepts, system design, and projects |

---

## 9. Verdict Rules

### 9.1 Not Interview-Ready

Use this when:

- SQL <= 1, or
- Python <= 1, or
- DE fundamentals <= 1, or
- project explanation <= 1 for experienced candidates, or
- candidate cannot explain basic work clearly

Example response:

```text
You are not interview-ready yet. The main issue is not effort; it is that your core interview skills are below the minimum bar. We need to fix SQL, Python basics, and project explanation first.
```

---

### 9.2 Partially Interview-Ready

Use this when:

- SQL is around 2
- Python is around 2
- candidate can handle basics but fails follow-ups
- system design is weak
- project explanation is incomplete
- DSA is weak but not blocking for all roles

Example response:

```text
You can start applying selectively, but you should expect failures in stronger rounds. Your current profile needs targeted repair before high-standard interviews.
```

---

### 9.3 Interview-Ready for Standard Companies

Use this when:

- SQL >= 3
- Python >= 3
- DE fundamentals >= 3
- project explanation >= 3
- communication >= 3
- candidate can handle medium-level questions with some gaps

Example response:

```text
You are ready for many standard Data Engineering interviews, but not yet at FAANG-level. The next step is stronger SQL, system design, and follow-up handling.
```

---

### 9.4 FAANG-Prep Ready

Use this when:

- SQL >= 4
- Python >= 3
- DSA >= 3
- DE fundamentals >= 4
- project explanation >= 4
- system design >= 3
- communication >= 3

Example response:

```text
You have the foundation to start FAANG-level preparation. Now the focus should be speed, depth, follow-ups, and mock interviews.
```

---

### 9.5 FAANG-Interview Ready

Use this only when:

- SQL >= 4
- Python >= 4
- DSA >= 3 or 4 depending on target
- DE fundamentals >= 4
- system design >= 4
- project explanation >= 4
- communication >= 4
- candidate performs well in mock interviews

Example response:

```text
You are close to FAANG-level readiness. The remaining risk is not knowledge, but consistency under pressure and handling unexpected follow-ups.
```

Do not give this verdict based only on self-rating. Confirm with drills or mock interviews.

---

## 10. Module Weights

Default weighting for Data Engineering interview readiness:

| Module | Weight |
|---|---:|
| SQL | 25% |
| Python | 15% |
| Data Engineering Fundamentals | 15% |
| Project Explanation | 15% |
| System Design | 10% |
| DSA | 8% |
| Data Modeling | 5% |
| Spark / PySpark | 3% |
| Warehousing / Cloud | 2% |
| Airflow / Orchestration | 2% |

These weights can change for specific roles.

### FAANG-Level Weighting

| Module | Weight |
|---|---:|
| SQL | 25% |
| Python | 18% |
| DSA | 15% |
| Data Engineering Fundamentals | 15% |
| System Design | 12% |
| Project Explanation | 10% |
| Data Modeling | 3% |
| Spark / Cloud / Orchestration | 2% |

### Senior-Level Weighting

| Module | Weight |
|---|---:|
| System Design | 20% |
| Project Explanation | 18% |
| Data Engineering Fundamentals | 18% |
| SQL | 15% |
| Python | 10% |
| Data Modeling | 8% |
| Spark / Cloud / Orchestration | 8% |
| DSA | 3% |

---

## 11. SQL Rubric

SQL is a top-priority skill.

For most Data Engineering interviews, weak SQL is a serious risk.

### SQL Score 0

Candidate cannot write basic SELECT queries.

Can’t reliably use:

- SELECT
- WHERE
- ORDER BY
- simple filters

Verdict:

```text
Critical gap
```

Action:

```text
Start with SQL basics immediately.
```

---

### SQL Score 1

Candidate can write simple SELECT queries but struggles with joins and aggregation.

May know:

- SELECT
- WHERE
- simple ORDER BY

Struggles with:

- GROUP BY
- HAVING
- joins
- NULLs
- date filters

Interview risk:

```text
Very high
```

---

### SQL Score 2

Candidate can solve easy SQL but fails medium questions.

Can handle:

- basic joins
- GROUP BY
- simple CTEs

Struggles with:

- window functions
- deduplication
- latest record per group
- top N per group
- date logic
- retention/cohort queries
- query explanation

Interview risk:

```text
High
```

---

### SQL Score 3

Candidate can handle some medium SQL.

Can handle:

- joins
- CTEs
- aggregation
- basic windows
- ROW_NUMBER use cases

Still weak in:

- gaps and islands
- retention
- performance reasoning
- complex multi-step queries
- edge cases

Interview risk:

```text
Moderate
```

---

### SQL Score 4

Candidate is interview-ready for most SQL rounds.

Can handle:

- window functions
- deduplication
- top N
- running totals
- date logic
- multi-CTE queries
- business-style SQL
- explain query logic clearly

Still may need:

- speed
- advanced optimization
- hard follow-ups

Interview risk:

```text
Low to moderate
```

---

### SQL Score 5

Candidate is strong.

Can handle:

- difficult SQL problems
- ambiguous business logic
- query optimization reasoning
- edge cases
- performance trade-offs
- dialect differences
- explaining under pressure

Interview risk:

```text
Low
```

---

## 12. SQL Subskill Checklist

Score each SQL subskill from 0 to 5 if detailed assessment is needed.

| Subskill | Score |
|---|---:|
| Basic SELECT/filtering | /5 |
| Joins | /5 |
| Aggregation | /5 |
| CTEs/subqueries | /5 |
| Window functions | /5 |
| Deduplication | /5 |
| Date/time logic | /5 |
| Gaps and islands | /5 |
| Retention/cohort queries | /5 |
| Query optimization | /5 |
| Explanation clarity | /5 |

### SQL Minimum Passing Standard

Candidate must be able to:

- identify output grain
- choose base table
- choose correct join type
- avoid duplicate explosion
- aggregate at correct level
- use CTEs for clarity
- use window functions
- handle NULLs
- handle date boundaries
- explain query logic

If they cannot do these, they are not SQL-interview-ready.

---

## 13. Python Rubric

Python is required for coding and data-processing rounds.

### Python Score 0

Candidate cannot write basic Python.

Struggles with:

- variables
- loops
- functions
- lists

Verdict:

```text
Critical gap
```

---

### Python Score 1

Candidate can write simple scripts but lacks confidence.

Can handle:

- simple loops
- basic lists
- basic functions

Struggles with:

- dictionaries
- sets
- parsing
- sorting
- edge cases

Interview risk:

```text
Very high
```

---

### Python Score 2

Candidate can solve easy Python tasks but not reliable for interviews.

Can handle:

- list operations
- simple dicts
- basic string operations

Struggles with:

- nested data
- JSON records
- CSV-style input
- custom sorting
- complexity
- malformed data

Interview risk:

```text
High
```

---

### Python Score 3

Candidate can handle medium data-processing tasks with some gaps.

Can handle:

- dictionaries
- sets
- sorting
- parsing
- transformations
- simple aggregations

Needs improvement in:

- clean code
- edge cases
- testing
- memory-conscious logic
- robust error handling

Interview risk:

```text
Moderate
```

---

### Python Score 4

Candidate is interview-ready for most Python rounds.

Can handle:

- realistic record-processing questions
- JSON/CSV-like data
- dict/set optimized logic
- custom sorting
- clean functions
- complexity explanation
- edge cases

Interview risk:

```text
Low to moderate
```

---

### Python Score 5

Candidate is strong.

Can handle:

- messy data
- streaming-like constraints
- memory trade-offs
- generators when needed
- clean abstraction
- testability
- follow-up variations

Interview risk:

```text
Low
```

---

## 14. Python Subskill Checklist

| Subskill | Score |
|---|---:|
| Lists/tuples | /5 |
| Dictionaries | /5 |
| Sets | /5 |
| Functions | /5 |
| String parsing | /5 |
| Sorting/custom keys | /5 |
| JSON handling | /5 |
| CSV/file-style processing | /5 |
| Error handling | /5 |
| Basic testing | /5 |
| Pandas basics | /5 |
| Complexity explanation | /5 |
| Code readability | /5 |

### Python Minimum Passing Standard

Candidate must be able to:

- write clean functions
- use dict/set/list correctly
- parse records
- handle missing fields
- transform data
- aggregate data
- avoid unnecessary nested loops
- explain time and space complexity

---

## 15. DSA Rubric

DSA should be high-ROI and Data Engineering relevant.

### DSA Score 0

Candidate cannot solve basic array/string problems.

Verdict:

```text
Critical if target companies ask coding rounds
```

---

### DSA Score 1

Candidate knows some basics but cannot solve without help.

Struggles with:

- hash maps
- two pointers
- sliding window
- complexity

---

### DSA Score 2

Candidate can solve easy problems but struggles with medium.

Can handle:

- simple arrays
- simple strings
- basic hash map

Struggles with:

- sliding window
- binary search
- heap
- intervals
- BFS/DFS

---

### DSA Score 3

Candidate can solve common easy and some medium problems.

Can handle:

- hash map
- sorting
- two pointers
- basic sliding window
- stack
- simple binary search

Needs improvement:

- speed
- pattern recognition
- edge cases
- explaining complexity

---

### DSA Score 4

Candidate is ready for most DE DSA rounds.

Can handle:

- common easy/medium problems
- hash maps
- sliding window
- binary search
- intervals
- heap basics
- BFS/DFS basics
- top K

---

### DSA Score 5

Candidate is strong for DE interviews.

Can handle:

- unfamiliar medium problems
- pressure
- follow-ups
- trade-offs
- alternative approaches

Advanced competitive-programming topics are not required unless target role demands them.

---

## 16. DSA Subskill Checklist

| Subskill | Score |
|---|---:|
| Arrays | /5 |
| Strings | /5 |
| Hash maps | /5 |
| Sorting | /5 |
| Binary search | /5 |
| Two pointers | /5 |
| Sliding window | /5 |
| Stack/queue | /5 |
| Heap/top K | /5 |
| Intervals | /5 |
| BFS/DFS basics | /5 |
| Complexity explanation | /5 |

### DSA Minimum Passing Standard

Candidate must be able to solve and explain common patterns:

- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements
- Longest Substring Without Repeating Characters
- Valid Parentheses
- Merge Intervals
- Number of Islands
- Binary Search

---

## 17. Data Engineering Fundamentals Rubric

### DE Fundamentals Score 0

Candidate cannot explain basic pipeline concepts.

Does not know:

- ETL
- batch
- warehouse
- pipeline

---

### DE Fundamentals Score 1

Candidate knows terms but not practical meaning.

May define ETL but cannot explain:

- why it matters
- where failures happen
- how data is validated
- how incremental loads work

---

### DE Fundamentals Score 2

Candidate can explain basics but fails follow-ups.

Knows:

- ETL vs ELT
- batch vs streaming
- warehouse vs lake

Struggles with:

- CDC
- idempotency
- backfills
- retries
- schema evolution
- data quality

---

### DE Fundamentals Score 3

Candidate can handle standard concept questions.

Can explain:

- incremental load
- partitioning
- file formats
- data quality checks
- basic monitoring
- retries

Needs improvement:

- trade-offs
- failure cases
- production examples

---

### DE Fundamentals Score 4

Candidate is interview-ready.

Can explain:

- CDC
- idempotency
- backfills
- schema evolution
- SLAs
- data freshness
- monitoring
- lineage
- at-least-once vs exactly-once basics
- file format trade-offs

---

### DE Fundamentals Score 5

Candidate is strong.

Can reason about:

- consistency
- reliability
- failure recovery
- cost
- scalability
- governance
- production trade-offs
- ambiguous scenarios

---

## 18. DE Fundamentals Subskill Checklist

| Subskill | Score |
|---|---:|
| ETL vs ELT | /5 |
| Batch vs streaming | /5 |
| Full vs incremental load | /5 |
| CDC | /5 |
| Idempotency | /5 |
| Backfills | /5 |
| Retries/failure handling | /5 |
| Data quality | /5 |
| Schema evolution | /5 |
| Partitioning | /5 |
| File formats | /5 |
| Monitoring/alerting | /5 |
| SLAs/freshness | /5 |
| Lineage/auditability | /5 |

### DE Fundamentals Minimum Passing Standard

Candidate must explain:

- ETL vs ELT
- batch vs streaming
- incremental load
- CDC
- idempotency
- backfills
- partitioning
- file formats
- data quality
- monitoring

---

## 19. Data Modeling Rubric

### Data Modeling Score 0

Candidate cannot explain facts, dimensions, or schema design.

---

### Data Modeling Score 1

Candidate has heard of star schema but cannot design one.

---

### Data Modeling Score 2

Candidate can explain facts and dimensions but struggles with grain and SCD.

---

### Data Modeling Score 3

Candidate can design simple star schemas.

Can identify:

- facts
- dimensions
- grain
- basic SCD Type 1/2

Needs improvement:

- late-arriving data
- snapshot facts
- query patterns
- trade-offs

---

### Data Modeling Score 4

Candidate is interview-ready.

Can explain:

- grain
- fact types
- dimension types
- SCD Type 2
- surrogate keys
- denormalization trade-offs
- query-driven modeling

---

### Data Modeling Score 5

Candidate is strong.

Can design under ambiguity and defend trade-offs across performance, history, cost, and usability.

---

## 20. Data Modeling Subskill Checklist

| Subskill | Score |
|---|---:|
| Normalization | /5 |
| Denormalization | /5 |
| Star schema | /5 |
| Snowflake schema | /5 |
| Fact tables | /5 |
| Dimension tables | /5 |
| Grain | /5 |
| Surrogate keys | /5 |
| Natural keys | /5 |
| SCD Type 1 | /5 |
| SCD Type 2 | /5 |
| Snapshot facts | /5 |
| Late-arriving data | /5 |
| Query-driven modeling | /5 |

### Modeling Minimum Passing Standard

Candidate must be able to:

- define grain
- identify facts
- identify dimensions
- explain SCD Type 2
- choose keys
- explain denormalization trade-offs

---

## 21. ETL / ELT Pipeline Rubric

### Pipeline Score 0

Candidate cannot explain a pipeline.

---

### Pipeline Score 1

Candidate can say “extract, transform, load” but lacks practical detail.

---

### Pipeline Score 2

Candidate can describe a simple pipeline but misses failure handling and incremental logic.

---

### Pipeline Score 3

Candidate can describe a standard batch pipeline.

Can explain:

- sources
- transformations
- destination
- schedule
- basic validation

Needs improvement:

- retries
- backfills
- idempotency
- monitoring
- late data

---

### Pipeline Score 4

Candidate is interview-ready.

Can explain:

- full vs incremental
- CDC
- validation
- retries
- idempotency
- backfills
- observability
- ownership

---

### Pipeline Score 5

Candidate is strong.

Can reason about:

- scale
- reliability
- cost
- failure recovery
- schema evolution
- multi-consumer design
- data contracts

---

## 22. Pipeline Subskill Checklist

| Subskill | Score |
|---|---:|
| Source ingestion | /5 |
| Transformations | /5 |
| Full load | /5 |
| Incremental load | /5 |
| CDC | /5 |
| Data validation | /5 |
| Idempotency | /5 |
| Retries | /5 |
| Backfills | /5 |
| Late-arriving data | /5 |
| Monitoring | /5 |
| SLA/freshness | /5 |
| Cost awareness | /5 |

---

## 23. Spark / PySpark Rubric

### Spark Score 0

Candidate has no Spark knowledge.

---

### Spark Score 1

Candidate has used Spark superficially but cannot explain execution.

---

### Spark Score 2

Candidate knows basic DataFrame operations but struggles with architecture.

---

### Spark Score 3

Candidate can explain:

- driver/executors
- transformations/actions
- lazy evaluation
- basic joins
- reading/writing Parquet

Needs improvement:

- shuffles
- partitioning
- skew
- caching
- optimization

---

### Spark Score 4

Candidate is interview-ready.

Can explain:

- narrow vs wide transformations
- shuffles
- broadcast joins
- partitioning
- repartition vs coalesce
- caching
- skew
- small files

---

### Spark Score 5

Candidate is strong.

Can reason about job performance, debugging, trade-offs, and production failure scenarios.

---

## 24. Spark Subskill Checklist

| Subskill | Score |
|---|---:|
| Driver/executors | /5 |
| Transformations/actions | /5 |
| Lazy evaluation | /5 |
| Narrow vs wide transformations | /5 |
| Shuffles | /5 |
| Joins | /5 |
| Broadcast joins | /5 |
| Partitioning | /5 |
| Repartition/coalesce | /5 |
| Caching | /5 |
| Skew handling | /5 |
| Small files problem | /5 |
| PySpark coding | /5 |

---

## 25. Data Warehousing Rubric

### Warehouse Score 0

Candidate cannot explain a data warehouse.

---

### Warehouse Score 1

Candidate knows warehouse as “place to store data” but lacks analytics concepts.

---

### Warehouse Score 2

Candidate understands warehouse basics but not partitioning, clustering, or cost.

---

### Warehouse Score 3

Candidate can explain:

- warehouse vs database
- lake vs warehouse
- columnar storage
- basic partitioning
- star schema relationship

---

### Warehouse Score 4

Candidate is interview-ready.

Can explain:

- partitioning
- clustering
- materialized views
- storage/compute separation
- cost-aware queries
- data marts

---

### Warehouse Score 5

Candidate is strong.

Can reason about performance, governance, cost, modeling, and platform trade-offs.

---

## 26. Warehouse Subskill Checklist

| Subskill | Score |
|---|---:|
| Warehouse vs database | /5 |
| Lake vs warehouse vs lakehouse | /5 |
| Columnar storage | /5 |
| Partitioning | /5 |
| Clustering | /5 |
| Materialized views | /5 |
| Cost-aware querying | /5 |
| Storage/compute separation | /5 |
| Data marts | /5 |
| Governance basics | /5 |

---

## 27. Cloud Data Platforms Rubric

Use cloud-agnostic assessment by default.

### Cloud Score 0

No cloud knowledge.

---

### Cloud Score 1

Knows names like AWS/GCP/Azure but cannot explain data services.

---

### Cloud Score 2

Can explain object storage and basic warehouse services but lacks design reasoning.

---

### Cloud Score 3

Can explain:

- object storage
- IAM basics
- warehouse services
- storage/compute
- basic cost concerns

---

### Cloud Score 4

Can reason across platforms.

Understands:

- S3/GCS/ADLS
- BigQuery/Snowflake/Redshift concepts
- security basics
- cost
- partitioning
- access control

---

### Cloud Score 5

Strong platform reasoning.

Can discuss:

- multi-environment architecture
- governance
- cost optimization
- security
- reliability
- service trade-offs

---

## 28. Cloud Subskill Checklist

| Subskill | Score |
|---|---:|
| Object storage | /5 |
| Warehouse services | /5 |
| IAM/access control | /5 |
| Encryption basics | /5 |
| Cost awareness | /5 |
| Batch ingestion services | /5 |
| Streaming services | /5 |
| Monitoring basics | /5 |
| Governance basics | /5 |
| Cross-cloud concept transfer | /5 |

---

## 29. Airflow / Orchestration Rubric

### Orchestration Score 0

Candidate does not know orchestration.

---

### Orchestration Score 1

Candidate has heard of DAGs but cannot explain scheduling/failure.

---

### Orchestration Score 2

Candidate can explain simple DAGs but misses retries/backfills/idempotency.

---

### Orchestration Score 3

Candidate can explain:

- DAG
- tasks
- dependencies
- schedules
- retries
- basic backfill

Needs improvement:

- sensors
- catchup
- idempotency
- alerting
- SLA

---

### Orchestration Score 4

Candidate is interview-ready.

Can explain:

- DAG design
- retries
- backfills
- catchup
- sensors
- failure handling
- alerting
- idempotent tasks

---

### Orchestration Score 5

Candidate is strong.

Can reason about complex workflows, reliability, environment management, and operational trade-offs.

---

## 30. Orchestration Subskill Checklist

| Subskill | Score |
|---|---:|
| DAGs | /5 |
| Tasks | /5 |
| Dependencies | /5 |
| Scheduling | /5 |
| Retries | /5 |
| Backfills | /5 |
| Catchup | /5 |
| Sensors | /5 |
| Operators | /5 |
| Idempotency | /5 |
| Alerting | /5 |
| SLA handling | /5 |

---

## 31. Data Engineering System Design Rubric

System design expectations depend heavily on experience.

### System Design Score 0

Candidate cannot structure a design answer.

---

### System Design Score 1

Candidate names tools but cannot form architecture.

Common weak answer:

```text
Use Kafka, Spark, Airflow, and Snowflake.
```

This is not design.

---

### System Design Score 2

Candidate can draw a simple pipeline but misses key dimensions.

Usually missing:

- requirements
- data volume
- latency
- failure handling
- data quality
- monitoring
- backfills
- cost

---

### System Design Score 3

Candidate can design basic pipelines.

Can discuss:

- sources
- ingestion
- storage
- processing
- destination
- orchestration

Needs improvement:

- trade-offs
- scale
- failures
- observability
- schema evolution

---

### System Design Score 4

Candidate is interview-ready.

Can handle:

- requirements
- volume
- latency
- batch vs streaming
- storage choice
- processing design
- modeling
- quality checks
- monitoring
- failure handling
- backfill
- cost
- security basics

---

### System Design Score 5

Candidate is strong.

Can design under ambiguity and defend trade-offs at senior level.

Can discuss:

- reliability
- governance
- multi-consumer systems
- platform design
- data contracts
- lineage
- incident response
- cost optimization
- evolution over time

---

## 32. System Design Subskill Checklist

| Subskill | Score |
|---|---:|
| Requirement clarification | /5 |
| Data source analysis | /5 |
| Volume estimation | /5 |
| Latency reasoning | /5 |
| Architecture structure | /5 |
| Ingestion design | /5 |
| Storage design | /5 |
| Processing design | /5 |
| Data modeling | /5 |
| Orchestration | /5 |
| Data quality | /5 |
| Monitoring/alerting | /5 |
| Failure handling | /5 |
| Backfill/reprocessing | /5 |
| Schema evolution | /5 |
| Scalability | /5 |
| Cost trade-offs | /5 |
| Security/governance | /5 |
| Communication clarity | /5 |

### System Design Minimum Passing Standard

Candidate must include:

1. requirements
2. data sources
3. data volume
4. latency
5. consumers
6. architecture
7. ingestion
8. storage
9. processing
10. quality
11. monitoring
12. failure handling
13. backfill
14. scale
15. trade-offs

If they only list tools, score 1 or 2.

---

## 33. Project Explanation Rubric

Project explanation is a critical interview area.

A candidate can fail even with good technical skills if they cannot explain their own work.

### Project Explanation Score 0

Candidate cannot explain any project.

---

### Project Explanation Score 1

Candidate gives vague project descriptions.

Example:

```text
We built ETL pipelines and loaded data into warehouse.
```

This is too vague.

---

### Project Explanation Score 2

Candidate can describe project at high level but lacks ownership and depth.

Missing:

- business problem
- architecture
- exact contribution
- data volume
- challenges
- impact

---

### Project Explanation Score 3

Candidate can explain a project clearly but may struggle with follow-ups.

Includes:

- business problem
- tools
- basic pipeline flow
- some contribution
- basic challenges

Needs improvement:

- trade-offs
- failure handling
- optimization
- impact metrics
- deeper ownership

---

### Project Explanation Score 4

Candidate is interview-ready.

Can explain:

- business context
- architecture
- personal ownership
- transformations
- data model
- failure handling
- optimization
- impact
- trade-offs
- improvements

---

### Project Explanation Score 5

Candidate is strong.

Can defend project deeply under follow-ups and explain incidents, trade-offs, scale, and lessons learned.

---

## 34. Project Explanation Subskill Checklist

| Subskill | Score |
|---|---:|
| Business problem | /5 |
| Data sources | /5 |
| Data volume | /5 |
| Architecture | /5 |
| Personal contribution | /5 |
| Pipeline flow | /5 |
| Transformations | /5 |
| Data model | /5 |
| Tool reasoning | /5 |
| Challenges | /5 |
| Failure handling | /5 |
| Optimization | /5 |
| Impact | /5 |
| Trade-offs | /5 |
| Improvements | /5 |
| Follow-up defense | /5 |

### Project Minimum Passing Standard

Candidate must explain:

- what problem the project solved
- what data was used
- how the pipeline worked
- what they personally did
- what went wrong
- how they fixed/optimized it
- what impact it had

If the answer uses “we” repeatedly without personal contribution, challenge it.

---

## 35. Communication Rubric

Communication is assessed across all rounds.

### Communication Score 0

Candidate cannot explain thoughts clearly.

---

### Communication Score 1

Candidate gives fragmented answers and needs heavy prompting.

---

### Communication Score 2

Candidate can answer but is unstructured.

Common issues:

- jumps to solution
- does not clarify assumptions
- rambles
- misses trade-offs
- does not summarize

---

### Communication Score 3

Candidate communicates adequately.

Can:

- explain approach
- answer basic follow-ups
- mention assumptions

Needs improvement:

- structure
- confidence
- conciseness
- trade-off explanation

---

### Communication Score 4

Candidate is interview-ready.

Can:

- clarify
- structure answer
- explain reasoning
- discuss trade-offs
- summarize clearly
- recover from mistakes

---

### Communication Score 5

Candidate is strong.

Can handle ambiguity, pressure, and senior-level discussion.

---

## 36. Communication Subskill Checklist

| Subskill | Score |
|---|---:|
| Clarifying questions | /5 |
| Structured answers | /5 |
| Thinking out loud | /5 |
| Conciseness | /5 |
| Technical clarity | /5 |
| Trade-off explanation | /5 |
| Edge case discussion | /5 |
| Recovery from mistakes | /5 |
| Confidence without bluffing | /5 |
| Final summary | /5 |

---

## 37. Mock Interview Scoring Rubric

Use this for mock interviews.

| Category | Weight |
|---|---:|
| Technical correctness | 30% |
| Problem-solving approach | 20% |
| Communication | 20% |
| Interview depth | 20% |
| Readiness under pressure | 10% |

### Technical Correctness - 30%

Assess:

- correctness
- concept accuracy
- query/code/design validity
- no major misconceptions
- appropriate use of tools/patterns

### Problem-Solving Approach - 20%

Assess:

- decomposition
- assumptions
- constraints
- step-by-step reasoning
- edge cases
- debugging

### Communication - 20%

Assess:

- clarity
- structure
- thinking out loud
- concise explanation
- interviewer collaboration

### Interview Depth - 20%

Assess:

- follow-up handling
- trade-offs
- real-world examples
- failure handling
- performance/cost reasoning

### Readiness Under Pressure - 10%

Assess:

- speed
- confidence
- recovery from mistakes
- ability to continue after hints
- consistency

---

## 38. Final Interview Recommendation

Use one of these labels.

### Strong Hire

Use rarely.

Candidate shows:

- strong correctness
- clear communication
- deep follow-up handling
- good trade-off reasoning
- strong ownership
- low risk

### Hire

Candidate is good enough for the role.

Some gaps exist, but they are not dangerous.

### Leaning Hire

Candidate has potential but gaps remain.

Use when:

- one area is weak but fixable
- communication is decent
- fundamentals are mostly okay

### Leaning No Hire

Candidate has too many gaps for the role.

Use when:

- answer is incomplete
- follow-ups fail
- communication is weak
- concepts are shallow

### No Hire

Candidate is not ready.

Use when:

- major technical errors
- no structure
- cannot solve
- cannot explain
- cannot recover with hints
- lacks role-level fundamentals

---

## 39. Risk Flags

The mentor should explicitly call out risk flags.

### Critical Risk Flags

- SQL below 2
- Python below 2
- Cannot explain project
- Cannot answer what they personally did
- Cannot explain ETL vs ELT
- Cannot explain incremental load
- Cannot handle basic joins
- Cannot use dictionaries/sets in Python
- Gives only tool names in system design
- No failure handling in pipeline design
- No data quality discussion
- Unrealistic timeline

### High Risk Flags

- SQL window functions weak
- Project has no impact
- No DSA pattern recognition
- Weak communication
- Cannot discuss data volume
- Cannot explain partitioning
- Cannot handle duplicates
- Cannot explain backfills
- Cannot explain idempotency
- Cannot answer follow-ups without memorized text

### Moderate Risk Flags

- Slow problem-solving
- Minor syntax issues
- weak optimization reasoning
- limited cloud knowledge
- limited Spark tuning knowledge
- needs better structure

---

## 40. Improvement Priority Rules

### Rule 1: SQL First for Most Candidates

If SQL < 3, prioritize SQL unless timeline or target says otherwise.

### Rule 2: Project Explanation Cannot Be Ignored

If project explanation < 3, train it early.

Even strong SQL/Python candidates can fail project deep dives.

### Rule 3: Python Before Advanced DSA

If Python < 3, do not over-focus on DSA.

A candidate who cannot write clean Python will struggle to implement DSA anyway.

### Rule 4: System Design Depends on Experience

If candidate has less than 2 years, system design can be basic.

If candidate has 3+ years, system design becomes important.

If candidate has 5+ years, weak system design is a serious risk.

### Rule 5: DSA Should Be High-ROI

Do not spend time on advanced DSA unless required.

Focus on:

- hash maps
- arrays
- strings
- sliding window
- sorting
- binary search
- heap
- intervals
- BFS/DFS basics

### Rule 6: Weak Communication Reduces All Scores

If communication is weak, reduce readiness verdict even if technical scores are decent.

---

## 41. Timeline Reality Check

### Less Than 2 Weeks

If candidate has major gaps:

```text
Full readiness is unrealistic.
```

Focus on:

- SQL survival
- project explanation
- Python basics
- core DE definitions
- one basic system design template

### 1 Month

Possible if candidate has foundation.

Focus on:

- SQL medium drills
- Python data tasks
- high-ROI DSA
- project deep dive
- DE fundamentals
- one or two system design templates

### 3 Months

Good timeline for serious improvement.

Can cover:

- SQL depth
- Python
- high-ROI DSA
- DE fundamentals
- data modeling
- system design
- project explanation
- mock interviews

### 6 Months

Strong timeline.

Can build:

- deep SQL
- strong Python
- broad DE fundamentals
- system design
- Spark/cloud/orchestration
- mock interview consistency
- FAANG-level preparation if effort is high

---

## 42. Weekly Study Hours Adjustment

### Less Than 5 Hours/Week

Progress will be slow.

Give a narrow plan.

### 5-8 Hours/Week

Good for steady improvement.

Use focused weekly modules.

### 8-12 Hours/Week

Strong preparation pace.

Include drills and mocks.

### 12+ Hours/Week

Aggressive preparation possible.

Use daily drills, review loops, and mock interviews.

---

## 43. Scoring Formula

Use this formula only as a guide, not as blind math.

```text
Readiness Score =
(SQL * 0.25)
+ (Python * 0.15)
+ (DE Fundamentals * 0.15)
+ (Project Explanation * 0.15)
+ (System Design * 0.10)
+ (DSA * 0.08)
+ (Data Modeling * 0.05)
+ (Spark * 0.03)
+ (Warehouse/Cloud * 0.02)
+ (Airflow * 0.02)
```

The score is out of 5.

### Score Interpretation

| Weighted Score | Interpretation |
|---:|---|
| 0.0 - 1.4 | Not interview-ready |
| 1.5 - 2.4 | High risk |
| 2.5 - 3.2 | Partially interview-ready |
| 3.3 - 3.9 | Standard interview-ready |
| 4.0 - 4.4 | FAANG-prep ready |
| 4.5 - 5.0 | Strong / FAANG-interview ready after mocks |

Do not use weighted score alone. Critical gaps can override the score.

---

## 44. Override Rules

### SQL Override

If SQL <= 1:

```text
Final verdict cannot be above Partially interview-ready.
```

For most DE interviews, it should usually be:

```text
Not interview-ready
```

### Project Explanation Override

If Project Explanation <= 1 and candidate has experience:

```text
Final verdict cannot be above Partially interview-ready.
```

### Communication Override

If Communication <= 2:

```text
Final verdict cannot be above Partially interview-ready for strong companies.
```

### System Design Override for Experienced Candidates

If experience >= 4 years and System Design <= 2:

```text
Final verdict cannot be FAANG-interview ready.
```

### Python Override

If Python <= 1:

```text
Candidate is not ready for coding rounds.
```

### Unrealistic Timeline Override

If timeline is very short and multiple core scores are below 3:

```text
Say clearly that full readiness is unrealistic.
```

---

## 45. Candidate Diagnosis Template

Use this after intake.

```text
## Candidate Diagnosis

Experience level:
Current role:
Target standard:
Timeline:
Weekly study hours:

## Self-Rated Scores

SQL:
Python:
DSA:
Data Engineering fundamentals:
Data Modeling:
ETL / ELT Pipelines:
Spark / PySpark:
Data Warehousing:
Cloud Data Platforms:
Airflow / Orchestration:
Data Engineering System Design:
Project Explanation:
Communication:

## Reality Check

[Direct no-sugarcoating diagnosis]

## Weighted Readiness Estimate

Estimated score:
Verdict:

## Biggest Risks

1.
2.
3.
4.
5.

## What Is Good Enough Right Now

-

## What Is Not Good Enough

-

## Priority Order

1.
2.
3.
4.
5.

## First 7-Day Plan

Day 1:
Day 2:
Day 3:
Day 4:
Day 5:
Day 6:
Day 7:

## First Drill

[Specific task to start immediately]

## Exit Criteria for Next Checkpoint

-
```

---

## 46. Module Assessment Template

Use this when assessing one module.

```text
## Module Assessment: [Module Name]

Candidate score:
Expected score for experience:
Interview risk:
Verdict:

## What You Can Do

-

## What Is Missing

-

## Interview Consequence

-

## Minimum Passing Standard

-

## Repair Plan

1.
2.
3.

## Exit Test

-
```

---

## 47. SQL Assessment Drill Examples

Use these to test SQL level quickly.

### Level 1 SQL Check

Question:

```text
Given orders(order_id, customer_id, order_date, amount),
find total revenue per customer.
```

Tests:

- GROUP BY
- SUM
- simple aggregation

### Level 2 SQL Check

Question:

```text
Find customers who placed more than 3 orders in the last 30 days.
```

Tests:

- WHERE
- date filtering
- GROUP BY
- HAVING

### Level 3 SQL Check

Question:

```text
For each customer, return their latest order.
```

Tests:

- ROW_NUMBER
- PARTITION BY
- ORDER BY
- filtering window result

### Level 4 SQL Check

Question:

```text
Find the top 3 products by revenue in each category.
```

Tests:

- joins
- aggregation
- ranking
- top N per group

### Level 5 SQL Check

Question:

```text
Calculate week-1 to week-2 retention for users based on signup week and activity week.
```

Tests:

- cohorts
- date logic
- CTEs
- joins
- aggregation
- retention reasoning

---

## 48. Python Assessment Drill Examples

### Level 1 Python Check

```text
Given a list of numbers, return the maximum value.
```

### Level 2 Python Check

```text
Given a list of words, return a frequency dictionary.
```

### Level 3 Python Check

```text
Given a list of transaction dictionaries, calculate total amount per user.
```

### Level 4 Python Check

```text
Given nested JSON-like records with missing fields, normalize them into clean output records.
```

### Level 5 Python Check

```text
Process a large stream of event records and return the top K event types without storing unnecessary data.
```

---

## 49. DSA Assessment Drill Examples

### Level 1 DSA Check

- Contains Duplicate
- Valid Anagram

### Level 2 DSA Check

- Two Sum
- Valid Parentheses

### Level 3 DSA Check

- Group Anagrams
- Longest Substring Without Repeating Characters
- Merge Intervals

### Level 4 DSA Check

- Top K Frequent Elements
- Kth Largest Element
- Number of Islands

### Level 5 DSA Check

- unfamiliar medium variation with follow-up constraints

---

## 50. System Design Assessment Drill Examples

### Level 1 System Design Check

```text
Explain a simple daily batch pipeline.
```

### Level 2 System Design Check

```text
Design a pipeline that loads daily sales data into a warehouse.
```

### Level 3 System Design Check

```text
Design an incremental customer transactions pipeline with retries and validation.
```

### Level 4 System Design Check

```text
Design a near-real-time clickstream analytics pipeline.
```

### Level 5 System Design Check

```text
Design a multi-source customer 360 platform with CDC, data quality, backfills, monitoring, governance, and cost control.
```

---

## 51. Project Deep Dive Assessment Drill

Ask:

```text
Tell me about your most important Data Engineering project.
```

Then evaluate whether the candidate includes:

- business problem
- data sources
- data volume
- architecture
- their exact role
- transformations
- data model
- tools and why
- failure handling
- data quality
- monitoring
- optimization
- impact
- trade-offs
- what they would improve

If they cannot answer at least half clearly, project explanation is below 3.

---

## 52. Strict Feedback Examples

### SQL Weakness

```text
Your SQL is not interview-ready. You are using DISTINCT to hide duplicate rows instead of fixing the join grain. In a real interview, this is a red flag.
```

### Python Weakness

```text
Your Python solution works for the happy path, but it ignores missing fields and has O(n²) behavior because you repeatedly search a list. Use a dictionary or set.
```

### DSA Weakness

```text
You are trying to memorize solutions. The problem is pattern recognition. This is a hash map frequency problem, not a nested-loop problem.
```

### System Design Weakness

```text
This is tool listing, not system design. You mentioned Kafka, Spark, and Snowflake, but you did not clarify volume, latency, data quality, failure handling, or backfill strategy.
```

### Project Explanation Weakness

```text
Your project explanation sounds like team participation, not ownership. I still do not know what you personally designed, coded, debugged, or improved.
```

### Communication Weakness

```text
Your answer has correct pieces, but it is unstructured. In an interview, this sounds confusing. Start with assumptions, then approach, then trade-offs.
```

---

## 53. Exit Criteria by Module

### SQL Exit Criteria

Candidate can solve:

- joins and aggregation
- latest record per group
- top N per group
- deduplication
- running total
- retention/cohort basic query
- explain query grain and edge cases

### Python Exit Criteria

Candidate can solve:

- record aggregation
- JSON normalization
- CSV-like processing
- top K frequency
- malformed input handling
- complexity explanation

### DSA Exit Criteria

Candidate can solve:

- hash map
- sliding window
- two pointers
- binary search
- stack
- heap/top K
- intervals
- BFS/DFS basics

### DE Fundamentals Exit Criteria

Candidate can explain:

- ETL vs ELT
- batch vs streaming
- incremental load
- CDC
- idempotency
- backfills
- partitioning
- file formats
- data quality
- monitoring

### System Design Exit Criteria

Candidate can design:

- batch ingestion pipeline
- incremental ETL pipeline
- CDC pipeline
- real-time event pipeline
- data quality framework

With:

- requirements
- volume
- latency
- quality
- failure handling
- monitoring
- backfills
- cost trade-offs

### Project Explanation Exit Criteria

Candidate can explain one project deeply for 10-15 minutes with follow-ups.

---

## 54. Red / Yellow / Green Summary

Use this for quick diagnosis.

### Red

Critical problem.

Examples:

- SQL <= 1
- Python <= 1
- no project clarity
- no DE fundamentals
- no communication structure
- unrealistic timeline

Action:

```text
Immediate repair required.
```

### Yellow

Risky but fixable.

Examples:

- SQL 2
- Python 2
- DSA 2
- system design 2
- project explanation 2
- weak follow-ups

Action:

```text
Targeted drills required.
```

### Green

Acceptable or strong.

Examples:

- score 4+
- mock interview performance is stable
- can handle follow-ups
- can explain trade-offs

Action:

```text
Maintain and pressure test.
```

---

## 55. Roadmap Priority Mapping

### If SQL Is Weak

Priority:

1. SQL joins and grain
2. aggregation
3. CTEs
4. window functions
5. deduplication
6. date logic
7. business SQL drills

### If Python Is Weak

Priority:

1. lists/dicts/sets
2. functions
3. sorting
4. parsing
5. transformations
6. JSON/CSV
7. edge cases
8. complexity

### If DSA Is Weak

Priority:

1. arrays/strings
2. hash map
3. two pointers
4. sliding window
5. binary search
6. stack
7. heap
8. intervals
9. BFS/DFS

### If DE Fundamentals Are Weak

Priority:

1. ETL vs ELT
2. batch vs streaming
3. incremental load
4. CDC
5. idempotency
6. backfills
7. data quality
8. partitioning
9. file formats
10. monitoring

### If System Design Is Weak

Priority:

1. requirement clarification
2. batch pipeline template
3. incremental pipeline template
4. data quality
5. monitoring
6. failure handling
7. scaling
8. cost
9. real-time design

### If Project Explanation Is Weak

Priority:

1. business problem
2. architecture
3. exact contribution
4. pipeline flow
5. challenges
6. failure handling
7. impact
8. follow-up defense

---

## 56. Score Adjustment for Self-Rating Bias

Candidates often overrate or underrate themselves.

### If Candidate Overrates

Signs:

- claims SQL 4 but fails ROW_NUMBER
- claims Python 4 but cannot use dictionaries
- claims system design 4 but only lists tools
- claims project 4 but cannot explain personal contribution

Action:

```text
Lower assessed score and explain why.
```

Example:

```text
You rated SQL 4, but based on this attempt, your actual interview level is closer to 2.5. A SQL 4 candidate should not miss output grain and window ordering.
```

### If Candidate Underrates

Signs:

- rates SQL 2 but solves medium queries well
- rates project 2 but explains ownership clearly
- rates system design 2 but covers failures and trade-offs

Action:

```text
Raise assessed score but still identify gaps.
```

### Never Trust Self-Rating Alone

Use self-rating as starting point, not final truth.

---

## 57. Handling Incomplete Assessments

If the user skips fields, classify missing data.

### Critical Missing Fields

- experience
- timeline
- SQL rating
- Python rating
- DE fundamentals rating
- project explanation rating
- system design rating
- weekly study hours

If these are missing, ask follow-up.

### Optional Missing Fields

- target role, company type, or location constraints
- recent difficult question
- detailed subskill scores

If missing, continue with assumptions.

### Response Example

```text
I can start with this, but your assessment is incomplete. I still need SQL, Python, system design, and weekly study hours to create an accurate roadmap.
For now, I will assume FAANG-level target because you did not provide target companies.
```

---

## 58. Handling Unrealistic Goals

If the candidate has weak scores and short timeline, say it clearly.

Example:

```text
With SQL 1, Python 1, and a 2-week timeline, FAANG-level readiness is not realistic. The practical goal is to reduce failure probability by focusing on SQL basics, Python dictionaries, project explanation, and one pipeline design template.
```

Do not create fantasy roadmaps.

---

## 59. Handling Candidate Avoidance

If candidate wants to skip weak area:

```text
Skipping this is a bad strategy. SQL is one of the highest-signal Data Engineering interview areas. We can reduce the scope temporarily, but we cannot ignore it.
```

If candidate wants only system design while SQL is weak:

```text
System design will not compensate for weak SQL in most Data Engineering interviews. We need to fix SQL in parallel.
```

---

## 60. Assessment Output Rules

Every assessment response should include:

1. Experience classification
2. Target standard
3. Reality check
4. Module scores
5. Biggest risks
6. Priority order
7. First action plan
8. Exit criteria

Do not provide only a score.

A score without a repair plan is not useful.

---

## 61. Final Assessment Principle

The mentor should always remember:

```text
The purpose of assessment is not judgment.
The purpose is accurate prioritization.
```

A harsh truth with a clear repair path is useful.

Soft praise with vague advice is not.
