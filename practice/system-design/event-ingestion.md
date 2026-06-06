# Event Ingestion System Design Guide

Generated: 2026-06-06

This guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/system-design/event-ingestion.md
```

This guide trains the mentor and candidate on **event ingestion system design** for Data Engineering interviews.

The guide is interview-focused. It teaches how to design production-grade event ingestion systems that collect, validate, transport, store, process, monitor, and serve high-volume event data from applications, websites, mobile apps, services, IoT devices, and backend systems.

Event ingestion design is high-ROI because Data Engineering interviews often ask:

```text
Design an event ingestion pipeline.
Design clickstream ingestion.
Design mobile app event ingestion.
Design a logging pipeline.
Design a Kafka-based ingestion system.
Design real-time event ingestion into a data lake.
Design event ingestion for analytics.
Design event ingestion for product metrics.
Design ingestion for IoT sensor data.
Design event schema and validation.
Design an event pipeline with exactly-once-like behavior.
Design event deduplication.
Design event ordering strategy.
Design event replay.
Design backfill for events.
Design event ingestion with late events.
Design sessionization from events.
Design event quality and monitoring.
Design a scalable ingestion system for billions of events per day.
Explain producer, broker, topic, partition, consumer, offset, checkpoint, dead-letter queue.
Explain batch vs streaming event ingestion.
Explain event time vs processing time vs ingestion time.
Explain Kafka/Kinesis/PubSub style systems at interview level.
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
practice/system-design/data-lake.md
practice/system-design/data-quality-framework.md
practice/system-design/data-warehouse.md
practice/sql/window-functions.md
practice/sql/deduplication.md
practice/sql/query-optimization.md
practice/python/api-processing.md
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

The purpose of this guide is to make the candidate strong at event ingestion system design interviews.

The candidate should learn to answer:

```text
What is event ingestion?
What is an event?
What are event producers and consumers?
How do events move from application to analytics?
How do we design event schema?
How do we validate events?
How do we handle high volume?
How do we handle spikes?
How do we partition events?
How do we deduplicate events?
How do we handle late events?
How do we handle out-of-order events?
How do we track offsets and checkpoints?
How do we store raw events?
How do we process streaming events?
How do we process batch events?
How do we support replay?
How do we design a dead-letter queue?
How do we monitor ingestion lag?
How do we protect PII?
How do we control cost?
How do we guarantee data quality?
How do we serve events to lake, warehouse, dashboards, ML, and real-time systems?
```

A candidate is interview-ready only when they can design:

```text
event producers
event schema and contracts
collection endpoints/SDKs
message broker topics
partitioning strategy
raw event storage
stream processing
batch processing
deduplication
late/out-of-order handling
schema evolution
dead-letter/quarantine flow
offset/checkpoint strategy
replay strategy
data quality checks
monitoring and alerting
scaling and backpressure
security and PII handling
cost and retention strategy
downstream serving layers
```


## 2. What Interviewers Are Testing

Event ingestion design tests whether the candidate can handle high-volume, append-heavy, time-based data.

Interviewers evaluate:

```text
does the candidate clarify event use case and SLA?
does the candidate define event schema?
does the candidate distinguish event time, ingestion time, and processing time?
does the candidate design reliable producer collection?
does the candidate understand broker topics, partitions, offsets, and consumers?
does the candidate handle duplicates?
does the candidate handle late and out-of-order events?
does the candidate design raw immutable storage?
does the candidate support replay?
does the candidate monitor lag and volume?
does the candidate handle bad events and schema drift?
does the candidate protect PII?
does the candidate scale to spikes and high throughput?
does the candidate explain batch vs streaming trade-offs?
```

Weak answer:

```text
Send events to Kafka and process with Spark.
```

Strong answer:

```text
I would define event contracts with event_id, event_name, user_id, event_time, producer metadata, and schema version. Producers send events through SDKs or backend services to a collection API, which validates lightweight schema and writes to a durable broker partitioned by event type or user_id. A raw sink writes immutable events to the data lake partitioned by ingestion time, while stream processors validate, deduplicate by event_id, handle late events with watermarks, route invalid records to a dead-letter queue, and publish silver/gold outputs to lakehouse tables, warehouse marts, and real-time consumers. I would monitor event volume, lag, malformed rate, duplicate rate, late-arrival rate, schema drift, cost, and freshness.
```

Interview line:

```text
Event ingestion is not just sending data to Kafka; it is reliable collection, validation, ordering, replay, quality, and serving.
```


## 3. Core Mental Model

Event ingestion converts many small actions into durable analytical and operational data.

Mental model:

```text
Event producers
  web apps
  mobile apps
  backend services
  IoT devices
  logs
      ↓
Collection layer
  SDKs
  APIs
  agents
  collectors
      ↓
Transport layer
  Kafka
  Kinesis
  Pub/Sub
  queues
      ↓
Raw storage
  immutable event lake
      ↓
Processing
  validation
  enrichment
  deduplication
  windowing
  aggregation
      ↓
Serving
  lake/warehouse
  dashboards
  ML features
  alerts
  real-time services
```

Operational control plane:

```text
schema registry
data quality
monitoring
alerts
dead-letter queue
replay tooling
offset/checkpoint store
access control
retention policy
cost tracking
```

Core interview line:

```text
I design event ingestion as a durable append-only flow with schema contracts, raw replay, validation, and observable downstream processing.
```


## 4. Event Ingestion Vocabulary

Important terms:

```text
Event:
A record of something that happened.

Event producer:
System or client that emits events.

Event consumer:
System that reads and processes events.

Collector:
Endpoint or agent that receives events from producers.

Broker:
Durable transport system such as Kafka, Kinesis, or Pub/Sub.

Topic:
Logical stream/category of events.

Partition:
Ordered shard within a topic.

Offset:
Position of a message in a partition.

Checkpoint:
Persisted consumer progress.

Event time:
Time the action happened.

Ingestion time:
Time the event reached the ingestion system.

Processing time:
Time the processing job handled the event.

Watermark:
Progress marker for event-time processing and late data.

Late event:
Event that arrives after expected event-time window.

Out-of-order event:
Event that arrives in a different order than event_time.

Duplicate event:
Same logical event received more than once.

Event schema:
Defined structure of an event.

Schema registry:
System to store and validate schemas.

Dead-letter queue:
Location for events that cannot be processed.

Quarantine:
Storage for invalid records with error metadata.

Backpressure:
System slows or pushes back when consumers cannot keep up.

Replay:
Rereading stored events to rebuild downstream state.

At-least-once:
Events may be delivered more than once.

At-most-once:
Events may be lost but not duplicated.

Exactly-once-like:
Final output behaves as if each event was applied once through idempotency.

Sessionization:
Grouping user events into sessions.

Windowing:
Aggregating events over time windows.

Retention:
How long events are stored in broker/lake.
```


## 5. Standard Event Ingestion Answer Framework

Use this framework for event ingestion system design:

```text
1. Clarify use case.
2. Identify event producers.
3. Identify event consumers.
4. Define event volume and spikes.
5. Define latency/freshness SLA.
6. Define event schema.
7. Define event collection layer.
8. Define transport/broker.
9. Define topic and partition strategy.
10. Define raw immutable storage.
11. Define stream/batch processing.
12. Define deduplication strategy.
13. Define ordering strategy.
14. Define late-event handling.
15. Define schema evolution.
16. Define dead-letter/quarantine handling.
17. Define offsets/checkpoints.
18. Define replay/backfill strategy.
19. Define data quality checks.
20. Define monitoring and alerts.
21. Define security and privacy.
22. Define scaling and backpressure.
23. Define retention and cost.
24. Define downstream serving.
25. Explain trade-offs.
```

Short version:

```text
Producers → Collectors → Broker → Raw storage → Processing → Serving → Operations
```

Strict rule:

```text
No event ingestion design is strong without event schema, raw storage, deduplication, late/out-of-order handling, monitoring, and replay.
```


## 6. Scoring Rubric

Score event ingestion design answers from 0 to 5.

### Score 0

No meaningful architecture. Only says Kafka.

### Score 1

Basic producer-to-broker flow but no schema, validation, storage, or operations.

### Score 2

Has broker and consumers but weak on dedupe, late events, replay, monitoring, or data quality.

### Score 3

Reasonable design but weak on partitioning, schema evolution, backpressure, security, or cost.

### Score 4

Interview-ready. Covers producers, schema, collectors, broker, partitioning, raw storage, processing, dedupe, late/out-of-order handling, DLQ, replay, DQ, monitoring, security, and trade-offs.

### Score 5

Strong. Handles billions of events, mobile offline events, schema registry, event contracts, idempotent producers/consumers, exactly-once-like sinks, watermarking, sessionization, hot partitions, multi-region ingestion, PII governance, retention tiers, replay/backfill, and real-time plus batch serving.

Automatic score cap below 4 if:

```text
no event schema
no raw event storage
no deduplication
no late-event handling
no offset/checkpoint discussion
no dead-letter/quarantine
no monitoring of lag and volume
no replay plan
no security/PII discussion
only names Kafka/Spark
```


## 7. Requirement Clarification Questions

Ask these before designing.

### Use case

```text
What events are being ingested?
Clickstream, mobile events, logs, IoT, service events, transactions, audit events?
What business problem is solved?
Analytics, monitoring, ML, alerts, personalization, reporting?
```

### Producers

```text
Who emits events?
Web browser, mobile app, backend service, IoT device, server agent?
Can producers retry?
Can producers go offline?
Can producers batch events?
Do producers have stable event IDs?
```

### Consumers

```text
Who consumes events?
Data lake, warehouse, real-time dashboard, alerting, ML features, search, operational service?
Do consumers need raw events, cleaned events, aggregates, or current state?
```

### Scale and SLA

```text
Events per second?
Events per day?
Peak traffic multiplier?
Average event size?
Retention requirement?
Latency requirement?
Allowed data loss?
Allowed duplicates?
```

### Semantics

```text
Is ordering required?
Ordering per user, device, session, or globally?
Are duplicates possible?
How late can events arrive?
What happens to invalid events?
What PII exists?
```

Interview line:

```text
I clarify producers, consumers, volume, latency, ordering, duplicates, and late-event tolerance before choosing the architecture.
```


## 8. Event Requirements

Functional requirements:

```text
collect events from producers
validate schema
durably store events
support high throughput
route events to consumers
store raw events for replay
process events into clean/aggregated datasets
handle invalid events
support replay/backfill
```

Non-functional requirements:

```text
low latency
high availability
durability
scalability
fault tolerance
idempotency
observability
privacy
cost efficiency
schema evolution
backpressure handling
```

Interview line:

```text
Event ingestion requirements must explicitly define latency, durability, duplicate tolerance, ordering, and late-arrival expectations.
```


## 9. Reference Event Ingestion Architecture

Reference architecture:

```text
[Producers]
  web SDK
  mobile SDK
  backend services
  IoT devices
  server logs
        ↓
[Collection Layer]
  event API
  load balancer
  validation
  auth/rate limit
        ↓
[Broker / Stream]
  Kafka / Kinesis / PubSub
  topics and partitions
        ↓
[Raw Sink]
  object storage / lake bronze
  immutable events
        ↓
[Processing]
  stream jobs
  batch jobs
  validation
  dedupe
  enrichment
  windowing
        ↓
[Serving]
  lakehouse silver/gold
  warehouse marts
  real-time dashboards
  ML features
  alerting
```

Control plane:

```text
schema registry
offset/checkpoint store
dead-letter queue
data quality results
monitoring dashboards
alerts
catalog
access control
cost tracking
replay tools
```

Interview line:

```text
I separate durable ingestion from processing so raw events are preserved even if downstream jobs fail.
```


## 10. Event Time vs Ingestion Time vs Processing Time

### Event time

```text
When the event actually happened.
Example: user clicked button at 10:01.
```

### Ingestion time

```text
When the event reached the ingestion system.
Example: event received by collector at 10:05.
```

### Processing time

```text
When the job processed the event.
Example: stream job processed it at 10:06.
```

Why this matters:

```text
mobile offline events may have old event_time
late events affect event-date partitions
dashboards may use event time
monitoring may use ingestion time
watermarks use event time
```

Interview line:

```text
I store event_time, ingestion_time, and processing_time separately because they answer different operational and analytical questions.
```


## 11. Event Producer Design

### Web producers

```text
Browser SDK emits user actions such as page views, clicks, impressions, and form submissions.
```

### Mobile producers

```text
Mobile SDK batches events, handles offline mode, retries later, and includes app/device metadata.
```

### Backend producers

```text
Services emit reliable server-side events for transactions, orders, payments, and audit logs.
```

### IoT producers

```text
Devices emit telemetry with device_id, event_time, sequence number, and network constraints.
```

### Log producers

```text
Agents collect application/server logs and forward them to ingestion systems.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 12. Event Collection Layer

### Purpose

```text
Receive events from many producers and durably forward them.
```

### Components

```text
Load balancer, API endpoint, auth, rate limit, lightweight validation, buffering, broker producer.
```

### Do validate

```text
Required fields, schema version, event size, authentication, basic format.
```

### Do not overdo

```text
Avoid heavy enrichment or slow joins in the collection path.
```

### Reliability

```text
Return success only after event is safely accepted or buffered.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 13. Event Schema Design

### event_id

```text
Unique identifier used for deduplication.
```

### event_name

```text
Name/type of event.
```

### event_time

```text
When the action happened.
```

### user_id

```text
Known user if available.
```

### anonymous_id

```text
Anonymous/session/device identity.
```

### session_id

```text
Session identifier if available.
```

### producer

```text
web, mobile, backend, IoT, service name.
```

### schema_version

```text
Schema version for evolution.
```

### properties

```text
Event-specific attributes.
```

### ingested_at

```text
Time collector received event.
```

### source_ip/user_agent/device

```text
Useful metadata if policy allows.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 14. Event Contract

### Purpose

```text
Define what producers must emit and consumers can rely on.
```

### Includes

```text
event names, required fields, data types, allowed values, ownership, versioning, PII classification.
```

### Benefit

```text
Prevents random event drift and broken downstream analytics.
```

### Ownership

```text
Each event type should have a producer owner and consumer owner.
```

### Evolution

```text
Add optional fields safely; breaking changes require versioning or migration.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 15. Schema Registry

### Purpose

```text
Store event schemas and validate compatibility.
```

### Supports

```text
schema versioning, compatibility checks, documentation, producer validation, consumer discovery.
```

### Formats

```text
Avro, Protobuf, JSON Schema, or custom schema registry.
```

### Rule

```text
Critical event types should be contract-driven, not free-form JSON forever.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 16. Broker / Transport Layer

### Purpose

```text
Durably buffer and distribute event streams.
```

### Examples

```text
Kafka, Kinesis, Pub/Sub, Pulsar, managed queues.
```

### Responsibilities

```text
durability, ordering within partition, fan-out to consumers, retention, replay within retention.
```

### Design choices

```text
topics, partitions/shards, replication, retention, compression, access control.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 17. Topic Design

### By domain

```text
user_events, payment_events, inventory_events.
```

### By event class

```text
clickstream, backend_logs, audit_events.
```

### By criticality

```text
critical_transaction_events separate from noisy analytics events.
```

### By schema

```text
events with compatible schemas together.
```

### Anti-pattern

```text
one topic for everything with no contract or routing.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 18. Partitioning Strategy

### By user_id

```text
Preserves per-user order and balances high-cardinality traffic.
```

### By device_id

```text
Useful for IoT/device ordering.
```

### By session_id

```text
Useful for session processing if available.
```

### By event_id hash

```text
Good distribution but no per-user ordering.
```

### By event_type

```text
Can create hot partitions if one event dominates.
```

### Rule

```text
Partition by the key whose ordering matters and has enough cardinality.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 19. Consumer Groups

### Purpose

```text
Allow multiple independent applications to consume the same topic.
```

### Examples

```text
raw sink consumer, real-time metrics consumer, ML feature consumer, alerting consumer.
```

### Scaling

```text
Consumers in same group share partitions.
```

### Caution

```text
A consumer group cannot process more parallel units than topic partitions.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 20. Offset and Checkpoint Strategy

### Offset

```text
Position of message in broker partition.
```

### Checkpoint

```text
Saved consumer progress.
```

### Safe commit

```text
Commit offset after processing and sink write succeeds.
```

### Failure behavior

```text
If failure before commit, events replay; sink must be idempotent.
```

### Monitoring

```text
Consumer lag shows how far behind processing is.
```

Interview line:

```text
The event architecture should define producers, schema, broker topics, partitions, consumers, and checkpoints clearly.
```


## 21. Delivery Semantics

Common delivery semantics:

### At-most-once

```text
Event may be lost but not duplicated.
Usually not acceptable for critical analytics.
```

### At-least-once

```text
Event may be duplicated but should not be lost.
Common default for event pipelines.
Requires deduplication/idempotent sinks.
```

### Exactly-once-like

```text
Final output behaves as if each event was applied once.
Usually achieved with idempotent writes, dedupe keys, transactions, and checkpoint discipline.
```

Interview line:

```text
For analytics ingestion, I usually assume at-least-once delivery and design deduplication/idempotent sinks.
```


## 22. Deduplication Strategy

Duplicates can happen from producer retries, network failures, broker redelivery, or consumer restarts.

Deduplication keys:

```text
event_id
producer_id + producer_sequence
device_id + event_time + event_name + sequence
topic + partition + offset for broker event identity
business key for server-side events
```

Dedup pattern:

```sql
WITH ranked_events AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY event_id
      ORDER BY ingested_at DESC
    ) AS rn
  FROM raw_events
)
SELECT *
FROM ranked_events
WHERE rn = 1;
```

Interview line:

```text
Deduplication requires a stable event identity; without event_id, dedupe becomes approximate and risky.
```


## 23. Ordering Strategy

Ordering can be global, per key, or not required.

Global ordering:

```text
expensive and rarely needed for analytics.
```

Per-user ordering:

```text
partition by user_id.
```

Per-device ordering:

```text
partition by device_id.
```

Per-entity ordering:

```text
partition by order_id, account_id, or entity key.
```

Important:

```text
Brokers usually guarantee order only within a partition.
```

Interview line:

```text
I avoid promising global ordering unless required; most event systems need ordering per user/device/entity.
```


## 24. Late Events

Late events arrive after their event-time window.

Causes:

```text
mobile offline mode
device network delay
retry after failure
batch upload
clock skew
collector outage
```

Handling:

```text
store event_time and ingestion_time
use watermarks
allow lateness window
reprocess affected event_date partitions
track late-arrival rate
define closed-period policy for reports
```

Interview line:

```text
Late events should update event-time outputs through watermarks or partition lookbacks, not be blindly assigned to ingestion date.
```


## 25. Out-of-Order Events

Out-of-order events arrive in a different order than event_time.

Handling:

```text
process by event_time where needed
buffer small windows
use watermarks
sort within session/entity window
use sequence numbers if producer provides them
design logic to tolerate reorder
```

Example:

```text
mobile app sends event A then B, but B reaches server first.
```

Interview line:

```text
Out-of-order handling depends on whether the downstream logic requires sequence correctness.
```


## 26. Watermarks

A watermark estimates that most events earlier than a time have arrived.

Use for:

```text
windowed aggregations
sessionization
late-event handling
state cleanup
```

Example:

```text
process 10-minute windows with 30-minute allowed lateness
```

Trade-off:

```text
longer lateness = more correctness but more state and delayed output
shorter lateness = faster output but more late corrections
```

Interview line:

```text
Watermarks balance result timeliness against late-event correctness.
```


## 27. Raw Event Storage

Raw storage is mandatory for replay and audit.

Design:

```text
write immutable events to object storage/data lake
partition by ingestion_date/hour
include topic, partition, offset, batch_id, schema_version
store original payload when allowed
compress and use efficient formats
```

Why raw matters:

```text
replay after processing bug
new consumers
backfills
audits
schema drift debugging
incident investigation
```

Interview line:

```text
I always preserve raw events before heavy transformations so downstream failures do not cause data loss.
```


## 28. Bronze / Silver / Gold Event Layers

Event lake layers:

### Bronze

```text
raw immutable events with minimal validation.
```

### Silver

```text
cleaned, typed, deduplicated, schema-valid events.
```

### Gold

```text
aggregates, sessions, funnels, DAU, metrics, ML features.
```

Interview line:

```text
Bronze preserves, silver trusts, and gold serves event data.
```


## 29. Stream Processing

Stream processing handles events continuously or in micro-batches.

Common tasks:

```text
schema validation
filtering
deduplication
enrichment
windowed aggregation
sessionization
alerting
feature updates
routing to sinks
```

Concerns:

```text
checkpointing
state management
watermarks
late data
backpressure
exactly-once-like sinks
monitoring lag
```

Interview line:

```text
Stream processing should be state-aware, checkpointed, and designed for replay/idempotency.
```


## 30. Batch Processing of Events

Batch processing is still common for events.

Use when:

```text
daily/hourly dashboards are enough
reprocessing large history
building gold marts
cost is more important than low latency
complex joins and backfills are needed
```

Pattern:

```text
raw events land continuously
batch job processes event_date partitions
dedupe and validate
build silver and gold outputs
overwrite affected partitions
```

Interview line:

```text
Even if ingestion is streaming, many analytical outputs can be built in batch from raw events.
```


## 31. Hybrid Streaming + Batch

Hybrid design combines fast and accurate paths.

Fast path:

```text
streaming approximate metrics for low latency.
```

Batch path:

```text
daily/hourly recomputation for accuracy and late events.
```

Use cases:

```text
real-time dashboard plus certified daily report
fraud alerts plus warehouse facts
live counters plus accurate marts
```

Interview line:

```text
A common pattern is streaming for speed and batch recomputation for correctness.
```


## 32. Dead-Letter Queue / Quarantine

Invalid events should not disappear.

DLQ stores:

```text
raw event
error type
error message
schema version
producer
topic/partition/offset
ingested_at
detected_at
rule_id
```

Use for:

```text
schema mismatch
missing required fields
invalid JSON
oversized event
unknown event type
bad timestamp
PII policy violation
```

Interview line:

```text
A DLQ makes bad events visible and recoverable instead of silently dropped.
```


## 33. Event Enrichment

Enrichment adds context to events.

Examples:

```text
geo from IP
device type from user agent
user account attributes
experiment assignment
product metadata
session information
```

Caution:

```text
heavy enrichment in the collector can hurt ingestion reliability
dimension joins may create late/missing data issues
PII policies may restrict enrichment
```

Pattern:

```text
keep collection lightweight
enrich in stream/silver processing
record enrichment version if needed
```

Interview line:

```text
I keep ingestion lightweight and perform heavier enrichment downstream where failures are recoverable.
```


## 34. Sessionization

Sessionization groups events into user sessions.

Common rule:

```text
new session after 30 minutes of inactivity
```

Needed fields:

```text
user_id or anonymous_id
event_time
event_id
event_name
```

Pattern:

```text
order events by user and event_time
use previous event timestamp
flag session break
cumulative sum break flags to assign session number
```

Interview line:

```text
Sessionization requires per-user ordering, late-event policy, and stable identity.
```


## 35. Identity Resolution

Events may have multiple identities.

Examples:

```text
anonymous_id before login
user_id after login
device_id from mobile
account_id for B2B
session_id for browsing
```

Design:

```text
store all identities in raw/silver
build identity mapping table
do not overwrite raw identities
apply identity resolution in curated/gold layer
version identity mapping if needed
```

Interview line:

```text
Identity resolution should be explicit and versioned because it changes analytics results.
```


## 36. Event Data Quality Checks

- event_id present
- event_name valid
- event_time present and reasonable
- schema_version supported
- required properties present
- payload size under limit
- duplicate event rate
- malformed event rate
- late-arrival rate
- null user_id/anonymous_id rate
- event volume by type
- producer error rate

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 37. Event Freshness Checks

- latest event ingested time
- latest event_time processed
- consumer lag
- raw sink freshness
- silver table freshness
- gold mart freshness
- dashboard freshness

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 38. Event Volume Checks

- events per minute/hour/day
- events by producer
- events by event_name
- drop/spike compared to baseline
- zero events from critical producer
- regional/app-version volume drift

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 39. Schema Evolution Checks

- schema version allowed
- required fields present
- new optional fields detected
- breaking type changes blocked
- unknown event names flagged
- compatibility checked before producer rollout

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 40. Monitoring Metrics

- broker ingress rate
- broker egress rate
- consumer lag
- collector error rate
- collector latency
- event validation failure rate
- DLQ count
- duplicate rate
- late-event rate
- processing latency
- sink write latency
- raw storage freshness
- cost by topic/consumer

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 41. Alert Conditions

- collector down
- broker unavailable
- consumer lag above threshold
- DLQ spike
- event volume drops to zero
- critical event schema breaks
- raw sink stops writing
- late-event rate spike
- duplicate rate spike
- cost spike
- PII policy violation

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 42. Backpressure Handling

- scale consumers
- increase partitions/shards
- buffer at collector if safe
- rate limit producers
- drop non-critical events only with explicit policy
- prioritize critical topics
- use compression and batching
- monitor lag and queue depth

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 43. Scaling Strategy

- horizontal collectors behind load balancer
- broker partitions/shards sized for throughput
- producer batching and compression
- consumer parallelism by partition
- separate critical and noisy event streams
- autoscale stream processing
- partition raw storage by time and event source

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 44. Retention Strategy

- broker retention for short-term replay
- raw lake retention for long-term replay/audit
- silver/gold retention by business needs
- archive cold raw data
- expire DLQ after investigation window
- apply privacy/legal retention rules

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 45. Security and Privacy

- authenticate producers
- authorize event sources
- encrypt in transit and at rest
- avoid sending unnecessary PII
- mask/tokenize sensitive fields
- restrict raw event access
- avoid logging sensitive payloads
- audit access
- support deletion policies where required

Interview line:

```text
Event ingestion must be observable across producer, broker, processing, storage, and serving layers.
```


## 46. Practice Case 1: Clickstream Event Ingestion

Prompt:

```text
Design event ingestion for clickstream event ingestion.
```

Source:

```text
web and mobile user actions
```

Goal:

```text
product analytics and dashboards
```

Strong design points:

- web/mobile SDK emits page_view, click, impression, search, add_to_cart events
- collector validates event_id, event_name, event_time, schema_version
- broker topic partitioned by user_id or anonymous_id
- raw sink stores immutable events partitioned by ingestion_date/hour
- silver job dedupes by event_id and validates schema
- gold jobs build sessions, funnels, DAU, conversion metrics
- late events handled with event_date lookback and watermarks
- monitor event volume, null identity rate, duplicate rate, late rate

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 47. Practice Case 2: Mobile Offline Event Ingestion

Prompt:

```text
Design event ingestion for mobile offline event ingestion.
```

Source:

```text
mobile app events with offline mode
```

Goal:

```text
accurate app analytics
```

Strong design points:

- SDK persists events locally when offline
- events include event_id, device_id, sequence_number, event_time
- batch upload when online
- collector handles retries and duplicate batches
- dedupe by event_id or device_id + sequence
- late events assigned to event_time partitions
- clock skew checks and correction policy
- monitor offline delay and late-arrival rate

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 48. Practice Case 3: Backend Service Event Ingestion

Prompt:

```text
Design event ingestion for backend service event ingestion.
```

Source:

```text
orders/payments/service events
```

Goal:

```text
transaction analytics and audit
```

Strong design points:

- backend emits server-side events after transaction commit
- events include business key and trace_id
- separate critical transaction topic from noisy analytics topic
- at-least-once delivery with idempotent consumers
- raw event audit retained
- warehouse fact tables built from trusted backend events
- stronger DQ and reconciliation than client events

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 49. Practice Case 4: IoT Sensor Event Ingestion

Prompt:

```text
Design event ingestion for iot sensor event ingestion.
```

Source:

```text
devices and sensors
```

Goal:

```text
telemetry analytics and alerts
```

Strong design points:

- devices emit device_id, event_time, sequence_number, readings
- collector supports high volume and unreliable networks
- partition by device_id or region/device group
- late/offline events handled with watermarks
- bad sensor readings quarantined
- hot device/region monitoring
- archive raw telemetry after retention period

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 50. Practice Case 5: Application Log Ingestion

Prompt:

```text
Design event ingestion for application log ingestion.
```

Source:

```text
service logs
```

Goal:

```text
observability and analytics
```

Strong design points:

- agents collect logs from services
- logs include service, environment, timestamp, trace_id, severity
- broker/log pipeline separates prod/non-prod
- raw logs stored with retention policy
- parse structured logs into searchable/indexed store
- aggregate error rates and latency metrics
- protect sensitive payloads

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 51. Practice Case 6: Real-Time Metrics Ingestion

Prompt:

```text
Design event ingestion for real-time metrics ingestion.
```

Source:

```text
event stream
```

Goal:

```text
live dashboard and alerts
```

Strong design points:

- stream processor computes rolling metrics
- low-latency path publishes approximate live numbers
- batch path recomputes certified metrics
- monitor processing latency and lag
- watermarks handle late events
- alerts triggered by metric thresholds

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 52. Practice Case 7: Event Ingestion to Data Lake

Prompt:

```text
Design event ingestion for event ingestion to data lake.
```

Source:

```text
multiple event topics
```

Goal:

```text
bronze/silver/gold lake tables
```

Strong design points:

- raw bronze stores topic/partition/offset metadata
- silver tables enforce event schema and dedupe
- gold tables aggregate by event_date and business dimensions
- use Parquet/lakehouse format for analytics
- compact small files
- catalog event datasets
- monitor freshness and file layout

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 53. Practice Case 8: Event Ingestion to Warehouse

Prompt:

```text
Design event ingestion for event ingestion to warehouse.
```

Source:

```text
product events
```

Goal:

```text
warehouse facts and marts
```

Strong design points:

- raw lake stores all events first
- silver event table deduped and typed
- warehouse loads fact_events partitioned by event_date
- gold marts compute DAU, sessions, funnels
- partition overwrite recent event_date for late events
- validate event counts and dashboard freshness

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 54. Practice Case 9: Fraud / Alert Event Ingestion

Prompt:

```text
Design event ingestion for fraud / alert event ingestion.
```

Source:

```text
transaction and behavior events
```

Goal:

```text
real-time alerting
```

Strong design points:

- critical events separated into priority topic
- low-latency stream processor
- enrichment with user/account risk features
- stateful rules or model scoring
- exactly-once-like alert suppression using alert_id
- DLQ for unscorable events
- monitor end-to-end latency

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 55. Practice Case 10: Experiment Analytics Event Ingestion

Prompt:

```text
Design event ingestion for experiment analytics event ingestion.
```

Source:

```text
exposure and conversion events
```

Goal:

```text
A/B test reporting
```

Strong design points:

- exposure events must include experiment_id and variant
- conversion events link by user/session
- identity resolution policy documented
- dedupe exposure events
- late conversions handled by attribution window
- gold experiment metrics built with consistent definitions
- guard against sample ratio mismatch

Minimum interview answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DQ
monitoring
replay
trade-offs
```

Interview line:

```text
Tie the event ingestion design to the producer reliability, consumer latency, and correctness requirements.
```


## 56. Hot Partitions

Hot partitions happen when one partition receives too much traffic.

Causes:

```text
partitioning by low-cardinality key
one event type dominates
one user/device/account is extremely active
bad hash distribution
```

Fixes:

```text
use higher-cardinality partition key
add salting for hot keys if ordering allows
separate noisy event types
increase partitions/shards
monitor partition-level throughput
```

Interview line:

```text
Partitioning must balance ordering needs with traffic distribution.
```


## 57. Producer Retry and Idempotency

Producer retries can create duplicates.

Design:

```text
producer generates event_id before send
collector/broker accepts retries
downstream dedupes by event_id
server-side events use business key or transaction id
mobile events include device sequence
```

Interview line:

```text
Producer retries are safe only if events have stable IDs and consumers are idempotent.
```


## 58. Clock Skew

Producer clocks can be wrong.

Issues:

```text
event_time in future
event_time too old
wrong timezone
device clock changed
```

Handling:

```text
store ingestion_time separately
validate event_time range
quarantine or correct impossible timestamps
monitor clock skew by producer/app version/device
use server time for critical server-side events
```

Interview line:

```text
Client event_time is useful but not always trustworthy, so I store ingestion_time and validate timestamp sanity.
```


## 59. Event Versioning

Events evolve over time.

Rules:

```text
add optional fields safely
avoid changing field meaning
avoid removing required fields without new version
use schema_version
support multiple versions during migration
document producer ownership
```

Interview line:

```text
Event versioning protects downstream consumers from silent producer changes.
```


## 60. PII in Events

Events often accidentally contain PII.

Controls:

```text
define allowed properties
reject disallowed PII fields
mask/tokenize sensitive fields
restrict raw access
classify event schemas
audit event access
avoid logging raw payloads in errors
```

Interview line:

```text
Event schemas should explicitly define which fields are allowed so producers do not leak PII into analytics streams.
```


## 61. Multi-Region Event Ingestion

Multi-region ingestion improves availability and latency.

Design options:

```text
regional collectors
regional broker topics
replication to central lake
active-active or active-passive routing
region metadata on events
dedupe during global merge
```

Trade-offs:

```text
lower latency and better availability
more complexity in ordering, dedupe, and governance
```

Interview line:

```text
For global apps, regional ingestion can reduce latency, but global dedupe and consistency become harder.
```


## 62. Event Replay

Replay is rereading events to rebuild downstream outputs.

Replay sources:

```text
broker retention if still available
raw event lake for long-term replay
archived events
```

Replay design:

```text
choose time range/topic/event type
read raw events
write to isolated processing job or replay topic
avoid duplicating existing sink outputs
use idempotent writes
validate outputs
record replay metadata
```

Interview line:

```text
Raw event retention is what makes long-term replay possible after broker retention expires.
```


## 63. Event Backfills

Backfills rebuild event-derived datasets.

Use cases:

```text
new metric logic
bug fix
new event consumer
identity resolution update
late historical events
schema mapping correction
```

Pattern:

```text
read raw events by event_date or ingestion_date
dedupe
apply new transformation
write to temp or overwrite affected partitions
validate metrics
publish
```

Interview line:

```text
Backfills should use raw immutable events and idempotent partition writes.
```


## 64. Exactly-Once-Like Sinks

True exactly-once across distributed systems is hard.

Practical design:

```text
at-least-once ingestion
stable event_id
dedupe in processing
idempotent sink writes
checkpoint after successful sink commit
transactional table/batch writes where available
```

Interview line:

```text
I do not rely on magic exactly-once; I design event IDs, dedupe, idempotent sinks, and checkpoint discipline.
```


## 65. Event Ingestion Anti-Patterns

Avoid:

```text
no event_id
no schema contract
free-form event properties forever
heavy processing in collector
no raw storage
no DLQ
committing offsets before sink success
partitioning by low-cardinality event type only
not tracking event_time vs ingestion_time
dropping late events silently
storing PII in raw events without controls
no lag monitoring
no replay plan
```

Interview line:

```text
Most event ingestion failures come from missing event identity, missing schema control, or missing raw replay.
```


## 66. Event Ingestion Trade-Offs

Common trade-offs:

```text
low latency vs correctness
long broker retention vs cost
strict schema validation vs producer flexibility
partition ordering vs load distribution
drop invalid events vs quarantine
streaming outputs vs batch recomputation
PII-rich events vs privacy risk
global ingestion vs regional complexity
exact dedupe vs approximate dedupe
```

Interview line:

```text
Event ingestion design is about balancing latency, durability, correctness, cost, and producer flexibility.
```


## 67. Pattern Classification Drill

### Mobile app sends same batch twice

```text
Producer retry duplicate; dedupe by event_id/device sequence.
```

### Events arrive with old event_time

```text
Late events; use event_time, watermarks, lookback.
```

### Consumer falls behind broker

```text
Consumer lag/backpressure; scale consumers or partitions.
```

### Topic has one overloaded partition

```text
Hot partition; change key or add partitions/salting.
```

### Dashboard missing yesterday's late events

```text
Partition overwrite/event-time lookback issue.
```

### Invalid JSON events appear

```text
DLQ/quarantine and producer alert.
```

### Revenue event emitted from browser only

```text
Use backend/server-side event for critical transactions.
```

### Users cannot trust event definitions

```text
Event contract/schema registry missing.
```

### Raw events deleted after 1 day

```text
Replay/backfill risk; retention too short.
```

### PII appears in event properties

```text
Schema policy and masking violation.
```

### Events processed twice after restart

```text
At-least-once replay; sink must be idempotent.
```

### Sessionization wrong due to ordering

```text
Per-user ordering and late-event handling issue.
```

### New event field breaks consumer

```text
Schema evolution compatibility issue.
```

### Real-time dashboard must be fast

```text
Stream processing fast path.
```

### Certified report must be accurate

```text
Batch recomputation/correction path.
```

### App version emits zero events

```text
Producer volume monitoring.
```

### Event_time in future

```text
Clock skew validation.
```

### DLQ grows silently

```text
DLQ monitoring and ownership missing.
```

### Broker retention exceeded during outage

```text
Need raw sink/replay or longer retention.
```

### Many tiny files in raw lake

```text
Batching/compaction strategy.
```


## 68. High-ROI Event Ingestion Topics

### event schema

```text
event_id, event_name, event_time, producer, schema_version
```

### event contract

```text
producer/consumer agreement
```

### collector

```text
API/SDK/agent ingestion
```

### broker

```text
durable transport
```

### topics

```text
logical streams
```

### partitions

```text
parallelism and ordering
```

### offsets

```text
consumer progress
```

### checkpoints

```text
safe resume
```

### dedupe

```text
stable event identity
```

### late events

```text
watermarks/lookback
```

### out-of-order

```text
event-time ordering
```

### raw storage

```text
replay and audit
```

### DLQ

```text
bad event handling
```

### monitoring

```text
lag, volume, schema, duplicates
```

### replay

```text
rebuild downstream
```

### security

```text
PII and access control
```

### cost

```text
retention, compression, compaction
```


## 69. Review Checklist

### Did candidate clarify use case and consumers?

```text
Required.
```

### Did candidate define producers?

```text
Required.
```

### Did candidate define event schema?

```text
Critical.
```

### Did candidate define collection layer?

```text
Reliability.
```

### Did candidate define broker/topic design?

```text
Transport.
```

### Did candidate define partitioning?

```text
Scale/order.
```

### Did candidate define offset/checkpoint behavior?

```text
Recovery.
```

### Did candidate handle duplicates?

```text
Correctness.
```

### Did candidate handle late events?

```text
Analytics correctness.
```

### Did candidate handle out-of-order events?

```text
Sequence correctness.
```

### Did candidate store raw events?

```text
Replay.
```

### Did candidate define DLQ/quarantine?

```text
Bad events.
```

### Did candidate define DQ checks?

```text
Trust.
```

### Did candidate monitor lag/volume?

```text
Operations.
```

### Did candidate discuss backpressure?

```text
Scale.
```

### Did candidate protect PII?

```text
Governance.
```

### Did candidate define retention/cost?

```text
Production.
```

### Did candidate explain trade-offs?

```text
System design maturity.
```


## 70. Weakness Repair Map

### Only says Kafka

```text
Practice full event architecture.
```

### No event schema

```text
Practice event contract design.
```

### No dedupe

```text
Practice event_id and idempotent sink.
```

### No late data

```text
Practice event_time/watermark scenarios.
```

### No ordering

```text
Practice partition key and per-key order.
```

### No DLQ

```text
Practice invalid event handling.
```

### No raw storage

```text
Practice replay/backfill.
```

### No monitoring

```text
Practice lag/volume/DQ metrics.
```

### No privacy

```text
Practice PII-safe schema.
```

### No scale thinking

```text
Practice partitions, backpressure, hot keys.
```

### Poor communication

```text
Practice whiteboard template.
```


## 71. 7-Day Event Ingestion Study Plan

### Day 1

```text
Event concepts, producers, schema, event time vs ingestion time.
```

### Day 2

```text
Collectors, brokers, topics, partitions, offsets, checkpoints.
```

### Day 3

```text
Deduplication, ordering, late events, watermarks.
```

### Day 4

```text
Raw storage, stream processing, batch processing, replay.
```

### Day 5

```text
DLQ, data quality, monitoring, alerts, backpressure.
```

### Day 6

```text
Security, PII, scaling, cost, retention, case studies.
```

### Day 7

```text
Full event ingestion mock and weakness repair.
```


## 72. 30-Day Event Ingestion Study Plan

### Week 1

```text
Foundation: schema, producers, collectors, brokers.
```

### Week 2

```text
Correctness: dedupe, ordering, late events, watermarks, replay.
```

### Week 3

```text
Operations: monitoring, DLQ, DQ, security, cost, scaling.
```

### Week 4

```text
Case studies and timed mocks.
```


## 73. Timed Interview Protocol

### 0-5 minutes

```text
Clarify use case, producers, consumers, SLA, volume.
```

### 5-12 minutes

```text
Draw producers → collector → broker → raw → processing → serving.
```

### 12-22 minutes

```text
Deep dive schema, partitioning, offsets, checkpoints.
```

### 22-32 minutes

```text
Deep dive dedupe, ordering, late events, DLQ, replay.
```

### 32-40 minutes

```text
Discuss monitoring, scaling, security, cost.
```

### 40-45 minutes

```text
Trade-offs and final summary.
```


## 74. Event Ingestion Whiteboard Template

```text
Requirements:
- event types:
- producers:
- consumers:
- volume:
- peak traffic:
- latency SLA:
- ordering needs:
- duplicate tolerance:
- late event tolerance:
- PII/security:

Architecture:
producers → collector/API/SDK → broker/topics/partitions → raw sink → stream/batch processing → serving

Correctness:
- schema:
- event_id:
- dedupe:
- partition key:
- offsets/checkpoints:
- late events:
- watermarks:
- DLQ:
- replay:

Operations:
- monitoring:
- alerts:
- backpressure:
- retention:
- cost:
- access control:
```


## 75. Event Schema Template

```text
event_id:
event_name:
event_time:
ingested_at:
producer:
producer_version:
schema_version:
user_id:
anonymous_id:
device_id:
session_id:
trace_id:
properties:
context:
pii_classification:
```


## 76. Event Topic Design Template

```text
topic_name:
event_domain:
event_types:
producer_owners:
consumer_groups:
partition_key:
partition_count:
retention:
schema:
PII classification:
SLA:
DLQ topic:
monitoring:
```


## 77. Event DQ Checklist Template

```text
Schema:
- event_id present
- event_name valid
- event_time valid
- schema_version supported

Quality:
- duplicate rate
- null identity rate
- malformed rate
- late event rate
- event volume baseline

Operations:
- consumer lag
- raw sink freshness
- DLQ count
- producer error rate
```


## 78. Event Replay Template

```text
Replay reason:
Event source/topic:
Date/time range:
Event types:
Raw source:
Target outputs:
Dedupe strategy:
Write strategy:
Validation:
Owner:
Status:

Steps:
1. Read raw events.
2. Validate schema.
3. Deduplicate.
4. Apply transformation.
5. Write temp/overwrite target.
6. Validate metrics.
7. Publish.
8. Record replay metadata.
```


## 79. Mock Set 1: Event Ingestion Foundation

Problems:

- Explain event time vs ingestion time vs processing time.
- Design an event schema for clickstream.
- Explain topic and partition design.
- Explain consumer offsets and checkpoints.
- Explain at-least-once vs exactly-once-like output.

Expected answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DLQ
monitoring
security
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 80. Mock Set 2: Correctness

Problems:

- Design event deduplication.
- Handle late mobile events.
- Handle out-of-order events.
- Design a DLQ for invalid events.
- Design event replay from raw storage.

Expected answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DLQ
monitoring
security
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 81. Mock Set 3: Scale and Operations

Problems:

- Scale ingestion to billions of events per day.
- Handle hot partitions.
- Handle consumer lag.
- Monitor event volume and freshness.
- Design retention and cost controls.

Expected answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DLQ
monitoring
security
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 82. Mock Set 4: Security and Quality

Problems:

- Design event schema governance.
- Prevent PII leakage in events.
- Design event DQ checks.
- Handle schema evolution.
- Design alerting for event pipeline failures.

Expected answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DLQ
monitoring
security
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 83. Mock Set 5: Case Designs

Problems:

- Design clickstream ingestion.
- Design mobile offline event ingestion.
- Design IoT event ingestion.
- Design backend service event ingestion.
- Design real-time metrics ingestion.

Expected answer must include:

```text
producers
schema
collector
broker
partitioning
raw storage
processing
dedupe
late events
DLQ
monitoring
security
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 84. Event Ingestion FAQ

### FAQ 1: What is event ingestion?

```text
Collecting events from producers and reliably moving them to storage and processing systems.
```

### FAQ 2: What is an event?

```text
A record that something happened, usually with event_id, event_name, event_time, identity, and properties.
```

### FAQ 3: Why is event_id important?

```text
It enables deduplication and idempotent processing.
```

### FAQ 4: Why store raw events?

```text
Raw events enable replay, backfills, audits, and recovery from transformation bugs.
```

### FAQ 5: What is a partition key?

```text
The key used to route events to broker partitions and preserve per-key order.
```

### FAQ 6: What is consumer lag?

```text
How far a consumer is behind the latest broker messages.
```

### FAQ 7: What is a late event?

```text
An event that arrives after its expected event-time window.
```

### FAQ 8: What is a watermark?

```text
A marker used to decide when event-time windows are mostly complete.
```

### FAQ 9: What is a DLQ?

```text
A dead-letter queue for invalid or unprocessable events.
```

### FAQ 10: What makes event ingestion strong?

```text
Schema contracts, durable broker, raw storage, dedupe, late-event handling, replay, DQ, monitoring, security, and scale.
```


## 85. Candidate Self-Review Questions

After every event ingestion design, candidate should answer:

```text
1. What events are ingested?
2. Who are the producers?
3. Who are the consumers?
4. What is the event volume?
5. What is peak traffic?
6. What is the latency SLA?
7. What is the event schema?
8. What is the event_id?
9. What identity fields exist?
10. What is the collection layer?
11. What broker is used?
12. What topics exist?
13. What is the partition key?
14. Is ordering required?
15. How are offsets/checkpoints handled?
16. How are duplicates handled?
17. How are late events handled?
18. How are out-of-order events handled?
19. How are invalid events handled?
20. Where are raw events stored?
21. How is replay supported?
22. What processing is streaming?
23. What processing is batch?
24. What data quality checks run?
25. What monitoring exists?
26. What alerts exist?
27. How is backpressure handled?
28. How is PII protected?
29. What retention/cost choices were made?
30. What trade-offs were chosen?
```

If candidate cannot answer these:

```text
The event ingestion design is not interview-ready.
```


## 86. Final Exit Test

Candidate passes event ingestion system design when they can explain:

```text
1. Event ingestion purpose.
2. Producers and consumers.
3. Event schema.
4. Event contracts.
5. Schema registry.
6. Collection layer.
7. Broker/transport layer.
8. Topic design.
9. Partitioning strategy.
10. Consumer groups.
11. Offsets and checkpoints.
12. Event time vs ingestion time vs processing time.
13. Delivery semantics.
14. Deduplication.
15. Ordering.
16. Late events.
17. Out-of-order events.
18. Watermarks.
19. Raw event storage.
20. Bronze/silver/gold event layers.
21. Stream processing.
22. Batch processing.
23. Hybrid streaming/batch.
24. DLQ/quarantine.
25. Event enrichment.
26. Sessionization.
27. Identity resolution.
28. Data quality checks.
29. Freshness and volume checks.
30. Schema evolution.
31. Monitoring metrics.
32. Alerting.
33. Backpressure.
34. Scaling.
35. Retention.
36. Security and privacy.
37. Hot partitions.
38. Producer idempotency.
39. Clock skew.
40. Replay and backfills.
41. Exactly-once-like sinks.
42. Case study: clickstream.
43. Case study: mobile offline.
44. Case study: IoT.
45. Case study: backend service events.
46. Trade-offs and final summary.
```

Passing standard:

```text
Average score >= 4/5.
No missing event schema.
No missing event_id/dedupe.
No missing raw storage.
No missing late-event handling.
No missing offset/checkpoint strategy.
No missing DLQ.
No missing monitoring.
No missing security/PII.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate designs a scalable, replayable, observable, privacy-aware event ingestion platform with clear correctness and operational trade-offs.
```


## 87. Final Summary

Event ingestion system design is a core Data Engineering interview skill.

The candidate must master:

```text
event producers
event consumers
event schema
event contracts
schema registry
collection layer
broker topics
partitioning
consumer groups
offsets
checkpoints
event time
ingestion time
processing time
delivery semantics
deduplication
ordering
late events
out-of-order events
watermarks
raw event storage
stream processing
batch processing
hybrid processing
DLQ/quarantine
event enrichment
sessionization
identity resolution
data quality
monitoring
alerting
backpressure
scaling
retention
security
PII handling
hot partitions
producer retry
clock skew
event versioning
replay
backfills
exactly-once-like sinks
trade-offs
```

The mentor must be strict:

```text
Only says Kafka → not interview-ready.
No event schema → not interview-ready.
No event_id → not interview-ready.
No deduplication → not interview-ready.
No raw storage → not interview-ready.
No late-event handling → not interview-ready.
No offset/checkpoint → not interview-ready.
No DLQ → not interview-ready.
No monitoring → not interview-ready.
No PII/security → not interview-ready.
```

Final interview line:

```text
A production event ingestion system must reliably collect events, preserve raw data, validate contracts, handle duplicates and late arrivals, support replay, and make data observable and trustworthy.
```


## 88. Additional Mini Scenario Cards

### Mini Scenario 1: Mobile sends duplicate events after retry

Recommended direction:

```text
Generate stable event_id and dedupe downstream.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 2: App goes offline and uploads next day

Recommended direction:

```text
Handle late events using event_time and lookback/watermarks.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 3: Broker consumer falls behind

Recommended direction:

```text
Monitor lag and scale consumers/partitions.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 4: One partition is overloaded

Recommended direction:

```text
Fix partition key or add salting/partitions.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 5: Invalid JSON floods pipeline

Recommended direction:

```text
Route to DLQ and alert producer owner.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 6: Dashboard uses ingestion_date instead of event_date

Recommended direction:

```text
Separate ingestion_time and event_time.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 7: Sessionization splits sessions incorrectly

Recommended direction:

```text
Use per-user ordering and late-event policy.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 8: Event schema changed without notice

Recommended direction:

```text
Use schema registry/event contracts.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 9: Raw events not stored

Recommended direction:

```text
Replay/backfill impossible after bug.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 10: PII sent in event properties

Recommended direction:

```text
Schema allowlist and masking/rejection.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 11: Offset committed before sink write

Recommended direction:

```text
Data loss risk; commit after successful write.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 12: Real-time metric differs from daily report

Recommended direction:

```text
Fast path vs batch correction trade-off.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 13: Event_time is in future

Recommended direction:

```text
Clock skew validation.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 14: DLQ is not monitored

Recommended direction:

```text
Add DLQ count alerts and ownership.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 15: Producer emits no events after release

Recommended direction:

```text
Volume check by app version/producer.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 16: Event volume spike increases cost

Recommended direction:

```text
Compression, batching, retention, autoscaling, cost alerts.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 17: Backend transaction tracked only client-side

Recommended direction:

```text
Use server-side event for critical truth.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 18: Late events update closed finance report

Recommended direction:

```text
Define closed-period/correction policy.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 19: Unknown event names appear

Recommended direction:

```text
Schema/domain validation and producer alert.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 20: Consumer processes event twice

Recommended direction:

```text
Idempotent sink by event_id.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 21: Raw lake has many small files

Recommended direction:

```text
Batch writes and compaction.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 22: Event property meaning changed

Recommended direction:

```text
Version event schema and semantic definition.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 23: User_id missing before login

Recommended direction:

```text
Store anonymous_id and identity mapping.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 24: Fraud alert duplicated

Recommended direction:

```text
Use alert_id/idempotent alert sink.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 25: IoT device sends sequence gaps

Recommended direction:

```text
Track device sequence and missing ranges.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 26: Event ingestion API overloaded

Recommended direction:

```text
Autoscale collectors and apply rate limiting/backpressure.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 27: Event retention too short

Recommended direction:

```text
Increase raw retention or archive based on replay needs.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 28: Schema validation too strict for optional field

Recommended direction:

```text
Classify safe additive change and compatibility rules.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 29: Consumer needs ordered events per account

Recommended direction:

```text
Partition by account_id if cardinality supports it.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 30: No owner for event type

Recommended direction:

```text
Event contract must include producer owner.
```

Candidate must explain:

```text
1. What failed.
2. Which event-ingestion principle applies.
3. Correct design pattern.
4. Validation or monitoring.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```


## 89. Quick Reference Cards

### Card 1: Event

Purpose:

```text
Record that something happened.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 2: Producer

Purpose:

```text
System emitting events.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 3: Collector

Purpose:

```text
Endpoint/agent receiving events.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 4: Broker

Purpose:

```text
Durable event transport.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 5: Topic

Purpose:

```text
Logical event stream.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 6: Partition

Purpose:

```text
Ordered shard for scale.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 7: Offset

Purpose:

```text
Message position.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 8: Checkpoint

Purpose:

```text
Saved consumer progress.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 9: Event time

Purpose:

```text
When event happened.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 10: Ingestion time

Purpose:

```text
When event arrived.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 11: Watermark

Purpose:

```text
Late-event progress marker.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 12: Event ID

Purpose:

```text
Deduplication key.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 13: DLQ

Purpose:

```text
Invalid event storage.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 14: Raw events

Purpose:

```text
Replay/audit storage.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 15: Deduplication

Purpose:

```text
Remove duplicate logical events.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 16: Backpressure

Purpose:

```text
Slow/scale under load.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 17: Replay

Purpose:

```text
Reprocess stored events.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 18: Schema registry

Purpose:

```text
Schema/version governance.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 19: Sessionization

Purpose:

```text
Group user activity.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 20: Hot partition

Purpose:

```text
Overloaded partition/shard.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```
