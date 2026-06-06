# Data Lake System Design Guide

Generated: 2026-06-06

This guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/system-design/data-lake.md
```

This guide trains the mentor and candidate on **data lake system design** for Data Engineering interviews.

The guide is interview-focused. It teaches how to design a production-grade data lake or lakehouse that is reliable, governed, scalable, cost-aware, secure, and useful for analytics, ML, and downstream data products.

Data lake design is high-ROI because Data Engineering interviews often ask:

```text
Design a data lake for clickstream analytics.
Design a data lake for raw and curated enterprise data.
Design a lakehouse architecture.
Design medallion architecture: bronze, silver, gold.
Design ingestion into a data lake from APIs, databases, files, and streams.
Design a data lake that supports batch and streaming.
Design a data lake that supports schema evolution.
Design a data lake with data quality checks.
Design a data lake with governance and access control.
Design a data lake that supports backfills and replay.
Design a data lake with Delta/Iceberg/Hudi-style tables.
Design a data lake for ML feature generation.
Design a data lake for CDC data.
Design a data lake that avoids the small files problem.
Design a data lake with partitioning and compaction.
Design a cost-optimized data lake.
Design a secure data lake for PII.
Explain data lake vs data warehouse vs lakehouse.
Explain raw, staging, curated, and mart layers.
Explain file formats, partitioning, catalog, lineage, and metadata.
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
practice/system-design/cdc-pipeline.md
practice/sql/query-optimization.md
practice/sql/deduplication.md
practice/sql/joins.md
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

The purpose of this guide is to make the candidate strong at data lake system design interviews.

The candidate should learn to answer:

```text
What is a data lake?
Why use a data lake?
How is a data lake different from a warehouse?
What is a lakehouse?
What are bronze, silver, and gold layers?
How do we ingest batch data into a lake?
How do we ingest streaming data into a lake?
How do we store raw data?
Which file format should we use?
How do we choose partitioning?
How do we avoid small files?
How do we handle schema evolution?
How do we catalog datasets?
How do we enforce governance?
How do we protect PII?
How do we support replay and backfills?
How do we handle CDC data?
How do we support analytics and ML?
How do we design data quality checks?
How do we optimize cost?
How do we monitor lake health?
How do we design access control?
How do we support lineage and discovery?
```

A candidate is interview-ready only when they can design:

```text
data lake zones
raw immutable landing
bronze/silver/gold or raw/stage/curated/mart layers
batch ingestion
stream ingestion
CDC ingestion
file format strategy
partitioning strategy
metadata/catalog layer
data quality gates
schema evolution handling
ACID/lakehouse table format strategy
compaction strategy
small files mitigation
security and governance
PII handling
lineage
observability
cost controls
backfill and replay
consumer serving patterns
```


## 2. What Interviewers Are Testing

Data lake design tests whether the candidate can design beyond storage buckets.

Interviewers evaluate:

```text
does the candidate understand lake zones?
does the candidate preserve raw data?
does the candidate know when to use Parquet/Avro/JSON/CSV?
does the candidate understand partitioning and file layout?
does the candidate know small files problem?
does the candidate understand lakehouse ACID tables?
does the candidate handle schema evolution?
does the candidate design data quality checks?
does the candidate design governance and access control?
does the candidate support replay and backfills?
does the candidate understand batch and streaming ingestion?
does the candidate handle CDC data?
does the candidate optimize query performance and cost?
does the candidate define consumers and serving layers?
does the candidate explain trade-offs clearly?
```

Weak answer:

```text
Store all data in S3 and query it with Spark.
```

Strong answer:

```text
I would design a layered data lake with immutable raw/bronze data partitioned by source and ingestion date, cleaned silver tables with typed schemas and data quality checks, curated gold tables optimized for BI and ML, a central catalog for schema/lineage/discovery, lakehouse table formats for ACID merges and time travel where needed, partitioning by business dates for query pruning, compaction jobs to avoid small files, access controls and PII masking, and monitoring for freshness, volume, schema drift, quality failures, cost, and file layout.
```

Interview line:

```text
A data lake is not just cheap storage; it needs organization, governance, quality, and operational discipline.
```


## 3. Core Mental Model

A data lake stores data at multiple trust levels.

Mental model:

```text
Sources
  databases
  APIs
  files
  streams
  SaaS
  logs
      ↓
Raw / Bronze
  immutable source-shaped data
      ↓
Silver / Staging
  typed, cleaned, deduplicated data
      ↓
Gold / Curated / Marts
  business-ready tables and aggregates
      ↓
Consumers
  BI
  data science
  ML
  warehouse
  reverse ETL
  applications
```

Control plane:

```text
catalog
schema registry
lineage
data quality
access control
monitoring
orchestration
metadata
cost controls
retention policies
```

Core interview line:

```text
I design the lake as layered storage plus metadata, quality, governance, and compute—not just object storage.
```


## 4. Data Lake Vocabulary

Important terms:

```text
Data lake:
Central storage for raw and processed data, often in object storage.

Lakehouse:
Data lake architecture with warehouse-like capabilities such as ACID transactions, schema enforcement, and time travel.

Bronze layer:
Raw or lightly processed source data.

Silver layer:
Cleaned, typed, deduplicated, standardized data.

Gold layer:
Business-ready aggregates, marts, and serving tables.

Object storage:
Cloud storage such as S3, ADLS, or GCS.

File format:
Physical format such as Parquet, ORC, Avro, JSON, CSV.

Table format:
Metadata and transaction layer such as Delta Lake, Apache Iceberg, or Apache Hudi.

Partitioning:
Splitting data into folder/table partitions for pruning and management.

Compaction:
Combining many small files into fewer larger files.

Schema evolution:
Managing source schema changes over time.

Catalog:
Metadata service for table discovery, schema, owner, and location.

Lineage:
Tracking data origin and transformations.

Data quality:
Checks for freshness, completeness, uniqueness, validity, consistency, and volume.

ACID:
Atomicity, Consistency, Isolation, Durability.

Time travel:
Querying previous table versions if table format supports it.

Retention:
Policy for how long data is stored.

Zone:
Logical area such as raw, staging, curated, sandbox, archive, or quarantine.

Quarantine:
Area for invalid or suspicious records.

PII:
Personally identifiable information.

RBAC/ABAC:
Role-based or attribute-based access control.
```


## 5. Standard Data Lake Answer Framework

Use this framework for every data lake system design interview:

```text
1. Clarify requirements.
2. Identify data sources.
3. Identify consumers.
4. Estimate scale and growth.
5. Define freshness and SLA.
6. Define lake zones/layers.
7. Design raw landing.
8. Choose file formats.
9. Choose table formats if lakehouse is needed.
10. Define partitioning and clustering strategy.
11. Define ingestion patterns:
    - batch
    - stream
    - CDC
    - API
    - files
12. Define transformation layers.
13. Define data quality gates.
14. Define schema evolution handling.
15. Define metadata catalog.
16. Define lineage and discovery.
17. Define security and governance.
18. Define PII handling.
19. Define compaction and small-file strategy.
20. Define backfill and replay.
21. Define monitoring and alerts.
22. Define cost controls.
23. Define serving patterns.
24. Explain trade-offs.
```

Short version:

```text
Requirements → Zones → Storage → Ingestion → Processing → Quality → Governance → Serving → Operations → Trade-offs
```

Strict rule:

```text
No data lake design is strong if it only says object storage and Spark without governance, quality, metadata, and file layout.
```


## 6. Scoring Rubric

Score data lake design answers from 0 to 5.

### Score 0

No meaningful architecture. Only says store files in cloud.

### Score 1

Mentions object storage and Spark but lacks zones, governance, quality, and consumers.

### Score 2

Has raw and processed zones but weak on partitioning, file formats, metadata, and operations.

### Score 3

Reasonable lake design but weak on schema evolution, security, small files, backfills, or cost.

### Score 4

Interview-ready. Covers requirements, zones, ingestion, file/table formats, partitioning, quality, catalog, governance, security, replay, monitoring, and cost.

### Score 5

Strong. Handles lakehouse ACID formats, CDC merges, streaming/batch unification, compaction, schema registry, lineage, data contracts, PII policy, retention, multi-tenant access, ML features, cross-region recovery, high-volume event data, and realistic trade-offs.

Automatic score cap below 4 if:

```text
no requirements clarification
no consumer/use-case definition
no lake zones/layers
no raw immutable data
no file format strategy
no partitioning strategy
no data quality design
no catalog/metadata design
no governance/security design
no small-file/compaction strategy
no monitoring
no cost discussion
```


## 7. Requirement Clarification Questions

Ask these before designing.

### Business and consumers

```text
What use cases should the lake support?
BI dashboards, ML, ad hoc analytics, compliance, data sharing, archival, or operational exports?
Who are the consumers?
What is the expected freshness?
What are the critical datasets?
What SLA is required?
```

### Sources

```text
What source systems feed the lake?
Databases, APIs, files, logs, SaaS, Kafka, CDC?
Is data batch, streaming, or both?
Is data structured, semi-structured, or unstructured?
Do sources change schemas often?
Are deletes and updates needed?
```

### Scale

```text
How much data per day?
How much historical data?
What is the expected growth rate?
What is the average and largest file size?
How many tables or topics?
How many users and queries?
```

### Governance

```text
Does the data contain PII?
What access controls are required?
What retention policies apply?
Do we need audit logs?
Do we need lineage?
Do we need data contracts?
```

### Operations

```text
Do we need backfills?
Do we need replay?
Do we need streaming low latency?
Do we need ACID merges?
What data quality checks are required?
What cost limits exist?
```

Interview line:

```text
I clarify use cases, sources, volume, freshness, governance, and consumers before choosing lake architecture.
```


## 8. Data Lake vs Warehouse vs Lakehouse

### Data lake

```text
Stores raw and processed data in object storage.
Flexible and scalable.
Requires governance and quality discipline.
```

### Data warehouse

```text
Structured, optimized for SQL analytics.
Strong performance and governance.
Less flexible for raw/semi-structured data at huge scale.
```

### Lakehouse

```text
Combines data lake storage with warehouse-like table management:
ACID transactions
schema enforcement
time travel
MERGE
metadata tables
```

Decision:

```text
Use a data lake for raw, diverse, large-scale data.
Use a warehouse for curated SQL analytics and BI.
Use a lakehouse when you need data lake scale plus reliable table operations.
```

Interview line:

```text
The lake is for flexible storage and processing; the warehouse is for curated analytics; the lakehouse tries to bring warehouse reliability to lake storage.
```


## 9. Reference Data Lake Architecture

Reference architecture:

```text
[Data Sources]
  OLTP DBs
  CDC streams
  APIs
  SaaS
  partner files
  clickstream/logs
  IoT/events
        ↓
[Ingestion]
  batch jobs
  file watchers
  API pullers
  Kafka/Kinesis/PubSub
  CDC connectors
        ↓
[Raw / Bronze Zone]
  immutable source-shaped data
  partitioned by source/table/ingestion_date
        ↓
[Validation and Quarantine]
  schema checks
  bad record isolation
  file checks
        ↓
[Silver Zone]
  typed
  cleaned
  deduped
  standardized
  ACID tables if needed
        ↓
[Gold Zone]
  aggregates
  facts/dimensions
  ML features
  data marts
        ↓
[Serving]
  SQL engines
  warehouse external tables
  BI
  ML notebooks
  feature store
  APIs/exports
```

Control plane:

```text
catalog
schema registry
lineage
access control
data quality
orchestration
monitoring
cost dashboards
retention policies
```

Interview line:

```text
I separate data storage into trust zones and wrap the lake with metadata, governance, and operations.
```


## 10. Medallion Architecture

Medallion architecture uses bronze, silver, and gold layers.

### Bronze

```text
raw or near-raw source data
append-only
minimal transformation
used for replay and audit
```

### Silver

```text
cleaned and conformed data
typed columns
deduplication
schema enforcement
quality checks
```

### Gold

```text
business-ready datasets
aggregates
marts
features
consumer-facing tables
```

Mapping to common terms:

```text
bronze = raw
silver = staging/cleaned/curated base
gold = marts/serving/analytics
```

Interview line:

```text
Bronze is for preservation, silver is for trust, and gold is for consumption.
```


## 11. Raw / Bronze Zone Design

### Purpose

```text
Preserve source data for replay, audit, and debugging.
```

### Mutability

```text
Usually append-only and immutable.
```

### Partitioning

```text
Commonly source/table/ingestion_date/hour.
```

### Format

```text
Can preserve original format, then convert to Parquet for analytical raw if needed.
```

### Metadata

```text
Add source, batch_id, ingested_at, schema_version, file_name, checksum.
```

### Access

```text
Restrict strongly because raw may contain sensitive data.
```

Interview line:

```text
Each lake zone should have a clear purpose, access policy, retention rule, and quality expectation.
```


## 12. Silver Zone Design

### Purpose

```text
Clean, type, dedupe, and standardize raw data.
```

### Schema

```text
Enforce expected column names and data types.
```

### Quality

```text
Run required-field, uniqueness, validity, and volume checks.
```

### Table format

```text
Use Delta/Iceberg/Hudi where MERGE, schema evolution, and time travel are needed.
```

### Partitioning

```text
Use business date or common query filter when appropriate.
```

### Consumers

```text
Silver can serve analysts but should not contain unstable raw semantics.
```

Interview line:

```text
Each lake zone should have a clear purpose, access policy, retention rule, and quality expectation.
```


## 13. Gold Zone Design

### Purpose

```text
Business-ready and consumer-optimized datasets.
```

### Examples

```text
daily revenue marts, customer 360, user_features_daily, campaign performance.
```

### Grain

```text
Every gold table must document row grain.
```

### Validation

```text
Reconcile gold metrics to silver/curated facts.
```

### Performance

```text
Pre-aggregate expensive metrics and optimize partitioning.
```

### Access

```text
Gold is usually safest layer for broader business access.
```

Interview line:

```text
Each lake zone should have a clear purpose, access policy, retention rule, and quality expectation.
```


## 14. Sandbox Zone

### Purpose

```text
Allow exploration without polluting trusted layers.
```

### Users

```text
Analysts, data scientists, experimentation.
```

### Controls

```text
Quota, retention, owner tags, access control.
```

### Risk

```text
Sandbox data must not be confused with certified datasets.
```

### Policy

```text
Auto-expire old sandbox data.
```

Interview line:

```text
Each lake zone should have a clear purpose, access policy, retention rule, and quality expectation.
```


## 15. Quarantine Zone

### Purpose

```text
Store invalid or suspicious records for investigation.
```

### Metadata

```text
error_type, error_message, source, batch_id, detected_at.
```

### Use cases

```text
schema mismatch, invalid JSON, missing required key, bad type, corrupted file.
```

### Policy

```text
Alert on critical quarantine spikes.
```

### Recovery

```text
Records can be corrected and reprocessed if needed.
```

Interview line:

```text
Each lake zone should have a clear purpose, access policy, retention rule, and quality expectation.
```


## 16. Archive Zone

### Purpose

```text
Low-cost long-term storage for old data.
```

### Data

```text
Old raw files, old partitions, audit snapshots.
```

### Access

```text
Rare and slower retrieval may be acceptable.
```

### Policy

```text
Retention based on business, legal, and cost requirements.
```

### Warning

```text
Do not archive data needed for frequent queries without consumer agreement.
```

Interview line:

```text
Each lake zone should have a clear purpose, access policy, retention rule, and quality expectation.
```


## 17. Object Storage Design

Object storage is the physical foundation for most data lakes.

Common services:

```text
Amazon S3
Azure Data Lake Storage
Google Cloud Storage
```

Design principles:

```text
use clear folder conventions
partition by source and date where useful
avoid deeply nested meaningless paths
store metadata columns in files/tables
separate raw, silver, gold, quarantine, and archive
enforce bucket/container policies
enable encryption and access logs
use lifecycle policies
```

Example layout:

```text
lake/raw/source=orders/table=orders/ingestion_date=2026-01-15/batch_id=20260115_010000/
lake/silver/table=orders/order_date=2026-01-15/
lake/gold/table=daily_revenue/report_date=2026-01-15/
lake/quarantine/source=orders/ingestion_date=2026-01-15/
```

Interview line:

```text
Folder layout should support operational management, replay, and query pruning.
```


## 18. File Format Strategy

File format choice affects cost, performance, and schema handling.

### CSV

```text
good for simple exchange
weak schema
large files
slow parsing
not ideal for repeated analytics
```

### JSON

```text
good for raw APIs and nested events
flexible schema
expensive repeated parsing
larger storage
```

### Avro

```text
good for row-oriented event/CDC data
schema evolution friendly
common in streaming systems
```

### Parquet

```text
columnar
compressed
supports predicate pushdown
best default for analytical lake tables
```

### ORC

```text
columnar
strong compression
common in Hive ecosystems
```

Default recommendation:

```text
Preserve source fidelity in raw if needed.
Use Parquet for cleaned analytical tables.
Use Avro/JSON when source or streaming schema evolution requires it.
```

Interview line:

```text
For analytics, Parquet is usually the best default because it is columnar, compressed, and query-efficient.
```


## 19. Table Format Strategy

Table formats add database-like capabilities on top of files.

Common table formats:

```text
Delta Lake
Apache Iceberg
Apache Hudi
```

Capabilities:

```text
ACID transactions
schema enforcement
schema evolution
MERGE/UPSERT support
time travel
metadata pruning
compaction support
snapshot isolation
partition evolution
```

Use table formats when:

```text
CDC merges are needed
updates/deletes are needed
concurrent readers/writers exist
schema evolution matters
time travel/replay is useful
data quality gates need atomic publish
```

Use plain files when:

```text
data is append-only
raw landing is simple
no update/delete/ACID requirement
low complexity is preferred
```

Interview line:

```text
For mutable lake tables, I prefer a lakehouse table format so MERGE, schema enforcement, and atomic commits are reliable.
```


## 20. Partitioning Strategy

Partitioning helps query pruning and operational management.

Good partition columns:

```text
ingestion_date
event_date
business_date
report_date
source_table
region if low cardinality and common filter
```

Bad partition columns:

```text
user_id with millions of values
timestamp to second
high-cardinality IDs
columns rarely filtered
```

Layer-specific partitioning:

```text
raw:
source/table/ingestion_date

silver event/fact:
event_date or business_date

gold mart:
report_date or feature_date
```

Trade-off:

```text
too few partitions = scans too much
too many partitions = metadata overhead and small files
```

Interview line:

```text
Partition by columns that are frequently filtered and moderate in cardinality.
```


## 21. Clustering / Sorting / Z-Ordering

Partitioning is not enough for all queries.

Clustering/sorting can help:

```text
user_id lookups within date partitions
join keys
high-cardinality filters not suitable for partitioning
range queries
common WHERE columns
```

Examples:

```text
partition events by event_date
cluster or sort by user_id

partition orders by order_date
cluster by customer_id or order_id
```

Trade-off:

```text
better query performance
extra write/maintenance cost
```

Interview line:

```text
I partition by broad pruning columns and cluster/sort by common high-cardinality filter or join keys.
```


## 22. Small Files Problem

Small files are a classic data lake issue.

Why it hurts:

```text
too many metadata operations
slow query planning
many tiny tasks
poor scan efficiency
higher cost
```

Causes:

```text
streaming micro-batches
over-partitioning
too many writers
small input batches
frequent CDC merges
```

Fixes:

```text
compaction jobs
optimize table commands if supported
target file size policies
batch small writes
avoid high-cardinality partitions
auto-compaction where available
```

Interview line:

```text
A production data lake needs file size management; otherwise query performance degrades even if the data model is correct.
```


## 23. Compaction Strategy

Compaction combines small files into larger files.

Design:

```text
run compaction on silver/gold tables
prioritize high-query and high-write tables
avoid compacting raw too aggressively if source fidelity matters
schedule during low-traffic windows
track file count and average file size
```

Metrics:

```text
file count per table/partition
average file size
query planning time
scan time
compaction duration
cost
```

Interview line:

```text
Compaction should be scheduled and monitored like any other production data job.
```


## 24. Schema Evolution Strategy

Data lake sources often change schemas.

Safe changes:

```text
new nullable column
new optional JSON field
new enum value if consumers tolerate it
```

Breaking changes:

```text
renamed column
removed column
data type change
new required column
semantic meaning change
```

Handling:

```text
store schema version in raw
use schema registry or contracts for important sources
allow additive changes with review
fail fast on breaking changes
quarantine invalid records
version silver/gold transformations
notify consumers
```

Interview line:

```text
Schema evolution should be controlled at silver/gold layers even if bronze accepts flexible raw data.
```


## 25. Metadata Catalog

A catalog makes the lake discoverable and governable.

Catalog metadata:

```text
table name
location
schema
owner
description
layer/zone
freshness SLA
grain
primary key
partition key
sensitivity classification
lineage
quality status
retention policy
```

Catalog benefits:

```text
discovery
access control
lineage
impact analysis
data quality visibility
governance
documentation
```

Interview line:

```text
Without a catalog, a data lake becomes a data swamp because users cannot discover or trust datasets.
```


## 26. Lineage Design

Lineage answers:

```text
Where did this dataset come from?
Which job produced it?
Which upstream sources affect it?
Which dashboards consume it?
What breaks if this column changes?
```

Lineage levels:

```text
table-level lineage
column-level lineage
job-level lineage
metric-level lineage
```

Implementation:

```text
orchestrator metadata
transformation framework metadata
catalog integration
manual metadata for critical datasets
query log analysis
```

Interview line:

```text
Lineage reduces operational risk by showing upstream and downstream dependencies.
```


## 27. Batch Ingestion into Data Lake

Batch ingestion patterns:

```text
database extract
API pull
partner file delivery
SaaS export
scheduled export from warehouse
```

Batch ingestion design:

```text
extract data
land raw files immutably
record batch metadata
validate file/schema/row count
convert to silver typed format
write idempotently
update audit/watermark after success
```

Audit metadata:

```text
batch_id
source
table
ingestion_date
records_read
records_written
file_count
status
started_at
completed_at
schema_version
```

Interview line:

```text
Batch ingestion into a lake should be auditable and rerunnable.
```


## 28. Streaming Ingestion into Data Lake

Streaming ingestion patterns:

```text
Kafka/Kinesis/PubSub to raw events
micro-batch writes to bronze
streaming table writes to lakehouse format
```

Streaming concerns:

```text
checkpointing
exactly-once-like writes
late events
watermarks
small files
schema evolution
backpressure
consumer lag
```

Design:

```text
stream source
write raw bronze append-only
checkpoint stream offsets
clean into silver with watermarks
compact small files
build gold aggregates in micro-batch or batch
```

Interview line:

```text
Streaming into a lake must handle checkpoints, late data, and small files carefully.
```


## 29. CDC Ingestion into Data Lake

CDC is common in lakehouse architectures.

Flow:

```text
source database log
CDC connector
raw CDC bronze
normalized silver CDC
current-state lakehouse table
history table if needed
gold marts
```

Key requirements:

```text
operation type
before/after payloads
source sequence/LSN
delete/tombstone handling
idempotent MERGE
raw replay
schema evolution
lag monitoring
```

Interview line:

```text
CDC in a lake usually requires a table format that supports MERGE and transactional updates.
```


## 30. API Ingestion into Data Lake

API ingestion challenges:

```text
pagination
rate limits
token refresh
schema drift
partial failures
duplicate responses
cursor state
```

Design:

```text
pull API pages with retry/backoff
store raw JSON responses with request metadata
parse into silver typed tables
dedupe by source object ID
track cursor/watermark after successful load
quarantine invalid responses
```

Raw metadata:

```text
endpoint
request_params
page_number
cursor
status_code
response_time_ms
batch_id
ingested_at
```

Interview line:

```text
For APIs, raw response storage and cursor discipline are critical for recovery.
```


## 31. File Ingestion into Data Lake

File ingestion challenges:

```text
missing files
duplicate files
partial uploads
bad schema
wrong delimiter
corrupted files
late files
```

Design:

```text
file arrival detector
file audit table
checksum validation
manifest validation if available
raw immutable copy
schema validation
parse to silver
quarantine bad records
mark file processed
```

File audit columns:

```text
file_name
file_path
source_system
business_date
file_size
checksum
row_count
status
processed_at
batch_id
```

Interview line:

```text
File-based lake ingestion should be controlled by file audit and manifest validation.
```


## 32. Ingestion Idempotency

Ingestion must be rerunnable.

Patterns:

```text
raw path includes batch_id
file audit prevents duplicate processing
source cursor advances only after success
stream checkpoint commits after successful write
CDC offset commits after successful sink
partition overwrite for reprocessed data
MERGE by source key for mutable tables
```

Bad:

```text
append same file repeatedly without audit
```

Interview line:

```text
Idempotency starts at ingestion; duplicates at raw or silver layers create downstream trust problems.
```


## 33. Replay and Backfills

Data lake should support replay.

Replay sources:

```text
raw bronze data
raw CDC logs
archived files
source snapshots
```

Backfill design:

```text
parameterize date/source/table range
read raw data
recompute silver/gold outputs
write to temp or overwrite affected partitions
run DQ checks
promote output
record backfill metadata
```

Interview line:

```text
Raw immutable data exists so historical transformations can be replayed safely.
```


## 34. Late-Arriving Data

Late data examples:

```text
mobile events uploaded late
partner files delayed
source timezone mismatch
CDC lag
IoT offline devices
```

Handling:

```text
store ingestion_date and event_date separately
use lookback windows
overwrite affected event_date partitions
track late-arrival rate
define closed-period policy for finance
```

Interview line:

```text
The lake should separate ingestion time from event/business time so late data can be corrected safely.
```


## 35. Data Quality in the Lake

Quality checks by layer:

### Bronze

```text
file arrived
schema readable
record count non-zero
raw parse success
```

### Silver

```text
required fields not null
valid types
dedupe keys
accepted values
referential checks where possible
```

### Gold

```text
metric reconciliation
one row per grain
freshness SLA
aggregate totals match silver
consumer-specific checks
```

Interview line:

```text
Data quality expectations should become stricter as data moves from bronze to silver to gold.
```


## 36. Data Quality Gates

Quality gates decide whether data can move forward.

Gate examples:

```text
bronze to silver:
schema parse and required raw metadata

silver to gold:
business key uniqueness, null checks, valid values

gold publish:
metric reconciliation, row count threshold, freshness
```

Severity:

```text
critical:
block publish

warning:
publish with visible alert

info:
log and trend
```

Interview line:

```text
Quality gates prevent bad raw data from becoming trusted business output.
```


## 37. Data Governance

- define data owners
- classify data by sensitivity
- enforce access policies
- document datasets
- track lineage
- define retention
- manage schema contracts
- certify trusted datasets
- separate sandbox from production zones

Interview line:

```text
A governed data lake prevents the lake from becoming an untrusted data swamp.
```


## 38. Access Control

- restrict raw data access
- use role-based access for zones
- use column-level masking for PII
- use row-level filters where needed
- use service identities for pipelines
- audit data access
- separate dev/staging/prod environments

Interview line:

```text
A governed data lake prevents the lake from becoming an untrusted data swamp.
```


## 39. PII Handling

- classify PII fields
- mask/tokenize PII in silver/gold when possible
- restrict raw access
- avoid logging sensitive payloads
- encrypt data at rest and in transit
- support deletion/retention policies
- audit access to sensitive datasets

Interview line:

```text
A governed data lake prevents the lake from becoming an untrusted data swamp.
```


## 40. Retention Policy

- raw retention depends on audit/replay needs
- silver/gold retention depends on consumers
- sandbox data should expire automatically
- quarantine data should have investigation and expiry policy
- archive cold data to lower-cost tiers
- privacy/legal retention overrides convenience

Interview line:

```text
A governed data lake prevents the lake from becoming an untrusted data swamp.
```


## 41. Data Contracts

- source schema
- data types
- primary keys
- update/delete semantics
- freshness expectations
- allowed enum values
- ownership
- evolution rules
- breaking change process

Interview line:

```text
A governed data lake prevents the lake from becoming an untrusted data swamp.
```


## 42. Data Discovery

- catalog search
- table descriptions
- column definitions
- owners
- sample queries
- freshness status
- quality score
- lineage graph
- certified dataset labels

Interview line:

```text
A governed data lake prevents the lake from becoming an untrusted data swamp.
```


## 43. Certified Datasets

- gold tables can be marked certified after checks
- certified tables need owner and SLA
- definition must be documented
- quality checks must pass
- lineage should be visible
- consumers should prefer certified tables over raw exploration data

Interview line:

```text
A governed data lake prevents the lake from becoming an untrusted data swamp.
```


## 44. Multi-Tenant Lake Design

- separate zones by environment and domain
- domain-level ownership
- common platform standards
- central catalog and governance
- shared quality framework
- cost attribution by domain/team
- quota and lifecycle policies

Interview line:

```text
A governed data lake prevents the lake from becoming an untrusted data swamp.
```


## 45. Observability

Lake observability includes:

```text
ingestion success
freshness by table
file count by partition
average file size
schema drift
DQ results
row count trends
null rate trends
duplicate rate
cost by table/job/team
query performance
compaction status
access audit events
```

Interview line:

```text
I monitor both pipeline health and lake storage health, including file layout and quality trends.
```


## 46. Alerting

Alert when:

```text
expected files missing
stream lag high
CDC lag high
freshness SLA missed
critical DQ check failed
schema breaking change detected
small-file count too high
cost spike
unauthorized access attempt
gold table publish failed
```

Alert content:

```text
dataset
zone
partition/date
severity
owner
error summary
dashboard/log link
runbook link
```

Interview line:

```text
Alerts should be actionable and routed to dataset owners.
```


## 47. Cost Optimization

Cost drivers:

```text
storage growth
raw retention
query scan bytes
small files
unpartitioned queries
expensive compaction
uncontrolled sandbox usage
duplicate datasets
full refreshes
```

Cost controls:

```text
partition pruning
Parquet compression
lifecycle policies
archive cold data
compact files
incremental processing
pre-aggregate gold datasets
delete temporary data
cost attribution tags
query guardrails
```

Interview line:

```text
Data lake cost is controlled through file format, partitioning, lifecycle policy, and preventing unnecessary scans.
```


## 48. Query Performance

Improve lake query performance with:

```text
columnar formats
partition pruning
metadata pruning
clustering/sorting
compaction
statistics collection
caching if available
materialized gold tables
avoiding SELECT *
filtering by partition columns
```

Anti-patterns:

```text
querying raw JSON repeatedly
unbounded scans
high-cardinality partitioning
many tiny files
no catalog statistics
```

Interview line:

```text
Lake performance depends heavily on file layout and metadata, not just compute size.
```


## 49. Orchestration

Lake jobs need orchestration.

Typical DAG:

```text
detect source/files
land bronze
validate bronze
build silver
validate silver
build gold
validate gold
publish/certify
compact/optimize
update catalog
notify consumers
```

Tools can include:

```text
Airflow
Dagster
Prefect
Databricks Workflows
cloud-native workflows
dbt for SQL transformations
```

Interview line:

```text
The orchestrator coordinates layers, but each task must still be idempotent.
```


## 50. Disaster Recovery

Disaster recovery design:

```text
raw data replication if required
catalog backup
table metadata backup
versioned table snapshots
cross-region replication for critical data
replay procedures
documented recovery point objective
documented recovery time objective
```

Interview line:

```text
A critical data lake should have recovery plans for both files and metadata/catalog state.
```


## 51. Environment Strategy

Use separate environments:

```text
dev:
small sample data and testing

staging:
production-like validation

prod:
scheduled trusted pipelines
```

Controls:

```text
separate storage paths
separate catalogs or namespaces
separate service accounts
promotion process
CI/CD for transformations
```

Interview line:

```text
Dev and production lake data should not mix because trust and access policies differ.
```


## 52. Testing Strategy

Test data lake pipelines with:

```text
unit tests for transformations
schema compatibility tests
DQ tests
integration tests from bronze to gold
backfill tests
performance tests on large partitions
access control tests
reconciliation tests
```

Interview line:

```text
Lake pipelines require tests for code, data assumptions, and access controls.
```


## 53. Practice Case 1: Enterprise Data Lake

Prompt:

```text
Design a data lake for enterprise data lake.
```

Sources:

```text
multiple databases, APIs, SaaS, and files
```

Output:

```text
bronze/silver/gold lake with catalog
```

Strong design points:

- define domains and data owners
- land all sources in raw/bronze immutably
- clean and standardize into silver tables
- build gold marts for BI and ML
- use Parquet and lakehouse table formats where mutable tables need MERGE
- central catalog with owner, schema, lineage, and sensitivity
- data quality gates between zones
- RBAC and PII masking
- monitor freshness, DQ, cost, and file layout

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 54. Practice Case 2: Clickstream Data Lake

Prompt:

```text
Design a data lake for clickstream data lake.
```

Sources:

```text
website/app events
```

Output:

```text
fact_events, sessions, DAU marts
```

Strong design points:

- stream or batch land raw events partitioned by ingestion_date/hour
- parse and validate event schema
- dedupe by event_id
- silver events partitioned by event_date
- sessionize events
- gold user_day and session aggregates
- handle late events with lookback
- compact streaming small files
- monitor event volume, null user IDs, schema drift, late data

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 55. Practice Case 3: CDC Lakehouse

Prompt:

```text
Design a data lake for cdc lakehouse.
```

Sources:

```text
OLTP database CDC logs
```

Output:

```text
current and history lakehouse tables
```

Strong design points:

- land raw CDC in bronze with operation and source_lsn
- normalize CDC into silver staging
- use table format with MERGE for current-state tables
- handle deletes and tombstones
- build SCD history if needed
- track CDC lag and offsets
- replay from raw CDC if target rebuild is needed

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 56. Practice Case 4: ML Feature Data Lake

Prompt:

```text
Design a data lake for ml feature data lake.
```

Sources:

```text
events, orders, users, support tickets
```

Output:

```text
user_features_daily and training datasets
```

Strong design points:

- curate source facts in silver
- compute point-in-time features by feature_date
- store feature tables partitioned by feature_date
- avoid data leakage
- support historical backfills
- monitor feature freshness and distribution drift
- serve to training and optional feature store

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 57. Practice Case 5: Finance Data Lake

Prompt:

```text
Design a data lake for finance data lake.
```

Sources:

```text
payments, invoices, bank files
```

Output:

```text
audited finance lake and reconciliation marts
```

Strong design points:

- preserve raw files and extracts immutably
- strict access control and audit logs
- validate file completeness and totals
- silver standardized transactions
- gold reconciliation reports
- block publish on critical mismatches
- longer retention policy
- lineage and certification required

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 58. Practice Case 6: IoT Data Lake

Prompt:

```text
Design a data lake for iot data lake.
```

Sources:

```text
sensor and device events
```

Output:

```text
device telemetry lake
```

Strong design points:

- stream raw telemetry to bronze
- partition by ingestion_date and device/event date
- handle late/offline device uploads
- validate device_id and payload schema
- silver typed telemetry
- gold aggregates by device/time window
- archive cold high-volume raw data
- monitor volume spikes and malformed records

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 59. Practice Case 7: Partner File Data Lake

Prompt:

```text
Design a data lake for partner file data lake.
```

Sources:

```text
daily partner files
```

Output:

```text
trusted partner datasets
```

Strong design points:

- file audit table with checksum and manifest
- raw immutable file copy
- schema and row-level validation
- quarantine bad records
- silver typed partner records
- gold business marts
- late/missing file alerts
- reprocess by file_id or business_date

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 60. Practice Case 8: Streaming Lakehouse

Prompt:

```text
Design a data lake for streaming lakehouse.
```

Sources:

```text
Kafka/Kinesis/PubSub streams
```

Output:

```text
bronze streams and silver/gold tables
```

Strong design points:

- write raw stream to bronze with checkpoints
- handle watermarks and late data
- small-file compaction
- silver transformations with schema enforcement
- gold aggregates in micro-batch or batch
- monitor stream lag and checkpoint progress

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 61. Practice Case 9: Research / Data Science Lake

Prompt:

```text
Design a data lake for research / data science lake.
```

Sources:

```text
raw datasets and curated features
```

Output:

```text
sandbox and certified ML datasets
```

Strong design points:

- provide sandbox zone with quotas and expiry
- certified curated datasets for reuse
- feature tables with point-in-time correctness
- catalog and sample notebooks
- PII restrictions
- cost attribution by user/team
- promotion path from experiment to production

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 62. Practice Case 10: Data Lake to Warehouse Serving

Prompt:

```text
Design a data lake for data lake to warehouse serving.
```

Sources:

```text
lake silver/gold tables
```

Output:

```text
warehouse external/internal tables
```

Strong design points:

- store large raw/semi-structured data in lake
- publish curated gold tables to warehouse or external tables
- pre-aggregate high-demand metrics
- manage freshness SLA
- reconcile warehouse marts to lake source
- govern access consistently

Minimum interview answer must include:

```text
requirements
zones/layers
storage formats
partitioning
ingestion
quality
catalog/governance
security
monitoring
cost
trade-offs
```

Interview line:

```text
Tie the lake architecture to the consumers and the trust level of each data layer.
```


## 63. Lakehouse ACID Design

Lakehouse table formats provide ACID-like behavior on object storage.

Use cases:

```text
CDC MERGE
updates and deletes
atomic gold publishes
time travel
schema evolution
concurrent reads/writes
```

Design:

```text
bronze raw may be append-only files
silver/gold mutable tables use Delta/Iceberg/Hudi
commit metadata stored in table log/catalog
compaction and vacuum managed carefully
```

Interview line:

```text
If the lake needs updates, deletes, or reliable concurrent writes, I use a lakehouse table format.
```


## 64. Data Lake Anti-Patterns

Avoid:

```text
dumping all files in one bucket with no zones
no catalog
no owners
no data quality
raw JSON queried by dashboards
no partitioning
over-partitioning by user_id
many tiny files
manual access grants everywhere
PII exposed in raw
no retention policy
no backfill/replay plan
no certified datasets
no monitoring
```

Interview line:

```text
A lake without structure, metadata, quality, and governance becomes a data swamp.
```


## 65. Batch and Streaming Unification

A data lake can support both batch and streaming.

Pattern:

```text
streaming writes raw bronze
batch processes silver/gold
or streaming builds silver and batch builds gold
```

Key concerns:

```text
consistent schema
checkpointing
late data
small files
idempotent writes
consumer freshness expectations
```

Interview line:

```text
Batch and streaming can share the same lake layers if schemas, checkpoints, and file layout are managed carefully.
```


## 66. Data Product Thinking

A strong data lake exposes data products, not random files.

Data product includes:

```text
owner
description
schema
SLA
quality checks
access policy
lineage
sample queries
support channel
```

Interview line:

```text
Certified gold datasets should be treated as data products with ownership and SLAs.
```


## 67. Domain-Oriented Data Lake

For large organizations, organize by domains.

Examples:

```text
sales
marketing
finance
product
support
risk
operations
```

Design:

```text
central platform standards
domain-owned data products
shared catalog
shared governance
cost attribution by domain
common DQ framework
```

Interview line:

```text
A domain-oriented lake scales ownership while keeping platform governance centralized.
```


## 68. Open Table Format Trade-Offs

Delta, Iceberg, and Hudi all provide lakehouse features, but differ.

Interview-safe comparison:

```text
all can support ACID-like table operations
all can improve metadata management
all can support updates/deletes in lake workloads
specific choice depends on platform, engine support, team skills, and ecosystem
```

Do not overclaim in interviews.

Interview line:

```text
I choose the table format based on engine compatibility, operations, and required features like MERGE, time travel, and schema evolution.
```


## 69. Data Retention and Lifecycle

Retention design:

```text
raw:
retain based on replay/audit needs

silver:
retain based on operational and analytical needs

gold:
retain based on reporting needs

sandbox:
short expiry

quarantine:
expire after investigation window

archive:
move cold data to lower-cost storage
```

Interview line:

```text
Retention must balance cost, replay needs, analytics, and legal requirements.
```


## 70. Lake Cost Attribution

Cost attribution helps prevent uncontrolled spending.

Track by:

```text
team/domain
pipeline
table
query engine
storage path
environment
```

Controls:

```text
tags
budgets
alerts
quotas
sandbox expiry
query limits
storage lifecycle policies
```

Interview line:

```text
Without cost attribution, lake storage and query costs become hard to control.
```


## 71. Pattern Classification Drill

### Raw files must be replayable

```text
Bronze/raw immutable zone.
```

### Dashboards query raw JSON slowly

```text
Build gold marts from silver tables.
```

### Many tiny files in event table

```text
Compaction and write-size tuning.
```

### Need updates/deletes in lake table

```text
Use lakehouse table format.
```

### Source adds optional column

```text
Safe additive schema evolution.
```

### Source changes amount from number to string

```text
Breaking schema change.
```

### Users cannot find datasets

```text
Catalog and documentation problem.
```

### PII visible to analysts

```text
Access control and masking problem.
```

### Late mobile events affect yesterday

```text
Use event_date partitions and lookback.
```

### Partner file uploaded twice

```text
File audit and checksum.
```

### Cost spike from full scans

```text
Partition pruning and query guardrails.
```

### ML features use future data

```text
Point-in-time feature logic.
```

### No owner for table

```text
Governance/catalog ownership issue.
```

### Raw and curated mixed together

```text
Zone separation problem.
```

### High-cardinality partitions by user_id

```text
Over-partitioning.
```

### Need build current table from CDC

```text
Lakehouse MERGE with CDC operation handling.
```

### Need audit historical versions

```text
History/SCD table.
```

### Sandbox grows forever

```text
Lifecycle expiry and quotas.
```

### Gold metric does not match silver

```text
Reconciliation/data quality failure.
```

### Catalog metadata lost

```text
Metadata backup/DR issue.
```


## 72. High-ROI Data Lake Topics

### zones

```text
bronze/silver/gold or raw/stage/gold
```

### raw immutability

```text
replay and audit
```

### file formats

```text
Parquet for analytics
```

### table formats

```text
Delta/Iceberg/Hudi for ACID/MERGE
```

### partitioning

```text
date/source based pruning
```

### small files

```text
compaction
```

### schema evolution

```text
contracts and safe changes
```

### catalog

```text
discovery and governance
```

### lineage

```text
impact analysis
```

### data quality

```text
gates by layer
```

### security

```text
PII and least privilege
```

### retention

```text
lifecycle policies
```

### streaming

```text
checkpoints and late data
```

### CDC

```text
operation and MERGE
```

### cost

```text
storage and query optimization
```

### serving

```text
BI, ML, warehouse, exports
```


## 73. Review Checklist

### Did candidate clarify use cases?

```text
Consumers drive design.
```

### Did candidate define sources and scale?

```text
Volume matters.
```

### Did candidate define lake zones?

```text
Raw/silver/gold trust layers.
```

### Did candidate preserve raw data?

```text
Replay and audit.
```

### Did candidate choose file formats?

```text
Performance and schema.
```

### Did candidate choose table formats?

```text
ACID/update needs.
```

### Did candidate define partitioning?

```text
Cost and pruning.
```

### Did candidate address small files?

```text
Production performance.
```

### Did candidate handle schema evolution?

```text
Source changes.
```

### Did candidate define data quality gates?

```text
Trust.
```

### Did candidate define catalog?

```text
Discovery.
```

### Did candidate define lineage?

```text
Impact analysis.
```

### Did candidate define access control?

```text
Security.
```

### Did candidate address PII?

```text
Governance.
```

### Did candidate support replay/backfill?

```text
Recovery.
```

### Did candidate monitor freshness and quality?

```text
Operations.
```

### Did candidate address cost?

```text
Cloud maturity.
```

### Did candidate define serving layers?

```text
Consumer usefulness.
```

### Did candidate explain trade-offs?

```text
System design maturity.
```


## 74. Weakness Repair Map

### Only says S3 and Spark

```text
Practice full lake architecture.
```

### No zones

```text
Practice medallion architecture.
```

### No file format reasoning

```text
Practice CSV/JSON/Parquet/Avro trade-offs.
```

### No partitioning

```text
Practice partition design drills.
```

### No small-file strategy

```text
Practice compaction scenarios.
```

### No catalog/governance

```text
Practice metadata and ownership.
```

### No security

```text
Practice PII and access controls.
```

### No DQ

```text
Practice quality gates by layer.
```

### No replay/backfill

```text
Practice raw replay.
```

### No cost thinking

```text
Practice lifecycle and query scan optimization.
```

### Poor communication

```text
Practice whiteboard template.
```


## 75. 7-Day Data Lake Study Plan

### Day 1

```text
Data lake vs warehouse vs lakehouse, zones, medallion architecture.
```

### Day 2

```text
Object storage, file formats, table formats, partitioning.
```

### Day 3

```text
Batch, streaming, API, file, and CDC ingestion.
```

### Day 4

```text
Data quality, schema evolution, catalog, lineage.
```

### Day 5

```text
Security, PII, governance, retention, access control.
```

### Day 6

```text
Cost, performance, small files, compaction, serving patterns.
```

### Day 7

```text
Full data lake system design mock and weakness repair.
```


## 76. 30-Day Data Lake Study Plan

### Week 1

```text
Foundation: zones, storage, formats, partitioning.
```

### Week 2

```text
Ingestion: batch, streaming, CDC, API, files.
```

### Week 3

```text
Governance: catalog, DQ, security, lineage, retention.
```

### Week 4

```text
Scale: cost, performance, lakehouse, case studies, mocks.
```


## 77. Timed Interview Protocol

### 0-5 minutes

```text
Clarify use cases, sources, scale, SLA, governance.
```

### 5-12 minutes

```text
Draw zones: sources → bronze → silver → gold → consumers.
```

### 12-22 minutes

```text
Deep dive storage formats, partitioning, table formats, ingestion.
```

### 22-32 minutes

```text
Discuss DQ, schema evolution, catalog, governance, security.
```

### 32-40 minutes

```text
Discuss performance, compaction, cost, monitoring, replay.
```

### 40-45 minutes

```text
Trade-offs and final summary.
```


## 78. Data Lake Whiteboard Template

```text
Requirements:
- use cases:
- consumers:
- sources:
- data volume:
- freshness:
- PII/security:
- retention:
- query patterns:

Architecture:
sources → ingestion → bronze/raw → validation/quarantine → silver → gold → serving

Storage:
- object storage:
- file formats:
- table formats:
- partitioning:
- compaction:

Governance:
- catalog:
- lineage:
- access control:
- data quality:
- schema evolution:
- retention:

Operations:
- orchestration:
- monitoring:
- alerts:
- cost:
- replay/backfill:
- disaster recovery:
```


## 79. Data Lake Dataset Template

```text
Dataset name:
Layer:
Owner:
Description:
Source:
Grain:
Primary key:
Partition key:
File format:
Table format:
Freshness SLA:
Retention:
Sensitivity:
DQ checks:
Lineage:
Consumers:
Sample query:
```


## 80. Data Lake DQ Checklist Template

```text
Bronze:
- file exists
- file readable
- schema captured
- row count > 0
- raw metadata present

Silver:
- required fields not null
- types valid
- duplicate keys handled
- accepted values valid
- schema contract passed

Gold:
- one row per grain
- metric totals reconcile
- freshness SLA met
- consumer-specific checks passed
- certified status updated
```


## 81. Data Lake Runbook Template

```text
Dataset:
Layer:
Owner:
SLA:
Failed job:
Affected partition:
Error:
Severity:

Steps:
1. Check ingestion status.
2. Check raw files.
3. Check schema drift.
4. Check DQ results.
5. Check compaction/file count.
6. Rerun affected partition.
7. Validate silver/gold outputs.
8. Notify consumers if SLA missed.
```


## 82. Backfill Template

```text
Backfill reason:
Source:
Layer:
Date range:
Code version:
Target tables:
Write strategy:
Validation:
Rollback:
Owner:
Status:

Steps:
1. Read raw bronze data.
2. Recompute silver.
3. Recompute dependent gold.
4. Run DQ.
5. Compare metrics.
6. Publish/swap.
7. Record metadata.
```


## 83. Mock Set 1: Data Lake Foundations

Problems:

- Explain data lake vs data warehouse vs lakehouse.
- Design bronze/silver/gold architecture.
- Choose file formats for raw and curated data.
- Choose table format for mutable lake tables.
- Explain why catalog and governance are needed.

Expected answer must include:

```text
requirements
zones
formats
partitioning
quality
catalog
security
monitoring
cost
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 84. Mock Set 2: Storage and Performance

Problems:

- Design partitioning for clickstream events.
- Fix small files problem.
- Optimize slow lake queries.
- Design compaction policy.
- Explain clustering/sorting with partitions.

Expected answer must include:

```text
requirements
zones
formats
partitioning
quality
catalog
security
monitoring
cost
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 85. Mock Set 3: Ingestion

Problems:

- Design batch ingestion from databases.
- Design API ingestion into lake.
- Design partner file ingestion.
- Design streaming ingestion.
- Design CDC ingestion into lakehouse.

Expected answer must include:

```text
requirements
zones
formats
partitioning
quality
catalog
security
monitoring
cost
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 86. Mock Set 4: Governance and Quality

Problems:

- Design data quality gates by layer.
- Design catalog metadata.
- Design PII access controls.
- Handle schema evolution.
- Design lineage and certified datasets.

Expected answer must include:

```text
requirements
zones
formats
partitioning
quality
catalog
security
monitoring
cost
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 87. Mock Set 5: Case Designs

Problems:

- Design enterprise data lake.
- Design clickstream data lake.
- Design ML feature lake.
- Design finance data lake.
- Design data lake to warehouse serving layer.

Expected answer must include:

```text
requirements
zones
formats
partitioning
quality
catalog
security
monitoring
cost
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 88. Data Lake FAQ

### FAQ 1: What is a data lake?

```text
A scalable storage architecture for raw and processed data, usually on object storage.
```

### FAQ 2: What is a lakehouse?

```text
A lake architecture with table-management features such as ACID, schema enforcement, MERGE, and time travel.
```

### FAQ 3: What are bronze, silver, and gold?

```text
Bronze is raw, silver is cleaned/trusted, gold is business-ready/serving.
```

### FAQ 4: What file format is best for analytics?

```text
Parquet is usually the best default because it is columnar and compressed.
```

### FAQ 5: When do you use JSON?

```text
Raw API or semi-structured landing, not repeated analytical querying unless transformed.
```

### FAQ 6: What causes small files?

```text
Streaming writes, over-partitioning, many writers, and frequent tiny batches.
```

### FAQ 7: How do you fix small files?

```text
Compaction, target file sizes, batching writes, and avoiding over-partitioning.
```

### FAQ 8: Why do you need a catalog?

```text
For discovery, schema, ownership, governance, lineage, and trust.
```

### FAQ 9: How do you protect PII?

```text
Restrict raw access, mask/tokenize sensitive fields, audit access, and apply least privilege.
```

### FAQ 10: How do you support backfills?

```text
Replay raw bronze data into silver/gold with idempotent partition rewrites and validation.
```


## 89. Candidate Self-Review Questions

After every data lake design, candidate should answer:

```text
1. What use cases does the lake support?
2. Who are the consumers?
3. What are the sources?
4. What is the data volume?
5. What freshness is required?
6. What are the lake zones?
7. What belongs in bronze?
8. What belongs in silver?
9. What belongs in gold?
10. What file formats are used?
11. Is a lakehouse table format needed?
12. What is the partitioning strategy?
13. How are small files handled?
14. How is schema evolution handled?
15. How is data quality enforced?
16. What catalog metadata exists?
17. How is lineage tracked?
18. How is PII protected?
19. What access controls exist?
20. What retention policies exist?
21. How are batch sources ingested?
22. How are streaming sources ingested?
23. How is CDC handled?
24. How are backfills supported?
25. How is replay supported?
26. How is cost controlled?
27. How is query performance optimized?
28. What monitoring exists?
29. What alerts exist?
30. What trade-offs were chosen?
```

If candidate cannot answer these:

```text
The data lake design is not interview-ready.
```


## 90. Final Exit Test

Candidate passes data lake system design when they can explain:

```text
1. Data lake vs warehouse vs lakehouse.
2. Medallion architecture.
3. Raw/bronze zone.
4. Silver zone.
5. Gold zone.
6. Sandbox zone.
7. Quarantine zone.
8. Archive zone.
9. Object storage layout.
10. File format strategy.
11. Table format strategy.
12. Partitioning.
13. Clustering/sorting.
14. Small files problem.
15. Compaction.
16. Schema evolution.
17. Catalog.
18. Lineage.
19. Batch ingestion.
20. Streaming ingestion.
21. CDC ingestion.
22. API ingestion.
23. File ingestion.
24. Ingestion idempotency.
25. Replay.
26. Backfills.
27. Late-arriving data.
28. Data quality by layer.
29. Quality gates.
30. Governance.
31. Access control.
32. PII handling.
33. Retention.
34. Data contracts.
35. Certified datasets.
36. Observability.
37. Alerting.
38. Cost optimization.
39. Query performance.
40. Orchestration.
41. Disaster recovery.
42. Case study: enterprise lake.
43. Case study: clickstream lake.
44. Case study: CDC lakehouse.
45. Case study: ML feature lake.
46. Trade-offs and final summary.
```

Passing standard:

```text
Average score >= 4/5.
No object-storage-only answers.
No missing zones.
No missing file/partition strategy.
No missing data quality.
No missing catalog/governance.
No missing security.
No missing small-file strategy.
No missing cost discussion.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate designs a governed, scalable, cost-aware data lake/lakehouse with clear trust layers and production operations.
```


## 91. Final Summary

Data lake system design is a core Data Engineering interview skill.

The candidate must master:

```text
data lake concepts
lakehouse concepts
medallion architecture
raw/bronze storage
silver cleaned tables
gold serving datasets
object storage
file formats
table formats
partitioning
clustering/sorting
small files
compaction
schema evolution
metadata catalog
lineage
batch ingestion
stream ingestion
CDC ingestion
API ingestion
file ingestion
idempotency
replay
backfills
late data
data quality
governance
access control
PII protection
retention
data contracts
certified datasets
observability
alerting
cost optimization
query performance
orchestration
disaster recovery
trade-offs
```

The mentor must be strict:

```text
Only says S3/Spark → not interview-ready.
No zones → not interview-ready.
No file format strategy → not interview-ready.
No partitioning → not interview-ready.
No small-file handling → not interview-ready.
No catalog/governance → not interview-ready.
No data quality → not interview-ready.
No security/PII → not interview-ready.
No backfill/replay → not interview-ready.
No cost controls → not interview-ready.
```

Final interview line:

```text
A production data lake must be organized, governed, query-efficient, secure, replayable, and trusted by consumers.
```


## 92. Additional Mini Scenario Cards

### Mini Scenario 1: Raw files mixed with curated outputs

Recommended direction:

```text
Separate lake zones with clear trust levels.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 2: Dashboard queries raw JSON and is slow

Recommended direction:

```text
Build silver typed tables and gold aggregates.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 3: Event table has millions of tiny files

Recommended direction:

```text
Run compaction and tune write batch size.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 4: Table partitioned by user_id

Recommended direction:

```text
Replace with date partition and clustering/sorting by user_id if needed.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 5: Source adds nullable column

Recommended direction:

```text
Allow additive schema evolution after validation.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 6: Source renames required column

Recommended direction:

```text
Treat as breaking contract change.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 7: Users cannot find trusted tables

Recommended direction:

```text
Add catalog, owners, descriptions, and certified labels.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 8: Analysts access raw PII

Recommended direction:

```text
Restrict raw and mask/tokenize PII in serving layers.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 9: Late events affect yesterday's metrics

Recommended direction:

```text
Use event_date partitions and lookback overwrite.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 10: Partner file processed twice

Recommended direction:

```text
Use file audit with checksum and status.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 11: Gold revenue does not match silver facts

Recommended direction:

```text
Run reconciliation and block certification.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 12: Sandbox costs keep growing

Recommended direction:

```text
Set quotas and lifecycle expiry.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 13: No one owns a failing dataset

Recommended direction:

```text
Require owner metadata in catalog.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 14: CDC lake target needs updates

Recommended direction:

```text
Use lakehouse table format with MERGE.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 15: Streaming writes produce small files

Recommended direction:

```text
Use micro-batch sizing and auto-compaction.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 16: Raw data deleted too early

Recommended direction:

```text
Retention policy broke replay; align raw retention with recovery needs.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 17: Schema drift breaks pipeline

Recommended direction:

```text
Use schema registry/contracts and quarantine breaking records.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 18: Queries scan all partitions

Recommended direction:

```text
Enforce partition filters and optimize table layout.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 19: ML training uses future data

Recommended direction:

```text
Use point-in-time feature generation by feature_date.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 20: Catalog metadata lost

Recommended direction:

```text
Back up catalog/table metadata.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 21: Unstructured files dumped without metadata

Recommended direction:

```text
Attach metadata, owner, format, retention, and classification.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 22: Gold table has no grain defined

Recommended direction:

```text
Document row grain and primary key.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 23: Data quality only runs in gold

Recommended direction:

```text
Add quality gates in bronze and silver too.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 24: Quarantine records never reviewed

Recommended direction:

```text
Add owner, SLA, and alerting for quarantine.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 25: Compaction runs during peak hours

Recommended direction:

```text
Schedule compaction off-peak and monitor cost.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 26: Archive data needed by dashboard

Recommended direction:

```text
Review consumer access before lifecycle transition.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 27: External table performance poor

Recommended direction:

```text
Use optimized columnar format, partitioning, stats, and possibly managed table.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 28: Cross-domain duplicate datasets

Recommended direction:

```text
Use catalog and data product ownership to reduce duplication.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 29: No lineage for metric

Recommended direction:

```text
Capture table/column lineage from transformations.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 30: Cost spike from ad hoc queries

Recommended direction:

```text
Use query guardrails, cost attribution, and gold marts.
```

Candidate must explain:

```text
1. What failed.
2. Why it matters.
3. Correct data lake design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```


## 93. Quick Reference Cards

### Card 1: Data lake

Purpose:

```text
Flexible object-storage-based data platform.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 2: Lakehouse

Purpose:

```text
Lake with ACID/table-management features.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 3: Bronze

Purpose:

```text
Raw or near-raw preserved data.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 4: Silver

Purpose:

```text
Cleaned, typed, deduplicated data.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 5: Gold

Purpose:

```text
Business-ready serving datasets.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 6: Parquet

Purpose:

```text
Columnar default for analytics.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 7: Avro

Purpose:

```text
Schema-friendly row format often used in streaming.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 8: Delta/Iceberg/Hudi

Purpose:

```text
Table formats for ACID, MERGE, and metadata.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 9: Partitioning

Purpose:

```text
Pruning and operational management.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 10: Compaction

Purpose:

```text
Small-file mitigation.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 11: Catalog

Purpose:

```text
Discovery, schema, owner, governance.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 12: Lineage

Purpose:

```text
Upstream/downstream traceability.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 13: Data quality gate

Purpose:

```text
Blocks or warns before promotion.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 14: Quarantine

Purpose:

```text
Bad record isolation.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 15: PII masking

Purpose:

```text
Sensitive data protection.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 16: Retention

Purpose:

```text
Lifecycle and cost policy.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 17: Certified dataset

Purpose:

```text
Trusted consumer-facing table.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 18: Replay

Purpose:

```text
Rebuild from raw data.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 19: Backfill

Purpose:

```text
Historical reprocessing.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 20: Cost attribution

Purpose:

```text
Track spend by team/table/job.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```
