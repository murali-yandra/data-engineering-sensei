# SQL Drills Index

This is the canonical SQL practice index for Data Engineering Sensei.

Use it to route candidates to realistic SQL interview drills.

## Drill Files

| File | Focus |
|---|---|
| `practice/sql/joins.md` | joins, grain, duplicate risk |
| `practice/sql/ctes-subqueries.md` | CTEs, subqueries, decomposition |
| `practice/sql/window-functions.md` | ROW_NUMBER, RANK, LAG/LEAD, running totals |
| `practice/sql/deduplication.md` | latest record, duplicate removal |
| `practice/sql/gaps-and-islands.md` | consecutive periods and session logic |
| `practice/sql/query-optimization.md` | indexes, execution plans, query shape |
| `practice/sql/business-sql-cases.md` | product/business analytics cases |

## Default Drill Flow

Every SQL drill should include:

```text
Schema:
Table grain:
Business question:
Expected output grain:
Candidate approach:
Candidate query:
Review:
Corrected query:
Follow-up variation:
```

## Minimum SQL Topics

The candidate must practice:

- joins
- GROUP BY and HAVING
- CTEs
- subqueries
- window functions
- deduplication
- latest record per group
- top N per group
- date boundaries
- NULL behavior
- reconciliation
- query optimization basics

## Strict Review Checklist

When reviewing SQL, check:

1. Did the candidate state output grain?
2. Did they choose the right base table?
3. Can joins create duplicate rows?
4. Is the join type correct?
5. Is aggregation at the right level?
6. Are window partitions and orderings correct?
7. Are NULLs handled?
8. Are date boundaries clear?
9. Is the query readable?
10. Can the candidate explain it under pressure?

Do not accept a query as interview-ready if the candidate cannot explain it.
