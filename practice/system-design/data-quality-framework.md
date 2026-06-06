# Data Quality Framework System Design Guide

Generated: 2026-06-06

This guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/system-design/data-quality-framework.md
```

This guide trains the mentor and candidate on **data quality framework system design** for Data Engineering interviews.

The guide is interview-focused. It teaches how to design a production-grade data quality framework that validates pipelines, tables, files, streams, CDC feeds, marts, and ML feature datasets with clear rules, severity, ownership, observability, and remediation.

Data quality framework design is high-ROI because Data Engineering interviews often ask:

```text
Design a data quality framework.
Design data quality checks for a batch pipeline.
Design data quality checks for CDC pipeline.
Design data quality checks for a data lake.
Design a framework to validate freshness, completeness, uniqueness, and accuracy.
Design a system to detect data anomalies.
Design a data validation framework for dashboards.
Design a source-to-target reconciliation system.
Design a DQ platform that supports rules, alerts, dashboards, and ownership.
Design a data quality system for finance reporting.
Design a data quality system for ML feature pipelines.
Design DQ checks for late-arriving data.
Design a system to quarantine bad records.
Design a DQ framework with severity levels.
Design an automated DQ rules engine.
Explain Great Expectations/dbt tests/Deequ-style frameworks at interview level.
Explain hard checks vs soft checks.
Explain data observability vs data quality.
Explain how to prevent bad data from reaching gold tables.
Explain how to monitor data quality over time.
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

The purpose of this guide is to make the candidate strong at designing data quality frameworks in Data Engineering interviews.

The candidate should learn to answer:

```text
What is a data quality framework?
Why do data quality checks matter?
What dimensions of data quality should be checked?
Where should checks run in a pipeline?
How are checks configured?
How are checks executed?
How are check results stored?
How are severity levels defined?
How do we block bad data from publishing?
How do we quarantine bad records?
How do we alert the right owner?
How do we build DQ dashboards?
How do we validate freshness?
How do we validate completeness?
How do we validate uniqueness?
How do we validate validity?
How do we validate consistency?
How do we validate accuracy?
How do we validate referential integrity?
How do we validate source-to-target reconciliation?
How do we detect anomalies?
How do we handle false positives?
How do we design DQ for batch, streaming, CDC, and lakehouse pipelines?
How do we track quality trends over time?
How do we make checks scalable and cost-aware?
```

A candidate is interview-ready only when they can design:

```text
rule configuration
rule execution engine
check result storage
severity model
pipeline quality gates
quarantine flow
alerting and ownership
DQ dashboards
freshness checks
volume checks
schema checks
null checks
uniqueness checks
validity checks
referential integrity checks
reconciliation checks
anomaly checks
CDC-specific checks
streaming checks
ML feature checks
cost-aware execution
remediation workflow
```


## 2. What Interviewers Are Testing

Data quality framework design tests whether the candidate can think beyond writing one-off SQL checks.

Interviewers evaluate:

```text
does the candidate understand data quality dimensions?
does the candidate distinguish pipeline success from data correctness?
does the candidate design configurable rules rather than hardcoded checks?
does the candidate define severity and gate behavior?
does the candidate know where checks should run?
does the candidate track historical DQ results?
does the candidate alert the right owners?
does the candidate support quarantine and remediation?
does the candidate handle false positives and thresholds?
does the candidate consider cost and scalability?
does the candidate design source-target reconciliation?
does the candidate understand data observability?
does the candidate cover batch, streaming, CDC, and lake use cases?
```

Weak answer:

```text
Check if columns are null and send alert.
```

Strong answer:

```text
I would design a metadata-driven DQ framework where rules are stored in a config table with owner, severity, threshold, schedule, and target dataset. The orchestrator runs checks at bronze, silver, and gold layers. Results are written to a DQ results table, critical checks block publishing, warnings alert but do not block, bad records are quarantined with error metadata, dashboards show freshness, volume, duplicates, null rates, schema drift, and reconciliation trends, and alerts are routed to dataset owners with runbook links.
```

Interview line:

```text
A good data quality framework turns data trust into a measurable, monitored, and operational process.
```


## 3. Core Mental Model

A data quality framework is a control system around data pipelines.

Mental model:

```text
Data sources / tables / files / streams
        ->
DQ rule configuration
        ->
DQ execution engine
        ->
DQ results store
        ->
Quality gates
        ->
Alerts / dashboards / remediation
```

It should answer:

```text
What should be checked?
When should it be checked?
How is pass/fail decided?
Who owns failures?
Does failure block publishing?
Where are bad records stored?
How are trends monitored?
How are false positives handled?
How is quality improved over time?
```

Core interview line:

```text
Data quality is not a single SQL check; it is rules, execution, results, severity, alerts, and remediation.
```


## 4. Data Quality Vocabulary

Important terms:

```text
Data quality:
The degree to which data is fit for its intended use.

Data quality rule:
A condition that a dataset or record must satisfy.

Data quality check:
Execution of a rule against data.

Expectation:
A declarative rule, often used by frameworks like Great Expectations.

Freshness:
Data is updated within expected time.

Completeness:
Expected records, partitions, files, or fields exist.

Uniqueness:
Keys do not have duplicates.

Validity:
Values follow allowed formats, ranges, and domains.

Consistency:
Data agrees across related columns/tables/sources.

Accuracy:
Data matches real-world or source-of-truth values.

Referential integrity:
Foreign keys match dimension/reference records.

Reconciliation:
Comparing source and target counts, keys, hashes, or metrics.

Anomaly detection:
Detecting unusual changes compared to historical patterns.

Quality gate:
A rule set that decides whether data can move to the next layer or be published.

Severity:
Critical, warning, or info classification of a quality issue.

Quarantine:
Location for bad records and error metadata.

DQ result:
Stored output of a data quality check.

Owner:
Person/team responsible for fixing quality issues.

SLA:
Expected freshness or availability agreement.

SLO:
Target quality or reliability objective.

Data observability:
Monitoring data health across freshness, volume, schema, lineage, and quality.
```


## 5. Standard DQ Framework Answer Framework

Use this framework for every data quality system design question:

```text
1. Clarify requirements.
2. Identify datasets and consumers.
3. Define quality dimensions.
4. Define critical vs warning checks.
5. Define where checks run:
   - ingestion
   - bronze/raw
   - silver/staging
   - gold/marts
   - serving
6. Design rule configuration.
7. Design rule execution engine.
8. Design result storage.
9. Design quality gates.
10. Design quarantine handling.
11. Design alerting and ownership.
12. Design DQ dashboards.
13. Design historical trend/anomaly detection.
14. Design remediation workflow.
15. Design integration with orchestration.
16. Design metadata/catalog integration.
17. Design cost and performance controls.
18. Design security and access.
19. Explain trade-offs.
20. Summarize final design.
```

Short version:

```text
Rules → Execution → Results → Gates → Alerts → Remediation → Trends
```

Strict rule:

```text
No DQ framework design is strong if it only lists checks and does not explain severity, result storage, alerting, ownership, and quality gates.
```


## 6. Scoring Rubric

Score data quality framework answers from 0 to 5.

### Score 0

No meaningful framework. Only says check nulls.

### Score 1

Mentions basic checks but no architecture, severity, alerts, or storage.

### Score 2

Has checks and alerts but lacks configurable rules, result history, gating, or ownership.

### Score 3

Reasonable framework but weak on quarantine, reconciliation, anomaly detection, cost, or integration with pipelines.

### Score 4

Interview-ready. Covers configurable rules, execution, result storage, severity, quality gates, quarantine, alerts, dashboards, ownership, pipeline integration, and key DQ dimensions.

### Score 5

Strong. Handles batch/streaming/CDC/lakehouse contexts, anomaly detection, source-target reconciliation, false positives, domain ownership, catalog integration, lineage, remediation workflow, cost-aware execution, PII-safe results, and quality SLOs.

Automatic score cap below 4 if:

```text
no rule configuration
no DQ result storage
no severity model
no quality gate behavior
no owner/alert routing
no freshness/completeness/uniqueness checks
no reconciliation strategy
no monitoring dashboard
no remediation/quarantine
only hardcoded SQL examples
```


## 7. Requirement Clarification Questions

Ask these before designing.

### Business and consumers

```text
Which datasets are critical?
Who consumes the data?
Is this for finance, BI, ML, operations, or compliance?
What happens if bad data reaches consumers?
Which failures must block publishing?
Which failures can be warnings?
```

### Data and pipeline

```text
What are the sources?
Batch, streaming, CDC, files, APIs, or warehouse tables?
What are the target layers?
Raw, staging, curated, gold, feature tables?
What is the data volume?
How often does data arrive?
What is the freshness SLA?
```

### Rules

```text
What are the key columns?
What fields are required?
What values are allowed?
What are expected row count ranges?
What source-target reconciliations are required?
Are there business metric totals that must match?
```

### Operations

```text
Who owns each dataset?
How should alerts be routed?
Do we need quarantine?
Do we need automatic remediation?
How long should DQ results be retained?
Do we need audit/compliance reporting?
What cost limits exist?
```

Interview line:

```text
I first identify critical datasets, consumers, failure impact, and ownership before designing checks.
```


## 8. Data Quality Dimensions

Core data quality dimensions:

### Freshness

```text
Data is updated within expected time.
```

### Completeness

```text
Expected records, files, columns, or partitions exist.
```

### Uniqueness

```text
Primary or business keys are not duplicated.
```

### Validity

```text
Values follow allowed formats, ranges, and domains.
```

### Consistency

```text
Data agrees across columns, tables, or systems.
```

### Accuracy

```text
Data matches source-of-truth or real-world expectations.
```

### Referential integrity

```text
Foreign keys match dimensions/reference data.
```

### Timeliness

```text
Data arrives and is processed within SLA.
```

### Conformity

```text
Data follows standard formats and business definitions.
```

### Volume

```text
Row counts and metric amounts are within expected ranges.
```

Interview line:

```text
I organize checks by quality dimensions so the framework is complete and not just null checks.
```


## 9. Reference Data Quality Architecture

Reference architecture:

```text
[Datasets]
  files
  raw tables
  staging tables
  curated tables
  marts
  streams
  CDC targets
        ->
[DQ Rule Config]
  rule metadata
  severity
  threshold
  owner
  schedule
        ->
[DQ Execution Engine]
  SQL checks
  Spark checks
  file checks
  schema checks
  API checks
        ->
[DQ Results Store]
  check status
  actual value
  expected value
  run metadata
  sample failures
        ->
[Quality Gates]
  block / warn / pass
        ->
[Actions]
  alerts
  quarantine
  tickets
  dashboards
  remediation
        ->
[Consumers]
  pipeline orchestrator
  catalog
  BI
  owners
  incident management
```

Control plane:

```text
orchestrator integration
catalog metadata
lineage
alert routing
runbooks
access controls
cost tracking
```

Interview line:

```text
The DQ framework should be metadata-driven and integrated with pipeline publishing decisions.
```


## 10. Where DQ Checks Run

Checks should run at multiple points.

### Ingestion

```text
file exists
API response valid
schema readable
row count non-zero
source freshness
```

### Bronze/raw

```text
raw metadata present
schema captured
file checksum valid
CDC operation valid
payload parse success
```

### Silver/staging

```text
types valid
required fields not null
dedupe rules applied
business keys valid
accepted values valid
```

### Curated

```text
primary key uniqueness
referential integrity
SCD interval validity
source-target reconciliation
business constraints
```

### Gold/marts

```text
metric totals reconcile
one row per published grain
freshness SLA met
dashboard-ready checks pass
```

### ML feature tables

```text
one row per entity/date
no future leakage
feature null rate within threshold
distribution drift within threshold
```

Interview line:

```text
Data quality should become stricter as data moves closer to consumers.
```


## 11. Rule Configuration Design

### Rule ID

```text
Unique identifier for the check.
```

### Dataset

```text
Target table/file/topic being checked.
```

### Layer

```text
Bronze, silver, gold, warehouse, stream, or feature table.
```

### Check type

```text
freshness, null, uniqueness, range, schema, reconciliation, anomaly.
```

### Expression

```text
SQL, configuration, or engine-specific check definition.
```

### Threshold

```text
Allowed value or tolerance.
```

### Severity

```text
critical, warning, info.
```

### Owner

```text
Team or person responsible.
```

### Schedule

```text
When the check runs.
```

### Gate behavior

```text
block, warn, quarantine, or observe.
```

### Runbook

```text
Instructions for failure.
```

### Enabled flag

```text
Allows controlled rollout.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 12. DQ Rule Config Table

### rule_id

```text
Unique rule key.
```

### dataset_name

```text
Dataset being checked.
```

### column_name

```text
Optional target column.
```

### check_type

```text
Type of check.
```

### rule_sql

```text
SQL expression or query.
```

### expected_value

```text
Expected threshold or value.
```

### comparison_operator

```text
equals, greater_than, between, etc.
```

### severity

```text
critical/warning/info.
```

### owner_team

```text
Responsible team.
```

### schedule_cron

```text
Execution schedule.
```

### blocking_flag

```text
Whether failure blocks publish.
```

### is_active

```text
Whether rule is active.
```

### created_at

```text
Rule creation timestamp.
```

### updated_at

```text
Rule update timestamp.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 13. DQ Result Table

### run_id

```text
Pipeline or DQ run identifier.
```

### rule_id

```text
Rule executed.
```

### dataset_name

```text
Dataset checked.
```

### partition_value

```text
Date/partition checked.
```

### status

```text
pass/fail/warn/error/skipped.
```

### actual_value

```text
Observed value.
```

### expected_value

```text
Threshold or expected value.
```

### severity

```text
critical/warning/info.
```

### failure_sample_path

```text
Optional path/table for failed records.
```

### started_at

```text
Check start time.
```

### completed_at

```text
Check end time.
```

### duration_seconds

```text
Check runtime.
```

### error_message

```text
Error if check execution failed.
```

### owner_team

```text
Responsible owner.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 14. DQ Rule Types

### Schema checks

```text
Columns, types, required fields, schema version.
```

### Freshness checks

```text
Max timestamp or latest partition within SLA.
```

### Completeness checks

```text
Expected files/partitions/records exist.
```

### Volume checks

```text
Row counts or byte counts within thresholds.
```

### Null checks

```text
Required fields not null.
```

### Uniqueness checks

```text
Primary/business keys are unique.
```

### Validity checks

```text
Ranges, regex, accepted values, types.
```

### Referential checks

```text
Foreign keys match dimension/reference table.
```

### Consistency checks

```text
Cross-column and cross-table logic.
```

### Reconciliation checks

```text
Source vs target counts, sums, hashes, keys.
```

### Anomaly checks

```text
Historical trend deviations.
```

### Custom business checks

```text
Domain-specific rules.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 15. Severity Model

### Critical

```text
Blocks publish; requires immediate owner action.
```

### Warning

```text
Does not block by default; alerts owner and tracks trend.
```

### Info

```text
Logged for observability; no immediate action.
```

### Severity should depend on consumer impact

```text
Finance critical, exploratory sandbox often warning/info.
```

### Severity should be configurable

```text
Not every null check is equally important.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 16. Quality Gate Behavior

### Block

```text
Stop pipeline or prevent table publish.
```

### Warn

```text
Allow publish but alert and mark dataset as degraded.
```

### Quarantine

```text
Separate bad records and continue if policy allows.
```

### Observe

```text
Record result only for trend tracking.
```

### Manual approval

```text
Require owner approval for critical but recoverable cases.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 17. Hard Checks vs Soft Checks

### Hard check

```text
Failure blocks data movement or publish.
```

### Soft check

```text
Failure alerts but data continues.
```

### Use hard checks for

```text
Duplicate primary keys, missing partition, schema break, finance reconciliation mismatch.
```

### Use soft checks for

```text
Small volume variation, optional field null spike, early anomaly detection.
```

### Interview rule

```text
Hard checks protect correctness; soft checks protect awareness without over-blocking.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 18. Threshold Design

### Static threshold

```text
Example: row_count > 0.
```

### Range threshold

```text
Example: null_rate between 0 and 0.01.
```

### Relative threshold

```text
Example: row_count within 20% of 7-day average.
```

### Dynamic threshold

```text
Historical anomaly detection.
```

### Seasonal threshold

```text
Compare same weekday or same hour.
```

### Manual threshold

```text
Business-owned limit.
```

### Warning

```text
Bad thresholds create false positives or missed failures.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 19. Ownership Model

### Every dataset needs owner

```text
Alerts must route somewhere accountable.
```

### Every rule needs owner

```text
Business or technical owner decides severity.
```

### Ownership metadata

```text
team, Slack/email, escalation path, runbook.
```

### Domain ownership

```text
Sales owns sales metrics, finance owns finance reconciliation.
```

### Platform ownership

```text
DQ engine owned by data platform team.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 20. Rule Lifecycle

### Proposed

```text
Rule requested or drafted.
```

### Test mode

```text
Rule runs but does not alert/block.
```

### Warning mode

```text
Rule alerts but does not block.
```

### Blocking mode

```text
Rule can fail pipeline/publish.
```

### Deprecated

```text
Rule retired because data or business logic changed.
```

### Versioned

```text
Rule changes should be auditable.
```

Interview line:

```text
A scalable DQ framework is metadata-driven, not a pile of hardcoded one-off SQL checks.
```


## 21. Freshness Checks

Freshness checks ensure data is updated on time.

Examples:

```sql
SELECT MAX(ingested_at) AS latest_ingestion_time
FROM fact_orders;
```

```sql
SELECT MAX(order_date) AS latest_order_date
FROM fact_orders;
```

Freshness rule:

```text
latest partition for fact_orders must be available by 7 AM daily
```

Freshness dimensions:

```text
source freshness
raw landing freshness
silver freshness
gold freshness
dashboard freshness
```

Common failure modes:

```text
source job failed
file missing
stream lag
CDC connector stopped
transformation failed
gold table not published
```

Interview line:

```text
Freshness should be measured at the consumer-facing table, not only at raw ingestion.
```


## 22. Completeness Checks

Completeness checks ensure expected data exists.

Examples:

```text
expected files arrived
expected partition exists
row count is non-zero
all required columns exist
all expected stores/countries/products are present
```

SQL:

```sql
SELECT COUNT(*) AS rows_loaded
FROM fact_orders
WHERE order_date = DATE '2026-01-15';
```

Missing expected dimension combinations:

```sql
SELECT
  s.store_id,
  c.calendar_date
FROM stores s
CROSS JOIN calendar c
LEFT JOIN sales_daily d
  ON s.store_id = d.store_id
 AND c.calendar_date = d.sales_date
WHERE d.store_id IS NULL;
```

Interview line:

```text
Completeness is about expected data, not just non-zero row counts.
```


## 23. Uniqueness Checks

Uniqueness checks ensure keys are not duplicated.

Primary key check:

```sql
SELECT
  order_id,
  COUNT(*) AS row_count
FROM fact_orders
GROUP BY order_id
HAVING COUNT(*) > 1;
```

Composite key check:

```sql
SELECT
  user_id,
  feature_date,
  COUNT(*) AS row_count
FROM user_features_daily
GROUP BY user_id, feature_date
HAVING COUNT(*) > 1;
```

Severity:

```text
duplicate primary keys in curated/gold tables are usually critical
```

Interview line:

```text
Uniqueness checks must match the table grain.
```


## 24. Null Checks

Null checks validate required fields.

Example:

```sql
SELECT COUNT(*) AS null_order_ids
FROM fact_orders
WHERE order_id IS NULL;
```

Multi-column required check:

```sql
SELECT COUNT(*) AS bad_rows
FROM fact_orders
WHERE order_id IS NULL
   OR user_id IS NULL
   OR order_time IS NULL;
```

Null rate check:

```sql
SELECT
  SUM(CASE WHEN user_id IS NULL THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS null_rate
FROM events
WHERE event_date = DATE '2026-01-15';
```

Interview line:

```text
Null checks should distinguish required fields from optional fields and should often use rates, not only counts.
```


## 25. Validity Checks

Validity checks ensure values are allowed.

Accepted values:

```sql
SELECT status, COUNT(*)
FROM orders
WHERE status NOT IN ('PENDING', 'COMPLETED', 'CANCELLED', 'REFUNDED')
GROUP BY status;
```

Range check:

```sql
SELECT COUNT(*)
FROM payments
WHERE amount < 0;
```

Regex or format check:

```text
email format
phone number format
country code format
postal code format
```

Date validity:

```sql
SELECT COUNT(*)
FROM orders
WHERE order_time > CURRENT_TIMESTAMP;
```

Interview line:

```text
Validity checks enforce business domains and catch impossible values.
```


## 26. Referential Integrity Checks

Referential integrity checks ensure facts match dimensions.

Example:

```sql
SELECT COUNT(*) AS missing_users
FROM fact_orders o
LEFT JOIN dim_user u
  ON o.user_id = u.user_id
WHERE u.user_id IS NULL;
```

Common checks:

```text
orders.user_id exists in dim_user
order_items.product_id exists in dim_product
events.session_id exists in sessions
payments.order_id exists in orders
```

Nuance:

```text
Late-arriving dimensions may require grace periods.
Unknown dimension rows can be used intentionally.
```

Interview line:

```text
Referential integrity checks must account for late-arriving facts and dimensions.
```


## 27. Consistency Checks

Consistency checks validate relationships within or across data.

Examples:

```text
order_total equals sum(order_items)
payment currency matches order currency
cancelled order has cancellation timestamp
end_date >= start_date
is_current matches effective_to IS NULL
```

SQL example:

```sql
SELECT
  o.order_id,
  o.total_amount,
  SUM(oi.quantity * oi.unit_price) AS item_total
FROM orders o
JOIN order_items oi
  ON o.order_id = oi.order_id
GROUP BY o.order_id, o.total_amount
HAVING ABS(o.total_amount - SUM(oi.quantity * oi.unit_price)) > 0.01;
```

Interview line:

```text
Consistency checks catch business logic contradictions that simple null checks miss.
```


## 28. Reconciliation Checks

Reconciliation compares source and target.

Types:

```text
row count reconciliation
key set reconciliation
sum/metric reconciliation
hash reconciliation
sample record reconciliation
partition-level reconciliation
```

Count example:

```sql
SELECT
  source_count,
  target_count,
  source_count - target_count AS count_diff
FROM reconciliation_summary;
```

Amount total example:

```sql
SELECT
  source_payment_total,
  target_payment_total,
  source_payment_total - target_payment_total AS diff
FROM payment_reconciliation;
```

Interview line:

```text
For critical pipelines, source-to-target reconciliation is stronger than only checking target table constraints.
```


## 29. Schema Checks

Schema checks validate structure.

Check:

```text
expected columns exist
unexpected critical columns not missing
data types match
nullable vs required fields match
schema version is allowed
nested schema compatible
```

Failure examples:

```text
amount changed from numeric to string
required column missing
new enum field added without mapping
source renamed customer_id to client_id
```

Interview line:

```text
Schema checks should fail fast on breaking changes before bad data reaches trusted layers.
```


## 30. Volume Checks

Volume checks detect unusual row counts or data size.

Examples:

```text
row count > 0
row count within 20% of 7-day average
file size within expected range
hourly event count does not drop to zero
delete count not unusually high
```

SQL example:

```sql
WITH today AS (
  SELECT COUNT(*) AS row_count
  FROM events
  WHERE event_date = CURRENT_DATE
),
baseline AS (
  SELECT AVG(row_count) AS avg_row_count
  FROM daily_event_counts
  WHERE event_date BETWEEN CURRENT_DATE - INTERVAL '8 days'
                      AND CURRENT_DATE - INTERVAL '1 day'
)
SELECT
  today.row_count,
  baseline.avg_row_count
FROM today, baseline
WHERE today.row_count < baseline.avg_row_count * 0.5;
```

Interview line:

```text
Volume checks are useful early-warning signals but need historical context to avoid false positives.
```


## 31. Anomaly Detection Checks

Anomaly checks detect unusual changes.

Examples:

```text
row count spike/drop
null rate spike
duplicate rate spike
revenue spike/drop
category distribution shift
CDC delete spike
late-arrival spike
```

Methods:

```text
static thresholds
rolling averages
standard deviation bands
same weekday comparison
seasonality-aware thresholds
manual business thresholds
```

Caution:

```text
Anomaly checks should often start in warning mode to avoid noisy pipeline failures.
```

Interview line:

```text
Anomaly detection is valuable, but thresholds must be tuned to reduce false positives.
```


## 32. Accuracy Checks

Accuracy checks compare data with a trusted source or business truth.

Examples:

```text
finance totals match payment provider
warehouse order count matches source database
billing amounts match invoice system
inventory stock matches warehouse management system
```

Accuracy is hard because:

```text
truth source may be delayed
systems may have different cutoffs
business rules may differ
late-arriving data can change totals
```

Interview line:

```text
Accuracy checks require a defined source of truth and agreed reconciliation rules.
```


## 33. Timeliness Checks

Timeliness checks ensure data arrives and is processed within expected time.

Examples:

```text
partner file must arrive by 2 AM
raw landing must finish by 3 AM
gold mart must publish by 7 AM
CDC lag must stay under 15 minutes
stream processing delay under 5 minutes
```

Implementation:

```text
compare expected time vs actual arrival/publish time
```

Interview line:

```text
Timeliness is end-to-end: source arrival, pipeline processing, and consumer availability.
```


## 34. Distribution Checks

Distribution checks validate data shape.

Examples:

```text
country distribution changed unexpectedly
payment method mix shifted
event_name distribution shifted
status distribution changed
feature distribution drifted
```

Approaches:

```text
top category comparison
percentage share thresholds
histogram comparison
statistical drift metrics if required
```

Interview line:

```text
Distribution checks are useful for detecting subtle data shifts that row counts cannot catch.
```


## 35. Business Rule Checks

Business rules are domain-specific.

Examples:

```text
completed order must have completed_at
refunded order must have refund amount
payment amount cannot exceed order amount by more than tolerance
subscription end date must be after start date
active user cannot have deleted status
finance report must balance debits and credits
```

Interview line:

```text
The highest-value DQ checks often come from business rules, not generic technical checks.
```


## 36. DQ Execution Engine

The execution engine runs configured checks.

Execution options:

```text
SQL engine for warehouse/lakehouse checks
Spark for large lake checks
Python for file/API checks
stream processor for streaming DQ
dbt tests for transformation-layer checks
Great Expectations-style expectations for declarative checks
```

Engine responsibilities:

```text
read active rules
parameterize by dataset/partition/date
execute checks
capture actual values
write result rows
write failure samples if needed
trigger gate decision
emit metrics
```

Interview line:

```text
The execution engine should run checks from metadata and write standardized results.
```


## 37. DQ Result Storage

Result storage makes DQ observable over time.

Store:

```text
rule_id
dataset
partition/date
status
severity
actual_value
expected_value
failure_count
sample_failure_path
run_id
duration
error_message
owner
timestamp
```

Benefits:

```text
trend analysis
incident debugging
SLA reporting
quality scorecards
owner accountability
audit trail
false positive tuning
```

Interview line:

```text
If DQ results are not stored historically, the team cannot measure quality trends or prove improvement.
```


## 38. Failure Sample Storage

Failure samples help debugging.

Example sample table:

```text
dq_failure_samples
- run_id
- rule_id
- dataset_name
- business_key
- failed_column
- failed_value
- error_reason
- source_record_metadata
- detected_at
```

Guidelines:

```text
limit sample size
avoid exposing PII unnecessarily
store path to quarantine if large
include enough keys to reproduce issue
```

Interview line:

```text
Alerts should include enough failure context to debug without scanning the entire table manually.
```


## 39. Quarantine Design

Quarantine stores bad records separately.

Use quarantine for:

```text
malformed files
invalid JSON
missing required key
bad data type
invalid enum
failed business rule
unmatched reference record if policy requires
```

Quarantine metadata:

```text
raw_record
dataset
batch_id
rule_id
error_type
error_message
field_name
detected_at
owner
status
```

Policy:

```text
critical bad records may block pipeline
non-critical bad records may be quarantined and reported
```

Interview line:

```text
Quarantine should make bad data visible and recoverable, not silently dropped.
```


## 40. Pipeline Integration

DQ should integrate with orchestration.

Typical pipeline:

```text
extract
land raw
run bronze checks
stage/clean
run silver checks
build curated
run curated checks
build gold
run gold checks
publish/certify
alert/report
```

Behavior:

```text
critical failure stops publish
warning failure continues with degraded status
info result logged
```

Interview line:

```text
DQ checks should gate data promotion between layers, not run only after consumers complain.
```


## 41. Alerting Design

Alerts should be actionable.

Alert content:

```text
dataset
rule name
severity
actual vs expected
affected partition
owner
run_id
failure sample link
dashboard link
runbook link
recommended action
```

Routing:

```text
critical → on-call/page/channel
warning → owner channel/ticket
info → dashboard only
```

Avoid alert fatigue:

```text
deduplicate repeated alerts
group related failures
use severity
start noisy anomaly checks as warnings
auto-resolve alerts when checks pass
```

Interview line:

```text
A DQ alert must tell the owner what failed, where, why it matters, and how to investigate.
```


## 42. DQ Dashboard Design

DQ dashboards should show:

```text
overall quality score by domain
failed checks by severity
freshness status by dataset
row count trends
null rate trends
duplicate rate trends
schema changes
quarantine counts
reconciliation status
top failing datasets
SLA misses
owner/team breakdown
```

Views:

```text
executive summary
domain owner view
pipeline operator view
dataset detail view
rule detail view
incident history
```

Interview line:

```text
DQ dashboards should make data health visible at dataset, domain, and platform levels.
```


## 43. Quality Score

A quality score can summarize data health.

Inputs:

```text
freshness status
critical check failures
warning count
DQ pass rate
incident count
SLA misses
quarantine rate
reconciliation status
```

Caution:

```text
quality scores can hide critical failures if weighted badly
do not average away critical issues
```

Example policy:

```text
any critical failure = red
warnings reduce score but do not hide critical pass/fail
```

Interview line:

```text
Quality scorecards are useful, but critical failures should never be hidden by averages.
```


## 44. Remediation Workflow

A DQ framework should support fixing issues.

Workflow:

```text
detect failure
alert owner
create ticket if needed
investigate source/pipeline issue
fix data or rule
rerun affected pipeline/check
validate result
close incident
record root cause
add preventive check if needed
```

Ticket fields:

```text
dataset
rule
severity
owner
failure sample
affected partitions
business impact
status
resolution
root cause
```

Interview line:

```text
DQ is only valuable if failures lead to ownership, remediation, and prevention.
```


## 45. False Positive Management

False positives reduce trust.

Common causes:

```text
bad threshold
seasonality ignored
business event like sale/campaign
source migration
new valid enum
temporary expected delay
```

Management:

```text
test mode before blocking
warning mode before critical
threshold tuning
same-weekday comparisons
owner approval for rule changes
snooze with expiry
incident notes
```

Interview line:

```text
I would roll out noisy rules in observe or warning mode before making them blocking.
```


## 46. Batch Pipeline DQ

- check expected partitions arrived
- check row counts after load
- check duplicate business keys
- check required fields
- check source-target reconciliation
- check mart totals against curated facts
- block publish on critical failures

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 47. Streaming DQ

- monitor stream lag
- validate schema per message
- track malformed message rate
- track late event rate
- track dropped record count
- check event-time completeness by window
- alert on volume drops/spikes

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 48. CDC DQ

- operation type valid
- primary key not null
- source_lsn/offset present
- duplicate CDC event rate
- delete count trends
- target current table duplicate keys
- source-target row count reconciliation
- CDC lag within SLA

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 49. Data Lake DQ

- bronze file readable
- schema captured
- silver type casting success
- quarantine rate
- gold metric reconciliation
- file count and small-file monitoring
- partition freshness

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 50. Warehouse DQ

- dimension key uniqueness
- fact table row count by partition
- referential integrity
- SCD interval validity
- mart grain uniqueness
- metric totals
- dashboard freshness

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 51. ML Feature DQ

- one row per entity + feature_date
- no future data leakage
- feature null rate thresholds
- feature distribution drift
- label availability
- training-serving consistency
- freshness for inference features

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 52. Finance DQ

- strict source-target reconciliation
- amount totals by currency
- debit-credit balance
- duplicate transaction IDs
- missing provider/internal transactions
- status mismatch
- critical failures block publish

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 53. API Ingestion DQ

- API response status success
- pagination completeness
- schema compatibility
- required ID fields
- duplicate object IDs
- cursor not advanced before success
- rate limit/error rate monitoring

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 54. File Ingestion DQ

- expected file arrived
- checksum matches
- manifest row count matches
- file not previously processed
- schema valid
- bad row count under threshold
- late/missing file alert

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 55. Dashboard DQ

- published table freshness
- metric totals reconcile
- dimension filters populated
- no duplicate dashboard grain
- top metrics not null
- certified dataset status visible

Interview line:

```text
DQ checks should be tailored to the pipeline type and business risk.
```


## 56. Practice Case 1: Daily Sales Mart DQ Framework

Prompt:

```text
Design a data quality framework for daily sales mart dq framework.
```

Dataset / Area:

```text
sales reporting mart
```

Goal:

```text
trusted dashboard data
```

Strong design points:

- freshness check by report_date before 7 AM
- row count by sales_date compared to historical baseline
- order_id uniqueness in fact_orders
- revenue total in mart reconciles to fact_orders
- country/category values are valid
- critical failures block dashboard publish
- warnings alert data owner
- DQ dashboard shows revenue trends, failures, and SLA misses

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 57. Practice Case 2: CDC Orders DQ Framework

Prompt:

```text
Design a data quality framework for cdc orders dq framework.
```

Dataset / Area:

```text
orders_current from CDC
```

Goal:

```text
accurate current-state replication
```

Strong design points:

- operation type and source_lsn required
- order_id not null
- dedupe duplicate CDC events by order_id + source_lsn
- target has one row per order_id
- delete count monitored for spikes
- CDC lag monitored against SLA
- source-target row count reconciliation runs periodically
- raw CDC retained for replay

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 58. Practice Case 3: Data Lake DQ Framework

Prompt:

```text
Design a data quality framework for data lake dq framework.
```

Dataset / Area:

```text
bronze/silver/gold lake
```

Goal:

```text
trusted lake data products
```

Strong design points:

- bronze file readability and schema capture
- silver casting and required field checks
- quarantine invalid records with metadata
- gold metric reconciliation
- catalog stores quality status
- critical gold failures block certification
- file count and small-file health tracked

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 59. Practice Case 4: Partner File DQ Framework

Prompt:

```text
Design a data quality framework for partner file dq framework.
```

Dataset / Area:

```text
daily partner CSV files
```

Goal:

```text
validated partner data
```

Strong design points:

- expected file arrival by deadline
- checksum and manifest validation
- schema and delimiter validation
- row count matches manifest
- duplicate file detection
- bad rows quarantined
- late/missing file alerts
- file audit table stores status

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 60. Practice Case 5: Finance Reconciliation DQ Framework

Prompt:

```text
Design a data quality framework for finance reconciliation dq framework.
```

Dataset / Area:

```text
payments and bank/provider files
```

Goal:

```text
finance trusted reports
```

Strong design points:

- transaction_id uniqueness
- amount totals by currency
- source-target full outer comparison
- status mismatch detection
- missing provider/internal transaction detection
- critical mismatch blocks publish
- audit history retained
- owner escalation and incident ticketing

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 61. Practice Case 6: ML Feature DQ Framework

Prompt:

```text
Design a data quality framework for ml feature dq framework.
```

Dataset / Area:

```text
user_features_daily
```

Goal:

```text
training and inference features
```

Strong design points:

- one row per user_id + feature_date
- feature freshness by feature_date
- null rate checks per feature
- distribution drift checks
- point-in-time leakage checks
- training-serving consistency checks
- warnings for drift, critical for missing key features
- feature quality dashboard

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 62. Practice Case 7: Streaming Event DQ Framework

Prompt:

```text
Design a data quality framework for streaming event dq framework.
```

Dataset / Area:

```text
clickstream events
```

Goal:

```text
event analytics
```

Strong design points:

- schema validation per event
- malformed event rate
- late event rate
- stream lag
- event volume by hour
- null user_id rate
- duplicate event_id rate
- quarantine bad events

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 63. Practice Case 8: Customer 360 DQ Framework

Prompt:

```text
Design a data quality framework for customer 360 dq framework.
```

Dataset / Area:

```text
customer_360 table
```

Goal:

```text
one row per customer snapshot
```

Strong design points:

- one row per user_id + snapshot_date
- source freshness by domain
- lifetime revenue reconciles to orders
- ticket counts reconcile to support facts
- current plan matches subscription table
- null key checks
- metric distribution anomaly detection

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 64. Practice Case 9: SCD Dimension DQ Framework

Prompt:

```text
Design a data quality framework for scd dimension dq framework.
```

Dataset / Area:

```text
dim_user_history
```

Goal:

```text
valid historical dimensions
```

Strong design points:

- one current row per user
- no overlapping effective intervals
- effective_from before effective_to
- valid current flag
- attribute changes tracked correctly
- delete/end-date behavior validated
- as-of join sample checks

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 65. Practice Case 10: DQ Platform for Enterprise

Prompt:

```text
Design a data quality framework for dq platform for enterprise.
```

Dataset / Area:

```text
many domains and datasets
```

Goal:

```text
central DQ platform
```

Strong design points:

- metadata-driven rule config
- domain ownership
- standard result table
- severity model
- orchestrator integration
- catalog quality status
- central dashboard
- alert routing and runbooks
- cost-aware partition-level execution

Minimum interview answer must include:

```text
rule config
execution
result storage
severity
quality gates
alerts
ownership
dashboard
remediation
trade-offs
```

Interview line:

```text
Tie DQ checks to business impact and pipeline publish decisions.
```


## 66. Data Observability vs Data Quality

Data quality focuses on whether data meets rules.

Data observability monitors data health more broadly.

Observability includes:

```text
freshness
volume
schema changes
lineage
quality checks
pipeline health
usage
cost
```

Interview line:

```text
Data quality is rule validation; data observability is the broader monitoring of data health and behavior.
```


## 67. Data Contracts and DQ

Data contracts prevent quality issues upstream.

Contract includes:

```text
schema
primary key
required fields
valid values
freshness SLA
update/delete semantics
owner
evolution rules
```

DQ framework uses contracts to:

```text
validate schema
validate required fields
validate allowed values
alert producers on violations
block breaking changes
```

Interview line:

```text
Data contracts shift quality left by defining expectations before data reaches downstream pipelines.
```


## 68. Cost-Aware DQ Execution

DQ checks can be expensive.

Cost controls:

```text
run checks on affected partitions
sample non-critical checks
use metadata counts where safe
reuse pipeline aggregates
schedule heavy checks off-peak
avoid full table scans daily
prioritize critical datasets
incremental reconciliation
```

Interview line:

```text
DQ should be cost-aware; not every check needs to scan all history every run.
```


## 69. DQ for Large Tables

Large-table strategy:

```text
partition-level checks daily
full-table checks weekly/monthly
sample row-level checks where acceptable
metadata-based file/partition checks
incremental source-target reconciliation
precomputed audit summaries
```

Interview line:

```text
For large tables, I validate recent/affected partitions frequently and run full checks less often.
```


## 70. DQ for Late-Arriving Data

Late data complicates quality.

Issues:

```text
row counts change after initial publish
metrics may be corrected
freshness and completeness depend on business date
```

Strategy:

```text
track ingestion_date and event_date
use lookback windows
run DQ after partition overwrite
monitor late-arrival rate
define closed-period policy
```

Interview line:

```text
DQ must account for late data by checking affected business-date partitions, not only ingestion date.
```


## 71. DQ and Certification

Certified datasets should meet higher standards.

Certification requires:

```text
owner
documentation
grain
freshness SLA
core DQ checks
lineage
access policy
quality status dashboard
```

Certification can be revoked if:

```text
critical checks fail
freshness SLA repeatedly missed
owner missing
definition undocumented
```

Interview line:

```text
Certification helps consumers know which datasets are safe for business use.
```


## 72. DQ Incident Management

DQ incidents should be tracked.

Incident fields:

```text
incident_id
dataset
rule_id
severity
business impact
owner
detected_at
resolved_at
root_cause
resolution
preventive_action
```

Benefits:

```text
recurring issue detection
SLA reporting
root cause tracking
team accountability
continuous improvement
```

Interview line:

```text
DQ incidents should produce root-cause learning, not only one-time alerts.
```


## 73. DQ Framework Trade-Offs

Common trade-offs:

```text
blocking vs availability
strict checks vs false positives
full scans vs cost
generic framework vs custom business checks
central ownership vs domain ownership
sampling vs exact validation
automatic quarantine vs fail-fast
speed vs accuracy
```

Interview line:

```text
DQ design is about balancing trust, cost, noise, and business impact.
```


## 74. DQ Anti-Patterns

Avoid:

```text
only null checks
hardcoded checks spread across pipelines
no result history
no severity levels
no owners
no alert routing
no runbooks
no quarantine
no reconciliation
full table scans for every check every day
blocking noisy anomaly checks too early
ignoring false positives
checking only after bad data reaches dashboards
```

Interview line:

```text
A DQ framework without ownership and action is just logging.
```


## 75. Rollout Strategy

Roll out DQ gradually.

Steps:

```text
start with critical datasets
add basic checks first
run new rules in observe mode
tune thresholds
move to warning mode
move critical stable checks to blocking mode
add dashboards and ownership
expand by domain
```

Interview line:

```text
I would not turn every new DQ rule into a blocking check on day one.
```


## 76. Pattern Classification Drill

### Gold table missing today's partition

```text
Freshness/completeness critical check.
```

### fact_orders has duplicate order_id

```text
Uniqueness critical check.
```

### status has new unexpected value

```text
Validity/schema/domain check.
```

### orders.user_id missing in dim_user

```text
Referential integrity check.
```

### revenue dropped 80% from normal

```text
Volume/anomaly check.
```

### payment provider total differs from warehouse

```text
Reconciliation/accuracy check.
```

### source added nullable column

```text
Schema evolution safe additive check.
```

### source changed amount type

```text
Breaking schema check.
```

### bad JSON records found

```text
Quarantine malformed records.
```

### critical check failed before gold publish

```text
Quality gate blocks publish.
```

### optional field null rate increased

```text
Warning null-rate check.
```

### new anomaly rule too noisy

```text
Observe/warning mode and threshold tuning.
```

### stream lag increasing

```text
Streaming freshness/timeliness check.
```

### CDC delete count spikes

```text
CDC anomaly check.
```

### ML feature distribution shifts

```text
Feature drift check.
```

### DQ scans all history daily

```text
Cost issue; use partition-level checks.
```

### alert has no owner

```text
Ownership/routing metadata missing.
```

### dashboard shows quality unknown

```text
DQ result/catalog integration missing.
```

### bad records silently dropped

```text
Quarantine/reporting failure.
```

### same incident repeats weekly

```text
Incident root-cause/prevention failure.
```


## 77. High-ROI DQ Topics

### quality dimensions

```text
freshness, completeness, uniqueness, validity, consistency, accuracy
```

### rule config

```text
metadata-driven checks
```

### result storage

```text
historical tracking
```

### severity

```text
critical/warning/info
```

### quality gates

```text
block/warn/quarantine/observe
```

### freshness

```text
consumer-facing SLA
```

### completeness

```text
expected data exists
```

### uniqueness

```text
grain keys are unique
```

### validity

```text
allowed values and ranges
```

### referential integrity

```text
facts match dimensions
```

### reconciliation

```text
source-target trust
```

### anomaly detection

```text
trend-based checks
```

### quarantine

```text
bad record isolation
```

### alerting

```text
owner and runbook
```

### dashboard

```text
quality visibility
```

### remediation

```text
ticket/root cause/prevention
```

### cost

```text
partition-level checks
```

### rollout

```text
observe to warning to blocking
```


## 78. Review Checklist

### Did candidate clarify critical datasets and consumers?

```text
Business impact drives severity.
```

### Did candidate define DQ dimensions?

```text
Completeness beyond nulls.
```

### Did candidate design rule config?

```text
Scalable framework.
```

### Did candidate design execution engine?

```text
How checks run.
```

### Did candidate design result storage?

```text
History and dashboard.
```

### Did candidate define severity?

```text
Critical vs warning.
```

### Did candidate define quality gates?

```text
Block/warn/quarantine.
```

### Did candidate define quarantine?

```text
Bad record handling.
```

### Did candidate define alerting?

```text
Owner and action.
```

### Did candidate define dashboards?

```text
Visibility.
```

### Did candidate include reconciliation?

```text
Accuracy/trust.
```

### Did candidate include anomaly detection?

```text
Trend monitoring.
```

### Did candidate include cost controls?

```text
Large-scale practicality.
```

### Did candidate integrate with orchestration?

```text
Pipeline gates.
```

### Did candidate discuss false positives?

```text
Operational maturity.
```

### Did candidate define remediation?

```text
Closure and prevention.
```

### Did candidate discuss security?

```text
PII-safe samples/results.
```

### Did candidate explain trade-offs?

```text
System design maturity.
```


## 79. Weakness Repair Map

### Only says null checks

```text
Practice full quality dimensions.
```

### No rule config

```text
Practice metadata-driven framework.
```

### No result table

```text
Practice DQ results schema.
```

### No severity

```text
Practice critical/warning/info cases.
```

### No gates

```text
Practice publish-blocking scenarios.
```

### No alerts/owners

```text
Practice ownership model.
```

### No reconciliation

```text
Practice source-target checks.
```

### No quarantine

```text
Practice bad record flows.
```

### No cost thinking

```text
Practice partition-level checks.
```

### No false-positive handling

```text
Practice rollout and threshold tuning.
```

### Poor communication

```text
Practice DQ architecture script.
```


## 80. 7-Day DQ Framework Study Plan

### Day 1

```text
DQ dimensions, severity, quality gates.
```

### Day 2

```text
Rule config, result tables, execution engine.
```

### Day 3

```text
Freshness, completeness, uniqueness, null, validity checks.
```

### Day 4

```text
Referential integrity, reconciliation, anomaly detection.
```

### Day 5

```text
Quarantine, alerting, dashboards, ownership, remediation.
```

### Day 6

```text
Batch, streaming, CDC, data lake, ML feature DQ cases.
```

### Day 7

```text
Full DQ framework mock and weakness repair.
```


## 81. 30-Day DQ Framework Study Plan

### Week 1

```text
Foundation: dimensions, rules, severity, result storage.
```

### Week 2

```text
Checks: freshness, completeness, uniqueness, reconciliation, anomalies.
```

### Week 3

```text
Operations: gates, alerts, quarantine, dashboards, remediation.
```

### Week 4

```text
Case studies: finance, CDC, lake, streaming, ML, mocks.
```


## 82. Timed Interview Protocol

### 0-5 minutes

```text
Clarify datasets, consumers, impact, SLA, ownership.
```

### 5-12 minutes

```text
Draw rules → engine → results → gates → alerts architecture.
```

### 12-22 minutes

```text
Deep dive checks and quality dimensions.
```

### 22-32 minutes

```text
Deep dive severity, gates, quarantine, remediation.
```

### 32-40 minutes

```text
Discuss dashboards, cost, scaling, security, false positives.
```

### 40-45 minutes

```text
Trade-offs and final summary.
```


## 83. DQ Framework Whiteboard Template

```text
Requirements:
- critical datasets:
- consumers:
- business impact:
- SLA:
- owners:
- pipeline types:
- data volume:

Architecture:
datasets → rule config → execution engine → result store → quality gates → alerts/dashboard/remediation

Rules:
- check types:
- severity:
- thresholds:
- schedule:
- owner:
- blocking behavior:

Operations:
- quarantine:
- alerting:
- dashboard:
- remediation:
- false-positive handling:
- cost controls:
- security:
```


## 84. DQ Rule Template

```text
rule_id:
rule_name:
dataset_name:
layer:
column_name:
check_type:
rule_definition:
expected_value:
threshold:
severity:
blocking_flag:
owner_team:
schedule:
partition_filter:
failure_sample_enabled:
runbook_url:
is_active:
```


## 85. DQ Result Template

```text
run_id:
rule_id:
dataset_name:
partition_value:
status:
severity:
actual_value:
expected_value:
failure_count:
failure_sample_location:
started_at:
completed_at:
duration_seconds:
error_message:
owner_team:
```


## 86. DQ Alert Template

```text
Severity:
Dataset:
Partition:
Rule:
Actual:
Expected:
Business impact:
Owner:
Run ID:
Failure samples:
Dashboard:
Runbook:
Recommended next action:
```


## 87. Quarantine Template

```text
quarantine_id:
dataset_name:
source_system:
batch_id:
business_key:
raw_record:
failed_rule_id:
error_type:
error_message:
field_name:
detected_at:
owner_team:
status:
resolution_notes:
```


## 88. Mock Set 1: DQ Framework Foundation

Problems:

- Design a metadata-driven DQ framework.
- Design a DQ rule config table.
- Design a DQ result table.
- Define severity and gate behavior.
- Explain where checks run in a pipeline.

Expected answer must include:

```text
rules
execution
results
severity
gates
alerts
dashboard
ownership
remediation
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 89. Mock Set 2: Core Checks

Problems:

- Design freshness checks.
- Design completeness checks.
- Design uniqueness checks.
- Design validity checks.
- Design referential integrity checks.

Expected answer must include:

```text
rules
execution
results
severity
gates
alerts
dashboard
ownership
remediation
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 90. Mock Set 3: Advanced Checks

Problems:

- Design source-target reconciliation.
- Design anomaly detection for row counts.
- Design distribution drift checks.
- Design schema evolution checks.
- Design business rule checks.

Expected answer must include:

```text
rules
execution
results
severity
gates
alerts
dashboard
ownership
remediation
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 91. Mock Set 4: Operations

Problems:

- Design quarantine handling.
- Design DQ alerting.
- Design DQ dashboard.
- Design remediation workflow.
- Handle false positives and threshold tuning.

Expected answer must include:

```text
rules
execution
results
severity
gates
alerts
dashboard
ownership
remediation
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 92. Mock Set 5: Case Designs

Problems:

- Design DQ for daily sales mart.
- Design DQ for CDC pipeline.
- Design DQ for data lake.
- Design DQ for finance reconciliation.
- Design DQ for ML features.

Expected answer must include:

```text
rules
execution
results
severity
gates
alerts
dashboard
ownership
remediation
trade-offs
```

Passing standard:

```text
Average score >= 4/5.
```


## 93. Data Quality FAQ

### FAQ 1: What is a data quality framework?

```text
A system for defining, executing, storing, monitoring, and acting on data quality rules.
```

### FAQ 2: What are the main DQ dimensions?

```text
Freshness, completeness, uniqueness, validity, consistency, accuracy, referential integrity, and volume.
```

### FAQ 3: What is a quality gate?

```text
A control point that blocks, warns, quarantines, or observes based on check results.
```

### FAQ 4: What should be critical?

```text
Issues that make data unsafe for consumers, such as missing partitions, duplicate primary keys, schema breaks, and finance mismatches.
```

### FAQ 5: Why store DQ results?

```text
For dashboards, trends, incidents, audit, SLA reporting, and threshold tuning.
```

### FAQ 6: What is quarantine?

```text
A controlled area for bad records with error metadata.
```

### FAQ 7: How do you avoid alert fatigue?

```text
Use severity, deduplication, thresholds, observe mode, and actionable alerts.
```

### FAQ 8: How do you make DQ cost-aware?

```text
Run checks on affected partitions, use summaries, sample non-critical checks, and schedule heavy checks appropriately.
```

### FAQ 9: What is reconciliation?

```text
Comparing source and target counts, keys, hashes, or metrics.
```

### FAQ 10: What is the difference between DQ and observability?

```text
DQ validates rules; observability monitors broader data health and behavior.
```


## 94. Candidate Self-Review Questions

After every DQ framework design, candidate should answer:

```text
1. What datasets are critical?
2. Who consumes the data?
3. What is the business impact of failure?
4. What quality dimensions are checked?
5. Which checks are critical?
6. Which checks are warnings?
7. Where do checks run?
8. How are rules configured?
9. How are checks executed?
10. Where are results stored?
11. What does the result schema look like?
12. How do quality gates work?
13. What gets blocked?
14. What gets quarantined?
15. How are alerts routed?
16. Who owns failures?
17. What dashboard exists?
18. How are failure samples stored?
19. How are false positives handled?
20. How are thresholds tuned?
21. How is reconciliation done?
22. How are anomalies detected?
23. How are streaming checks different?
24. How are CDC checks different?
25. How are ML feature checks different?
26. How is cost controlled?
27. How is PII protected in samples/results?
28. How is remediation tracked?
29. How is improvement measured?
30. What trade-offs were chosen?
```

If candidate cannot answer these:

```text
The DQ framework design is not interview-ready.
```


## 95. Final Exit Test

Candidate passes data quality framework system design when they can explain:

```text
1. Data quality framework purpose.
2. Data quality vs data observability.
3. Freshness checks.
4. Completeness checks.
5. Uniqueness checks.
6. Null checks.
7. Validity checks.
8. Referential integrity checks.
9. Consistency checks.
10. Accuracy checks.
11. Reconciliation checks.
12. Schema checks.
13. Volume checks.
14. Anomaly checks.
15. Business rule checks.
16. Rule configuration.
17. Rule lifecycle.
18. Result storage.
19. Failure sample storage.
20. Severity model.
21. Quality gates.
22. Hard vs soft checks.
23. Threshold design.
24. Ownership model.
25. Alerting.
26. Dashboarding.
27. Quarantine.
28. Pipeline integration.
29. Remediation workflow.
30. False positive management.
31. Batch DQ.
32. Streaming DQ.
33. CDC DQ.
34. Data lake DQ.
35. Warehouse DQ.
36. ML feature DQ.
37. Finance DQ.
38. Cost-aware execution.
39. Rollout strategy.
40. Trade-offs and final summary.
```

Passing standard:

```text
Average score >= 4/5.
No null-check-only answers.
No missing rule config.
No missing result storage.
No missing severity/gates.
No missing alerts/ownership.
No missing reconciliation.
No missing remediation.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate designs a metadata-driven, operational, cost-aware DQ framework that works across batch, streaming, CDC, lake, warehouse, finance, and ML use cases.
```


## 96. Final Summary

Data quality framework design is a core Data Engineering system design skill.

The candidate must master:

```text
quality dimensions
rule configuration
rule execution
result storage
severity
quality gates
freshness
completeness
uniqueness
validity
consistency
accuracy
referential integrity
reconciliation
schema checks
volume checks
anomaly detection
business rule checks
quarantine
alerts
dashboards
ownership
runbooks
remediation
false-positive handling
batch DQ
streaming DQ
CDC DQ
lake DQ
warehouse DQ
ML feature DQ
finance DQ
cost-aware execution
security
rollout strategy
trade-offs
```

The mentor must be strict:

```text
Only says null checks → not interview-ready.
No rule config → not interview-ready.
No result history → not interview-ready.
No severity model → not interview-ready.
No quality gates → not interview-ready.
No owner/alert routing → not interview-ready.
No reconciliation → not interview-ready.
No quarantine/remediation → not interview-ready.
No cost control → not interview-ready.
```

Final interview line:

```text
A production data quality framework must define rules, run checks, store results, gate publishing, alert owners, support remediation, and continuously measure trust.
```


## 97. Additional Mini Scenario Cards

### Mini Scenario 1: Gold table missing today's partition

Recommended direction:

```text
Critical freshness/completeness check should block publish.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 2: fact_orders has duplicate order_id

Recommended direction:

```text
Critical uniqueness check based on table grain.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 3: payment amount is negative

Recommended direction:

```text
Validity/range check.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 4: orders.user_id does not exist in dim_user

Recommended direction:

```text
Referential integrity check with late-dimension policy.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 5: Revenue dropped 80%

Recommended direction:

```text
Anomaly/volume check, likely warning until tuned.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 6: Provider total differs from warehouse

Recommended direction:

```text
Source-target reconciliation critical check.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 7: API response schema changed

Recommended direction:

```text
Schema compatibility check.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 8: CSV file row count differs from manifest

Recommended direction:

```text
File completeness check.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 9: Bad JSON records silently dropped

Recommended direction:

```text
Quarantine with error metadata.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 10: Alert sent with no owner

Recommended direction:

```text
Owner metadata/routing missing.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 11: DQ result not stored

Recommended direction:

```text
No historical trend or audit visibility.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 12: Rule fails every Monday due to seasonality

Recommended direction:

```text
Threshold should compare same weekday or use seasonality.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 13: Critical check is too noisy

Recommended direction:

```text
Start observe/warning, tune threshold before blocking.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 14: DQ query scans all history daily

Recommended direction:

```text
Use partition-level or summary checks.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 15: CDC lag exceeds SLA

Recommended direction:

```text
CDC freshness/timeliness alert.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 16: CDC current table has duplicate key

Recommended direction:

```text
Target uniqueness check and merge logic issue.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 17: ML feature null rate spikes

Recommended direction:

```text
Feature null-rate drift check.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 18: ML feature uses future data

Recommended direction:

```text
Point-in-time leakage check.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 19: Finance report published despite mismatch

Recommended direction:

```text
Quality gate missing or misclassified severity.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 20: Quarantine grows but no one reviews

Recommended direction:

```text
Remediation ownership and SLA missing.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 21: Schema adds optional column

Recommended direction:

```text
Safe additive change with catalog update.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 22: Schema changes type of amount

Recommended direction:

```text
Breaking schema check should fail fast.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 23: Dashboard shows stale data

Recommended direction:

```text
Consumer-facing freshness check missing.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 24: Gold metric does not match curated fact

Recommended direction:

```text
Gold reconciliation check.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 25: Duplicate partner file processed

Recommended direction:

```text
File audit and checksum rule.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 26: New enum value appears

Recommended direction:

```text
Validity check may warn and require business approval.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 27: High null rate in optional field

Recommended direction:

```text
Warning null-rate trend check.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 28: DQ alert fatigue

Recommended direction:

```text
Deduplicate alerts, tune thresholds, use severity.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 29: No root-cause tracking

Recommended direction:

```text
DQ incident workflow missing.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 30: PII appears in failure sample

Recommended direction:

```text
Mask samples or restrict result access.
```

Candidate must explain:

```text
1. What failed.
2. Which quality dimension applies.
3. Correct DQ rule or framework behavior.
4. Severity and gate action.
5. Alert/remediation path.
```

Passing score:

```text
4/5 or higher.
```


## 98. Quick Reference Cards

### Card 1: Freshness

Purpose:

```text
Data is updated on time.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 2: Completeness

Purpose:

```text
Expected data exists.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 3: Uniqueness

Purpose:

```text
Keys match table grain without duplicates.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 4: Validity

Purpose:

```text
Values follow allowed domains and ranges.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 5: Consistency

Purpose:

```text
Related data agrees.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 6: Accuracy

Purpose:

```text
Data matches source of truth.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 7: Referential integrity

Purpose:

```text
Facts match dimensions.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 8: Reconciliation

Purpose:

```text
Source-target comparison.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 9: Anomaly detection

Purpose:

```text
Unusual trend detection.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 10: Rule config

Purpose:

```text
Metadata that defines checks.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 11: Result store

Purpose:

```text
Historical check outcomes.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 12: Severity

Purpose:

```text
Critical/warning/info impact.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 13: Quality gate

Purpose:

```text
Block/warn/quarantine/observe decision.
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

### Card 15: Alerting

Purpose:

```text
Owner notification and action.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 16: Dashboard

Purpose:

```text
Quality visibility.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 17: Remediation

Purpose:

```text
Fix workflow and root cause.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 18: False positives

Purpose:

```text
Noisy check management.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 19: Cost-aware DQ

Purpose:

```text
Partition-level and efficient checks.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```

### Card 20: Certified dataset

Purpose:

```text
Trusted dataset with quality status.
```

Interview check:

```text
Explain where it fits, what breaks if missing, and how to validate it.
```
