# Warehouse and Cloud Guide

This canonical guide connects two closely related Data Engineering interview areas:

```text
data warehouses
cloud data platforms
data lakes and lakehouse concepts
storage and compute trade-offs
security, governance, and cost
```

Detailed companion files:

```text
docs/data-warehouse-guide.md
docs/cloud-data-platforms-guide.md
docs/data-modeling-guide.md
docs/system-design-guide.md
practice/system-design/data-warehouse.md
practice/system-design/data-lake.md
```

## Interview Goal

The candidate must be able to explain how analytical data is stored, modeled, governed, and served in modern cloud environments.

A strong answer does not list tools first. It explains:

1. Business requirement.
2. Data sources.
3. Storage layer.
4. Processing layer.
5. Warehouse or lakehouse model.
6. Access pattern.
7. Data quality.
8. Security.
9. Monitoring.
10. Cost trade-offs.

## Warehouse Core Concepts

Required topics:

- OLTP vs OLAP
- data warehouse purpose
- columnar storage
- facts and dimensions
- star schema
- data marts
- grain
- partitioning
- clustering
- materialized views
- query cost
- semantic or metrics layer
- access control
- retention
- auditability

Weak answer:

```text
A warehouse stores data for reporting.
```

Strong answer:

```text
A data warehouse is optimized for analytical queries across historical, cleaned, modeled data. It usually stores curated facts and dimensions at defined grains so analysts, dashboards, and data science users can query trusted metrics efficiently. The design must consider partitioning, cost, freshness, access control, data quality, and metric consistency.
```

## Cloud Platform Core Concepts

Required topics:

- object storage
- managed warehouses
- compute separation
- serverless vs cluster-based processing
- batch ingestion
- streaming ingestion
- IAM and least privilege
- encryption
- networking basics
- monitoring and logging
- cost controls
- retention and lifecycle policies
- governance and lineage

Use cloud examples only after explaining the concept:

| Concept | AWS example | GCP example | Azure example |
|---|---|---|---|
| Object storage | S3 | Cloud Storage | ADLS |
| Warehouse | Redshift | BigQuery | Synapse |
| Batch processing | Glue/EMR | Dataflow/Dataproc | Data Factory/Synapse |
| Orchestration | MWAA | Cloud Composer | Data Factory |
| Streaming | Kinesis/MSK | Pub/Sub | Event Hubs |

Do not train vendor trivia before the candidate understands the design reason.

## Warehouse vs Lake vs Lakehouse

| System | Best for | Interview explanation |
|---|---|---|
| Data warehouse | Curated analytics and BI | Structured, governed, query-optimized |
| Data lake | Raw/semi-structured storage | Flexible, cheap, scalable, needs governance |
| Lakehouse | Lake storage with warehouse-like controls | Combines flexible storage with table formats and ACID-style management |

## Common Interview Prompts

Use these prompts for drills:

1. Design a sales analytics warehouse.
2. Explain warehouse vs lake vs lakehouse.
3. Explain partitioning and clustering.
4. How would you reduce BigQuery/Snowflake/Redshift cost?
5. How would you secure sensitive data in a warehouse?
6. How would you design raw, staging, and curated layers?
7. How would you support both dashboards and ML consumers?
8. How would you handle late-arriving data?
9. How would you validate source-to-warehouse reconciliation?
10. How would you manage retention and deletion requirements?

## Review Checklist

When reviewing an answer, check:

- Did the candidate define consumers and query patterns?
- Did they define table grain?
- Did they separate raw, staging, and curated data?
- Did they explain data quality and reconciliation?
- Did they mention access control and sensitive data?
- Did they discuss partitioning or clustering only where useful?
- Did they discuss cost without guessing fake numbers?
- Did they explain freshness and SLA?
- Did they avoid tool-name dumping?

## Minimum Passing Standard

The candidate is ready when they can:

1. Explain warehouse, lake, and lakehouse clearly.
2. Design a basic analytical warehouse with facts, dimensions, and marts.
3. Explain partitioning, clustering, and columnar storage at a conceptual level.
4. Discuss cloud storage, compute, IAM, encryption, monitoring, and cost.
5. Connect the design to interview requirements instead of listing products.
