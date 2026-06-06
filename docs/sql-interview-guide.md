# SQL Interview Guide for Data Engineering Interviews

Generated: 2026-06-06

This guide teaches **SQL for Data Engineering interviews**.

It is written for **Data Engineering Sensei**, a strict, no-sugarcoating Data Engineering interview mentor. The goal is not to memorize SQL syntax. The goal is to make the candidate capable of solving real interview SQL questions, explaining query logic, avoiding grain mistakes, handling nulls and dates, using window functions correctly, writing reliable ETL/ELT-style SQL, and defending performance choices.

Use this guide for:

- SQL coding interviews
- Data Engineering technical screens
- warehouse transformation interviews
- ETL/ELT SQL discussions
- data modeling query drills
- analytics SQL rounds
- mock interview scoring
- weakness repair
- roadmap generation

Default style:

```text
ANSI SQL first.
Mention dialect differences when relevant.
Use SQL Server / PostgreSQL / BigQuery / Snowflake examples only when needed.
```


## 1. Purpose

SQL is one of the highest-signal skills in Data Engineering interviews.

A Data Engineer must use SQL to:

1. Extract data.
2. Transform data.
3. Validate data.
4. Build warehouse tables.
5. Deduplicate records.
6. Join facts and dimensions.
7. Aggregate metrics.
8. Build data quality checks.
9. Investigate production issues.
10. Reconcile source and target.
11. Write incremental load logic.
12. Explain performance trade-offs.

A weak candidate says:

```text
I know SELECT, JOIN, GROUP BY.
```

A strong candidate says:

```text
I can define output grain, choose the base table, join safely, aggregate at the correct level, use window functions for deduplication/ranking, handle nulls and dates, validate results, and explain performance implications.
```


## 2. Interview Standard

A SQL answer is interview-ready only when the candidate can explain:

```text
Business question:
Expected output grain:
Base table:
Required joins:
Join type:
Join keys:
Duplicate risk:
Filters:
Aggregation level:
Window logic:
Date boundaries:
NULL handling:
Tie-breakers:
Performance considerations:
Final query:
Validation checks:
```

If the candidate writes SQL without defining grain, the answer is not strong.

Strict mentor correction:

```text
You wrote a query before defining output grain. That is dangerous. In Data Engineering interviews, grain comes before joins and aggregation.
```


## 3. SQL Readiness Levels

### Score 0

Cannot write basic SELECT queries.

### Score 1

Can write simple SELECT/WHERE but weak joins and aggregation.

### Score 2

Can solve basic business questions but makes grain, join, and null mistakes.

### Score 3

Can solve many medium questions with some hints. Needs better windows, date logic, and performance reasoning.

### Score 4

Interview-ready for standard Data Engineering SQL rounds. Handles joins, windows, aggregation, dedupe, dates, nulls, and explanation.

### Score 5

Strong / FAANG-level. Handles ambiguous business questions, complex windows, retention/cohort/funnel queries, incremental SQL, data quality, performance, and follow-ups under pressure.

Do not give 4+ if the candidate cannot explain output grain.


## 4. Core Rule: Define Grain First

Grain means:

```text
What does one output row represent?
```

Examples:

| Question | Output Grain |
|---|---|
| Total revenue per customer | one row per customer |
| Latest order per customer | one row per customer |
| Daily revenue by product | one row per product per day |
| Top 3 products per category | one row per product per category rank |
| Week 1 retention by signup week | one row per signup week |

Strong answer:

```text
The output grain is one row per customer. I will start from customers if I need all customers, or orders if I only need customers with orders.
```

Weak answer:

```text
I will join customers and orders.
```

That is not enough.


## 5. SQL Answer Template

Use this template before writing SQL.

```text
## Clarification

Business question:
Output grain:
Date range:
Metric definition:
Inclusion/exclusion rules:
Tie-breaker:

## Table Understanding

Base table:
Join tables:
Join keys:
Potential duplicate risk:

## Approach

Filters:
Aggregations:
Window functions:
CTEs:

## Query

[SQL]

## Validation

Expected row count:
Duplicate check:
Null check:
Metric reconciliation:
Edge cases:

## Complexity / Performance

Large tables:
Indexes/partitions:
Filter pushdown:
Pre-aggregation:
```


## 6. SQL Dialect Notes

Interview SQL varies by platform.

Common differences:

| Concept | SQL Server | PostgreSQL | BigQuery/Snowflake-like |
|---|---|---|---|
| Limit rows | TOP | LIMIT | LIMIT |
| Current date | GETDATE() / SYSDATETIME() | CURRENT_DATE / NOW() | CURRENT_DATE |
| Date add | DATEADD | + INTERVAL | DATE_ADD / DATEADD |
| String concat | + or CONCAT | || or CONCAT | CONCAT |
| Null replacement | ISNULL / COALESCE | COALESCE | COALESCE |
| Temporary table | #temp | temp table | temp table / CTE |
| Boolean | BIT/no true boolean in old patterns | boolean | boolean |

Mentor rule:

```text
Do not penalize dialect syntax if the logic is correct, unless the interview explicitly tests that dialect.
```

But do penalize logic mistakes:

- wrong grain
- wrong join
- wrong aggregation
- wrong window partition
- wrong date boundary
- wrong null handling


## 7. SELECT Basics

Basic query:

```sql
SELECT
    customer_id,
    order_date,
    amount
FROM orders;
```

Interview expectation:

The candidate should not just know syntax. They should explain:

```text
Which columns are needed?
What table contains the base records?
Does this preserve row grain?
Are duplicate rows possible?
```

Common mistake:

```sql
SELECT *
FROM large_table;
```

In interviews, say:

```text
I will select only needed columns to reduce data movement and improve readability.
```


## 8. WHERE Filtering

`WHERE` filters rows before aggregation.

Example:

```sql
SELECT
    order_id,
    customer_id,
    amount
FROM orders
WHERE order_status = 'SUCCESS';
```

Strong explanation:

```text
I filter successful orders before aggregation because cancelled or failed orders should not count toward revenue.
```

Common mistakes:

- filtering after join when it changes outer join behavior
- wrong date boundary
- null comparison using `= NULL`
- filtering on derived aggregate in WHERE instead of HAVING


## 9. NULL Handling

NULL means unknown or missing.

Important rules:

```sql
column = NULL       -- wrong
column IS NULL      -- correct
column IS NOT NULL  -- correct
```

Aggregates:

- `COUNT(*)` counts rows.
- `COUNT(column)` counts non-null values.
- `SUM(column)` ignores null values.
- comparisons with NULL usually return unknown.

Examples:

```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT(email) AS rows_with_email
FROM customers;
```

Strong answer:

```text
I need to decide how nulls should be handled. For required keys, nulls may be invalid. For optional attributes, nulls may be allowed or filled as UNKNOWN.
```

Strict correction:

```text
You ignored NULL behavior. In SQL interviews, NULLs often break otherwise correct-looking queries.
```


## 10. COALESCE

`COALESCE` returns the first non-null value.

Example:

```sql
SELECT
    customer_id,
    COALESCE(country, 'UNKNOWN') AS country
FROM customers;
```

Use cases:

- default optional dimension values
- replacing null metrics with 0
- safe display values

Warning:

```text
Do not blindly COALESCE required fields. It can hide data quality problems.
```

Example:

```sql
SELECT
    order_id,
    COALESCE(discount_amount, 0) AS discount_amount
FROM orders;
```

This may be acceptable if missing discount means no discount.


## 11. CASE Expressions

`CASE` creates conditional logic.

Example:

```sql
SELECT
    order_id,
    amount,
    CASE
        WHEN amount >= 1000 THEN 'high'
        WHEN amount >= 100 THEN 'medium'
        ELSE 'low'
    END AS amount_bucket
FROM orders;
```

Use cases:

- bucketing
- conditional metrics
- flags
- business rules
- data quality labels

Common mistake:

```text
Overlapping conditions in wrong order.
```

Example:

```sql
CASE
    WHEN amount >= 100 THEN 'medium'
    WHEN amount >= 1000 THEN 'high'
END
```

The high condition never executes.


## 12. Aggregation Basics

Aggregation summarizes rows.

Example:

```sql
SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY customer_id;
```

Output grain:

```text
one row per customer_id
```

Strong explanation:

```text
The GROUP BY columns define the output grain. Here the grain is customer_id.
```

Common mistake:

Adding extra columns to GROUP BY and changing the grain.

Example:

```sql
GROUP BY customer_id, order_date
```

Now the output is per customer per date, not per customer.


## 13. COUNT Variants

Important count patterns:

```sql
COUNT(*)                  -- all rows
COUNT(column_name)         -- non-null values
COUNT(DISTINCT user_id)    -- unique users
```

Examples:

```sql
SELECT
    event_date,
    COUNT(*) AS event_count,
    COUNT(DISTINCT user_id) AS active_users
FROM events
GROUP BY event_date;
```

Interview warning:

`COUNT(DISTINCT)` can be expensive on large data. In system design/performance follow-ups, mention approximate distinct or pre-aggregations only if relevant.


## 14. Conditional Aggregation

Conditional aggregation is very important.

Example:

```sql
SELECT
    customer_id,
    SUM(CASE WHEN order_status = 'SUCCESS' THEN amount ELSE 0 END) AS successful_revenue,
    COUNT(CASE WHEN order_status = 'FAILED' THEN 1 END) AS failed_order_count
FROM orders
GROUP BY customer_id;
```

Alternative:

```sql
SUM(CASE WHEN condition THEN 1 ELSE 0 END)
```

Use cases:

- success/failure counts
- event type metrics
- payment status metrics
- conversion flags
- data quality counts

Strong answer:

```text
Conditional aggregation lets me calculate multiple metrics at the same grain in one grouped query.
```


## 15. HAVING

`HAVING` filters groups after aggregation.

Example:

```sql
SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;
```

Difference:

```text
WHERE filters rows before grouping.
HAVING filters groups after grouping.
```

Strict correction:

```text
You used WHERE for an aggregate condition. That is incorrect. Use HAVING after GROUP BY.
```


## 16. ORDER BY

`ORDER BY` sorts output.

Example:

```sql
SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY customer_id
ORDER BY total_revenue DESC;
```

Interview notes:

- specify descending/ascending
- define tie-breakers
- sorting can be expensive on large outputs
- ORDER BY inside CTE does not guarantee final output order unless used with ranking/limit in a dialect-specific way

Strong answer:

```text
If two customers have same revenue, I will tie-break by customer_id for deterministic output.
```


## 17. LIMIT / TOP

Different SQL dialects limit rows differently.

SQL Server:

```sql
SELECT TOP 10 *
FROM orders
ORDER BY order_date DESC;
```

PostgreSQL / BigQuery / Snowflake-like:

```sql
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 10;
```

Interview rule:

```text
If dialect is not specified, focus on logic. Mention that syntax may change by SQL engine.
```


## 18. Joins Overview

Joins combine rows from multiple tables.

Common join types:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- CROSS JOIN
- SEMI JOIN concept
- ANTI JOIN concept

Strong answer before any join:

```text
I will identify the base table, join key, relationship cardinality, and whether unmatched records should be kept.
```

Common red flags:

- joining before understanding grain
- using INNER JOIN and accidentally dropping records
- using LEFT JOIN but filtering right table in WHERE
- many-to-many join explosion
- hiding duplicate issue with DISTINCT


## 19. INNER JOIN

INNER JOIN keeps only matching rows.

Example:

```sql
SELECT
    o.order_id,
    o.customer_id,
    c.country
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id;
```

Use when:

```text
Only matched records should be included.
```

Risk:

```text
Unmatched orders are dropped.
```

Strong explanation:

```text
I would use INNER JOIN only if orders without a matching customer should be excluded. Otherwise, I would use LEFT JOIN.
```


## 20. LEFT JOIN

LEFT JOIN keeps all rows from the left/base table.

Example:

```sql
SELECT
    o.order_id,
    o.customer_id,
    c.country
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id;
```

Use when:

```text
All base records must be preserved.
```

Common Data Engineering use:

```text
Keep all fact records while enriching with dimension attributes.
```

Mistake:

```sql
SELECT ...
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.country = 'IN';
```

This can turn the LEFT JOIN into INNER JOIN behavior.

Safer if wanting all orders but only IN country attribute:

```sql
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
   AND c.country = 'IN'
```

Clarify business requirement first.


## 21. FULL OUTER JOIN

FULL OUTER JOIN keeps unmatched rows from both sides.

Use cases:

- reconciliation
- source vs target comparison
- finding missing records in either table

Example:

```sql
SELECT
    COALESCE(s.order_id, t.order_id) AS order_id,
    s.amount AS source_amount,
    t.amount AS target_amount
FROM source_orders s
FULL OUTER JOIN target_orders t
    ON s.order_id = t.order_id
WHERE s.order_id IS NULL
   OR t.order_id IS NULL
   OR s.amount <> t.amount;
```

Strong answer:

```text
FULL OUTER JOIN is useful for reconciliation because I can detect records missing from either side.
```


## 22. CROSS JOIN

CROSS JOIN creates all combinations.

Example:

```sql
SELECT
    d.calendar_date,
    p.product_id
FROM calendar d
CROSS JOIN products p;
```

Use cases:

- generating date-product grids
- building expected combinations
- filling missing metrics
- testing completeness

Warning:

```text
CROSS JOIN can explode row counts. Use only intentionally.
```

Strong answer:

```text
I would use CROSS JOIN only when I need every combination, and I would estimate row count before doing it.
```


## 23. Anti Join

Anti join finds records in one table that do not exist in another.

Common pattern:

```sql
SELECT
    s.*
FROM source_orders s
LEFT JOIN target_orders t
    ON s.order_id = t.order_id
WHERE t.order_id IS NULL;
```

Use cases:

- missing records
- incremental inserts
- reconciliation
- data quality checks

Alternative:

```sql
SELECT *
FROM source_orders s
WHERE NOT EXISTS (
    SELECT 1
    FROM target_orders t
    WHERE t.order_id = s.order_id
);
```

Strong answer:

```text
I use anti join when I need records from source that are not yet in target.
```


## 24. Semi Join

Semi join returns rows from one table where a match exists in another table, without bringing columns from the second table.

Pattern:

```sql
SELECT
    c.*
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

Use cases:

- customers with orders
- users who performed an event
- products that were sold
- existence checks

Strong answer:

```text
EXISTS is useful when I only need to check presence and do not need columns from the joined table.
```


## 25. Join Grain and Duplicate Explosion

Duplicate explosion happens when joins multiply rows unexpectedly.

Example:

```text
orders has one row per order.
order_items has multiple rows per order.
Joining orders to order_items changes grain to one row per order item.
```

If candidate then sums order amount, revenue may be duplicated.

Bad:

```sql
SELECT
    SUM(o.order_amount) AS revenue
FROM orders o
JOIN order_items i
    ON o.order_id = i.order_id;
```

If each order has multiple items, order_amount is repeated.

Correct approach depends on question.

If revenue is at order grain:

```sql
SELECT
    SUM(order_amount) AS revenue
FROM orders;
```

If revenue is item grain:

```sql
SELECT
    SUM(i.quantity * i.unit_price) AS revenue
FROM order_items i;
```

Strict correction:

```text
Your join changed the grain and duplicated revenue. Do not fix this with DISTINCT. Fix the grain.
```


## 26. DISTINCT

`DISTINCT` removes duplicate output rows.

Example:

```sql
SELECT DISTINCT customer_id
FROM orders;
```

Acceptable use:

```text
Question explicitly asks for unique customers.
```

Red flag use:

```text
Using DISTINCT to hide duplicate rows caused by wrong joins.
```

Strict correction:

```text
Using DISTINCT here is a red flag. Explain why duplicates appear first. If the join is wrong, DISTINCT hides the symptom but not the logic error.
```

Use DISTINCT carefully.


## 27. CTEs

CTE means Common Table Expression.

Example:

```sql
WITH successful_orders AS (
    SELECT
        order_id,
        customer_id,
        amount
    FROM orders
    WHERE order_status = 'SUCCESS'
)
SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM successful_orders
GROUP BY customer_id;
```

Use CTEs for:

- readability
- step-by-step logic
- pre-aggregation
- deduplication
- isolating transformations
- interview explanation

Strong answer:

```text
I will use CTEs to separate filtering, deduplication, aggregation, and ranking so the query is easier to review.
```


## 28. Subqueries

Subqueries can be used in SELECT, FROM, or WHERE.

Example with EXISTS:

```sql
SELECT
    c.customer_id
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

Example derived table:

```sql
SELECT
    customer_id,
    total_revenue
FROM (
    SELECT
        customer_id,
        SUM(amount) AS total_revenue
    FROM orders
    GROUP BY customer_id
) x
WHERE total_revenue > 1000;
```

Interview note:

CTEs are often easier to read than nested subqueries in interviews.


## 29. Set Operations

Set operations combine result sets.

### UNION

Removes duplicates.

```sql
SELECT customer_id FROM online_orders
UNION
SELECT customer_id FROM store_orders;
```

### UNION ALL

Keeps duplicates.

```sql
SELECT customer_id FROM online_orders
UNION ALL
SELECT customer_id FROM store_orders;
```

### INTERSECT

Rows present in both.

### EXCEPT / MINUS

Rows present in first but not second.

Strong answer:

```text
I use UNION ALL when duplicates are meaningful or when I know inputs do not overlap. UNION does extra deduplication work.
```


## 30. Window Functions Overview

Window functions calculate values across related rows while preserving row-level detail.

Basic syntax:

```sql
function() OVER (
    PARTITION BY ...
    ORDER BY ...
)
```

Common window functions:

- ROW_NUMBER
- RANK
- DENSE_RANK
- LAG
- LEAD
- SUM OVER
- COUNT OVER
- AVG OVER
- FIRST_VALUE
- LAST_VALUE

Strong answer:

```text
Unlike GROUP BY, window functions do not collapse rows. They add analytical values over a partition of rows.
```


## 31. ROW_NUMBER

`ROW_NUMBER` assigns a unique sequence number within a partition.

Latest order per customer:

```sql
WITH ranked_orders AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date DESC, order_id DESC
        ) AS rn
    FROM orders
)
SELECT
    order_id,
    customer_id,
    order_date,
    amount
FROM ranked_orders
WHERE rn = 1;
```

Strong explanation:

```text
I partition by customer because I need one latest order per customer. I order by order_date descending and use order_id as tie-breaker for deterministic output.
```

Common mistake:

```text
No tie-breaker.
```


## 32. RANK and DENSE_RANK

Use ranking functions for top N with ties.

Example:

```sql
SELECT
    product_id,
    category,
    revenue,
    RANK() OVER (
        PARTITION BY category
        ORDER BY revenue DESC
    ) AS revenue_rank
FROM product_revenue;
```

Difference:

| Function | Behavior |
|---|---|
| ROW_NUMBER | unique sequence; no ties |
| RANK | ties share rank, gaps appear |
| DENSE_RANK | ties share rank, no gaps |

Example revenue values:

```text
100, 100, 90
ROW_NUMBER: 1, 2, 3
RANK:      1, 1, 3
DENSE_RANK:1, 1, 2
```

Strong answer:

```text
If ties should all be included, I would use RANK or DENSE_RANK instead of ROW_NUMBER.
```


## 33. Top N Per Group

Prompt:

```text
Return top 3 products by revenue in each category.
```

Solution:

```sql
WITH product_revenue AS (
    SELECT
        p.category,
        oi.product_id,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM order_items oi
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY
        p.category,
        oi.product_id
),
ranked AS (
    SELECT
        category,
        product_id,
        revenue,
        ROW_NUMBER() OVER (
            PARTITION BY category
            ORDER BY revenue DESC, product_id
        ) AS rn
    FROM product_revenue
)
SELECT
    category,
    product_id,
    revenue
FROM ranked
WHERE rn <= 3;
```

Strong explanation:

```text
First I aggregate to product-category grain. Then I rank products within each category and keep top 3.
```


## 34. LAG and LEAD

`LAG` accesses previous row. `LEAD` accesses next row.

Example: compare current order amount to previous order for same customer.

```sql
SELECT
    customer_id,
    order_id,
    order_date,
    amount,
    LAG(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS previous_amount
FROM orders;
```

Use cases:

- previous status
- next event
- day-over-day change
- detecting changes
- sessionization
- SCD comparisons

Strong answer:

```text
LAG and LEAD are useful when comparing a row to previous or next events within the same entity.
```


## 35. Running Totals

Running total:

```sql
SELECT
    customer_id,
    order_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_revenue
FROM orders;
```

Strong explanation:

```text
The window frame defines which rows are included in each running total.
```

Interview note:

Some SQL engines have default window frames that can surprise candidates. For clarity, specify `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.


## 36. Moving Average

7-day moving average:

```sql
SELECT
    event_date,
    daily_revenue,
    AVG(daily_revenue) OVER (
        ORDER BY event_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS revenue_7_day_avg
FROM daily_revenue;
```

Strong answer:

```text
The frame includes the current row and previous 6 rows. If dates are missing, this is previous 6 rows, not necessarily previous 6 calendar days.
```

Follow-up:

```text
What if dates are missing?
```

Answer:

```text
Use a calendar table to create complete date series before applying moving window.
```


## 37. Deduplication with Window Functions

Latest record per business key:

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

Use cases:

- CDC latest state
- dedupe API records
- dedupe event records
- latest dimension record
- latest status per order

Strong answer:

```text
I use ROW_NUMBER for deterministic deduplication because I need to define exactly which duplicate wins.
```

Red flag:

```sql
SELECT DISTINCT *
FROM staging_table;
```

This does not solve latest-record logic.


## 38. Date Filtering

Date filters are common interview traps.

Bad ambiguous pattern:

```sql
WHERE order_date BETWEEN '2025-01-01' AND '2025-01-31'
```

If `order_date` is timestamp, this may exclude records after midnight on Jan 31 in some systems.

Safer timestamp pattern:

```sql
WHERE order_date >= '2025-01-01'
  AND order_date <  '2025-02-01'
```

Strong answer:

```text
I prefer inclusive start and exclusive end for timestamp ranges because it avoids end-of-day boundary bugs.
```


## 39. Event Time vs Ingestion Time

Data Engineering queries often need two times:

```text
event_time: when the business event happened
ingestion_time: when the pipeline received it
```

Example:

```sql
SELECT
    CAST(event_time AS DATE) AS event_date,
    COUNT(*) AS event_count
FROM events
GROUP BY CAST(event_time AS DATE);
```

Strong answer:

```text
Analytics usually groups by event_time, while ingestion_time is useful for pipeline monitoring, late arrival detection, and operational debugging.
```

Common mistake:

```text
Using ingestion date for business metrics when event date is required.
```


## 40. Timezone Awareness

Timezone can affect date logic.

Issues:

- UTC vs local business date
- daylight saving time
- source timestamps without timezone
- dashboard timezone
- late-night events crossing date boundary

Strong answer:

```text
I would clarify whether reporting date is based on UTC or business timezone. I would avoid silently casting timestamps to date without knowing timezone rules.
```

Interview note:

You do not need advanced timezone code unless asked, but you must mention the risk.


## 41. Data Quality SQL

SQL is often used for data quality checks.

Required field check:

```sql
SELECT
    COUNT(*) AS invalid_count
FROM orders
WHERE order_id IS NULL
   OR customer_id IS NULL
   OR order_date IS NULL;
```

Duplicate key check:

```sql
SELECT
    order_id,
    COUNT(*) AS record_count
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;
```

Accepted value check:

```sql
SELECT
    order_status,
    COUNT(*) AS record_count
FROM orders
GROUP BY order_status;
```

Freshness check:

```sql
SELECT
    MAX(ingestion_time) AS latest_ingestion_time
FROM events;
```

Strong answer:

```text
A successful pipeline run does not guarantee correct data. I would add SQL checks for nulls, duplicates, row counts, accepted values, freshness, and reconciliation.
```


## 42. Reconciliation SQL

Compare source and target counts by date.

```sql
WITH source_counts AS (
    SELECT
        order_date,
        COUNT(*) AS source_count,
        SUM(amount) AS source_revenue
    FROM source_orders
    GROUP BY order_date
),
target_counts AS (
    SELECT
        order_date,
        COUNT(*) AS target_count,
        SUM(amount) AS target_revenue
    FROM fact_orders
    GROUP BY order_date
)
SELECT
    COALESCE(s.order_date, t.order_date) AS order_date,
    s.source_count,
    t.target_count,
    s.source_revenue,
    t.target_revenue
FROM source_counts s
FULL OUTER JOIN target_counts t
    ON s.order_date = t.order_date
WHERE COALESCE(s.source_count, 0) <> COALESCE(t.target_count, 0)
   OR COALESCE(s.source_revenue, 0) <> COALESCE(t.target_revenue, 0);
```

Strong answer:

```text
I reconcile by partition/date so I can quickly identify where the pipeline output differs from source.
```


## 43. Incremental Load SQL

Incremental load processes only new or changed records.

Example using watermark:

```sql
SELECT
    *
FROM source_orders
WHERE updated_at > (
    SELECT last_successful_watermark
    FROM pipeline_watermarks
    WHERE pipeline_name = 'orders_load'
);
```

Important:

```text
Watermark should be advanced only after successful load and validation.
```

Strong answer:

```text
Incremental loading reduces work, but it requires reliable watermark logic, idempotent writes, and handling late-arriving updates.
```


## 44. MERGE / UPSERT Concept

MERGE updates existing rows and inserts new rows.

Generic concept:

```sql
MERGE INTO target_table AS t
USING staging_table AS s
ON t.business_key = s.business_key
WHEN MATCHED THEN
    UPDATE SET ...
WHEN NOT MATCHED THEN
    INSERT (...);
```

Use cases:

- CDC apply
- dimension updates
- incremental fact loads
- latest state table
- idempotent loading

Interview-safe answer:

```text
MERGE is useful for upserts when source records can update existing target records. The exact syntax differs by SQL engine.
```

Warning:

```text
MERGE requires stable keys and deduplicated staging data. If staging has multiple rows for the same key, results may be invalid or fail.
```


## 45. Delete and Reload Partition

For partitioned fact tables, an idempotent pattern is:

```text
Delete target partition.
Insert recomputed data for that partition.
```

Example:

```sql
DELETE FROM fact_orders
WHERE order_date >= '2025-01-01'
  AND order_date <  '2025-01-02';

INSERT INTO fact_orders (...)
SELECT ...
FROM staging_orders
WHERE order_date >= '2025-01-01'
  AND order_date <  '2025-01-02';
```

Strong answer:

```text
Partition delete-and-reload can be simple and idempotent for batch fact data, as long as the delete scope is correct and validation runs before publish.
```

Risk:

```text
Wrong date filter can delete too much data.
```


## 46. SCD Type 1 SQL

SCD Type 1 overwrites old values.

Use when history is not required.

Example concept:

```sql
MERGE INTO dim_customer t
USING staging_customer s
ON t.customer_id = s.customer_id
WHEN MATCHED THEN
    UPDATE SET
        customer_name = s.customer_name,
        country = s.country,
        updated_at = s.updated_at
WHEN NOT MATCHED THEN
    INSERT (customer_id, customer_name, country, updated_at)
    VALUES (s.customer_id, s.customer_name, s.country, s.updated_at);
```

Strong answer:

```text
SCD Type 1 keeps only current values. It is simpler but loses history.
```


## 47. SCD Type 2 SQL Concept

SCD Type 2 preserves history by creating new versions.

Typical columns:

```text
surrogate_key
business_key
attributes
effective_start_date
effective_end_date
is_current
```

Strong answer:

```text
For SCD Type 2, when tracked attributes change, I expire the current row and insert a new current row with a new effective date.
```

Interview logic:

1. Compare incoming record to current dimension record.
2. Identify changed tracked attributes.
3. Expire old current row.
4. Insert new current version.
5. Preserve unchanged rows.

Common mistake:

```text
Updating current row directly when history is required.
```


## 48. Fact and Dimension Query Awareness

Data Engineering SQL often uses warehouse models.

Fact table:

```text
Events or measurements.
Example: orders, payments, page views.
```

Dimension table:

```text
Descriptive context.
Example: customers, products, dates.
```

Strong answer:

```text
Before writing SQL, I identify fact grain and dimension keys. This prevents duplicate joins and incorrect metrics.
```

Example:

```sql
SELECT
    d.month,
    p.category,
    SUM(f.revenue) AS revenue
FROM fact_sales f
JOIN dim_date d
    ON f.date_key = d.date_key
JOIN dim_product p
    ON f.product_key = p.product_key
GROUP BY
    d.month,
    p.category;
```


## 49. Output Grain in Fact Queries

Prompt:

```text
Revenue by category and month.
```

Expected grain:

```text
one row per category per month
```

Query pattern:

```sql
SELECT
    d.month,
    p.category,
    SUM(f.revenue) AS revenue
FROM fact_sales f
JOIN dim_date d
    ON f.date_key = d.date_key
JOIN dim_product p
    ON f.product_key = p.product_key
GROUP BY
    d.month,
    p.category;
```

Strong answer:

```text
The GROUP BY defines the output grain. I must ensure joins to dimensions are one-to-one at the relevant keys, otherwise revenue can duplicate.
```


## 50. Latest Record Per Group

Prompt:

```text
For each customer, return the latest order.
```

Query:

```sql
WITH ranked AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date DESC, order_id DESC
        ) AS rn
    FROM orders
)
SELECT
    order_id,
    customer_id,
    order_date,
    amount
FROM ranked
WHERE rn = 1;
```

Follow-ups:

1. What if order_date ties?
2. What if customers with no orders should appear?
3. What if latest successful order only?
4. How would you optimize on large table?
5. What is the output grain?

Passing answer must include tie-breaker.


## 51. Top K Per Group

Prompt:

```text
Return top 2 products by revenue for each category.
```

Pattern:

```sql
WITH product_revenue AS (
    SELECT
        p.category,
        oi.product_id,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM order_items oi
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY
        p.category,
        oi.product_id
),
ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY category
            ORDER BY revenue DESC, product_id
        ) AS rn
    FROM product_revenue
)
SELECT
    category,
    product_id,
    revenue
FROM ranked
WHERE rn <= 2;
```

Strong explanation:

```text
First aggregate to product/category grain, then rank within category.
```


## 52. Retention Query

Prompt:

```text
Calculate week-1 retention by signup week.
A user is retained if they return between 7 and 13 days after signup.
```

Example:

```sql
WITH signups AS (
    SELECT
        user_id,
        signup_date,
        DATE_TRUNC('week', signup_date) AS signup_week
    FROM users
),
activity AS (
    SELECT DISTINCT
        user_id,
        activity_date
    FROM user_activity
),
retention AS (
    SELECT
        s.signup_week,
        s.user_id,
        CASE
            WHEN COUNT(a.activity_date) > 0 THEN 1
            ELSE 0
        END AS retained_week_1
    FROM signups s
    LEFT JOIN activity a
        ON s.user_id = a.user_id
       AND a.activity_date >= s.signup_date + INTERVAL '7 day'
       AND a.activity_date <  s.signup_date + INTERVAL '14 day'
    GROUP BY
        s.signup_week,
        s.user_id
)
SELECT
    signup_week,
    COUNT(*) AS signup_users,
    SUM(retained_week_1) AS retained_users,
    1.0 * SUM(retained_week_1) / COUNT(*) AS week_1_retention_rate
FROM retention
GROUP BY signup_week;
```

Dialect warning:

```text
DATE_TRUNC and INTERVAL syntax vary by SQL engine.
```

Strong answer:

```text
The tricky part is defining retention window and preserving all signup users with LEFT JOIN.
```


## 53. Funnel Query

Prompt:

```text
Calculate users who viewed product, added to cart, and purchased.
```

Pattern:

```sql
WITH user_steps AS (
    SELECT
        user_id,
        MIN(CASE WHEN event_type = 'view_product' THEN event_time END) AS view_time,
        MIN(CASE WHEN event_type = 'add_to_cart' THEN event_time END) AS cart_time,
        MIN(CASE WHEN event_type = 'purchase' THEN event_time END) AS purchase_time
    FROM events
    GROUP BY user_id
)
SELECT
    COUNT(CASE WHEN view_time IS NOT NULL THEN 1 END) AS viewed_users,
    COUNT(CASE WHEN view_time IS NOT NULL
                 AND cart_time IS NOT NULL
                 AND cart_time >= view_time THEN 1 END) AS cart_users,
    COUNT(CASE WHEN view_time IS NOT NULL
                 AND cart_time IS NOT NULL
                 AND purchase_time IS NOT NULL
                 AND cart_time >= view_time
                 AND purchase_time >= cart_time THEN 1 END) AS purchase_users
FROM user_steps;
```

Strong answer:

```text
Funnel queries require event order. Counting users who did all events is not enough if purchase happened before add_to_cart.
```


## 54. Cohort Query

Cohort analysis groups users by starting period and tracks behavior over future periods.

Example concept:

```text
signup_week + activity_week offset
```

Pattern:

```sql
WITH signups AS (
    SELECT
        user_id,
        DATE_TRUNC('week', signup_date) AS signup_week
    FROM users
),
activity AS (
    SELECT DISTINCT
        user_id,
        DATE_TRUNC('week', activity_date) AS activity_week
    FROM user_activity
),
cohort_activity AS (
    SELECT
        s.signup_week,
        a.activity_week,
        COUNT(DISTINCT s.user_id) AS active_users
    FROM signups s
    JOIN activity a
        ON s.user_id = a.user_id
       AND a.activity_week >= s.signup_week
    GROUP BY
        s.signup_week,
        a.activity_week
)
SELECT *
FROM cohort_activity;
```

Follow-ups:

- calculate week offset
- include inactive weeks
- divide by cohort size
- use calendar table
- handle timezone


## 55. Gaps and Islands

Gaps and islands questions identify consecutive ranges.

Use cases:

- consecutive login days
- continuous subscription periods
- missing dates
- active windows
- SLA gaps

Simple missing date pattern with calendar table:

```sql
SELECT
    c.calendar_date
FROM calendar c
LEFT JOIN daily_orders d
    ON c.calendar_date = d.order_date
WHERE d.order_date IS NULL;
```

Strong answer:

```text
For missing-date problems, I usually start with a calendar table because fact tables only contain dates where events exist.
```

Consecutive date problems often use:

```text
date - row_number offset
```

but exact syntax varies by dialect.


## 56. Sessions Query

Sessionization groups events when the gap between events exceeds a threshold.

Concept:

1. Sort events by user and event_time.
2. Use LAG to get previous event time.
3. Mark new session when gap > threshold.
4. Cumulative SUM of new-session flag creates session number.

Example concept:

```sql
WITH ordered AS (
    SELECT
        user_id,
        event_time,
        LAG(event_time) OVER (
            PARTITION BY user_id
            ORDER BY event_time
        ) AS previous_event_time
    FROM events
),
flagged AS (
    SELECT
        *,
        CASE
            WHEN previous_event_time IS NULL THEN 1
            WHEN event_time > previous_event_time + INTERVAL '30 minute' THEN 1
            ELSE 0
        END AS new_session_flag
    FROM ordered
),
sessionized AS (
    SELECT
        *,
        SUM(new_session_flag) OVER (
            PARTITION BY user_id
            ORDER BY event_time
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS session_number
    FROM flagged
)
SELECT *
FROM sessionized;
```

Strong answer:

```text
Sessionization requires ordering events per user and using LAG to detect gaps.
```


## 57. Query Performance Basics

SQL performance depends on:

- table size
- filter selectivity
- indexes/partitions
- join keys
- join order
- aggregation level
- distinct usage
- window sorting
- data skew
- file layout in warehouses/lakes
- scanned columns
- scanned partitions

Strong answer:

```text
I would first check the query plan and data volume. Then I would filter early, select only needed columns, aggregate before joining when appropriate, and ensure joins use correct keys.
```

Weak answer:

```text
Add index.
```

Too shallow and not always relevant in cloud warehouses.


## 58. Indexes

Indexes help lookup and filtering in row-store databases like OLTP systems.

Common index use:

- WHERE filters
- JOIN keys
- ORDER BY
- uniqueness enforcement

Strong answer:

```text
Indexes can improve lookups and joins in transactional databases, but in analytical warehouses, partitioning, clustering, columnar storage, and scan reduction may matter more.
```

Interview caution:

```text
Do not blindly suggest indexes for every SQL performance problem. Know the engine context.
```


## 59. Partitioning and Clustering

Analytical systems often use partitioning and clustering/sorting.

Partitioning:

```text
Physically/logically groups data by partition column such as event_date.
```

Clustering/sorting:

```text
Organizes data within partitions for faster pruning or joins depending on engine.
```

Strong answer:

```text
For large event tables, partitioning by event_date can reduce scanned data for date-filtered queries. Clustering by frequently filtered or joined columns may improve performance depending on the warehouse.
```


## 60. Filter Early and Pre-Aggregate

Good pattern:

```sql
WITH filtered_orders AS (
    SELECT
        order_id,
        customer_id,
        amount
    FROM orders
    WHERE order_date >= '2025-01-01'
      AND order_date <  '2025-02-01'
),
customer_revenue AS (
    SELECT
        customer_id,
        SUM(amount) AS revenue
    FROM filtered_orders
    GROUP BY customer_id
)
SELECT *
FROM customer_revenue;
```

Strong answer:

```text
Filtering early reduces data volume. Pre-aggregating before joining can prevent duplicate explosion and reduce join size.
```

But:

```text
Do not pre-aggregate if row-level detail is needed later.
```


## 61. SQL Query Review Checklist

When reviewing a SQL answer, check:

```text
Business question understood:
Output grain stated:
Base table correct:
Join type correct:
Join keys correct:
Many-to-many risk handled:
WHERE filters correct:
Date boundaries correct:
NULL handling correct:
Aggregation level correct:
Window partition correct:
Window ordering correct:
Tie-breaker included:
DISTINCT not abused:
Performance considered:
Validation checks included:
Communication structured:
```

If output grain, join risk, and window ordering are missing, score low.


## 62. Common SQL Mistakes

Common mistakes:

1. No output grain.
2. Wrong base table.
3. Wrong join type.
4. Missing join condition.
5. Many-to-many join explosion.
6. Using DISTINCT to hide duplicates.
7. Wrong GROUP BY level.
8. Filtering aggregates in WHERE.
9. Ignoring NULLs.
10. Wrong date boundary.
11. No timestamp tie-breaker.
12. ROW_NUMBER without correct PARTITION BY.
13. Ranking before aggregation.
14. Aggregating after duplicate join.
15. Inner join drops unmatched records.
16. WHERE clause breaks LEFT JOIN.
17. COUNT(column) when COUNT(*) needed.
18. COUNT(*) when distinct users needed.
19. No performance explanation.
20. No validation checks.


## 63. Basic SQL Drill Set

### Drill 1: Total Revenue Per Customer

Tables:

```text
orders(order_id, customer_id, order_date, amount, status)
```

Prompt:

```text
Return total successful revenue per customer.
```

Expected:

```sql
SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM orders
WHERE status = 'SUCCESS'
GROUP BY customer_id;
```

Must explain:

- output grain: customer
- filter before aggregation
- null amount handling if relevant

### Drill 2: Customers With No Orders

Tables:

```text
customers(customer_id, name)
orders(order_id, customer_id)
```

Expected:

```sql
SELECT
    c.customer_id,
    c.name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

Must explain:

- anti join pattern
- why LEFT JOIN from customers


## 64. Medium SQL Drill Set

### Drill 1: Latest Order Per Customer

Use ROW_NUMBER.

### Drill 2: Top 3 Products Per Category

Aggregate first, rank second.

### Drill 3: Daily Active Users

```sql
SELECT
    event_date,
    COUNT(DISTINCT user_id) AS active_users
FROM events
GROUP BY event_date;
```

### Drill 4: Duplicate Transaction IDs

```sql
SELECT
    transaction_id,
    COUNT(*) AS record_count
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;
```

### Drill 5: Source Target Reconciliation

Use FULL OUTER JOIN on counts by partition.

Mentor rule:

```text
Do not let candidate move to hard SQL until they can solve these without major hints.
```


## 65. Advanced SQL Drill Set

Advanced drills:

1. Week-1 retention by signup week.
2. Funnel conversion with ordered events.
3. Sessionization with 30-minute gap.
4. SCD Type 2 current record detection.
5. CDC merge staging validation.
6. Gaps and islands for consecutive login days.
7. Rolling 7-day active users.
8. Revenue reconciliation by date/product.
9. Top N per group with ties.
10. Late-arriving event correction.

Passing standard:

```text
Candidate explains grain, date window, dedupe logic, tie-breakers, and validation.
```


## 66. SQL Mock Interview 1: Joins and Aggregation

Prompt:

```text
Given customers and orders, return each customer's successful revenue in January 2025, including customers with no orders.
```

Expected approach:

1. Base table is customers because all customers must appear.
2. LEFT JOIN orders.
3. Put order filters carefully so customers with no orders remain.
4. Aggregate by customer.
5. Use COALESCE for revenue display.

Example:

```sql
SELECT
    c.customer_id,
    c.customer_name,
    COALESCE(SUM(o.amount), 0) AS january_revenue
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
   AND o.status = 'SUCCESS'
   AND o.order_date >= '2025-01-01'
   AND o.order_date <  '2025-02-01'
GROUP BY
    c.customer_id,
    c.customer_name;
```

Follow-ups:

1. Why are filters in ON instead of WHERE?
2. What if amount is null?
3. What is output grain?
4. How do you validate row count?
5. How do you optimize on large orders table?


## 67. SQL Mock Interview 2: Deduplication

Prompt:

```text
A staging table has duplicate customer records. Keep the latest record per customer_id using updated_at and ingestion_time as tie-breaker.
```

Expected:

```sql
WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY updated_at DESC, ingestion_time DESC
        ) AS rn
    FROM staging_customers
    WHERE customer_id IS NOT NULL
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Follow-ups:

1. What if updated_at is null?
2. What if customer_id is null?
3. Why not DISTINCT?
4. How do you validate duplicates removed?
5. How would this feed a MERGE?


## 68. SQL Mock Interview 3: Retention

Prompt:

```text
Calculate week-1 user retention by signup week.
```

Expected candidate behavior:

- define retention window
- preserve all signup users
- use LEFT JOIN activity
- count retained flag
- divide retained users by cohort size
- clarify date/week syntax by dialect

Fail conditions:

- counts activity rows instead of users
- inner joins and drops non-retained users
- no retention window definition
- no cohort grain


## 69. SQL Mock Interview 4: Funnel

Prompt:

```text
For each day, calculate users who viewed product, added to cart, and purchased in order.
```

Expected candidate behavior:

- define event order
- group by user/day or user session depending requirement
- use MIN event times
- enforce step order
- count users at each step
- clarify same-day vs cross-day funnel

Follow-ups:

1. What if user purchases without cart?
2. What if multiple views exist?
3. What if cart happens before view?
4. What is the output grain?
5. How would you optimize?


## 70. SQL Mock Interview 5: Reconciliation

Prompt:

```text
A target fact table has wrong counts. Write SQL to compare source and target row counts and revenue by order_date.
```

Expected:

- aggregate source by date
- aggregate target by date
- FULL OUTER JOIN
- compare counts and revenue
- handle missing dates
- show differences

Follow-ups:

1. Why not inner join?
2. How do you handle null dates?
3. What if revenue differs by small rounding amount?
4. How do you locate affected partition?
5. What is the next repair action?


## 71. SQL Performance Mock

Prompt:

```text
A query joining orders, order_items, customers, and products is slow and revenue is doubled. What do you do?
```

Strong answer:

```text
First I check correctness: doubled revenue suggests grain or join duplication issue. I identify fact grain, inspect join cardinalities, and pre-aggregate at the correct grain before joining. Then I check performance: filters, selected columns, partitions/indexes, join keys, and query plan.
```

Expected points:

- correctness before speed
- output grain
- many-to-many risk
- pre-aggregation
- no blind DISTINCT
- query plan
- filter early
- reduce scanned columns


## 72. SQL for Project Deep Dives

Candidates must explain SQL used in projects.

Weak:

```text
I wrote SQL queries for reports.
```

Strong:

```text
I wrote SQL transformations to load fact_sales from order and payment staging tables. I defined grain as one row per order item, joined product and customer dimensions, handled cancelled orders, deduplicated staging records using ROW_NUMBER, and added reconciliation checks for row count and revenue by date.
```

Project SQL explanation should include:

```text
Business problem:
Tables used:
Output table:
Output grain:
Main joins:
Transformations:
Dedupe logic:
Incremental logic:
Data quality checks:
Performance issue:
Optimization:
Impact:
My responsibility:
```


## 73. SQL and Data Engineering System Design

In system design, SQL appears in:

- warehouse transformations
- data quality checks
- reconciliation
- marts
- incremental loads
- SCD logic
- deduplication
- metric definitions
- dashboard serving

Strong answer:

```text
SQL transformations should be modular, testable, and aligned to clear data models. I would separate staging cleanup, intermediate transformations, and final marts instead of writing one huge query.
```

Red flag:

```text
One giant SQL query with no validation or ownership.
```


## 74. SQL Style Standards

Good interview SQL should be readable.

Rules:

1. Use meaningful aliases.
2. Put each selected column on its own line.
3. Use CTEs for complex logic.
4. Avoid SELECT * in final answers.
5. Use explicit join conditions.
6. Align GROUP BY with output grain.
7. Name derived columns clearly.
8. Include tie-breakers.
9. Keep filters readable.
10. Add comments only when they clarify business logic.

Good style:

```sql
WITH customer_revenue AS (
    SELECT
        customer_id,
        SUM(amount) AS total_revenue
    FROM orders
    WHERE status = 'SUCCESS'
    GROUP BY customer_id
)
SELECT
    customer_id,
    total_revenue
FROM customer_revenue
ORDER BY total_revenue DESC;
```


## 75. Communication Standard for SQL

Before writing query, candidate should say:

```text
The output grain is...
The base table is...
I will use LEFT JOIN because...
I will aggregate before ranking because...
I will use ROW_NUMBER because...
The date filter is inclusive start and exclusive end...
I will validate duplicates by...
```

Bad communication:

```text
Let me write query.
```

Strong communication:

```text
I will first define grain. Since the question asks for revenue per customer, the output is one row per customer. I will filter successful orders in January, group by customer_id, then left join to customers if customers with no revenue must appear.
```


## 76. SQL Feedback Templates

### Grain issue

```text
Your output grain is wrong. You grouped by extra columns, so the result is not one row per customer anymore.
```

### Join issue

```text
This join can multiply rows. Explain the relationship between the tables before summing metrics.
```

### DISTINCT misuse

```text
DISTINCT is hiding a duplicate problem. Fix the join or aggregation grain instead.
```

### Window issue

```text
Your ROW_NUMBER partition/order is wrong. Partition by the entity you need one row for and order by the timestamp that defines latest.
```

### Date issue

```text
Your date filter is risky for timestamps. Use inclusive start and exclusive end.
```

### Null issue

```text
You ignored NULL behavior. Decide whether nulls should be excluded, filled, or treated as data quality failures.
```


## 77. 7-Day SQL Repair Plan

### Day 1: Grain, SELECT, WHERE, GROUP BY

Drills:

- total revenue per customer
- revenue by date
- active users by date

Exit:

```text
Candidate states output grain before query.
```

### Day 2: Joins

Drills:

- customers with revenue
- customers without orders
- enrich orders with customer country

Exit:

```text
Candidate explains join type and unmatched records.
```

### Day 3: Duplicate risk

Drills:

- orders joined to order_items
- pre-aggregation before join
- detect duplicate keys

Exit:

```text
Candidate identifies join multiplication.
```

### Day 4: Window functions

Drills:

- latest order per customer
- top 3 products per category
- running total

Exit:

```text
Candidate uses correct PARTITION BY and ORDER BY.
```

### Day 5: Dates and NULLs

Drills:

- January revenue with timestamp
- null email counts
- missing required fields

Exit:

```text
Candidate handles date boundaries and nulls.
```

### Day 6: Data Engineering SQL

Drills:

- dedupe staging
- source-target reconciliation
- incremental load with watermark

Exit:

```text
Candidate explains pipeline use.
```

### Day 7: Mock interview

Prompt:

```text
Solve a mixed SQL interview with joins, windows, dedupe, and data quality.
```

Exit:

```text
Candidate scores at least 4/5.
```


## 78. 30-Day SQL Plan

### Week 1: Foundations

- SELECT
- WHERE
- GROUP BY
- HAVING
- CASE
- NULLs
- dates
- basic joins

Practice:

- revenue metrics
- counts
- filters
- simple joins

### Week 2: Joins and Grain

- join types
- anti joins
- semi joins
- many-to-many risk
- pre-aggregation
- DISTINCT risk

Practice:

- customers without orders
- fact/dimension joins
- duplicate detection
- reconciliation

### Week 3: Window Functions

- ROW_NUMBER
- RANK
- DENSE_RANK
- LAG
- LEAD
- running totals
- moving averages

Practice:

- latest record
- top N per group
- dedupe
- trend queries

### Week 4: Data Engineering SQL

- incremental loads
- MERGE concept
- SCD Type 1/2
- data quality
- retention
- funnels
- cohorts
- performance
- mocks


## 79. SQL LeetCode-Style Practice Map

High-ROI SQL problem types:

| Pattern | Example Problem Style |
|---|---|
| Aggregation | total revenue by customer |
| Conditional aggregation | success/failure counts |
| Joins | employees and departments |
| Anti join | customers with no orders |
| Window latest | latest record per group |
| Ranking | top N per group |
| Consecutive values | gaps and islands |
| Retention | users returning after signup |
| Funnel | ordered event steps |
| Reconciliation | source vs target differences |
| Data quality | duplicates/nulls/freshness |

Recommended practice focus:

1. Basic aggregation.
2. Joins and anti joins.
3. Window functions.
4. Top N per group.
5. Date ranges.
6. Retention and funnels.
7. Data quality/reconciliation.
8. Performance explanation.

Do not grind random SQL puzzles before mastering grain and joins.


## 80. SQL Readiness Thresholds

### Not SQL Interview Ready

- cannot define grain
- cannot write joins
- cannot aggregate correctly
- cannot use windows
- ignores nulls and dates

### Basic SQL Ready

- solves simple SELECT/GROUP BY/JOIN
- needs help on windows and edge cases

### Standard DE SQL Ready

- solves medium joins/windows/dedupe
- explains grain
- handles nulls/dates
- validates results

### FAANG-Prep SQL Ready

- solves medium+ under time
- handles follow-ups
- explains performance
- handles retention/funnel/reconciliation

### FAANG-Level SQL Ready

- consistent 4+/5 on mocks
- no critical grain mistakes
- strong communication
- handles ambiguity and edge cases


## 81. Final SQL Exit Test

Candidate must solve and explain this.

### Prompt

```text
You have:

customers(customer_id, customer_name, signup_date, country)

orders(order_id, customer_id, order_date, status, amount, updated_at, ingestion_time)

order_items(order_id, product_id, quantity, unit_price)

products(product_id, category)

events(event_id, user_id, event_type, event_time, ingestion_time)

Tasks:
1. Return January 2025 successful revenue per customer, including customers with zero revenue.
2. Return the latest order per customer.
3. Return top 3 products by revenue per category.
4. Detect duplicate event_ids and keep the latest event by event_time, ingestion_time.
5. Calculate daily active users by event_date.
6. Write one data quality check for null required fields.
7. Explain how you would validate source vs target revenue by date.
```

Passing answer must include:

- output grain for each query
- correct join type
- correct date filter
- correct aggregation
- deterministic ROW_NUMBER
- duplicate risk explanation
- null handling
- validation logic
- performance considerations

Fail if candidate:

- uses DISTINCT to hide joins
- misses output grain
- uses wrong join type
- misses timestamp tie-breaker
- ignores date boundaries
- cannot explain validation


## 82. Final Summary

SQL for Data Engineering interviews is not about writing syntax quickly.

It is about writing correct, explainable, production-aware queries.

The strongest candidates:

- define output grain first
- choose correct base table
- join safely
- avoid duplicate explosions
- aggregate at correct level
- use window functions correctly
- handle nulls and dates
- write data quality checks
- reconcile source and target
- explain performance
- communicate clearly

The weakest candidates:

```text
join tables first, add DISTINCT later, and hope the number looks right.
```

That is not acceptable.

Data Engineering Sensei should train SQL as interview engineering: correctness first, then clarity, then performance.


## 83. Drill Appendix

### Drill 1: Output Grain Drill

```text
For each prompt, state output grain before writing SQL: revenue per customer, daily active users, latest order per customer, top products per category.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 2: Join Type Drill

```text
For each scenario, choose INNER, LEFT, FULL, EXISTS, or anti join and explain why.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 3: Duplicate Explosion Drill

```text
Given orders and order_items, explain when revenue duplicates and how to fix it.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 4: Window Partition Drill

```text
Write ROW_NUMBER for latest record per customer, per product, and per order status.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 5: Date Boundary Drill

```text
Rewrite BETWEEN timestamp filters using inclusive start and exclusive end.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 6: NULL Drill

```text
Explain COUNT(*), COUNT(column), COALESCE, and IS NULL with examples.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 7: Conditional Aggregation Drill

```text
Calculate success, failed, and pending order counts in one query.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 8: Top N Drill

```text
Return top 3 products per category with and without ties.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 9: Retention Drill

```text
Define and calculate week-1 retention with LEFT JOIN.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 10: Funnel Drill

```text
Calculate ordered view -> cart -> purchase funnel.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 11: Reconciliation Drill

```text
Compare source and target counts and revenue by date.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 12: Incremental Load Drill

```text
Write source extraction using updated_at watermark and explain safe watermark update.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 13: SCD Drill

```text
Explain SCD Type 1 vs Type 2 and write the conceptual SQL steps.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 14: Performance Drill

```text
Given a slow query, list evidence you check before tuning.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.

### Drill 15: Project SQL Drill

```text
Explain one project SQL transformation with output grain, joins, checks, and impact.
```

Minimum passing standard:

- State the output grain.
- Explain the chosen SQL pattern.
- Mention edge cases.
- Mention validation.
- Avoid unsupported assumptions.
