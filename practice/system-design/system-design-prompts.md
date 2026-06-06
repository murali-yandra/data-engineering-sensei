# System Design Prompts Index

This is the canonical Data Engineering system design prompt index.

Use these prompts for mock interviews, roadmap checkpoints, and weakness repair.

## Prompt Files

| File | Scenario |
|---|---|
| `practice/system-design/batch-pipeline.md` | batch ingestion and processing |
| `practice/system-design/cdc-pipeline.md` | change data capture |
| `practice/system-design/realtime-pipeline.md` | near-real-time analytics |
| `practice/system-design/event-ingestion.md` | event collection and processing |
| `practice/system-design/data-warehouse.md` | analytical warehouse |
| `practice/system-design/data-lake.md` | lake or lakehouse storage |
| `practice/system-design/data-quality-framework.md` | quality checks and monitoring |
| `practice/system-design/reporting-pipeline.md` | dashboard/reporting pipeline |

## Required Design Structure

Every system design answer should cover:

```text
1. Requirements
2. Data sources
3. Consumers
4. Data volume
5. Latency and SLA
6. High-level architecture
7. Ingestion
8. Storage
9. Processing
10. Data model
11. Orchestration
12. Data quality
13. Monitoring
14. Failure handling
15. Backfill and reprocessing
16. Security and governance
17. Cost trade-offs
18. Final summary
```

## Default Prompts

1. Design a daily sales analytics pipeline.
2. Design a CDC pipeline from an OLTP database to a warehouse.
3. Design clickstream event ingestion for product analytics.
4. Design a data quality framework for critical dashboards.
5. Design a reporting pipeline for executives.
6. Design a data lake for raw and curated data.
7. Design a near-real-time metrics pipeline.
8. Design a warehouse model for orders, customers, and payments.

## Review Standard

Do not accept tool-only answers.

Flag:

- no requirements
- no data volume
- no latency discussion
- no data quality
- no failure handling
- no backfill strategy
- no monitoring
- no cost trade-off
- no security/governance
