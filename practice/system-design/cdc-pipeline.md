# CDC Pipeline System Design Guide

Generated: 2026-06-06

This guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/system-design/cdc-pipeline.md
```

This guide trains the mentor and candidate on **Change Data Capture pipeline system design** for Data Engineering interviews.

The guide is interview-focused. It teaches how to design CDC pipelines that replicate mutable source systems into warehouses, lakes, marts, and history tables with correctness, ordering, delete handling, idempotency, observability, and recovery.

CDC pipeline design is high-ROI because Data Engineering interviews often ask:

```text
Design a CDC pipeline from OLTP database to warehouse.
Design a pipeline that captures inserts, updates, and deletes.
Design a near-real-time or micro-batch replication system.
Design a current-state table from CDC events.
Design a history table from CDC events.
Design a CDC pipeline that supports backfills and replay.
Design CDC into a data lake.
Design CDC into Snowflake/BigQuery/Redshift.
Design a pipeline that handles out-of-order events.
Design a pipeline that handles duplicate CDC events.
Design a pipeline that handles schema evolution.
Design a pipeline that handles deletes and tombstones.
Design an exactly-once-like CDC sink.
Design a CDC pipeline with data quality and reconciliation.
Design CDC for customer, orders, payments, or inventory data.
Explain Debezium/Kafka/log-based CDC concepts.
Explain source offset, LSN, binlog position, WAL position, SCN, and checkpointing.
Explain snapshot + CDC catch-up.
Explain full refresh vs incremental timestamp vs CDC.
```

Use this with:

```text
docs/system-design-guide.md
docs/data-engineering-fundamentals.md
docs/etl-elt-pipelines-guide.md
docs/data-warehouse-guide.md
docs/cloud-data-platforms-guide.md
docs/orchestration-airflow-guide.md
docs/spark-pyspark-guide.md
docs/sql-interview-guide.md
docs/assessment-rubric.md
docs/communication-rubric.md
modes/system-design-mode.md
modes/interview-mode.md
modes/feedback-mode.md
modes/weakness-repair-mode.md
practice/system-design/batch-pipeline.md
practice/sql/deduplication.md
practice/sql/joins.md
practice/sql/query-optimization.md
practice/sql/window-functions.md
progress/CANDIDATE_PROFILE.md
progress/CURRENT_STATE.md
progress/ROADMAP_PROGRESS.md
progress/NEXT_STEPS.md
```

Default interview target:

```text
FAANG-style Data Engineering interview standard, adjusted by candidate experience.
```


## 1. Purpose

The purpose of this guide is to make the candidate strong at CDC pipeline system design interviews.

The candidate should learn to answer:

```text
What is Change Data Capture?
Why use CDC instead of batch timestamp extraction?
What source systems support CDC?
What database log is used?
How are inserts, updates, and deletes represented?
How do we preserve event ordering?
How do we track offsets/checkpoints?
How do we perform initial snapshot plus CDC catch-up?
How do we handle duplicate events?
How do we handle out-of-order events?
How do we handle late-arriving CDC records?
How do we build current-state tables?
How do we build history/SCD Type 2 tables?
How do we handle deletes and tombstones?
How do we merge CDC into warehouse tables?
How do we design exactly-once-like output?
How do we handle schema evolution?
How do we replay CDC events?
How do we backfill historical data?
How do we monitor CDC lag?
How do we validate source and target reconciliation?
How do we scale CDC for high-volume tables?
```

A candidate is interview-ready only when they can design:

```text
source database log capture
initial snapshot
stream or micro-batch CDC transport
raw CDC landing
offset/checkpoint tracking
staging normalization
deduplication
ordering
delete handling
current table merge
history table construction
data quality validation
source-target reconciliation
monitoring and lag alerts
schema evolution handling
replay/backfill strategy
failure recovery
cost and scale trade-offs
```


## 2. What Interviewers Are Testing

CDC system design tests whether the candidate understands mutable data and production correctness.

Interviewers evaluate:

```text
does the candidate know why updated_at extraction can miss deletes?
does the candidate understand source logs?
does the candidate preserve operation type?
does the candidate track source ordering?
does the candidate handle initial snapshot plus ongoing changes?
does the candidate design idempotent sinks?
does the candidate handle duplicate delivery?
does the candidate handle out-of-order records?
does the candidate handle delete/tombstone semantics?
does the candidate build current and history outputs correctly?
does the candidate monitor lag and failures?
does the candidate reconcile source and target?
does the candidate explain trade-offs between CDC, incremental, and full refresh?
```

Weak answer:

```text
Use Kafka and load to warehouse.
```

Strong answer:

```text
I would take an initial consistent snapshot, start log-based CDC from the snapshot position, land raw change events immutably with source LSN/binlog position and operation type, normalize them in staging, deduplicate by primary key and source sequence for current-state tables, apply inserts/updates/deletes using idempotent MERGE, build optional SCD history by applying changes in order, track offsets only after successful sink validation, and monitor CDC lag, duplicate keys, schema changes, and source-target reconciliation.
```

Interview line:

```text
CDC is not just streaming rows; it is preserving source database change semantics correctly.
```


## 3. CDC Mental Model

CDC captures changes from a source system and applies them downstream.

Basic flow:

```text
Source database
    ↓
Transaction log / binlog / WAL / redo log
    ↓
CDC connector
    ↓
Message bus or raw storage
    ↓
CDC raw landing
    ↓
Staging normalization
    ↓
Current-state merge / history construction
    ↓
Warehouse tables / lake tables / marts
```

Every CDC record should answer:

```text
what table changed?
what key changed?
what operation happened?
when did source commit it?
what is the source ordering position?
what were the before values?
what are the after values?
when was it captured?
which connector/batch produced it?
```

Core interview line:

```text
A CDC pipeline must preserve operation type, ordering, and checkpoint position so downstream tables can be reconstructed correctly.
```


## 4. CDC Vocabulary

Important CDC terms:

```text
CDC:
Change Data Capture. Capturing inserts, updates, and deletes from source systems.

Transaction log:
Database log that records committed changes.

Binlog:
MySQL binary log.

WAL:
PostgreSQL write-ahead log.

Redo log:
Oracle-style transaction log concept.

LSN:
Log Sequence Number, source ordering position.

SCN:
System Change Number, often Oracle-style ordering point.

Offset:
Connector progress marker in a log or stream.

Snapshot:
Initial copy of existing source data.

Incremental snapshot:
Chunked snapshot while CDC is also running.

Backfill:
Historical reprocessing or rebuilding output.

Operation type:
Insert, update, delete, snapshot/read.

Before image:
Record values before an update/delete.

After image:
Record values after an insert/update.

Tombstone:
A delete marker or null-value message used by some CDC systems.

Current-state table:
Target table representing latest non-deleted row per key.

History table:
Target table preserving change history over time.

SCD Type 2:
Dimension pattern preserving historical versions with effective_from/effective_to.

Idempotency:
Safe replay without duplicate/corrupt final state.

At-least-once delivery:
Events may be delivered more than once.

Exactly-once-like output:
Final sink behaves as if changes were applied once, using idempotency.

CDC lag:
Delay between source commit and downstream availability.
```


## 5. Standard CDC Answer Framework

Use this framework for CDC design questions:

```text
1. Clarify requirements.
2. Identify source database and tables.
3. Identify consumers and target tables.
4. Estimate scale and update rate.
5. Define freshness/latency SLA.
6. Define source keys and delete behavior.
7. Choose CDC method:
   - log-based
   - trigger-based
   - timestamp-based pseudo-CDC
   - snapshot diff
8. Design initial snapshot.
9. Design CDC capture and transport.
10. Design raw CDC landing.
11. Define CDC event schema.
12. Define offset/checkpoint strategy.
13. Define deduplication and ordering.
14. Define current-state merge.
15. Define history/SCD construction if required.
16. Define delete/tombstone behavior.
17. Define schema evolution handling.
18. Define failure recovery and replay.
19. Define backfills and re-snapshots.
20. Define data quality and reconciliation.
21. Define monitoring and alerting.
22. Define security and governance.
23. Define scale and cost trade-offs.
24. Summarize final design.
```

Short version:

```text
Requirements → Source log → Snapshot → CDC stream → Raw → Stage → Merge/History → Quality → Monitoring → Recovery
```

Strict rule:

```text
No CDC design is strong without operation handling, ordering, offsets, idempotency, deletes, and reconciliation.
```


## 6. Scoring Rubric

Score CDC system design answers from 0 to 5.

### Score 0

No CDC understanding. Only names tools.

### Score 1

Mentions Kafka or Debezium but not operation type, offset, snapshot, or sink correctness.

### Score 2

Basic CDC flow but weak on deletes, ordering, idempotency, and recovery.

### Score 3

Reasonable design but weak on snapshot catch-up, schema evolution, reconciliation, or monitoring.

### Score 4

Interview-ready. Covers snapshot, log capture, operation schema, offsets, raw landing, dedupe, ordering, idempotent merge, delete handling, DQ, reconciliation, monitoring, and replay.

### Score 5

Strong. Handles snapshot consistency, incremental snapshotting, out-of-order events, duplicate delivery, schema drift, tombstones, SCD history, exactly-once-like sink semantics, source protection, multi-table dependencies, high-volume scale, lag alerting, backfills, and disaster recovery.

Automatic score cap below 4 if:

```text
no initial snapshot strategy
no offset/checkpoint strategy
no delete handling
no operation type handling
no ordering/LSN/binlog discussion
no idempotent sink design
no duplicate event handling
no source-target reconciliation
no CDC lag monitoring
only lists tools
```


## 7. Requirement Clarification Questions

Ask these before designing.

### Business and consumers

```text
What business problem does CDC solve?
Is the output current state, history, or both?
Who consumes the data?
Is this for BI, operational analytics, finance, ML, or replication?
What latency is required?
Is eventual consistency acceptable?
```

### Source

```text
What database is the source?
MySQL, PostgreSQL, SQL Server, Oracle, MongoDB, etc.?
Is log-based CDC available?
Can we enable binlog/WAL/logical replication?
Can we read from replica?
What tables are needed?
What are primary keys?
Are deletes important?
Are before images available?
Are schema changes common?
```

### Scale

```text
How many rows initially?
How many changes per second/minute/day?
How many tables?
How large are rows?
What is update/delete frequency?
What is growth rate?
```

### Target

```text
Where does data land?
Data lake, warehouse, Kafka, lakehouse table, operational store?
Do targets support MERGE?
Do targets support transactions?
Do consumers need current table, history table, or marts?
```

### Operations

```text
How much lag is acceptable?
How are failures handled?
How far back must replay be possible?
How are backfills handled?
What DQ checks are required?
What reconciliation is required?
```

Interview line:

```text
CDC design depends on source log capability, primary keys, delete semantics, latency SLA, and target write support.
```


## 8. CDC Requirements

CDC designs need clear functional and non-functional requirements.

Functional requirements:

```text
capture inserts
capture updates
capture deletes
capture schema changes if needed
initial load existing data
maintain current-state tables
maintain history tables if needed
support replay
support backfills
support downstream marts
```

Non-functional requirements:

```text
low lag
high reliability
ordering correctness
idempotent writes
recoverability
observability
source safety
cost control
security
scalability
schema evolution tolerance
```

Interview line:

```text
CDC requirements must explicitly state whether deletes, history, and low-latency are required.
```


## 9. Reference CDC Architecture

Reference architecture:

```text
[Source DB]
  tables + transaction log
        ↓
[CDC Connector]
  Debezium / DMS / Datastream / Fivetran / custom log reader
        ↓
[Transport]
  Kafka / Pub/Sub / Kinesis / object storage micro-batches
        ↓
[Raw CDC Landing]
  immutable events partitioned by source/table/ingestion date
        ↓
[Staging]
  normalized schema, operation type, key, source sequence, timestamps
        ↓
[Processing]
  dedupe, order, merge, history construction
        ↓
[Targets]
  current-state tables
  history/SCD tables
  downstream marts
        ↓
[Consumers]
  BI, ML, analysts, services
```

Control plane:

```text
offset/checkpoint store
schema registry/data contracts
DQ results
reconciliation tables
monitoring dashboards
alerts
runbooks
access controls
```

Interview line:

```text
I keep raw CDC events because they allow replaying target tables if merge logic or schema handling changes.
```


## 10. CDC Method Decision

CDC methods:

### Log-based CDC

```text
Reads database transaction logs.
Best for high-volume mutable data.
Low source impact.
Captures deletes.
Requires source configuration and permissions.
```

### Trigger-based CDC

```text
Database triggers write changes to audit tables.
Can be easier where log access is unavailable.
Adds write overhead to source.
Harder to maintain.
```

### Timestamp-based incremental

```text
Extracts rows where updated_at changed.
Simple but not true CDC.
Can miss deletes.
Can miss updates if updated_at is unreliable.
```

### Snapshot diff

```text
Compares snapshots to infer changes.
Works without log access.
Expensive for large tables.
```

Decision line:

```text
For large mutable source tables with deletes, log-based CDC is usually the strongest option.
```


## 11. Full Refresh vs Incremental vs CDC

### Full refresh

```text
Rebuilds everything. Simple, but expensive and slow for large mutable data.
```

### Timestamp incremental

```text
Processes rows where updated_at changed. Efficient, but weak for deletes and unreliable timestamps.
```

### CDC

```text
Captures inserts, updates, deletes from logs. More complex, but best for mutable high-volume systems.
```

### Snapshot diff

```text
Infers changes by comparing snapshots. Useful when CDC is unavailable, expensive at scale.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 12. Source Database Log Concepts

### MySQL

```text
Binary log / binlog records committed changes.
```

### PostgreSQL

```text
WAL with logical replication can expose row-level changes.
```

### SQL Server

```text
CDC/Change Tracking or transaction log-based tools.
```

### Oracle

```text
Redo logs and SCN-based change ordering.
```

### MongoDB

```text
Change streams can expose document changes.
```

### Key point

```text
Every source has different log, offset, schema, and permission model.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 13. Initial Snapshot

### Purpose

```text
Load existing source rows before applying new changes.
```

### Consistency

```text
Snapshot should be tied to a log position so changes after that point are captured.
```

### Large tables

```text
Use chunked or incremental snapshots to avoid source overload.
```

### Raw storage

```text
Store snapshot records with operation type such as snapshot/read.
```

### Catch-up

```text
After snapshot, apply CDC events from the captured offset onward.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 14. Snapshot Plus CDC Catch-Up

### Step 1

```text
Start CDC connector or identify starting log position.
```

### Step 2

```text
Take consistent snapshot of source tables.
```

### Step 3

```text
Record snapshot high-watermark/log position.
```

### Step 4

```text
Load snapshot to target as baseline.
```

### Step 5

```text
Apply CDC events after snapshot point.
```

### Step 6

```text
Validate target against source.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 15. CDC Event Schema

### source_system

```text
Origin system name.
```

### database_name

```text
Source database.
```

### schema_name

```text
Source schema.
```

### table_name

```text
Source table.
```

### primary_key

```text
Business/source primary key.
```

### operation

```text
insert/update/delete/snapshot.
```

### before

```text
Before image if available.
```

### after

```text
After image if available.
```

### source_commit_time

```text
Time source committed transaction.
```

### source_lsn

```text
Log position / sequence / binlog offset.
```

### transaction_id

```text
Source transaction identifier if available.
```

### ingested_at

```text
Time CDC event reached pipeline.
```

### connector_name

```text
Connector/source task.
```

### schema_version

```text
Schema version.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 16. Operation Types

### INSERT

```text
Create or upsert a new target row.
```

### UPDATE

```text
Update existing target row or insert if target missing depending on policy.
```

### DELETE

```text
Delete target current row, mark deleted, or end-date history row.
```

### SNAPSHOT / READ

```text
Initial snapshot row that seeds target state.
```

### TOMBSTONE

```text
Delete marker or null payload used by some log systems.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 17. Offset and Checkpoint Strategy

### Offset

```text
Progress position in the source log or message stream.
```

### Checkpoint

```text
Persisted state showing what has been safely processed.
```

### Rule

```text
Advance target checkpoint only after successful write and validation.
```

### Recovery

```text
On failure, resume from last committed checkpoint.
```

### Duplicate risk

```text
At-least-once replay may reprocess events, so sink must be idempotent.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 18. Ordering Strategy

### Within key

```text
Changes for the same primary key must be applied in source order.
```

### Across table

```text
Global table ordering may matter for constraints and reconciliation.
```

### Across tables

```text
Foreign-key dependencies can require careful ordering or eventual consistency.
```

### Ordering fields

```text
LSN, binlog position, SCN, transaction ID, source commit timestamp, sequence number.
```

### Tie-breaker

```text
Use source sequence, not ingestion time, for logical ordering.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 19. Raw CDC Landing

### Immutable

```text
Do not overwrite raw CDC events.
```

### Partition

```text
source/table/ingestion_date/hour or source_commit_date.
```

### Metadata

```text
operation, key, source_lsn, transaction_id, ingested_at, batch_id.
```

### Replay

```text
Raw CDC should rebuild current or history tables.
```

### Audit

```text
Raw CDC supports debugging missing/mismatched target rows.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 20. CDC Staging Layer

### Flatten

```text
Extract before/after fields into typed columns.
```

### Normalize

```text
Standardize operation names and timestamps.
```

### Validate

```text
Check primary key, operation, source sequence, schema.
```

### Dedupe

```text
Remove duplicate delivered events if needed.
```

### Prepare

```text
Create current-state and history inputs.
```

Interview line:

```text
CDC correctness depends on operation type, source order, and checkpoint discipline.
```


## 21. Current-State Table Design

A current-state table contains the latest non-deleted version of each source row.

Example target:

```text
orders_current
- order_id
- user_id
- status
- amount
- updated_at
- _source_lsn
- _is_deleted
- _ingested_at
```

Processing logic:

```text
snapshot/read → insert baseline row
insert → insert or update row
update → update row
delete → delete row or mark _is_deleted = true
```

Pseudo-SQL:

```sql
MERGE INTO orders_current t
USING latest_cdc_per_key s
ON t.order_id = s.order_id
WHEN MATCHED AND s.operation = 'DELETE' THEN DELETE
WHEN MATCHED THEN UPDATE SET ...
WHEN NOT MATCHED AND s.operation <> 'DELETE' THEN INSERT (...);
```

Interview line:

```text
For current-state tables, I keep only the latest source state per key and apply deletes explicitly.
```


## 22. History Table / SCD Type 2 Design

A history table preserves versions over time.

Example:

```text
dim_user_history
- user_id
- plan
- country
- effective_from
- effective_to
- is_current
- source_lsn
- operation
```

Processing logic:

```text
if insert:
  create new current version

if update changes tracked fields:
  end-date previous current row
  insert new current row

if delete:
  end-date previous current row
  optionally insert deleted/tombstone version
```

Validation:

```text
one current row per key
no overlapping intervals per key
effective_from < effective_to where effective_to exists
source ordering preserved
```

Interview line:

```text
If historical reporting is required, CDC should build SCD intervals using source commit order, not ingestion order.
```


## 23. Deduplication of CDC Events

CDC systems often deliver at-least-once.

Duplicate event causes:

```text
connector restart
retry after sink failure
message bus redelivery
checkpoint not advanced
network failure
```

Deduplication key options:

```text
source table + primary key + source_lsn
source table + primary key + transaction_id + event_sequence
message topic + partition + offset
event_id if connector provides it
```

Pattern:

```sql
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY table_name, primary_key, source_lsn
      ORDER BY ingested_at DESC
    ) AS rn
  FROM raw_cdc
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Interview line:

```text
CDC sinks should tolerate duplicate delivery by deduping or using idempotent application keyed by source sequence.
```


## 24. Latest Event Per Key for Current State

For current-state loading from a micro-batch, keep the latest event per key in that batch.

SQL pattern:

```sql
WITH ranked_changes AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY primary_key
      ORDER BY source_lsn DESC, source_commit_time DESC
    ) AS rn
  FROM staging_cdc
)
SELECT *
FROM ranked_changes
WHERE rn = 1;
```

Important:

```text
This is safe for current-state tables when only final state matters.
It is not enough for history tables where every change must be preserved.
```

Interview line:

```text
For current-state tables, a micro-batch can collapse to latest event per key; for history, every ordered change matters.
```


## 25. Out-of-Order Events

Out-of-order events happen when ingestion order differs from source commit order.

Causes:

```text
parallel connector tasks
network delay
message bus partitioning
micro-batch arrival differences
retries
```

Handling:

```text
apply by source_lsn/source sequence, not ingested_at
buffer small windows if needed
use per-key ordering
ignore older events if target already has newer source_lsn
validate monotonic source_lsn per key
```

Current-state guard:

```text
Only update target if incoming source_lsn is greater than target source_lsn.
```

Interview line:

```text
In CDC, source order beats ingestion order.
```


## 26. Delete Handling

Deletes are the main reason timestamp incremental extraction is not enough.

Delete strategies:

### Hard delete in target

```text
Remove row from current table.
```

### Soft delete in target

```text
Set is_deleted = true and deleted_at.
```

### Tombstone/history

```text
End-date history row and preserve delete event.
```

Decision depends on:

```text
consumer expectations
audit requirements
privacy requirements
warehouse policy
history needs
```

Interview line:

```text
CDC pipelines must handle deletes intentionally; ignoring delete events creates stale target data.
```


## 27. Tombstone Events

Some CDC systems emit tombstone events after deletes.

Tombstone may mean:

```text
a null payload for Kafka compaction
a delete marker
a signal that the key was removed
```

Handling:

```text
understand connector semantics
do not accidentally treat tombstone as malformed data
use delete event before tombstone to update target
optionally store tombstone metadata in raw CDC
```

Interview line:

```text
Tombstones are not random bad records; they can be part of delete semantics.
```


## 28. Idempotent CDC Sink

CDC delivery is commonly at-least-once, so target writes must be idempotent.

Idempotent sink patterns:

```text
MERGE by primary key with source_lsn guard
dedupe by source event ID
transactional batch writes
commit offset only after target success
partition overwrite for derived tables
raw event replay
```

Source LSN guard:

```text
update target only when incoming.source_lsn > target._source_lsn
```

Interview line:

```text
Exactly-once-like CDC output is achieved with idempotent sink logic and disciplined checkpoint commits.
```


## 29. Checkpoint Commit Discipline

Checkpoint mistakes cause data loss or duplicates.

Bad:

```text
commit offset before target write succeeds
```

Failure:

```text
sink fails after offset commit
event is skipped forever
```

Safe:

```text
read events
write target idempotently
validate batch
commit checkpoint
```

If failure happens before checkpoint:

```text
events may replay
idempotent sink handles duplicates
```

Interview line:

```text
Never advance CDC progress beyond what has been safely written and validated downstream.
```


## 30. Raw Replay Strategy

Replay means rebuilding target from raw CDC.

Needed for:

```text
buggy merge logic
schema fix
target corruption
backfills
new downstream table
audit investigation
```

Replay design:

```text
store raw CDC events immutably
store source_lsn and operation
make transformation deterministic
support replay by table and LSN/date range
write to temp target
validate against source/current target
swap/promote after validation
```

Interview line:

```text
Raw CDC landing turns CDC into a recoverable system instead of a one-way stream.
```


## 31. Data Quality Checks for CDC

- primary key not null
- operation type valid
- source_lsn not null
- duplicate event count
- target duplicate key count
- current table one row per key
- history table no overlapping intervals
- delete count trends
- update count trends
- source-target row count reconciliation
- source-target checksum or aggregate reconciliation
- CDC lag within SLA
- schema version expected

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 32. Source-Target Reconciliation

- Compare source count to target current count, adjusted for deletes.
- Compare primary key sets.
- Compare aggregates such as sum(amount) by date/status.
- Compare row hashes for sampled or full records.
- Run full reconciliation periodically and incremental reconciliation frequently.
- Store reconciliation results by table and run date.

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 33. CDC Lag Monitoring

- Source commit time to connector capture time.
- Connector capture time to raw landing time.
- Raw landing time to target apply time.
- End-to-end source commit to target availability.
- Alert if lag exceeds SLA.

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 34. Operational Metrics

- events captured per table
- events applied per table
- inserts/updates/deletes count
- duplicate event count
- failed event count
- quarantine count
- checkpoint age
- connector status
- sink write latency
- merge duration
- replay/backfill status

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 35. Alert Conditions

- connector stopped
- CDC lag above threshold
- source log retention risk
- schema breaking change
- sink merge failed
- target duplicate keys
- delete spike
- zero events unexpectedly
- offset not advancing
- reconciliation mismatch
- raw landing missing

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 36. Failure Handling

- Connector failure: restart from stored offset.
- Sink failure: replay from last safe checkpoint.
- Schema failure: pause affected table and alert.
- Bad records: quarantine with raw event and error reason.
- Target corruption: replay raw CDC to rebuild.
- Source log expired: re-snapshot affected table.

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 37. Schema Evolution

- Add nullable column: usually safe.
- Add required column: requires transformation/consumer review.
- Rename column: breaking change unless mapped.
- Drop column: breaking change for consumers.
- Type change: potentially breaking and should fail fast.
- Enum change: may be warning or breaking depending on contract.

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 38. Data Contracts for CDC

- primary key
- operation semantics
- before/after image availability
- source ordering field
- delete behavior
- schema evolution rules
- freshness SLA
- owner and escalation path
- retention period

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 39. Security and Governance

- CDC can expose sensitive row-level changes.
- Restrict raw CDC access.
- Encrypt in transit and at rest.
- Mask PII in curated/mart layers.
- Store secrets in secret manager.
- Audit access to CDC logs.
- Handle right-to-delete/privacy requirements intentionally.

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 40. Cost and Scaling

- Filter to needed tables and columns if possible.
- Partition raw CDC by table and ingestion date/hour.
- Compact small CDC files.
- Use micro-batches for warehouse merges.
- Group merge operations by table.
- Scale connectors by table/partition where safe.
- Avoid too many tiny merge operations.
- Pre-aggregate downstream marts instead of querying raw CDC.

Interview line:

```text
CDC production readiness requires both operational health metrics and data correctness checks.
```


## 41. Practice Case 1: OLTP Orders CDC to Warehouse

Prompt:

```text
Design a CDC pipeline for oltp orders cdc to warehouse.
```

Source:

```text
orders table in OLTP database
```

Output:

```text
orders_current and orders_history
```

Strong design points:

- take consistent initial snapshot
- start log-based CDC from snapshot position
- land raw CDC events with order_id, operation, source_lsn, before/after
- dedupe duplicate events by table/key/source_lsn
- for current table, keep latest event per order_id per micro-batch
- MERGE inserts and updates, apply deletes
- for history, apply every ordered change and end-date old versions
- monitor CDC lag, duplicate keys, delete spikes, reconciliation

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 42. Practice Case 2: Payments CDC with Finance Reconciliation

Prompt:

```text
Design a CDC pipeline for payments cdc with finance reconciliation.
```

Source:

```text
payments table with updates and deletes
```

Output:

```text
payments_current and payment_reconciliation
```

Strong design points:

- capture all payment status changes
- preserve before/after images for audit
- hard or soft delete based on finance policy
- merge current table by payment_id
- reconcile provider totals and internal target totals
- alert on amount/status mismatch
- retain raw CDC and reconciliation history

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 43. Practice Case 3: User Profile CDC to SCD Type 2

Prompt:

```text
Design a CDC pipeline for user profile cdc to scd type 2.
```

Source:

```text
users table with profile changes
```

Output:

```text
dim_user_current and dim_user_history
```

Strong design points:

- capture inserts, updates, deletes
- track changed fields such as country, plan, status
- close previous history row when tracked attributes change
- insert new current history row
- ensure one current row per user
- validate no overlapping effective intervals
- support as-of joins from facts to user history

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 44. Practice Case 4: Inventory CDC

Prompt:

```text
Design a CDC pipeline for inventory cdc.
```

Source:

```text
inventory item quantity changes
```

Output:

```text
inventory_current and inventory_movement_history
```

Strong design points:

- capture updates to quantity and warehouse
- apply current quantity by product_id + warehouse_id
- preserve history for audit
- monitor negative quantity anomalies
- handle high update frequency and hot keys
- reconcile daily stock snapshot with source

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 45. Practice Case 5: CDC into Data Lake

Prompt:

```text
Design a CDC pipeline for cdc into data lake.
```

Source:

```text
multiple source tables
```

Output:

```text
bronze CDC, silver current tables
```

Strong design points:

- land raw events in bronze partitioned by table and ingestion date
- normalize into silver staging
- merge into lakehouse tables supporting ACID/MERGE
- compact small files
- track offsets and table-specific checkpoints
- monitor lag and table-level DQ

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 46. Practice Case 6: Kafka Debezium CDC

Prompt:

```text
Design a CDC pipeline for kafka debezium cdc.
```

Source:

```text
MySQL/Postgres database
```

Output:

```text
Kafka topics and warehouse sink
```

Strong design points:

- Debezium reads binlog/WAL
- one topic per table
- messages include key, operation, before/after, source metadata
- sink reads topics in order by partition
- dedupe/replay with topic partition offset
- handle tombstones
- commit consumer offset after sink success

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 47. Practice Case 7: Micro-Batch CDC to Snowflake/BigQuery

Prompt:

```text
Design a CDC pipeline for micro-batch cdc to snowflake/bigquery.
```

Source:

```text
CDC stream or raw files
```

Output:

```text
warehouse current tables
```

Strong design points:

- buffer CDC into micro-batches
- stage batch files in cloud storage
- load into staging tables
- dedupe latest event per key for current table
- MERGE into target
- commit offsets after merge success
- monitor merge duration and warehouse cost

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 48. Practice Case 8: Multi-Table CDC Pipeline

Prompt:

```text
Design a CDC pipeline for multi-table cdc pipeline.
```

Source:

```text
orders, order_items, payments, users
```

Output:

```text
warehouse facts and dimensions
```

Strong design points:

- capture each table independently
- preserve table-specific offsets
- load current state tables first
- build downstream marts after CDC tables are updated
- handle referential consistency eventually
- run reconciliation by table
- monitor lag per table

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 49. Practice Case 9: CDC Backfill / Re-Snapshot

Prompt:

```text
Design a CDC pipeline for cdc backfill / re-snapshot.
```

Source:

```text
target table corrupted or new table added
```

Output:

```text
rebuilt target
```

Strong design points:

- pause or isolate target writes if needed
- replay raw CDC from chosen point if available
- or run new consistent snapshot
- apply CDC catch-up from snapshot position
- write to temp target
- validate source-target reconciliation
- swap/promote rebuilt target

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 50. Practice Case 10: CDC Schema Change Event

Prompt:

```text
Design a CDC pipeline for cdc schema change event.
```

Source:

```text
source adds/changes columns
```

Output:

```text
staging and target evolution
```

Strong design points:

- detect schema change from connector/schema registry
- allow additive nullable columns if policy permits
- pause on breaking type/rename/drop changes
- update staging and target schema
- run compatibility tests
- notify downstream consumers

Minimum interview answer must include:

```text
snapshot
log capture
operation schema
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay/backfill
trade-offs
```

Interview line:

```text
CDC correctness is measured by whether the target can be trusted after failures, retries, deletes, and schema changes.
```


## 51. Initial Snapshot Consistency

The initial snapshot must align with CDC log position.

Problem:

```text
If snapshot and log position are not coordinated, changes can be missed or duplicated.
```

Safe approach:

```text
capture starting log position
snapshot existing rows consistently
start applying CDC changes after snapshot position
make sink idempotent in case overlap occurs
```

Interview line:

```text
A CDC pipeline must avoid gaps between initial snapshot and ongoing log capture.
```


## 52. Incremental Snapshotting

For huge tables, full snapshot in one transaction may be impossible.

Incremental snapshot strategy:

```text
split table into chunks by primary key range
snapshot chunks gradually
keep CDC running during snapshot
reconcile chunk completion
apply CDC changes after chunk baseline
avoid source overload
```

Interview line:

```text
For very large tables, I use chunked snapshots with CDC catch-up instead of locking/scanning everything at once.
```


## 53. Transaction Boundaries

Some CDC events belong to the same source transaction.

Why it matters:

```text
multi-row consistency
foreign key relationships
audit correctness
exact ordering
```

Design options:

```text
preserve transaction_id and event sequence
apply events in transaction order
accept eventual consistency in analytical targets
group transaction events when needed
```

Interview line:

```text
For analytics, eventual consistency across tables may be acceptable, but the design should preserve transaction metadata for correctness-sensitive use cases.
```


## 54. Multi-Table Dependencies

CDC per table can arrive at different times.

Example:

```text
order inserted before user dimension update arrives downstream
```

Handling:

```text
allow temporary unknown dimension
run referential checks with grace period
process dimension tables before marts
build marts after all required table CDC checkpoints pass
use eventual consistency policy
```

Interview line:

```text
For downstream marts, I wait for required CDC tables to reach compatible checkpoints before publishing.
```


## 55. High-Volume CDC

High-volume CDC challenges:

```text
many changes per second
hot keys
large rows
expensive warehouse merges
small files
connector lag
source log retention risk
```

Strategies:

```text
micro-batch merges
partition raw CDC by table/time
cluster target by primary key
compact files
collapse current-state batch to latest event per key
parallelize by table where safe
scale connector tasks carefully
monitor lag and backpressure
```

Interview line:

```text
For high-volume CDC, I separate raw capture from sink application and optimize merges with micro-batching and latest-per-key collapsing.
```


## 56. Hot Keys and Update Storms

A hot key receives many updates.

Examples:

```text
inventory counter
account balance
popular product
system status row
```

Risks:

```text
large number of CDC events for one key
merge contention
history explosion
lag
```

Handling:

```text
collapse to latest event for current state
preserve full history only if business needs it
aggregate or compress history if allowed
monitor top updated keys
separate high-churn tables
```

Interview line:

```text
For current-state CDC, hot-key update storms can be collapsed to latest state per micro-batch.
```


## 57. Warehouse Merge Optimization

MERGE can be expensive.

Optimization:

```text
dedupe source batch before MERGE
only merge affected keys/partitions
cluster target by primary key
avoid updating unchanged rows
batch changes instead of per-event merge
separate deletes if helpful
track merge duration and bytes scanned
```

Interview line:

```text
A CDC sink should avoid one warehouse MERGE per event; micro-batch and dedupe before merging.
```


## 58. Lakehouse CDC Tables

Lakehouse CDC often writes to ACID table formats.

Concepts:

```text
append raw CDC to bronze
normalize to silver
MERGE into current table
OPTIMIZE/compact files
VACUUM/retention policy
time travel if supported
```

Risks:

```text
small files
many small commits
concurrent writers
retention misconfiguration
```

Interview line:

```text
For CDC on lakehouse tables, file compaction and transactional merge behavior are critical.
```


## 59. CDC Replay and Disaster Recovery

Replay plan:

```text
identify target corruption or bug
choose replay range
read raw CDC events or source logs
write rebuilt target to temp table
validate source-target reconciliation
swap target atomically
record replay metadata
```

If raw CDC is not retained:

```text
may need fresh snapshot and catch-up from current log position
```

Interview line:

```text
CDC retention policy decides how far back the system can recover without re-snapshotting.
```


## 60. Source Log Retention Risk

CDC connectors must keep up before source logs expire.

Risk:

```text
connector down too long
source binlog/WAL older changes deleted
cannot resume from old offset
```

Mitigation:

```text
monitor lag and log retention window
alert before retention risk
increase source log retention if needed
recover connector quickly
re-snapshot if offset is lost
```

Interview line:

```text
CDC lag is not just freshness; if lag exceeds source log retention, data loss can occur.
```


## 61. Privacy and Deletes

Deletes can be business deletes or privacy deletes.

Privacy delete implications:

```text
must remove/mask data from downstream targets
raw CDC may contain PII
retention policy matters
legal requirements may override analytics history
```

Design:

```text
classify delete type if possible
propagate deletion to current, history, marts
handle raw retention and access controls
audit deletion processing
```

Interview line:

```text
Delete handling in CDC must align with business, audit, and privacy requirements.
```


## 62. CDC vs Event Sourcing

CDC and event sourcing are different.

CDC:

```text
captures database changes after the fact
source of truth is database state
events are technical data changes
```

Event sourcing:

```text
application emits business events as source of truth
events represent domain actions
state is derived from events
```

Interview line:

```text
CDC captures row changes, while event sourcing captures business events; they are not the same design.
```


## 63. Pattern Classification Drill

### Need deletes from mutable OLTP table

```text
Use log-based CDC if available.
```

### Need existing data before changes

```text
Initial snapshot plus CDC catch-up.
```

### Connector restarts and duplicates events

```text
Idempotent sink and event dedupe.
```

### Events arrive out of ingestion order

```text
Apply by source_lsn, not ingested_at.
```

### Target current table has stale deleted rows

```text
Delete/tombstone handling missing.
```

### Need historical user profile

```text
Build SCD Type 2 history from CDC.
```

### CDC lag near log retention limit

```text
Critical alert; risk of data loss.
```

### Warehouse MERGE too slow

```text
Micro-batch, dedupe latest per key, cluster target.
```

### Schema type changed

```text
Breaking schema evolution event.
```

### Need rebuild after bug

```text
Replay raw CDC or re-snapshot.
```

### Source updated_at unreliable

```text
Timestamp incremental is unsafe; prefer CDC.
```

### Multiple updates to same key in batch

```text
Collapse to latest for current state, preserve all for history.
```

### Need finance audit

```text
Preserve before/after images and reconciliation.
```

### Kafka tombstone seen

```text
Handle delete/compaction semantics.
```

### Offset committed before sink write

```text
Data loss risk.
```

### No primary key

```text
CDC target merge is difficult; need key strategy.
```

### Raw CDC not stored

```text
Replay and audit are limited.
```

### Marts publish before all tables caught up

```text
Checkpoint coordination issue.
```

### Privacy delete

```text
Propagate delete/mask downstream and audit.
```

### Small CDC files

```text
Compaction and micro-batch sizing.
```


## 64. High-ROI CDC Topics

### CDC basics

```text
insert/update/delete capture
```

### transaction logs

```text
binlog/WAL/LSN/SCN
```

### initial snapshot

```text
baseline source state
```

### snapshot catch-up

```text
no gaps between snapshot and log
```

### event schema

```text
operation, before/after, key, source_lsn
```

### offsets

```text
progress tracking
```

### ordering

```text
source sequence over ingestion time
```

### dedupe

```text
at-least-once delivery
```

### current table

```text
latest non-deleted row
```

### history table

```text
ordered versions/SCD Type 2
```

### deletes

```text
hard/soft/tombstone
```

### idempotency

```text
safe replay
```

### reconciliation

```text
source-target correctness
```

### lag monitoring

```text
freshness and log retention
```

### schema evolution

```text
safe vs breaking changes
```

### replay

```text
rebuild from raw CDC
```

### merge optimization

```text
micro-batch and collapse
```

### security

```text
PII and raw change access
```


## 65. Review Checklist

### Did candidate clarify source DB and CDC capability?

```text
Must know source constraints.
```

### Did candidate define current vs history output?

```text
Different processing logic.
```

### Did candidate design initial snapshot?

```text
Needed for existing rows.
```

### Did candidate avoid snapshot-log gaps?

```text
Correctness risk.
```

### Did candidate preserve raw CDC?

```text
Replay and audit.
```

### Did candidate define event schema?

```text
Operation and source sequence needed.
```

### Did candidate define offset/checkpoint?

```text
Recovery.
```

### Did candidate handle duplicates?

```text
At-least-once delivery.
```

### Did candidate handle ordering?

```text
LSN/binlog/SCN.
```

### Did candidate handle deletes?

```text
Critical.
```

### Did candidate design idempotent sink?

```text
Safe replay.
```

### Did candidate define current merge?

```text
Latest state.
```

### Did candidate define history/SCD if needed?

```text
Historical reporting.
```

### Did candidate handle schema changes?

```text
Production risk.
```

### Did candidate define reconciliation?

```text
Trust.
```

### Did candidate monitor lag?

```text
Freshness and retention.
```

### Did candidate handle failure/replay?

```text
Recovery.
```

### Did candidate explain scale/cost?

```text
Production readiness.
```

### Did candidate discuss security?

```text
CDC has sensitive data.
```

### Did candidate explain trade-offs?

```text
System design maturity.
```


## 66. Weakness Repair Map

### Only says Kafka/Debezium

```text
Practice CDC architecture framework.
```

### No snapshot

```text
Practice initial snapshot + catch-up.
```

### No delete handling

```text
Practice tombstone/delete cases.
```

### No ordering

```text
Practice LSN/binlog ordering drills.
```

### No offset strategy

```text
Practice checkpoint discipline.
```

### No idempotency

```text
Practice replay-safe MERGE.
```

### No reconciliation

```text
Practice source-target checks.
```

### No history design

```text
Practice SCD from CDC.
```

### No schema evolution

```text
Practice data contract drills.
```

### No monitoring

```text
Practice lag and alert drills.
```

### No scale thinking

```text
Practice high-volume CDC and merge optimization.
```

### Poor communication

```text
Practice whiteboard scripts.
```


## 67. 7-Day CDC Study Plan

### Day 1

```text
CDC basics, logs, operation types, event schema.
```

### Day 2

```text
Initial snapshot, catch-up, offsets, checkpointing.
```

### Day 3

```text
Current-state merge, dedupe, idempotency, deletes.
```

### Day 4

```text
History/SCD Type 2, ordering, out-of-order events.
```

### Day 5

```text
Data quality, reconciliation, lag monitoring, alerts.
```

### Day 6

```text
Scale, merge optimization, schema evolution, replay.
```

### Day 7

```text
CDC system design mock and weakness repair.
```


## 68. 30-Day CDC Study Plan

### Week 1

```text
Foundation: CDC concepts, source logs, snapshot, event schema.
```

### Week 2

```text
Correctness: offsets, ordering, deletes, idempotency, current tables.
```

### Week 3

```text
Production: history, DQ, reconciliation, monitoring, schema evolution.
```

### Week 4

```text
Advanced: high-volume CDC, replay, lakehouse/warehouse sinks, mocks.
```


## 69. Timed Interview Protocol

### 0-5 minutes

```text
Clarify source DB, tables, latency, outputs, deletes, scale.
```

### 5-12 minutes

```text
Draw source log → connector → transport → raw → stage → sink.
```

### 12-22 minutes

```text
Deep dive into snapshot, offsets, ordering, event schema.
```

### 22-32 minutes

```text
Deep dive into current merge, history, deletes, idempotency.
```

### 32-40 minutes

```text
Discuss DQ, reconciliation, monitoring, failure/replay.
```

### 40-45 minutes

```text
Discuss scale, security, cost, trade-offs, final summary.
```


## 70. CDC Whiteboard Template

```text
Requirements:
- source DB:
- tables:
- output:
- current/history:
- latency SLA:
- volume:
- deletes:
- schema changes:

Architecture:
source DB log → CDC connector → transport/raw landing → staging → merge/history → warehouse/marts

Correctness:
- initial snapshot:
- log position:
- offset/checkpoint:
- ordering field:
- dedupe key:
- delete handling:
- idempotent sink:

Operations:
- DQ:
- reconciliation:
- lag monitoring:
- schema evolution:
- replay:
- backfill:
- alerts:
- security:
- cost/scale:
```


## 71. CDC Event Schema Template

```text
event_id:
source_system:
database_name:
schema_name:
table_name:
primary_key:
operation:
before_payload:
after_payload:
source_commit_time:
source_lsn:
transaction_id:
transaction_sequence:
connector_name:
topic:
partition:
offset:
ingested_at:
schema_version:
batch_id:
```


## 72. CDC Current Table Template

```text
table_name_current

Business columns:
- source primary key
- source attributes

Metadata columns:
- _source_lsn
- _source_commit_time
- _operation
- _ingested_at
- _is_deleted if soft delete
- _updated_by_cdc_batch_id
```


## 73. CDC History Table Template

```text
table_name_history

Business columns:
- source primary key
- tracked attributes

History columns:
- effective_from
- effective_to
- is_current
- operation
- source_lsn
- source_commit_time
- ingested_at
```


## 74. CDC DQ Checklist Template

```text
Raw checks:
- operation valid
- primary key present
- source_lsn present
- schema version known

Staging checks:
- duplicate event count
- invalid payload count
- out-of-order event count

Target checks:
- current table duplicate key count = 0
- history intervals do not overlap
- delete count expected
- source-target row count reconciles
- checksum/sample comparison passes

Operational checks:
- connector running
- lag within SLA
- offset advancing
- source log retention safe
```


## 75. CDC Failure Runbook Template

```text
Failure:
Affected source:
Affected table:
Affected target:
Last safe checkpoint:
Current lag:
Source log retention remaining:

Steps:
1. Check connector status.
2. Check source log availability.
3. Check raw landing.
4. Check sink errors.
5. Check schema changes.
6. Resume from last safe checkpoint.
7. If offset expired, re-snapshot affected table.
8. Validate source-target reconciliation.
9. Notify consumers if SLA missed.

Escalation:
- source owner:
- data platform owner:
- business owner:
```


## 76. Mock Set 1: CDC Foundations

Problems:

- Explain CDC vs timestamp incremental.
- Design initial snapshot plus CDC catch-up.
- Define a CDC event schema.
- Explain LSN/binlog/WAL/offset.
- Explain why deletes need CDC.

Expected answer must include:

```text
snapshot
operation type
ordering
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 77. Mock Set 2: Current-State Loading

Problems:

- Build orders_current from CDC.
- Handle duplicate CDC events.
- Handle out-of-order CDC events.
- Design idempotent MERGE.
- Handle delete/tombstone events.

Expected answer must include:

```text
snapshot
operation type
ordering
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 78. Mock Set 3: History and SCD

Problems:

- Build user plan history from CDC.
- End-date previous versions.
- Validate no overlapping intervals.
- Handle delete events in history.
- Support as-of joins from facts.

Expected answer must include:

```text
snapshot
operation type
ordering
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 79. Mock Set 4: Operations and Recovery

Problems:

- Monitor CDC lag.
- Handle connector failure.
- Handle source log retention risk.
- Replay raw CDC after target corruption.
- Handle schema evolution.

Expected answer must include:

```text
snapshot
operation type
ordering
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 80. Mock Set 5: Case Designs

Problems:

- Design MySQL orders CDC to warehouse.
- Design payment CDC with reconciliation.
- Design Debezium Kafka CDC pipeline.
- Design CDC into data lakehouse.
- Design multi-table CDC for customer 360.

Expected answer must include:

```text
snapshot
operation type
ordering
offset/checkpoint
idempotent sink
delete handling
reconciliation
monitoring
replay
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 81. CDC FAQ

### FAQ 1: What is CDC?

```text
Change Data Capture is capturing inserts, updates, and deletes from source systems, often using database logs.
```

### FAQ 2: Why use CDC instead of updated_at extraction?

```text
CDC can capture deletes and reliable ordered changes; updated_at extraction may miss deletes or unreliable timestamps.
```

### FAQ 3: What is the initial snapshot?

```text
The baseline copy of existing source rows before applying ongoing CDC events.
```

### FAQ 4: What is an offset?

```text
A progress marker showing how far the connector or sink has processed in a log or stream.
```

### FAQ 5: Why is ordering important?

```text
Changes for the same key must be applied in source order to avoid stale target state.
```

### FAQ 6: How do you handle duplicate CDC events?

```text
Use event/source sequence dedupe and idempotent sink logic.
```

### FAQ 7: How do you handle deletes?

```text
Apply hard delete, soft delete, or tombstone/history behavior based on target requirements.
```

### FAQ 8: How do you build a current table?

```text
Merge latest source state per key, applying inserts, updates, and deletes.
```

### FAQ 9: How do you build history?

```text
Apply changes in order and create effective_from/effective_to intervals.
```

### FAQ 10: What do you monitor?

```text
Connector status, lag, offset progress, event counts, errors, duplicates, target DQ, and reconciliation.
```


## 82. Candidate Self-Review Questions

After every CDC design, candidate should answer:

```text
1. What source database is used?
2. Does source support log-based CDC?
3. What tables are captured?
4. What are the primary keys?
5. Are deletes required?
6. Is current state, history, or both needed?
7. What is the latency SLA?
8. What is the update/delete volume?
9. How is the initial snapshot taken?
10. How is snapshot position tied to CDC log?
11. What does each CDC event contain?
12. What is the ordering field?
13. What is the checkpoint/offset strategy?
14. When is checkpoint advanced?
15. How are duplicate events handled?
16. How are out-of-order events handled?
17. How are deletes and tombstones handled?
18. How is current-state MERGE idempotent?
19. How is history/SCD built?
20. How are schema changes handled?
21. What DQ checks run?
22. How is source-target reconciliation done?
23. How is CDC lag monitored?
24. What happens if connector fails?
25. What happens if source logs expire?
26. How can target be replayed?
27. How are backfills handled?
28. How is sensitive data protected?
29. How is cost controlled?
30. What are the trade-offs?
```

If candidate cannot answer these:

```text
The CDC design is not interview-ready.
```


## 83. Final Exit Test

Candidate passes CDC pipeline system design when they can explain:

```text
1. CDC vs full refresh vs timestamp incremental.
2. Source log concepts.
3. Initial snapshot.
4. Snapshot + CDC catch-up.
5. CDC event schema.
6. Operation types.
7. Before/after images.
8. Tombstones.
9. Offsets and checkpoints.
10. Checkpoint commit discipline.
11. Source ordering.
12. Duplicate event handling.
13. Out-of-order event handling.
14. Raw CDC landing.
15. CDC staging.
16. Current-state table merge.
17. History/SCD Type 2 construction.
18. Delete handling.
19. Idempotent sink design.
20. Replay from raw CDC.
21. Source-target reconciliation.
22. CDC lag monitoring.
23. Alerting.
24. Failure recovery.
25. Schema evolution.
26. Data contracts.
27. Security/governance.
28. Cost and scaling.
29. High-volume CDC.
30. Warehouse merge optimization.
31. Lakehouse CDC.
32. Source log retention risk.
33. Multi-table CDC.
34. Privacy deletes.
35. Case study: orders CDC.
36. Case study: payments CDC.
37. Case study: user SCD CDC.
38. Case study: Debezium/Kafka CDC.
39. Case study: CDC to warehouse micro-batch.
40. Trade-offs and final summary.
```

Passing standard:

```text
Average score >= 4/5.
No missing snapshot.
No missing offset/checkpoint.
No missing delete handling.
No missing ordering.
No missing idempotency.
No missing reconciliation.
No missing lag monitoring.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles production CDC edge cases clearly under interview pressure.
```


## 84. Final Summary

CDC pipeline design is a core Data Engineering system design skill.

The candidate must master:

```text
CDC concepts
source transaction logs
initial snapshot
snapshot catch-up
operation types
before/after images
offsets
checkpoints
source ordering
raw CDC landing
staging normalization
deduplication
out-of-order handling
current-state merge
history/SCD construction
delete/tombstone handling
idempotent sinks
replay
backfills
schema evolution
data contracts
data quality
source-target reconciliation
lag monitoring
failure recovery
security
cost
scaling
trade-offs
```

The mentor must be strict:

```text
Only says Kafka/Debezium → not interview-ready.
No initial snapshot → not interview-ready.
No offset/checkpoint → not interview-ready.
No ordering → not interview-ready.
No delete handling → not interview-ready.
No idempotent sink → not interview-ready.
No reconciliation → not interview-ready.
No lag monitoring → not interview-ready.
No replay plan → not interview-ready.
```

Final interview line:

```text
A production CDC pipeline must preserve source change semantics and make downstream tables correct, replayable, observable, and safe to rerun.
```


## 85. Additional Mini Scenario Cards

### Mini Scenario 1: Connector restarts and replays same events

Recommended direction:

```text
Use idempotent sink and dedupe by source_lsn/topic offset.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 2: Delete events ignored

Recommended direction:

```text
Apply hard delete, soft delete, or end-date logic intentionally.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 3: Snapshot and CDC have a gap

Recommended direction:

```text
Tie snapshot to log position and apply changes from that point.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 4: Target has stale row after out-of-order event

Recommended direction:

```text
Use source_lsn guard, not ingestion time.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 5: Offset committed before sink write

Recommended direction:

```text
Data loss risk; commit after successful write and validation.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 6: CDC lag exceeds source log retention

Recommended direction:

```text
Critical incident; re-snapshot may be required.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 7: Warehouse MERGE too slow

Recommended direction:

```text
Micro-batch, collapse latest per key, cluster target.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 8: History table has overlapping intervals

Recommended direction:

```text
Apply changes in source order and validate intervals.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 9: Tombstone treated as malformed

Recommended direction:

```text
Understand connector delete/compaction semantics.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 10: Schema column type changes

Recommended direction:

```text
Fail fast as breaking schema event.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 11: No raw CDC storage

Recommended direction:

```text
Replay and audit are limited.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 12: Privacy delete arrives

Recommended direction:

```text
Propagate deletion/masking downstream and audit.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 13: Current table duplicate keys

Recommended direction:

```text
Fix MERGE key and dedupe source batch.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 14: Multiple updates to same key in one batch

Recommended direction:

```text
For current table, keep latest; for history, apply all in order.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 15: Multi-table mart publishes inconsistently

Recommended direction:

```text
Wait for all required table checkpoints.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 16: Source primary key missing

Recommended direction:

```text
CDC merge needs key strategy or target cannot be trusted.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 17: Connector reads source primary DB heavily

Recommended direction:

```text
Use log-based CDC/read replica and source-safe configuration.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 18: Small CDC files accumulate

Recommended direction:

```text
Compact files and tune micro-batch size.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 19: Reconciliation mismatch

Recommended direction:

```text
Compare keys, row hashes, counts, and recent changes.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 20: Need new target from existing CDC

Recommended direction:

```text
Replay raw CDC into a new table.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 21: Snapshot locks source table

Recommended direction:

```text
Use chunked/incremental snapshot or replica.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 22: CDC captures before image unavailable

Recommended direction:

```text
Design history based on after images and target current state, or adjust source config.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 23: Deletes should be audited

Recommended direction:

```text
Preserve delete events in history/audit table.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 24: BI table should not expose deleted users

Recommended direction:

```text
Filter is_deleted or apply hard delete depending policy.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 25: Consumer wants near-real-time

Recommended direction:

```text
Use streaming/micro-batch CDC with lag SLA.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 26: Consumer accepts daily

Recommended direction:

```text
CDC can land continuously but target marts may update in batch.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 27: Update timestamp unreliable

Recommended direction:

```text
Prefer log-based CDC.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 28: Source log permission unavailable

Recommended direction:

```text
Consider trigger-based CDC or snapshot diff with trade-offs.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 29: Very high update volume table

Recommended direction:

```text
Separate high-churn table and optimize current-state merging.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 30: Backfill requested for historical history table

Recommended direction:

```text
Replay raw CDC or re-snapshot plus apply logs.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct CDC design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```


## 86. Quick Reference Cards

### Card 1: CDC

Purpose:

```text
Captures source inserts, updates, and deletes.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 2: Initial snapshot

Purpose:

```text
Loads existing source rows before CDC catch-up.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 3: Source LSN

Purpose:

```text
Ordering position in source log.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 4: Offset

Purpose:

```text
Progress marker for connector/consumer.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 5: Operation

Purpose:

```text
Insert, update, delete, snapshot/read.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 6: Before image

Purpose:

```text
Record state before change.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 7: After image

Purpose:

```text
Record state after change.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 8: Tombstone

Purpose:

```text
Delete marker/null payload in some CDC systems.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 9: Raw CDC

Purpose:

```text
Immutable landed change events.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 10: Current table

Purpose:

```text
Latest non-deleted state per key.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 11: History table

Purpose:

```text
Ordered versions over time.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 12: SCD Type 2

Purpose:

```text
History table with effective intervals.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 13: Idempotent sink

Purpose:

```text
Safe replay without duplicate/corrupt target.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 14: Dedupe key

Purpose:

```text
Event uniqueness key such as table/key/LSN.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 15: Lag

Purpose:

```text
Delay from source commit to target availability.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 16: Reconciliation

Purpose:

```text
Source-target correctness comparison.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 17: Schema evolution

Purpose:

```text
Handling source structure changes.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 18: Replay

Purpose:

```text
Rebuilding target from raw CDC.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 19: Checkpoint discipline

Purpose:

```text
Commit progress only after success.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 20: Merge optimization

Purpose:

```text
Micro-batch and collapse latest per key.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```
