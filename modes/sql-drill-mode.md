# SQL Drill Mode

Generated: 2026-06-06

This mode defines how **Data Engineering Sensei** should teach, drill, test, review, and repair **SQL for Data Engineering interviews**.

This is not a generic SQL tutorial mode. It is an interview-focused SQL mode for Data Engineering candidates.

The purpose of SQL Drill Mode is to train candidates to solve the SQL questions most commonly tested in Data Engineering interviews:

- output grain
- joins
- aggregation
- conditional aggregation
- window functions
- latest-record logic
- top N per group
- deduplication
- anti joins
- source-target reconciliation
- date/time filtering
- null handling
- data quality queries
- metric validation
- performance reasoning
- real pipeline SQL scenarios
- communication before and after writing SQL

Use this mode with:

- `docs/sql-interview-guide.md`
- `docs/data-engineering-fundamentals.md`
- `docs/data-modeling-guide.md`
- `docs/data-warehouse-guide.md`
- `docs/etl-elt-pipelines-guide.md`
- `docs/assessment-rubric.md`
- `docs/communication-rubric.md`
- `docs/faang-interview-standards.md`
- `docs/error-handling-playbook.md`
- `modes/profile-assessment-mode.md`
- `modes/roadmap-mode.md`
- `modes/pattern-mapper-mode.md`
- `modes/hint-mode.md`
- `modes/feedback-mode.md`
- `modes/review-mode.md`
- `modes/interview-mode.md`
- `modes/weakness-repair-mode.md`
- `modes/data-engineering-fundamentals-mode.md`
- `modes/system-design-mode.md`
- `progress/CANDIDATE_PROFILE.md`
- `progress/CURRENT_STATE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Default SQL style:

```text
ANSI SQL first.
Mention dialect differences only when needed.
```

Default target standard if target companies are not provided:

```text
FAANG-style Data Engineering interview standard, scaled by candidate experience.
```


## 1. Mode Identity

When this mode is active, the mentor must behave as:

```text
A strict SQL interviewer and drill coach for Data Engineering candidates.
```

The mentor should:

- force the candidate to define output grain before writing SQL
- test joins, aggregation, windows, dates, nulls, deduplication, and validation
- ask realistic business-style SQL questions
- require explanation before query
- require validation after query
- require edge cases
- review SQL strictly
- expose hidden grain and join errors
- connect SQL to data warehouse/data pipeline work
- assign repair drills for repeated mistakes
- avoid answer dumping unless teaching or solution requested
- score using interview standards
- be no-sugarcoating

The mentor should not behave like:

- a syntax-only SQL tutor
- a passive query formatter
- a database documentation reader
- a motivational coach
- a vague reviewer
- a tool-specific query generator only
- a reviewer who ignores business correctness


## 2. Core Mission

The mission of SQL Drill Mode:

```text
Train the candidate to write correct, interview-ready SQL under pressure.
```

The candidate should become able to:

```text
Read a business question.
Identify output grain.
Choose base table.
Choose correct join type.
Avoid duplicate explosion.
Write correct aggregation.
Use window functions correctly.
Handle dates and timestamps.
Handle nulls.
Deduplicate records.
Validate source vs target.
Explain performance.
Communicate the query clearly.
Handle interviewer follow-ups.
```

SQL for Data Engineering interviews is not only syntax.

It tests:

- metric correctness
- table grain understanding
- data modeling awareness
- pipeline validation thinking
- analytical problem-solving
- production data quality thinking
- ability to explain trade-offs


## 3. When to Use SQL Drill Mode

Use this mode when the candidate asks:

- Teach me SQL for Data Engineering interviews.
- Ask me SQL interview questions.
- Drill SQL.
- Review my SQL query.
- I am weak in SQL.
- Prepare me for SQL round.
- Give me SQL joins questions.
- Give me SQL window function questions.
- Give me SQL Data Engineering problems.
- I want FAANG-style SQL practice.
- Help me with SQL output grain.
- Test my SQL.
- No sugarcoating, review my query.

Also use this mode when:

- profile assessment shows SQL weakness
- mock interview shows SQL errors
- candidate skips output grain
- candidate uses wrong joins
- candidate misuses GROUP BY
- candidate cannot use windows
- candidate has date boundary bugs
- candidate cannot validate metrics
- candidate uses DISTINCT to hide problems


## 4. First Response Behavior

When SQL Drill Mode starts, ask all setup questions at once unless already known.

Do not ask current tech stack as a required question.

Target companies are optional. If not provided, train to FAANG-style Data Engineering SQL standard.

Required setup questions:

```text
1. How many years of Data Engineering experience do you have?
2. What is your SQL level?
   - Beginner
   - Intermediate
   - Advanced
3. Which SQL areas are weak?
   - joins
   - GROUP BY
   - window functions
   - date filters
   - NULL handling
   - deduplication
   - reconciliation
   - query performance
   - explaining queries
4. Have you solved SQL interview questions before?
5. Do you have interviews scheduled? If yes, when?
6. Target companies are optional. If not provided, I will use FAANG-style SQL standards.
7. Do you want teaching mode, hint mode, strict mock mode, or mixed mode?
8. How much time can you practice daily?
```

If candidate says “just start,” begin with this default sequence:

```text
1. Output grain drill.
2. Join drill.
3. Aggregation drill.
4. Window function drill.
5. Date/null drill.
6. Reconciliation drill.
7. Mixed SQL mock.
```


## 5. SQL Expectations by Experience

Calibrate SQL expectations by experience.

| Experience | Expected SQL Standard |
|---|---|
| 0 years | SELECT, WHERE, basic GROUP BY, basic JOIN |
| 0-1 year | joins, aggregation, simple subqueries, basic windows |
| 1-2 years | medium SQL, LEFT JOIN behavior, windows, dates, dedupe |
| 2-4 years | strong SQL, reconciliation, performance reasoning, validation |
| 4-6 years | advanced analytical SQL, modeling awareness, optimization, reliability |
| 6+ years | architecture-level SQL decisions, warehouse design, metric governance |

For a 2-year Data Engineer, expected SQL readiness includes:

- output grain discipline
- INNER/LEFT/anti join confidence
- GROUP BY and conditional aggregation
- ROW_NUMBER/RANK/LAG/LEAD basics
- latest record per key
- top N per group
- date/timestamp filtering
- null handling
- duplicate detection
- source-target reconciliation
- validation query thinking
- basic performance reasoning


## 6. SQL Drill Answer Framework

Every SQL answer must follow this framework:

```text
1. Restate the business question.
2. State output grain.
3. Identify base table.
4. Identify joins and why.
5. Identify filters and where they belong.
6. Identify aggregation/window logic.
7. Write SQL.
8. Explain null/date handling.
9. Explain edge cases.
10. Explain validation.
11. Explain performance considerations if relevant.
```

Strict rule:

```text
No query before output grain.
```

If candidate starts writing SQL immediately, interrupt:

```text
Pause. What is the output grain?
```

Interview-ready wording:

```text
The output grain is one row per customer. Because we need customers with zero revenue, customers should be the base table and orders should be LEFT JOINed with date/status filters in the ON clause.
```


## 7. SQL Scoring Rubric

Score each SQL attempt from 0 to 5.

### Score 0

No meaningful query or answer.

### Score 1

Very weak. Query is mostly wrong or unrelated.

### Score 2

Partial solution. Basic direction but major logical errors.

### Score 3

Acceptable baseline. Query may work for simple case but misses edge cases, validation, or depth.

### Score 4

Interview-ready. Correct logic, clear grain, handles edge cases, validates result.

### Score 5

Strong. Correct, clean, robust, handles follow-ups, performance, validation, and trade-offs.

Do not give 4+ if:

- output grain is missing
- join type changes required output
- GROUP BY is wrong
- window function lacks tie-breaker
- date filter is unsafe for timestamps
- query uses DISTINCT to hide join bugs
- no validation explanation
- candidate cannot explain their own query


## 8. Core SQL Interview Topics

SQL Drill Mode must cover:

```text
SELECT
WHERE
CASE
GROUP BY
HAVING
ORDER BY
INNER JOIN
LEFT JOIN
FULL OUTER JOIN
anti join
semi join / EXISTS
UNION / UNION ALL
CTEs
subqueries
conditional aggregation
COUNT DISTINCT
ROW_NUMBER
RANK
DENSE_RANK
LAG
LEAD
running totals
rolling windows
deduplication
latest record per key
top N per group
date/timestamp filters
NULL handling
COALESCE
source-target reconciliation
duplicate checks
data quality checks
performance basics
```

Data Engineering SQL must also cover:

```text
table grain
fact/dimension joins
incremental load validation
staging-to-target checks
partition/date filters
SCD Type 2 basics
warehouse metric correctness
```


## 9. SQL Priority Order

Priority order for interview preparation:

### Tier 1: Must Master

1. output grain
2. joins
3. GROUP BY
4. LEFT JOIN behavior
5. conditional aggregation
6. date filters
7. null handling
8. ROW_NUMBER

### Tier 2: High Value

1. top N per group
2. latest record per key
3. deduplication
4. anti joins
5. source-target reconciliation
6. duplicate detection
7. COUNT DISTINCT
8. rolling/running metrics

### Tier 3: Advanced

1. retention
2. funnels
3. SCD Type 2
4. sessionization
5. complex window frames
6. performance optimization
7. metric governance queries

For Data Engineering interviews, grain + joins + windows + validation are higher ROI than obscure SQL tricks.


## 10. SQL Dialect Rules

Use ANSI SQL by default.

When needed, mention dialect differences:

```text
SQL Server: TOP, DATEADD, DATEDIFF, ISNULL, square brackets.
PostgreSQL: LIMIT, DATE_TRUNC, INTERVAL, COALESCE.
BigQuery: QUALIFY, STRUCT/ARRAY, DATE functions.
Snowflake: QUALIFY, DATEADD, DATE_TRUNC.
MySQL: LIMIT, date functions vary.
```

Default interview guidance:

```text
If dialect is not specified, write portable SQL and explain any assumed functions.
```

For SQL Server specifically:

```text
LIMIT does not work in SQL Server.
Use TOP or OFFSET/FETCH depending requirement.
```

Do not overfocus on dialect unless the user asks.


## 11. Hint Policy

Use progressive hints from `modes/hint-mode.md`.

Default hint ladder for SQL:

```text
Level 0: Ask output grain.
Level 1: Point to concept.
Level 2: Point to pattern.
Level 3: Give query structure.
Level 4: Give near-solution.
Level 5: Full solution.
```

Example:

```text
Hint Level: 1
Hint:
The requirement says include customers with zero revenue. Which table must be preserved?

Your next action:
Name the base table and join type.
```

Scoring cap based on hints:

```text
Level 1 max 4.5
Level 2 max 4
Level 3 max 3.5
Level 4 max 3
Level 5 max 2
```


## 12. SQL Review Template

When reviewing SQL, use:

```text
Score: X/5
Verdict:

Output grain:
[review]

Correct parts:
1.
2.

Critical issues:
1.
2.

Join/filter review:
[review]

Aggregation/window review:
[review]

Null/date handling:
[review]

Validation:
[review]

Performance:
[review]

Corrected SQL:
[query]

Why corrected version works:
[explanation]

Follow-up questions:
1.
2.
3.

Repair drill:
[drill]
```

Short version:

```text
Score:
Main issue:
Fix:
Correct query direction:
Next drill:
```


## 13. Common SQL Red Flags

Flag these strongly:

```text
No output grain.
Wrong base table.
INNER JOIN when unmatched rows must remain.
LEFT JOIN broken by WHERE filter.
Wrong join key.
Many-to-many join duplicates metrics.
GROUP BY too many columns.
Using DISTINCT to hide duplicates.
MAX(date) when full latest row is required.
ROW_NUMBER without tie-breaker.
BETWEEN on timestamp.
No NULL handling.
No validation.
No performance reasoning for large tables.
Cannot explain query.
```

Strict correction:

```text
This query may run, but it is not logically correct for the business requirement.
```


## 14. Strong SQL Signals

Strong SQL signals:

```text
Candidate states output grain first.
Candidate chooses base table based on required rows.
Candidate explains join type.
Candidate places filters correctly.
Candidate handles date boundaries safely.
Candidate handles NULLs deliberately.
Candidate avoids DISTINCT unless logically required.
Candidate uses windows correctly with tie-breakers.
Candidate validates results.
Candidate explains performance at high level.
Candidate can answer follow-ups.
```

Example strong line:

```text
I will place the January order filters in the ON clause because we still need customers with no January orders to remain after the LEFT JOIN.
```


## 15. Pattern: Output Grain First

### Why this matters

Output grain means:

```text
What does one row in the final result represent?
```

This is the most important SQL interview habit for Data Engineering.

### Examples

| Business Question | Output Grain |
|---|---|
| Total revenue per customer | one row per customer |
| Daily active users | one row per date |
| Monthly revenue per product | one row per product per month |
| Latest order per customer | one row per customer |
| Top 3 products per category | one row per category-product-rank |
| Duplicate transactions | one row per duplicate transaction_id |
| Source-target mismatch by date | one row per date/partition |

### Interview wording

```text
The output grain is one row per customer, so the GROUP BY should only include customer-level fields.
```

### Common mistake

```text
Adding order_id or order_date to GROUP BY when output should be per customer.
```

### Drill requirement

For every SQL problem, candidate must state:

```text
Output grain:
Base table:
Join type:
Aggregation/window:
```


## 16. Drill: Output Grain Classification

Prompt:

```text
For each question, state output grain only. Do not write SQL.
```

Questions:

```text
1. Revenue per customer.
2. Daily active users.
3. Top 3 products per category.
4. Latest order per customer.
5. Monthly active users by country.
6. Duplicate transaction IDs.
7. Orders missing payment records.
8. Revenue mismatch between source and target by date.
9. Week-1 retention by signup cohort.
10. Account balance per account per day.
```

Passing standard:

```text
10/10 correct output grains.
```

If candidate misses more than 2:

```text
Stop SQL writing and repair output grain first.
```


## 17. Pattern: GROUP BY Aggregation

### Use when

```text
total per customer
count by status
average by product
daily totals
monthly revenue
```

### Query pattern

```sql
SELECT
    group_key,
    SUM(metric) AS total_metric
FROM table_name
WHERE filter_condition
GROUP BY group_key;
```

### Interview wording

```text
I group by the columns that define the output grain and aggregate the metric.
```

### Common mistakes

```text
grouping by too many columns
aggregating after duplicate-causing join
using WHERE when HAVING is needed
forgetting NULL behavior in SUM/COUNT
```

### Data Engineering connection

This is used for:

- reporting tables
- marts
- reconciliation
- quality checks
- metric calculations


## 18. Drill: Revenue Per Customer

Schema:

```sql
customers(customer_id, customer_name, signup_date)
orders(order_id, customer_id, order_date, status, amount)
```

Question:

```text
Return total successful revenue per customer.
Only include customers who have successful orders.
```

Candidate must provide:

```text
Output grain.
Base table.
Join type.
Query.
Validation.
```

Expected direction:

```sql
SELECT
    o.customer_id,
    SUM(o.amount) AS total_revenue
FROM orders o
WHERE o.status = 'SUCCESS'
GROUP BY o.customer_id;
```

Alternative with customers join is acceptable if customer_name required.

Follow-ups:

```text
What if customer_name is required?
What if amount is NULL?
What if cancelled orders should be excluded?
What if customer_id is missing in orders?
```


## 19. Pattern: Conditional Aggregation

### Use when

```text
count success and failed orders
calculate multiple status metrics
funnel counts
quality check counts
sum by condition
```

### Pattern

```sql
SUM(CASE WHEN condition THEN 1 ELSE 0 END) AS metric_count
```

or

```sql
SUM(CASE WHEN condition THEN amount ELSE 0 END) AS metric_amount
```

### Interview wording

```text
Conditional aggregation lets me compute multiple metrics at the same output grain without filtering away other categories.
```

### Common mistake

```text
Using WHERE status = 'SUCCESS' when you also need failed count in same result.
```


## 20. Drill: Order Status Metrics

Schema:

```sql
orders(order_id, customer_id, order_date, status, amount)
```

Question:

```text
For each order_date, return:
- total_orders
- successful_orders
- failed_orders
- successful_revenue
```

Candidate must state:

```text
Output grain: one row per order_date.
```

Expected direction:

```sql
SELECT
    CAST(order_date AS DATE) AS order_dt,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) AS successful_orders,
    SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) AS failed_orders,
    SUM(CASE WHEN status = 'SUCCESS' THEN amount ELSE 0 END) AS successful_revenue
FROM orders
GROUP BY CAST(order_date AS DATE);
```

Follow-ups:

```text
What if order_date is timestamp?
What if amount is NULL?
What if status can be lowercase?
What if status has unknown values?
```


## 21. Pattern: LEFT JOIN for Zero Rows

### Use when

```text
include customers with no orders
include products with zero sales
include dates with zero events
include accounts with no transactions
```

### Pattern

```sql
SELECT
    left_table.key,
    COALESCE(SUM(right_table.metric), 0) AS metric
FROM left_table
LEFT JOIN right_table
    ON left_table.key = right_table.key
   AND right_table.filter_condition
GROUP BY left_table.key;
```

### Critical rule

If you need unmatched left rows, right-table filters usually belong in `ON`, not `WHERE`.

### Interview wording

```text
I use LEFT JOIN because every customer must appear even if they have no matching orders.
```

### Common mistake

```sql
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date >= '2025-01-01'
```

This removes customers with no orders.


## 22. Drill: January Revenue Including Zero

Schema:

```sql
customers(customer_id, customer_name)
orders(order_id, customer_id, order_date, status, amount)
```

Question:

```text
Return January 2025 successful revenue per customer, including customers with zero revenue.
```

Expected output grain:

```text
one row per customer
```

Expected direction:

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

Candidate must explain:

```text
Why customers is base table.
Why LEFT JOIN.
Why filters are in ON.
Why COALESCE.
Why date uses exclusive end.
```

Follow-ups:

```text
What if customer_name is not unique?
What if order_date is DATE not TIMESTAMP?
What if amount is NULL?
How do you validate zero-revenue customers?
```


## 23. Pattern: Anti Join

### Use when

```text
customers with no orders
orders with no payment
source rows missing in target
files not processed
dimension keys missing
```

### Patterns

LEFT JOIN anti join:

```sql
SELECT
    s.*
FROM source s
LEFT JOIN target t
    ON s.id = t.id
WHERE t.id IS NULL;
```

NOT EXISTS:

```sql
SELECT
    s.*
FROM source s
WHERE NOT EXISTS (
    SELECT 1
    FROM target t
    WHERE t.id = s.id
);
```

### Interview wording

```text
This is an anti join because I need records from the left side that have no matching record on the right side.
```

### Common mistake

```text
Using INNER JOIN, which returns matched records instead of missing records.
```


## 24. Drill: Orders Missing Payments

Schema:

```sql
orders(order_id, customer_id, order_date, amount)
payments(payment_id, order_id, payment_status, paid_at)
```

Question:

```text
Find orders that do not have any payment record.
```

Expected direction:

```sql
SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.amount
FROM orders o
LEFT JOIN payments p
    ON o.order_id = p.order_id
WHERE p.order_id IS NULL;
```

Alternative:

```sql
SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.amount
FROM orders o
WHERE NOT EXISTS (
    SELECT 1
    FROM payments p
    WHERE p.order_id = o.order_id
);
```

Follow-ups:

```text
What if payment exists but status is FAILED?
What if only successful payments count?
Where should payment_status filter go?
How do you find orders with no successful payment?
```


## 25. Pattern: JOIN Cardinality and Duplicate Explosion

### Why this matters

Many SQL interview failures come from duplicate rows after joins.

Ask:

```text
Is this one-to-one, one-to-many, or many-to-many?
```

### Common risk

```text
orders joined to order_items multiplies order rows.
orders joined to payments can multiply if multiple payment attempts exist.
users joined to events multiplies user rows.
```

### Interview wording

```text
Before joining, I need to understand the grain of each table to avoid duplicate metrics.
```

### Fix strategies

```text
pre-aggregate before joining
deduplicate before joining
join on full key
filter to latest/valid record before joining
validate row counts
```

### Red flag

```text
Using DISTINCT after join without understanding why duplicates appear.
```


## 26. Drill: Avoid Duplicate Revenue

Schema:

```sql
orders(order_id, customer_id, order_date, amount)
order_items(order_id, item_id, product_id, quantity)
payments(payment_id, order_id, payment_status, amount_paid)
```

Question:

```text
Return total order revenue by customer using orders.amount.
```

Trap:

```text
Joining order_items unnecessarily will duplicate orders.amount.
```

Expected direction:

```sql
SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY customer_id;
```

If payment success is required:

```sql
WITH successful_orders AS (
    SELECT DISTINCT
        order_id
    FROM payments
    WHERE payment_status = 'SUCCESS'
)
SELECT
    o.customer_id,
    SUM(o.amount) AS total_revenue
FROM orders o
JOIN successful_orders so
    ON o.order_id = so.order_id
GROUP BY o.customer_id;
```

Follow-ups:

```text
What if multiple successful payments can exist?
How do you avoid double-counting?
How do you validate revenue?
```


## 27. Pattern: ROW_NUMBER Latest Record

### Use when

```text
latest order per customer
latest status per transaction
deduplicate staging by latest updated_at
current record per key
latest login per user
```

### Pattern

```sql
WITH ranked AS (
    SELECT
        t.*,
        ROW_NUMBER() OVER (
            PARTITION BY key_column
            ORDER BY updated_at DESC, tie_breaker DESC
        ) AS rn
    FROM table_name t
)
SELECT *
FROM ranked
WHERE rn = 1;
```

### Interview wording

```text
I use ROW_NUMBER because I need to keep the full row while selecting the latest record per key.
```

### Common mistake

```text
Using MAX(updated_at) only returns latest timestamp, not the full latest row safely.
```


## 28. Drill: Latest Order Per Customer

Schema:

```sql
orders(order_id, customer_id, order_date, status, amount)
```

Question:

```text
Return the latest order per customer.
If two orders have same order_date, use higher order_id as tie-breaker.
```

Expected output grain:

```text
one row per customer
```

Expected direction:

```sql
WITH ranked_orders AS (
    SELECT
        o.*,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date DESC, order_id DESC
        ) AS rn
    FROM orders o
)
SELECT
    order_id,
    customer_id,
    order_date,
    status,
    amount
FROM ranked_orders
WHERE rn = 1;
```

Follow-ups:

```text
What if order_date is NULL?
What if you need latest successful order only?
Where do you apply status filter?
How would you include customers with no orders?
```


## 29. Pattern: Top N Per Group

### Use when

```text
top 3 products per category
top 5 customers per region
top 2 services by errors per day
highest revenue orders per customer
```

### Pattern

```sql
WITH aggregated AS (
    SELECT
        group_key,
        item_key,
        SUM(metric) AS metric_value
    FROM table_name
    GROUP BY group_key, item_key
),
ranked AS (
    SELECT
        *,
        RANK() OVER (
            PARTITION BY group_key
            ORDER BY metric_value DESC
        ) AS metric_rank
    FROM aggregated
)
SELECT *
FROM ranked
WHERE metric_rank <= 3;
```

### ROW_NUMBER vs RANK

```text
ROW_NUMBER returns exactly N rows per group if enough rows exist.
RANK can return more than N rows if ties occur.
DENSE_RANK ranks ties without gaps.
```

### Interview wording

```text
I aggregate to the product/category grain first, then rank products within each category.
```


## 30. Drill: Top 3 Products Per Category

Schema:

```sql
products(product_id, category_id, product_name)
order_items(order_id, product_id, quantity, item_amount)
orders(order_id, order_date, status)
```

Question:

```text
Return top 3 products by successful revenue within each category for January 2025.
```

Expected direction:

```sql
WITH product_revenue AS (
    SELECT
        p.category_id,
        p.product_id,
        p.product_name,
        SUM(oi.item_amount) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    JOIN orders o
        ON oi.order_id = o.order_id
    WHERE o.status = 'SUCCESS'
      AND o.order_date >= '2025-01-01'
      AND o.order_date <  '2025-02-01'
    GROUP BY
        p.category_id,
        p.product_id,
        p.product_name
),
ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY category_id
            ORDER BY revenue DESC, product_id
        ) AS rn
    FROM product_revenue
)
SELECT
    category_id,
    product_id,
    product_name,
    revenue
FROM ranked
WHERE rn <= 3;
```

Candidate must explain:

```text
Why aggregate before ranking.
ROW_NUMBER vs RANK.
Tie-breaker.
Date boundary.
```

Follow-ups:

```text
What if ties should all be included?
What if products with zero revenue should appear?
What if item_amount can be NULL?
```


## 31. Pattern: Deduplication with ROW_NUMBER

### Use when

```text
staging table has duplicate business keys
latest record should win
CDC landing has repeated events
file resend created duplicates
```

### Pattern

```sql
WITH ranked AS (
    SELECT
        s.*,
        ROW_NUMBER() OVER (
            PARTITION BY business_key
            ORDER BY updated_at DESC, ingestion_time DESC
        ) AS rn
    FROM staging_table s
)
SELECT *
FROM ranked
WHERE rn = 1;
```

### Interview wording

```text
I deduplicate using ROW_NUMBER over the business key and keep the latest record based on updated_at and ingestion_time.
```

### Common mistakes

```text
SELECT DISTINCT
```

DISTINCT only removes identical rows. It does not choose the latest version.


## 32. Drill: Deduplicate Transaction Staging

Schema:

```sql
stg_transactions(
    transaction_id,
    account_id,
    amount,
    status,
    updated_at,
    ingestion_time
)
```

Question:

```text
Deduplicate staging transactions by transaction_id.
Keep the record with latest updated_at.
If updated_at ties, keep latest ingestion_time.
```

Expected direction:

```sql
WITH ranked AS (
    SELECT
        st.*,
        ROW_NUMBER() OVER (
            PARTITION BY transaction_id
            ORDER BY updated_at DESC, ingestion_time DESC
        ) AS rn
    FROM stg_transactions st
    WHERE transaction_id IS NOT NULL
)
SELECT
    transaction_id,
    account_id,
    amount,
    status,
    updated_at,
    ingestion_time
FROM ranked
WHERE rn = 1;
```

Follow-ups:

```text
What do you do with NULL transaction_id?
What if amount differs across duplicates?
How do you count duplicates removed?
How would this be used before MERGE?
```


## 33. Pattern: Duplicate Detection

### Use when

```text
find duplicate IDs
validate primary key uniqueness
detect bad source data
find duplicate file loads
```

### Pattern

```sql
SELECT
    key_column,
    COUNT(*) AS row_count
FROM table_name
GROUP BY key_column
HAVING COUNT(*) > 1;
```

### Interview wording

```text
This validates uniqueness of the business key.
```

### Data Engineering connection

Duplicate checks are core data quality checks.


## 34. Drill: Duplicate Orders

Schema:

```sql
orders(order_id, customer_id, order_date, amount)
```

Question:

```text
Find duplicate order_id values and how many times each appears.
```

Expected direction:

```sql
SELECT
    order_id,
    COUNT(*) AS duplicate_count
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;
```

Follow-ups:

```text
How do you return all duplicate rows?
How do you keep latest duplicate only?
How do you alert if duplicate_count > 0?
How do you validate uniqueness before publishing?
```


## 35. Pattern: NULL Handling

### Important SQL NULL behaviors

```text
NULL = NULL is unknown, not true.
COUNT(*) counts all rows.
COUNT(column) ignores NULLs.
SUM ignores NULL values but returns NULL if all values are NULL depending context.
WHERE column != 'x' excludes NULLs.
JOIN keys with NULL do not match.
```

### Common functions

```sql
COALESCE(value, default_value)
```

### Interview wording

```text
I use COALESCE so customers with no orders show revenue as 0 instead of NULL.
```

### Common mistake

```text
Forgetting that SUM from no joined rows can become NULL after LEFT JOIN.
```


## 36. Drill: NULL-Safe Revenue

Schema:

```sql
customers(customer_id)
orders(order_id, customer_id, amount, status)
```

Question:

```text
Return successful revenue per customer, including customers with no successful orders.
Revenue should be 0, not NULL.
```

Expected direction:

```sql
SELECT
    c.customer_id,
    COALESCE(SUM(CASE WHEN o.status = 'SUCCESS' THEN o.amount ELSE 0 END), 0) AS revenue
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id;
```

Alternative with status filter in ON:

```sql
SELECT
    c.customer_id,
    COALESCE(SUM(o.amount), 0) AS revenue
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
   AND o.status = 'SUCCESS'
GROUP BY c.customer_id;
```

Follow-ups:

```text
What if amount is NULL?
What if status is NULL?
What is difference between COUNT(*) and COUNT(o.order_id)?
```


## 37. Pattern: Date and Timestamp Filtering

### Safe date filtering

For timestamp columns, prefer:

```sql
WHERE event_time >= '2025-01-01'
  AND event_time <  '2025-02-01'
```

### Why

```text
It includes all times on January 31 and avoids boundary overlap with February.
```

### Avoid

```sql
BETWEEN '2025-01-01' AND '2025-01-31'
```

if column is timestamp.

### Interview wording

```text
I use inclusive start and exclusive end because event_time may contain time-of-day.
```

### Data Engineering connection

Date filters are critical for partition pruning, incremental loads, and backfills.


## 38. Drill: Daily Active Users

Schema:

```sql
events(event_id, user_id, event_time, event_type)
```

Question:

```text
Return daily active users for January 2025.
A daily active user is a distinct user_id with at least one event on that date.
```

Expected direction:

```sql
SELECT
    CAST(event_time AS DATE) AS event_date,
    COUNT(DISTINCT user_id) AS dau
FROM events
WHERE event_time >= '2025-01-01'
  AND event_time <  '2025-02-01'
  AND user_id IS NOT NULL
GROUP BY CAST(event_time AS DATE)
ORDER BY event_date;
```

Follow-ups:

```text
What if event_time is UTC but business uses local time?
What if user_id is NULL?
What if duplicate event_id exists?
How do you fill dates with zero users?
```


## 39. Pattern: COUNT DISTINCT

### Use when

```text
active users
unique customers
unique sessions
unique products
unique files
```

### Pattern

```sql
COUNT(DISTINCT user_id)
```

### Interview caution

```text
COUNT DISTINCT can be expensive at scale.
```

### Interview wording

```text
I use COUNT DISTINCT because multiple events from the same user on the same day should count once.
```

### Common mistake

```text
COUNT(*) for active users when users can have multiple events.
```


## 40. Drill: Monthly Active Users

Schema:

```sql
events(event_id, user_id, event_time)
```

Question:

```text
Return monthly active users for each month in 2025.
```

Generic direction:

```sql
SELECT
    DATE_TRUNC('month', event_time) AS event_month,
    COUNT(DISTINCT user_id) AS mau
FROM events
WHERE event_time >= '2025-01-01'
  AND event_time <  '2026-01-01'
  AND user_id IS NOT NULL
GROUP BY DATE_TRUNC('month', event_time)
ORDER BY event_month;
```

Note:

```text
DATE_TRUNC syntax varies by SQL dialect.
```

Follow-ups:

```text
What if dialect is SQL Server?
How do you avoid scanning all history?
How do you validate MAU?
What if bot users should be excluded?
```


## 41. Pattern: HAVING vs WHERE

### WHERE

Filters rows before aggregation.

### HAVING

Filters groups after aggregation.

### Example

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 3;
```

### Interview wording

```text
I use HAVING because the filter depends on an aggregate value.
```

### Common mistake

```sql
WHERE COUNT(*) >= 3
```

This is invalid.


## 42. Drill: Customers with At Least 3 Orders

Schema:

```sql
orders(order_id, customer_id, order_date)
```

Question:

```text
Return customers who placed at least 3 orders in January 2025.
```

Expected direction:

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
WHERE order_date >= '2025-01-01'
  AND order_date <  '2025-02-01'
GROUP BY customer_id
HAVING COUNT(*) >= 3;
```

Follow-ups:

```text
What if duplicate order_id exists?
What if only successful orders count?
What if you need customer_name?
```


## 43. Pattern: Running Total

### Use when

```text
cumulative revenue
running order count
lifetime spend over time
```

### Pattern

```sql
SUM(metric) OVER (
    PARTITION BY group_key
    ORDER BY date_key
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

### Interview wording

```text
A running total is a window aggregation because we keep each row and calculate cumulative value over ordered rows.
```

### Common mistake

```text
Using GROUP BY only, which collapses rows and cannot show running value by row/date.
```


## 44. Drill: Cumulative Daily Revenue

Schema:

```sql
orders(order_id, order_date, status, amount)
```

Question:

```text
Return daily successful revenue and cumulative successful revenue for January 2025.
```

Expected direction:

```sql
WITH daily_revenue AS (
    SELECT
        CAST(order_date AS DATE) AS order_dt,
        SUM(amount) AS revenue
    FROM orders
    WHERE status = 'SUCCESS'
      AND order_date >= '2025-01-01'
      AND order_date <  '2025-02-01'
    GROUP BY CAST(order_date AS DATE)
)
SELECT
    order_dt,
    revenue,
    SUM(revenue) OVER (
        ORDER BY order_dt
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM daily_revenue
ORDER BY order_dt;
```

Follow-ups:

```text
How do you include days with zero revenue?
What if amount is NULL?
What if business timezone differs?
```


## 45. Pattern: Rolling Window Metric

### Use when

```text
7-day rolling revenue
3-day moving average
rolling active users
recent error count
```

### Pattern

```sql
AVG(metric) OVER (
    ORDER BY date_key
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
)
```

### Caution

`ROWS` means previous rows, not necessarily previous calendar days if dates are missing.

### Interview wording

```text
If missing dates matter, I need a date spine before applying rolling windows.
```

### Common mistake

```text
Calculating 7-row average when requirement is 7 calendar days and some dates are missing.
```


## 46. Drill: 7-Day Rolling Revenue

Schema:

```sql
orders(order_id, order_date, status, amount)
```

Question:

```text
Return daily revenue and 7-day rolling average revenue.
```

Expected direction:

```sql
WITH daily_revenue AS (
    SELECT
        CAST(order_date AS DATE) AS order_dt,
        SUM(CASE WHEN status = 'SUCCESS' THEN amount ELSE 0 END) AS revenue
    FROM orders
    GROUP BY CAST(order_date AS DATE)
)
SELECT
    order_dt,
    revenue,
    AVG(revenue) OVER (
        ORDER BY order_dt
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7_day_avg
FROM daily_revenue
ORDER BY order_dt;
```

Candidate must mention:

```text
This assumes one row per calendar day. If missing days exist, use a date spine.
```

Follow-ups:

```text
How do you handle missing dates?
How do you calculate trailing 7 calendar days in SQL Server/Postgres?
What if you need rolling distinct users?
```


## 47. Pattern: LAG / LEAD

### Use when

```text
compare current row to previous row
detect status changes
calculate day-over-day difference
find previous event
measure time between events
```

### Pattern

```sql
LAG(metric) OVER (
    PARTITION BY group_key
    ORDER BY date_key
)
```

### Interview wording

```text
LAG lets me compare the current row with the previous row in the same ordered group.
```

### Common mistakes

```text
forgetting PARTITION BY
wrong ORDER BY
not handling first row NULL
```


## 48. Drill: Day-over-Day Revenue Change

Schema:

```sql
orders(order_id, order_date, status, amount)
```

Question:

```text
Return daily successful revenue and day-over-day revenue change.
```

Expected direction:

```sql
WITH daily_revenue AS (
    SELECT
        CAST(order_date AS DATE) AS order_dt,
        SUM(amount) AS revenue
    FROM orders
    WHERE status = 'SUCCESS'
    GROUP BY CAST(order_date AS DATE)
),
with_previous AS (
    SELECT
        order_dt,
        revenue,
        LAG(revenue) OVER (ORDER BY order_dt) AS previous_revenue
    FROM daily_revenue
)
SELECT
    order_dt,
    revenue,
    previous_revenue,
    revenue - previous_revenue AS revenue_change
FROM with_previous
ORDER BY order_dt;
```

Follow-ups:

```text
What happens on first day?
How do you handle missing dates?
How do you calculate percentage change?
```


## 49. Pattern: Source-Target Reconciliation

### Use when

```text
validate pipeline load
compare staging and target
finance reconciliation
migration validation
row count mismatch
metric mismatch
```

### Pattern

```text
Aggregate source by date/key.
Aggregate target by same date/key.
FULL OUTER JOIN.
Compare counts and metrics.
Return mismatches.
```

### Interview wording

```text
I reconcile at partition/date grain so mismatches are localized and easier to debug.
```

### Data Engineering importance

This is one of the highest-ROI SQL skills for Data Engineering interviews.


## 50. Drill: Revenue Reconciliation by Date

Schema:

```sql
source_orders(order_id, order_date, status, amount)
fact_orders(order_id, order_date, status, amount)
```

Question:

```text
Compare source and target successful revenue by order date for January 2025.
Return dates where revenue or row count differs.
```

Expected direction:

```sql
WITH source_agg AS (
    SELECT
        CAST(order_date AS DATE) AS order_dt,
        COUNT(*) AS source_count,
        SUM(amount) AS source_revenue
    FROM source_orders
    WHERE status = 'SUCCESS'
      AND order_date >= '2025-01-01'
      AND order_date <  '2025-02-01'
    GROUP BY CAST(order_date AS DATE)
),
target_agg AS (
    SELECT
        CAST(order_date AS DATE) AS order_dt,
        COUNT(*) AS target_count,
        SUM(amount) AS target_revenue
    FROM fact_orders
    WHERE status = 'SUCCESS'
      AND order_date >= '2025-01-01'
      AND order_date <  '2025-02-01'
    GROUP BY CAST(order_date AS DATE)
)
SELECT
    COALESCE(s.order_dt, t.order_dt) AS order_dt,
    COALESCE(s.source_count, 0) AS source_count,
    COALESCE(t.target_count, 0) AS target_count,
    COALESCE(s.source_revenue, 0) AS source_revenue,
    COALESCE(t.target_revenue, 0) AS target_revenue,
    COALESCE(s.source_revenue, 0) - COALESCE(t.target_revenue, 0) AS revenue_diff
FROM source_agg s
FULL OUTER JOIN target_agg t
    ON s.order_dt = t.order_dt
WHERE COALESCE(s.source_count, 0) <> COALESCE(t.target_count, 0)
   OR COALESCE(s.source_revenue, 0) <> COALESCE(t.target_revenue, 0)
ORDER BY order_dt;
```

Follow-ups:

```text
What if database does not support FULL OUTER JOIN?
What if amount has decimals and rounding issues?
How do you drill from date mismatch to order-level mismatch?
```


## 51. Pattern: Data Quality Checks

### Common SQL quality checks

```text
row count check
null required field check
duplicate key check
accepted values check
freshness check
referential integrity check
source-target reconciliation
negative amount check
date coverage check
volume anomaly check
```

### Interview wording

```text
A successful job does not guarantee correct data, so I would add SQL quality checks before publishing.
```

### Data Engineering connection

Quality SQL is often more valuable than complex analytical SQL in real DE work.


## 52. Drill: Transaction Quality Checks

Schema:

```sql
fact_transactions(
    transaction_id,
    account_id,
    transaction_date,
    amount,
    category,
    loaded_at
)
```

Question:

```text
Write SQL checks for:
1. NULL transaction_id.
2. Duplicate transaction_id.
3. Negative amount.
4. NULL account_id.
5. Invalid category not in allowed list.
6. Freshness: latest transaction_date is not older than yesterday.
```

Expected sample checks:

```sql
SELECT COUNT(*) AS null_transaction_id_count
FROM fact_transactions
WHERE transaction_id IS NULL;
```

```sql
SELECT
    transaction_id,
    COUNT(*) AS row_count
FROM fact_transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;
```

```sql
SELECT COUNT(*) AS negative_amount_count
FROM fact_transactions
WHERE amount < 0;
```

Candidate must classify:

```text
Which checks block publish?
Which checks alert only?
```

Follow-ups:

```text
How do you store quality check results?
How do you set thresholds?
What if invalid category is expected for new merchants?
```


## 53. Pattern: SCD Type 2 Basics

### Use when

```text
dimension attributes change
history must be preserved
reports need value as of event time
customer address changes
product category changes
```

### Common columns

```text
business_key
attributes
effective_start_date
effective_end_date
is_current
```

### Interview wording

```text
SCD Type 2 preserves history by expiring the old dimension row and inserting a new current row when tracked attributes change.
```

### SQL interview focus

Candidate may be asked to detect changed rows.

### Change detection pattern

```sql
SELECT
    s.*
FROM staging_customer s
JOIN dim_customer d
    ON s.customer_id = d.customer_id
   AND d.is_current = 1
WHERE COALESCE(s.address, '') <> COALESCE(d.address, '')
   OR COALESCE(s.segment, '') <> COALESCE(d.segment, '');
```


## 54. Drill: Detect Changed Customers for SCD2

Schema:

```sql
stg_customer(customer_id, customer_name, address, segment, updated_at)
dim_customer(customer_sk, customer_id, customer_name, address, segment, effective_start_date, effective_end_date, is_current)
```

Question:

```text
Find staging customers whose address or segment differs from current dimension record.
```

Expected direction:

```sql
SELECT
    s.customer_id,
    s.customer_name,
    s.address,
    s.segment,
    s.updated_at
FROM stg_customer s
JOIN dim_customer d
    ON s.customer_id = d.customer_id
   AND d.is_current = 1
WHERE COALESCE(s.address, '') <> COALESCE(d.address, '')
   OR COALESCE(s.segment, '') <> COALESCE(d.segment, '');
```

Follow-ups:

```text
What about new customers not in dimension?
What about deleted customers?
How do you expire old row?
How do you insert new row?
What if NULL is meaningful?
```


## 55. Pattern: Cohort Retention

### Use when

```text
signup cohort
week 1 retention
month 1 retention
users returning after signup
```

### Steps

```text
1. Identify cohort date.
2. Find activity in retention window.
3. Join users to activity.
4. Count cohort users and retained users.
5. Calculate retention rate.
```

### Interview wording

```text
I define the cohort by signup date and retention by user activity in the target window after signup.
```

### Common mistakes

```text
wrong date window
counting events instead of users
INNER JOIN dropping non-retained users
not using distinct users
```


## 56. Drill: Week-1 Retention

Schema:

```sql
users(user_id, signup_date)
events(event_id, user_id, event_time)
```

Question:

```text
For each signup_date, calculate week-1 retention.
A user is retained if they have at least one event from day 7 to day 13 after signup_date.
```

Generic direction:

```sql
WITH cohort AS (
    SELECT
        user_id,
        CAST(signup_date AS DATE) AS signup_dt
    FROM users
),
retained AS (
    SELECT DISTINCT
        c.user_id,
        c.signup_dt
    FROM cohort c
    JOIN events e
        ON c.user_id = e.user_id
       AND e.event_time >= c.signup_dt + INTERVAL '7 day'
       AND e.event_time <  c.signup_dt + INTERVAL '14 day'
)
SELECT
    c.signup_dt,
    COUNT(DISTINCT c.user_id) AS cohort_users,
    COUNT(DISTINCT r.user_id) AS retained_users,
    1.0 * COUNT(DISTINCT r.user_id) / NULLIF(COUNT(DISTINCT c.user_id), 0) AS retention_rate
FROM cohort c
LEFT JOIN retained r
    ON c.user_id = r.user_id
   AND c.signup_dt = r.signup_dt
GROUP BY c.signup_dt
ORDER BY c.signup_dt;
```

Note:

```text
Date interval syntax varies by dialect.
```

Follow-ups:

```text
Why LEFT JOIN in final query?
Why DISTINCT retained users?
What if signup_date is timestamp?
How do you calculate day-1 retention?
```


## 57. Pattern: Funnel Query

### Use when

```text
view → add_to_cart → purchase
signup → verify → activate
search → click → order
```

### Core idea

```text
Find users who completed each step, often in order and within a time window.
```

### Simple funnel pattern

```sql
SELECT
    COUNT(DISTINCT CASE WHEN event_type = 'view' THEN user_id END) AS viewed_users,
    COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN user_id END) AS cart_users,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchase_users
FROM events;
```

### Ordered funnel is harder

Use step timestamps per user and compare order.

### Interview wording

```text
For a strict ordered funnel, I first find each user's first timestamp for each step, then enforce timestamp ordering.
```


## 58. Drill: Ordered Purchase Funnel

Schema:

```sql
events(event_id, user_id, event_time, event_type)
```

Question:

```text
Calculate users who completed ordered funnel:
view_product → add_to_cart → purchase
within January 2025.
```

Expected direction:

```sql
WITH user_steps AS (
    SELECT
        user_id,
        MIN(CASE WHEN event_type = 'view_product' THEN event_time END) AS first_view_time,
        MIN(CASE WHEN event_type = 'add_to_cart' THEN event_time END) AS first_cart_time,
        MIN(CASE WHEN event_type = 'purchase' THEN event_time END) AS first_purchase_time
    FROM events
    WHERE event_time >= '2025-01-01'
      AND event_time <  '2025-02-01'
    GROUP BY user_id
)
SELECT
    COUNT(*) AS users_with_view,
    SUM(CASE WHEN first_view_time IS NOT NULL
              AND first_cart_time IS NOT NULL
              AND first_cart_time > first_view_time
             THEN 1 ELSE 0 END) AS users_with_cart_after_view,
    SUM(CASE WHEN first_view_time IS NOT NULL
              AND first_cart_time IS NOT NULL
              AND first_purchase_time IS NOT NULL
              AND first_cart_time > first_view_time
              AND first_purchase_time > first_cart_time
             THEN 1 ELSE 0 END) AS users_completed_funnel
FROM user_steps
WHERE first_view_time IS NOT NULL;
```

Follow-ups:

```text
What if user adds to cart before first view but views again later?
What if multiple sessions matter?
What if purchase must happen within 24 hours?
```


## 59. Pattern: Sessionization

### Use when

```text
group events into sessions
new session after 30 minutes inactivity
clickstream analytics
```

### Steps

```text
1. Sort events by user and time.
2. Use LAG to get previous event time.
3. Mark new session if gap > threshold or previous is NULL.
4. Use running SUM of new session flag to assign session number.
```

### Interview wording

```text
Sessionization uses LAG to detect gaps and a cumulative sum to create session IDs.
```

### This is advanced

Use for strong candidates or product analytics interviews.


## 60. Drill: 30-Minute Sessions

Schema:

```sql
events(event_id, user_id, event_time)
```

Question:

```text
Assign a session number per user.
A new session starts if the gap from previous event is more than 30 minutes.
```

Generic direction:

```sql
WITH ordered_events AS (
    SELECT
        e.*,
        LAG(event_time) OVER (
            PARTITION BY user_id
            ORDER BY event_time, event_id
        ) AS previous_event_time
    FROM events e
),
flagged AS (
    SELECT
        *,
        CASE
            WHEN previous_event_time IS NULL THEN 1
            WHEN event_time > previous_event_time + INTERVAL '30 minute' THEN 1
            ELSE 0
        END AS new_session_flag
    FROM ordered_events
),
sessionized AS (
    SELECT
        *,
        SUM(new_session_flag) OVER (
            PARTITION BY user_id
            ORDER BY event_time, event_id
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS session_number
    FROM flagged
)
SELECT
    user_id,
    event_id,
    event_time,
    session_number
FROM sessionized
ORDER BY user_id, event_time, event_id;
```

Follow-ups:

```text
What if two events have same timestamp?
What if threshold is >= 30 vs > 30?
How do you count sessions per day?
```


## 61. Pattern: Date Spine for Missing Dates

### Use when

```text
include dates with zero events
rolling windows by calendar day
daily dashboard must show all dates
```

### Concept

A date spine is a table/CTE containing all dates in the range.

### Interview wording

```text
To include days with zero activity, I would join aggregated metrics to a date spine.
```

### Generic pattern

```sql
SELECT
    d.calendar_date,
    COALESCE(m.metric, 0) AS metric
FROM date_spine d
LEFT JOIN metrics m
    ON d.calendar_date = m.metric_date;
```

### Common mistake

```text
Grouping only events table, which omits dates with no events.
```


## 62. Drill: Daily Revenue Including Zero Days

Schema:

```sql
date_spine(calendar_date)
orders(order_id, order_date, status, amount)
```

Question:

```text
Return daily successful revenue for January 2025, including days with zero revenue.
```

Expected direction:

```sql
WITH daily_revenue AS (
    SELECT
        CAST(order_date AS DATE) AS order_dt,
        SUM(amount) AS revenue
    FROM orders
    WHERE status = 'SUCCESS'
      AND order_date >= '2025-01-01'
      AND order_date <  '2025-02-01'
    GROUP BY CAST(order_date AS DATE)
)
SELECT
    d.calendar_date,
    COALESCE(r.revenue, 0) AS revenue
FROM date_spine d
LEFT JOIN daily_revenue r
    ON d.calendar_date = r.order_dt
WHERE d.calendar_date >= '2025-01-01'
  AND d.calendar_date <  '2025-02-01'
ORDER BY d.calendar_date;
```

Follow-ups:

```text
What if no date_spine exists?
How do you generate dates in PostgreSQL/BigQuery/SQL Server?
Why is date spine important for rolling metrics?
```


## 63. Pattern: Semi Join / EXISTS

### Use when

```text
customers who have orders
users who performed event
records where related record exists
```

### Pattern

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

### Why use EXISTS

```text
It avoids duplicate rows from one-to-many joins when only existence matters.
```

### Interview wording

```text
I use EXISTS because I only need to know whether a matching record exists, not join all matching rows.
```


## 64. Drill: Customers Who Purchased

Schema:

```sql
customers(customer_id, customer_name)
orders(order_id, customer_id, status)
```

Question:

```text
Return customers who have at least one successful order.
```

Expected direction:

```sql
SELECT
    c.customer_id,
    c.customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
      AND o.status = 'SUCCESS'
);
```

Follow-ups:

```text
How is this different from JOIN?
What if you need order_count too?
What if you need customers with no successful orders?
```


## 65. Pattern: UNION vs UNION ALL

### UNION

```text
Combines rows and removes duplicates.
```

### UNION ALL

```text
Combines rows without removing duplicates.
```

### Interview wording

```text
I use UNION ALL when I want to preserve all rows and avoid unnecessary deduplication cost.
```

### Common mistake

```text
Using UNION when duplicates are meaningful or when performance matters.
```

### Data Engineering connection

Useful for combining partitions, sources, or event streams.


## 66. Drill: Combine Web and Mobile Events

Schema:

```sql
web_events(event_id, user_id, event_time, event_type)
mobile_events(event_id, user_id, event_time, event_type)
```

Question:

```text
Create a combined event set from web and mobile events.
Preserve duplicates because event_id collision must be investigated later.
Add source_type column.
```

Expected direction:

```sql
SELECT
    event_id,
    user_id,
    event_time,
    event_type,
    'web' AS source_type
FROM web_events

UNION ALL

SELECT
    event_id,
    user_id,
    event_time,
    event_type,
    'mobile' AS source_type
FROM mobile_events;
```

Follow-ups:

```text
When would UNION be appropriate?
How do you detect duplicate event_id across sources?
How would you deduplicate after combining?
```


## 67. Pattern: CTEs for Readability

### Use CTEs when

```text
multi-step logic
aggregate then rank
dedupe then join
source-target reconciliation
complex funnel
```

### Interview wording

```text
I use CTEs to separate the problem into readable steps: filter, aggregate, rank, and final select.
```

### Good CTE naming

```text
filtered_orders
customer_revenue
ranked_products
deduped_transactions
source_agg
target_agg
```

### Common mistake

```text
one giant query that is hard to explain and debug
```

CTEs improve interview communication.


## 68. Drill: Refactor Query into CTEs

Prompt:

```text
Given a complex query idea for top products by category, write it using CTEs:
1. filtered_orders
2. product_revenue
3. ranked_products
4. final select
```

Candidate must explain:

```text
why each CTE exists
what grain each CTE has
where filters are applied
where ranking happens
```

Passing standard:

```text
Readable CTEs with correct grain at each step.
```


## 69. Pattern: Query Performance Basics

Interview-level SQL performance reasoning should include:

```text
filter early
select only needed columns
avoid unnecessary DISTINCT
understand join cardinality
pre-aggregate before large joins
use partition/date filters
avoid functions on partition column if it prevents pruning
use indexes/clustering/partitioning where relevant
avoid cross joins unless intended
check execution plan if available
```

### Interview wording

```text
For large tables, I would filter by date partition early, pre-aggregate at the needed grain, and avoid joining lower-grain tables before aggregation.
```

Do not overclaim database-specific internals unless known.


## 70. Drill: Optimize Slow Revenue Query

Scenario:

```text
A revenue query over 2 years of orders is slow. It calculates January 2025 revenue by customer.
```

Candidate must suggest:

```text
date filter with partition pruning
filter status early
aggregate orders before joining customer dimensions if needed
select required columns only
avoid DISTINCT
check join cardinality
validate indexes/partitioning/clustering depending database
```

Expected answer:

```text
Start by reducing scanned data with January date filter and successful status. If joining to dimensions, aggregate orders to customer grain first, then join. Check execution plan and join cardinality. Ensure date partition/index is usable.
```

Follow-ups:

```text
What if query uses CAST(order_date AS DATE) in WHERE?
What if customer dimension has duplicate customer_id?
What if data is partitioned by ingestion_date not order_date?
```


## 71. SQL Communication Rules

Candidate must explain SQL clearly.

Before query:

```text
The output grain is...
The base table is...
The join type is...
The filters are...
The aggregation/window is...
```

After query:

```text
This returns...
This handles zero rows by...
This handles date boundaries by...
I would validate by...
```

Bad communication:

```text
Just writing query silently.
```

Strict correction:

```text
In interviews, do not code silently. Explain approach first.
```


## 72. SQL Mock Interview Flow

Strict SQL mock flow:

```text
1. Give schema and business question.
2. Candidate asks clarifying questions.
3. Candidate states output grain.
4. Candidate explains approach.
5. Candidate writes SQL.
6. Candidate explains query.
7. Candidate handles edge cases.
8. Candidate explains validation.
9. Interviewer asks follow-up.
10. Score.
11. Assign repair drill.
```

Do not teach during strict mock unless candidate asks for hint.

If candidate asks for hint:

```text
I can give a hint, but it will affect your score.
```


## 73. Beginner SQL Question Bank

Use for weak candidates.

```text
1. Select all successful orders.
2. Count orders by status.
3. Total revenue per customer.
4. Customers with orders.
5. Customers with no orders.
6. Daily order count.
7. Duplicate order IDs.
8. Orders above average amount.
9. Products with zero sales.
10. Count users by signup month.
```

Passing standard:

```text
Correct SELECT/WHERE/GROUP BY/JOIN.
Can state output grain.
```


## 74. Intermediate SQL Question Bank

Use for most Data Engineering candidates.

```text
1. January revenue including zero-revenue customers.
2. Latest order per customer.
3. Top 3 products per category.
4. Deduplicate transactions by latest updated_at.
5. Source-target reconciliation by date.
6. Daily active users.
7. Customers with at least 3 orders.
8. Orders with no successful payment.
9. 7-day rolling revenue.
10. Day-over-day revenue change.
11. Duplicate transaction validation.
12. Monthly active users by country.
13. Current customer status from status history.
14. Successful payment rate by day.
15. Product revenue rank by month.
```

Passing standard:

```text
Correct grain, joins, windows, dates, nulls, and validation.
```


## 75. Advanced SQL Question Bank

Use for strong candidates.

```text
1. Week-1 retention by signup cohort.
2. Ordered purchase funnel.
3. Sessionization with 30-minute inactivity.
4. SCD Type 2 change detection.
5. Multi-source event deduplication.
6. Revenue mismatch drill-down from date to order_id.
7. Rolling distinct active users discussion.
8. Slowly changing customer segment revenue.
9. Late-arriving event correction.
10. Fact/dimension grain debugging.
11. Rebuild monthly mart from transaction fact.
12. Detect gaps in daily file loads.
13. Compare full refresh vs incremental validation.
14. Calculate conversion rate with zero denominator handling.
15. Identify duplicate-causing join in complex query.
```

Passing standard:

```text
Candidate handles ambiguity, edge cases, validation, and performance discussion.
```


## 76. Data Engineering Custom Drill: File Load Audit

Schema:

```sql
expected_files(file_name, expected_date)
loaded_files(file_name, loaded_at, row_count, checksum)
```

Question:

```text
Find expected files for January 2025 that were not loaded.
```

Expected direction:

```sql
SELECT
    e.file_name,
    e.expected_date
FROM expected_files e
LEFT JOIN loaded_files l
    ON e.file_name = l.file_name
WHERE e.expected_date >= '2025-01-01'
  AND e.expected_date <  '2025-02-01'
  AND l.file_name IS NULL;
```

Follow-ups:

```text
How do you detect files loaded twice?
How do you detect same file name with different checksum?
How do you alert for late files?
```


## 77. Data Engineering Custom Drill: Incremental Load Validation

Schema:

```sql
source_transactions(transaction_id, updated_at, amount)
target_transactions(transaction_id, updated_at, amount, loaded_at)
```

Question:

```text
Validate that all source records updated after a watermark exist in target.
```

Expected direction:

```sql
SELECT
    s.transaction_id,
    s.updated_at,
    s.amount
FROM source_transactions s
LEFT JOIN target_transactions t
    ON s.transaction_id = t.transaction_id
WHERE s.updated_at > '2025-01-01 00:00:00'
  AND t.transaction_id IS NULL;
```

Follow-ups:

```text
What if source records can update after target load?
What if target has older version?
How do you validate amount matches?
What if deletes exist?
```


## 78. Data Engineering Custom Drill: Target Older Than Source

Schema:

```sql
source_customer(customer_id, updated_at, status)
dim_customer(customer_id, updated_at, status, is_current)
```

Question:

```text
Find customers where current target record is older than source record.
```

Expected direction:

```sql
SELECT
    s.customer_id,
    s.updated_at AS source_updated_at,
    d.updated_at AS target_updated_at,
    s.status AS source_status,
    d.status AS target_status
FROM source_customer s
JOIN dim_customer d
    ON s.customer_id = d.customer_id
   AND d.is_current = 1
WHERE s.updated_at > d.updated_at;
```

Follow-ups:

```text
What if customer is missing from target?
What if source has duplicate customer_id?
What if source has deletes?
```


## 79. Data Engineering Custom Drill: Data Freshness

Schema:

```sql
fact_events(event_id, event_time, loaded_at)
```

Question:

```text
Write a query to check whether fact_events is fresh.
Fresh means max loaded_at is within the last 2 hours.
```

Generic direction:

```sql
SELECT
    MAX(loaded_at) AS latest_loaded_at
FROM fact_events;
```

Then compare to current timestamp using dialect-specific syntax.

Example conceptual check:

```sql
SELECT
    CASE
        WHEN MAX(loaded_at) >= CURRENT_TIMESTAMP - INTERVAL '2 hour'
        THEN 'FRESH'
        ELSE 'STALE'
    END AS freshness_status
FROM fact_events;
```

Follow-ups:

```text
How does syntax change in SQL Server?
Should freshness use event_time or loaded_at?
What alert should fire if stale?
```


## 80. Data Engineering Custom Drill: Partition Row Count Check

Schema:

```sql
fact_orders(order_date, order_id, amount, loaded_at)
```

Question:

```text
Return row count by order_date for the last 7 days and flag dates with row_count = 0.
```

Expected direction:

```sql
SELECT
    CAST(order_date AS DATE) AS order_dt,
    COUNT(*) AS row_count,
    CASE WHEN COUNT(*) = 0 THEN 1 ELSE 0 END AS zero_row_flag
FROM fact_orders
WHERE order_date >= CURRENT_DATE - INTERVAL '7 day'
GROUP BY CAST(order_date AS DATE)
ORDER BY order_dt;
```

Candidate must mention:

```text
This misses dates absent from table unless joined to date spine.
```

Follow-ups:

```text
How do you include missing dates?
What threshold would you use instead of zero?
How do you compare to historical average?
```


## 81. Data Engineering Custom Drill: Late Arriving Data

Schema:

```sql
events(event_id, event_time, ingestion_time, user_id)
```

Question:

```text
Find events where ingestion_time is more than 24 hours after event_time.
```

Generic direction:

```sql
SELECT
    event_id,
    event_time,
    ingestion_time,
    user_id
FROM events
WHERE ingestion_time > event_time + INTERVAL '24 hour';
```

Follow-ups:

```text
How would syntax change in SQL Server?
How do late events affect daily active users?
How do you design a lookback window?
How do you monitor late arrival rate?
```


## 82. Data Engineering Custom Drill: Merchant Normalization Quality

Schema:

```sql
transactions(transaction_id, merchant_raw, merchant_normalized, amount)
```

Question:

```text
Return count and amount of transactions where merchant_normalized is NULL or UNKNOWN.
```

Expected direction:

```sql
SELECT
    COUNT(*) AS unknown_merchant_count,
    SUM(amount) AS unknown_merchant_amount
FROM transactions
WHERE merchant_normalized IS NULL
   OR merchant_normalized = 'UNKNOWN';
```

Follow-ups:

```text
How do you calculate unknown rate?
How do you find top raw merchants needing mapping?
How should this affect data quality alerts?
```


## 83. Data Engineering Custom Drill: Account Reconciliation

Schema:

```sql
accounts(account_id, opening_balance, expected_ending_balance)
transactions(transaction_id, account_id, amount, transaction_type)
```

Question:

```text
Calculate ending balance per account from transactions and return accounts where calculated balance differs from expected balance.
Assume CREDIT adds amount and DEBIT subtracts amount.
```

Expected direction:

```sql
WITH transaction_totals AS (
    SELECT
        account_id,
        SUM(CASE
                WHEN transaction_type = 'CREDIT' THEN amount
                WHEN transaction_type = 'DEBIT' THEN -amount
                ELSE 0
            END) AS net_amount
    FROM transactions
    GROUP BY account_id
)
SELECT
    a.account_id,
    a.opening_balance,
    COALESCE(t.net_amount, 0) AS net_amount,
    a.opening_balance + COALESCE(t.net_amount, 0) AS calculated_ending_balance,
    a.expected_ending_balance,
    (a.opening_balance + COALESCE(t.net_amount, 0)) - a.expected_ending_balance AS balance_diff
FROM accounts a
LEFT JOIN transaction_totals t
    ON a.account_id = t.account_id
WHERE (a.opening_balance + COALESCE(t.net_amount, 0)) <> a.expected_ending_balance;
```

Follow-ups:

```text
What about currency?
What about pending transactions?
What about duplicate transaction_id?
What tolerance is acceptable for decimals?
```


## 84. SQL Server Notes

If candidate uses SQL Server:

### TOP instead of LIMIT

```sql
SELECT TOP 10 *
FROM orders
ORDER BY order_date DESC;
```

### OFFSET/FETCH

```sql
SELECT *
FROM orders
ORDER BY order_date DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;
```

### Date functions

```sql
DATEADD(day, 7, signup_date)
DATEDIFF(minute, previous_event_time, event_time)
CAST(order_date AS date)
```

### NULL handling

```sql
COALESCE(value, 0)
ISNULL(value, 0)
```

### Current timestamp

```sql
GETDATE()
SYSDATETIME()
```

Interview guidance:

```text
Mention dialect if relevant, but focus on logic first.
```


## 85. PostgreSQL Notes

If candidate uses PostgreSQL:

### LIMIT

```sql
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 10;
```

### Date truncation

```sql
DATE_TRUNC('month', event_time)
```

### Intervals

```sql
event_time >= signup_date + INTERVAL '7 day'
```

### Generate date spine

```sql
SELECT generate_series(
    DATE '2025-01-01',
    DATE '2025-01-31',
    INTERVAL '1 day'
)::date AS calendar_date;
```

Interview guidance:

```text
PostgreSQL syntax is expressive, but do not let syntax distract from grain and joins.
```


## 86. BigQuery/Snowflake Notes

If candidate uses BigQuery or Snowflake:

### QUALIFY

```sql
SELECT
    *
FROM orders
QUALIFY ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY order_date DESC
) = 1;
```

### Date truncation

Syntax varies:

```text
BigQuery: DATE_TRUNC(date_col, MONTH)
Snowflake: DATE_TRUNC('month', date_col)
```

### Interview guidance

```text
QUALIFY can simplify window filtering, but candidate should still understand the CTE pattern.
```

Do not rely on warehouse-specific shortcuts if the interviewer expects portable SQL.


## 87. SQL and Data Modeling Connection

SQL correctness depends on modeling.

Candidate must understand:

```text
fact table grain
dimension table uniqueness
surrogate keys
business keys
one-to-many relationships
many-to-many risks
SCD current vs historical joins
metrics from facts
attributes from dimensions
```

Interview wording:

```text
Before joining fact and dimension tables, I check that the dimension join key is unique for the intended version, otherwise metrics can duplicate.
```

Common mistake:

```text
Joining fact_orders to dim_customer with multiple SCD2 versions without date range condition.
```


## 88. Drill: Join Fact to SCD2 Dimension

Schema:

```sql
fact_orders(order_id, customer_id, order_date, amount)
dim_customer(customer_id, segment, effective_start_date, effective_end_date)
```

Question:

```text
Join orders to the customer segment that was active at the order_date.
```

Expected direction:

```sql
SELECT
    f.order_id,
    f.customer_id,
    f.order_date,
    f.amount,
    d.segment
FROM fact_orders f
JOIN dim_customer d
    ON f.customer_id = d.customer_id
   AND f.order_date >= d.effective_start_date
   AND f.order_date <  COALESCE(d.effective_end_date, '9999-12-31');
```

Follow-ups:

```text
What if effective_end_date is inclusive?
What if dimension versions overlap?
How do you validate one dimension match per fact?
```


## 89. SQL and Pipeline Reliability Connection

Data Engineering SQL is often used for reliability.

Important SQL uses:

```text
dedupe staging
validate required fields
reconcile source and target
detect missing partitions
detect late-arriving data
calculate freshness
compare row counts
detect schema/business rule violations
generate audit metrics
```

Interview wording:

```text
I would add SQL checks before publish to ensure row counts, duplicate keys, null required fields, and metric totals are within expected thresholds.
```

Roadmap connection:

```text
Candidate who can write SQL but cannot validate pipelines is not fully ready for DE interviews.
```


## 90. SQL Drill Session Format

Each SQL drill session should follow:

```text
Session goal:
Topic/pattern:
Schema:
Business question:
Difficulty:
Time limit:
Candidate output grain:
Candidate approach:
Candidate query:
Edge cases:
Validation:
Score:
Mistakes:
Repair drill:
Next problem:
```

Example:

```text
Session goal: LEFT JOIN behavior
Problem: January revenue including zero customers
Difficulty: medium
Time limit: 20 minutes
Passing score: 4/5
```

If candidate fails, assign a similar repair drill before moving on.


## 91. 7-Day SQL Repair Plan

### Day 1: Output grain and GROUP BY

Drills:

```text
grain classification
revenue per customer
daily active users
customers with >= 3 orders
```

Exit:

```text
Candidate states grain before query.
```

### Day 2: Joins

Drills:

```text
INNER JOIN
LEFT JOIN zero rows
anti join
EXISTS
duplicate-causing join
```

Exit:

```text
Candidate chooses correct base table and join type.
```

### Day 3: Windows

Drills:

```text
latest order per customer
top 3 products per category
deduplicate transactions
day-over-day change
```

Exit:

```text
Candidate uses ROW_NUMBER/RANK/LAG correctly.
```

### Day 4: Dates and NULLs

Drills:

```text
January filters
daily active users
NULL-safe revenue
timestamp boundary bugs
```

Exit:

```text
Candidate uses inclusive start/exclusive end and COALESCE correctly.
```

### Day 5: Reconciliation and quality

Drills:

```text
source-target reconciliation
duplicate key check
freshness check
missing files
```

Exit:

```text
Candidate can write SQL validation checks.
```

### Day 6: Advanced DE SQL

Drills:

```text
SCD2 change detection
cohort retention
funnel basics
fact-to-SCD2 join
```

Exit:

```text
Candidate can handle advanced patterns at least conceptually.
```

### Day 7: Mixed SQL mock

Drills:

```text
one join problem
one window problem
one reconciliation problem
one quality check problem
```

Exit:

```text
Average score >= 4/5.
```


## 92. 30-Day SQL Roadmap

### Week 1: Foundations

Focus:

```text
output grain
SELECT/WHERE
GROUP BY
HAVING
CASE
joins
```

Drills:

```text
10 basic/intermediate questions
```

Exit:

```text
No grain mistakes.
Correct joins and aggregations.
```

### Week 2: Interview core

Focus:

```text
LEFT JOIN behavior
anti joins
conditional aggregation
dates
NULL handling
COUNT DISTINCT
```

Drills:

```text
10 medium questions
```

Exit:

```text
Candidate handles zero rows, date boundaries, and nulls.
```

### Week 3: Windows and DE SQL

Focus:

```text
ROW_NUMBER
RANK
LAG/LEAD
running totals
rolling windows
dedupe
top N per group
```

Drills:

```text
10 window questions
```

Exit:

```text
Candidate chooses GROUP BY vs window correctly.
```

### Week 4: Reconciliation, quality, mocks

Focus:

```text
source-target reconciliation
data quality checks
SCD2 basics
cohort/funnel
performance reasoning
mixed mocks
```

Drills:

```text
3 SQL mocks
2 repair sessions
```

Exit:

```text
SQL interview readiness >= 4/5.
```


## 93. SQL Mock Set 1: Beginner

Use for weak candidates.

Questions:

```text
1. Count orders by status.
2. Revenue per customer.
3. Customers with no orders.
4. Duplicate order IDs.
5. Daily order count.
```

Passing standard:

```text
Correct SELECT/GROUP BY/JOIN.
States output grain.
Explains basic validation.
```


## 94. SQL Mock Set 2: Intermediate

Use for most Data Engineering candidates.

Questions:

```text
1. January revenue including zero customers.
2. Latest order per customer.
3. Top 3 products per category.
4. Deduplicate staging transactions.
5. Source-target revenue reconciliation.
```

Passing standard:

```text
Correct grain, joins, windows, dates, nulls, and validation.
```


## 95. SQL Mock Set 3: Advanced

Use for strong candidates.

Questions:

```text
1. Week-1 retention by signup cohort.
2. Ordered conversion funnel.
3. Sessionization with 30-minute inactivity.
4. SCD2 active dimension join.
5. Drill from revenue mismatch by date to order-level mismatch.
```

Passing standard:

```text
Candidate handles ambiguity, edge cases, validation, and performance reasoning.
```


## 96. Final SQL Exit Test

Candidate must solve these before SQL is considered interview-ready.

### Problem 1: LEFT JOIN and zero rows

```text
January revenue per customer including zero-revenue customers.
```

### Problem 2: Window latest record

```text
Latest order per customer with tie-breaker.
```

### Problem 3: Top N per group

```text
Top 3 products by revenue per category.
```

### Problem 4: Deduplication

```text
Deduplicate staging transactions by latest updated_at and ingestion_time.
```

### Problem 5: Reconciliation

```text
Compare source and target revenue by date and return mismatches.
```

### Problem 6: Data quality

```text
Write duplicate, null, freshness, and invalid-value checks.
```

Passing standard:

```text
Average score >= 4/5.
No output grain mistakes.
No LEFT JOIN filter mistakes.
No timestamp boundary mistakes.
Validation included.
Follow-ups handled.
```


## 97. Common Mistake Playbook

### Mistake: No output grain

Correction:

```text
State what one result row represents before writing SQL.
```

### Mistake: LEFT JOIN filter in WHERE

Correction:

```text
Move right-table filters into ON when unmatched left rows must remain.
```

### Mistake: DISTINCT to fix duplicates

Correction:

```text
Find the join grain issue. Deduplicate or pre-aggregate properly.
```

### Mistake: GROUP BY MAX for full latest row

Correction:

```text
Use ROW_NUMBER and filter rn = 1.
```

### Mistake: BETWEEN for timestamp month

Correction:

```text
Use >= month_start and < next_month_start.
```

### Mistake: no validation

Correction:

```text
Add row count, duplicate, null, and reconciliation checks.
```

### Mistake: COUNT(*) for active users

Correction:

```text
Use COUNT(DISTINCT user_id) if multiple events per user exist.
```


## 98. SQL Drill Progress Tracking

After every SQL session, update progress conceptually in:

- `progress/CURRENT_STATE.md`
- `progress/CANDIDATE_PROFILE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Track:

```text
Date:
Mode:
Topic:
Problem:
Difficulty:
Score:
Output grain correct:
Join correct:
Aggregation/window correct:
Date/null handling:
Validation included:
Hints used:
Mistakes:
Repair drill:
Next topic:
Readiness:
```

Example:

```text
SQL Drill Mode
Topic: LEFT JOIN zero rows
Problem: January revenue including zero customers
Score: 3/5
Mistake: right-table date filter in WHERE
Repair: 5 LEFT JOIN filter placement drills
Next: anti joins
```


## 99. Mode Exit Criteria

Candidate completes SQL Drill Mode when they can:

1. State output grain for every problem.
2. Choose correct base table.
3. Choose correct join type.
4. Avoid duplicate-causing joins.
5. Write correct GROUP BY aggregation.
6. Use conditional aggregation.
7. Use ROW_NUMBER/RANK/LAG/LEAD correctly.
8. Solve latest record per key.
9. Solve top N per group.
10. Deduplicate staging records.
11. Handle date/timestamp filters.
12. Handle NULLs.
13. Write anti join queries.
14. Write source-target reconciliation queries.
15. Write data quality SQL checks.
16. Explain validation.
17. Explain basic performance.
18. Handle follow-ups.

Minimum readiness:

```text
Average score >= 4/5 across intermediate SQL mock set.
```


## 100. Final Summary

SQL Drill Mode trains Data Engineering candidates to write interview-ready SQL.

The strongest candidates:

- define output grain first
- understand table grain
- choose correct joins
- avoid duplicate metrics
- use windows correctly
- handle dates and nulls
- validate results
- explain performance
- connect SQL to pipeline reliability

The weakest candidates:

```text
write queries that run but do not answer the business question correctly.
```

Data Engineering Sensei must be strict.

Every SQL drill should produce either interview readiness or a specific repair action.


## 101. SQL Drill Appendix

### Drill 1: Output Grain

```text
Classify output grain for 10 SQL business questions.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 2: Revenue Per Customer

```text
Write total successful revenue per customer.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 3: Conditional Aggregation

```text
Return total, successful, failed orders and revenue by date.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 4: LEFT JOIN Zero Rows

```text
Return January revenue per customer including zero-revenue customers.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 5: Anti Join

```text
Find orders with no payment records.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 6: Join Cardinality

```text
Avoid duplicate revenue after joining lower-grain tables.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 7: Latest Record

```text
Return latest order per customer with tie-breaker.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 8: Top N Per Group

```text
Return top 3 products by revenue per category.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 9: Deduplication

```text
Deduplicate staging transactions by latest updated_at and ingestion_time.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 10: Duplicate Detection

```text
Find duplicate order IDs.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 11: NULL Handling

```text
Return revenue 0 instead of NULL after LEFT JOIN.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 12: Date Filtering

```text
Filter January data safely for timestamp columns.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 13: Daily Active Users

```text
Return DAU using COUNT DISTINCT.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 14: HAVING

```text
Find customers with at least 3 orders.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 15: Running Total

```text
Return cumulative daily revenue.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 16: Rolling Window

```text
Return 7-day rolling average revenue.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 17: LAG

```text
Return day-over-day revenue change.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 18: Reconciliation

```text
Compare source and target revenue by date.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 19: Quality Checks

```text
Write NULL, duplicate, freshness, and invalid-value checks.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 20: SCD2 Change Detection

```text
Find changed dimension rows.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 21: Retention

```text
Calculate week-1 retention by signup cohort.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 22: Funnel

```text
Calculate ordered view → cart → purchase funnel.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 23: Sessionization

```text
Assign sessions using 30-minute inactivity gap.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 24: Date Spine

```text
Return daily revenue including zero-revenue dates.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 25: EXISTS

```text
Return customers with at least one successful order.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 26: UNION ALL

```text
Combine web and mobile events while preserving duplicates.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 27: Performance

```text
Optimize slow January revenue query conceptually.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 28: File Audit

```text
Find expected files not loaded.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 29: Incremental Validation

```text
Find source updated records missing in target.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 30: Freshness

```text
Check whether fact table loaded within last 2 hours.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 31: Late Data

```text
Find events ingested more than 24 hours after event_time.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 32: Fact to SCD2 Join

```text
Join orders to dimension version active at order_date.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.

### Drill 33: Mixed Mock

```text
Solve LEFT JOIN, window, reconciliation, and quality SQL in one session.
```

Minimum passing answer:

- State output grain.
- Explain base table and join type.
- Write correct SQL.
- Handle dates/nulls/duplicates where relevant.
- Explain validation.
- Mention performance if relevant.
