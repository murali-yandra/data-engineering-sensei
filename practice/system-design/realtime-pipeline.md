# Realtime Pipeline System Design Guide

Generated: 2026-06-06

This guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/system-design/realtime-pipeline.md
```

This guide trains the mentor and candidate on **realtime data pipeline system design** for Data Engineering interviews.

The guide is interview-focused. It teaches how to design production-grade realtime pipelines that ingest, process, enrich, aggregate, alert, and serve data with low latency, correctness, fault tolerance, observability, replayability, and cost control.

Realtime pipeline design is high-ROI because Data Engineering interviews often ask:

```text
Design a realtime analytics pipeline.
Design a streaming pipeline for clickstream metrics.
Design a realtime fraud detection pipeline.
Design a realtime alerting pipeline.
Design a realtime dashboard pipeline.
Design a streaming ETL pipeline.
Design a Kafka/Flink/Spark Streaming pipeline.
Design a pipeline with event-time windows and watermarks.
Design a pipeline that handles late events.
Design a realtime CDC pipeline.
Design a realtime feature pipeline for ML.
Design a pipeline with exactly-once-like output.
Design a streaming pipeline with deduplication.
Design a streaming pipeline with stateful processing.
Design a system that joins event streams with reference data.
Design a realtime pipeline that supports replay and backfills.
Explain batch vs streaming vs realtime.
Explain event time vs processing time.
Explain windowing, watermarking, checkpointing, and state stores.
Explain consumer lag, backpressure, and scaling.
Explain dead-letter queues and bad event handling.
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
practice/system-design/event-ingestion.md
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

The purpose of this guide is to make the candidate strong at realtime pipeline system design interviews.

The candidate should learn to answer:

```text
What is a realtime pipeline?
How is realtime different from batch and streaming?
What are producers, brokers, processors, and sinks?
What is the latency SLA?
What correctness guarantee is needed?
How do events enter the pipeline?
How are events validated?
How are events processed continuously?
How are windows and watermarks designed?
How are late events handled?
How are duplicates handled?
How is state stored and recovered?
How are offsets and checkpoints managed?
How are alerts triggered?
How are aggregates served to dashboards?
How are realtime features served to ML models?
How are sinks made idempotent?
How is replay supported?
How are bad events handled?
How is consumer lag monitored?
How is backpressure handled?
How does the pipeline scale?
How is cost controlled?
How is privacy protected?
```

A candidate is interview-ready only when they can design:

```text
event producers
collection layer
broker/topics/partitions
stream processor
state store
checkpointing
watermarks
windowing
deduplication
late-event handling
dead-letter/quarantine
raw event storage
replay path
idempotent sinks
low-latency serving layer
batch correction path
data quality checks
monitoring and alerting
scaling/backpressure strategy
security and governance
cost and retention strategy
```


## 2. What Interviewers Are Testing

Realtime pipeline design tests whether the candidate can reason about latency and correctness at the same time.

Interviewers evaluate:

```text
does the candidate clarify latency SLA?
does the candidate understand event time vs processing time?
does the candidate handle duplicates?
does the candidate handle late and out-of-order events?
does the candidate understand broker partitions and ordering?
does the candidate understand stateful stream processing?
does the candidate know checkpointing and recovery?
does the candidate design idempotent sinks?
does the candidate separate raw replay from realtime outputs?
does the candidate monitor lag, throughput, and processing latency?
does the candidate handle backpressure and spikes?
does the candidate explain trade-offs between speed, cost, and accuracy?
```

Weak answer:

```text
Use Kafka and Spark Streaming and show dashboard.
```

Strong answer:

```text
I would collect events through a validated event API, publish them to Kafka topics partitioned by user_id or entity key, persist raw events to a lake for replay, process events with a stateful stream job using event time, watermarks, deduplication by event_id, and windowed aggregations, write idempotently to a low-latency serving store for dashboards/alerts, route invalid events to a DLQ, checkpoint offsets and state after sink commits, and monitor consumer lag, processing latency, event volume, duplicate rate, late-event rate, DLQ count, and sink freshness.
```

Interview line:

```text
A realtime pipeline is not only low-latency; it must also be correct, recoverable, observable, and safe under retries.
```


## 3. Core Mental Model

A realtime pipeline continuously converts incoming events into immediate outputs.

Mental model:

```text
Producers
  apps
  services
  devices
  CDC logs
      ->
Collection / ingestion
      ->
Broker / stream
      ->
Realtime processing
  validation
  enrichment
  dedupe
  stateful joins
  windowed aggregation
  rules / scoring
      ->
Serving sinks
  realtime dashboard
  alerting system
  online feature store
  operational database
  lakehouse/warehouse
```

Supporting systems:

```text
raw event lake
schema registry
state store
checkpoint store
dead-letter queue
metadata catalog
monitoring dashboards
alerting
replay tooling
access control
cost tracking
```

Core interview line:

```text
I design realtime pipelines as low-latency dataflows with durable input, recoverable state, idempotent outputs, and strong observability.
```


## 4. Realtime Pipeline Vocabulary

Important terms:

```text
Realtime pipeline:
A pipeline that processes data continuously with low latency.

Near-realtime:
Low-latency processing, often seconds to minutes, not necessarily instant.

Streaming:
Continuous processing of unbounded data.

Micro-batch:
Processing small batches frequently, such as every few seconds or minutes.

Producer:
System that emits events.

Broker:
Durable stream transport such as Kafka, Kinesis, or Pub/Sub.

Topic:
Logical event stream.

Partition:
Ordered shard within a topic.

Consumer:
Application that reads events.

Offset:
Position in a broker partition.

Checkpoint:
Persisted progress and state.

State:
Data remembered across events, such as counts, sessions, or user history.

State store:
Storage for stream-processing state.

Event time:
Time the event happened.

Processing time:
Time the event was processed.

Ingestion time:
Time the event entered the pipeline.

Window:
Time range used for aggregation.

Watermark:
Estimate of event-time progress used for late events.

Late event:
Event that arrives after its expected window.

Out-of-order event:
Event arriving in different order than event time or sequence.

Backpressure:
Slowdown caused by downstream bottlenecks.

Consumer lag:
Amount by which consumers are behind producers.

DLQ:
Dead-letter queue for bad/unprocessable events.

Idempotent sink:
Sink that can safely receive repeated writes.

Exactly-once-like:
Final output behaves as if each event was applied once.

Replay:
Reprocessing old events from broker or raw storage.

Hot partition:
Partition receiving disproportionate traffic.

Serving store:
Low-latency database or cache used by dashboards, alerts, or online applications.
```


## 5. Standard Realtime Pipeline Answer Framework

Use this framework for every realtime pipeline system design question:

```text
1. Clarify use case.
2. Define producers.
3. Define consumers and outputs.
4. Define latency SLA.
5. Define throughput and peak traffic.
6. Define correctness requirements.
7. Define event schema and contracts.
8. Design ingestion and broker.
9. Design topics and partitioning.
10. Design raw event storage.
11. Design stream processor.
12. Define event-time, windowing, and watermarks.
13. Define state store and checkpointing.
14. Define deduplication.
15. Define late/out-of-order handling.
16. Define enrichment and joins.
17. Define serving sinks.
18. Define idempotency and delivery semantics.
19. Define DLQ/quarantine.
20. Define replay/backfill path.
21. Define data quality checks.
22. Define monitoring and alerting.
23. Define scaling and backpressure.
24. Define security and privacy.
25. Define cost and retention.
26. Explain trade-offs.
```

Short version:

```text
Use case → Events → Broker → Processor → State → Sink → Correctness → Operations → Trade-offs
```

Strict rule:

```text
No realtime design is strong without latency SLA, event schema, checkpoints, state/replay, dedupe, late-event handling, idempotent sinks, and monitoring.
```


## 6. Scoring Rubric

Score realtime pipeline answers from 0 to 5.

### Score 0

No meaningful design. Only names Kafka/Spark/Flink.

### Score 1

Basic stream flow but no correctness, state, or monitoring.

### Score 2

Has producers, broker, and processor but weak on dedupe, late data, checkpoints, replay, or sinks.

### Score 3

Reasonable architecture but weak on state store, watermarks, idempotency, backpressure, or data quality.

### Score 4

Interview-ready. Covers requirements, latency, schema, broker, partitions, processing, state, checkpoints, watermarks, dedupe, idempotent sinks, DLQ, replay, monitoring, scaling, and trade-offs.

### Score 5

Strong. Handles high-volume streams, multi-consumer fanout, state recovery, exactly-once-like sink semantics, hot partitions, dynamic scaling, late corrections, fast path plus batch correction, multi-region failover, PII governance, cost, and realistic incident recovery.

Automatic score cap below 4 if:

```text
no latency SLA
no event schema
no broker partitioning
no checkpoint/offset strategy
no state recovery
no deduplication
no late-event strategy
no idempotent sink
no replay plan
no monitoring of lag/latency
only lists tools
```


## 7. Requirement Clarification Questions

Ask these before designing.

### Business

```text
What realtime problem are we solving?
Dashboard, alerting, fraud detection, personalization, monitoring, ML features, or operational automation?
What happens if output is delayed?
What happens if output is wrong?
Is approximate output acceptable?
Is a later correction acceptable?
```

### Producers and events

```text
Who emits events?
What event types exist?
What is the event schema?
Are events client-side, server-side, CDC, or device-generated?
Do events have event_id?
Can events arrive late or out of order?
```

### Consumers and sinks

```text
Who consumes realtime output?
Dashboard, alerting system, feature store, warehouse, lake, database, API?
Do consumers need raw events, aggregates, alerts, or enriched records?
What query latency is expected?
```

### Scale

```text
Events per second?
Peak multiplier?
Average event size?
Number of topics/partitions?
State size?
Number of consumers?
Retention period?
```

### Correctness

```text
Are duplicates allowed?
Is per-user/per-entity ordering required?
How late can events arrive?
Should old windows be corrected?
What delivery guarantee is required?
What is acceptable data loss?
```

Interview line:

```text
I clarify latency, correctness, ordering, volume, and consumer requirements before choosing a realtime architecture.
```


## 8. Realtime vs Streaming vs Batch

### Batch

```text
Processes bounded data periodically.
Latency is minutes, hours, or daily.
Simpler and often cheaper.
Good for certified reports and backfills.
```

### Streaming

```text
Processes unbounded data continuously.
Can be realtime or near-realtime.
Requires checkpoints, state, and lag monitoring.
```

### Realtime

```text
Streaming with strict low-latency output requirements.
Typically seconds or sub-seconds to few minutes.
Requires careful serving and operational reliability.
```

Interview line:

```text
All realtime pipelines are streaming-like, but not all streaming pipelines need strict realtime latency.
```


## 9. Reference Realtime Pipeline Architecture

Reference architecture:

```text
[Producers]
  web/mobile/backend/CDC/IoT
        ->
[Collection Layer]
  API/SDK/agent
  auth/rate limit/light validation
        ->
[Broker]
  Kafka/Kinesis/PubSub
  topics + partitions
        ->
[Raw Sink]
  immutable event lake
        ->
[Stream Processor]
  validation
  dedupe
  enrichment
  windowing
  stateful processing
  rules/scoring
        ->
[Serving Sinks]
  dashboard store
  alerting system
  online feature store
  operational DB/cache
  lakehouse/warehouse
```

Control plane:

```text
schema registry
state store
checkpoint store
DLQ/quarantine
data quality results
monitoring dashboards
alert routing
replay tools
access control
retention/cost policies
```

Interview line:

```text
I keep raw events separate from realtime serving so failures in processing do not destroy replayability.
```


## 10. Latency Budget

A realtime pipeline should have a latency budget.

Example:

```text
producer to collector: 100 ms
collector to broker: 50 ms
broker queue delay: 200 ms
stream processing: 500 ms
sink write: 200 ms
dashboard/API read: 100 ms
total target: under 2 seconds
```

Latency components:

```text
producer batching
network latency
collector validation
broker queueing
consumer lag
processing time
state store access
sink write time
serving read time
alert dispatch time
```

Interview line:

```text
I break the realtime SLA into a latency budget across ingestion, processing, sink, and serving.
```


## 11. Producer Design

### Web/mobile producers

```text
Emit user events, may retry, may batch, may go offline.
```

### Backend producers

```text
Emit reliable server-side events after transactions commit.
```

### CDC producers

```text
Emit database changes from logs.
```

### IoT producers

```text
Emit telemetry with unreliable network and possible clock skew.
```

### Producer requirements

```text
stable event_id, event_time, schema_version, producer metadata, retry behavior.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 12. Collection Layer

### Purpose

```text
Receive events and forward them safely with minimal latency.
```

### Responsibilities

```text
auth, rate limiting, lightweight schema validation, request batching, broker writes.
```

### Avoid

```text
heavy joins, slow enrichment, expensive business logic in ingestion path.
```

### Reliability

```text
Return success only after event is safely accepted or buffered.
```

### Scaling

```text
Stateless collectors behind load balancer are easy to scale.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 13. Event Schema

### event_id

```text
Unique ID for dedupe.
```

### event_name

```text
Event type.
```

### event_time

```text
When event happened.
```

### ingested_at

```text
When event entered system.
```

### producer

```text
Source app/service/device.
```

### schema_version

```text
Schema version.
```

### entity key

```text
user_id, account_id, device_id, order_id, etc.
```

### properties

```text
Event-specific data.
```

### trace_id

```text
Debugging and request correlation.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 14. Broker Design

### Purpose

```text
Durable buffering and fanout to multiple consumers.
```

### Examples

```text
Kafka, Kinesis, Pub/Sub, Pulsar.
```

### Design choices

```text
topics, partitions/shards, retention, replication, compression, ACLs.
```

### Critical property

```text
Ordering is usually guaranteed only within a partition.
```

### Interview rule

```text
Explain topic and partition strategy, not just broker name.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 15. Topic Design

### By domain

```text
clickstream_events, payment_events, inventory_events.
```

### By criticality

```text
critical_fraud_events separate from noisy analytics events.
```

### By schema

```text
compatible event types together.
```

### By latency

```text
low-latency alert topics separate from batch analytics topics.
```

### Anti-pattern

```text
one massive topic for unrelated event types without schema control.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 16. Partitioning Strategy

### By user_id

```text
Per-user order and good distribution if cardinality is high.
```

### By account_id

```text
Good for account-level rules, but may hot-spot large accounts.
```

### By device_id

```text
Good for IoT/mobile ordering.
```

### By event_id hash

```text
Excellent distribution, weak entity ordering.
```

### By event_type

```text
Can create hot partitions if one type dominates.
```

### Rule

```text
Partition by the key whose ordering matters and has enough cardinality.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 17. Consumer Groups

### Raw sink consumer

```text
Writes immutable events to lake.
```

### Realtime metric consumer

```text
Computes dashboard metrics.
```

### Alert consumer

```text
Triggers notifications or actions.
```

### Feature consumer

```text
Updates online feature store.
```

### Warehouse/lakehouse consumer

```text
Writes cleaned stream output.
```

### Scaling rule

```text
Parallelism is bounded by partitions per consumer group.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 18. Stream Processor

### Purpose

```text
Continuously transforms and routes events.
```

### Engines

```text
Flink, Spark Structured Streaming, Kafka Streams, Beam, cloud stream processors.
```

### Common work

```text
validate, filter, dedupe, enrich, window, aggregate, join, score, alert, sink.
```

### Key design

```text
stateful processing requires state store and checkpoints.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 19. State Store

### Purpose

```text
Stores state across events.
```

### Examples

```text
window counts, session state, dedupe cache, user risk state, running aggregates.
```

### Requirements

```text
durable checkpoints, TTL, recovery, size monitoring, key distribution.
```

### Risk

```text
unbounded state grows until latency/cost breaks.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 20. Checkpointing

### Purpose

```text
Recover offsets and state after failure.
```

### Includes

```text
broker offsets, state snapshots, sink commit progress.
```

### Safe pattern

```text
write sink idempotently, then checkpoint progress.
```

### Failure behavior

```text
if checkpoint not committed, events replay; sink must tolerate duplicates.
```

### Monitoring

```text
checkpoint age, checkpoint duration, checkpoint failures.
```

Interview line:

```text
Realtime architecture must define how data moves, how state is recovered, and how outputs remain correct under retries.
```


## 21. Event Time, Processing Time, and Ingestion Time

Realtime systems must separate time concepts.

```text
event_time:
when the event happened

ingestion_time:
when the system received it

processing_time:
when the stream job processed it
```

Use cases:

```text
analytics windows usually use event_time
operational monitoring often uses ingestion_time or processing_time
latency metrics compare event_time/ingestion_time to sink time
```

Interview line:

```text
Realtime correctness usually depends on event time, while operations depend on ingestion and processing time.
```


## 22. Windowing

Windowing groups events by time.

Common windows:

### Tumbling window

```text
Fixed non-overlapping windows.
Example: count clicks every 1 minute.
```

### Sliding window

```text
Overlapping windows.
Example: last 5 minutes updated every 1 minute.
```

### Session window

```text
Dynamic window based on inactivity.
Example: user session ends after 30 minutes idle.
```

### Global window

```text
All events in one unbounded window, usually needs triggers.
```

Interview line:

```text
Window choice depends on the business question: fixed intervals, rolling metrics, or activity sessions.
```


## 23. Watermarks

Watermarks handle event-time progress.

Example:

```text
Assume most events older than event_time - 10 minutes have arrived.
```

Watermark controls:

```text
when windows close
how long state is kept
how late events are accepted
when outputs are finalized
```

Trade-off:

```text
long watermark delay = more correctness, higher latency/state
short watermark delay = faster output, more late corrections/drops
```

Interview line:

```text
Watermarks are the main trade-off between realtime speed and event-time correctness.
```


## 24. Late Events

Late events arrive after expected window progress.

Handling strategies:

```text
allowed lateness window
update previous aggregates
emit correction events
send to late-event side output
recompute batch correction later
drop only if business accepts it
```

Metrics:

```text
late event count
late event rate
lateness distribution
dropped late events
corrected windows
```

Interview line:

```text
I do not silently drop late events unless the business explicitly accepts that trade-off.
```


## 25. Out-of-Order Events

Events may arrive out of sequence.

Handling:

```text
process by event_time
partition by ordering key
use sequence numbers when available
buffer within watermark delay
design state updates to tolerate reorder
monitor disorder rate
```

Example:

```text
mobile sends add_to_cart after purchase due to offline upload order.
```

Interview line:

```text
Out-of-order events are normal in distributed systems, so stream logic should rely on event time and sequence where needed.
```


## 26. Deduplication

Duplicates happen from retries and at-least-once delivery.

Dedup keys:

```text
event_id
producer_id + sequence_number
device_id + event_time + event_name
business transaction id
topic + partition + offset for broker identity
```

Stateful dedupe:

```text
keep recent event_ids in state with TTL
drop event_id if already seen
```

Batch/lake dedupe:

```sql
ROW_NUMBER() OVER (
  PARTITION BY event_id
  ORDER BY ingested_at DESC
) = 1
```

Interview line:

```text
Realtime dedupe needs a stable event ID and bounded state TTL.
```


## 27. Stateful Aggregation

Stateful aggregation maintains running values.

Examples:

```text
clicks per minute
orders per merchant last 5 minutes
failed login count per user
revenue last 15 minutes
device readings average per 1 minute
```

Requirements:

```text
state store
keyed partitioning
checkpointing
TTL
watermark cleanup
state size monitoring
```

Interview line:

```text
Stateful realtime aggregation requires careful state TTL and recovery design.
```


## 28. Stream Joins

Stream joins combine realtime events with other data.

Types:

```text
stream-stream join
stream-static dimension join
stream-changing dimension join
stream-table join
```

Challenges:

```text
out-of-order events
late dimension updates
state size
join window selection
dimension freshness
key skew
```

Interview line:

```text
Realtime joins must define the join window, dimension freshness, and state retention strategy.
```


## 29. Enrichment

Enrichment adds context.

Examples:

```text
IP to geo
user segment
device type
experiment assignment
merchant risk score
product category
```

Strategies:

```text
cached reference data
broadcast dimension
stream-table join
external API lookup only if latency budget allows
async enrichment
```

Caution:

```text
slow external calls can break realtime latency.
```

Interview line:

```text
For realtime pipelines, enrichment should usually use cached or preloaded reference data, not slow per-event API calls.
```


## 30. Realtime Feature Computation

Realtime features are used by ML or rules.

Examples:

```text
failed_logins_last_5_min
orders_last_10_min
amount_spent_last_1_hour
distinct_devices_last_24_hours
merchant_decline_rate_last_15_min
```

Requirements:

```text
event-time logic
low-latency state
online feature store sink
idempotent updates
training-serving consistency
backfill from historical events
feature freshness monitoring
```

Interview line:

```text
Realtime features need consistency with offline training features or models will behave unpredictably.
```


## 31. Realtime Alerting

Realtime alerts trigger actions.

Examples:

```text
fraud alert
system error spike
inventory stockout
payment failure spike
security anomaly
SLA breach
```

Design:

```text
rules/model scoring
dedupe alerts by alert_id
suppress repeated alerts
route by severity
store alert history
monitor alert latency
provide explanation/context
```

Interview line:

```text
Realtime alerting must prevent duplicate/noisy alerts while still meeting low-latency requirements.
```


## 32. Idempotent Sinks

Sinks must tolerate repeated events.

Sink patterns:

```text
upsert by event_id or aggregate key
conditional update by sequence/version
transactional batch commit
dedupe table/cache
partition overwrite for correction path
alert_id to prevent duplicate alert
```

Bad:

```text
append alert or metric blindly on every retry
```

Interview line:

```text
At-least-once input is safe only when the output sink is idempotent.
```


## 33. Exactly-Once-Like Output

True exactly-once across all systems is hard.

Practical design:

```text
stable event_id
dedupe in processor
checkpoint after sink success
transactional writes where available
idempotent updates/upserts
replay-safe transformations
```

Failure scenario:

```text
sink write succeeds but checkpoint fails
events replay
idempotent sink prevents duplicate output
```

Interview line:

```text
I design exactly-once-like final results through dedupe, idempotent sinks, and checkpoint discipline.
```


## 34. Dead-Letter Queue

DLQ stores events that cannot be processed.

DLQ record includes:

```text
raw event
error type
error message
schema version
topic/partition/offset
producer
ingested_at
processing job
detected_at
```

Use for:

```text
invalid schema
missing required fields
bad timestamp
bad enum
unparseable payload
enrichment failure if unrecoverable
PII policy violation
```

Interview line:

```text
Bad events should be isolated with enough metadata to debug and reprocess if fixed.
```


## 35. Replay and Backfill

Replay reprocesses historical events.

Sources:

```text
broker retention
raw event lake
archived events
```

Replay design:

```text
choose topic/time/event range
read raw events
use same transformation code
write to isolated sink/temp table
validate output
promote or correct serving table
record replay metadata
```

Use cases:

```text
bug fix
new metric
new consumer
state recovery
model feature rebuild
late correction
```

Interview line:

```text
Realtime speed should not sacrifice the ability to replay and correct results.
```


## 36. Data Quality Checks

- event_id present
- event_name valid
- schema_version supported
- event_time valid and not impossible
- required fields present
- duplicate rate within threshold
- late-event rate within threshold
- DLQ rate within threshold
- event volume by producer/event type
- null identity rate
- sink freshness
- aggregate reconciliation with batch correction path

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 37. Monitoring Metrics

- producer event rate
- collector request latency
- collector error rate
- broker ingress/egress rate
- broker partition lag
- consumer lag
- processing latency
- watermark delay
- checkpoint duration
- checkpoint failures
- state size
- state TTL cleanup
- sink write latency
- DLQ count
- duplicate rate
- late-event rate
- cost by topic/job/sink

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 38. Alert Conditions

- consumer lag above threshold
- processing latency above SLA
- checkpoint failures
- state size growing unexpectedly
- DLQ spike
- event volume drops to zero
- event volume spike
- broker unavailable
- sink write failures
- freshness SLA miss
- watermark stuck
- cost spike

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 39. Backpressure Handling

- scale stream consumers
- increase partitions/shards
- optimize slow sink
- batch sink writes
- reduce external lookups
- apply rate limits to producers
- separate critical from non-critical streams
- drop/degrade only non-critical data with explicit policy

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 40. Scaling Strategy

- stateless collectors behind load balancer
- topics partitioned by high-cardinality key
- stream job parallelism aligned with partitions
- state sharded by key
- autoscaling based on lag and CPU
- separate hot topics
- compression and batching
- right-size serving sink

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 41. Hot Partition Handling

- detect partition-level lag/throughput
- avoid low-cardinality partition keys
- salt hot keys if ordering can be relaxed
- split high-volume tenants/accounts
- increase partitions for future growth
- separate noisy event types

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 42. State Management

- state TTL
- checkpoint state regularly
- monitor state size
- avoid unbounded keys
- use compact state representation
- separate large offline history from realtime state
- recover state from checkpoint or replay

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 43. Serving Sink Options

- low-latency key-value store for features
- OLAP store for realtime dashboards
- search/index store for logs
- warehouse/lakehouse for analytical queries
- cache for read-heavy metrics
- alerting/ticket system for actions

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 44. Security and Privacy

- authenticate producers
- authorize topics and consumers
- encrypt in transit and at rest
- classify event fields
- mask/tokenize PII
- restrict raw event access
- avoid sensitive payloads in logs/DLQ
- audit consumer access
- apply retention and deletion policy

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 45. Cost Controls

- compress broker messages
- tune retention
- archive raw events to lower-cost storage
- avoid excessive state retention
- avoid over-partitioning
- batch sink writes
- separate high-value realtime from low-value batch-only events
- monitor cost by topic and consumer

Interview line:

```text
Realtime pipelines need operational metrics for every layer: producer, broker, processor, state, sink, and consumer output.
```


## 46. Practice Case 1: Realtime Clickstream Dashboard

Prompt:

```text
Design a realtime pipeline for realtime clickstream dashboard.
```

Source:

```text
web/mobile clickstream events
```

Goal:

```text
live product analytics dashboard
```

Strong design points:

- events include event_id, user_id/anonymous_id, event_name, event_time, schema_version
- broker topic partitioned by user_id or anonymous_id
- raw event sink writes immutable events to lake
- stream job dedupes and validates events
- windowed aggregations compute page views, clicks, DAU approximations, and funnel counts
- watermark handles mobile late events
- serving store supports low-latency dashboard reads
- batch job recomputes certified metrics daily
- monitor lag, event volume, late rate, duplicate rate, dashboard freshness

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 47. Practice Case 2: Realtime Fraud Detection Pipeline

Prompt:

```text
Design a realtime pipeline for realtime fraud detection pipeline.
```

Source:

```text
payment and behavior events
```

Goal:

```text
fraud alerts and risk features
```

Strong design points:

- critical backend events emitted after transaction commit
- separate high-priority fraud topic
- partition by account_id or payment_id depending on rule ordering
- stream job enriches with cached user/account risk features
- stateful features track amount/count/device changes over rolling windows
- model/rule scoring emits fraud alerts
- alert_id prevents duplicate alerts
- online feature store updated idempotently
- monitor end-to-end alert latency and false-positive volume

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 48. Practice Case 3: Realtime Error Monitoring Pipeline

Prompt:

```text
Design a realtime pipeline for realtime error monitoring pipeline.
```

Source:

```text
application logs and metrics
```

Goal:

```text
live incident alerts
```

Strong design points:

- agents collect structured logs with service, severity, trace_id, timestamp
- broker topics separated by environment/service
- stream job validates and parses logs
- rolling windows detect error-rate spikes
- alerts deduped by service + rule + window
- serving dashboard stores live service health
- DLQ captures unparseable logs
- monitor collector lag and alert latency

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 49. Practice Case 4: Realtime IoT Telemetry Pipeline

Prompt:

```text
Design a realtime pipeline for realtime iot telemetry pipeline.
```

Source:

```text
sensor/device events
```

Goal:

```text
telemetry dashboard and threshold alerts
```

Strong design points:

- devices emit device_id, sequence_number, event_time, reading values
- collector handles unreliable network and burst uploads
- broker partitioned by device_id
- stateful processor computes rolling averages and anomaly rules
- watermarks handle offline late uploads
- DLQ/quarantine invalid readings
- raw telemetry archived for replay
- monitor device silence, late rate, hot devices, and state size

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 50. Practice Case 5: Realtime Inventory Pipeline

Prompt:

```text
Design a realtime pipeline for realtime inventory pipeline.
```

Source:

```text
orders, returns, warehouse updates
```

Goal:

```text
live inventory availability
```

Strong design points:

- events emitted for stock movement, reservation, purchase, return
- partition by product_id or product_id + warehouse_id
- state store maintains current inventory count
- exactly-once-like updates through idempotent event_id and sequence guard
- sink writes to inventory serving database
- reconciliation batch compares realtime state to warehouse source
- alert on negative inventory or stockout

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 51. Practice Case 6: Realtime CDC Pipeline

Prompt:

```text
Design a realtime pipeline for realtime cdc pipeline.
```

Source:

```text
database change events
```

Goal:

```text
current-state analytical table
```

Strong design points:

- CDC source emits insert/update/delete with LSN and operation
- broker partitioned by table/key
- raw CDC events stored in lake
- processor applies ordered updates per key
- idempotent MERGE/upsert to lakehouse/warehouse current table
- delete/tombstone handling explicit
- monitor CDC lag, duplicate LSNs, target duplicate keys
- replay raw CDC to rebuild target

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 52. Practice Case 7: Realtime ML Feature Pipeline

Prompt:

```text
Design a realtime pipeline for realtime ml feature pipeline.
```

Source:

```text
events and transactions
```

Goal:

```text
online features for model serving
```

Strong design points:

- stream processor computes rolling features by user/account/entity
- feature definitions versioned
- state store maintains rolling windows
- online feature store sink upserts by entity + feature name + timestamp
- offline batch path builds training features from raw history
- monitor feature freshness, null rate, distribution drift
- ensure training-serving consistency

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 53. Practice Case 8: Realtime Recommendation Signals

Prompt:

```text
Design a realtime pipeline for realtime recommendation signals.
```

Source:

```text
user actions and product events
```

Goal:

```text
fresh recommendation features
```

Strong design points:

- click/view/cart/purchase events ingested continuously
- partition by user_id for per-user action order
- stream processor updates recent user interests and item popularity
- serving store provides low-latency feature reads
- late events accepted within business-defined window
- batch recomputation corrects long-term aggregates
- monitor event volume and feature update lag

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 54. Practice Case 9: Realtime Payment Monitoring

Prompt:

```text
Design a realtime pipeline for realtime payment monitoring.
```

Source:

```text
payment attempts and status events
```

Goal:

```text
payment operations dashboard
```

Strong design points:

- backend payment events include payment_id, merchant_id, status, amount, event_time
- partition by merchant_id for merchant-level windows
- rolling aggregates track decline rate, success rate, latency
- alerts trigger on spikes by merchant/payment provider
- finance-grade totals reconciled in batch
- duplicate payment events handled by event_id/payment status sequence
- monitor alert latency and false positives

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 55. Practice Case 10: Realtime Security Event Pipeline

Prompt:

```text
Design a realtime pipeline for realtime security event pipeline.
```

Source:

```text
login and access events
```

Goal:

```text
security alerts
```

Strong design points:

- events include user_id, device_id, IP, event_time, action, result
- partition by user_id or account_id
- stateful rules track failed logins and impossible travel
- cached geo/device enrichment
- alerts deduped and severity-routed
- strict PII/security access controls
- long raw retention for investigation
- monitor event gaps and rule latency

Minimum interview answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processing
state/checkpoints
dedupe
late events
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Interview line:

```text
Tie the realtime design to latency, correctness, state, and consumer actionability.
```


## 56. Fast Path + Correct Path

Many systems need both immediate and certified output.

Fast path:

```text
streaming output with low latency
may be approximate or temporarily incomplete
```

Correct path:

```text
batch or replay-based recomputation
handles late events and corrections
certified for reporting
```

Examples:

```text
live dashboard now
certified daily report tomorrow
```

Interview line:

```text
For many analytics use cases, I combine realtime speed with batch correction for accuracy.
```


## 57. Realtime vs Request-Time Computation

Some features/metrics can be computed on ingestion, others at request time.

Realtime precompute:

```text
lower read latency
higher write/compute cost
good for dashboards/features/alerts
```

Request-time compute:

```text
more flexible
higher read latency
may overload serving systems
```

Interview line:

```text
I precompute metrics when low read latency and repeated access justify the write-time cost.
```


## 58. External API Calls in Stream Jobs

External calls can break realtime SLAs.

Risks:

```text
high latency
rate limits
partial outages
backpressure
non-deterministic replay
cost
```

Alternatives:

```text
cached reference data
periodically loaded dimension table
async enrichment
fallback/default values
side output for enrichment failures
```

Interview line:

```text
Realtime processors should avoid slow external calls in the critical path unless the latency budget allows it.
```


## 59. Stateful Join With Changing Dimensions

Joining events to changing dimensions is hard.

Options:

```text
use latest dimension state from compacted topic/table
use versioned dimension with event-time as-of join
use cached dimension with periodic refresh
enrich later in batch if not needed realtime
```

Trade-off:

```text
latest dimension is fast but may be historically incorrect
as-of join is correct but more complex
```

Interview line:

```text
Realtime enrichment must define whether it uses current dimension state or event-time historical state.
```


## 60. Realtime Corrections

Late or corrected events can change previous outputs.

Correction approaches:

```text
update aggregate windows if still open
emit correction/upsert to serving sink
write correction event
batch recompute affected partitions
mark dashboard metric as provisional
```

Interview line:

```text
Realtime outputs should be clear about whether they are final or provisional.
```


## 61. Multi-Region Realtime Pipelines

Multi-region design supports global users and availability.

Options:

```text
regional producers and collectors
regional broker clusters
replicate events to central lake
global aggregation layer
dedupe by global event_id
route consumers to nearest region
```

Trade-offs:

```text
lower latency and higher availability
more complex dedupe, ordering, failover, and governance
```

Interview line:

```text
Multi-region realtime systems improve availability but make ordering and global aggregation harder.
```


## 62. Disaster Recovery

Realtime DR requires data and state recovery.

Components:

```text
broker replication or raw event backup
stream job checkpoint backups
state store snapshots
sink backup/restore
replay tooling
runbook
RPO/RTO definitions
```

Interview line:

```text
For realtime systems, disaster recovery must include both events and processing state.
```


## 63. Stateful Processing Failure Modes

Common failure modes:

```text
checkpoint corruption
unbounded state growth
hot key state overload
state TTL too short
state TTL too long
sink commit succeeds but checkpoint fails
job restart reprocesses events
watermark stuck
```

Mitigation:

```text
state metrics
checkpoint monitoring
idempotent sinks
bounded TTL
hot-key detection
replay testing
```

Interview line:

```text
State is the hardest part of realtime pipelines; it must be bounded, checkpointed, and observable.
```


## 64. Realtime Data Quality vs Batch DQ

Realtime DQ:

```text
fast checks
schema validation
malformed rate
volume/lag checks
duplicate/late-event rate
critical field checks
```

Batch DQ:

```text
heavier reconciliation
full partition checks
source-to-target totals
metric correctness
historical anomaly detection
```

Interview line:

```text
Realtime DQ catches immediate issues; batch DQ provides stronger certified correctness.
```


## 65. Realtime Pipeline Anti-Patterns

Avoid:

```text
no latency SLA
no event_id
no raw event storage
no checkpointing
committing offsets before sink success
unbounded state
no watermark/late data policy
blind append to sink on retries
heavy API calls in processor
no DLQ
no lag monitoring
no PII controls
one topic/partition for everything
```

Interview line:

```text
Most realtime failures come from ignoring retries, state, late data, and observability.
```


## 66. Realtime Pipeline Trade-Offs

Common trade-offs:

```text
latency vs correctness
watermark delay vs output speed
state retention vs cost
strict schema vs producer flexibility
ordering vs partition distribution
realtime compute cost vs batch simplicity
raw retention vs storage cost
exact dedupe vs approximate dedupe
fast provisional output vs certified output
external enrichment richness vs latency
```

Interview line:

```text
Realtime design is choosing the right balance between speed, correctness, cost, and operational complexity.
```


## 67. Pattern Classification Drill

### Dashboard needs updates under 2 seconds

```text
Realtime serving and latency budget.
```

### Events replay after restart and duplicate alerts fire

```text
Idempotent sink / alert_id dedupe.
```

### Consumer lag keeps growing

```text
Backpressure; scale/optimize processor or sink.
```

### Watermark is stuck

```text
Late/out-of-order stream or timestamp issue.
```

### State store keeps growing

```text
Missing TTL or unbounded keys.
```

### A large customer creates hot partition

```text
Hot key/partition issue.
```

### Mobile events arrive next day

```text
Late events with event-time handling.
```

### Sink write succeeds but checkpoint fails

```text
Replay-safe idempotent sink needed.
```

### External enrichment API slows job

```text
Use cache/reference table/async enrichment.
```

### Realtime number differs from daily report

```text
Fast path vs batch correction.
```

### Unknown event schema appears

```text
Schema registry/contract violation.
```

### DLQ spikes after app release

```text
Producer schema/quality issue.
```

### Feature freshness delayed

```text
Online feature sink or processing lag issue.
```

### Fraud alerts duplicate

```text
Alert dedupe/suppression missing.
```

### Raw events not retained

```text
Replay/backfill risk.
```

### No per-user order in sessions

```text
Partitioning/order issue.
```

### Checkpoint takes too long

```text
State size/checkpoint tuning issue.
```

### Kafka topic has low partitions

```text
Parallelism bottleneck.
```

### PII appears in DLQ logs

```text
Security/privacy handling failure.
```

### Low-value event costs too much realtime compute

```text
Route to batch-only pipeline.
```


## 68. High-ROI Realtime Topics

### latency SLA

```text
drives design
```

### event schema

```text
contract and validation
```

### broker

```text
durable stream transport
```

### partitioning

```text
parallelism and ordering
```

### offsets

```text
consumer progress
```

### checkpoints

```text
state recovery
```

### state store

```text
window/session/feature state
```

### watermarks

```text
late-event handling
```

### windows

```text
time-based aggregation
```

### dedupe

```text
event_id and TTL state
```

### idempotent sink

```text
safe retries
```

### DLQ

```text
bad event isolation
```

### raw storage

```text
replay and backfills
```

### monitoring

```text
lag, latency, state, DLQ
```

### backpressure

```text
scale and bottlenecks
```

### serving store

```text
low-latency outputs
```

### fast + correct path

```text
speed plus accuracy
```


## 69. Review Checklist

### Did candidate clarify latency SLA?

```text
Required.
```

### Did candidate clarify correctness and data loss tolerance?

```text
Required.
```

### Did candidate define producers and event schema?

```text
Critical.
```

### Did candidate design broker/topics/partitions?

```text
Scale and order.
```

### Did candidate define raw storage?

```text
Replay.
```

### Did candidate define stream processing logic?

```text
Core pipeline.
```

### Did candidate handle state and checkpointing?

```text
Recovery.
```

### Did candidate define windows/watermarks?

```text
Event-time correctness.
```

### Did candidate handle duplicates?

```text
At-least-once safety.
```

### Did candidate handle late/out-of-order events?

```text
Correctness.
```

### Did candidate define idempotent sinks?

```text
Safe output.
```

### Did candidate define DLQ/quarantine?

```text
Bad events.
```

### Did candidate define monitoring/alerts?

```text
Operations.
```

### Did candidate address scaling/backpressure?

```text
Production.
```

### Did candidate address security/PII?

```text
Governance.
```

### Did candidate explain cost/retention?

```text
Maturity.
```

### Did candidate explain trade-offs?

```text
System design maturity.
```


## 70. Weakness Repair Map

### Only says Kafka/Spark

```text
Practice full architecture framework.
```

### No latency budget

```text
Practice SLA breakdown.
```

### No state/checkpointing

```text
Practice stateful processing drills.
```

### No watermarks

```text
Practice late event/window drills.
```

### No dedupe

```text
Practice event_id/idempotent sink.
```

### No raw storage

```text
Practice replay/backfill scenarios.
```

### No sink design

```text
Practice serving store and idempotency.
```

### No monitoring

```text
Practice lag/latency/state metrics.
```

### No scaling

```text
Practice partitions/backpressure/hot keys.
```

### No privacy

```text
Practice event PII controls.
```

### Poor communication

```text
Practice whiteboard template.
```


## 71. 7-Day Realtime Pipeline Study Plan

### Day 1

```text
Realtime basics, latency SLA, event schema, broker concepts.
```

### Day 2

```text
Topics, partitions, offsets, consumer groups, checkpoints.
```

### Day 3

```text
Windows, watermarks, late events, out-of-order events.
```

### Day 4

```text
Stateful processing, dedupe, idempotent sinks, exactly-once-like output.
```

### Day 5

```text
DLQ, data quality, monitoring, alerts, backpressure.
```

### Day 6

```text
Serving stores, ML features, fraud alerts, CDC realtime, cost/security.
```

### Day 7

```text
Full realtime system design mock and weakness repair.
```


## 72. 30-Day Realtime Pipeline Study Plan

### Week 1

```text
Foundation: producers, broker, event schema, latency.
```

### Week 2

```text
Correctness: windows, watermarks, state, dedupe, idempotency.
```

### Week 3

```text
Operations: monitoring, DLQ, backpressure, scaling, security, cost.
```

### Week 4

```text
Case studies and timed mocks.
```


## 73. Timed Interview Protocol

### 0-5 minutes

```text
Clarify use case, producers, consumers, SLA, scale, correctness.
```

### 5-12 minutes

```text
Draw producers → broker → stream processor → sinks + raw storage.
```

### 12-22 minutes

```text
Deep dive partitioning, event schema, state, windows, watermarks.
```

### 22-32 minutes

```text
Deep dive dedupe, checkpointing, idempotent sinks, replay, DLQ.
```

### 32-40 minutes

```text
Discuss monitoring, scaling, backpressure, security, cost.
```

### 40-45 minutes

```text
Trade-offs and final summary.
```


## 74. Realtime Pipeline Whiteboard Template

```text
Requirements:
- use case:
- producers:
- consumers:
- latency SLA:
- throughput:
- peak traffic:
- event size:
- correctness requirement:
- ordering requirement:
- late event tolerance:
- PII/security:

Architecture:
producers → collector → broker/topics/partitions → raw sink → stream processor/state/checkpoints → serving sinks

Correctness:
- event schema:
- event_id:
- partition key:
- checkpoint strategy:
- state store:
- windowing:
- watermark:
- dedupe:
- idempotent sink:
- DLQ:
- replay:

Operations:
- lag monitoring:
- processing latency:
- state metrics:
- alerts:
- backpressure:
- scaling:
- retention:
- cost:
```


## 75. Realtime Event Schema Template

```text
event_id:
event_name:
event_time:
ingested_at:
producer:
schema_version:
entity_key:
user_id:
device_id:
session_id:
trace_id:
properties:
pii_classification:
```


## 76. Stream Processing Design Template

```text
Job name:
Input topics:
Partition key:
Processing engine:
Event-time field:
Window type:
Watermark:
Allowed lateness:
State required:
State TTL:
Dedupe key:
Enrichment:
Output sinks:
Checkpoint location:
DLQ:
Monitoring:
```


## 77. Realtime DQ Checklist Template

```text
Input:
- event_id present
- schema valid
- event_time valid
- producer authorized

Processing:
- duplicate rate
- late-event rate
- DLQ rate
- watermark progress
- state size

Output:
- sink freshness
- output row/key uniqueness
- alert duplicates
- aggregate sanity
- batch correction reconciliation
```


## 78. Realtime Incident Runbook Template

```text
Incident:
Pipeline:
Severity:
Affected topic:
Affected consumer:
Current lag:
Processing latency:
DLQ count:
State size:
Sink status:

Steps:
1. Check producer volume.
2. Check broker health.
3. Check consumer lag.
4. Check checkpoint status.
5. Check DLQ errors.
6. Check sink write latency.
7. Scale or pause if needed.
8. Replay from last safe checkpoint/raw events.
9. Validate sink output.
10. Notify consumers.
```


## 79. Mock Set 1: Realtime Foundations

Problems:

- Explain realtime vs streaming vs batch.
- Design a realtime pipeline high-level architecture.
- Explain event time vs processing time.
- Explain broker topics, partitions, offsets, and consumer groups.
- Create a latency budget for a realtime dashboard.

Expected answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processor
state/checkpoints
windows/watermarks
dedupe
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 80. Mock Set 2: Correctness

Problems:

- Design deduplication for realtime events.
- Design late-event handling with watermarks.
- Design checkpointing and recovery.
- Design idempotent sink writes.
- Explain exactly-once-like output.

Expected answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processor
state/checkpoints
windows/watermarks
dedupe
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 81. Mock Set 3: Stateful Processing

Problems:

- Design rolling 5-minute counts.
- Design sessionization.
- Design stream-table enrichment.
- Design realtime feature computation.
- Handle unbounded state growth.

Expected answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processor
state/checkpoints
windows/watermarks
dedupe
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 82. Mock Set 4: Operations

Problems:

- Monitor consumer lag and processing latency.
- Handle backpressure.
- Handle hot partitions.
- Design DLQ and quarantine.
- Design replay after stream job bug.

Expected answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processor
state/checkpoints
windows/watermarks
dedupe
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 83. Mock Set 5: Case Designs

Problems:

- Design realtime clickstream dashboard.
- Design realtime fraud detection.
- Design realtime IoT telemetry.
- Design realtime CDC pipeline.
- Design realtime ML feature pipeline.

Expected answer must include:

```text
latency SLA
event schema
broker/partitioning
stream processor
state/checkpoints
windows/watermarks
dedupe
idempotent sink
DLQ
monitoring
scaling
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 84. Realtime Pipeline FAQ

### FAQ 1: What is a realtime pipeline?

```text
A data pipeline that processes and serves events continuously with low latency.
```

### FAQ 2: Is realtime the same as streaming?

```text
Realtime is a low-latency streaming use case; not every streaming job has strict realtime SLA.
```

### FAQ 3: What is the hardest part of realtime pipelines?

```text
State, checkpointing, late events, and idempotent output under retries.
```

### FAQ 4: Why do we need watermarks?

```text
To handle event-time windows when events arrive late or out of order.
```

### FAQ 5: Why do we need raw storage?

```text
To support replay, backfills, debugging, and corrections.
```

### FAQ 6: What is consumer lag?

```text
How far a consumer is behind the latest broker messages.
```

### FAQ 7: What is backpressure?

```text
When downstream systems cannot keep up with incoming data.
```

### FAQ 8: What is an idempotent sink?

```text
A sink that can safely receive the same event/update more than once without duplicate/corrupt output.
```

### FAQ 9: What should be monitored?

```text
Lag, latency, throughput, DLQ, duplicates, late events, checkpoint health, state size, sink freshness, and cost.
```

### FAQ 10: What makes a realtime answer strong?

```text
Latency budget, schema, broker design, state/checkpoints, watermarks, dedupe, idempotent sinks, replay, monitoring, scaling, and trade-offs.
```


## 85. Candidate Self-Review Questions

After every realtime pipeline design, candidate should answer:

```text
1. What is the realtime use case?
2. What is the latency SLA?
3. What are the producers?
4. What are the consumers?
5. What is the event schema?
6. What is the event_id?
7. What is the broker?
8. What topics are used?
9. What partition key is used?
10. What ordering is required?
11. What processing engine is used?
12. What state is stored?
13. What is the state TTL?
14. Where are checkpoints stored?
15. When are offsets committed?
16. What windows are used?
17. What watermark is used?
18. How are late events handled?
19. How are duplicates handled?
20. How are sinks idempotent?
21. What DLQ exists?
22. Where are raw events stored?
23. How is replay supported?
24. What serving store is used?
25. What data quality checks run?
26. What monitoring exists?
27. What alerts exist?
28. How is backpressure handled?
29. How is cost controlled?
30. What trade-offs were chosen?
```

If candidate cannot answer these:

```text
The realtime pipeline design is not interview-ready.
```


## 86. Final Exit Test

Candidate passes realtime pipeline system design when they can explain:

```text
1. Realtime vs streaming vs batch.
2. Latency SLA and latency budget.
3. Producers and consumers.
4. Event schema and contracts.
5. Broker/topic/partition design.
6. Consumer groups.
7. Offsets and checkpoints.
8. Stream processor responsibilities.
9. Event time vs processing time.
10. Windowing.
11. Watermarks.
12. Late-event handling.
13. Out-of-order handling.
14. Deduplication.
15. Stateful aggregation.
16. State store.
17. State TTL.
18. Stream joins.
19. Enrichment.
20. Realtime features.
21. Realtime alerting.
22. Idempotent sinks.
23. Exactly-once-like output.
24. DLQ/quarantine.
25. Raw event storage.
26. Replay and backfills.
27. Data quality checks.
28. Monitoring metrics.
29. Alert conditions.
30. Backpressure handling.
31. Scaling strategy.
32. Hot partition handling.
33. Serving sink options.
34. Security and privacy.
35. Cost controls.
36. Fast path plus correct path.
37. Disaster recovery.
38. Case study: clickstream dashboard.
39. Case study: fraud detection.
40. Case study: IoT telemetry.
41. Case study: realtime CDC.
42. Case study: realtime ML features.
43. Trade-offs and final summary.
```

Passing standard:

```text
Average score >= 4/5.
No missing latency SLA.
No missing event schema.
No missing checkpoint/state strategy.
No missing watermarks/late-event handling.
No missing dedupe/idempotent sink.
No missing replay/raw storage.
No missing monitoring/scaling.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate designs a low-latency, stateful, replayable, observable, cost-aware realtime pipeline with clear correctness trade-offs.
```


## 87. Final Summary

Realtime pipeline system design is a core Data Engineering interview skill.

The candidate must master:

```text
realtime vs streaming vs batch
latency budgets
event producers
event consumers
event schema
event contracts
brokers
topics
partitions
consumer groups
offsets
checkpoints
stream processors
state stores
state TTL
event time
processing time
ingestion time
windows
watermarks
late events
out-of-order events
deduplication
stateful aggregation
stream joins
enrichment
realtime features
realtime alerting
idempotent sinks
exactly-once-like output
DLQ/quarantine
raw event storage
replay
backfills
data quality
monitoring
alerting
backpressure
scaling
hot partitions
serving stores
security
privacy
cost
retention
fast path plus correct path
trade-offs
```

The mentor must be strict:

```text
Only says Kafka/Spark → not interview-ready.
No latency SLA → not interview-ready.
No event schema → not interview-ready.
No checkpoint/state strategy → not interview-ready.
No dedupe → not interview-ready.
No late-event handling → not interview-ready.
No idempotent sink → not interview-ready.
No replay/raw storage → not interview-ready.
No monitoring/backpressure → not interview-ready.
```

Final interview line:

```text
A production realtime pipeline must deliver low-latency outputs while preserving correctness, recovery, observability, and operational control.
```


## 88. Additional Mini Scenario Cards

### Mini Scenario 1: Consumer lag keeps increasing

Recommended direction:

```text
Scale consumers, increase partitions, optimize sink, or reduce processing bottleneck.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 2: Dashboard is fast but wrong after late events

Recommended direction:

```text
Add watermarks, allowed lateness, corrections, or batch recomputation.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 3: Duplicate alerts after job restart

Recommended direction:

```text
Use alert_id and idempotent alert sink.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 4: State store grows without limit

Recommended direction:

```text
Add state TTL and monitor state size/cardinality.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 5: Sink write succeeds but checkpoint fails

Recommended direction:

```text
Design idempotent sink so replay is safe.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 6: Large tenant causes one partition to lag

Recommended direction:

```text
Hot partition; choose better key or salt/split tenant if ordering allows.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 7: External API enrichment causes backpressure

Recommended direction:

```text
Use cached reference data or async enrichment.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 8: No raw event lake

Recommended direction:

```text
Replay/backfill impossible after processing bug.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 9: Unknown schema after app release

Recommended direction:

```text
Schema registry/event contract validation.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 10: DLQ spikes after deploy

Recommended direction:

```text
Alert producer owner and inspect failure samples.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 11: Watermark stuck

Recommended direction:

```text
Timestamp issue, extreme late events, or source stall.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 12: Realtime metric differs from daily certified metric

Recommended direction:

```text
Use fast path plus batch correction and label provisional metrics.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 13: PII appears in raw event

Recommended direction:

```text
Schema allowlist, masking/tokenization, restrict raw access.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 14: Event processed twice

Recommended direction:

```text
At-least-once replay; dedupe by event_id and idempotent sink.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 15: Window output delayed too much

Recommended direction:

```text
Watermark allowed lateness may be too long.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 16: Late event dropped but business needs accuracy

Recommended direction:

```text
Extend allowed lateness or emit corrections.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 17: Feature store is stale

Recommended direction:

```text
Monitor feature freshness and sink latency.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 18: Checkpoint duration rises

Recommended direction:

```text
State too large or storage bottleneck.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 19: Low-value events consume expensive realtime compute

Recommended direction:

```text
Route to batch-only path or lower priority stream.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 20: Broker retention expired during outage

Recommended direction:

```text
Replay from raw lake or increase retention.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 21: No per-user ordering for sessions

Recommended direction:

```text
Partition by user_id/anonymous_id.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 22: Backfill changes realtime feature logic

Recommended direction:

```text
Replay raw events and write versioned features.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 23: Alert storm happens

Recommended direction:

```text
Add suppression, grouping, and severity routing.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 24: Processing job cannot keep up at peak

Recommended direction:

```text
Autoscale, increase partitions, batch writes, optimize state and sink.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 25: Client clock sends future events

Recommended direction:

```text
Validate event_time and store ingestion_time.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 26: Stream-table join uses stale dimension

Recommended direction:

```text
Define dimension freshness and update strategy.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 27: Fraud model needs last 1 hour features

Recommended direction:

```text
Stateful rolling window feature computation.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 28: Warehouse sink has duplicates

Recommended direction:

```text
Use upsert/MERGE and event_id/aggregate key.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 29: DLQ contains PII in error payload

Recommended direction:

```text
Mask DLQ samples and restrict access.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 30: No cost visibility by topic

Recommended direction:

```text
Add cost attribution by topic/job/sink.
```

Candidate must explain:

```text
1. What failed.
2. Which realtime principle applies.
3. Correct design pattern.
4. Monitoring or validation.
5. Trade-off.
```

Passing score:

```text
4/5 or higher.
```


## 89. Quick Reference Cards

### Card 1: Realtime pipeline

Purpose:

```text
Low-latency continuous data processing.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 2: Latency budget

Purpose:

```text
Time allocation across pipeline stages.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 3: Broker

Purpose:

```text
Durable stream transport.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 4: Partition key

Purpose:

```text
Controls ordering and parallelism.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 5: Consumer lag

Purpose:

```text
How far processing is behind.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 6: Checkpoint

Purpose:

```text
Saved progress and state.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 7: State store

Purpose:

```text
Stores state across events.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 8: Window

Purpose:

```text
Time range for aggregation.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 9: Watermark

Purpose:

```text
Event-time progress and late-data control.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 10: Late event

Purpose:

```text
Event arriving after expected window.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 11: Deduplication

Purpose:

```text
Remove duplicate logical events.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 12: Idempotent sink

Purpose:

```text
Safe repeated writes.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 13: DLQ

Purpose:

```text
Bad event isolation.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 14: Replay

Purpose:

```text
Reprocess past events.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 15: Backpressure

Purpose:

```text
Downstream cannot keep up.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 16: Hot partition

Purpose:

```text
One partition overloaded.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 17: Serving store

Purpose:

```text
Low-latency output database/cache.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 18: Fast path

Purpose:

```text
Low-latency provisional output.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 19: Correct path

Purpose:

```text
Batch/replay certified output.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 20: State TTL

Purpose:

```text
Bounded state lifetime.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```
