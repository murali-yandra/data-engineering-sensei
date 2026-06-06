# ETL / ELT Pipelines Guide

Generated: 2026-06-06

This guide teaches **ETL and ELT pipeline design for Data Engineering interviews**.

It is written for **Data Engineering Sensei**, a strict, no-sugarcoating Data Engineering interview mentor. The goal is not to memorize “Extract, Transform, Load.” The goal is to make the candidate capable of explaining how real data pipelines are designed, loaded, validated, monitored, retried, backfilled, optimized, and defended in interviews.

Use this guide for:

- Data Engineering fundamentals interviews
- ETL/ELT interview questions
- project deep dives
- Data Engineering system design
- cloud data platform discussions
- SQL and warehouse pipeline discussions
- mock interviews
- weakness repair for pipeline design gaps

---

## 1. What Is a Data Pipeline?

A data pipeline is a controlled process that moves data from one or more sources to one or more destinations.

A pipeline usually includes:

1. Source extraction
2. Data ingestion
3. Raw landing
4. Validation
5. Transformation
6. Loading
7. Quality checks
8. Publishing
9. Monitoring
10. Failure handling
11. Backfill/reprocessing support

A weak candidate says:

```text
A pipeline takes data from source and loads it to target.
```

A strong candidate says:

```text
A data pipeline extracts data from sources, lands it safely, validates and transforms it, loads it into a target like a warehouse or lakehouse, and includes orchestration, data quality checks, monitoring, retry handling, idempotency, and backfill support.
```

---

## 2. Interview Standard

In interviews, the candidate should explain more than the happy path.

A pipeline answer must cover:

```text
Source:
Data format:
Volume:
Frequency:
Latency:
Full or incremental:
Raw landing:
Transformation:
Target:
Load strategy:
Data quality:
Orchestration:
Monitoring:
Failure handling:
Idempotency:
Backfill:
Security:
Cost:
Trade-offs:
```

If the candidate only says:

```text
Extract from source, transform, and load into warehouse.
```

that is not interview-ready.

---

## 3. ETL vs ELT

## 3.1 ETL

ETL means:

```text
Extract → Transform → Load
```

Data is transformed before being loaded into the final target.

### Common flow

```text
Source
  ↓
Extract
  ↓
Transform in processing layer
  ↓
Load cleaned data into target
```

### Good for

- legacy warehouses
- strict preprocessing before target
- sensitive data masking before storage
- smaller controlled datasets
- transformation outside warehouse
- systems where target cannot handle heavy transformations

### Trade-offs

Pros:

- target receives cleaner data
- transformation logic controlled before loading
- useful when target is limited

Cons:

- raw data may not be preserved unless separately stored
- harder replay if raw is discarded
- transformation layer can become bottleneck
- less flexible for ad hoc reprocessing

### Interview-ready answer

```text
In ETL, transformation happens before loading into the final target. It can be useful when the target should only receive cleaned or masked data, or when the warehouse cannot handle transformation efficiently. But if raw data is not retained, debugging and backfills become harder.
```

---

## 3.2 ELT

ELT means:

```text
Extract → Load → Transform
```

Data is loaded first, often into object storage or a warehouse, then transformed later.

### Common flow

```text
Source
  ↓
Extract
  ↓
Load raw data
  ↓
Transform inside warehouse/lakehouse
  ↓
Publish curated data
```

### Good for

- cloud warehouses
- data lakes
- lakehouses
- raw data retention
- auditability
- replayability
- flexible transformations
- scalable SQL-based transformations

### Trade-offs

Pros:

- raw data is preserved
- easier backfills
- easier debugging
- flexible transformation logic
- cloud warehouses can scale transformation compute

Cons:

- raw sensitive data may land before masking
- governance must be stronger
- warehouse cost can increase
- badly managed ELT can create messy raw layers

### Interview-ready answer

```text
ELT is common in modern cloud data platforms because raw data can be loaded cheaply and transformed later using scalable compute. It improves replayability and debugging, but it requires strong governance, access control, and data quality processes.
```

---

## 3.3 ETL vs ELT Comparison

| Area | ETL | ELT |
|---|---|---|
| Transformation timing | Before loading target | After loading raw data |
| Raw data retention | Optional, often separate | Usually easier |
| Cloud warehouse fit | Less common by default | Very common |
| Debugging | Harder if raw not retained | Easier with raw layer |
| Backfills | Harder without raw data | Easier from raw data |
| Security | can mask before loading | must secure raw zone |
| Flexibility | lower | higher |
| Cost risk | processing layer cost | warehouse/query cost |

### Strong answer

```text
I would choose ELT for most cloud warehouse pipelines because it preserves raw data and enables flexible reprocessing. But if sensitive data must be masked before landing, or if the target should not store raw data, ETL may be safer.
```

---

## 4. Pipeline Design Mindset

A strong candidate designs pipelines around failure, not only success.

Every pipeline design should answer:

1. What data is coming?
2. How much data is coming?
3. How often does it arrive?
4. How fresh does it need to be?
5. What happens if source is late?
6. What happens if the job fails halfway?
7. What happens if data is duplicated?
8. What happens if schema changes?
9. How do we validate output?
10. How do we rerun safely?
11. How do we backfill?
12. How do users know data is fresh?

Weak candidates only draw arrows.

Strong candidates explain operations.

---

## 5. Pipeline Architecture Layers

A common pipeline architecture:

```text
Source Systems
  ↓
Ingestion Layer
  ↓
Raw / Landing Layer
  ↓
Staging Layer
  ↓
Transformation Layer
  ↓
Curated / Warehouse Layer
  ↓
Serving / BI / ML Layer
  ↓
Monitoring / Governance
```

### Strong explanation

```text
I separate raw, staging, and curated layers so that ingestion, validation, transformation, and serving responsibilities are clear. Raw data supports replay. Staging standardizes source data. Curated data is trusted and business-ready.
```

---

## 6. Source Systems

Common pipeline sources:

- OLTP databases
- APIs
- flat files
- object storage
- event streams
- message queues
- SaaS tools
- logs
- spreadsheets
- legacy systems
- third-party vendors

### Source questions to ask

```text
What is the source system?
What is the data format?
How often does it update?
Can records be updated or deleted?
Can the source provide incremental changes?
What is the expected volume?
Who owns the source schema?
What happens if the source is unavailable?
```

### Common mistakes

- assuming sources are always available
- ignoring source schema changes
- ignoring source deletes
- ignoring source system load
- not checking source ownership
- no retry or rate limit handling
- no raw source capture

---

## 7. Ingestion Patterns

## 7.1 File-Based Ingestion

Used when data arrives as files.

Examples:

- daily CSV from vendor
- JSON logs
- exported reports
- parquet dumps
- partner data feeds

### Design considerations

- file naming convention
- file arrival detection
- duplicate files
- corrupt files
- missing files
- late files
- schema validation
- checksum if needed
- idempotent loads
- archive strategy

### Strong answer

```text
For file ingestion, I would track file arrival, validate schema, detect duplicate files, quarantine corrupt files, and write raw copies before transformation. The pipeline should be idempotent so reprocessing the same file does not duplicate records.
```

---

## 7.2 Database Extraction

Used when pulling from source databases.

Patterns:

- full extract
- timestamp-based incremental extract
- ID-based incremental extract
- partition-based extract
- CDC

### Design considerations

- source load impact
- isolation level
- consistency
- updated_at reliability
- deleted records
- late updates
- schema changes
- extraction window
- retry safety

### Strong answer

```text
For database extraction, I would avoid full loads for large tables. I would use incremental extraction or CDC, track watermarks, and ensure the extraction does not overload the production database.
```

---

## 7.3 API Ingestion

Used when source is external service or SaaS API.

### Design considerations

- authentication
- pagination
- rate limits
- retries
- timeout handling
- incremental sync
- deleted records
- API version changes
- schema changes
- error responses
- partial responses

### Strong answer

```text
For API ingestion, I would handle pagination, rate limits, retries with backoff, authentication through a secrets manager, and incremental sync using updated timestamps or cursors if the API supports them.
```

---

## 7.4 Streaming Ingestion

Used when events arrive continuously.

Examples:

- clickstream
- user activity
- IoT
- logs
- payments
- fraud signals

### Design considerations

- event schema
- event ID
- partition key
- ordering
- duplicates
- late events
- retention
- replay
- consumer lag
- checkpointing
- exactly-once vs at-least-once semantics

### Strong answer

```text
For streaming ingestion, I would design for duplicates and late events. Events should have stable event IDs and event_time. I would store raw events for replay and make downstream writes idempotent.
```

---

## 8. Batch Pipelines

Batch pipelines process data at scheduled intervals.

Examples:

- hourly load
- daily warehouse refresh
- weekly report pipeline
- monthly finance close

### When batch is appropriate

- daily/hourly latency is enough
- source data arrives periodically
- cost matters
- operational simplicity matters
- exact real-time updates are not required

### Strong answer

```text
If the business needs daily reporting, batch is usually simpler, cheaper, and easier to operate than streaming. I would design batch jobs with partition-based processing, quality checks, retries, and backfill support.
```

### Common mistakes

- using streaming when batch is enough
- no freshness monitoring
- no backfill
- no idempotency
- full refresh on huge tables
- no late data handling

---

## 9. Streaming Pipelines

Streaming pipelines process events continuously or near-real-time.

### When streaming is appropriate

- low latency is required
- events are continuous
- dashboards need minute-level freshness
- alerts must trigger quickly
- fraud/risk systems need near-real-time
- user behavior must update quickly

### Costs of streaming

Streaming adds complexity:

- duplicates
- late events
- out-of-order events
- checkpointing
- state management
- replay
- lag monitoring
- schema evolution
- operational cost

### Strong answer

```text
I would choose streaming only when latency requirements justify the complexity. If the business can tolerate hourly or daily updates, batch is usually better.
```

---

## 10. Full Load

Full load means processing the entire dataset every run.

### Good for

- small reference tables
- small dimensions
- simple early-stage systems
- source does not support incremental extraction
- periodic complete snapshots

### Bad for

- large fact tables
- high-volume events
- production databases
- cost-sensitive workloads
- time-sensitive SLAs

### Strong answer

```text
Full load is simple but does not scale well. I would use it for small reference tables, but for large transactional tables I would prefer incremental load or CDC.
```

---

## 11. Incremental Load

Incremental load processes only new or changed data.

### Common strategies

- updated_at watermark
- created_at for append-only tables
- increasing ID
- CDC log
- partition-based extraction
- API cursor
- file manifest
- event offset

### Strong answer

```text
Incremental loading reduces processing time and source load. But it requires reliable watermark tracking, idempotent writes, and logic for late-arriving updates and deletes.
```

### Common mistakes

- assuming updated_at is always reliable
- ignoring deletes
- no lookback window
- no retry-safe watermark update
- missing late records
- no deduplication

---

## 12. Watermarks

A watermark records the last successfully processed point.

Examples:

- max updated_at
- max ID
- last processed file name
- API cursor
- Kafka offset
- partition date

### Strong answer

```text
A watermark should be updated only after successful processing. If it is updated too early and the load fails, data can be skipped permanently.
```

### Safe watermark pattern

```text
1. Read current watermark.
2. Extract data greater than watermark.
3. Land raw data.
4. Validate.
5. Load target.
6. Commit new watermark only after success.
```

### Common mistakes

- update watermark before load finishes
- no transaction-like behavior
- no handling duplicate timestamps
- no overlap/lookback
- no manual correction process

---

## 13. Lookback Windows

A lookback window reprocesses a recent time range to catch late updates.

Example:

```text
Every daily run processes last 3 days instead of only yesterday.
```

### Good for

- late-arriving updates
- delayed files
- source corrections
- mobile offline events
- eventual consistency

### Trade-offs

- more processing
- potential duplicates if not idempotent
- higher cost

### Strong answer

```text
If late data is common, I may use a rolling lookback window and overwrite or merge affected partitions. This catches late updates while keeping processing bounded.
```

---

## 14. Change Data Capture

CDC captures inserts, updates, and deletes from a source database.

### Why CDC matters

CDC is useful when:

- source tables are large
- near-real-time sync is needed
- updates/deletes matter
- full extraction is too expensive
- downstream must reflect source changes

### CDC events may include

- operation type
- before values
- after values
- timestamp
- log sequence number
- table name
- transaction ID

### Strong answer

```text
CDC captures row-level changes such as inserts, updates, and deletes. It is efficient for syncing source databases to a warehouse, but the pipeline must handle ordering, duplicates, deletes, schema changes, replay, and idempotent merges.
```

### Common mistakes

- ignoring deletes
- ignoring operation order
- no offset tracking
- no replay strategy
- no schema change handling
- assuming CDC means no data quality checks

---

## 15. Pipeline Idempotency

Idempotency means rerunning the same task produces the same final result.

### Why it matters

Pipelines fail and retry. Without idempotency, reruns can duplicate data or corrupt output.

### Idempotency strategies

1. Delete and reload partition.
2. Merge/upsert by stable key.
3. Write to staging then swap.
4. Use deterministic output paths.
5. Deduplicate by natural key.
6. Use transaction-safe writes if supported.
7. Track processed files/events.
8. Use idempotent API calls when writing externally.

### Strong answer

```text
A pipeline should be idempotent because retries and backfills are normal. For a daily fact table, I can overwrite the affected date partition or merge records by business key so rerunning the job does not duplicate data.
```

### Weak answer

```text
Idempotency means no duplicates.
```

Too shallow.

---

## 16. Backfills

A backfill reprocesses historical data.

### Reasons for backfill

- transformation bug
- new business logic
- late data
- source correction
- missing partitions
- new metric
- model redesign
- warehouse migration

### Backfill requirements

- raw data retention
- parameterized date range
- idempotent writes
- validation
- dependency awareness
- downstream refresh
- communication to consumers
- cost planning

### Strong answer

```text
A backfill should be controlled and safe. I would identify affected partitions, rerun from raw or staging data, overwrite or merge deterministically, validate the output, refresh downstream marts, and communicate impact.
```

### Common mistakes

- pipeline only works for current day
- no raw data to replay
- no date parameterization
- no validation after backfill
- duplicating historical data
- forgetting downstream tables

---

## 17. Reprocessing

Reprocessing means rerunning logic over data.

Backfill is one type of reprocessing.

Other examples:

- reprocess failed file
- reprocess one customer partition
- rerun affected event window
- rebuild one table
- replay event stream from offset

### Strong answer

```text
Reprocessing should be deterministic, traceable, and scoped. I would avoid blind full reruns if only specific partitions are affected.
```

---

## 18. Data Quality in ETL/ELT

A pipeline is not successful just because it ran.

Data quality must be checked.

### Common quality checks

- schema validation
- row count checks
- null checks
- uniqueness checks
- duplicate checks
- referential integrity
- accepted values
- range checks
- freshness checks
- anomaly checks
- reconciliation checks
- business rule checks

### Strong answer

```text
I would add quality checks before publishing curated data. A job can succeed technically but still produce wrong business numbers.
```

---

## 19. Quality Checks by Layer

| Layer | Example Checks |
|---|---|
| Raw | file exists, schema, corrupt records |
| Staging | type casting, required fields, deduplication |
| Cleaned | accepted values, referential checks |
| Curated | business rules, metric reconciliation |
| Serving | freshness, dashboard totals, SLA checks |

### Strong answer

```text
Quality checks should exist at multiple points. Raw checks catch ingestion problems, staging checks catch record-level issues, and curated checks protect business metrics.
```

---

## 20. Data Validation Failures

When validation fails, possible actions:

1. Fail the pipeline.
2. Quarantine bad records.
3. Warn but continue.
4. Route to manual review.
5. Use default values.
6. Reject the file.
7. Roll back publish step.

### Choosing action

Critical checks should fail the pipeline.

Examples:

- missing primary key
- missing required file
- schema breaking change
- duplicate transaction ID in curated fact
- revenue mismatch beyond threshold

Non-critical checks may warn.

Examples:

- optional field missing
- small anomaly within tolerance
- new accepted value needing review

### Strong answer

```text
Not every quality failure should be handled the same. Critical failures should block publishing, while non-critical issues may be logged and monitored depending on business impact.
```

---

## 21. Schema Evolution

Schema evolution means source schema changes over time.

Examples:

- new column added
- column removed
- column renamed
- type changed
- nested field added
- enum values changed

### Handling strategy

1. Detect schema.
2. Compare with expected schema.
3. Classify change as compatible or breaking.
4. Alert owners if breaking.
5. Quarantine or stop publish if needed.
6. Update transformations intentionally.
7. Version schema if needed.

### Strong answer

```text
I would detect schema changes and separate compatible changes from breaking changes. Adding a nullable column may be acceptable, but changing a field type or removing a required column should alert and stop the pipeline from publishing bad data.
```

---

## 22. Late-Arriving Data

Late-arriving data arrives after expected processing time.

Examples:

- delayed mobile events
- API sync delay
- late vendor file
- CDC lag
- delayed transactions

### Handling strategies

- process by event time
- use lookback window
- update affected partitions
- maintain ingestion_time and event_time
- run backfill
- monitor late arrival rate

### Strong answer

```text
I would separate event_time from ingestion_time. Late records should update the correct business date partition when required, not automatically be counted as today's activity.
```

---

## 23. Duplicate Data

Duplicates happen because of:

- source retries
- file resends
- API pagination bugs
- CDC replay
- stream reprocessing
- pipeline retries
- join multiplication
- lack of natural key

### Handling strategies

- stable event_id
- natural business key
- source file manifest
- processed-file tracking
- row hash
- ROW_NUMBER dedupe
- merge/upsert
- idempotent partition overwrite

### Strong answer

```text
Duplicate handling starts with defining the expected grain and key. I would deduplicate in staging using deterministic rules and validate uniqueness before publishing.
```

---

## 24. Deletes and Updates

Pipelines must handle source changes.

### Insert-only data

Examples:

- immutable logs
- events
- append-only transactions

Simple append may work.

### Mutable data

Examples:

- customer profile
- order status
- subscription plan
- product catalog

Requires:

- merge/upsert
- CDC
- SCD strategy
- current-state table
- history table

### Deletes

Delete handling options:

- hard delete downstream
- soft delete flag
- tombstone records
- CDC delete events
- effective end dating

### Strong answer

```text
If source records can update or delete, append-only loading is not enough. I need merge logic, CDC, soft delete handling, or history tracking depending on reporting requirements.
```

---

## 25. Pipeline Orchestration

Orchestration manages tasks and dependencies.

Core concepts:

- DAG
- tasks
- dependencies
- schedule
- retries
- sensors
- backfills
- parameters
- alerts
- SLAs

### Strong answer

```text
I would use orchestration to run pipeline tasks in dependency order, retry transient failures, alert on persistent failures, and support backfills through parameterized date ranges.
```

### Common mistakes

- no dependency management
- no retry strategy
- no alerting
- non-idempotent tasks
- no backfill support
- hardcoded dates

---

## 26. Pipeline Monitoring

Monitor both pipeline health and data health.

### Pipeline health metrics

- job success/failure
- runtime
- retries
- task duration
- resource usage
- dependency failures
- queue delay

### Data health metrics

- row counts
- freshness
- null rate
- duplicate rate
- schema changes
- late-arriving records
- metric anomalies

### Strong answer

```text
Pipeline monitoring should include job health and data health. A job may complete successfully but produce stale or incorrect data.
```

---

## 27. Alerts and SLAs

Alerts should be tied to impact.

Examples:

- daily sales table not refreshed by 8 AM
- stream lag over 10 minutes
- row count drops by 80%
- duplicate transaction IDs detected
- required file missing
- schema changed unexpectedly
- revenue reconciliation fails

### Strong answer

```text
I would define freshness and quality SLAs based on business consumption. Alerts should fire when data is late, wrong, or pipeline failures threaten downstream users.
```

---

## 28. Error Handling and Retry

Errors can be transient or permanent.

### Transient errors

Examples:

- network timeout
- temporary API failure
- temporary warehouse issue
- rate limit

Action:

- retry with backoff
- log failure
- alert after threshold

### Permanent errors

Examples:

- schema mismatch
- invalid data
- missing required columns
- permission issue
- code bug

Action:

- fail fast
- alert owner
- quarantine bad data if relevant
- do not keep retrying blindly

### Strong answer

```text
Retries should be used for transient failures, not for permanent data quality or schema errors. Retrying bad data repeatedly only delays the real fix.
```

---

## 29. Staging Tables

Staging tables hold intermediate data.

### Uses

- raw-to-clean transformations
- deduplication
- validation
- type casting
- merge preparation
- auditability
- rollback safety

### Strong answer

```text
I would load data into staging first, validate and deduplicate it, then merge into the final target. This reduces the chance of corrupting curated tables.
```

---

## 30. Audit Columns

Useful audit columns:

- ingestion_time
- source_system
- source_file_name
- batch_id
- run_id
- created_at
- updated_at
- record_hash
- is_deleted
- effective_start
- effective_end

### Strong answer

```text
Audit columns help trace where a record came from, when it was loaded, and which pipeline run created it. This is useful for debugging and lineage.
```

---

## 31. Pipeline Metadata

Metadata tables can track:

- pipeline runs
- processed files
- watermarks
- row counts
- quality check results
- source-to-target mapping
- backfill history
- failure logs

### Strong answer

```text
I would maintain metadata for pipeline runs, watermarks, processed files, and quality results so failures and backfills are traceable.
```

---

## 32. File Format Choices

### CSV

Good for:

- simple exchange
- vendor files
- human-readable data

Weakness:

- no strong schema
- parsing issues
- inefficient analytics

### JSON

Good for:

- APIs
- nested data
- event payloads

Weakness:

- schema drift
- parsing overhead
- inconsistent fields

### Parquet

Good for:

- analytics
- columnar reads
- compression
- large-scale processing

Weakness:

- not human-readable
- small files issue

### Avro

Good for:

- schema-based event data
- streaming
- schema evolution

### Strong answer

```text
I may ingest CSV or JSON because sources provide them, but for large analytical processing I would usually store curated data in Parquet because it is columnar and compressed.
```

---

## 33. Partitioning Pipelines

Partitioning helps process and query data efficiently.

Common partition columns:

- event_date
- ingestion_date
- transaction_date
- source
- region

### Strong answer

```text
For large fact data, I would partition by business date or event date if queries filter by that date. For raw landing, ingestion date may also be useful for operational tracking.
```

### Common mistakes

- high-cardinality partitions
- too many small files
- wrong date column
- no late data strategy
- no partition overwrite strategy

---

## 34. Small Files Problem

Small files occur when pipelines write too many tiny files.

### Why it hurts

- slower reads
- metadata overhead
- inefficient Spark jobs
- query planning overhead
- storage listing cost

### Causes

- over-partitioning
- streaming micro-batches
- too many small tasks
- frequent tiny loads
- no compaction

### Fixes

- compaction jobs
- tune output partitions
- batch small files
- avoid excessive partition columns
- write larger files
- optimize table layout

### Strong answer

```text
If a pipeline writes too many small files, downstream queries and Spark jobs slow down. I would reduce partition cardinality, control output file sizes, and run compaction where appropriate.
```

---

## 35. ETL/ELT and SQL Transformations

In ELT, many transformations happen in SQL.

Common SQL transformations:

- type casting
- deduplication
- joins
- aggregations
- SCD merge logic
- fact/dimension loading
- data quality checks
- snapshot creation
- incremental merges

### Strong answer

```text
For warehouse ELT, SQL transformations should be modular, tested, and understandable. I would use staging models, intermediate models, and final marts rather than one huge query.
```

---

## 36. ETL/ELT and Python Transformations

Python is useful for:

- API ingestion
- file parsing
- JSON normalization
- custom business logic
- orchestration helpers
- validation scripts
- small/medium transformations
- data quality checks

### Strong answer

```text
I would use Python when transformation requires procedural logic, API handling, JSON parsing, or custom validation. For large warehouse transformations, SQL or distributed processing may be more appropriate.
```

---

## 37. ETL/ELT and Spark Transformations

Spark is useful for:

- large-scale batch processing
- distributed joins
- heavy transformations
- big file processing
- large event logs
- parquet processing
- large aggregations outside warehouse

### Strong answer

```text
I would choose Spark when the data volume or transformation complexity requires distributed processing. But for simple warehouse transformations, warehouse SQL may be simpler and cheaper.
```

---

## 38. Pipeline Testing

Testing should include:

- unit tests for transformation logic
- schema tests
- uniqueness tests
- null checks
- accepted value checks
- row count tests
- reconciliation tests
- integration tests
- sample data tests
- backfill tests

### Strong answer

```text
I would test both code logic and data assumptions. For example, a transaction fact should have unique transaction IDs, non-null required fields, and revenue totals reconciled against source control totals.
```

---

## 39. Pipeline Deployment

Pipeline changes should be controlled.

Good practices:

- version control
- code review
- environment separation
- automated tests
- deployment approvals
- rollback plan
- monitoring after deployment
- documentation update

### Strong answer

```text
I would deploy pipeline changes through version control and testing environments. For risky transformations, I would compare old and new outputs before switching production consumers.
```

---

## 40. Security in Pipelines

Security considerations:

- secrets management
- least privilege
- service accounts
- encryption
- PII masking
- access control
- audit logs
- secure transfer
- environment separation

### Strong answer

```text
I would not hardcode credentials in pipeline code. Secrets should be stored in a secrets manager, service accounts should follow least privilege, and sensitive data should be masked or restricted.
```

---

## 41. Pipeline Cost Awareness

Cost drivers:

- full refreshes
- large scans
- always-on clusters
- inefficient queries
- too much streaming
- no partitioning
- no incremental processing
- repeated transformations
- small files
- duplicated storage

### Cost controls

- incremental loads
- partition pruning
- columnar formats
- right-sized compute
- auto-shutdown
- materialize repeated logic
- monitor expensive jobs
- lifecycle policies
- batch where streaming is unnecessary

### Strong answer

```text
I would control pipeline cost by avoiding unnecessary full refreshes, processing incrementally, partitioning large datasets, using columnar formats, and monitoring expensive jobs or queries.
```

---

## 42. Pipeline Documentation

Document:

```text
Pipeline purpose:
Owner:
Source systems:
Target tables:
Schedule:
SLA:
Watermark:
Load type:
Data quality checks:
Failure handling:
Backfill command/process:
Dependencies:
Security notes:
Known limitations:
```

### Strong answer

```text
Pipeline documentation helps operations. If a pipeline fails, the owner, SLA, dependencies, and backfill process should be clear.
```

---

## 43. Common ETL/ELT Interview Questions

### Basic

1. What is ETL?
2. What is ELT?
3. ETL vs ELT?
4. What is a data pipeline?
5. What is batch processing?
6. What is streaming?
7. What is incremental load?
8. What is a watermark?
9. What is idempotency?
10. What is a backfill?

### Medium

1. How do you design a daily batch pipeline?
2. How do you make a pipeline idempotent?
3. How do you handle duplicate files?
4. How do you handle schema evolution?
5. How do you handle late-arriving data?
6. How do you validate data before loading warehouse?
7. How do you choose between full load and incremental load?
8. How do you handle API rate limits?
9. How do you monitor pipeline freshness?
10. How do you recover from failed loads?

### Advanced

1. Design a CDC pipeline from OLTP to warehouse.
2. Design an event pipeline with late and duplicate events.
3. Design a backfill strategy after a transformation bug.
4. Design a data quality framework inside pipelines.
5. Design an ELT architecture for cloud warehouse.
6. Design a pipeline migration from legacy ETL to cloud ELT.
7. Explain how to handle schema evolution across many sources.
8. Explain exactly-once vs at-least-once in pipeline context.
9. Design pipeline SLAs and alerting.
10. Design pipeline cost controls.

---

## 44. Scenario: Daily Batch ETL Pipeline

### Prompt

```text
Design a daily pipeline that loads orders from an OLTP database into a cloud data warehouse.
```

### Strong answer outline

1. Clarify reporting SLA.
2. Identify source tables.
3. Use incremental extraction by updated_at or CDC.
4. Land raw extract.
5. Validate schema and row counts.
6. Load staging tables.
7. Deduplicate by order_id and updated_at.
8. Transform into fact_order or fact_order_line.
9. Run quality checks.
10. Publish curated warehouse table.
11. Monitor freshness and failures.
12. Support backfills by date range.
13. Make load idempotent using merge or partition overwrite.
14. Secure credentials and PII.

### Weak answer

```text
Extract orders, transform, and load to warehouse.
```

This is too shallow.

---

## 45. Scenario: API ELT Pipeline

### Prompt

```text
Design a pipeline that ingests customer data from a third-party API every hour.
```

### Strong answer outline

1. Clarify API limits and data volume.
2. Use secure credentials.
3. Handle pagination.
4. Use cursor or updated_at for incremental sync.
5. Retry transient failures with backoff.
6. Store raw API responses.
7. Validate schema.
8. Normalize JSON into staging.
9. Merge into customer dimension.
10. Track API cursor/watermark.
11. Monitor freshness and error rates.
12. Handle deleted or deactivated customers.

### Follow-ups

1. What if the API rate limits you?
2. What if page 5 fails?
3. What if schema changes?
4. What if records are deleted?
5. How do you avoid duplicates?

---

## 46. Scenario: Streaming Event Pipeline

### Prompt

```text
Design a pipeline for near-real-time user activity events.
```

### Strong answer outline

1. Clarify latency requirement.
2. Define event schema and event_id.
3. Ingest through event stream.
4. Store raw events for replay.
5. Validate schema.
6. Deduplicate by event_id.
7. Handle late events with event_time.
8. Process events into curated table.
9. Monitor lag and error rates.
10. Alert on schema or volume anomalies.
11. Support replay from raw/events.
12. Secure PII fields.

---

## 47. Scenario: CDC ELT Pipeline

### Prompt

```text
Design a CDC pipeline from a transactional database to a warehouse.
```

### Strong answer outline

1. Capture inserts, updates, deletes.
2. Store raw change events.
3. Track offsets or log sequence.
4. Apply changes in order.
5. Use staging change tables.
6. Merge into warehouse target.
7. Handle deletes with soft delete or tombstones.
8. Validate row counts and key uniqueness.
9. Monitor CDC lag.
10. Handle schema changes.
11. Support replay from offsets.
12. Make merge idempotent.

---

## 48. Scenario: Backfill After Bad Transformation

### Prompt

```text
A bug caused wrong revenue for the last 90 days. How do you fix it?
```

### Strong answer

```text
I would first identify affected tables and date partitions, stop or flag affected dashboards if needed, fix the transformation logic, reprocess the affected date range from raw or staging data, overwrite or merge affected partitions idempotently, validate revenue against source totals, refresh downstream marts, and communicate the correction.
```

### Weak answer

```text
Rerun the pipeline.
```

Too shallow.

---

## 49. Weak vs Strong Answers

### Question: What is ETL?

Weak:

```text
ETL is extract, transform, load.
```

Strong:

```text
ETL extracts data from sources, transforms it before final loading, and then loads it into a target. It is useful when data must be cleaned or masked before landing in the target. A good ETL pipeline also includes validation, orchestration, retries, monitoring, idempotency, and backfill support.
```

---

### Question: What is ELT?

Weak:

```text
ELT is extract, load, transform.
```

Strong:

```text
ELT loads raw data first, usually into a warehouse or lake, and transforms it later. It is common in cloud data platforms because storage is cheap and warehouse compute can scale. The trade-off is that raw data must be governed and secured properly.
```

---

### Question: How do you make a pipeline idempotent?

Weak:

```text
Remove duplicates.
```

Strong:

```text
I make a pipeline idempotent by ensuring reruns produce the same final result. For example, I can overwrite a date partition, merge by stable business key, track processed files, or stage and swap output only after validation.
```

---

### Question: How do you handle late-arriving data?

Weak:

```text
Load it later.
```

Strong:

```text
I would process late-arriving records based on event time, update affected partitions or aggregates, use a lookback window if needed, and make the pipeline idempotent so reprocessing does not duplicate data.
```

---

## 50. Common Interview Red Flags

Flag these strongly:

1. Candidate only expands ETL acronym.
2. No source analysis.
3. No data volume discussion.
4. No latency discussion.
5. No full vs incremental decision.
6. No watermark.
7. No idempotency.
8. No retry strategy.
9. No backfill strategy.
10. No data quality checks.
11. No monitoring.
12. No duplicate handling.
13. No schema evolution handling.
14. No security for credentials/PII.
15. No cost awareness.
16. Says streaming is always better.
17. Uses full load for huge tables without justification.
18. Updates watermark before successful load.
19. Cannot explain CDC deletes.
20. Cannot explain how reruns avoid duplicate data.

---

## 51. Review Checklist

When reviewing a candidate pipeline answer, check:

```text
Business goal clarified:
Source systems identified:
Data format explained:
Data volume estimated:
Latency requirement discussed:
Batch/streaming choice justified:
Full/incremental choice justified:
Watermark or offset explained:
Raw landing included:
Staging included:
Transformation logic explained:
Load strategy explained:
Idempotency included:
Data quality checks included:
Error handling included:
Retry strategy included:
Monitoring included:
SLA/freshness included:
Backfill/reprocessing included:
Schema evolution included:
Duplicate handling included:
Security included:
Cost trade-offs included:
Answer structured clearly:
```

If idempotency, data quality, monitoring, and backfills are missing, the answer is not interview-ready.

---

## 52. Scoring Rubric

### Score 0

No usable understanding.

Cannot explain:

- ETL
- ELT
- pipeline flow
- basic source-to-target movement

### Score 1

Knows acronyms but not practical pipeline design.

Weak in:

- failure handling
- data quality
- incremental loads
- monitoring

### Score 2

Can explain simple pipeline but misses operations.

Can describe:

- source
- transform
- target

Weak in:

- idempotency
- backfills
- schema evolution
- late data
- duplicates

### Score 3

Can design standard batch pipeline.

Includes:

- source
- load strategy
- transformations
- target
- basic checks

Needs improvement:

- failure recovery
- cost
- advanced incremental logic
- CDC
- streaming

### Score 4

Interview-ready.

Can explain:

- ETL vs ELT
- batch vs streaming
- full vs incremental
- watermarks
- CDC
- idempotency
- retries
- backfills
- data quality
- monitoring
- schema evolution
- security
- cost

### Score 5

Strong.

Can handle:

- ambiguous requirements
- complex CDC
- late events
- replay
- multi-source pipelines
- migration
- cost optimization
- operational incidents
- senior-level trade-offs

---

## 53. Minimum Passing Standard

Candidate must explain:

1. ETL vs ELT.
2. Batch vs streaming.
3. Full load vs incremental load.
4. Watermarks.
5. CDC basics.
6. Idempotency.
7. Retry strategy.
8. Backfills.
9. Data quality checks.
10. Monitoring/freshness.
11. Duplicate handling.
12. Schema evolution.
13. Late-arriving data.
14. Security basics.
15. Cost basics.

---

## 54. Strong Candidate Standard

A strong candidate can also explain:

1. CDC ordering and deletes.
2. Streaming replay and late events.
3. Schema contracts.
4. Data quality framework design.
5. Pipeline metadata tables.
6. Backfill dependency management.
7. Exactly-once vs at-least-once implications.
8. Multi-source ingestion.
9. Pipeline migration from legacy ETL to ELT.
10. Operational incident handling.
11. Cost/performance tuning.
12. SLA design and alerting.

---

## 55. 7-Day ETL/ELT Repair Plan

### Day 1: ETL vs ELT and pipeline layers

Drill:

```text
Explain ETL vs ELT using a cloud warehouse example.
```

### Day 2: Full vs incremental load

Drill:

```text
Design incremental order loading using updated_at watermark.
```

### Day 3: Idempotency and retries

Drill:

```text
Explain how rerunning a failed daily load avoids duplicates.
```

### Day 4: Data quality and validation

Drill:

```text
Design quality checks for a transaction fact pipeline.
```

### Day 5: Backfills and reprocessing

Drill:

```text
Fix a 30-day transformation bug and rebuild affected data.
```

### Day 6: CDC and late data

Drill:

```text
Design CDC merge into warehouse and handle deletes.
```

### Day 7: Mock pipeline design

Prompt:

```text
Design an end-to-end pipeline from OLTP orders to warehouse dashboards.
```

---

## 56. 10-Minute Mock Interview

### Prompt

```text
Design an ELT pipeline for an e-commerce company. Data comes from orders, order_items, customers, products, and payments. The business needs daily sales dashboards by 8 AM with accurate revenue and customer segmentation.
```

### Candidate should clarify

1. What is the data volume?
2. What is the SLA?
3. Are updates/deletes possible?
4. How are returns handled?
5. Does customer segmentation need history?
6. What are the source systems?
7. What quality checks are required?

### Expected answer

Should include:

- source extraction
- incremental load or CDC
- raw landing
- staging
- transformation
- fact/dimension model
- warehouse load
- SCD if needed
- data quality checks
- orchestration
- monitoring
- idempotent reruns
- backfill by date
- security
- cost controls

### Follow-ups

1. What if the pipeline fails after staging but before final load?
2. What if source sends duplicate records?
3. What if customer segment changes?
4. How do you validate revenue?
5. How do you backfill last month?
6. How do you avoid full reload every day?
7. How do you know dashboard data is fresh?
8. How do you handle late-arriving orders?

---

## 57. Answer Template

Use this for ETL/ELT interview answers.

```text
I will first clarify the requirements.

Business goal:
[what the pipeline supports]

Sources:
[systems and tables/files/APIs]

Data characteristics:
Volume:
Format:
Frequency:
Latency/SLA:

Pipeline approach:
[ETL or ELT and why]

Ingestion:
[batch/API/CDC/stream/file]

Raw landing:
[where and why]

Staging:
[standardization/deduplication/validation]

Transformation:
[logic, modeling, business rules]

Load strategy:
[full/incremental/merge/partition overwrite]

Data quality:
[checks]

Idempotency:
[how reruns are safe]

Failure handling:
[retries, alerts, quarantine]

Monitoring:
[job health, data freshness, quality]

Backfill:
[how historical data is rebuilt]

Security:
[credentials, PII, access]

Cost:
[incremental, partitioning, compute]

Trade-offs:
[why this design]

Summary:
[final concise design]
```

---

## 58. Mentor Behavior Rules

When using this guide, the mentor should:

1. Never accept acronym-only answers.
2. Ask whether the pipeline is batch or streaming.
3. Ask whether loading is full or incremental.
4. Force the candidate to explain watermarks.
5. Ask how reruns avoid duplicates.
6. Ask how failures are retried.
7. Ask how bad data is blocked.
8. Ask how backfills work.
9. Ask how freshness is monitored.
10. Ask how schema changes are handled.
11. Ask how cost is controlled.
12. Ask how credentials and PII are protected.
13. Score strictly.
14. Give repair drills for missing parts.

Strict correction:

```text
This pipeline answer is not interview-ready. You described the happy path only. Add idempotency, data quality, monitoring, retries, and backfill strategy.
```

---

## 59. Exit Test

Candidate must answer:

```text
Design a reliable ELT pipeline that ingests orders from an OLTP database and customer events from an event stream into a cloud warehouse. The system must support daily dashboards, late-arriving data, retries, duplicates, schema changes, and backfills.
```

Passing answer must include:

- source analysis
- batch + streaming decision
- raw landing
- staging
- transformation
- incremental load or CDC
- event deduplication
- watermarks/offsets
- idempotency
- data quality checks
- monitoring/freshness
- retry strategy
- schema evolution
- backfill/replay
- warehouse serving
- security
- cost trade-offs

If idempotency and backfill are missing, the answer fails.

---

## 60. Final Summary

ETL and ELT interviews are not about expanding acronyms.

They test whether the candidate can design reliable data movement.

The strongest candidates explain:

- source characteristics
- batch vs streaming choice
- ETL vs ELT choice
- full vs incremental strategy
- watermarks and CDC
- idempotency
- retries and failure handling
- data quality
- monitoring and freshness
- backfills and replay
- security and cost trade-offs

The weakest candidates describe only the happy path.

Data pipelines fail in real life. Interview-ready candidates design for that from the beginning.
