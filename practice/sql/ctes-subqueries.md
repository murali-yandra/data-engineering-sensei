# CTEs and Subqueries Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/sql/ctes-subqueries.md
```

This guide teaches and drills **CTEs and subqueries for Data Engineering interviews**.

This is not a generic SQL syntax note. It is an interview-focused guide for candidates who need to structure SQL clearly, break complex business logic into steps, avoid duplicated logic, use subqueries correctly, solve ranking/filtering/aggregation problems, and explain when a CTE, derived table, scalar subquery, correlated subquery, EXISTS, or window function is the right choice.

CTEs and subqueries are high-ROI because Data Engineering interviews often ask you to:

- simplify complex SQL
- build multi-step transformations
- filter aggregated results
- deduplicate records
- find first/latest rows
- calculate business metrics in stages
- avoid repeated expressions
- compare against aggregate values
- perform anti-joins with NOT EXISTS
- perform semi-joins with EXISTS
- build recursive hierarchy queries
- create readable SQL pipelines
- debug query grain issues
- prevent double counting
- validate intermediate results
- translate SQL logic to data pipeline steps

Use this guide with:

- `docs/sql-interview-guide.md`
- `docs/data-engineering-fundamentals.md`
- `docs/data-warehouse-guide.md`
- `docs/data-modeling-guide.md`
- `docs/faang-interview-standards.md`
- `docs/assessment-rubric.md`
- `docs/communication-rubric.md`
- `modes/sql-drill-mode.md`
- `modes/interview-mode.md`
- `modes/review-mode.md`
- `modes/feedback-mode.md`
- `modes/weakness-repair-mode.md`
- `practice/sql/business-sql-cases.md`
- `practice/python/pandas-basics.md`
- `progress/CANDIDATE_PROFILE.md`
- `progress/CURRENT_STATE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Default interview standard if target companies are not provided:

```text
FAANG-style Data Engineering interview standard, scaled by candidate experience.
```


## 1. Purpose

The purpose of this guide is to make the candidate strong at using CTEs and subqueries in interview SQL.

The candidate should learn to answer:

```text
What is a CTE?
What is a subquery?
When should I use a CTE instead of a subquery?
When should I use a derived table?
When should I use EXISTS?
When should I use IN?
When should I avoid NOT IN?
When should I use a correlated subquery?
When should I replace a correlated subquery with a join or window function?
How do I filter on aggregated values?
How do I filter on window function results?
How do I structure multi-step business logic?
How do I build readable SQL transformations?
How do I validate intermediate query stages?
How do recursive CTEs work?
How can CTEs help with Data Engineering pipelines?
```

A candidate is interview-ready only when they can:

```text
write clean CTE-based SQL
name CTEs by purpose and grain
use subqueries in SELECT, FROM, WHERE, and HAVING
use EXISTS for semi-joins
use NOT EXISTS for anti-joins
avoid NOT IN NULL traps
use derived tables for inline aggregation
filter window results using CTEs
deduplicate using ROW_NUMBER in a CTE
calculate metrics in stages
debug double-counting by checking intermediate CTE grains
explain performance trade-offs
explain CTE materialization behavior at a high level
use recursive CTEs for hierarchy or date expansion when needed
```


## 2. Why CTEs and Subqueries Matter for Data Engineers

Data Engineering SQL often becomes complex because raw data needs several steps before it becomes a reliable metric or table.

Common production patterns:

```text
filter raw events
deduplicate events
normalize statuses
aggregate to daily grain
join dimensions
calculate ratios
compare source and target
detect missing records
build latest snapshots
create incremental transforms
validate data quality
```

CTEs and subqueries help because they let you:

```text
break the logic into readable steps
name each transformation stage
avoid repeating complex filters
validate each step independently
make business logic easier to explain
reduce mistakes around grain and joins
```

Weak answer:

```text
Write one huge nested query that works only by luck.
```

Strong answer:

```text
Break the logic into CTEs such as base_orders, completed_orders, customer_revenue, ranked_customers, and final_output, with each CTE having a clear grain.
```

Interview line:

```text
CTEs are not only syntax. They are a way to make complex SQL explainable, testable, and safer.
```


## 3. Core Mental Model

Think of a SQL query as a pipeline.

```text
Raw data
  -> filter
  -> clean
  -> deduplicate
  -> aggregate
  -> join
  -> rank
  -> calculate final metrics
  -> validate output
```

CTEs let you name each stage.

Example:

```sql
WITH base_orders AS (
  SELECT *
  FROM orders
  WHERE order_time >= DATE '2026-01-01'
    AND order_time <  DATE '2026-02-01'
),
completed_orders AS (
  SELECT *
  FROM base_orders
  WHERE order_status = 'COMPLETED'
),
customer_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue
  FROM completed_orders
  GROUP BY user_id
)
SELECT *
FROM customer_revenue;
```

Core interview line:

```text
Every CTE should have a clear purpose and grain. If I cannot explain the grain of a CTE, the query is not safe enough.
```


## 4. Vocabulary

Important terms:

```text
CTE:
Common Table Expression. A named temporary result set defined with WITH.

Subquery:
A query nested inside another query.

Derived table:
A subquery in the FROM clause that behaves like a temporary table.

Scalar subquery:
A subquery that returns one value.

Correlated subquery:
A subquery that references columns from the outer query.

EXISTS:
Checks whether a subquery returns at least one row.

IN:
Checks whether a value is in a set returned by a subquery.

NOT EXISTS:
Anti-join style check for missing related rows.

NOT IN:
Can be dangerous when subquery returns NULL.

Recursive CTE:
A CTE that references itself, useful for hierarchies or sequence generation.

Materialization:
Whether the database physically stores a CTE result before continuing. Behavior depends on database.

Grain:
What one row in a result represents.

Semi-join:
Return rows from left side that have at least one match on right side.

Anti-join:
Return rows from left side that do not have a match on right side.
```


## 5. Standard Answer Framework

Use this framework for CTE/subquery interview problems:

```text
1. Restate the business problem.
2. Identify the final output grain.
3. Identify each intermediate grain.
4. Decide if logic needs multiple steps.
5. Use CTEs for named multi-step logic.
6. Use derived tables for small inline aggregation.
7. Use EXISTS/NOT EXISTS for existence checks.
8. Use scalar subqueries only when one value is expected.
9. Avoid NOT IN if NULLs are possible.
10. Use CTEs to filter window function results.
11. Validate intermediate row counts.
12. Explain performance and readability trade-offs.
```

Short version:

```text
Purpose:
Grain:
CTE stages:
Subquery type:
NULL behavior:
Validation:
Performance:
```

Strict rule:

```text
No CTE/subquery answer is strong if the candidate cannot explain why they chose CTE, EXISTS, IN, JOIN, or window function.
```


## 6. Scoring Rubric

Score each CTE/subquery answer from 0 to 5.

### Score 0

No meaningful SQL structure.

### Score 1

Uses nested query or CTE randomly without understanding.

### Score 2

Works for simple cases but unclear grain, aliases, or NULL handling.

### Score 3

Mostly correct but weak on readability, validation, or performance trade-offs.

### Score 4

Interview-ready. Clear CTE names, correct subquery use, correct NULL handling, and explainable logic.

### Score 5

Strong. Handles complex business logic, EXISTS/NOT EXISTS, anti-joins, window filtering, recursive CTE basics, performance implications, and Data Engineering pipeline reasoning.

Do not give 4+ if:

```text
candidate uses NOT IN without considering NULLs
candidate cannot explain correlated subquery
candidate filters window function in WHERE incorrectly
candidate writes unreadable nested SQL
candidate does not alias derived tables
candidate creates CTEs with unclear names
candidate cannot explain intermediate grain
candidate uses scalar subquery that can return multiple rows
candidate ignores join cardinality
candidate cannot explain performance trade-offs
candidate repeats the same subquery unnecessarily
```


## 7. CTE Syntax

Basic CTE syntax:

```sql
WITH cte_name AS (
  SELECT ...
  FROM ...
)
SELECT *
FROM cte_name;
```

Multiple CTEs:

```sql
WITH base_orders AS (
  SELECT *
  FROM orders
),
completed_orders AS (
  SELECT *
  FROM base_orders
  WHERE order_status = 'COMPLETED'
)
SELECT *
FROM completed_orders;
```

Important rules:

```text
CTE exists only for the statement that follows it.
CTE names should describe the stage.
CTEs can reference earlier CTEs.
Most databases require commas between CTE definitions.
```

Interview line:

```text
I use CTEs to split complex logic into named steps that are easier to test and explain.
```


## 8. Subquery Syntax Overview

Subqueries can appear in several places.

### Subquery in WHERE

```sql
SELECT *
FROM users
WHERE user_id IN (
  SELECT user_id
  FROM orders
);
```

### Subquery in FROM

```sql
SELECT
  customer_id,
  revenue
FROM (
  SELECT
    customer_id,
    SUM(amount) AS revenue
  FROM payments
  GROUP BY customer_id
) customer_revenue;
```

### Scalar subquery in SELECT

```sql
SELECT
  user_id,
  total_amount,
  (SELECT AVG(total_amount) FROM orders) AS avg_order_amount
FROM orders;
```

### EXISTS subquery

```sql
SELECT *
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
);
```

Interview line:

```text
The type of subquery depends on whether I need a value, a set, an inline table, or an existence check.
```


## 9. CTE vs Subquery Decision Table

| Need | Usually Prefer |
|---|---|
| Multi-step transformation | CTE |
| Improve readability | CTE |
| Reuse intermediate result in same query | CTE |
| Filter window function result | CTE or derived table |
| Small inline aggregation | Derived table |
| Single aggregate value comparison | Scalar subquery |
| Check if related rows exist | EXISTS |
| Check if related rows do not exist | NOT EXISTS |
| Generate hierarchy | Recursive CTE |
| One-time simple filter | Subquery can be fine |
| Complex business metric | CTEs |

Interview line:

```text
I prefer CTEs for readable multi-step business logic and EXISTS/NOT EXISTS for existence checks.
```


## 10. Naming CTEs

Good CTE names describe purpose and grain.

Good:

```text
base_events
valid_orders
deduped_payments
daily_revenue
customer_totals
ranked_customers
final_metric
```

Bad:

```text
a
b
c
temp
query1
cte2
```

Recommended naming pattern:

```text
base_<table/entity>
valid_<entity>
deduped_<entity>
<grain>_<metric>
ranked_<entity>
final_<result>
```

Example:

```sql
WITH base_orders AS (...),
completed_orders AS (...),
customer_revenue AS (...),
ranked_customers AS (...)
SELECT ...
```

Interview line:

```text
Good CTE names make the query read like a data pipeline.
```


## 11. CTE Grain Discipline

Every CTE should have a known grain.

Example:

```sql
WITH daily_user_activity AS (
  SELECT DISTINCT
    user_id,
    CAST(event_time AS DATE) AS activity_date
  FROM events
)
```

Grain:

```text
one row per user per activity_date
```

Another example:

```sql
WITH customer_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue
  FROM orders
  GROUP BY user_id
)
```

Grain:

```text
one row per user
```

Bad:

```text
CTE has unclear duplicates and mixed grain.
```

Interview line:

```text
I state the grain of each CTE to prevent double counting later.
```


## 12. Example: Multi-Step Revenue Query

Problem:

```text
Find top 10 customers by completed order revenue in January 2026.
```

CTE solution:

```sql
WITH base_orders AS (
  SELECT
    order_id,
    user_id,
    total_amount,
    order_time,
    order_status
  FROM orders
  WHERE order_time >= DATE '2026-01-01'
    AND order_time <  DATE '2026-02-01'
),
completed_orders AS (
  SELECT
    order_id,
    user_id,
    total_amount
  FROM base_orders
  WHERE order_status = 'COMPLETED'
    AND user_id IS NOT NULL
),
customer_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue,
    COUNT(DISTINCT order_id) AS completed_orders
  FROM completed_orders
  GROUP BY user_id
),
ranked_customers AS (
  SELECT
    user_id,
    revenue,
    completed_orders,
    ROW_NUMBER() OVER (
      ORDER BY revenue DESC, user_id
    ) AS rn
  FROM customer_revenue
)
SELECT
  user_id,
  revenue,
  completed_orders
FROM ranked_customers
WHERE rn <= 10
ORDER BY rn;
```

Why CTEs help:

```text
Each stage is clear:
base filter
completed order filter
customer aggregation
ranking
final output
```

Interview line:

```text
For top-N business metrics, CTEs help separate filtering, aggregation, ranking, and final selection.
```


## 13. Derived Tables

A derived table is a subquery in the FROM clause.

Example:

```sql
SELECT
  customer_id,
  revenue
FROM (
  SELECT
    customer_id,
    SUM(amount) AS revenue
  FROM payments
  WHERE payment_status = 'SUCCESS'
  GROUP BY customer_id
) revenue_by_customer
WHERE revenue > 1000;
```

Important:

```text
Always alias derived tables.
```

Equivalent CTE:

```sql
WITH revenue_by_customer AS (
  SELECT
    customer_id,
    SUM(amount) AS revenue
  FROM payments
  WHERE payment_status = 'SUCCESS'
  GROUP BY customer_id
)
SELECT
  customer_id,
  revenue
FROM revenue_by_customer
WHERE revenue > 1000;
```

When derived table is okay:

```text
small one-time inline aggregation
simple query
interviewer asks for compact SQL
```

When CTE is better:

```text
multi-step logic
complex business metric
reuse
readability
debugging
```

Interview line:

```text
A derived table is fine for small inline logic, but I switch to CTEs when the query becomes multi-step.
```


## 14. Scalar Subqueries

A scalar subquery returns one value.

Example:

```sql
SELECT
  order_id,
  total_amount,
  (SELECT AVG(total_amount) FROM orders) AS avg_order_amount
FROM orders;
```

Compare each order to global average:

```sql
SELECT
  order_id,
  total_amount
FROM orders
WHERE total_amount > (
  SELECT AVG(total_amount)
  FROM orders
);
```

Danger:

```text
If scalar subquery returns more than one row, the query fails.
```

Bad:

```sql
SELECT *
FROM orders
WHERE total_amount > (
  SELECT total_amount
  FROM orders
);
```

Why bad:

```text
The subquery returns many values, not one scalar value.
```

Interview line:

```text
I use scalar subqueries only when I can guarantee one value, such as a single aggregate.
```


## 15. IN Subqueries

IN checks whether a value appears in a subquery result.

Example:

```sql
SELECT *
FROM users
WHERE user_id IN (
  SELECT user_id
  FROM orders
  WHERE order_status = 'COMPLETED'
);
```

Meaning:

```text
Return users who have completed at least one order.
```

Equivalent EXISTS:

```sql
SELECT *
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
    AND o.order_status = 'COMPLETED'
);
```

When IN is okay:

```text
simple membership check
subquery returns one column
NULL behavior is not risky for positive IN
```

Interview line:

```text
IN is readable for simple membership, but EXISTS is often safer and more explicit for related-row checks.
```


## 16. EXISTS Subqueries

EXISTS checks whether the subquery returns at least one row.

Example:

```sql
SELECT
  u.user_id,
  u.signup_at
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
    AND o.order_status = 'COMPLETED'
);
```

Why SELECT 1:

```text
The actual selected value does not matter. EXISTS only checks row existence.
```

Use EXISTS when:

```text
you only care whether a match exists
you want to avoid row multiplication
you are doing semi-join logic
the right side can have many matching rows
```

Interview line:

```text
EXISTS is useful when I need to know whether a related record exists without joining and multiplying rows.
```


## 17. NOT EXISTS Anti-Join

NOT EXISTS finds rows with no matching related rows.

Problem:

```text
Find users who never placed a completed order.
```

SQL:

```sql
SELECT
  u.user_id,
  u.signup_at
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
    AND o.order_status = 'COMPLETED'
);
```

Equivalent anti-join:

```sql
SELECT
  u.user_id,
  u.signup_at
FROM users u
LEFT JOIN orders o
  ON u.user_id = o.user_id
 AND o.order_status = 'COMPLETED'
WHERE o.user_id IS NULL;
```

Interview line:

```text
NOT EXISTS is my preferred anti-join pattern when I need records with no related matches.
```


## 18. NOT IN NULL Trap

NOT IN can behave unexpectedly when the subquery returns NULL.

Problem example:

```sql
SELECT user_id
FROM users
WHERE user_id NOT IN (
  SELECT user_id
  FROM orders
);
```

If `orders.user_id` contains NULL, this can return no rows in many SQL dialects.

Safer version:

```sql
SELECT user_id
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
);
```

Or filter NULLs:

```sql
SELECT user_id
FROM users
WHERE user_id NOT IN (
  SELECT user_id
  FROM orders
  WHERE user_id IS NOT NULL
);
```

Interview line:

```text
I avoid NOT IN when NULLs are possible and prefer NOT EXISTS for anti-joins.
```


## 19. Correlated Subqueries

A correlated subquery references columns from the outer query.

Example:

```sql
SELECT
  u.user_id,
  u.signup_at
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
);
```

Here:

```text
o.user_id = u.user_id references the outer query's user_id.
```

Another example:

```sql
SELECT
  o.order_id,
  o.user_id,
  o.total_amount
FROM orders o
WHERE o.total_amount > (
  SELECT AVG(o2.total_amount)
  FROM orders o2
  WHERE o2.user_id = o.user_id
);
```

Meaning:

```text
Orders greater than that user's average order amount.
```

Caution:

```text
Correlated subqueries can be expensive if executed row by row, depending on optimizer.
Often a join/window function can be clearer or faster.
```

Interview line:

```text
Correlated subqueries are useful for row-specific comparisons, but I consider joins or window functions for performance and readability.
```


## 20. Rewriting Correlated Subquery as Join

Correlated subquery:

```sql
SELECT
  o.order_id,
  o.user_id,
  o.total_amount
FROM orders o
WHERE o.total_amount > (
  SELECT AVG(o2.total_amount)
  FROM orders o2
  WHERE o2.user_id = o.user_id
);
```

Join rewrite:

```sql
WITH user_avg_order AS (
  SELECT
    user_id,
    AVG(total_amount) AS avg_order_amount
  FROM orders
  GROUP BY user_id
)
SELECT
  o.order_id,
  o.user_id,
  o.total_amount,
  a.avg_order_amount
FROM orders o
JOIN user_avg_order a
  ON o.user_id = a.user_id
WHERE o.total_amount > a.avg_order_amount;
```

Window rewrite:

```sql
WITH orders_with_avg AS (
  SELECT
    order_id,
    user_id,
    total_amount,
    AVG(total_amount) OVER (
      PARTITION BY user_id
    ) AS avg_order_amount
  FROM orders
)
SELECT
  order_id,
  user_id,
  total_amount,
  avg_order_amount
FROM orders_with_avg
WHERE total_amount > avg_order_amount;
```

Interview line:

```text
If the comparison is against a group-level aggregate, a CTE join or window function is often clearer than a correlated subquery.
```


## 21. Filtering Aggregated Results

Problem:

```text
Find customers with more than 5 completed orders.
```

Using HAVING:

```sql
SELECT
  user_id,
  COUNT(DISTINCT order_id) AS completed_orders
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY user_id
HAVING COUNT(DISTINCT order_id) > 5;
```

Using CTE:

```sql
WITH customer_orders AS (
  SELECT
    user_id,
    COUNT(DISTINCT order_id) AS completed_orders
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
)
SELECT *
FROM customer_orders
WHERE completed_orders > 5;
```

When CTE is better:

```text
computed aggregate reused
more columns/calculations needed
query readability
next stage needs the aggregate
```

Interview line:

```text
HAVING filters groups directly; a CTE is clearer when the aggregate becomes an intermediate dataset.
```


## 22. Filtering Window Function Results

Window functions are usually not allowed directly in WHERE.

Bad:

```sql
SELECT
  user_id,
  order_id,
  ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY order_time DESC
  ) AS rn
FROM orders
WHERE rn = 1;
```

Why bad:

```text
WHERE is evaluated before SELECT alias rn is available.
```

Correct with CTE:

```sql
WITH ranked_orders AS (
  SELECT
    user_id,
    order_id,
    order_time,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time DESC, order_id DESC
    ) AS rn
  FROM orders
)
SELECT
  user_id,
  order_id,
  order_time
FROM ranked_orders
WHERE rn = 1;
```

Some dialects support QUALIFY:

```sql
SELECT
  user_id,
  order_id,
  order_time
FROM orders
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY order_time DESC, order_id DESC
) = 1;
```

Interview line:

```text
When a dialect does not support QUALIFY, I use a CTE to filter window function results.
```


## 23. CTE for Deduplication

Problem:

```text
Deduplicate events by event_id, keeping latest ingested_at.
```

SQL:

```sql
WITH ranked_events AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY event_id
      ORDER BY ingested_at DESC
    ) AS rn
  FROM events
)
SELECT *
FROM ranked_events
WHERE rn = 1;
```

Tie-breaker:

```sql
ORDER BY ingested_at DESC, event_time DESC
```

Better if event_id can be NULL:

```sql
WITH ranked_events AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY event_id
      ORDER BY ingested_at DESC
    ) AS rn
  FROM events
  WHERE event_id IS NOT NULL
)
SELECT *
FROM ranked_events
WHERE rn = 1;
```

Interview line:

```text
Deduplication requires a business key and a deterministic keep rule.
```


## 24. CTE for Latest Snapshot

Problem:

```text
Get latest user profile row per user.
```

SQL:

```sql
WITH ranked_profiles AS (
  SELECT
    user_id,
    country,
    plan,
    updated_at,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY updated_at DESC
    ) AS rn
  FROM user_profiles
)
SELECT
  user_id,
  country,
  plan,
  updated_at
FROM ranked_profiles
WHERE rn = 1;
```

If ties are possible:

```sql
ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY updated_at DESC, profile_version DESC
) AS rn
```

Interview line:

```text
Latest snapshot queries should always include a deterministic tie-breaker when possible.
```


## 25. CTE for First Purchase

Problem:

```text
Find first completed purchase per user.
```

SQL:

```sql
WITH ranked_orders AS (
  SELECT
    user_id,
    order_id,
    order_time,
    total_amount,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time, order_id
    ) AS rn
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT
  user_id,
  order_id AS first_order_id,
  order_time AS first_order_time,
  total_amount AS first_order_amount
FROM ranked_orders
WHERE rn = 1;
```

Why not only MIN(order_time):

```text
MIN(order_time) does not return associated order_id and amount safely.
```

Interview line:

```text
Use ROW_NUMBER when the answer needs columns from the first or latest row.
```


## 26. CTE for Business Metric Stages

Problem:

```text
Calculate repeat purchase rate by signup month.
```

SQL:

```sql
WITH signup_users AS (
  SELECT
    user_id,
    DATE_TRUNC('month', signup_at) AS signup_month
  FROM users
),
completed_orders AS (
  SELECT DISTINCT
    order_id,
    user_id
  FROM orders
  WHERE order_status = 'COMPLETED'
),
orders_per_user AS (
  SELECT
    s.signup_month,
    s.user_id,
    COUNT(o.order_id) AS completed_orders
  FROM signup_users s
  LEFT JOIN completed_orders o
    ON s.user_id = o.user_id
  GROUP BY
    s.signup_month,
    s.user_id
),
monthly_repeat AS (
  SELECT
    signup_month,
    COUNT(*) AS signup_users,
    SUM(CASE WHEN completed_orders >= 2 THEN 1 ELSE 0 END) AS repeat_users
  FROM orders_per_user
  GROUP BY signup_month
)
SELECT
  signup_month,
  signup_users,
  repeat_users,
  repeat_users * 1.0 / NULLIF(signup_users, 0) AS repeat_purchase_rate
FROM monthly_repeat
ORDER BY signup_month;
```

CTE grains:

```text
signup_users: one row per user
completed_orders: one row per completed order
orders_per_user: one row per signup month/user
monthly_repeat: one row per signup month
```

Interview line:

```text
For metric queries, I state the grain of each CTE so denominator mistakes are easier to catch.
```


## 27. CTE for Source-Target Reconciliation

Problem:

```text
Compare source and warehouse transactions.
```

SQL:

```sql
WITH source_base AS (
  SELECT
    transaction_id,
    amount
  FROM source_transactions
),
warehouse_base AS (
  SELECT
    transaction_id,
    amount
  FROM warehouse_transactions
),
reconciled AS (
  SELECT
    COALESCE(s.transaction_id, w.transaction_id) AS transaction_id,
    s.amount AS source_amount,
    w.amount AS warehouse_amount,
    CASE
      WHEN s.transaction_id IS NOT NULL AND w.transaction_id IS NULL THEN 'ONLY_IN_SOURCE'
      WHEN s.transaction_id IS NULL AND w.transaction_id IS NOT NULL THEN 'ONLY_IN_WAREHOUSE'
      WHEN s.amount <> w.amount THEN 'AMOUNT_MISMATCH'
      ELSE 'MATCH'
    END AS reconciliation_status
  FROM source_base s
  FULL OUTER JOIN warehouse_base w
    ON s.transaction_id = w.transaction_id
)
SELECT *
FROM reconciled
WHERE reconciliation_status <> 'MATCH'
ORDER BY reconciliation_status, transaction_id;
```

Interview line:

```text
CTEs make reconciliation queries clearer by separating source shaping, target shaping, and comparison.
```


## 28. CTE for Avoiding Double Counting

Problem:

```text
Calculate average order value when order_items is item-grain.
```

Bad:

```sql
SELECT
  AVG(o.total_amount) AS avg_order_value
FROM orders o
JOIN order_items oi
  ON o.order_id = oi.order_id
WHERE o.order_status = 'COMPLETED';
```

Why bad:

```text
Orders with more items appear multiple times.
```

Correct CTE:

```sql
WITH completed_orders AS (
  SELECT DISTINCT
    order_id,
    total_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT
  SUM(total_amount) * 1.0 / NULLIF(COUNT(*), 0) AS avg_order_value
FROM completed_orders;
```

If total must be built from items:

```sql
WITH order_totals AS (
  SELECT
    o.order_id,
    SUM(oi.quantity * oi.unit_price) AS order_amount
  FROM orders o
  JOIN order_items oi
    ON o.order_id = oi.order_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY o.order_id
)
SELECT
  AVG(order_amount) AS avg_order_value
FROM order_totals;
```

Interview line:

```text
When joining one-to-many tables, I often use CTEs to collapse to the metric grain before calculating rates or averages.
```


## 29. CTE for Funnel Analysis

Problem:

```text
Calculate user-level funnel conversion from view to cart to purchase.
```

SQL:

```sql
WITH base_events AS (
  SELECT
    user_id,
    event_name,
    event_time
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2026-02-01'
    AND event_name IN ('product_view', 'add_to_cart', 'purchase')
    AND user_id IS NOT NULL
),
user_steps AS (
  SELECT
    user_id,
    MIN(CASE WHEN event_name = 'product_view' THEN event_time END) AS view_time,
    MIN(CASE WHEN event_name = 'add_to_cart' THEN event_time END) AS cart_time,
    MIN(CASE WHEN event_name = 'purchase' THEN event_time END) AS purchase_time
  FROM base_events
  GROUP BY user_id
),
valid_steps AS (
  SELECT
    user_id,
    view_time,
    CASE
      WHEN cart_time >= view_time THEN cart_time
    END AS valid_cart_time,
    CASE
      WHEN purchase_time >= cart_time
       AND cart_time >= view_time THEN purchase_time
    END AS valid_purchase_time
  FROM user_steps
)
SELECT
  COUNT(*) AS viewed_users,
  SUM(CASE WHEN valid_cart_time IS NOT NULL THEN 1 ELSE 0 END) AS cart_users,
  SUM(CASE WHEN valid_purchase_time IS NOT NULL THEN 1 ELSE 0 END) AS purchase_users
FROM valid_steps
WHERE view_time IS NOT NULL;
```

Interview line:

```text
Funnel CTEs should separate event filtering, step extraction, ordering validation, and final conversion calculation.
```


## 30. CTE for Retention

Problem:

```text
Calculate day-1 retention by signup date.
```

SQL:

```sql
WITH signup_cohort AS (
  SELECT
    user_id,
    CAST(signup_at AS DATE) AS signup_date
  FROM users
),
activity_days AS (
  SELECT DISTINCT
    user_id,
    CAST(event_time AS DATE) AS activity_date
  FROM events
),
retained_day1 AS (
  SELECT
    s.user_id,
    s.signup_date
  FROM signup_cohort s
  JOIN activity_days a
    ON s.user_id = a.user_id
   AND a.activity_date = s.signup_date + INTERVAL '1 day'
)
SELECT
  s.signup_date,
  COUNT(DISTINCT s.user_id) AS cohort_users,
  COUNT(DISTINCT r.user_id) AS retained_users,
  COUNT(DISTINCT r.user_id) * 1.0 / NULLIF(COUNT(DISTINCT s.user_id), 0) AS day1_retention
FROM signup_cohort s
LEFT JOIN retained_day1 r
  ON s.user_id = r.user_id
 AND s.signup_date = r.signup_date
GROUP BY s.signup_date
ORDER BY s.signup_date;
```

Interview line:

```text
Retention CTEs should preserve the cohort denominator and left join retained users to it.
```


## 31. Nested CTEs vs Many CTEs

Use enough CTEs to clarify logic, but not so many that simple logic becomes noisy.

Too compact:

```sql
SELECT ...
FROM (
  SELECT ...
  FROM (
    SELECT ...
  ) a
) b;
```

Usually better:

```sql
WITH base AS (...),
filtered AS (...),
aggregated AS (...),
final AS (...)
SELECT *
FROM final;
```

Too many unnecessary CTEs:

```text
one CTE only to rename one column
one CTE only to select all rows with no transformation
one CTE per trivial expression
```

Good balance:

```text
one CTE per meaningful transformation stage
```

Interview line:

```text
I use CTEs for meaningful stages, not for every tiny expression.
```


## 32. Reusing CTEs

Some databases allow referencing a CTE multiple times.

Example:

```sql
WITH monthly_revenue AS (
  SELECT
    DATE_TRUNC('month', order_time) AS month,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY DATE_TRUNC('month', order_time)
)
SELECT
  current.month,
  current.revenue,
  previous.revenue AS previous_revenue
FROM monthly_revenue current
LEFT JOIN monthly_revenue previous
  ON current.month = previous.month + INTERVAL '1 month';
```

Caution:

```text
Depending on database optimizer, referencing a CTE multiple times can be optimized or materialized differently.
```

Interview line:

```text
CTE reuse improves readability, but I consider database-specific optimization behavior for large datasets.
```


## 33. CTE Materialization and Performance

CTE performance behavior depends on database.

Important points:

```text
Some optimizers inline CTEs.
Some may materialize CTEs.
Some allow hints to force materialization or not.
CTEs are not automatically indexed temporary tables.
A CTE does not always improve performance.
A CTE often improves readability.
```

General guidance:

```text
Filter early.
Select needed columns only.
Aggregate before large joins when appropriate.
Avoid unnecessary repeated CTE scans.
Check execution plan for production performance.
Use temp tables/materialized tables for heavy reused intermediate results when needed.
```

Interview-safe statement:

```text
I use CTEs primarily for readability and correctness. For performance, I check the execution plan because materialization behavior differs by database.
```


## 34. Subquery Performance Principles

Subquery performance depends on optimizer and data size.

General principles:

```text
EXISTS can stop after finding first match.
IN can be fine for small/simple sets.
Correlated subqueries can be expensive if not optimized.
Repeated scalar subqueries may be inefficient.
Joins and windows often express group comparisons more clearly.
NOT EXISTS avoids NULL traps from NOT IN.
```

Example better as join/window:

```text
orders greater than user average order
```

Poor approach if repeated per row:

```sql
WHERE total_amount > (
  SELECT AVG(total_amount)
  FROM orders o2
  WHERE o2.user_id = o.user_id
)
```

Often clearer:

```sql
AVG(total_amount) OVER (PARTITION BY user_id)
```

Interview line:

```text
I choose the clearest correct pattern first, then consider performance with execution plan and data volume.
```


## 35. Recursive CTE Basics

Recursive CTEs allow a query to reference itself.

Common use cases:

```text
organization hierarchy
category tree
bill of materials
date sequence generation
graph traversal with limits
```

Generic structure:

```sql
WITH RECURSIVE hierarchy AS (
  -- anchor query
  SELECT
    employee_id,
    manager_id,
    employee_name,
    1 AS level
  FROM employees
  WHERE manager_id IS NULL

  UNION ALL

  -- recursive query
  SELECT
    e.employee_id,
    e.manager_id,
    e.employee_name,
    h.level + 1 AS level
  FROM employees e
  JOIN hierarchy h
    ON e.manager_id = h.employee_id
)
SELECT *
FROM hierarchy;
```

Important:

```text
Anchor produces starting rows.
Recursive part adds next level.
Must eventually stop.
Use safeguards against cycles.
```

Interview line:

```text
Recursive CTEs are useful for hierarchical data, but I mention cycle protection and depth limits.
```


## 36. Recursive CTE for Date Series

Some databases can generate dates using recursive CTEs.

Example:

```sql
WITH RECURSIVE dates AS (
  SELECT DATE '2026-01-01' AS calendar_date

  UNION ALL

  SELECT calendar_date + INTERVAL '1 day'
  FROM dates
  WHERE calendar_date < DATE '2026-01-31'
)
SELECT *
FROM dates;
```

Use case:

```text
fill missing dates for rolling metrics
find missing partitions
build calendar-like output
```

Caution:

```text
In production, a permanent calendar dimension is usually better.
Dialect syntax and recursion limits vary.
```

Interview line:

```text
Recursive CTEs can generate small date ranges, but production warehouses usually use a calendar dimension.
```


## 37. Subquery in SELECT for Percent of Total

Problem:

```text
Show category revenue and percentage of total revenue.
```

Scalar subquery version:

```sql
SELECT
  p.category,
  SUM(oi.quantity * oi.unit_price) AS category_revenue,
  SUM(oi.quantity * oi.unit_price) * 1.0
    / NULLIF((
      SELECT SUM(oi2.quantity * oi2.unit_price)
      FROM order_items oi2
      JOIN orders o2
        ON oi2.order_id = o2.order_id
      WHERE o2.order_status = 'COMPLETED'
    ), 0) AS revenue_share
FROM order_items oi
JOIN orders o
  ON oi.order_id = o.order_id
JOIN products p
  ON oi.product_id = p.product_id
WHERE o.order_status = 'COMPLETED'
GROUP BY p.category;
```

CTE/window version:

```sql
WITH category_revenue AS (
  SELECT
    p.category,
    SUM(oi.quantity * oi.unit_price) AS revenue
  FROM order_items oi
  JOIN orders o
    ON oi.order_id = o.order_id
  JOIN products p
    ON oi.product_id = p.product_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY p.category
)
SELECT
  category,
  revenue,
  revenue * 1.0 / NULLIF(SUM(revenue) OVER (), 0) AS revenue_share
FROM category_revenue;
```

Interview line:

```text
For percent-of-total, a CTE plus window SUM is often cleaner than repeating a scalar subquery.
```


## 38. Subquery in HAVING

Problem:

```text
Find customers whose revenue is above average customer revenue.
```

SQL:

```sql
WITH customer_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
)
SELECT
  user_id,
  revenue
FROM customer_revenue
WHERE revenue > (
  SELECT AVG(revenue)
  FROM customer_revenue
);
```

Alternative:

```sql
WITH customer_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
),
with_avg AS (
  SELECT
    user_id,
    revenue,
    AVG(revenue) OVER () AS avg_customer_revenue
  FROM customer_revenue
)
SELECT
  user_id,
  revenue,
  avg_customer_revenue
FROM with_avg
WHERE revenue > avg_customer_revenue;
```

Interview line:

```text
When comparing against an aggregate of aggregates, I first build the lower-grain aggregate as a CTE.
```


## 39. EXISTS vs JOIN

Problem:

```text
Find users with at least one completed order.
```

JOIN version:

```sql
SELECT DISTINCT
  u.user_id
FROM users u
JOIN orders o
  ON u.user_id = o.user_id
WHERE o.order_status = 'COMPLETED';
```

EXISTS version:

```sql
SELECT
  u.user_id
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
    AND o.order_status = 'COMPLETED'
);
```

Difference:

```text
JOIN creates matched rows and may require DISTINCT.
EXISTS only checks existence and avoids row multiplication.
```

Interview line:

```text
If I only need existence, EXISTS can be clearer than JOIN plus DISTINCT.
```


## 40. NOT EXISTS vs LEFT JOIN Anti-Join

Problem:

```text
Find products never sold.
```

NOT EXISTS:

```sql
SELECT
  p.product_id
FROM products p
WHERE NOT EXISTS (
  SELECT 1
  FROM order_items oi
  JOIN orders o
    ON oi.order_id = o.order_id
  WHERE oi.product_id = p.product_id
    AND o.order_status = 'COMPLETED'
);
```

LEFT JOIN:

```sql
WITH sold_products AS (
  SELECT DISTINCT
    oi.product_id
  FROM order_items oi
  JOIN orders o
    ON oi.order_id = o.order_id
  WHERE o.order_status = 'COMPLETED'
)
SELECT
  p.product_id
FROM products p
LEFT JOIN sold_products s
  ON p.product_id = s.product_id
WHERE s.product_id IS NULL;
```

When CTE version is clearer:

```text
when sold_products logic is complex
when sold_products is reused
when you want to inspect sold product set
```

Interview line:

```text
Both patterns are valid, but NOT EXISTS avoids NULL traps and expresses anti-existence clearly.
```


## 41. CTE for Data Quality Checks

Problem:

```text
Create order data quality summary.
```

SQL:

```sql
WITH base_orders AS (
  SELECT *
  FROM orders
),
quality_flags AS (
  SELECT
    order_id,
    CASE WHEN user_id IS NULL THEN 1 ELSE 0 END AS missing_user_id,
    CASE WHEN order_time IS NULL THEN 1 ELSE 0 END AS missing_order_time,
    CASE WHEN total_amount IS NULL THEN 1 ELSE 0 END AS missing_total_amount,
    CASE WHEN total_amount < 0 THEN 1 ELSE 0 END AS negative_total_amount
  FROM base_orders
)
SELECT
  COUNT(*) AS total_rows,
  SUM(missing_user_id) AS missing_user_id_rows,
  SUM(missing_order_time) AS missing_order_time_rows,
  SUM(missing_total_amount) AS missing_total_amount_rows,
  SUM(negative_total_amount) AS negative_total_amount_rows
FROM quality_flags;
```

Interview line:

```text
CTEs help separate data quality flags from final quality summary.
```


## 42. CTE for Orphan Records

Problem:

```text
Find order records whose user_id does not exist in users.
```

SQL:

```sql
WITH order_users AS (
  SELECT DISTINCT
    order_id,
    user_id
  FROM orders
  WHERE user_id IS NOT NULL
),
orphan_orders AS (
  SELECT
    o.order_id,
    o.user_id
  FROM order_users o
  WHERE NOT EXISTS (
    SELECT 1
    FROM users u
    WHERE u.user_id = o.user_id
  )
)
SELECT *
FROM orphan_orders;
```

Alternative left join:

```sql
SELECT
  o.order_id,
  o.user_id
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id
WHERE o.user_id IS NOT NULL
  AND u.user_id IS NULL;
```

Interview line:

```text
Orphan checks are a classic NOT EXISTS or anti-join use case.
```


## 43. CTE for Missing Dates

Problem:

```text
Find dates with no order records.
```

SQL:

```sql
WITH expected_dates AS (
  SELECT calendar_date
  FROM dim_calendar
  WHERE calendar_date >= DATE '2026-01-01'
    AND calendar_date <  DATE '2026-02-01'
),
actual_order_dates AS (
  SELECT DISTINCT
    CAST(order_time AS DATE) AS order_date
  FROM orders
  WHERE order_time >= DATE '2026-01-01'
    AND order_time <  DATE '2026-02-01'
)
SELECT
  e.calendar_date AS missing_date
FROM expected_dates e
WHERE NOT EXISTS (
  SELECT 1
  FROM actual_order_dates a
  WHERE a.order_date = e.calendar_date
)
ORDER BY missing_date;
```

Interview line:

```text
Missing-date checks are clearer when expected dates and actual dates are separate CTEs.
```


## 44. CTE for Incremental Watermark Logic

Problem:

```text
Select records updated after the last successful watermark.
```

Tables:

```sql
source_table(id, updated_at, payload)
pipeline_watermarks(pipeline_name, last_successful_watermark)
```

SQL:

```sql
WITH watermark AS (
  SELECT
    last_successful_watermark
  FROM pipeline_watermarks
  WHERE pipeline_name = 'orders_ingestion'
),
incremental_records AS (
  SELECT
    s.*
  FROM source_table s
  CROSS JOIN watermark w
  WHERE s.updated_at > w.last_successful_watermark
)
SELECT *
FROM incremental_records;
```

Alternative scalar subquery:

```sql
SELECT *
FROM source_table
WHERE updated_at > (
  SELECT last_successful_watermark
  FROM pipeline_watermarks
  WHERE pipeline_name = 'orders_ingestion'
);
```

Caution:

```text
The scalar subquery must return exactly one row.
```

Interview line:

```text
Watermark subqueries must be guaranteed to return one value, or the pipeline should fail clearly.
```


## 45. CTE for Upsert/Merge Staging Prep

Problem:

```text
Prepare latest source rows before merging into target.
```

SQL:

```sql
WITH source_latest AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY business_key
      ORDER BY updated_at DESC, ingested_at DESC
    ) AS rn
  FROM source_staging
),
deduped_source AS (
  SELECT
    business_key,
    col1,
    col2,
    updated_at
  FROM source_latest
  WHERE rn = 1
)
SELECT *
FROM deduped_source;
```

Usage:

```text
Use deduped_source as input to MERGE/UPSERT.
```

Interview line:

```text
Before merging incremental data, I deduplicate staging rows to one row per business key using a CTE.
```


## 46. Recursive CTE for Employee Hierarchy

Problem:

```text
Return each employee with hierarchy level from CEO.
```

Table:

```sql
employees(employee_id, manager_id, employee_name)
```

SQL:

```sql
WITH RECURSIVE employee_tree AS (
  SELECT
    employee_id,
    manager_id,
    employee_name,
    1 AS level,
    CAST(employee_name AS VARCHAR(1000)) AS path
  FROM employees
  WHERE manager_id IS NULL

  UNION ALL

  SELECT
    e.employee_id,
    e.manager_id,
    e.employee_name,
    t.level + 1 AS level,
    t.path || ' > ' || e.employee_name AS path
  FROM employees e
  JOIN employee_tree t
    ON e.manager_id = t.employee_id
)
SELECT *
FROM employee_tree
ORDER BY path;
```

Dialect note:

```text
String concatenation differs by database.
SQL Server uses + or CONCAT.
PostgreSQL uses || or CONCAT.
```

Interview line:

```text
For hierarchy queries, recursive CTEs use an anchor row and recursive expansion.
```


## 47. Recursive CTE Cycle Risk

Recursive hierarchy data can contain cycles.

Problem:

```text
A reports to B and B reports to A.
```

Risk:

```text
recursive query can loop until recursion limit
```

Conceptual protection:

```sql
WITH RECURSIVE employee_tree AS (
  SELECT
    employee_id,
    manager_id,
    employee_name,
    1 AS level,
    CAST(employee_id AS VARCHAR(1000)) AS path_ids
  FROM employees
  WHERE manager_id IS NULL

  UNION ALL

  SELECT
    e.employee_id,
    e.manager_id,
    e.employee_name,
    t.level + 1,
    t.path_ids || ',' || e.employee_id
  FROM employees e
  JOIN employee_tree t
    ON e.manager_id = t.employee_id
  WHERE t.path_ids NOT LIKE '%' || e.employee_id || '%'
)
SELECT *
FROM employee_tree;
```

Interview line:

```text
When using recursive CTEs, I mention cycle protection and recursion limits.
```


## 48. Common CTE/Subquery Mistakes

Common mistakes:

```text
unclear CTE names
too many trivial CTEs
one giant nested subquery
no aliases for derived tables
scalar subquery returns multiple rows
NOT IN with NULLs
correlated subquery where window function is cleaner
filtering window alias in WHERE
not stating intermediate grain
joining one-to-many CTE before aggregating
reusing a heavy CTE multiple times without considering performance
assuming CTE always improves performance
missing deterministic tie-breaker in ROW_NUMBER
forgetting CTE only exists for one statement
recursive CTE without stop condition
```

Strict feedback:

```text
This is not interview-ready. The query uses NOT IN against a nullable column, so it may return incorrect results. Use NOT EXISTS or filter NULLs explicitly.
```


## 49. Debugging CTE Queries

Debug CTEs stage by stage.

Checklist:

```text
1. Run base CTE count.
2. Check duplicate keys in each CTE.
3. Check grain after each aggregation.
4. Check join row counts before/after.
5. Check NULLs in join keys.
6. Check denominator counts.
7. Check final output duplicate keys.
8. Compare sample rows to expected behavior.
```

Example:

```sql
WITH base_orders AS (...),
customer_revenue AS (...)
SELECT COUNT(*) FROM base_orders;
```

Then:

```sql
WITH base_orders AS (...),
customer_revenue AS (...)
SELECT
  user_id,
  COUNT(*) AS rows_per_user
FROM customer_revenue
GROUP BY user_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
CTEs are easy to debug because I can inspect each stage independently.
```


## 50. Validation Queries

After a CTE-heavy query, validate.

### Check final duplicate keys

```sql
SELECT
  output_key,
  COUNT(*) AS row_count
FROM final_output
GROUP BY output_key
HAVING COUNT(*) > 1;
```

### Check row count before and after join

```sql
SELECT COUNT(*) FROM left_cte;
SELECT COUNT(*) FROM joined_cte;
```

### Check unmatched dimensions

```sql
SELECT COUNT(*)
FROM facts f
LEFT JOIN dim d
  ON f.dim_id = d.dim_id
WHERE d.dim_id IS NULL;
```

### Check denominator

```sql
SELECT COUNT(DISTINCT user_id)
FROM signup_cohort;
```

Interview line:

```text
For interview SQL, I explain how I would validate intermediate CTEs and final output.
```


## 51. Pattern: Base Filter CTE

Use a base CTE to apply shared filters once.

Example:

```sql
WITH base_events AS (
  SELECT
    event_id,
    user_id,
    event_name,
    event_time
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2026-02-01'
    AND user_id IS NOT NULL
)
SELECT
  event_name,
  COUNT(*) AS events
FROM base_events
GROUP BY event_name;
```

Benefits:

```text
shared date filter
shared user_id filter
less repetition
clear starting dataset
```

Interview line:

```text
A base CTE defines the eligible dataset for the metric.
```


## 52. Pattern: Aggregate Then Join

Use when joining facts to dimensions or multiple facts.

Bad:

```text
Join detailed fact rows first, then aggregate, causing row multiplication.
```

Better:

```sql
WITH order_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
)
SELECT
  u.country,
  SUM(o.revenue) AS revenue
FROM order_revenue o
JOIN users u
  ON o.user_id = u.user_id
GROUP BY u.country;
```

Caution:

```text
Ensure users has one row per user_id.
```

Interview line:

```text
Aggregating to the needed grain before joining often prevents double counting.
```


## 53. Pattern: Join Then Aggregate

Sometimes joining before aggregation is correct.

Example:

```text
Revenue by product category from order_items.
Need product category from products table before grouping.
```

SQL:

```sql
SELECT
  p.category,
  SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p
  ON oi.product_id = p.product_id
JOIN orders o
  ON oi.order_id = o.order_id
WHERE o.order_status = 'COMPLETED'
GROUP BY p.category;
```

Why join before aggregate:

```text
Category lives in products table.
The metric grain is item/category amount.
```

Interview line:

```text
Whether to aggregate before or after join depends on the metric grain and where dimensions live.
```


## 54. Pattern: Semi-Join with EXISTS

Problem:

```text
Find users who had at least one login event.
```

SQL:

```sql
SELECT
  u.user_id
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM events e
  WHERE e.user_id = u.user_id
    AND e.event_name = 'login'
);
```

Why not join:

```text
A user can have many login events. EXISTS avoids row multiplication and DISTINCT.
```

Interview line:

```text
EXISTS expresses semi-join logic: keep left rows where a right-side match exists.
```


## 55. Pattern: Anti-Join with NOT EXISTS

Problem:

```text
Find users who did not log in during January 2026.
```

SQL:

```sql
SELECT
  u.user_id
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM events e
  WHERE e.user_id = u.user_id
    AND e.event_name = 'login'
    AND e.event_time >= DATE '2026-01-01'
    AND e.event_time <  DATE '2026-02-01'
);
```

Interview line:

```text
NOT EXISTS is safer than NOT IN when the subquery column may contain NULL.
```


## 56. Pattern: Window Filter CTE

Problem:

```text
Get top 3 orders by amount per customer.
```

SQL:

```sql
WITH ranked_orders AS (
  SELECT
    user_id,
    order_id,
    total_amount,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY total_amount DESC, order_id
    ) AS rn
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT
  user_id,
  order_id,
  total_amount
FROM ranked_orders
WHERE rn <= 3;
```

Interview line:

```text
Use a CTE to filter on window function outputs when QUALIFY is unavailable.
```


## 57. Pattern: Compare to Overall Aggregate

Problem:

```text
Find orders above overall average order amount.
```

Scalar subquery:

```sql
SELECT
  order_id,
  total_amount
FROM orders
WHERE total_amount > (
  SELECT AVG(total_amount)
  FROM orders
  WHERE order_status = 'COMPLETED'
)
AND order_status = 'COMPLETED';
```

CTE/window alternative:

```sql
WITH completed_orders AS (
  SELECT
    order_id,
    total_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
),
orders_with_avg AS (
  SELECT
    order_id,
    total_amount,
    AVG(total_amount) OVER () AS avg_amount
  FROM completed_orders
)
SELECT *
FROM orders_with_avg
WHERE total_amount > avg_amount;
```

Interview line:

```text
A scalar subquery is fine for a single global aggregate, while a CTE/window version is easier if I need to show the average too.
```


## 58. Pattern: Compare to Group Aggregate

Problem:

```text
Find orders above the customer's average order amount.
```

Window solution:

```sql
WITH orders_with_avg AS (
  SELECT
    order_id,
    user_id,
    total_amount,
    AVG(total_amount) OVER (
      PARTITION BY user_id
    ) AS user_avg_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT
  order_id,
  user_id,
  total_amount,
  user_avg_amount
FROM orders_with_avg
WHERE total_amount > user_avg_amount;
```

CTE join solution:

```sql
WITH user_avg AS (
  SELECT
    user_id,
    AVG(total_amount) AS user_avg_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
)
SELECT
  o.order_id,
  o.user_id,
  o.total_amount,
  a.user_avg_amount
FROM orders o
JOIN user_avg a
  ON o.user_id = a.user_id
WHERE o.order_status = 'COMPLETED'
  AND o.total_amount > a.user_avg_amount;
```

Interview line:

```text
For group aggregate comparisons, window functions or CTE joins are often clearer than correlated subqueries.
```


## 59. Pattern: Isolate Final SELECT

For complex transformations, keep final SELECT simple.

Example:

```sql
WITH base AS (...),
clean AS (...),
aggregated AS (...),
final_metric AS (
  SELECT
    metric_date,
    numerator,
    denominator,
    numerator * 1.0 / NULLIF(denominator, 0) AS metric_rate
  FROM aggregated
)
SELECT
  metric_date,
  numerator,
  denominator,
  metric_rate
FROM final_metric
ORDER BY metric_date;
```

Benefits:

```text
final output columns are clear
debugging is easier
business metric is easy to explain
```

Interview line:

```text
I like the final SELECT to be boring; the logic should already be clear in named CTEs.
```


## 60. Case Study: Complete Metric Query

Problem:

```text
For each signup month, calculate:
- signup users
- users who purchased within 7 days
- conversion rate
```

SQL:

```sql
WITH signup_users AS (
  SELECT
    user_id,
    signup_at,
    DATE_TRUNC('month', signup_at) AS signup_month
  FROM users
  WHERE signup_at >= DATE '2026-01-01'
    AND signup_at <  DATE '2027-01-01'
),
first_purchase AS (
  SELECT
    user_id,
    MIN(order_time) AS first_purchase_time
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
),
user_conversion AS (
  SELECT
    s.signup_month,
    s.user_id,
    CASE
      WHEN f.first_purchase_time >= s.signup_at
       AND f.first_purchase_time <  s.signup_at + INTERVAL '7 days'
      THEN 1 ELSE 0
    END AS purchased_within_7_days
  FROM signup_users s
  LEFT JOIN first_purchase f
    ON s.user_id = f.user_id
),
monthly_conversion AS (
  SELECT
    signup_month,
    COUNT(*) AS signup_users,
    SUM(purchased_within_7_days) AS converted_users
  FROM user_conversion
  GROUP BY signup_month
)
SELECT
  signup_month,
  signup_users,
  converted_users,
  converted_users * 1.0 / NULLIF(signup_users, 0) AS conversion_rate
FROM monthly_conversion
ORDER BY signup_month;
```

Why this is strong:

```text
clear denominator
first purchase isolated
left join preserves non-purchasers
conversion flag at user grain
monthly aggregation after user-level classification
safe division
```

Interview line:

```text
For conversion metrics, I classify each entity first, then aggregate to reporting grain.
```


## 61. SQL Execution Order Reminder

Logical SQL execution order helps understand CTE/subquery needs.

Approximate order:

```text
FROM / JOIN
WHERE
GROUP BY
HAVING
SELECT
WINDOW functions
ORDER BY
LIMIT
```

Important consequences:

```text
WHERE cannot use SELECT aliases.
WHERE cannot filter aggregate results.
HAVING filters grouped results.
Window results usually need CTE/derived table/QUALIFY for filtering.
```

Example:

```sql
WITH grouped AS (
  SELECT
    user_id,
    COUNT(*) AS order_count
  FROM orders
  GROUP BY user_id
)
SELECT *
FROM grouped
WHERE order_count > 5;
```

Interview line:

```text
Knowing SQL's logical execution order helps decide when a CTE is needed.
```


## 62. CTEs in CREATE TABLE AS

Data Engineering often uses CTEs to build tables.

Example:

```sql
CREATE TABLE mart.daily_revenue AS
WITH completed_orders AS (
  SELECT
    order_id,
    CAST(order_time AS DATE) AS order_date,
    total_amount
  FROM raw.orders
  WHERE order_status = 'COMPLETED'
),
daily_revenue AS (
  SELECT
    order_date,
    SUM(total_amount) AS revenue,
    COUNT(DISTINCT order_id) AS orders
  FROM completed_orders
  GROUP BY order_date
)
SELECT
  order_date,
  revenue,
  orders,
  CURRENT_TIMESTAMP AS created_at
FROM daily_revenue;
```

Interview line:

```text
CTEs map naturally to transformation steps in ELT jobs and dbt-style models.
```


## 63. CTEs in INSERT INTO SELECT

Example:

```sql
INSERT INTO mart.customer_revenue_daily (
  revenue_date,
  user_id,
  revenue,
  order_count
)
WITH completed_orders AS (
  SELECT
    CAST(order_time AS DATE) AS revenue_date,
    user_id,
    order_id,
    total_amount
  FROM staging.orders
  WHERE order_status = 'COMPLETED'
),
customer_daily AS (
  SELECT
    revenue_date,
    user_id,
    SUM(total_amount) AS revenue,
    COUNT(DISTINCT order_id) AS order_count
  FROM completed_orders
  GROUP BY revenue_date, user_id
)
SELECT
  revenue_date,
  user_id,
  revenue,
  order_count
FROM customer_daily;
```

Production caution:

```text
For reruns, use idempotent strategy such as partition overwrite, delete+insert for date range, or merge/upsert.
```

Interview line:

```text
CTEs can stage transformation logic before insert, but the write strategy must still be idempotent.
```


## 64. CTEs in MERGE Preparation

Generic pattern:

```sql
MERGE INTO target_table t
USING (
  WITH ranked_source AS (
    SELECT
      *,
      ROW_NUMBER() OVER (
        PARTITION BY business_key
        ORDER BY updated_at DESC, ingested_at DESC
      ) AS rn
    FROM source_staging
  ),
  deduped_source AS (
    SELECT *
    FROM ranked_source
    WHERE rn = 1
  )
  SELECT *
  FROM deduped_source
) s
ON t.business_key = s.business_key
WHEN MATCHED THEN UPDATE SET ...
WHEN NOT MATCHED THEN INSERT ...;
```

Dialect note:

```text
MERGE syntax differs significantly between warehouses.
```

Interview line:

```text
Before MERGE, I deduplicate source staging to one row per business key to avoid ambiguous updates.
```


## 65. Interview Clarifying Questions

Ask these before writing complex CTE/subquery SQL:

```text
What is the final output grain?
What is the grain of each input table?
Are duplicate rows possible?
Which timestamp should be used?
Which records are valid?
Should NULLs be included or excluded?
Should missing dimension matches be kept?
Is this existence check or do we need joined attributes?
Can right-side table have multiple matches?
Should ties return one row or all tied rows?
Does the database support QUALIFY?
Does the database support recursive CTEs?
Does the query need to be production-optimized or interview-readable?
```

Interview line:

```text
The right CTE/subquery pattern depends on grain, cardinality, and whether I need existence or attributes.
```


## 66. Communication Scripts

### CTE script

```text
I will use CTEs here because the logic has multiple stages: base filtering, deduplication, aggregation, and final metric calculation.
```

### Subquery script

```text
A scalar subquery is fine here because I only need one global aggregate value.
```

### EXISTS script

```text
I will use EXISTS because I only care whether a related row exists and I do not need to join attributes.
```

### NOT EXISTS script

```text
I prefer NOT EXISTS for anti-join logic because it avoids NOT IN NULL issues.
```

### Window filter script

```text
I will calculate ROW_NUMBER in a CTE and then filter rn = 1 in the outer query.
```

### Grain script

```text
This CTE is one row per user per day, and the final output is one row per day.
```

### Performance script

```text
I am using CTEs for clarity. In production, I would check the execution plan because CTE materialization behavior is database-specific.
```

### Validation script

```text
I would validate each CTE by checking row counts, duplicate keys, and join cardinality before trusting the final metric.
```


## 67. Practice Problem 1: Customers Above Average Revenue

Problem:

```text
Find customers whose total completed order revenue is above the average customer revenue.
```

Solution:

```sql
WITH customer_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
),
revenue_with_average AS (
  SELECT
    user_id,
    revenue,
    AVG(revenue) OVER () AS average_customer_revenue
  FROM customer_revenue
)
SELECT
  user_id,
  revenue,
  average_customer_revenue
FROM revenue_with_average
WHERE revenue > average_customer_revenue;
```

Key idea:

```text
Aggregate to customer grain first, then compare each customer to the average customer revenue.
```


## 68. Practice Problem 2: Users With No Events

Problem:

```text
Find users who signed up in January 2026 but had no events after signup.
```

Solution:

```sql
WITH january_users AS (
  SELECT
    user_id,
    signup_at
  FROM users
  WHERE signup_at >= DATE '2026-01-01'
    AND signup_at <  DATE '2026-02-01'
)
SELECT
  u.user_id,
  u.signup_at
FROM january_users u
WHERE NOT EXISTS (
  SELECT 1
  FROM events e
  WHERE e.user_id = u.user_id
    AND e.event_time >= u.signup_at
);
```

Key idea:

```text
Use NOT EXISTS for absence of related activity after signup.
```


## 69. Practice Problem 3: First and Latest Order Per User

Problem:

```text
Return first and latest completed order date per user.
```

Solution:

```sql
WITH completed_orders AS (
  SELECT
    user_id,
    order_id,
    order_time
  FROM orders
  WHERE order_status = 'COMPLETED'
),
ranked_orders AS (
  SELECT
    user_id,
    order_id,
    order_time,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time, order_id
    ) AS first_rn,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time DESC, order_id DESC
    ) AS latest_rn
  FROM completed_orders
),
first_orders AS (
  SELECT
    user_id,
    order_id AS first_order_id,
    order_time AS first_order_time
  FROM ranked_orders
  WHERE first_rn = 1
),
latest_orders AS (
  SELECT
    user_id,
    order_id AS latest_order_id,
    order_time AS latest_order_time
  FROM ranked_orders
  WHERE latest_rn = 1
)
SELECT
  f.user_id,
  f.first_order_id,
  f.first_order_time,
  l.latest_order_id,
  l.latest_order_time
FROM first_orders f
JOIN latest_orders l
  ON f.user_id = l.user_id;
```

Key idea:

```text
Use ranking CTEs when you need row attributes from first/latest records.
```


## 70. Practice Problem 4: Products Never Purchased

Problem:

```text
Find products that are active but never appeared in completed orders.
```

Solution:

```sql
SELECT
  p.product_id,
  p.category
FROM products p
WHERE p.is_active = true
  AND NOT EXISTS (
    SELECT 1
    FROM order_items oi
    JOIN orders o
      ON oi.order_id = o.order_id
    WHERE oi.product_id = p.product_id
      AND o.order_status = 'COMPLETED'
  );
```

Key idea:

```text
Use NOT EXISTS for products with no completed-order relationship.
```


## 71. Practice Problem 5: Daily Revenue with Missing Dates

Problem:

```text
Return daily revenue for January 2026, including dates with zero revenue.
```

Solution:

```sql
WITH calendar AS (
  SELECT calendar_date
  FROM dim_calendar
  WHERE calendar_date >= DATE '2026-01-01'
    AND calendar_date <  DATE '2026-02-01'
),
daily_revenue AS (
  SELECT
    CAST(order_time AS DATE) AS order_date,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
    AND order_time >= DATE '2026-01-01'
    AND order_time <  DATE '2026-02-01'
  GROUP BY CAST(order_time AS DATE)
)
SELECT
  c.calendar_date,
  COALESCE(d.revenue, 0) AS revenue
FROM calendar c
LEFT JOIN daily_revenue d
  ON c.calendar_date = d.order_date
ORDER BY c.calendar_date;
```

Key idea:

```text
Use a calendar CTE/table to preserve missing dates.
```


## 72. Practice Problem 6: Duplicate Detection and Dedup

Problem:

```text
Find duplicate transactions and produce deduped latest version.
```

Duplicate report:

```sql
SELECT
  transaction_id,
  COUNT(*) AS row_count,
  MIN(ingested_at) AS first_seen,
  MAX(ingested_at) AS last_seen
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;
```

Deduped CTE:

```sql
WITH ranked_transactions AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY transaction_id
      ORDER BY ingested_at DESC
    ) AS rn
  FROM transactions
)
SELECT *
FROM ranked_transactions
WHERE rn = 1;
```

Key idea:

```text
Separate duplicate detection from deduped output.
```


## 73. Practice Problem 7: Orders Greater Than User Average

Problem:

```text
Find completed orders whose amount is greater than the user's average completed order amount.
```

Solution:

```sql
WITH completed_orders AS (
  SELECT
    order_id,
    user_id,
    total_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
),
orders_with_user_avg AS (
  SELECT
    order_id,
    user_id,
    total_amount,
    AVG(total_amount) OVER (
      PARTITION BY user_id
    ) AS user_avg_amount
  FROM completed_orders
)
SELECT *
FROM orders_with_user_avg
WHERE total_amount > user_avg_amount;
```

Key idea:

```text
Window aggregate avoids a correlated subquery and keeps row-level order data.
```


## 74. Practice Problem 8: Active Users with Purchases

Problem:

```text
Find users active in January who also made at least one completed purchase in January.
```

Solution:

```sql
WITH january_active_users AS (
  SELECT DISTINCT
    user_id
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2026-02-01'
    AND user_id IS NOT NULL
)
SELECT
  a.user_id
FROM january_active_users a
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = a.user_id
    AND o.order_status = 'COMPLETED'
    AND o.order_time >= DATE '2026-01-01'
    AND o.order_time <  DATE '2026-02-01'
);
```

Key idea:

```text
CTE defines active users; EXISTS checks purchase existence.
```


## 75. Practice Problem 9: Latest Plan at Order Time

Problem:

```text
For each order, attach the user's plan active at order_time.
```

Solution:

```sql
SELECT
  o.order_id,
  o.user_id,
  o.order_time,
  p.plan
FROM orders o
LEFT JOIN user_plan_history p
  ON o.user_id = p.user_id
 AND o.order_time >= p.effective_from
 AND (p.effective_to IS NULL OR o.order_time < p.effective_to);
```

Validation CTE:

```sql
WITH matches AS (
  SELECT
    o.order_id,
    COUNT(*) AS matching_plan_rows
  FROM orders o
  LEFT JOIN user_plan_history p
    ON o.user_id = p.user_id
   AND o.order_time >= p.effective_from
   AND (p.effective_to IS NULL OR o.order_time < p.effective_to)
  GROUP BY o.order_id
)
SELECT *
FROM matches
WHERE matching_plan_rows > 1;
```

Key idea:

```text
As-of joins need validation that intervals do not overlap.
```


## 76. Practice Problem 10: Category Revenue Share

Problem:

```text
Find revenue share by product category.
```

Solution:

```sql
WITH category_revenue AS (
  SELECT
    p.category,
    SUM(oi.quantity * oi.unit_price) AS revenue
  FROM order_items oi
  JOIN orders o
    ON oi.order_id = o.order_id
  JOIN products p
    ON oi.product_id = p.product_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY p.category
)
SELECT
  category,
  revenue,
  revenue * 1.0 / NULLIF(SUM(revenue) OVER (), 0) AS revenue_share
FROM category_revenue
ORDER BY revenue DESC;
```

Key idea:

```text
Use a CTE for category aggregation, then a window total for share.
```


## 77. Practice Problem 11: Users With More Than One Account

Problem:

```text
Find emails associated with more than one user account.
```

Solution:

```sql
WITH normalized_users AS (
  SELECT
    user_id,
    LOWER(TRIM(email)) AS normalized_email
  FROM users
  WHERE email IS NOT NULL
),
email_counts AS (
  SELECT
    normalized_email,
    COUNT(DISTINCT user_id) AS user_count
  FROM normalized_users
  GROUP BY normalized_email
)
SELECT
  normalized_email,
  user_count
FROM email_counts
WHERE user_count > 1
ORDER BY user_count DESC, normalized_email;
```

Key idea:

```text
Normalize first, aggregate second, filter third.
```


## 78. Practice Problem 12: Orders Without Successful Payment

Problem:

```text
Find completed orders that do not have a successful payment.
```

Solution:

```sql
SELECT
  o.order_id,
  o.user_id,
  o.order_time
FROM orders o
WHERE o.order_status = 'COMPLETED'
  AND NOT EXISTS (
    SELECT 1
    FROM payments p
    WHERE p.order_id = o.order_id
      AND p.payment_status = 'SUCCESS'
  );
```

Key idea:

```text
This is anti-existence logic; NOT EXISTS is clean and safe.
```


## 79. Practice Problem 13: Monthly New and Repeat Buyers

Problem:

```text
For each order month, count new buyers and repeat buyers.
New buyer means their first completed order is in that month.
```

Solution:

```sql
WITH completed_orders AS (
  SELECT
    order_id,
    user_id,
    order_time,
    DATE_TRUNC('month', order_time) AS order_month
  FROM orders
  WHERE order_status = 'COMPLETED'
    AND user_id IS NOT NULL
),
first_order AS (
  SELECT
    user_id,
    MIN(order_time) AS first_order_time
  FROM completed_orders
  GROUP BY user_id
),
monthly_buyers AS (
  SELECT DISTINCT
    user_id,
    order_month
  FROM completed_orders
)
SELECT
  mb.order_month,
  COUNT(DISTINCT CASE
    WHEN DATE_TRUNC('month', f.first_order_time) = mb.order_month THEN mb.user_id
  END) AS new_buyers,
  COUNT(DISTINCT CASE
    WHEN DATE_TRUNC('month', f.first_order_time) < mb.order_month THEN mb.user_id
  END) AS repeat_buyers
FROM monthly_buyers mb
JOIN first_order f
  ON mb.user_id = f.user_id
GROUP BY mb.order_month
ORDER BY mb.order_month;
```

Key idea:

```text
Separate first-order logic from monthly activity logic.
```


## 80. Practice Problem 14: Top 2 Categories Per Country

Problem:

```text
Find top 2 product categories by revenue for each country.
```

Solution:

```sql
WITH category_country_revenue AS (
  SELECT
    u.country,
    p.category,
    SUM(oi.quantity * oi.unit_price) AS revenue
  FROM orders o
  JOIN users u
    ON o.user_id = u.user_id
  JOIN order_items oi
    ON o.order_id = oi.order_id
  JOIN products p
    ON oi.product_id = p.product_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY
    u.country,
    p.category
),
ranked AS (
  SELECT
    country,
    category,
    revenue,
    ROW_NUMBER() OVER (
      PARTITION BY country
      ORDER BY revenue DESC, category
    ) AS rn
  FROM category_country_revenue
)
SELECT
  country,
  category,
  revenue
FROM ranked
WHERE rn <= 2
ORDER BY country, rn;
```

Key idea:

```text
Aggregate to country/category grain, then rank within country.
```


## 81. Practice Problem 15: Month-over-Month Active User Growth

Problem:

```text
Calculate MAU and month-over-month MAU growth.
```

Solution:

```sql
WITH monthly_active AS (
  SELECT
    DATE_TRUNC('month', event_time) AS activity_month,
    COUNT(DISTINCT user_id) AS mau
  FROM events
  WHERE user_id IS NOT NULL
  GROUP BY DATE_TRUNC('month', event_time)
),
with_previous AS (
  SELECT
    activity_month,
    mau,
    LAG(mau) OVER (
      ORDER BY activity_month
    ) AS previous_mau
  FROM monthly_active
)
SELECT
  activity_month,
  mau,
  previous_mau,
  mau - previous_mau AS mau_change,
  (mau - previous_mau) * 1.0 / NULLIF(previous_mau, 0) AS mau_growth_rate
FROM with_previous
ORDER BY activity_month;
```

Key idea:

```text
Build monthly aggregate first, then use LAG in the next stage.
```


## 82. CTE/Subquery Pattern Classification Drill

Classify each prompt.

```text
1. Need users with at least one order.
2. Need users with no orders.
3. Need latest row per user.
4. Need filter row_number = 1.
5. Need compare orders to global average.
6. Need compare orders to user average.
7. Need percent of total revenue by category.
8. Need multi-stage retention query.
9. Need products never sold.
10. Need source-target reconciliation.
11. Need generate employee hierarchy.
12. Need generate small date sequence.
13. Need calculate repeat purchase rate.
14. Need remove duplicate events.
15. Need order count > 5 by user.
16. Need avoid NOT IN NULL issue.
17. Need join order to active plan at order_time.
18. Need prepare source for MERGE.
19. Need debug intermediate row counts.
20. Need simplify a huge nested query.
```

Expected classification:

```text
1. EXISTS semi-join
2. NOT EXISTS anti-join
3. ROW_NUMBER in CTE
4. CTE or QUALIFY
5. scalar subquery or window OVER ()
6. window PARTITION BY or CTE join
7. CTE aggregate + window total
8. multiple CTEs
9. NOT EXISTS or anti-join CTE
10. FULL OUTER JOIN CTE
11. recursive CTE
12. recursive CTE or calendar table
13. CTE staged metric
14. ROW_NUMBER dedupe CTE
15. HAVING or aggregate CTE
16. NOT EXISTS
17. interval/as-of join
18. deduped staging CTE
19. inspect CTE stages
20. refactor into named CTEs
```

Passing standard:

```text
18/20 correct before timed CTE/subquery mocks.
```


## 83. High-ROI Topics

Practice these first.

| Topic | Candidate Must Explain |
|---|---|
| CTE basics | WITH syntax and named result |
| derived table | subquery in FROM |
| scalar subquery | returns one value |
| correlated subquery | references outer query |
| EXISTS | existence check |
| NOT EXISTS | anti-join |
| NOT IN issue | NULL trap |
| window filtering | CTE around ROW_NUMBER |
| deduplication | ROW_NUMBER partition by key |
| first/latest row | ROW_NUMBER with tie-breaker |
| staged metrics | base/filter/aggregate/final |
| grain | one row meaning per CTE |
| recursive CTE | hierarchy/date generation |
| validation | inspect each CTE |
| performance | optimizer/materialization varies |


## 84. 7-Day CTE/Subquery Plan

### Day 1: CTE basics

Problems:

```text
base filter CTE
multi-step revenue query
aggregate CTE
final metric CTE
CTE naming and grain drills
```

Focus:

```text
readability
grain
staging logic
```

### Day 2: Subquery basics

Problems:

```text
scalar subquery
IN subquery
derived table
subquery in WHERE
subquery in FROM
```

Focus:

```text
subquery types
aliases
single-value guarantee
```

### Day 3: EXISTS and NOT EXISTS

Problems:

```text
users with orders
users without orders
products never sold
orders without payment
orphan facts
```

Focus:

```text
semi-join
anti-join
NULL safety
```

### Day 4: Window filtering CTEs

Problems:

```text
latest order per user
first event per user
top N per group
deduplicate events
latest profile snapshot
```

Focus:

```text
ROW_NUMBER
RANK
tie-breakers
filtering window outputs
```

### Day 5: Business metrics with CTEs

Problems:

```text
conversion rate
retention
repeat purchase rate
revenue share
monthly growth
```

Focus:

```text
multi-stage metrics
denominators
safe division
```

### Day 6: Data Engineering cases

Problems:

```text
source-target reconciliation
watermark incremental query
staging dedupe before merge
missing dates
data quality checks
```

Focus:

```text
DE transformations
validation
idempotent thinking
```

### Day 7: Mock and repair

Tasks:

```text
Run CTE/subquery mock.
Review mistakes.
Repair weakest topic.
Update progress.
```


## 85. 30-Day CTE/Subquery Plan

### Week 1: CTE foundation

Focus:

```text
WITH syntax
multiple CTEs
naming
grain
base/filter/aggregate/final patterns
```

Exit:

```text
Candidate can structure simple business SQL with clear CTEs.
```

### Week 2: Subqueries and EXISTS

Focus:

```text
scalar subqueries
derived tables
IN
EXISTS
NOT EXISTS
correlated subqueries
NULL behavior
```

Exit:

```text
Candidate chooses correct subquery type and avoids NOT IN traps.
```

### Week 3: Windows and business metrics

Focus:

```text
ROW_NUMBER filtering
dedupe
first/latest
top N
retention
conversion
revenue share
growth
```

Exit:

```text
Candidate can solve complex interview metrics cleanly.
```

### Week 4: Data Engineering production SQL

Focus:

```text
reconciliation
watermarks
merge preparation
as-of joins
data quality
recursive CTEs
performance
mock interviews
```

Exit:

```text
Average mock score >= 4/5.
```


## 86. Mock Set 1: CTE Fundamentals

Problems:

```text
1. Rewrite a nested query into CTEs.
2. Calculate customer revenue with base/completed/customer CTEs.
3. State grain of each CTE.
4. Filter aggregate result using CTE.
5. Validate duplicate output keys.
```

Expected skills:

```text
CTE syntax
readability
grain discipline
aggregate filtering
validation
```

Passing standard:

```text
Average score >= 4/5.
Candidate uses meaningful CTE names and clear grain.
```


## 87. Mock Set 2: Subqueries and EXISTS

Problems:

```text
1. Users with completed orders using EXISTS.
2. Users without completed orders using NOT EXISTS.
3. Orders above global average using scalar subquery.
4. Orders above user average using window/CTE.
5. Explain NOT IN NULL issue.
```

Expected skills:

```text
EXISTS
NOT EXISTS
scalar subquery
correlated subquery alternative
NULL handling
```

Passing standard:

```text
Average score >= 4/5.
Candidate avoids NOT IN when NULLs are possible.
```


## 88. Mock Set 3: Window CTEs

Problems:

```text
1. Latest order per user.
2. First event per user.
3. Deduplicate events.
4. Top 3 orders per customer.
5. Current profile snapshot.
```

Expected skills:

```text
ROW_NUMBER
RANK
tie-breakers
CTE window filtering
dedupe rules
```

Passing standard:

```text
Average score >= 4/5.
Candidate includes deterministic tie-breakers.
```


## 89. Mock Set 4: Data Engineering CTE Cases

Problems:

```text
1. Source-target reconciliation.
2. Incremental records after watermark.
3. Deduped staging source before MERGE.
4. Missing daily partitions.
5. Data quality summary using flags CTE.
```

Expected skills:

```text
FULL OUTER JOIN
scalar watermark
ROW_NUMBER dedupe
calendar anti-join
quality flags
```

Passing standard:

```text
Average score >= 4/5.
Candidate validates intermediate CTEs and explains production concerns.
```


## 90. Timed Drill Protocol

Use this timing protocol.

### Simple CTE/subquery problem

```text
10-20 minutes
```

### Medium business metric

```text
25-40 minutes
```

### Complex DE transformation

```text
35-45 minutes
```

Per drill:

```text
Minute 0-3:
Clarify final output and grain.

Minute 3-6:
Choose CTE/subquery/window/EXISTS pattern.

Minute 6-25:
Write SQL with named CTEs.

Minute 25-35:
Validate intermediate row counts and key uniqueness.

Minute 35-45:
Explain performance, NULL behavior, and production trade-offs.
```

If candidate writes one huge nested query:

```text
Stop and ask them to refactor into named CTEs.
```


## 91. Review Checklist

Review CTE/subquery answers using:

```text
1. Did candidate identify final output grain?
2. Did candidate identify each CTE grain?
3. Are CTE names meaningful?
4. Is each CTE doing a meaningful step?
5. Are derived tables aliased?
6. Is scalar subquery guaranteed to return one value?
7. Is EXISTS used for existence checks?
8. Is NOT EXISTS used for anti-joins?
9. Did candidate avoid NOT IN NULL traps?
10. Did candidate filter window function results correctly?
11. Did candidate use deterministic tie-breakers?
12. Did candidate avoid accidental row multiplication?
13. Did candidate handle NULLs and safe division?
14. Did candidate validate intermediate counts?
15. Did candidate check duplicate output keys?
16. Did candidate explain CTE vs subquery choice?
17. Did candidate explain performance considerations?
18. Did candidate mention database dialect when needed?
19. Did candidate explain production use?
20. Is the final SQL readable?
```

Verdict examples:

```text
Correct result but unreadable.
Good CTEs but unclear grain.
Good EXISTS usage.
Wrong NOT IN with NULL risk.
Good window CTE but missing tie-breaker.
Interview-ready.
Strong.
```


## 92. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Unclear CTE names | Naming drills |
| Grain confusion | CTE grain drills |
| Huge nested SQL | Refactor-to-CTE drills |
| Scalar subquery misuse | Single-value guarantee drills |
| NOT IN NULL bug | NOT EXISTS drills |
| EXISTS confusion | Semi-join drills |
| NOT EXISTS confusion | Anti-join drills |
| Correlated subquery slow/unclear | Rewrite as join/window drills |
| Window alias in WHERE | Window CTE drills |
| Missing tie-breakers | ROW_NUMBER drills |
| Double counting after join | Aggregate-to-grain drills |
| No validation | Intermediate CTE count drills |
| Recursive CTE confusion | Anchor/recursive drills |
| Performance overclaims | Execution plan/materialization drills |

If weakness repeats:

```text
Use weakness-repair-mode.md.
```


## 93. Candidate Self-Review Questions

After every CTE/subquery problem, candidate should answer:

```text
1. What is the final output grain?
2. What is the grain of each CTE?
3. Why did I use a CTE here?
4. Could a derived table be enough?
5. Is this an existence check?
6. Should I use EXISTS instead of JOIN?
7. Is this an anti-join?
8. Should I use NOT EXISTS instead of NOT IN?
9. Can any subquery return multiple rows unexpectedly?
10. Are NULLs handled safely?
11. Am I filtering on a window function correctly?
12. Do I have deterministic tie-breakers?
13. Can joins multiply rows?
14. Should I aggregate before joining?
15. How would I validate each stage?
16. Is the SQL readable?
17. What is the performance risk?
18. Does database dialect affect syntax?
19. Can this query be used in an ETL/ELT job?
20. What would I test in production?
```

If candidate cannot answer these:

```text
The CTE/subquery solution is not interview-ready.
```


## 94. Maintenance Drills

After completing CTEs and subqueries, maintain skill with:

```text
1 CTE refactoring drill per week
1 EXISTS/NOT EXISTS drill per week
1 window filter CTE drill per week
1 business metric CTE drill every 2 weeks
1 DE transformation CTE drill every 2 weeks
1 full SQL mock every month
```

Maintenance rotation:

```text
Week 1: base/filter/aggregate/final CTEs
Week 2: EXISTS/NOT EXISTS and NULL behavior
Week 3: ROW_NUMBER dedupe and latest rows
Week 4: reconciliation/watermark/merge prep
```

If score drops below 4:

```text
Run weakness-repair-mode.md for failed topic.
```


## 95. Progress Tracking Template

Use this progress format.

```text
# CTEs and Subqueries Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

CTE syntax:
CTE naming:
CTE grain:
Multiple CTEs:
Derived tables:
Scalar subqueries:
IN subqueries:
EXISTS:
NOT EXISTS:
NOT IN NULL behavior:
Correlated subqueries:
Subquery rewrite:
Window filter CTEs:
ROW_NUMBER dedupe:
First/latest rows:
Aggregate filtering:
Percent of total:
Business metrics:
Reconciliation:
Watermarks:
Merge preparation:
Data quality CTEs:
Recursive CTEs:
Performance reasoning:
Validation:

## Repeated Mistakes

-

## Repair Items

-

## Next Practice

Today:
This week:
Next mock:
```


## 96. Final Exit Test

Candidate passes CTEs and subqueries when they can solve/explain:

```text
1. Basic WITH CTE syntax.
2. Multiple CTEs referencing earlier CTEs.
3. Meaningful CTE naming.
4. CTE grain explanation.
5. Derived table syntax and aliasing.
6. Scalar subquery use and risks.
7. IN subquery use.
8. EXISTS semi-join.
9. NOT EXISTS anti-join.
10. NOT IN NULL trap.
11. Correlated subquery.
12. Correlated subquery rewrite to join/window.
13. Aggregate filtering using HAVING and CTEs.
14. Window function filtering using CTE.
15. Deduplication using ROW_NUMBER.
16. First/latest row retrieval.
17. Top N per group.
18. Percent of total using CTE + window.
19. Conversion metric using staged CTEs.
20. Retention metric using staged CTEs.
21. Source-target reconciliation.
22. Missing date check.
23. Orphan record check.
24. Watermark incremental filter.
25. Merge preparation with staging dedupe.
26. Recursive CTE hierarchy basics.
27. Recursive CTE date generation basics.
28. CTE validation strategy.
29. CTE performance considerations.
30. Data Engineering production usage.
```

Passing standard:

```text
Average score >= 4/5.
No NOT IN NULL mistakes.
No unclear CTE grain.
No filtering window aliases in WHERE.
No unreadable nested SQL.
No missing validation explanation.
Can choose between CTE, subquery, EXISTS, JOIN, and window function.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles complex multi-step business SQL, DE transformations, NULL traps, recursive basics, performance trade-offs, and validation clearly under pressure.
```


## 97. Final Summary

CTEs and subqueries are core SQL tools for Data Engineering interviews.

They map directly to:

```text
business metric queries
warehouse transformations
ETL/ELT staging
deduplication
latest snapshot creation
source-target reconciliation
data-quality checks
anti-join validation
watermark incremental processing
merge preparation
hierarchy traversal
date sequence generation
query debugging
```

The candidate must master:

```text
CTE syntax
multiple CTEs
CTE naming
CTE grain
derived tables
scalar subqueries
IN
EXISTS
NOT EXISTS
NOT IN NULL behavior
correlated subqueries
window filtering CTEs
ROW_NUMBER dedupe
first/latest rows
aggregate filtering
business metric staging
data-quality CTEs
reconciliation CTEs
recursive CTE basics
performance trade-offs
validation strategy
```

The mentor must be strict:

```text
Unclear CTE grain → not interview-ready.
NOT IN with nullable subquery → not interview-ready.
Window alias filtered in WHERE → not interview-ready.
Scalar subquery returning many rows → not interview-ready.
Unreadable nested SQL → not interview-ready.
No validation plan → not interview-ready.
```

The goal is not to use CTEs everywhere.

The goal is to choose the right structure so SQL is correct, readable, explainable, and safe for Data Engineering interview problems.


## 98. Problem Card Appendix

### Card 1: Base CTE

Topic:

```text
filtering
```

Core idea:

```text
Apply shared date/status filters once.
```

Data Engineering connection:

```text
Pipeline staging.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Aggregate CTE

Topic:

```text
grouping
```

Core idea:

```text
Build lower-grain metric first.
```

Data Engineering connection:

```text
Data marts.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Derived Table

Topic:

```text
inline table
```

Core idea:

```text
Small one-time aggregation.
```

Data Engineering connection:

```text
Compact SQL.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Scalar Subquery

Topic:

```text
single value
```

Core idea:

```text
Compare to global aggregate.
```

Data Engineering connection:

```text
Metric thresholds.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: EXISTS

Topic:

```text
semi-join
```

Core idea:

```text
Find rows with related records.
```

Data Engineering connection:

```text
Activity checks.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: NOT EXISTS

Topic:

```text
anti-join
```

Core idea:

```text
Find rows without related records.
```

Data Engineering connection:

```text
Orphan/missing checks.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Correlated Subquery

Topic:

```text
outer reference
```

Core idea:

```text
Row-specific comparison.
```

Data Engineering connection:

```text
Per-user comparisons.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Window CTE

Topic:

```text
filter windows
```

Core idea:

```text
Filter ROW_NUMBER/RANK results.
```

Data Engineering connection:

```text
Dedup/latest.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Dedup CTE

Topic:

```text
ROW_NUMBER
```

Core idea:

```text
Keep latest per business key.
```

Data Engineering connection:

```text
Incremental staging.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Reconciliation CTE

Topic:

```text
full outer
```

Core idea:

```text
Compare source and target.
```

Data Engineering connection:

```text
Data validation.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Watermark CTE

Topic:

```text
incremental
```

Core idea:

```text
Filter after last successful time.
```

Data Engineering connection:

```text
Ingestion pipelines.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Recursive CTE

Topic:

```text
hierarchy
```

Core idea:

```text
Traverse parent-child relationships.
```

Data Engineering connection:

```text
Org/category trees.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Date Recursive CTE

Topic:

```text
sequence
```

Core idea:

```text
Generate small date ranges.
```

Data Engineering connection:

```text
Missing date checks.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Percent Total

Topic:

```text
window total
```

Core idea:

```text
Share of total metric.
```

Data Engineering connection:

```text
Analytics.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Retention CTE

Topic:

```text
cohort
```

Core idea:

```text
Preserve cohort denominator.
```

Data Engineering connection:

```text
Product analytics.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Funnel CTE

Topic:

```text
staged events
```

Core idea:

```text
Extract and validate ordered steps.
```

Data Engineering connection:

```text
Conversion metrics.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Data Quality CTE

Topic:

```text
flags
```

Core idea:

```text
Create rule flags then summarize.
```

Data Engineering connection:

```text
DQ reporting.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Merge Prep CTE

Topic:

```text
staging dedupe
```

Core idea:

```text
One row per business key before upsert.
```

Data Engineering connection:

```text
Warehouse loads.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: As-of Join CTE

Topic:

```text
intervals
```

Core idea:

```text
Attach dimension active at event time.
```

Data Engineering connection:

```text
SCD logic.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Validation CTE

Topic:

```text
debug
```

Core idea:

```text
Check duplicate output keys.
```

Data Engineering connection:

```text
Production reliability.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Input grain.
3. Output grain.
4. SQL skeleton.
5. Edge case.
6. Validation check.
7. Performance consideration.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 99. Data Engineering Scenario Appendix

### Scenario 1: Debug Huge Nested SQL

Pattern:

```text
refactor to CTEs
```

Task:

```text
Break query into named stages.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: Bad NOT IN Result

Pattern:

```text
NULL trap
```

Task:

```text
Replace with NOT EXISTS.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: Latest User Profile

Pattern:

```text
ROW_NUMBER CTE
```

Task:

```text
Get current row per user.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: Duplicate Event Cleanup

Pattern:

```text
dedupe CTE
```

Task:

```text
Keep latest ingestion per event_id.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: Users With No Purchase

Pattern:

```text
anti-join
```

Task:

```text
Find non-converting users.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: Revenue Share

Pattern:

```text
aggregate + window
```

Task:

```text
Percent contribution by category.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: Watermark Load

Pattern:

```text
scalar/CTE
```

Task:

```text
Select new records after checkpoint.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: MERGE Source Prep

Pattern:

```text
staging dedupe
```

Task:

```text
Avoid duplicate business key merge.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: Missing Partitions

Pattern:

```text
calendar + NOT EXISTS
```

Task:

```text
Find absent daily data.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: Hierarchy Query

Pattern:

```text
recursive CTE
```

Task:

```text
Traverse managers/categories.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: Retention Query

Pattern:

```text
staged CTEs
```

Task:

```text
Preserve denominator.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Join Explosion

Pattern:

```text
aggregate before join
```

Task:

```text
Prevent one-to-many overcounting.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: As-of Dimension

Pattern:

```text
interval join
```

Task:

```text
Attach historical state.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Data Quality Report

Pattern:

```text
flag CTE
```

Task:

```text
Summarize validation failures.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: Performance Review

Pattern:

```text
execution plan
```

Task:

```text
Discuss CTE materialization and filtering.
```

Minimum expected answer:

```text
1. Choose CTE/subquery pattern.
2. Explain why it fits.
3. Write SQL or pseudocode.
4. State edge cases.
5. State validation.
6. State production consideration.
```

Passing score:

```text
4/5 or higher.
```


## 100. Drill Appendix

### Drill 1: CTE Naming Drill

Task:

```text
Rename vague CTEs into purpose-based names.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Grain Drill

Task:

```text
State the row grain of every CTE.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Refactor Drill

Task:

```text
Rewrite nested subquery SQL into CTEs.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Derived Table Drill

Task:

```text
Use a FROM subquery with a proper alias.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Scalar Drill

Task:

```text
Use scalar subquery for global average.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: EXISTS Drill

Task:

```text
Write semi-join queries.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: NOT EXISTS Drill

Task:

```text
Write anti-join queries.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: NULL Trap Drill

Task:

```text
Explain and fix NOT IN with NULLs.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Correlated Drill

Task:

```text
Write and then rewrite a correlated subquery.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Window Filter Drill

Task:

```text
Filter ROW_NUMBER using CTE.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Dedup Drill

Task:

```text
Keep latest row per key.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Top N Drill

Task:

```text
Top N per group using ranking CTE.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Metric Stage Drill

Task:

```text
Break conversion metric into staged CTEs.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Reconciliation Drill

Task:

```text
Use full outer join with status classification.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Watermark Drill

Task:

```text
Filter incremental records with a watermark CTE.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Merge Prep Drill

Task:

```text
Deduplicate source before merge.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Recursive Drill

Task:

```text
Build basic employee hierarchy.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Validation Drill

Task:

```text
Write row count and duplicate key checks.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 19: Performance Drill

Task:

```text
Explain CTE materialization caveat.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 20: Production Drill

Task:

```text
Turn CTE query into CTAS/INSERT pattern.
```

Minimum passing answer:

```text
1. State the pattern.
2. Write correct SQL.
3. Explain grain.
4. Explain edge case.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 101. Quick Reference Cards

### Quick Card 1: CTE

Summary:

```text
Named temporary result inside one SQL statement.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 2: Derived table

Summary:

```text
Subquery in FROM; must be aliased.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 3: Scalar subquery

Summary:

```text
Returns exactly one value.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 4: Correlated subquery

Summary:

```text
References outer query columns.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 5: EXISTS

Summary:

```text
Checks at least one matching row.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 6: NOT EXISTS

Summary:

```text
Checks no matching rows; safe anti-join.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 7: NOT IN

Summary:

```text
Dangerous when subquery returns NULL.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 8: ROW_NUMBER CTE

Summary:

```text
Use to filter first/latest/dedup rows.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 9: HAVING

Summary:

```text
Filters grouped results.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 10: Window filter

Summary:

```text
Use CTE or QUALIFY.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 11: Recursive CTE

Summary:

```text
Anchor + recursive member.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 12: Grain

Summary:

```text
What one row represents.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 13: Materialization

Summary:

```text
Database-specific CTE execution behavior.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 14: Validation

Summary:

```text
Check counts, duplicates, joins after stages.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```


## 102. CTE/Subquery Interview FAQ

### FAQ 1: Are CTEs faster than subqueries?

Answer:

```text
Not automatically. CTEs improve readability; performance depends on database optimizer and execution plan.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 2: Can I use a CTE multiple times?

Answer:

```text
Often yes, but repeated references may have performance implications depending on database.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 3: Why should I avoid NOT IN?

Answer:

```text
If the subquery returns NULL, NOT IN can return unexpected results. NOT EXISTS is safer.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 4: When should I use EXISTS instead of JOIN?

Answer:

```text
When you only need to know whether a related row exists and do not need attributes from that table.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 5: Why do I need a CTE for ROW_NUMBER?

Answer:

```text
Most dialects do not allow filtering a SELECT alias/window result in WHERE; CTE makes it filterable.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 6: What is a correlated subquery?

Answer:

```text
A subquery that references values from the outer query.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 7: When should I rewrite a correlated subquery?

Answer:

```text
When a join or window function is clearer or likely more efficient.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 8: What is recursive CTE used for?

Answer:

```text
Hierarchies, trees, graph-like traversal, or small generated sequences.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 9: How do CTEs help debugging?

Answer:

```text
You can inspect intermediate row counts, duplicates, and grain at each named step.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```

### FAQ 10: Can CTEs be used in ETL/ELT jobs?

Answer:

```text
Yes. They are common in CTAS, INSERT SELECT, MERGE preparation, and dbt-style transformations.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation or performance note.
```
