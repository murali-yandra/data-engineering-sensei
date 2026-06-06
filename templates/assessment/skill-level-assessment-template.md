# Skill Level Assessment Template

Generated: 2026-06-06

Path:

```text
data-engineering-sensei/templates/assessment/skill-level-assessment-template.md
```

Purpose:

```text
This template is used by the Data Engineering Sensei AI mentor to assess the candidate's real skill level across Data Engineering interview areas.
```

It assesses:

```text
SQL
Python
DSA
Data Engineering fundamentals
Data modeling
ETL/ELT pipelines
Data warehouse
Data lake/lakehouse
Data quality
Orchestration
Spark/PySpark
Cloud data platforms
System design
Project deep dive
Resume/public portfolio
Communication
```

Important:

```text
This is a performance assessment, not a confidence survey.
Scores must come from answers, code, project proof, or mock performance.
```


## 1. Master Assessment Prompt

Use this prompt to start assessment.

```text
You are my Data Engineering Sensei interviewer and mentor.

Run a strict skill-level assessment for Data Engineering interview readiness.

Rules:
1. Ask one question at a time.
2. Do not give the answer before I respond.
3. Score every answer from 0 to 5.
4. Explain why I got the score.
5. Identify missing points.
6. Give the corrected answer after scoring.
7. Record weaknesses.
8. Assign repair drills.
9. Do not sugarcoat.
10. Do not mark me interview-ready without evidence.

Assess these areas:
- SQL
- Python data scripting
- DSA patterns
- Data Engineering fundamentals
- Data modeling and warehouse
- ETL/ELT pipeline design
- Data quality
- Orchestration
- Spark/PySpark
- Cloud data platforms
- System design
- Project deep dive
- Resume/public portfolio readiness
- Communication

Use my context:
I am targeting Data Engineering roles.
I am early-career or transitioning into Data Engineering.
My main project is Primary Portfolio Data Project.
I need job-focused preparation and practical feedback.

At the end:
1. give score table
2. list top strengths
3. list top weaknesses
4. create a 7-day repair plan
5. create a 30-day roadmap
6. tell me which progress files to update
```


## 2. Scoring Rubric

Use this score scale for every area.

```text
0 = not assessed / no answer
1 = beginner; knows words but cannot apply
2 = basic; can answer simple cases but weak under follow-up
3 = usable with support; partial interview readiness
4 = interview-ready for target level
5 = strong; can teach and handle deep follow-ups
```

Pass marks:

```text
SQL:
4/5

Python:
4/5

DSA:
3.5/5 for most DE roles

DE fundamentals:
4/5

System design:
4/5

Project deep dive:
4/5

Resume/public portfolio:
4/5

Communication:
3.5/5
```

Automatic score caps:

```text
If answer is tool-only:
max score 2.5

If no trade-offs in system design:
max score 3

If project is explained only as tech stack:
max score 2.5

If SQL ignores grain:
max score 3

If Python code has no edge cases:
max score 3.5

If resume claim has no evidence:
max score 2.5

If candidate cannot handle follow-up:
max score 3.5
```


## 3. Assessment Output Format

After each question, use this format:

```text
Score:
<0-5>

Verdict:
pass / partial / fail

What was good:
...

What was missing:
...

Why it matters:
...

Correct answer:
...

Weakness added:
<Weakness ID or none>

Repair drill:
...

Next question:
...
```

At the end, use:

```text
# Final Skill Assessment

## Overall Readiness
...

## Score Table
...

## Strongest Areas
...

## Weakest Areas
...

## Critical Weaknesses
...

## Recommended Roadmap
...

## Next 7 Days
...

## Files To Update
...
```


## 4. SQL Assessment

### Question 1: Explain the difference between INNER JOIN, LEFT JOIN, and FULL OUTER JOIN with a data example.

Skill tag:

```text
joins
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: Given orders and customers, write a query to find customers with no orders.

Skill tag:

```text
left join anti join
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: Find the latest transaction per account using SQL.

Skill tag:

```text
window function
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: Find duplicate transactions and keep only the latest record.

Skill tag:

```text
deduplication
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: Find top 3 products by revenue per category.

Skill tag:

```text
ranking
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: Explain what table grain means and why it matters.

Skill tag:

```text
grain
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: Explain when ROW_NUMBER, RANK, and DENSE_RANK differ.

Skill tag:

```text
window ranking
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: Explain how you would optimize a slow SQL query.

Skill tag:

```text
optimization
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: Design SQL checks for source-to-target reconciliation.

Skill tag:

```text
data quality SQL
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: Explain why using DISTINCT blindly can be dangerous.

Skill tag:

```text
SQL correctness
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 5. Python Assessment

### Question 1: Write a function that reads a list of transactions and groups total amount by category.

Skill tag:

```text
dict aggregation
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: How would you parse a CSV file and handle bad rows?

Skill tag:

```text
file processing
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: How would you process paginated API data safely?

Skill tag:

```text
API processing
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: Write pseudocode for reading JSON transactions and writing cleaned output.

Skill tag:

```text
JSON ETL
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: Explain how you would add logging to a data script.

Skill tag:

```text
logging
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: Explain exception handling strategy for a data pipeline script.

Skill tag:

```text
errors
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: When would you use list, dict, set, or tuple?

Skill tag:

```text
data structures
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: How would you deduplicate records in Python?

Skill tag:

```text
dedupe
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: How would you test a parser function?

Skill tag:

```text
testing
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: Explain pandas groupby, merge, and filter with examples.

Skill tag:

```text
pandas
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 6. DSA Pattern Assessment

### Question 1: Given an array, find two numbers that sum to target.

Skill tag:

```text
hashmap/two sum
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: Find first non-repeating character in a string.

Skill tag:

```text
hashmap frequency
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: Find longest substring without repeating characters.

Skill tag:

```text
sliding window
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: Merge overlapping intervals.

Skill tag:

```text
intervals
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: Find top K frequent elements.

Skill tag:

```text
heap/hashmap
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: Validate parentheses.

Skill tag:

```text
stack
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: Binary search in sorted array.

Skill tag:

```text
binary search
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: Explain when to use BFS vs DFS.

Skill tag:

```text
graph traversal
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: Given sorted array, find pair closest to target.

Skill tag:

```text
two pointers
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: Explain time and space complexity of hashmap-based solutions.

Skill tag:

```text
complexity
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 7. Data Engineering Fundamentals Assessment

### Question 1: Explain ETL vs ELT with examples.

Skill tag:

```text
ETL/ELT
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: Explain batch vs streaming pipelines.

Skill tag:

```text
batch/streaming
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: Explain data warehouse vs data lake vs lakehouse.

Skill tag:

```text
storage architecture
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: What is idempotency in data pipelines?

Skill tag:

```text
reliability
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: What is a backfill and how do you run it safely?

Skill tag:

```text
backfills
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: What is data partitioning and why does it matter?

Skill tag:

```text
performance
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: Explain schema evolution and how to handle breaking changes.

Skill tag:

```text
schema evolution
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: What are data quality checks you would add to a pipeline?

Skill tag:

```text
DQ
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: Explain orchestration and DAGs.

Skill tag:

```text
Airflow/DAGs
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: Explain monitoring and alerting for data pipelines.

Skill tag:

```text
observability
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 8. Data Modeling And Warehouse Assessment

### Question 1: Explain fact and dimension tables.

Skill tag:

```text
modeling
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: What is table grain?

Skill tag:

```text
grain
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: Design a star schema for orders and payments.

Skill tag:

```text
warehouse design
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: Explain SCD Type 1 vs Type 2.

Skill tag:

```text
SCD
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: How do you handle late-arriving facts?

Skill tag:

```text
late data
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: How do you avoid fact-to-fact join explosion?

Skill tag:

```text
grain
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: What is a reporting mart?

Skill tag:

```text
reporting
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: What is a semantic layer?

Skill tag:

```text
metrics governance
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: How would you reconcile a sales mart to source facts?

Skill tag:

```text
reconciliation
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: How would you optimize a slow dashboard?

Skill tag:

```text
performance
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 9. Pipeline System Design Assessment

### Question 1: Design a batch pipeline that loads daily orders into a warehouse.

Skill tag:

```text
batch pipeline
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: Design a CDC pipeline from PostgreSQL to a warehouse.

Skill tag:

```text
CDC
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: Design a data quality framework.

Skill tag:

```text
DQ framework
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: Design a data warehouse for e-commerce.

Skill tag:

```text
warehouse
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: Design a reporting pipeline for daily sales dashboard.

Skill tag:

```text
reporting
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: Design a data lake with bronze/silver/gold layers.

Skill tag:

```text
data lake
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: Design event ingestion for clickstream events.

Skill tag:

```text
event ingestion
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: Design a realtime fraud detection pipeline.

Skill tag:

```text
realtime
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: Explain how you handle failures and retries in a pipeline.

Skill tag:

```text
reliability
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: Explain how you monitor pipeline freshness and quality.

Skill tag:

```text
observability
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 10. Spark/PySpark Assessment

### Question 1: Explain Spark transformations vs actions.

Skill tag:

```text
Spark basics
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: What is lazy evaluation?

Skill tag:

```text
Spark execution
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: Explain narrow vs wide transformations.

Skill tag:

```text
shuffle
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: How do joins work in Spark and what causes skew?

Skill tag:

```text
joins/skew
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: What is partitioning in Spark?

Skill tag:

```text
partitioning
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: How would you optimize a slow PySpark job?

Skill tag:

```text
optimization
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: Explain cache/persist and when to use it.

Skill tag:

```text
performance
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: What file formats are good for Spark analytics?

Skill tag:

```text
Parquet/ORC
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: How do you handle small files?

Skill tag:

```text
file layout
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: Explain broadcast join.

Skill tag:

```text
join optimization
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 11. Cloud Data Platforms Assessment

### Question 1: What is BigQuery/Snowflake/Redshift used for?

Skill tag:

```text
warehouse
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: Explain object storage in data pipelines.

Skill tag:

```text
cloud storage
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: How would you design cloud data lake storage layout?

Skill tag:

```text
lake storage
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: How do you control cost in cloud warehouses?

Skill tag:

```text
cost
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: How do you secure data in cloud platforms?

Skill tag:

```text
security
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: What are service accounts/IAM at a high level?

Skill tag:

```text
access
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: How would you schedule data pipelines in cloud?

Skill tag:

```text
orchestration
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: How would you monitor cloud data jobs?

Skill tag:

```text
monitoring
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: What is partitioning/clustering in cloud warehouses?

Skill tag:

```text
performance
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: How do you choose between managed warehouse and Spark?

Skill tag:

```text
trade-offs
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 12. Project Deep Dive Assessment

### Question 1: Explain your Primary Portfolio Data Project in 2 minutes.

Skill tag:

```text
pitch
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: What problem does it solve?

Skill tag:

```text
problem
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: Explain the architecture.

Skill tag:

```text
architecture
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: Explain the database schema.

Skill tag:

```text
data model
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: Explain the transaction ingestion flow.

Skill tag:

```text
pipeline
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: How do you normalize merchants?

Skill tag:

```text
data cleaning
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: How does categorization work?

Skill tag:

```text
classification
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: How does user feedback improve the system?

Skill tag:

```text
feedback loop
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: How do you handle duplicate transactions?

Skill tag:

```text
data quality
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: How do you secure user financial data?

Skill tag:

```text
security
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 11: What tests did you write or plan?

Skill tag:

```text
testing
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 12: How would you scale this to more users?

Skill tag:

```text
scaling
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 13: What trade-offs did you make?

Skill tag:

```text
trade-offs
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 14: What would you improve next?

Skill tag:

```text
roadmap
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 15: What resume bullet can this project support?

Skill tag:

```text
resume evidence
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 13. Resume/public portfolio/Communication Assessment

### Question 1: Walk me through your resume in 90 seconds.

Skill tag:

```text
resume pitch
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 2: Explain your strongest project bullet and defend it.

Skill tag:

```text
resume evidence
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 3: What makes your public portfolio useful for recruiters?

Skill tag:

```text
public portfolio
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 4: What is your target role and why?

Skill tag:

```text
role clarity
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 5: Tell me about a technical challenge you solved.

Skill tag:

```text
behavioral technical
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 6: Tell me about a mistake and what you learned.

Skill tag:

```text
behavioral
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 7: Explain a complex technical topic simply.

Skill tag:

```text
communication
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 8: Answer a system design question with clear structure.

Skill tag:

```text
structure
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 9: Explain why you are ready for a Data Engineer role.

Skill tag:

```text
readiness
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```

### Question 10: What is your biggest current weakness and repair plan?

Skill tag:

```text
self-awareness
```

Expected evaluation:

```text
- correctness
- structure
- examples
- edge cases
- interview clarity
- ability to handle follow-up
```

Scoring note:

```text
Score strictly from 0 to 5.
Add weakness if score is below target.
```


## 14. Follow-Up Question Bank

Use follow-ups to test depth.

```text
Why did you choose that approach?
What happens if data arrives late?
How do you prevent duplicates?
How do you recover from failure?
How do you validate correctness?
How do you monitor this?
What are the trade-offs?
How would this scale?
What would you do differently with 10x data?
What security or PII risks exist?
What would you put on the dashboard?
How would you backfill historical data?
How would you make it idempotent?
How would you test this?
How would you explain this to a non-technical stakeholder?
```

Rule:

```text
A candidate who gives a good first answer but fails follow-ups should not receive a 4+ score.
```


## 15. Final Score Table Template

```text
| Area | Score | Pass Target | Status | Evidence | Main Weakness |
|---|---:|---:|---|---|---|
| SQL | 0 | 4 | not_assessed | none | unknown |
| Python | 0 | 4 | not_assessed | none | unknown |
| DSA | 0 | 3.5 | not_assessed | none | unknown |
| DE Fundamentals | 0 | 4 | not_assessed | none | unknown |
| Data Modeling | 0 | 4 | not_assessed | none | unknown |
| System Design | 0 | 4 | not_assessed | none | unknown |
| Spark/PySpark | 0 | 3.5 | not_assessed | none | unknown |
| Cloud | 0 | 3.5 | not_assessed | none | unknown |
| Project Deep Dive | 0 | 4 | not_assessed | none | unknown |
| Resume/public portfolio | 0 | 4 | not_assessed | none | unknown |
| Communication | 0 | 3.5 | not_assessed | none | unknown |
```

Status values:

```text
not_assessed
fail
partial
pass
strong
```


## 16. Readiness Verdict Template

Use this final verdict.

```text
Overall readiness:
not_ready / partially_ready / interview_ready

Reason:
...

Strongest evidence:
...

Biggest blockers:
...

Top 5 weaknesses:
1.
2.
3.
4.
5.

Fastest path to improvement:
...

Should candidate apply now?
yes/no/selectively

If no:
what score gates must be reached?

If selectively:
which roles are realistic?

If yes:
what application strategy?
```

No-sugarcoating rule:

```text
If scores are missing or below target, say not_ready.
```


## 17. 7-Day Repair Plan Template

Generate after assessment.

```text
Day 1:
Repair highest-priority SQL weakness.

Day 2:
Repair Python scripting weakness.

Day 3:
Repair DE fundamentals weakness.

Day 4:
Practice batch pipeline system design.

Day 5:
Project deep dive: portfolio project architecture.

Day 6:
Mock interview retest.

Day 7:
Update resume/public portfolio evidence and roadmap.
```

Customize based on actual scores.

Rule:

```text
The 7-day plan must target weaknesses, not random topics.
```


## 18. 30-Day Roadmap Template

Generate after assessment.

```text
Week 1:
Baseline repair and SQL/Python foundation.

Week 2:
Data engineering fundamentals, data modeling, warehouse, data quality.

Week 3:
System design mocks and project deep dive.

Week 4:
Mock interview loop, resume/public portfolio polish, job-search preparation.
```

For each week include:

```text
focus
tasks
evidence output
target score
progress files to update
```


## 19. Progress File Update Prompt

Use this after assessment.

```text
Update my Data Engineering Sensei progress files from this assessment.

Update:
1. progress/CANDIDATE_PROFILE.md with stable skill scores and risk profile.
2. progress/CURRENT_STATE.md with latest assessment summary and active next step.
3. progress/ROADMAP_PROGRESS.md with phase/module status.
4. progress/NEXT_STEPS.md with repair tasks.
5. progress/WEAKNESS_REGISTER.md with weaknesses and severity.
6. progress/SESSION_LOG.md with assessment session entry.
7. progress/MOCK_INTERVIEW_HISTORY.md if this was a mock.
8. progress/PROJECT_PROGRESS.md if project was assessed.
9. progress/RESUME_STATE.md if resume was assessed.

Do not duplicate full feedback everywhere.
Put detailed feedback in the right file.
```


## 20. Assessment Anti-Cheating Rules

Invalid evidence:

```text
I watched a video.
I read a guide.
I generated a file.
I feel confident.
AI gave me the answer.
I copied solution.
I understood after seeing answer.
```

Valid evidence:

```text
I solved it independently.
I explained it under time pressure.
I wrote working code.
I passed a mock.
I defended project follow-ups.
I created a resume bullet with proof.
I repaired a weakness and passed retest.
```

Final rule:

```text
Assessment measures performance, not preparation.
```


## 21. Final Assessment Rule

The skill assessment is complete only when:

```text
scores are recorded
evidence is recorded
weaknesses are named
repair tasks are assigned
next roadmap phase is chosen
progress files are updated
```

The AI mentor must end with:

```text
Your current readiness verdict is:
...

Your next 3 actions are:
1.
2.
3.

The files to update are:
...
```
