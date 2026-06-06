# Data Warehouse Guide

Generated: 2026-06-06

This guide teaches **data warehouse concepts for Data Engineering interviews**.

It is written for **Data Engineering Sensei**, a strict, no-sugarcoating Data Engineering interview mentor. The goal is not to memorize warehouse tool names. The goal is to make the candidate able to explain how a warehouse is designed, loaded, modeled, optimized, governed, and defended in interviews.

Use this guide for:

- Data warehouse interview preparation
- SQL interview reasoning
- Data Engineering system design
- Data modeling discussions
- Cloud warehouse discussions
- Project deep dives
- ETL/ELT architecture questions
- Query performance and cost discussions
- Mock interviews and answer review

---

## 1. What Is a Data Warehouse?

A data warehouse is a system used to store, organize, and serve **curated analytical data**.

It is designed for:

- reporting
- dashboards
- business intelligence
- analytics
- aggregated queries
- historical analysis
- decision-making
- metric consistency
- cross-functional data access

A warehouse is not just “a database with a lot of data.”

A weak answer:

```text
A data warehouse is a database where we store data.
```

A strong answer:

```text
A data warehouse is an analytical data store that contains cleaned, modeled, and trusted data from multiple sources. It is optimized for reporting and analysis rather than transactional updates. Data is usually organized into facts, dimensions, marts, or curated tables with clear grain, ownership, quality checks, and refresh logic.
```

---

## 2. Interview Standard

In interviews, the candidate should be able to explain:

1. Why a warehouse exists.
2. How it differs from an operational database.
3. How data gets into the warehouse.
4. How raw, staging, and curated layers are organized.
5. How facts and dimensions are modeled.
6. How incremental loads work.
7. How data quality is enforced.
8. How query performance is improved.
9. How cost is controlled.
10. How access/security is handled.
11. How freshness and SLAs are monitored.
12. How failures and backfills are handled.

If the candidate only says tool names like Snowflake, BigQuery, Redshift, or Synapse, the answer is incomplete.

---

## 3. Warehouse vs Database

## 3.1 Operational Database

Operational databases support applications.

They are usually:

- transaction-oriented
- normalized
- optimized for inserts/updates/deletes
- low-latency for small queries
- used by live applications
- focused on current state

Examples:

- customer profile database
- order management database
- payment transaction database
- inventory system

## 3.2 Data Warehouse

Data warehouses support analytics.

They are usually:

- read-heavy
- optimized for scans and aggregations
- denormalized or dimensional
- historical
- used by analysts and dashboards
- integrated from multiple sources

### Interview comparison

| Area | Operational Database | Data Warehouse |
|---|---|---|
| Purpose | Run application | Analyze business |
| Workload | Transactions | Analytical queries |
| Schema | normalized | dimensional / curated |
| Query pattern | point lookup | scans, joins, aggregates |
| Data freshness | real-time app state | batch/near-real-time analytics |
| Users | application services | analysts, BI, data science |
| Updates | frequent row updates | periodic loads, merges, append |

### Strong answer

```text
An operational database is optimized for transactional workloads, while a warehouse is optimized for analytical workloads. Data Engineering pipelines often extract data from OLTP systems and load modeled, historical data into a warehouse for reporting.
```

---

## 4. Warehouse vs Data Lake

## 4.1 Data Lake

A data lake stores raw and processed files, often in object storage.

Good for:

- raw data retention
- semi-structured data
- cheap storage
- replayability
- large historical storage
- flexible processing

Risks:

- poor governance
- messy data
- unclear quality
- harder direct BI usage

## 4.2 Data Warehouse

A warehouse stores curated analytical data.

Good for:

- governed analytics
- BI dashboards
- SQL reporting
- metric consistency
- business-ready tables

Risks:

- cost
- modeling effort
- less raw flexibility
- performance issues if poorly designed

### Strong answer

```text
A data lake is better for raw flexible storage and replay, while a data warehouse is better for trusted, modeled, analytics-ready data. In many architectures, raw data lands in a lake and curated data is loaded into the warehouse.
```

---

## 5. Warehouse vs Lakehouse

A lakehouse tries to combine data lake storage with warehouse-like table management.

### Lakehouse concepts

- object storage
- open table formats
- transactional table support
- schema evolution
- time travel
- metadata layer
- compute separation
- governed tables

### Strong answer

```text
A lakehouse is useful when teams want the flexibility and cost of data lake storage but also need warehouse-like reliability, table management, and governance. It can reduce duplication between lake and warehouse layers, but it still requires good modeling and quality practices.
```

---

## 6. Warehouse Architecture Layers

A warehouse design usually includes multiple layers.

```text
Source Systems
  ↓
Landing / Raw
  ↓
Staging
  ↓
Integration / Cleaned
  ↓
Core Warehouse
  ↓
Data Marts / Serving
  ↓
BI / Analytics / ML
```

Different companies use different names, but the purpose is similar.

---

## 7. Landing / Raw Layer

The landing or raw layer stores data close to source form.

### Purpose

- preserve original data
- enable replay
- enable debugging
- support backfills
- audit source extracts
- decouple ingestion from transformation

### Strong answer

```text
I would keep a raw layer so that if transformation logic changes or downstream data is corrupted, we can rebuild from the original source extract instead of asking the source system to resend data.
```

### Common mistakes

- not storing raw data
- overwriting raw data
- transforming raw data destructively
- no metadata about ingestion time
- no source file tracking
- no schema capture

---

## 8. Staging Layer

The staging layer prepares raw data for transformation.

### Purpose

- standardize types
- rename columns
- remove clearly invalid records
- deduplicate source extracts
- add metadata
- apply simple validations
- isolate source-specific logic

### Strong answer

```text
Staging tables should be close to source structure but cleaned enough for downstream transformation. They help isolate source-specific issues from the core warehouse model.
```

### Common mistakes

- putting business logic too early
- skipping staging and making transformations hard to debug
- not documenting staging assumptions
- mixing multiple source grains in one table

---

## 9. Core Warehouse Layer

The core warehouse contains integrated, modeled, trusted data.

Typical objects:

- fact tables
- dimension tables
- conformed dimensions
- history-tracked dimensions
- integrated business entities
- standardized metrics

### Strong answer

```text
The core warehouse layer should contain trusted, integrated models with clear grain and ownership. This is where facts, dimensions, and shared business entities are usually maintained.
```

---

## 10. Data Mart / Serving Layer

Data marts are business-specific serving models.

Examples:

- sales mart
- finance mart
- product analytics mart
- marketing mart
- customer success mart
- executive dashboard mart

### Purpose

- simplify analytics
- improve performance
- provide business-friendly tables
- centralize domain-specific metrics
- reduce repeated joins

### Strong answer

```text
Data marts sit on top of the core warehouse and are designed for specific business domains or dashboards. They should not become disconnected sources of truth with inconsistent metrics.
```

---

## 11. Warehouse Schema Design

Warehouses often use:

1. Star schema
2. Snowflake schema
3. Wide tables
4. Data vault patterns
5. One big table / denormalized marts
6. Hybrid approaches

For most interviews, star schema and dimensional modeling are the most important.

---

## 12. Star Schema in Warehouse

A star schema has a central fact table connected to dimensions.

```text
dim_customer
     |
dim_product -- fact_sales -- dim_date
     |
dim_store
```

### Benefits

- analyst-friendly
- simple joins
- clear grain
- good BI compatibility
- reusable dimensions

### Strong answer

```text
In a warehouse, a star schema is useful because it organizes metrics in fact tables and descriptive attributes in dimensions. This makes reporting easier and keeps business grain clear.
```

---

## 13. Snowflake Schema in Warehouse

A snowflake schema normalizes dimensions.

Example:

```text
fact_sales → dim_product → dim_category
```

### Benefits

- less dimension duplication
- cleaner hierarchies
- consistency for large shared dimensions

### Trade-offs

- more joins
- harder for analysts
- possible performance cost
- more complexity

### Strong answer

```text
I would usually prefer star schema for BI simplicity unless the dimension hierarchy is large or reused enough that snowflaking provides clear benefits.
```

---

## 14. Wide Tables in Warehouse

Wide tables combine many fields into one serving table.

### Good for

- dashboards
- self-service analytics
- simpler querying
- performance for fixed use cases

### Risks

- unclear grain
- duplicated data
- expensive refresh
- inconsistent metrics
- hard maintenance

### Strong answer

```text
A wide table can be useful as a serving layer for a dashboard, but I would prefer a governed model underneath. The wide table should be derived from trusted facts and dimensions, not become an ungoverned source of truth.
```

---

## 15. Warehouse Grain

Grain defines what one row represents.

Examples:

- one row per order
- one row per order line item
- one row per payment
- one row per user per day
- one row per product per store per day

### Interview rule

If the candidate cannot define grain, the warehouse model is not ready.

### Strong answer

```text
For sales analytics, I would choose order-line grain if the business needs product-level revenue analysis. If we only model at order grain, we may lose product-level detail or create complicated nested logic.
```

### Common mistakes

- mixed grain tables
- duplicate metrics
- incorrect joins
- using DISTINCT to hide duplicates
- aggregating at wrong level

---

## 16. Fact Tables

Fact tables store measurable business events or states.

Types:

1. Transaction facts
2. Periodic snapshot facts
3. Accumulating snapshot facts

### Transaction fact

Example:

```text
fact_order_line
```

Grain:

```text
one row per order line item
```

### Periodic snapshot fact

Example:

```text
fact_inventory_daily
```

Grain:

```text
one row per product per warehouse per day
```

### Accumulating snapshot fact

Example:

```text
fact_order_lifecycle
```

Tracks milestones:

- order created
- paid
- shipped
- delivered
- returned

### Strong answer

```text
The fact table type depends on the business process. Sales transactions are usually transaction facts, inventory is often a periodic snapshot, and order lifecycle can be modeled as an accumulating snapshot.
```

---

## 17. Dimension Tables

Dimensions provide descriptive context.

Examples:

- customer
- product
- date
- region
- store
- campaign
- channel
- payment method
- device
- merchant

### Strong answer

```text
Dimensions allow analysts to slice and filter facts by descriptive attributes. For example, sales revenue can be grouped by product category, customer segment, region, or date.
```

---

## 18. Slowly Changing Dimensions in Warehouse

Warehouses often need historical dimensions.

## 18.1 SCD Type 1

Overwrite value.

Good for:

- corrections
- fields where history does not matter

Risk:

- history lost

## 18.2 SCD Type 2

Create new version row.

Good for:

- historical reporting
- customer segment changes
- product category changes
- region assignment changes

### Strong answer

```text
SCD Type 2 preserves attribute history. The warehouse keeps multiple versions of a dimension row with effective dates and a current flag. Facts can link to the correct dimension version so historical reports remain accurate.
```

### Common mistakes

- no effective dates
- multiple current rows
- overlapping date ranges
- facts linked to wrong version
- no handling of late-arriving facts

---

## 19. Warehouse Loading Patterns

## 19.1 Full Refresh

Replace full table.

### Good for

- small reference tables
- simple dimensions
- low-volume data
- early prototypes

### Bad for

- huge fact tables
- high-cost refreshes
- source-load-sensitive systems

### Strong answer

```text
Full refresh is simple but does not scale well for large tables. I would use it for small dimensions or reference tables, not large transaction facts.
```

---

## 19.2 Append-Only Load

Add new rows.

### Good for

- immutable events
- logs
- transaction facts
- clickstream

### Risks

- duplicates
- late events
- correction handling
- source retries

### Strong answer

```text
Append-only works well for immutable events, but I still need deduplication keys and quality checks because source or pipeline retries can duplicate data.
```

---

## 19.3 Merge / Upsert

Insert new records and update existing records.

### Good for

- dimensions
- mutable facts
- CDC
- current-state tables
- late updates

### Risks

- expensive merges
- incorrect keys
- update order issues
- non-idempotent logic

### Strong answer

```text
For mutable warehouse tables, I would use merge/upsert logic based on stable keys. The merge should be idempotent so retries do not duplicate data.
```

---

## 19.4 Partition Overwrite

Replace one or more partitions.

### Good for

- daily fact partitions
- backfills
- late-arriving data
- deterministic batch outputs

### Strong answer

```text
For date-partitioned fact tables, replacing affected partitions can make reruns and backfills safer because the same partition is rebuilt deterministically.
```

---

## 20. Incremental Loading in Warehouse

Incremental loading processes only new or changed data.

Common methods:

- updated_at timestamp
- increasing ID
- source partition date
- CDC log
- watermark table
- file arrival tracking

### Strong answer

```text
For large warehouse tables, incremental loading is usually necessary. I would track a watermark, load only new or changed data, validate it, then merge or append depending on table behavior.
```

### Common mistakes

- updating watermark before successful load
- missing late-arriving updates
- ignoring deletes
- no idempotency
- no backfill logic
- no validation

---

## 21. CDC into Warehouse

CDC captures source inserts, updates, and deletes.

### Warehouse application

CDC data may be applied using:

- staging change table
- merge into target
- delete handling
- ordering by change timestamp or log sequence
- offset tracking
- replay capability

### Strong answer

```text
For CDC into a warehouse, I would store raw change events, apply them in order to staging or target tables, handle inserts/updates/deletes, track offsets, and make merges idempotent.
```

### Follow-up questions

1. How do you handle deletes?
2. What if changes arrive out of order?
3. What if the merge fails halfway?
4. How do you replay CDC events?
5. How do you handle schema changes?

---

## 22. Deduplication in Warehouse

Duplicates can occur due to:

- source retries
- pipeline retries
- CDC replay
- duplicate files
- bad joins
- late arriving corrections
- append-only loads

### Deduplication strategy

1. Define table grain.
2. Identify natural key.
3. Define tie-breaker.
4. Use ROW_NUMBER or merge logic.
5. Validate uniqueness.
6. Monitor duplicate rates.

### SQL pattern

```sql
WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY business_key
            ORDER BY updated_at DESC, ingestion_time DESC
        ) AS rn
    FROM staging_table
)
SELECT *
FROM ranked
WHERE rn = 1;
```

### Strong answer

```text
Deduplication should be based on the expected grain and a deterministic tie-breaker. Using DISTINCT blindly is a red flag because it can hide data quality or join problems.
```

---

## 23. Partitioning in Warehouse

Partitioning helps reduce scanned data and improve maintenance.

Common partition columns:

- event_date
- order_date
- transaction_date
- ingestion_date
- snapshot_date

### Strong answer

```text
I would partition large fact tables by the date most commonly used in filters, usually event or transaction date. I would avoid high-cardinality partitions like user_id because they can create too many small partitions.
```

### Date choice

Event date:

- better for analytics
- handles business reporting

Ingestion date:

- better for operational tracking
- useful for raw layer

Sometimes both are needed.

---

## 24. Clustering / Sorting in Warehouse

Clustering, sorting, or similar physical organization helps queries filter inside partitions.

Useful for:

- customer_id
- product_id
- region
- category
- tenant_id
- frequently filtered columns

### Strong answer

```text
Partitioning prunes large date ranges, while clustering or sorting can improve filtering within partitions on common query columns like customer_id or region.
```

---

## 25. Indexes in Warehouse

Traditional indexes are common in OLTP databases, but warehouses often use different optimization techniques.

Depending on platform, warehouses may use:

- columnar storage
- partitions
- clustering/sorting
- zone maps
- materialized views
- statistics
- distribution keys
- search optimization features
- result caching

### Strong answer

```text
In warehouses, performance is often improved through partitioning, clustering, columnar storage, statistics, and materialized aggregates rather than traditional OLTP-style indexes.
```

Do not give one vendor-specific answer unless platform is specified.

---

## 26. Columnar Storage

Columnar storage stores values by column instead of row.

### Why it helps analytics

Analytical queries often read only some columns.

Example:

```sql
SELECT region, SUM(revenue)
FROM fact_sales
WHERE order_date >= '2025-01-01'
GROUP BY region;
```

This query may only need:

- region
- revenue
- order_date

Columnar storage avoids scanning unnecessary columns.

### Strong answer

```text
Columnar storage is efficient for analytics because queries often scan many rows but only a few columns. It also compresses well, which improves performance and cost.
```

---

## 27. Materialized Views and Aggregate Tables

Materialized views or aggregate tables store precomputed results.

### Good for

- repeated dashboard queries
- expensive joins
- expensive aggregations
- stable business metrics
- performance improvement

### Risks

- stale data
- refresh cost
- storage cost
- metric inconsistency if unmanaged

### Strong answer

```text
If dashboards repeatedly run expensive aggregations, I may create aggregate tables or materialized views. But I must manage refresh logic, freshness, and metric consistency.
```

---

## 28. Warehouse Query Performance

Performance depends on:

- table size
- partition pruning
- clustering/sorting
- join strategy
- data skew
- file/table layout
- column selection
- statistics
- materialization
- query design
- warehouse compute size

### SQL anti-patterns

- SELECT *
- no partition filter
- joining huge tables before filtering
- using DISTINCT to hide duplicates
- functions on partition columns
- repeated subqueries
- unnecessary cross joins
- many-to-many joins without control
- unbounded window functions
- scanning raw tables for dashboards

### Strong answer

```text
I would optimize warehouse queries by filtering early, using partition predicates, selecting only required columns, joining at the correct grain, materializing repeated expensive logic, and checking the query plan or scanned data.
```

---

## 29. Warehouse Cost Control

Cloud warehouses can become expensive.

Cost drivers:

- scanned data
- compute runtime
- always-on clusters
- inefficient SQL
- repeated full refreshes
- unoptimized joins
- materialized view refreshes
- high concurrency
- no partitioning
- no lifecycle strategy
- duplicate data copies

### Cost-control strategies

1. Partition large tables.
2. Cluster/sort common filters.
3. Avoid SELECT *.
4. Use incremental loads.
5. Materialize only useful aggregates.
6. Monitor expensive queries.
7. Right-size compute.
8. Separate workloads if needed.
9. Use lifecycle/retention policies.
10. Avoid unnecessary streaming if batch works.

### Strong answer

```text
Cost control in a warehouse comes from reducing scanned data, using incremental processing, right-sizing compute, avoiding wasteful queries, and monitoring high-cost workloads.
```

---

## 30. Warehouse Data Quality

Warehouse quality protects business trust.

Common checks:

- primary key uniqueness
- not-null checks
- foreign key integrity
- row count comparisons
- accepted values
- duplicate checks
- freshness checks
- referential checks
- reconciliation against source
- metric sanity checks
- schema checks

### Strong answer

```text
Before publishing warehouse tables, I would validate row counts, uniqueness, required fields, referential integrity, and freshness. A successful pipeline that produces wrong numbers is still a failed pipeline.
```

---

## 31. Warehouse Monitoring

Monitor both pipeline and warehouse output.

### Pipeline monitoring

- job success/failure
- runtime
- retries
- dependency failures
- load duration

### Data monitoring

- freshness
- row counts
- duplicate counts
- null rates
- metric anomalies
- schema changes
- consumer-facing SLA

### Cost monitoring

- expensive queries
- compute usage
- storage growth
- repeated full refreshes
- dashboard query cost

### Strong answer

```text
I would monitor warehouse freshness, quality, job failures, and cost. BI users care less that a job succeeded and more that the dashboard is accurate and fresh by SLA.
```

---

## 32. Warehouse Security

Security topics:

- least privilege
- role-based access
- service accounts
- row-level security
- column-level security
- masking policies
- PII classification
- encryption
- audit logs
- environment separation
- secrets management

### Strong answer

```text
Warehouse access should follow least privilege. Sensitive columns like email or phone should be masked or restricted, service accounts should be separated by pipeline, and access should be auditable.
```

### Weak answer

```text
Only admins can access it.
```

Too vague.

---

## 33. Warehouse Governance

Governance ensures data is trusted and manageable.

Includes:

- data ownership
- data catalog
- lineage
- metric definitions
- access policies
- quality rules
- retention policies
- documentation
- change management
- certification of trusted tables

### Strong answer

```text
For governed warehouse tables, I would define owners, table purpose, grain, refresh SLA, quality checks, metric definitions, and lineage. This helps users trust and correctly use the data.
```

---

## 34. Warehouse Documentation

Every important warehouse table should document:

```text
Table purpose:
Owner:
Grain:
Primary key:
Source systems:
Refresh frequency:
SLA:
Partitioning:
Key columns:
Metric definitions:
Quality checks:
Known limitations:
Example queries:
```

### Interview answer

```text
A warehouse table without documented grain and owner is risky because analysts may misuse it or create inconsistent metrics.
```

---

## 35. Warehouse SLAs

SLAs define expectations.

Examples:

- sales dashboard refreshed by 8 AM
- hourly events table available within 15 minutes
- daily finance mart loaded by 6 AM
- failed loads alerted within 10 minutes

### Strong answer

```text
Warehouse SLAs should be tied to business consumption. If executives use a dashboard at 9 AM, the data mart must be fresh before then, and monitoring should alert on freshness failures.
```

---

## 36. Backfills in Warehouse

Backfills rebuild historical data.

Reasons:

- transformation bug
- metric definition change
- late data
- source correction
- model migration
- missing partition
- schema correction

### Warehouse-safe backfill strategy

1. Identify affected tables and partitions.
2. Stop or mark downstream consumption if needed.
3. Reprocess from raw/staging data.
4. Use idempotent writes.
5. Validate output.
6. Refresh downstream marts.
7. Communicate impact.
8. Track lineage/audit.

### Strong answer

```text
For warehouse backfills, I would rebuild affected partitions from raw or staging data, validate row counts and metrics, refresh dependent marts, and communicate affected dashboards.
```

---

## 37. Late-Arriving Data in Warehouse

Late data arrives after expected processing window.

Examples:

- delayed orders
- late files
- delayed API response
- mobile events synced later
- CDC lag

### Handling strategies

- process by event date
- update affected partitions
- maintain lookback window
- late-arrival monitoring
- backfill affected aggregates
- use event_time and ingestion_time

### Strong answer

```text
I would distinguish event time from ingestion time. Late records should update the correct event-date partition, not simply be counted as today's business activity unless that is the requirement.
```

---

## 38. Warehouse Environments

Common environments:

- development
- test
- staging
- production

### Good practice

- separate datasets/schemas
- separate credentials
- controlled deployment
- test with sample data
- avoid production data exposure
- use CI/CD where possible

### Strong answer

```text
I would separate dev, test, and production warehouse environments so pipeline changes can be validated before affecting business dashboards.
```

---

## 39. Warehouse CI/CD

Data warehouse CI/CD may include:

- SQL version control
- model tests
- schema checks
- unit tests for transformations
- sample data validation
- deployment approvals
- rollback plan
- documentation update
- environment promotion

### Strong answer

```text
Warehouse changes should be version-controlled and tested. Before deploying a transformation change, I would run tests for schema, uniqueness, nulls, and key business metrics.
```

---

## 40. Warehouse Migration

Warehouse migration questions may involve moving from:

- on-prem database to cloud warehouse
- one warehouse to another
- raw tables to dimensional model
- legacy ETL to ELT
- batch-only to hybrid batch/streaming

### Migration plan

1. Assess current sources and consumers.
2. Inventory tables and dependencies.
3. Identify critical dashboards.
4. Design target model.
5. Build ingestion and transformation.
6. Validate row counts and metrics.
7. Run parallel comparison.
8. Migrate consumers.
9. Monitor.
10. Decommission old system gradually.

### Strong answer

```text
I would not migrate blindly table by table. I would first identify business-critical datasets, dependencies, data quality issues, and consumer requirements, then migrate in phases with validation and parallel runs.
```

---

## 41. Warehouse Tool-Agnostic Concepts

This guide is vendor-neutral.

Examples of warehouse platforms:

- BigQuery
- Snowflake
- Redshift
- Synapse
- Databricks SQL / lakehouse SQL
- other analytical SQL engines

The candidate should learn concepts first:

- columnar storage
- partitioning
- clustering/sorting
- compute scaling
- materialization
- cost
- governance
- access control
- query optimization
- incremental loads

Then map to vendor-specific features if needed.

---

## 42. BigQuery-Style Concepts

Do not over-focus on tool trivia, but know common BigQuery-style ideas:

- serverless warehouse model
- columnar analytics
- partitioned tables
- clustered tables
- slots/compute concepts
- bytes scanned and cost awareness
- nested/repeated fields
- external tables
- materialized views
- scheduled queries
- access control

### Interview-safe answer

```text
In a BigQuery-style platform, cost and performance are strongly related to data scanned. Partitioning, clustering, avoiding SELECT *, and filtering early are important.
```

---

## 43. Snowflake-Style Concepts

Common Snowflake-style ideas:

- separation of storage and compute
- virtual warehouses
- micro-partition concepts
- clustering
- time travel
- zero-copy clone concepts
- stages
- streams/tasks concepts
- role-based access
- semi-structured data support

### Interview-safe answer

```text
In a Snowflake-style platform, compute can be scaled separately from storage. This helps isolate workloads, but cost control requires warehouse sizing, auto-suspend, and query monitoring.
```

---

## 44. Redshift-Style Concepts

Common Redshift-style ideas:

- columnar warehouse
- distribution style/key concepts
- sort keys
- workload management
- Spectrum/external querying concepts
- cluster/serverless options depending on setup
- vacuum/analyze concepts in some contexts

### Interview-safe answer

```text
In a Redshift-style platform, data distribution and sort choices can affect join and query performance. The core interview idea is to align physical design with query patterns and data volume.
```

---

## 45. Synapse / Fabric-Style Concepts

Common Azure-style ideas:

- warehouse/lake integration
- dedicated vs serverless SQL concepts
- data lake storage integration
- pipelines/orchestration
- Spark and SQL workloads
- access control
- workspace governance

### Interview-safe answer

```text
In Azure-style data platforms, warehouse, lake, Spark, and orchestration services may be integrated. The interview focus should still be architecture, data quality, security, and cost, not only service names.
```

---

## 46. Common Warehouse Interview Questions

### Basic

1. What is a data warehouse?
2. How is a warehouse different from a database?
3. How is a warehouse different from a data lake?
4. What is a fact table?
5. What is a dimension table?
6. What is grain?
7. What is a data mart?
8. What is a staging table?
9. What is SCD Type 2?
10. What is partitioning?

### Medium

1. How do you design a sales warehouse?
2. How do you load data incrementally into a warehouse?
3. How do you handle duplicates in warehouse tables?
4. How do you optimize warehouse query performance?
5. How do you control warehouse cost?
6. How do you handle late-arriving data?
7. How do you design a data mart?
8. How do you handle changing dimensions?
9. How do you validate warehouse data?
10. How do you support backfills?

### Advanced

1. Design a warehouse for multi-source customer analytics.
2. Design a warehouse migration from on-prem to cloud.
3. Design an incremental CDC-based warehouse load.
4. Design a warehouse model for subscriptions and churn.
5. Design data quality and governance for a warehouse.
6. How would you support both current and historical reporting?
7. How would you design warehouse SLAs and monitoring?
8. How would you prevent metric inconsistency across teams?
9. How would you optimize cost for a large warehouse?
10. How would you recover from corrupted warehouse tables?

---

## 47. Scenario: Sales Data Warehouse

### Prompt

```text
Design a data warehouse for sales analytics.
```

### Strong answer outline

1. Clarify business questions:
   - revenue by product
   - revenue by region
   - revenue by customer segment
   - returns
   - discounts
2. Define sources:
   - orders
   - order_items
   - customers
   - products
   - payments
3. Define grain:
   - one row per order line item
4. Fact:
   - fact_order_line
5. Dimensions:
   - dim_customer
   - dim_product
   - dim_date
   - dim_channel
   - dim_region
6. SCD:
   - customer segment and product category may need history
7. Loading:
   - incremental load by updated_at or CDC
8. Quality:
   - uniqueness, row counts, revenue reconciliation
9. Performance:
   - partition by order_date
10. Serving:
   - sales mart and dashboard aggregates

### Weak answer

```text
Create orders, customer, product tables and connect to dashboard.
```

This misses grain, measures, history, quality, and load strategy.

---

## 48. Scenario: Subscription Warehouse

### Prompt

```text
Design a warehouse for subscription analytics.
```

### Metrics

- MRR
- churn
- active subscribers
- new subscriptions
- renewals
- upgrades
- downgrades
- retention

### Strong model

- fact_subscription_event
- fact_subscription_snapshot_monthly
- fact_invoice_line
- dim_customer
- dim_plan
- dim_date
- dim_region

### Strong answer

```text
Subscription analytics often needs both event facts and periodic snapshots. Events capture changes like start, cancel, upgrade, and renew. Snapshots make active subscriber and MRR reporting easier.
```

---

## 49. Scenario: Customer 360 Warehouse

### Prompt

```text
Design a customer 360 warehouse.
```

### Sources

- orders
- support tickets
- marketing campaigns
- product usage
- billing
- profile data

### Strong design

- conformed dim_customer
- domain facts
- customer summary mart
- SCD for customer attributes
- quality checks across sources
- identity resolution strategy
- access control for PII

### Strong answer

```text
I would not force everything into one giant table. I would create a conformed customer dimension and connect domain-specific facts, then build a customer summary mart for common use cases.
```

---

## 50. Scenario: Warehouse Backfill After Bug

### Prompt

```text
A transformation bug caused incorrect revenue for the last 3 months. How do you fix it?
```

### Strong answer

1. Stop or flag affected dashboards.
2. Identify affected tables and partitions.
3. Fix transformation logic.
4. Reprocess from raw/staging data.
5. Overwrite affected partitions or merge safely.
6. Validate revenue against source/control totals.
7. Refresh downstream marts.
8. Communicate impact.
9. Add test to prevent recurrence.

### Weak answer

```text
Rerun the job.
```

Too shallow.

---

## 51. Weak vs Strong Answers

### Question: What is a warehouse?

Weak:

```text
It is a database for data.
```

Strong:

```text
A warehouse is an analytics-optimized store for cleaned and modeled data from multiple sources. It supports reporting, dashboards, historical analysis, and business metrics. It differs from OLTP databases because it is optimized for scans and aggregations, not transaction processing.
```

---

### Question: How do you optimize a warehouse query?

Weak:

```text
Add index.
```

Strong:

```text
First I would check whether the query scans unnecessary data. I would filter by partition columns, avoid SELECT *, join at the correct grain, materialize repeated expensive logic, and use clustering/sorting or warehouse-specific optimization features based on the platform.
```

---

### Question: How do you handle late-arriving data?

Weak:

```text
Load it when it comes.
```

Strong:

```text
I would process late-arriving records according to event date, update affected partitions or aggregates, and ensure reruns are idempotent. I would also monitor late-arrival rates and define a lookback window if needed.
```

---

### Question: How do you make warehouse loads idempotent?

Weak:

```text
Avoid duplicates.
```

Strong:

```text
An idempotent warehouse load can be rerun without changing the final result incorrectly. I can achieve this by overwriting deterministic partitions, using merge/upsert keys, staging before publishing, or deduplicating by stable business keys.
```

---

## 52. Common Interview Red Flags

Flag these strongly:

1. Cannot define warehouse vs database.
2. Cannot explain warehouse vs lake.
3. Does not define grain.
4. Uses one giant table without justification.
5. Ignores incremental load.
6. Ignores data quality.
7. Ignores duplicate handling.
8. Ignores backfills.
9. Ignores late-arriving data.
10. Ignores cost.
11. Ignores query performance.
12. Ignores security.
13. Cannot explain SCD Type 2.
14. Cannot explain facts and dimensions.
15. Uses DISTINCT to hide problems.
16. Cannot explain how data reaches the warehouse.
17. Cannot explain refresh frequency or SLA.
18. Cannot explain project warehouse tables.
19. Gives only tool names.
20. Claims indexes solve every warehouse performance problem.

---

## 53. Data Warehouse Review Checklist

When reviewing a candidate answer, check:

```text
Business goal clarified:
Sources identified:
Warehouse purpose explained:
Raw/staging/curated layers explained:
Grain defined:
Facts identified:
Dimensions identified:
SCD/history explained:
Load pattern explained:
Incremental strategy explained:
Deduplication explained:
Data quality included:
Performance included:
Cost included:
Security included:
Monitoring/SLA included:
Backfill strategy included:
Trade-offs explained:
Answer structured clearly:
```

If grain, load strategy, quality, and backfill are missing, the answer is not interview-ready.

---

## 54. Scoring Rubric

### Score 0

No useful warehouse understanding.

Cannot explain:

- warehouse purpose
- facts/dimensions
- warehouse vs database
- basic loading

### Score 1

Knows warehouse as a place to store data.

Weak in:

- modeling
- layers
- grain
- incremental load
- quality

### Score 2

Basic understanding.

Can explain:

- warehouse vs database
- basic facts/dimensions
- simple loading

Weak in:

- SCD
- performance
- cost
- backfills
- governance

### Score 3

Developing.

Can explain:

- staging
- facts/dimensions
- basic star schema
- incremental loads
- partitioning basics
- quality checks

Needs improvement:

- late data
- CDC
- cost control
- advanced modeling
- monitoring

### Score 4

Interview-ready.

Can design:

- warehouse layers
- dimensional model
- incremental loading
- SCD Type 2
- quality checks
- partitioning
- backfills
- monitoring
- security

### Score 5

Strong.

Can handle:

- ambiguous business requirements
- warehouse migration
- multi-source models
- cost optimization
- governance
- lineage
- metric consistency
- recovery from bad data
- senior-level trade-offs

---

## 55. Minimum Passing Standard

Candidate must explain:

1. Warehouse vs database.
2. Warehouse vs data lake.
3. Raw/staging/core/mart layers.
4. Fact and dimension tables.
5. Grain.
6. Star schema.
7. SCD Type 1 and Type 2.
8. Full vs incremental load.
9. Deduplication.
10. Data quality checks.
11. Partitioning.
12. Query performance basics.
13. Cost basics.
14. Backfills.
15. Monitoring/freshness.

---

## 56. Strong Candidate Standard

A strong candidate can additionally explain:

1. CDC into warehouse.
2. Late-arriving facts and dimensions.
3. Materialized views and aggregate marts.
4. Query optimization trade-offs.
5. Warehouse migration strategy.
6. Governance and lineage.
7. Metric layer consistency.
8. Warehouse SLAs.
9. Security and PII controls.
10. Recovery from corrupted warehouse data.
11. Multi-source conformed dimensions.
12. Cost optimization at workload level.

---

## 57. 7-Day Warehouse Repair Plan

### Day 1: Warehouse basics

Topics:

- warehouse vs database
- warehouse vs lake
- warehouse layers

Drill:

```text
Explain why a company needs a warehouse when it already has production databases.
```

### Day 2: Dimensional modeling

Topics:

- facts
- dimensions
- grain
- star schema

Drill:

```text
Design sales fact and dimensions.
```

### Day 3: Loading patterns

Topics:

- full refresh
- append
- merge
- partition overwrite
- incremental load

Drill:

```text
Explain how to load daily orders into a warehouse.
```

### Day 4: History and changes

Topics:

- SCD Type 1
- SCD Type 2
- CDC
- late data

Drill:

```text
Explain how customer address changes should be handled.
```

### Day 5: Quality and monitoring

Topics:

- uniqueness
- nulls
- row counts
- freshness
- SLA
- reconciliation

Drill:

```text
Design quality checks for fact_sales.
```

### Day 6: Performance and cost

Topics:

- partitioning
- clustering
- materialization
- SELECT *
- query cost

Drill:

```text
Optimize a slow revenue dashboard query.
```

### Day 7: Mock warehouse design

Prompt:

```text
Design a warehouse for e-commerce sales, returns, customers, products, and executive dashboards.
```

---

## 58. 10-Minute Mock Interview

### Prompt

```text
Design a cloud data warehouse for an e-commerce company. Data comes from orders, order_items, customers, products, payments, returns, and marketing campaigns. Business users need daily dashboards for revenue, product performance, customer segments, and campaign effectiveness.
```

### Candidate should clarify

1. What are the main business metrics?
2. What is the expected freshness?
3. What is the data volume?
4. Do dimensions change over time?
5. How are returns handled?
6. Are multiple currencies involved?
7. Who are the consumers?
8. Are there PII fields?

### Expected answer

Should include:

- raw/staging/core/mart layers
- fact_order_line
- fact_payment
- fact_return or return handling
- dim_customer
- dim_product
- dim_date
- dim_campaign
- SCD Type 2 for changing attributes if needed
- incremental loading
- partitioning by order_date
- quality checks
- monitoring and SLA
- backfill strategy
- security for PII
- aggregate marts for dashboards
- cost/performance trade-offs

### Scoring

| Area | Score |
|---|---:|
| Requirements | /5 |
| Warehouse layers | /5 |
| Grain | /5 |
| Facts/dimensions | /5 |
| Loading strategy | /5 |
| History/SCD | /5 |
| Quality | /5 |
| Performance/cost | /5 |
| Backfills/failure | /5 |
| Communication | /5 |

---

## 59. Answer Template

Use this for warehouse interview answers.

```text
I will start by clarifying the warehouse use case.

Business goal:
[reporting/analytics need]

Sources:
[list source systems]

Consumers:
[BI, analysts, executives, ML, apps]

Freshness/SLA:
[daily/hourly/near-real-time]

Architecture layers:
Raw:
Staging:
Core warehouse:
Data marts:

Model:
Facts:
Dimensions:
Grain:
Keys:
History/SCD:

Load strategy:
[full/incremental/CDC/merge/partition overwrite]

Data quality:
[checks]

Performance:
[partitioning, clustering, aggregates]

Monitoring:
[freshness, failures, row counts, cost]

Backfill/recovery:
[how to rebuild]

Security/governance:
[access, PII, ownership, documentation]

Trade-offs:
[why this design]

Summary:
[final design]
```

---

## 60. Mentor Behavior Rules

When using this guide, the mentor should:

1. Stop candidates who say “warehouse is a database.”
2. Force them to explain warehouse purpose.
3. Force grain definition.
4. Ask how data gets loaded.
5. Ask whether the load is full or incremental.
6. Ask how duplicates are handled.
7. Ask how SCD/history is handled.
8. Ask how quality is validated.
9. Ask how freshness is monitored.
10. Ask how backfills work.
11. Ask how query cost is controlled.
12. Ask how PII/security is handled.
13. Ask them to connect warehouse design to business questions.
14. Score strictly.
15. Give repair tasks for missing areas.

Strict correction:

```text
This warehouse answer is not interview-ready. You named tables, but you did not define grain, loading strategy, data quality, freshness, or backfill handling.
```

---

## 61. Exit Test

Candidate must answer:

```text
Design a data warehouse for a marketplace platform with orders, sellers, buyers, products, payments, returns, and campaign data. The warehouse must support daily revenue dashboards, seller analytics, customer segmentation, product performance, historical reporting, and backfills.
```

Passing answer must include:

- business questions
- sources
- warehouse layers
- facts and dimensions
- grain
- SCD/history
- incremental load
- deduplication
- data quality
- partitioning/performance
- cost awareness
- monitoring/SLA
- security
- backfill/recovery
- trade-offs

If the candidate cannot define grain or loading strategy, they fail.

---

## 62. Final Summary

A data warehouse is not just storage.

It is the trusted analytical layer where business meaning, history, metrics, and quality come together.

The strongest candidates explain:

- why the warehouse exists
- how it differs from operational databases and lakes
- how data flows through layers
- how facts and dimensions are modeled
- how incremental loads and history work
- how quality, freshness, cost, security, and backfills are handled

The weakest candidates list tables or tools without explaining design.

In interviews, warehouse answers must connect **business questions, model grain, load strategy, quality, performance, and operations**.
