# Data Engineering System Design Guide

Generated: 2026-06-06

This guide teaches **Data Engineering system design for interviews**.

It is written for **Data Engineering Sensei**, a strict, no-sugarcoating Data Engineering interview mentor. The goal is not to memorize cloud services or draw pretty boxes. The goal is to help a candidate design reliable, scalable, interview-ready data systems with clear requirements, trade-offs, data flow, storage, processing, data quality, orchestration, monitoring, failure handling, backfills, security, cost, and communication.

Use this guide for:

- Data Engineering system design interviews
- FAANG-style Data Engineering preparation
- data platform design rounds
- ETL/ELT architecture rounds
- batch pipeline design
- CDC pipeline design
- streaming/event pipeline design
- data warehouse/lake/lakehouse design
- project deep dives
- mock interviews
- weakness repair

Default standard:

```text
If target companies are not provided, train at FAANG-level Data Engineering system design standard.
```


## 1. Purpose

Data Engineering system design tests whether the candidate can design a production data system, not just explain tools.

A strong candidate can design systems that handle:

1. Data ingestion.
2. Data storage.
3. Data processing.
4. Data modeling.
5. Data quality.
6. Orchestration.
7. Monitoring.
8. Failure recovery.
9. Backfills.
10. Security.
11. Governance.
12. Cost.
13. Scale.
14. Trade-offs.
15. Consumer needs.

A weak answer says:

```text
Use Kafka, Spark, Airflow, and Snowflake.
```

A strong answer says:

```text
I will first clarify business requirements, data sources, volume, latency, consumers, and correctness needs. Then I will design ingestion, raw storage, processing, modeling, quality checks, orchestration, monitoring, backfill strategy, security, and cost controls. I will justify batch vs streaming and explain failure recovery.
```


## 2. What Data Engineering System Design Is

Data Engineering system design is the design of systems that move, transform, validate, store, and serve data reliably.

It usually includes:

- source systems
- ingestion layer
- raw/staging storage
- transformation layer
- serving layer
- data model
- orchestration
- data quality
- monitoring
- metadata
- failure handling
- backfills
- access/security
- cost controls

It is different from generic product system design.

Generic product design may focus on:

- APIs
- request latency
- caching
- databases
- load balancers
- microservices

Data Engineering design focuses more on:

- data volume
- freshness
- correctness
- schema evolution
- replayability
- idempotency
- lineage
- quality gates
- late data
- partitioning
- batch vs streaming
- data consumers
- analytical serving


## 3. Interview Standard

A Data Engineering system design answer is interview-ready only if it covers:

```text
Business goal:
Functional requirements:
Non-functional requirements:
Data sources:
Data volume:
Latency/freshness/SLA:
Consumers:
Batch/streaming/CDC choice:
Ingestion:
Raw storage:
Processing:
Data model:
Serving layer:
Orchestration:
Data quality:
Monitoring:
Failure handling:
Idempotency:
Backfills/replay:
Schema evolution:
Security/governance:
Cost:
Trade-offs:
Final summary:
```

If the candidate jumps to tools before requirements, score low.

Strict mentor correction:

```text
You jumped to Kafka and Spark before clarifying requirements. That is not system design. Start with business goal, data sources, volume, latency, and consumers.
```


## 4. The System Design Answer Flow

Use this flow in every interview.

```text
1. Clarify business goal.
2. Ask functional requirements.
3. Ask non-functional requirements.
4. Identify data sources.
5. Estimate data volume.
6. Define latency and freshness.
7. Identify consumers.
8. Choose batch, streaming, CDC, or hybrid.
9. Design ingestion.
10. Design raw/staging storage.
11. Design transformation layer.
12. Design serving layer.
13. Define data model.
14. Add orchestration.
15. Add data quality checks.
16. Add monitoring and alerting.
17. Add failure handling and idempotency.
18. Add backfill/replay strategy.
19. Add schema evolution.
20. Add security and governance.
21. Add cost controls.
22. Explain trade-offs.
23. Summarize final design.
```

This is the default structure for Data Engineering Sensei.


## 5. Clarifying Questions

Before designing, ask questions.

### Business goal

```text
What business decision or product does this data system support?
```

### Consumers

```text
Who will consume the data: dashboards, analysts, ML models, applications, finance, operations?
```

### Data sources

```text
What are the sources: OLTP databases, APIs, files, event streams, third-party vendors?
```

### Data volume

```text
How many records per day? What is the data size? What is peak volume?
```

### Latency

```text
Is this daily batch, hourly, near-real-time, or real-time?
```

### Correctness

```text
Is approximate data acceptable, or must it be exact?
```

### Updates and deletes

```text
Can source records update or delete after creation?
```

### Late data

```text
Can events arrive late?
```

### History

```text
Do we need historical changes or only latest state?
```

### Compliance

```text
Is there PII, financial data, or regulated data?
```

Strong answer:

```text
Before choosing architecture, I need to know volume, freshness, source behavior, consumers, and data correctness requirements.
```


## 6. Functional Requirements

Functional requirements describe what the system must do.

Examples:

```text
Ingest orders from OLTP database.
Ingest product files from vendor.
Process clickstream events.
Deduplicate events by event_id.
Build daily sales facts.
Build customer 360 table.
Expose dashboard marts.
Provide data quality reports.
Support historical backfills.
Support late-arriving events.
Track source-to-target lineage.
```

Strong answer format:

```text
The system must ingest [source], transform [data], produce [outputs], and serve [consumers].
```

Weak answer:

```text
The system should be scalable.
```

That is non-functional and too vague.


## 7. Non-Functional Requirements

Non-functional requirements describe system qualities.

Common Data Engineering non-functional requirements:

- freshness
- scalability
- reliability
- correctness
- observability
- replayability
- cost efficiency
- security
- governance
- maintainability
- fault tolerance
- idempotency
- SLA
- lineage
- auditability

Example:

```text
The sales dashboard must be fresh by 8 AM daily.
The system should handle 100 million events per day.
Pipeline failures should alert owners within 10 minutes.
Backfills should support 2 years of data.
PII must be masked for non-authorized users.
```

Strong answer:

```text
I will treat freshness, correctness, reliability, replayability, and cost as key non-functional requirements for this design.
```


## 8. Requirements vs Tools

Tools are not requirements.

Bad:

```text
We need Kafka, Spark, Airflow, Snowflake.
```

Better:

```text
We need near-real-time ingestion, distributed processing, workflow orchestration, and analytical serving.
```

Then map to tools:

```text
Kafka or managed streaming for ingestion.
Spark/Flink/warehouse SQL for processing.
Airflow or managed scheduler for orchestration.
Warehouse/lakehouse for serving.
```

Mentor rule:

```text
First define capability. Then choose tool.
```


## 9. Data Sources

Common sources:

- OLTP databases
- application event streams
- API endpoints
- vendor files
- SaaS exports
- logs
- object storage
- message queues
- legacy databases
- spreadsheets/manual uploads
- third-party data providers

For every source, ask:

```text
Source type:
Schema:
Volume:
Update frequency:
Change behavior:
Latency:
Access pattern:
Reliability:
Ownership:
Failure mode:
Security sensitivity:
```

Strong answer:

```text
Different source types need different ingestion patterns. Database tables may use CDC or incremental extraction, APIs need pagination and rate-limit handling, and vendor files need arrival checks and schema validation.
```


## 10. Data Volume Estimation

Estimate data volume early.

Questions:

```text
How many events per second?
How many records per day?
Average record size?
Peak traffic multiplier?
Retention period?
Number of source tables?
Number of consumers?
Historical backfill size?
```

Simple calculation:

```text
1000 events/second
= 86.4 million events/day

If each event is 1 KB:
86.4 GB/day before compression
```

Strong answer:

```text
Volume affects whether we use warehouse SQL, Spark, streaming, partitioning, file format, and storage design.
```

Weak answer:

```text
It should scale.
```

Not enough.


## 11. Latency and Freshness

Latency means how quickly data must be available.

Common categories:

| Requirement | Typical Design |
|---|---|
| Daily | batch |
| Hourly | scheduled batch/micro-batch |
| Minutes | streaming or frequent micro-batch |
| Seconds | streaming/event-driven |
| Ad hoc | query/warehouse/lake access |

Strong answer:

```text
If the dashboard only needs daily freshness, I would prefer batch for simplicity. I would choose streaming only if the business needs near-real-time data.
```

Strict correction:

```text
Do not choose streaming unless latency requirements justify the operational complexity.
```


## 12. Batch vs Streaming

### Batch

Good for:

- daily/hourly reports
- warehouse transformations
- simpler reliability
- easier backfills
- lower operational complexity
- historical processing

### Streaming

Good for:

- near-real-time alerts
- fraud detection
- live dashboards
- event-driven systems
- low-latency user activity
- operational monitoring

Trade-off:

```text
Streaming reduces latency but increases complexity around state, late data, replay, checkpointing, exactly-once/at-least-once semantics, and operations.
```

Strong answer:

```text
I choose batch unless the business requires low-latency data. If near-real-time is required, I design streaming with checkpoints, watermarks, replay, monitoring, and dead-letter handling.
```


## 13. Micro-Batch

Micro-batch processes data frequently in small batches.

Examples:

- every 5 minutes
- every 15 minutes
- hourly
- small streaming batches

Use when:

- near-real-time is useful
- full streaming is too complex
- data consumers can tolerate minutes of latency
- source supports incremental reads

Strong answer:

```text
Micro-batch is a practical middle ground between daily batch and continuous streaming.
```

Common use:

```text
Process events every 5 minutes and update operational dashboard.
```


## 14. CDC

CDC means Change Data Capture.

It captures inserts, updates, and deletes from source systems.

Use CDC when:

- source records update after creation
- deletes matter
- latest state must be accurate
- full table extraction is expensive
- downstream needs near-current database changes

CDC design considerations:

- source log capture
- ordering
- deletes
- schema changes
- offset tracking
- idempotent apply
- replay
- deduplication
- target merge logic
- lag monitoring

Strong answer:

```text
CDC is useful when source tables change over time and we need to capture inserts, updates, and deletes without full reloads.
```


## 15. Full Load vs Incremental Load

### Full load

Reloads everything.

Good for:

- small tables
- dimension reference data
- simple recovery
- initial load
- low cost/low volume

Bad for:

- huge tables
- frequent processing
- expensive scans

### Incremental load

Loads only new/changed data.

Good for:

- large tables
- regular pipelines
- lower cost
- faster processing

Needs:

- watermark
- CDC
- updated_at column
- reliable source change tracking
- idempotent target write
- late data handling

Strong answer:

```text
For small reference tables, full refresh may be simpler. For large fact/event tables, incremental load is usually needed.
```


## 16. Watermarking

A watermark tracks progress.

Batch incremental watermark example:

```text
last_successful_updated_at
```

Safe pattern:

```text
1. Read previous watermark.
2. Extract source changes after watermark.
3. Load staging.
4. Validate.
5. Merge target.
6. Commit new watermark only after success.
```

Strong answer:

```text
The watermark should advance only after the target load and validation succeed. Otherwise, failed runs can skip data permanently.
```

Common mistake:

```text
Updating watermark before target write completes.
```


## 17. Data Ingestion Layer

Ingestion brings data from sources into the data platform.

Ingestion patterns:

- database batch extraction
- CDC from database logs
- API pagination
- file ingestion
- event streaming
- SaaS connector sync
- log collection
- manual uploads

Ingestion must handle:

```text
Authentication:
Rate limits:
Pagination:
Retries:
Schema validation:
Raw data capture:
Deduplication:
Checkpoint/watermark:
Error handling:
Audit logs:
```

Strong answer:

```text
I would land raw data first before heavy transformations so we can replay and debug if downstream logic changes.
```


## 18. Raw Landing Zone

Raw landing stores source data with minimal transformation.

Purpose:

- replay
- audit
- debugging
- backfills
- lineage
- source preservation
- schema drift investigation

Common raw storage:

- object storage
- raw warehouse tables
- bronze tables
- immutable file paths
- partitioned by ingestion date/source

Strong answer:

```text
I preserve raw data so that if transformation logic changes, I can reprocess from the original source without calling the source again.
```

Red flag:

```text
Transforming and overwriting raw data immediately.
```


## 19. Staging Layer

Staging is the cleaned but not final layer.

Staging responsibilities:

- parse raw files
- standardize column names
- cast data types
- add ingestion metadata
- validate schema
- deduplicate raw records
- separate invalid records
- prepare for business transformations

Strong answer:

```text
Staging separates technical cleanup from business modeling. It makes final transformations cleaner and easier to test.
```

Common staging metadata:

```text
source_system
source_file
ingestion_time
batch_id
record_hash
pipeline_run_id
```


## 20. Curated / Serving Layer

Curated data is business-ready.

Examples:

- facts
- dimensions
- marts
- aggregates
- customer 360
- feature tables
- dashboard tables

Curated data should have:

- clear grain
- documented metrics
- quality checks
- ownership
- freshness SLA
- access controls
- lineage
- stable contracts

Strong answer:

```text
Curated tables should be consumer-ready and protected by quality gates before publishing.
```


## 21. Bronze, Silver, Gold

Common lakehouse/data lake layer pattern:

### Bronze

Raw or near-raw source data.

### Silver

Cleaned, standardized, deduplicated data.

### Gold

Business-ready facts, dimensions, aggregates, marts.

Strong answer:

```text
Bronze preserves raw data for replay, silver standardizes and cleans data, and gold provides business-ready datasets.
```

Do not assume every company uses these names. Explain the concept.


## 22. Storage Choices

Common storage/serving choices:

- object storage/data lake
- data warehouse
- lakehouse tables
- operational database
- search/index store
- cache
- feature store
- analytical marts

Choose based on:

```text
Data volume:
Query pattern:
Latency:
Cost:
Governance:
Update needs:
Consumer type:
Concurrency:
Schema evolution:
```

Strong answer:

```text
For raw large-scale files, object storage is cost-effective. For BI and SQL analytics, a warehouse or curated lakehouse table may be better.
```


## 23. Data Lake

A data lake stores raw and processed data, often in object storage.

Good for:

- large files
- raw data retention
- replay
- semi-structured data
- low-cost storage
- Spark processing
- ML/data science access

Risks:

- poor governance
- messy schemas
- small files
- unclear ownership
- hard discovery
- data swamp

Strong answer:

```text
A data lake is useful for scalable storage and replay, but it needs table organization, catalog, quality checks, ownership, and governance.
```


## 24. Data Warehouse

A data warehouse is optimized for analytical SQL and reporting.

Good for:

- BI dashboards
- governed analytics
- SQL transformations
- metric serving
- dimensional modeling
- analyst access

Strong answer:

```text
A warehouse is strong for curated analytical data and BI workloads. It should contain well-modeled, tested, documented tables, not uncontrolled raw dumps only.
```


## 25. Lakehouse

A lakehouse combines data lake storage with table-management features.

Common capabilities:

- ACID-like table operations
- schema evolution
- merge/upsert
- time travel in some systems
- metadata management
- scalable file storage
- SQL and Spark access

Interview-safe answer:

```text
A lakehouse approach can provide scalable storage with stronger table management than raw files, useful for large analytical datasets that need updates, schema evolution, and reliable reads.
```

Do not overclaim vendor-specific features unless platform is specified.


## 26. File Formats

File formats matter.

### CSV

Simple but weak schema and inefficient for analytics.

### JSON

Flexible and nested, but can be expensive to parse.

### Parquet

Columnar, compressed, efficient for analytics.

### Avro

Schema-based row format, common in event/streaming systems.

Strong answer:

```text
I may accept CSV/JSON as raw input, but for large analytical processing I would usually store curated data in columnar formats like Parquet or managed table formats.
```


## 27. Partitioning

Partitioning organizes data for pruning and manageability.

Common partition columns:

- event_date
- ingestion_date
- region
- source_system
- tenant_id for some multi-tenant designs

Avoid high-cardinality partitions:

- user_id
- event_id
- transaction_id
- email

Strong answer:

```text
For event/fact data, partitioning by date is often useful because most queries and backfills are date-bounded.
```

Warning:

```text
Bad partitioning can create too many small files or poor query pruning.
```


## 28. Clustering / Sorting

Some platforms support clustering, sorting, or ordering data within partitions.

Useful for:

- frequent filters
- joins
- range queries
- pruning
- performance on large tables

Strong answer:

```text
If queries often filter by customer_id within event_date, I may partition by event_date and cluster or sort by customer_id depending on the platform.
```

Do not force clustering if the platform does not support it.


## 29. Small Files Problem

Small files hurt data lake/lakehouse performance.

Causes:

- frequent small writes
- too many partitions
- streaming micro-batches
- high-cardinality partitioning
- no compaction

Impact:

- slow file listing
- many tasks
- metadata overhead
- slow query planning
- poor scan efficiency

Fixes:

- compaction
- tune output partitions
- avoid high-cardinality partition columns
- batch small writes
- use table optimization features where available

Strong answer:

```text
I would monitor file counts and sizes, and run compaction or tune write patterns to avoid small files.
```


## 30. Processing Layer

Processing transforms data.

Options:

- SQL in warehouse
- Spark/PySpark
- Flink or streaming engines
- dbt-style SQL transformations
- Python for small/custom processing
- managed cloud data processing
- stored procedures in some environments

Choose based on:

```text
Volume:
Latency:
Complexity:
Team skills:
Data location:
Cost:
Operational maturity:
```

Strong answer:

```text
I would use warehouse SQL for BI-style transformations when data is already in the warehouse, Spark for large data lake processing, and streaming engines when latency/state requirements justify them.
```


## 31. SQL vs Spark vs Python

### SQL

Good for:

- warehouse transformations
- aggregations
- joins
- BI datasets
- data quality checks

### Spark

Good for:

- large data lake processing
- distributed joins/aggregations
- big files
- heavy batch backfills

### Python

Good for:

- API ingestion
- orchestration helpers
- file parsing
- small/medium custom logic
- validation utilities

Strong answer:

```text
The choice depends on data volume, data location, latency, and maintainability. I would not use Spark if SQL can solve the problem more simply at acceptable cost.
```


## 32. Orchestration

Orchestration coordinates workflows.

It handles:

- task dependencies
- schedules
- retries
- sensors
- backfills
- alerts
- SLAs
- parameters
- run metadata

Strong answer:

```text
I would use orchestration to coordinate ingestion, transformation, validation, publishing, and alerting. Each task should be idempotent and backfill-safe.
```

Red flag:

```text
Airflow just schedules jobs.
```

Not enough.


## 33. DAG Design

A Data Engineering DAG should show meaningful task boundaries.

Example:

```text
check_source_ready
  ->
extract_source
  ->
land_raw
  ->
validate_raw
  ->
load_staging
  ->
transform_curated
  ->
run_quality_checks
  ->
publish
  ->
notify
```

Strong answer:

```text
I separate extraction, validation, transformation, quality checks, and publishing so failures are easier to isolate and rerun.
```

Avoid:

- one giant task
- hundreds of tiny tasks without reason
- hardcoded dates
- no retries
- no quality gates


## 34. Idempotency

Idempotency means rerunning produces the same final result.

Why it matters:

- retries
- manual reruns
- backfills
- partial failures
- duplicate source records
- exactly-once-like outcomes

Strategies:

- overwrite partition
- merge/upsert by stable key
- staging then swap
- delete-and-reload scoped partition
- processed file manifest
- deterministic output path
- commit watermark only after success

Strong answer:

```text
Every task that writes data should be safe to rerun. Otherwise retries can duplicate or corrupt data.
```


## 35. Backfills

Backfill means reprocessing historical data.

Reasons:

- missed runs
- bug fix
- schema change
- new metric logic
- source correction
- late data
- initial load
- replay after failure

Good backfill design:

```text
Parameterized date range:
Raw data retained:
Idempotent writes:
Partition-level processing:
Quality checks:
Controlled concurrency:
Cost awareness:
Downstream refresh:
Metadata logging:
Communication to consumers:
```

Strong answer:

```text
Backfills should use the same transformation logic as regular runs when possible to avoid logic drift.
```


## 36. Replay

Replay means reprocessing data from an earlier point.

Important for:

- streaming recovery
- CDC recovery
- event reprocessing
- bug fixes
- downstream rebuilds

Need:

- raw data retention
- offsets/checkpoints
- deterministic processing
- idempotent writes
- versioned logic if possible
- quality validation
- controlled load

Strong answer:

```text
I design raw storage and checkpoints so that data can be replayed safely if downstream logic fails or needs correction.
```


## 37. Data Quality

Data quality is mandatory in Data Engineering system design.

Types of checks:

- schema checks
- required fields
- null checks
- duplicate key checks
- row count checks
- accepted values
- referential integrity
- freshness
- reconciliation
- anomaly detection
- volume thresholds
- business rules

Strong answer:

```text
I would run quality checks before publishing curated data. Critical failures should block publish and alert owners.
```

Strict correction:

```text
A pipeline that runs successfully but publishes bad data is still a failed pipeline.
```


## 38. Quality Gates

A quality gate blocks bad data from reaching consumers.

Example flow:

```text
transform_curated
  ->
quality_checks
  ->
publish_if_passed
```

Critical quality failures:

- missing primary keys
- duplicate business keys
- severe row count drop
- schema mismatch
- revenue reconciliation failure
- stale data
- invalid required fields

Strong answer:

```text
I separate transform and publish so that failed quality checks do not expose bad data to dashboards.
```


## 39. Monitoring

Monitoring tracks system health and data health.

System monitoring:

- job success/failure
- runtime
- retries
- queue delays
- compute usage
- memory/CPU
- streaming lag

Data monitoring:

- freshness
- row count
- null rates
- duplicate rates
- schema changes
- metric anomalies
- reconciliation differences

Strong answer:

```text
I monitor both pipeline execution and data correctness. Job success alone is not enough.
```


## 40. Alerting

Alerts should be actionable.

Bad alert:

```text
Pipeline failed.
```

Good alert:

```text
daily_sales_pipeline failed on transform_fact_sales for process_date=2025-01-01. Source orders loaded 1.2M rows, target write failed due to duplicate order_id. Dashboard SLA 8 AM at risk. Owner: Sales Data Team. Runbook: link.
```

Alert should include:

- pipeline name
- task name
- run date
- severity
- affected dataset
- error reason
- SLA impact
- owner
- suggested action
- runbook link

Strong answer:

```text
Alerts should tell the on-call engineer what failed, what data is affected, and what action to take.
```


## 41. Run Metadata

Track pipeline metadata.

Useful metadata:

```text
pipeline_run_id
source_system
source_table/file
process_date
start_time
end_time
status
row_count_in
row_count_out
invalid_count
watermark_start
watermark_end
quality_check_status
error_message
retry_count
code_version
```

Strong answer:

```text
Run metadata supports debugging, auditability, backfills, and SLA tracking.
```


## 42. Lineage

Lineage shows where data came from and how it was transformed.

Lineage helps answer:

- Which sources feed this table?
- Which dashboards are affected by this source failure?
- Which jobs produced this column?
- What breaks if we change this schema?
- Which downstream consumers are impacted?

Strong answer:

```text
Lineage is important for impact analysis, debugging, governance, and consumer trust.
```


## 43. Data Contracts

A data contract defines expectations between producer and consumer.

Can include:

- schema
- column types
- required fields
- freshness
- allowed values
- ownership
- change process
- quality expectations
- SLA

Strong answer:

```text
Data contracts reduce unexpected breaking changes by making producer responsibilities explicit.
```

Use when:

- many teams depend on shared datasets
- source schema changes often
- data quality issues repeatedly break consumers


## 44. Schema Evolution

Schema changes are common.

Types:

- new column
- removed column
- renamed column
- type change
- nullable to non-nullable
- nested JSON change
- enum value change

Design response:

```text
Detect schema changes.
Classify compatible vs breaking.
Allow additive changes when safe.
Fail or alert on breaking changes.
Version contracts where needed.
Backfill if new field required historically.
```

Strong answer:

```text
I would not let unexpected schema changes silently flow into curated tables. Breaking changes should fail fast and alert owners.
```


## 45. Late-Arriving Data

Late-arriving data arrives after the expected processing window.

Examples:

- mobile events uploaded later
- CDC lag
- source system delay
- timezone issues
- vendor file resend
- network failure

Strategies:

- process by event_time but track ingestion_time
- use lookback windows
- reprocess recent partitions
- streaming watermarks
- late-event correction pipeline
- partition overwrite/merge
- alert on late volume spikes

Strong answer:

```text
I would design for late data by using event_time for business metrics, ingestion_time for operations, and a lookback or correction strategy for affected partitions.
```


## 46. Duplicate Handling

Duplicates can come from:

- retries
- source bugs
- CDC replay
- file resend
- API pagination overlap
- at-least-once delivery
- manual reprocessing

Deduplication needs:

```text
dedupe key
ordering field
tie-breaker
invalid key handling
scope/window
quality check
```

Strong answer:

```text
If records can duplicate, I need a stable dedupe key and deterministic rule for which record wins.
```

Example:

```text
event_id + latest event_time + ingestion_time tie-breaker
```


## 47. Deletes

Deletes are often forgotten.

Source delete types:

- hard delete
- soft delete
- CDC delete event
- status changed to inactive
- GDPR deletion request

Design options:

- propagate delete to target
- mark record inactive
- use is_deleted flag
- maintain history with SCD2
- tombstone records
- restrict delete in analytics but mask PII

Strong answer:

```text
I would clarify whether source deletes must be reflected downstream. CDC delete handling and compliance deletes need explicit design.
```


## 48. Security

Security must be included.

Topics:

- authentication
- authorization
- least privilege
- service accounts
- secrets management
- encryption at rest
- encryption in transit
- PII masking
- row/column-level access
- audit logs
- environment separation
- secure sharing

Strong answer:

```text
Data pipelines often move sensitive data, so secrets should not be hardcoded, access should follow least privilege, and PII should be masked or restricted for unauthorized users.
```


## 49. PII and Sensitive Data

PII examples:

- name
- email
- phone
- address
- government IDs
- payment identifiers
- precise location
- device identifiers in some contexts

Handling:

- classify sensitive fields
- mask/tokenize where possible
- encrypt
- restrict access
- avoid logging PII
- apply retention policies
- audit access
- support deletion requests if required

Strong answer:

```text
I would classify sensitive columns early and apply access controls, masking, and audit logging before exposing data broadly.
```


## 50. Governance

Governance includes:

- ownership
- documentation
- data catalog
- lineage
- quality SLAs
- access controls
- retention policies
- metric definitions
- certification/trusted datasets
- change management

Strong answer:

```text
Governance prevents the data platform from becoming a data swamp. Trusted datasets need owners, definitions, quality checks, and access controls.
```


## 51. Cost Design

Data systems can become expensive.

Cost drivers:

- compute runtime
- streaming infrastructure
- warehouse scans
- storage retention
- backfills
- repeated full refreshes
- small files
- over-partitioning
- unnecessary actions
- high concurrency
- duplicate pipelines
- inefficient joins

Cost controls:

- partition pruning
- incremental loads
- right-size compute
- autoscaling where appropriate
- compaction
- caching/materialization only when useful
- query optimization
- retention policies
- separate dev/prod
- monitor spend by pipeline

Strong answer:

```text
I would design for cost by reducing scanned data, avoiding unnecessary full refreshes, controlling backfill concurrency, and monitoring expensive queries/jobs.
```


## 52. Reliability

Reliability means the system works consistently and recovers from failures.

Design elements:

- retries with backoff
- idempotent writes
- quality gates
- checkpoints
- replay
- backfills
- alerts
- runbooks
- metadata tracking
- isolation of failures
- graceful degradation

Strong answer:

```text
Reliability is not only job retries. It includes idempotent recovery, validation, and clear operational ownership.
```


## 53. Failure Handling

Classify failures:

1. Source unavailable.
2. Source schema changed.
3. Missing file.
4. API rate limit.
5. Partial extraction.
6. Bad data.
7. Transformation error.
8. Write failure.
9. Quality check failure.
10. Orchestrator failure.
11. Compute failure.
12. Downstream publish failure.

For each failure, define:

```text
Detection:
Retry or fail:
Quarantine or block:
Alert owner:
Recovery action:
Validation after recovery:
```

Strong answer:

```text
Transient failures can retry. Data quality and schema failures should fail fast and alert because retrying will not fix bad data.
```


## 54. Runbooks

A runbook tells operators how to recover.

Runbook contents:

```text
Pipeline purpose:
Owner:
Schedule:
SLA:
Sources:
Targets:
Common failures:
How to rerun:
How to backfill:
Quality checks:
Alert meanings:
Escalation path:
Known limitations:
```

Strong answer:

```text
A production data system needs runbooks because failures often happen when the original developer is not available.
```


## 55. Serving Layer

Serving layer exposes data to consumers.

Serving options:

- warehouse tables
- marts
- dashboards
- APIs
- feature store
- search index
- reverse ETL destination
- extracts/files

Choose based on:

```text
Consumer:
Query pattern:
Latency:
Concurrency:
Access control:
Freshness:
Cost:
```

Strong answer:

```text
For BI consumers, curated warehouse marts are usually appropriate. For ML, feature tables or feature stores may be needed. For applications, an API or operational store may be required.
```


## 56. Data Modeling in System Design

System design must include data modeling.

You should define:

```text
Business process:
Output grain:
Facts:
Dimensions:
Keys:
History/SCD:
Metric definitions:
Aggregates:
Consumers:
Quality checks:
```

Strong answer:

```text
For a sales mart, I would define fact_sales at order-item grain, with dimensions for customer, product, date, and store. Revenue would be quantity * unit_price minus discounts, excluding cancelled orders based on business rule.
```

Red flag:

```text
No grain, just a list of tables.
```


## 57. Metric Definitions

Metrics must be defined clearly.

Example: revenue.

Questions:

```text
Does revenue include tax?
Does it include shipping?
Are refunds subtracted?
Are cancelled orders excluded?
Which timestamp defines revenue date?
What currency conversion is used?
```

Strong answer:

```text
I would document metric definitions and implement them consistently in curated marts to avoid multiple teams calculating different numbers.
```


## 58. SLA and Freshness

SLA defines when data must be ready.

Example:

```text
Daily sales dashboard fresh by 8 AM local time.
```

Design impact:

- schedule time
- retries
- upstream dependency timing
- alerting
- monitoring
- fallback behavior
- priority

Strong answer:

```text
Schedule is not the same as SLA. I need to monitor whether the final consumer table is fresh by the business deadline.
```


## 59. Multi-Tenant Design

Multi-tenant data systems serve multiple customers/tenants.

Consider:

- tenant_id in data model
- isolation requirements
- access controls
- partitioning/clustering
- noisy neighbor risk
- per-tenant backfills
- per-tenant SLAs
- data deletion
- audit logs

Strong answer:

```text
If the platform is multi-tenant, I need to ensure tenant isolation in storage, processing, access controls, and monitoring.
```


## 60. Build vs Buy

Sometimes system design includes tool choice.

Build when:

- requirements are custom
- scale is unique
- strong internal expertise
- cost justifies it
- existing tools are insufficient

Buy/use managed when:

- standard capability exists
- team wants lower ops burden
- faster delivery matters
- reliability/compliance is easier
- cost is acceptable

Strong answer:

```text
I would avoid building custom orchestration or ingestion if a reliable managed tool meets the requirements. Custom systems create maintenance burden.
```


## 61. Trade-Off Communication

System design is about trade-offs.

Common trade-offs:

| Choice | Benefit | Cost |
|---|---|---|
| Batch | simpler, cheaper | higher latency |
| Streaming | low latency | operational complexity |
| Full load | simple | expensive at scale |
| Incremental | efficient | watermark complexity |
| Data lake | cheap/replayable | governance risk |
| Warehouse | SQL/BI friendly | scan/compute cost |
| Spark | scalable processing | operational overhead |
| dbt/SQL | maintainable SQL | may struggle with huge files |
| Denormalized mart | faster queries | duplicate storage |
| Normalized model | consistency | more joins |

Strong answer:

```text
I choose batch here because the SLA is daily. Streaming would add complexity without business value.
```


## 62. High-Level Architecture Template

Use this template.

```text
Sources
  ->
Ingestion Layer
  ->
Raw/Bronze Storage
  ->
Staging/Silver Processing
  ->
Curated/Gold Data Model
  ->
Serving Layer
  ->
Consumers

Cross-cutting:
Orchestration
Data Quality
Monitoring
Metadata/Lineage
Security
Cost Controls
Backfill/Replay
```

Interview tip:

```text
Draw or describe the main flow first, then add operational concerns.
```


## 63. Batch Pipeline Design Template

Use for daily/hourly pipelines.

```text
1. Source extract by process date or watermark.
2. Land raw data.
3. Validate schema and required fields.
4. Load staging.
5. Deduplicate.
6. Transform into facts/dimensions.
7. Run quality checks.
8. Publish curated tables.
9. Update metadata/watermark.
10. Alert success/failure.
```

Must include:

- idempotent write
- backfill by date range
- quality gate
- SLA/freshness monitoring
- run metadata

Strong answer:

```text
For a daily reporting pipeline, batch is simpler and easier to backfill than streaming.
```


## 64. Streaming Pipeline Design Template

Use when low latency is required.

```text
Event producers
  ->
Message broker / streaming ingest
  ->
Stream processing
  ->
Raw event storage
  ->
Real-time serving / aggregates
  ->
Batch correction path
```

Must include:

- event schema
- event_id
- partition key
- ordering expectations
- checkpointing
- watermarks
- late data
- deduplication
- dead-letter queue
- monitoring lag
- replay strategy
- downstream consistency

Strong answer:

```text
For streaming, I design both real-time processing and a replay/correction path because streaming systems still fail and late data happens.
```


## 65. CDC Pipeline Design Template

CDC pipeline flow:

```text
Source database log
  ->
CDC capture connector
  ->
Change event stream/storage
  ->
Staging change table
  ->
Apply inserts/updates/deletes
  ->
Curated latest-state table or history table
  ->
Quality checks and lag monitoring
```

Must include:

- ordering
- primary keys
- deletes
- schema changes
- offset tracking
- idempotent apply
- replay
- lag monitoring
- merge/upsert
- SCD if history required

Strong answer:

```text
CDC is not just ingestion. The target apply logic must correctly handle inserts, updates, deletes, ordering, and replay.
```


## 66. API Ingestion Design Template

API ingestion flow:

```text
Read cursor/watermark
  ->
Call API pages
  ->
Handle rate limits/retries
  ->
Store raw responses
  ->
Normalize JSON
  ->
Validate records
  ->
Load staging/target
  ->
Commit cursor after success
```

Must include:

- pagination
- authentication
- rate limits
- retries with backoff
- partial page failure handling
- raw response storage
- schema drift
- cursor safety
- idempotent load

Strong answer:

```text
I would commit the API cursor only after raw storage, normalization, validation, and target load succeed.
```


## 67. File Ingestion Design Template

File ingestion flow:

```text
Wait/check file arrival
  ->
Validate filename/checksum/schema
  ->
Copy to raw/archive
  ->
Load staging
  ->
Validate rows
  ->
Transform
  ->
Publish
  ->
Mark file processed
```

Must include:

- file sensor with timeout
- duplicate file detection
- checksum
- schema validation
- bad file quarantine
- processed manifest
- late file handling
- resend/correction handling

Strong answer:

```text
For vendor files, I would track processed files with checksum so corrected resends can be handled safely.
```


## 68. Scenario: Daily Sales Analytics Platform

Prompt:

```text
Design a daily sales analytics pipeline for an e-commerce company.
```

Strong answer outline:

1. Clarify dashboard SLA and revenue definition.
2. Sources: orders, order_items, payments, customers, products.
3. Ingest source tables incrementally or via CDC.
4. Land raw data by ingestion date.
5. Stage and validate required fields.
6. Deduplicate by business keys.
7. Build fact_sales at order-item grain.
8. Build dimensions for customer, product, date.
9. Exclude cancelled orders or handle based on metric definition.
10. Run row count and revenue reconciliation.
11. Publish sales mart by date/category/customer segment.
12. Orchestrate daily before SLA.
13. Support backfills by order_date.
14. Monitor freshness and quality.
15. Secure PII in customer data.
16. Control cost with partitioning and incremental loads.

Follow-ups:

- What if orders are updated after creation?
- How do refunds affect revenue?
- How do you backfill last month?
- What if product dimension changes?
- How do you validate revenue?


## 69. Scenario: Clickstream Analytics

Prompt:

```text
Design a system to process clickstream events for product analytics.
```

Strong answer outline:

1. Clarify latency: real-time or daily?
2. Event producers send events with event_id, user_id, event_type, event_time.
3. Use streaming ingestion if near-real-time is needed, otherwise batch/micro-batch.
4. Store raw events in data lake partitioned by ingestion_date/event_date.
5. Validate schema and required fields.
6. Deduplicate by event_id.
7. Handle late events with lookback/window strategy.
8. Build event-level curated table.
9. Build aggregates by event_date, event_type, page, campaign.
10. Serve dashboards from warehouse/lakehouse mart.
11. Monitor event volume, freshness, duplicate rate, schema changes.
12. Add replay/backfill from raw events.
13. Secure user identifiers.

Follow-ups:

- What if event volume spikes?
- What if events arrive late?
- How do you handle duplicate event_id?
- What if schema changes?
- What if product wants real-time dashboard?


## 70. Scenario: Customer 360

Prompt:

```text
Design a Customer 360 data system.
```

Strong answer outline:

1. Identify consumers: marketing, support, analytics, ML.
2. Sources: CRM, orders, payments, web events, support tickets, email campaigns.
3. Resolve customer identity across systems.
4. Ingest raw data from multiple systems.
5. Standardize customer keys.
6. Build identity mapping table.
7. Build dimensions and customer attributes.
8. Aggregate behavioral metrics.
9. Handle SCD/history for profile changes.
10. Apply PII access controls.
11. Run quality checks for duplicate identities and missing keys.
12. Publish customer_360 table/mart.
13. Monitor freshness by source.
14. Support source-specific backfills.

Follow-ups:

- How do you resolve duplicate customers?
- How do you handle PII?
- What if email changes?
- How do you avoid incorrect merges?
- How do you track history?


## 71. Scenario: CDC to Warehouse

Prompt:

```text
Design a CDC pipeline from a transactional database to a warehouse.
```

Strong answer outline:

1. Identify source tables and primary keys.
2. Use CDC capture from database logs or managed connector.
3. Store change events raw for replay.
4. Track offsets and lag.
5. Apply changes to staging tables.
6. Merge into warehouse tables.
7. Handle inserts, updates, deletes.
8. Deduplicate/reorder if needed.
9. Monitor CDC lag and failures.
10. Handle schema changes.
11. Validate source-target counts or checksums.
12. Support replay from offsets.
13. Protect source database load.
14. Secure credentials and PII.

Follow-ups:

- What if delete events arrive?
- What if events are out of order?
- What if CDC connector fails for 2 hours?
- How do you backfill initial snapshot?
- How do you handle schema changes?


## 72. Scenario: Data Quality Platform

Prompt:

```text
Design a data quality framework for warehouse tables.
```

Strong answer outline:

1. Identify critical datasets and owners.
2. Define checks: nulls, duplicates, row counts, freshness, accepted values, reconciliation.
3. Store rules in metadata/config.
4. Run checks after transformations and before publish.
5. Store results in quality_results table.
6. Alert owners on critical failures.
7. Track quality trends over time.
8. Block publish for critical datasets.
9. Provide dashboard for quality health.
10. Support severity levels.
11. Integrate with orchestration.
12. Add runbooks.

Follow-ups:

- Which checks block publish?
- How do you avoid alert fatigue?
- How do you define thresholds?
- How do you handle false positives?
- How do you onboard new tables?


## 73. Scenario: Real-Time Fraud Signals

Prompt:

```text
Design a near-real-time fraud signal pipeline.
```

Strong answer outline:

1. Clarify latency requirement and correctness tolerance.
2. Event sources: transactions, login events, device events.
3. Stream ingestion with event_id and event_time.
4. Stream processing for features/signals.
5. State management for rolling windows.
6. Watermarks for late data.
7. Deduplication.
8. Low-latency serving store or feature store.
9. Dead-letter queue for malformed events.
10. Raw event storage for replay.
11. Monitor lag, error rate, duplicate rate.
12. Security for financial/PII data.
13. Batch reconciliation/correction path.

Follow-ups:

- What if events arrive late?
- What if duplicate transactions appear?
- What if model needs historical features?
- How do you replay events?
- What if streaming job fails?


## 74. Scenario: Reporting Warehouse

Prompt:

```text
Design a reporting warehouse for company-wide analytics.
```

Strong answer outline:

1. Identify domains: sales, finance, product, marketing.
2. Ingest sources into raw/staging.
3. Define dimensional models.
4. Build facts and dimensions.
5. Define metric layer or certified marts.
6. Add data quality checks.
7. Add lineage/catalog.
8. Add access controls.
9. Schedule transformations.
10. Monitor freshness and usage.
11. Control cost with partitioning/clustering.
12. Support backfills and historical corrections.

Follow-ups:

- How do you prevent metric inconsistency?
- How do analysts discover data?
- How do you handle slowly changing dimensions?
- How do you control warehouse costs?
- How do you govern access?


## 75. Scenario: ML Feature Pipeline

Prompt:

```text
Design a data pipeline to generate ML features daily.
```

Strong answer outline:

1. Clarify model use case and prediction time.
2. Identify source data and labels.
3. Prevent training-serving skew.
4. Build point-in-time correct features.
5. Avoid data leakage.
6. Store features with timestamp/entity key.
7. Validate feature completeness and distributions.
8. Support backfills for training.
9. Serve batch or online features depending need.
10. Monitor freshness and drift.
11. Version feature logic.
12. Secure sensitive data.

Follow-ups:

- What is data leakage?
- What does point-in-time correctness mean?
- How do you backfill training features?
- How do you monitor drift?
- Batch vs online features?


## 76. Scenario: Vendor File Platform

Prompt:

```text
Design a platform for ingesting daily vendor files.
```

Strong answer outline:

1. File arrival method: SFTP/object storage/email is not ideal but may happen.
2. File sensor with SLA/timeout.
3. Validate file naming, checksum, schema.
4. Store raw file in archive.
5. Track processed files in manifest.
6. Load staging.
7. Quarantine bad rows/files.
8. Transform and publish.
9. Handle late or corrected files.
10. Alert vendor/owner on missing or invalid file.
11. Support historical reloads.
12. Secure file transfer and access.

Follow-ups:

- What if file arrives late?
- What if vendor resends same filename with corrected data?
- What if schema changes?
- What if file is partially uploaded?
- How do you avoid duplicate processing?


## 77. Scenario: Data Platform Migration

Prompt:

```text
Design migration from legacy on-prem data warehouse to cloud data platform.
```

Strong answer outline:

1. Inventory sources, tables, jobs, consumers.
2. Classify criticality and dependencies.
3. Choose migration strategy: phased/domain-by-domain.
4. Build ingestion to cloud raw layer.
5. Rebuild transformations with validation.
6. Run parallel pipelines.
7. Reconcile source and target metrics.
8. Migrate dashboards and consumers.
9. Define rollback plan.
10. Secure access and networking.
11. Optimize costs.
12. Decommission legacy after signoff.

Follow-ups:

- How do you validate migration?
- Big bang vs phased?
- How do you handle downtime?
- How do you handle historical data?
- What is rollback plan?


## 78. Weak vs Strong Answers

### Question: Design a data pipeline

Weak:

```text
Use Kafka, Spark, Airflow, and Snowflake.
```

Strong:

```text
I will clarify requirements first. If the dashboard needs daily data, I will use batch ingestion into raw storage, transform into curated warehouse tables, run quality checks, orchestrate with retries and backfills, and monitor freshness. If near-real-time is needed, I will add streaming ingestion and a replay path.
```

### Question: How do you handle failures?

Weak:

```text
Airflow retries.
```

Strong:

```text
I classify failures. Transient infrastructure failures can retry with backoff. Schema and data quality failures should fail fast and alert owners. Writes must be idempotent so reruns do not duplicate data.
```

### Question: How do you handle backfills?

Weak:

```text
Rerun the job.
```

Strong:

```text
I parameterize by date range, read from raw data, write only affected partitions idempotently, validate each partition, control concurrency/cost, and refresh downstream marts.
```


## 79. Common Interview Red Flags

Flag strongly:

1. Jumps to tools before requirements.
2. No business goal.
3. No data volume estimate.
4. No latency/SLA discussion.
5. No consumers.
6. Batch vs streaming not justified.
7. No raw layer.
8. No data quality checks.
9. No monitoring.
10. No failure handling.
11. No idempotency.
12. No backfill/replay.
13. No schema evolution.
14. No late data handling.
15. No duplicate handling.
16. No security/PII.
17. No cost discussion.
18. No data model/grain.
19. No trade-offs.
20. Tool list with no architecture.
21. Streaming for everything.
22. Full reload for huge data without reason.
23. No ownership/runbook.
24. No reconciliation.
25. No final summary.


## 80. System Design Scoring Rubric

### Score 0

No usable design.

Candidate cannot explain sources, flow, or output.

### Score 1

Tool-name answer only.

Mentions tools but not requirements, quality, failures, or trade-offs.

### Score 2

Basic pipeline design.

Includes ingestion, processing, and storage, but misses production concerns.

### Score 3

Developing.

Covers main flow and some quality/monitoring, but lacks depth in backfills, idempotency, schema evolution, cost, or trade-offs.

### Score 4

Interview-ready.

Covers requirements, data flow, batch/stream choice, storage, processing, modeling, orchestration, quality, monitoring, failures, backfills, security, and cost.

### Score 5

Strong.

Handles ambiguity, scale, trade-offs, failure modes, replay, governance, multi-consumer needs, and pressure follow-ups clearly.


## 81. Module-Specific Scoring

Score each design by category.

| Category | Weight |
|---|---:|
| Requirements clarification | 15% |
| Architecture correctness | 20% |
| Data modeling and serving | 15% |
| Reliability and failure handling | 15% |
| Data quality and monitoring | 15% |
| Security, governance, cost | 10% |
| Communication and trade-offs | 10% |

A candidate cannot score above 3.5 if they miss idempotency and backfills.

A candidate cannot score above 3 if they miss data quality.

A candidate cannot score above 3 if they only list tools.


## 82. Review Checklist

When reviewing a system design answer, check:

```text
Business goal clarified:
Functional requirements listed:
Non-functional requirements listed:
Data sources identified:
Data volume estimated:
Latency/SLA defined:
Consumers identified:
Batch/streaming/CDC justified:
Ingestion design clear:
Raw storage included:
Processing layer clear:
Serving layer clear:
Data model/grain included:
Orchestration included:
Data quality checks included:
Monitoring and alerting included:
Failure handling included:
Idempotency included:
Backfill/replay included:
Schema evolution included:
Late data included:
Duplicate handling included:
Security/PII included:
Cost controls included:
Trade-offs explained:
Final summary given:
```


## 83. Communication Template

Use this exact communication structure.

```text
I will design this in stages.

First, I will clarify requirements:
[questions]

Assumptions:
[reasonable assumptions if interviewer does not specify]

High-level architecture:
[sources → ingestion → raw → processing → serving → consumers]

Ingestion:
[how data enters]

Storage:
[raw/staging/curated]

Processing:
[batch/stream/CDC and why]

Data model:
[facts/dimensions/grain or output datasets]

Quality:
[checks and gates]

Orchestration:
[schedule, dependencies, retries]

Monitoring:
[freshness, failures, data metrics]

Failure recovery:
[idempotency, backfills, replay]

Security/governance:
[PII, access, lineage]

Cost:
[partitioning, incremental loads, compute controls]

Trade-offs:
[why this design]

Summary:
[short final recap]
```


## 84. Strict Feedback Templates

### Tool-first answer

```text
This is a tool list, not a system design. Restart with requirements, data sources, volume, latency, and consumers.
```

### No data quality

```text
This design is not production-ready. You did not include data quality checks or quality gates before publishing.
```

### No idempotency

```text
Retries and backfills can duplicate data in your design. Explain how writes are idempotent.
```

### No backfill

```text
You did not explain how to reprocess historical data. A Data Engineering system must support backfills or replay.
```

### Streaming overuse

```text
You chose streaming without a latency requirement. Streaming adds complexity. Justify it or use batch/micro-batch.
```

### No cost

```text
This may work technically, but it ignores cost. Explain how you reduce scans, avoid full refreshes, and control backfill compute.
```


## 85. 7-Day System Design Repair Plan

### Day 1: Requirements and architecture flow

Drill:

```text
Design a daily batch sales pipeline.
```

Exit:

```text
Candidate clarifies business goal, sources, volume, SLA, and consumers.
```

### Day 2: Batch, incremental, CDC, streaming

Drill:

```text
Choose batch vs streaming vs CDC for 5 scenarios.
```

Exit:

```text
Candidate justifies choice with latency and source behavior.
```

### Day 3: Storage and modeling

Drill:

```text
Design raw, staging, curated layers and fact/dimension outputs.
```

Exit:

```text
Candidate defines table grain.
```

### Day 4: Quality and monitoring

Drill:

```text
Add quality gates and monitoring to a pipeline.
```

Exit:

```text
Candidate separates job success from data correctness.
```

### Day 5: Failures, idempotency, backfills

Drill:

```text
A pipeline fails halfway. Explain recovery.
```

Exit:

```text
Candidate explains idempotent rerun and watermark safety.
```

### Day 6: Security, governance, cost

Drill:

```text
Add PII protection, lineage, and cost controls.
```

Exit:

```text
Candidate covers non-functional requirements.
```

### Day 7: Full mock

Prompt:

```text
Design an end-to-end e-commerce data platform with batch orders, streaming events, CDC customers, quality checks, and dashboard serving.
```

Exit:

```text
Candidate scores 4/5 or higher.
```


## 86. 30-Day System Design Plan

### Week 1: Core design foundations

- requirements
- data sources
- batch vs streaming
- ingestion
- raw/staging/curated
- storage choices

Practice:

- daily sales pipeline
- vendor file ingestion
- API ingestion

### Week 2: Reliability and operations

- orchestration
- retries
- idempotency
- backfills
- monitoring
- alerting
- run metadata

Practice:

- failure recovery scenarios
- backfill design
- SLA monitoring

### Week 3: Advanced data systems

- CDC
- streaming
- late data
- schema evolution
- data contracts
- quality platform
- lineage

Practice:

- CDC to warehouse
- clickstream analytics
- data quality framework

### Week 4: FAANG-style mocks

- customer 360
- reporting warehouse
- ML feature pipeline
- data platform migration
- mixed follow-ups
- strict scoring


## 87. Mock Interview 1: Daily Batch Pipeline

Prompt:

```text
Design a daily orders reporting pipeline.
```

Expected answer:

- clarify SLA
- source database extraction
- incremental or CDC choice
- raw landing
- staging validation
- fact_orders/fact_sales model
- quality checks
- orchestration
- idempotent partition writes
- backfill by order_date
- freshness monitoring
- PII handling
- cost controls

Follow-ups:

1. What if orders update after creation?
2. What if the job fails after writing half the target?
3. How do you validate revenue?
4. How do you rerun last month?
5. Why batch instead of streaming?


## 88. Mock Interview 2: Streaming Events

Prompt:

```text
Design near-real-time event analytics for product usage.
```

Expected answer:

- clarify latency
- event schema
- event_id and event_time
- streaming ingestion
- raw event storage
- stream processing
- checkpointing
- watermarks
- deduplication
- late data handling
- real-time aggregate store
- batch correction path
- lag monitoring
- replay
- dead-letter queue

Follow-ups:

1. What if events arrive late?
2. What if duplicates happen?
3. How do you replay?
4. What if schema changes?
5. How do you monitor lag?


## 89. Mock Interview 3: CDC Pipeline

Prompt:

```text
Design a CDC pipeline from PostgreSQL/MySQL-style OLTP database to a warehouse.
```

Expected answer:

- initial snapshot
- log-based change capture
- raw change event storage
- offsets
- inserts/updates/deletes
- staging
- merge target
- schema evolution
- lag monitoring
- replay
- idempotent apply
- source impact protection

Follow-ups:

1. How do you handle deletes?
2. How do you handle out-of-order events?
3. What if connector fails?
4. How do you backfill initial data?
5. How do you validate source vs target?


## 90. Mock Interview 4: Data Quality Framework

Prompt:

```text
Design a framework that checks data quality across warehouse tables.
```

Expected answer:

- metadata-driven rules
- table owners
- check types
- severity levels
- quality results table
- orchestration integration
- blocking critical publish
- alert routing
- quality dashboard
- historical trends
- false positive management

Follow-ups:

1. Which checks are critical?
2. How do you onboard new tables?
3. How do you avoid alert fatigue?
4. How do you store results?
5. How do you handle schema drift?


## 91. Mock Interview 5: Customer 360

Prompt:

```text
Design Customer 360 for analytics and marketing.
```

Expected answer:

- identify consumers
- ingest multiple sources
- identity resolution
- customer keys
- source priority
- SCD/history
- behavioral aggregations
- PII handling
- access control
- quality checks for duplicates
- source freshness monitoring
- backfills
- governance

Follow-ups:

1. How do you merge duplicate customers?
2. How do you avoid wrong identity merges?
3. How do you handle email changes?
4. How do you protect PII?
5. How do you explain trust to business users?


## 92. Mock Interview 6: Warehouse Migration

Prompt:

```text
Move legacy warehouse pipelines to a cloud data platform.
```

Expected answer:

- inventory
- dependency mapping
- migration strategy
- raw data migration
- transformation rebuild
- parallel runs
- reconciliation
- dashboard migration
- access/security
- rollback
- cost monitoring
- decommission plan

Follow-ups:

1. Big bang or phased?
2. How do you validate correctness?
3. What are cutover risks?
4. How do you handle historical data?
5. How do you keep business running?


## 93. System Design Anti-Patterns

Avoid:

1. Tool list without requirements.
2. Streaming without latency need.
3. Full refresh for massive data without reason.
4. No raw layer.
5. No idempotency.
6. No backfill.
7. No data quality.
8. No monitoring.
9. No schema evolution plan.
10. No security.
11. No cost awareness.
12. No consumer-specific serving design.
13. No data model.
14. One giant pipeline task.
15. No runbook.
16. Ignoring deletes.
17. Ignoring late data.
18. Ignoring duplicate records.
19. Committing watermark too early.
20. Publishing before validation.


## 94. Strong Candidate Standard

A strong candidate can:

1. Start with requirements.
2. Ask the right clarifying questions.
3. Estimate volume.
4. Choose batch/streaming/CDC based on requirements.
5. Design raw, staging, and curated layers.
6. Define data model and grain.
7. Add quality gates.
8. Add monitoring and alerts.
9. Explain failure recovery.
10. Make writes idempotent.
11. Support backfills and replay.
12. Handle schema evolution.
13. Handle late and duplicate data.
14. Protect PII.
15. Control cost.
16. Explain trade-offs.
17. Summarize clearly.
18. Handle follow-ups calmly.


## 95. Minimum Passing Standard

Candidate must be able to explain:

1. Business goal.
2. Data sources.
3. Data volume.
4. Latency/SLA.
5. Batch vs streaming choice.
6. Ingestion layer.
7. Raw storage.
8. Processing layer.
9. Serving layer.
10. Data model/grain.
11. Orchestration.
12. Data quality checks.
13. Monitoring.
14. Failure handling.
15. Idempotency.
16. Backfills.
17. Security.
18. Cost.
19. Trade-offs.

Missing data quality + idempotency + backfills = not interview-ready.


## 96. Final Exit Test

Candidate must answer this.

### Prompt

```text
Design a data platform for an e-commerce company.

Requirements:
1. Orders come from an OLTP database and can be updated or cancelled.
2. Product catalog arrives as daily vendor files.
3. User clickstream events arrive continuously.
4. Business wants daily sales dashboards by 8 AM.
5. Product team wants near-real-time event analytics within 5 minutes.
6. Finance needs accurate revenue reconciliation.
7. Customer data contains PII.
8. The platform must support backfills for 2 years.
```

Passing answer must include:

- requirements clarification
- separate batch and streaming paths where justified
- CDC or incremental strategy for orders
- file ingestion strategy for product catalog
- streaming/micro-batch strategy for clickstream
- raw storage for replay
- staging and curated layers
- fact/dimension model
- data quality gates
- reconciliation for finance
- orchestration
- monitoring and alerting
- idempotency
- backfills
- schema evolution
- late data handling
- duplicate handling
- PII/security
- cost controls
- trade-offs
- final summary

Fail if candidate:

- only lists tools
- uses streaming for everything without justification
- misses backfills
- misses quality checks
- misses idempotency
- ignores PII
- ignores finance reconciliation
- cannot explain trade-offs


## 97. Final Summary

Data Engineering system design is not about memorizing architecture diagrams.

It is about designing data systems that survive production reality.

The strongest candidates design for:

- requirements
- data volume
- latency
- correctness
- ingestion
- storage
- processing
- modeling
- quality
- monitoring
- failures
- idempotency
- backfills
- security
- cost
- trade-offs

The weakest candidates say:

```text
Use Kafka, Spark, Airflow, and Snowflake.
```

That is not enough.

Data Engineering Sensei should train candidates to design systems that are correct, reliable, explainable, and operable.


## 98. Drill Appendix

### Drill 1: Requirements Drill

```text
Given any design prompt, ask 10 clarifying questions before choosing tools.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 2: Batch vs Streaming Drill

```text
For 10 scenarios, choose batch, micro-batch, streaming, or CDC and justify.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 3: Volume Estimation Drill

```text
Estimate daily storage for 5000 events/sec with 2 KB average event size.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 4: Raw Layer Drill

```text
Explain why raw data is stored and how it helps backfills.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 5: Idempotency Drill

```text
A task fails halfway through target write. Explain safe rerun strategy.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 6: Watermark Drill

```text
Design safe watermark update for incremental load.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 7: Backfill Drill

```text
Backfill 2 years of data without duplicate output or cost spike.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 8: Quality Gate Drill

```text
Define critical and non-critical quality checks for fact_sales.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 9: Monitoring Drill

```text
List system and data metrics for a daily dashboard pipeline.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 10: Alert Drill

```text
Write a useful alert message for a failed sales pipeline.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 11: Schema Evolution Drill

```text
Handle source column rename, type change, and new optional column.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 12: Late Data Drill

```text
Design correction strategy for events arriving 3 days late.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 13: CDC Drill

```text
Handle inserts, updates, deletes, and replay in CDC pipeline.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 14: Security Drill

```text
Add PII masking, access control, and audit logs to Customer 360.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 15: Cost Drill

```text
Reduce cost in a pipeline with full refreshes and expensive scans.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 16: Data Modeling Drill

```text
Define facts, dimensions, and grain for sales analytics.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 17: Failure Drill

```text
Classify source failure, schema failure, quality failure, and write failure.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 18: Runbook Drill

```text
Create a runbook outline for a critical daily pipeline.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 19: Migration Drill

```text
Plan phased migration from legacy warehouse to cloud platform.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.

### Drill 20: Final Mixed Drill

```text
Design e-commerce platform with orders, product files, clickstream, dashboards, and finance reconciliation.
```

Minimum passing standard:

- State assumptions.
- Define architecture impact.
- Include failure handling.
- Include data quality or validation.
- Include backfill/recovery where relevant.
- Explain trade-offs.
