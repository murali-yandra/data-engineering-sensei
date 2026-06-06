# SQL Joins Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/sql/joins.md
```

This guide teaches and drills **SQL joins for Data Engineering interviews**.

This is not a generic SQL syntax note. It is an interview-focused guide for candidates who need to join fact tables, dimension tables, event tables, snapshot tables, staging tables, historical tables, source-target reconciliation tables, and business analytics tables without corrupting row counts or metrics.

Joins are high-ROI for Data Engineering interviews because interviewers often test whether you can:

- choose the correct join type
- explain INNER JOIN vs LEFT JOIN vs FULL OUTER JOIN
- preserve the correct denominator in business metrics
- avoid accidental row multiplication
- detect duplicate join keys
- join fact tables to dimensions correctly
- perform anti-joins
- perform semi-joins
- join multiple fact tables safely
- join order headers to order items without double counting
- join events to users
- join source and target tables for reconciliation
- join slowly changing dimensions using as-of logic
- detect orphan records
- detect missing dimension records
- handle NULL join keys
- handle many-to-many joins
- aggregate before joining when needed
- debug wrong dashboard numbers caused by joins
- validate row counts before and after joins
- explain join performance considerations

Use this guide with:

- `docs/sql-interview-guide.md`
- `docs/data-engineering-fundamentals.md`
- `docs/data-warehouse-guide.md`
- `docs/data-modeling-guide.md`
- `docs/etl-elt-pipelines-guide.md`
- `docs/faang-interview-standards.md`
- `docs/assessment-rubric.md`
- `docs/communication-rubric.md`
- `modes/sql-drill-mode.md`
- `modes/interview-mode.md`
- `modes/review-mode.md`
- `modes/feedback-mode.md`
- `modes/weakness-repair-mode.md`
- `practice/sql/business-sql-cases.md`
- `practice/sql/ctes-subqueries.md`
- `practice/sql/deduplication.md`
- `practice/sql/gaps-and-islands.md`
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

The purpose of this guide is to make the candidate strong at SQL joins in Data Engineering interviews.

The candidate should learn to answer:

```text
What join type should I use?
What rows should be preserved?
What is the denominator?
What is the join key?
Is the join one-to-one, one-to-many, many-to-one, or many-to-many?
Can the join multiply rows?
Should I aggregate before joining?
Should I deduplicate before joining?
Should I use EXISTS instead of JOIN?
Should I use NOT EXISTS instead of LEFT JOIN?
How do I find orphan records?
How do I find unmatched records?
How do I reconcile source and target tables?
How do I join fact tables safely?
How do I join a fact table to a dimension table?
How do I join to a slowly changing dimension?
How do I handle NULL join keys?
How do I validate join output?
How do I explain join performance?
```

A candidate is interview-ready only when they can:

```text
identify the grain of both tables
identify primary key and foreign key
choose correct join type
predict row count behavior
detect duplicate join keys
preserve denominator correctly
avoid join explosion
aggregate to the correct grain before joining
use LEFT JOIN for conversion denominator
use FULL OUTER JOIN for reconciliation
use EXISTS for existence checks
use NOT EXISTS for anti-joins
handle NULL join keys intentionally
join SCD intervals using as-of logic
validate row counts before and after joins
explain join impact on business metrics
```


## 2. Why Joins Matter for Data Engineers

Data Engineering work is mostly about combining data from different sources safely.

Real examples:

```text
orders joined to users for country metrics
orders joined to order_items for product metrics
events joined to users for active users by country
payments joined to orders for payment success analysis
source table joined to target table for reconciliation
facts joined to dimensions for reporting
CDC staging joined to target for MERGE
tickets joined to users for support analytics
campaigns joined to users and orders for ROI
snapshots joined to calendar tables for missing dates
orders joined to SCD user plan history using order_time
```

Joins are dangerous because:

```text
a query can run successfully but produce wrong metrics
a dimension duplicate can multiply fact rows
an INNER JOIN can drop non-converters from denominator
a LEFT JOIN filter in WHERE can accidentally become INNER JOIN
a FULL OUTER JOIN can be required to see missing records on both sides
a many-to-many join can create inflated revenue
NULL join keys can silently not match
joining two fact tables at detail grain can explode rows
```

Weak answer:

```text
I will join the tables on user_id.
```

Strong answer:

```text
I will first identify the grain and cardinality. Since users should be one row per user_id and orders is many rows per user_id, joining orders to users is many-to-one. I will validate users uniqueness before joining, use LEFT JOIN if I need to preserve all orders, and check row counts before and after the join to detect row multiplication.
```

Interview line:

```text
A join answer is not complete until the candidate explains grain, cardinality, preserved rows, and validation.
```


## 3. Core Mental Model

Every join has five critical decisions:

```text
1. Left table:
   What rows start the query?

2. Right table:
   What data is added or compared?

3. Join key:
   Which columns match rows?

4. Join type:
   Which unmatched rows are kept?

5. Cardinality:
   How many matches can each row have?
```

Join safety flow:

```text
1. Define business goal.
2. Identify table grain.
3. Identify join keys.
4. Check key uniqueness.
5. Choose join type.
6. Predict row count impact.
7. Join at correct grain.
8. Aggregate after or before join intentionally.
9. Validate row counts and duplicates.
10. Explain assumptions.
```

Core interview line:

```text
I do not choose a join type by habit. I choose it based on which rows must be preserved and what the denominator should be.
```


## 4. Join Vocabulary

Important terms:

```text
Join:
Combines rows from two tables based on a condition.

Join key:
Column or columns used to match rows.

Primary key:
Column or set of columns that uniquely identify a table row.

Foreign key:
Column in one table referencing another table's key.

Grain:
What one row represents.

Cardinality:
Relationship between rows of two tables.

One-to-one:
One row on left matches at most one row on right.

One-to-many:
One row on left matches many rows on right.

Many-to-one:
Many rows on left match one row on right.

Many-to-many:
Many rows on left can match many rows on right.

Inner join:
Keeps only matched rows.

Left join:
Keeps all left rows and matched right rows.

Right join:
Keeps all right rows. Usually can be rewritten as left join.

Full outer join:
Keeps matched and unmatched rows from both sides.

Cross join:
Every left row matched with every right row.

Semi-join:
Keeps left rows where a match exists, usually EXISTS.

Anti-join:
Keeps left rows where no match exists, usually NOT EXISTS or LEFT JOIN IS NULL.

Join explosion:
Rows multiply unexpectedly after a join.

Orphan record:
Fact row whose dimension key has no match.

As-of join:
Join fact row to dimension row active at that time.

Bridge table:
Table used to resolve many-to-many relationships.
```


## 5. Standard Answer Framework

Use this framework for every join problem:

```text
1. Restate the business question.
2. Identify left table and right table.
3. State the grain of each table.
4. Identify join key or composite join key.
5. State expected cardinality:
   - one-to-one
   - one-to-many
   - many-to-one
   - many-to-many
6. Choose join type:
   - INNER
   - LEFT
   - FULL OUTER
   - EXISTS
   - NOT EXISTS
   - CROSS
7. Explain which rows are preserved.
8. Explain whether aggregation is needed before joining.
9. Explain NULL handling.
10. Write SQL.
11. Validate:
   - row count before and after
   - duplicate join keys
   - unmatched keys
   - metric reasonableness
12. Explain edge cases and performance.
```

Short version:

```text
Goal:
Grain:
Key:
Cardinality:
Join type:
Preserved rows:
SQL:
Validation:
```

Strict rule:

```text
No join answer is strong if the candidate cannot explain cardinality and row preservation.
```


## 6. Scoring Rubric

Score each join answer from 0 to 5.

### Score 0

No meaningful SQL or join reasoning.

### Score 1

Uses JOIN randomly without explaining key or row preservation.

### Score 2

Can write simple joins but misses cardinality, duplicates, or denominator.

### Score 3

Mostly correct SQL but weak validation, NULL handling, or metric impact.

### Score 4

Interview-ready. Correct join type, grain, cardinality, SQL, and validation.

### Score 5

Strong. Handles complex joins, anti/semi joins, SCD as-of joins, many-to-many joins, fact-to-fact joins, reconciliation, join explosion, performance, and production data-quality checks.

Do not give 4+ if:

```text
candidate does not state table grain
candidate does not identify join key
candidate cannot explain join type choice
candidate ignores duplicate right-side keys
candidate cannot predict row count impact
candidate uses INNER JOIN when denominator requires LEFT JOIN
candidate filters right-side columns in WHERE after LEFT JOIN incorrectly
candidate joins two fact tables at detail grain and double counts
candidate cannot explain NULL join behavior
candidate cannot validate join output
candidate cannot explain many-to-many risk
```


## 7. Join Types Overview

### INNER JOIN

Keeps only matched rows.

```sql
SELECT *
FROM orders o
JOIN users u
  ON o.user_id = u.user_id;
```

### LEFT JOIN

Keeps all left rows, matched right rows, NULLs for unmatched right rows.

```sql
SELECT *
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id;
```

### FULL OUTER JOIN

Keeps matched rows and unmatched rows from both sides.

```sql
SELECT *
FROM source s
FULL OUTER JOIN target t
  ON s.id = t.id;
```

### CROSS JOIN

Every combination.

```sql
SELECT *
FROM stores s
CROSS JOIN dim_calendar c;
```

### EXISTS

Keeps left rows where related row exists.

```sql
SELECT *
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
);
```

### NOT EXISTS

Keeps left rows where related row does not exist.

```sql
SELECT *
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
);
```

Interview line:

```text
Join type is chosen by which rows must remain in the answer.
```


## 8. Join Cardinality

Cardinality is the most important join concept for Data Engineering.

### One-to-one

```text
users_current.user_id -> user_profile_current.user_id
```

Expected:

```text
one user row matches at most one profile row
```

### One-to-many

```text
orders.order_id -> order_items.order_id
```

One order can have many items.

### Many-to-one

```text
orders.user_id -> users.user_id
```

Many orders can belong to one user.

### Many-to-many

```text
users joined to products through purchases
orders joined to promotions if multiple promotions per order and multiple orders per promotion
```

Danger:

```text
Many-to-many joins can multiply rows and inflate metrics.
```

Cardinality check:

```sql
SELECT
  join_key,
  COUNT(*) AS row_count
FROM right_table
GROUP BY join_key
HAVING COUNT(*) > 1;
```

Interview line:

```text
Before trusting a join, I check whether the right side is unique on the join key if I expect a many-to-one join.
```


## 9. Join Row Count Predictions

Expected row count behavior:

```text
INNER JOIN:
Output rows <= possible matched combinations.
Can drop unmatched left rows.

LEFT JOIN:
Output rows >= left rows if right side has duplicate matches.
Output rows = left rows only when right side has at most one match per left row.

FULL OUTER JOIN:
Output includes all matched and unmatched rows from both sides.

CROSS JOIN:
Output rows = left row count * right row count.

EXISTS:
Output rows <= left rows.
Does not multiply left rows.

NOT EXISTS:
Output rows <= left rows.
Does not multiply left rows.
```

Validation examples:

```sql
SELECT COUNT(*) FROM orders;

SELECT COUNT(*)
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id;
```

If left join output is greater than orders count:

```text
users is not unique by user_id or join key is wrong.
```

Interview line:

```text
A LEFT JOIN can still increase row count if the right side has multiple matches.
```


## 10. Basic INNER JOIN

Business question:

```text
List completed orders with user country.
```

Tables:

```sql
orders(order_id, user_id, order_status, total_amount)
users(user_id, country)
```

SQL:

```sql
SELECT
  o.order_id,
  o.user_id,
  u.country,
  o.total_amount
FROM orders o
JOIN users u
  ON o.user_id = u.user_id
WHERE o.order_status = 'COMPLETED';
```

When INNER JOIN is correct:

```text
only want orders with known matching users
missing users should be excluded
```

When INNER JOIN is risky:

```text
you need all orders as denominator
missing user records indicate data quality issue
```

Validation:

```sql
SELECT COUNT(*) AS completed_orders
FROM orders
WHERE order_status = 'COMPLETED';

SELECT COUNT(*) AS completed_orders_with_user
FROM orders o
JOIN users u
  ON o.user_id = u.user_id
WHERE o.order_status = 'COMPLETED';
```

Interview line:

```text
INNER JOIN drops unmatched records, so I use it only when unmatched rows should be excluded.
```


## 11. Basic LEFT JOIN

Business question:

```text
List all completed orders and attach user country if available.
```

SQL:

```sql
SELECT
  o.order_id,
  o.user_id,
  COALESCE(u.country, 'UNKNOWN') AS country,
  o.total_amount
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id
WHERE o.order_status = 'COMPLETED';
```

When LEFT JOIN is correct:

```text
preserve all left rows
need to keep non-matching facts
denominator is left table
missing dimension should appear as UNKNOWN or be measured
```

Find unmatched rows:

```sql
SELECT
  o.order_id,
  o.user_id
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id
WHERE u.user_id IS NULL;
```

Interview line:

```text
LEFT JOIN is appropriate when the left table defines the denominator.
```


## 12. LEFT JOIN Filter Trap

Common mistake:

```sql
SELECT
  u.user_id,
  o.order_id
FROM users u
LEFT JOIN orders o
  ON u.user_id = o.user_id
WHERE o.order_status = 'COMPLETED';
```

Problem:

```text
The WHERE filter on o.order_status removes NULL unmatched rows.
This turns the LEFT JOIN behavior into INNER JOIN behavior.
```

Correct if preserving all users:

```sql
SELECT
  u.user_id,
  o.order_id
FROM users u
LEFT JOIN orders o
  ON u.user_id = o.user_id
 AND o.order_status = 'COMPLETED';
```

Or aggregate:

```sql
SELECT
  u.user_id,
  COUNT(o.order_id) AS completed_orders
FROM users u
LEFT JOIN orders o
  ON u.user_id = o.user_id
 AND o.order_status = 'COMPLETED'
GROUP BY u.user_id;
```

Interview line:

```text
For LEFT JOINs, filters on the right table usually belong in the ON clause if unmatched left rows must be preserved.
```


## 13. FULL OUTER JOIN

Business question:

```text
Compare source and target transactions and find missing records on either side.
```

SQL:

```sql
SELECT
  COALESCE(s.transaction_id, t.transaction_id) AS transaction_id,
  s.amount AS source_amount,
  t.amount AS target_amount,
  CASE
    WHEN s.transaction_id IS NOT NULL AND t.transaction_id IS NULL THEN 'ONLY_IN_SOURCE'
    WHEN s.transaction_id IS NULL AND t.transaction_id IS NOT NULL THEN 'ONLY_IN_TARGET'
    WHEN s.amount <> t.amount THEN 'AMOUNT_MISMATCH'
    ELSE 'MATCH'
  END AS reconciliation_status
FROM source_transactions s
FULL OUTER JOIN target_transactions t
  ON s.transaction_id = t.transaction_id;
```

Use when:

```text
you need unmatched rows from both tables
source-target reconciliation
migration validation
completeness checks
```

Interview line:

```text
FULL OUTER JOIN is the standard pattern for reconciliation because it shows missing records from both sides.
```


## 14. CROSS JOIN

CROSS JOIN creates every combination.

Business question:

```text
Create expected store-date combinations for January 2026.
```

Tables:

```sql
stores(store_id)
dim_calendar(calendar_date)
```

SQL:

```sql
SELECT
  s.store_id,
  c.calendar_date
FROM stores s
CROSS JOIN dim_calendar c
WHERE c.calendar_date >= DATE '2026-01-01'
  AND c.calendar_date <  DATE '2026-02-01';
```

Use cases:

```text
expected combinations
store-date completeness checks
user-month skeletons
calendar expansion
test data generation
```

Danger:

```text
CROSS JOIN multiplies rows.
1000 stores * 365 days = 365,000 rows.
Large dimensions can explode quickly.
```

Interview line:

```text
I use CROSS JOIN only when I intentionally need every combination, and I filter dimensions early.
```


## 15. Semi-Join with EXISTS

Business question:

```text
Find users who have at least one completed order.
```

SQL:

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

Equivalent JOIN with DISTINCT:

```sql
SELECT DISTINCT
  u.user_id,
  u.signup_at
FROM users u
JOIN orders o
  ON u.user_id = o.user_id
WHERE o.order_status = 'COMPLETED';
```

Why EXISTS can be better:

```text
does not multiply user rows
does not require DISTINCT
clearly expresses existence
```

Interview line:

```text
If I only need to know whether a related row exists, EXISTS is often safer than JOIN plus DISTINCT.
```


## 16. Anti-Join with NOT EXISTS

Business question:

```text
Find users who signed up but never placed a completed order.
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

Alternative LEFT JOIN:

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

Why NOT EXISTS is safe:

```text
avoids NOT IN NULL trap
does not multiply rows
expresses anti-match clearly
```

Interview line:

```text
For anti-joins, I usually prefer NOT EXISTS because it is NULL-safe and clear.
```


## 17. NOT IN NULL Trap

Risky query:

```sql
SELECT
  user_id
FROM users
WHERE user_id NOT IN (
  SELECT user_id
  FROM orders
);
```

Problem:

```text
If orders.user_id contains NULL, NOT IN can return unexpected results, often zero rows.
```

Safer:

```sql
SELECT
  u.user_id
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.user_id
);
```

If using NOT IN, filter NULLs:

```sql
SELECT
  user_id
FROM users
WHERE user_id NOT IN (
  SELECT user_id
  FROM orders
  WHERE user_id IS NOT NULL
);
```

Interview line:

```text
I avoid NOT IN when the subquery may contain NULLs and use NOT EXISTS instead.
```


## 18. NULL Join Keys

SQL equality does not match NULL to NULL.

Example:

```sql
SELECT *
FROM a
JOIN b
  ON a.key = b.key;
```

Rows where both keys are NULL do not match.

Important questions:

```text
Should NULL keys match?
Are NULL keys valid?
Should NULL keys be treated as unknown?
Should NULL-key rows be quarantined?
```

Usually in Data Engineering:

```text
NULL required keys are data quality issues.
Do not force-match them unless business explicitly says so.
```

Find NULL join keys:

```sql
SELECT COUNT(*) AS null_user_id_orders
FROM orders
WHERE user_id IS NULL;
```

NULL-safe join exists in some dialects.

PostgreSQL:

```sql
a.key IS NOT DISTINCT FROM b.key
```

Generic explicit pattern:

```sql
ON (
  a.key = b.key
  OR (a.key IS NULL AND b.key IS NULL)
)
```

Caution:

```text
NULL-safe joins can create unexpected matches if many NULLs exist.
```

Interview line:

```text
I do not assume NULL join keys should match; I usually treat required NULL keys as data-quality issues.
```


## 19. Composite Join Keys

Sometimes one column is not enough.

Example:

```text
inventory_snapshot should join by product_id and snapshot_date.
```

SQL:

```sql
SELECT
  i.product_id,
  i.snapshot_date,
  p.category,
  i.inventory_quantity
FROM inventory_snapshot i
JOIN products p
  ON i.product_id = p.product_id;
```

Composite example:

```sql
SELECT
  a.store_id,
  a.sales_date,
  a.sales_amount,
  b.target_amount
FROM daily_store_sales a
LEFT JOIN daily_store_targets b
  ON a.store_id = b.store_id
 AND a.sales_date = b.target_date;
```

Common composite keys:

```text
user_id + event_date
store_id + calendar_date
product_id + snapshot_date
order_id + line_item_id
account_id + month_start
metric_date + metric_name
source_system + source_id
```

Validation:

```sql
SELECT
  store_id,
  target_date,
  COUNT(*) AS row_count
FROM daily_store_targets
GROUP BY store_id, target_date
HAVING COUNT(*) > 1;
```

Interview line:

```text
Composite joins should use all columns that define the matching grain.
```


## 20. Joining Fact to Dimension

Business question:

```text
Calculate daily revenue by user country.
```

Tables:

```sql
orders(order_id, user_id, order_time, order_status, total_amount)
users(user_id, country)
```

SQL:

```sql
WITH completed_orders AS (
  SELECT
    order_id,
    user_id,
    CAST(order_time AS DATE) AS order_date,
    total_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
),
deduped_users AS (
  SELECT
    user_id,
    country
  FROM users
)
SELECT
  o.order_date,
  COALESCE(u.country, 'UNKNOWN') AS country,
  SUM(o.total_amount) AS revenue,
  COUNT(DISTINCT o.order_id) AS orders
FROM completed_orders o
LEFT JOIN deduped_users u
  ON o.user_id = u.user_id
GROUP BY
  o.order_date,
  COALESCE(u.country, 'UNKNOWN')
ORDER BY o.order_date, country;
```

Before trusting:

```sql
SELECT user_id, COUNT(*)
FROM users
GROUP BY user_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
Fact-to-dimension joins are usually many-to-one, so the dimension key should be unique.
```


## 21. Joining Order Headers to Order Items

Business question:

```text
Calculate revenue by product category.
```

Tables:

```sql
orders(order_id, order_status)
order_items(order_id, product_id, quantity, unit_price)
products(product_id, category)
```

SQL:

```sql
SELECT
  p.category,
  SUM(oi.quantity * oi.unit_price) AS revenue
FROM orders o
JOIN order_items oi
  ON o.order_id = oi.order_id
JOIN products p
  ON oi.product_id = p.product_id
WHERE o.order_status = 'COMPLETED'
GROUP BY p.category
ORDER BY revenue DESC;
```

This is correct because:

```text
Revenue is item-grain.
Joining order_items is necessary.
```

But this is dangerous for order-level metrics:

```sql
SELECT
  AVG(o.total_amount) AS avg_order_value
FROM orders o
JOIN order_items oi
  ON o.order_id = oi.order_id;
```

Why wrong:

```text
Orders with more items appear multiple times.
```

Correct AOV:

```sql
SELECT
  SUM(total_amount) * 1.0 / NULLIF(COUNT(DISTINCT order_id), 0) AS avg_order_value
FROM orders
WHERE order_status = 'COMPLETED';
```

Interview line:

```text
Joining order headers to order items changes the grain from order to item, so order-level metrics must be protected.
```


## 22. Aggregate Before Join

Business question:

```text
Calculate revenue by country.
```

If users is unique by user_id, direct join is okay.

But for safety and performance, sometimes aggregate first:

```sql
WITH user_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue,
    COUNT(DISTINCT order_id) AS orders
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
),
deduped_users AS (
  SELECT
    user_id,
    country
  FROM users
)
SELECT
  COALESCE(u.country, 'UNKNOWN') AS country,
  SUM(r.revenue) AS revenue,
  SUM(r.orders) AS orders
FROM user_revenue r
LEFT JOIN deduped_users u
  ON r.user_id = u.user_id
GROUP BY COALESCE(u.country, 'UNKNOWN');
```

Use aggregate-before-join when:

```text
joining from detailed fact to dimension
metric grain is higher than raw fact
right side may be large
you want to reduce rows before join
you need to prevent double counting
```

Interview line:

```text
Aggregating to the metric grain before joining can improve correctness and performance.
```


## 23. Join Then Aggregate

Sometimes joining before aggregation is necessary.

Example:

```text
Revenue by product category requires product category from products table.
Revenue amount is item-grain.
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

Why join first:

```text
category is needed before grouping
revenue expression uses order item rows
```

Interview line:

```text
Whether to aggregate before or after joining depends on metric grain and where the grouping attributes live.
```


## 24. Avoid Joining Two Fact Tables at Detail Grain

Problem:

```text
Join orders and payments by user_id to calculate revenue and payment amount.
```

Bad:

```sql
SELECT
  o.user_id,
  SUM(o.total_amount) AS order_revenue,
  SUM(p.amount) AS payment_amount
FROM orders o
JOIN payments p
  ON o.user_id = p.user_id
GROUP BY o.user_id;
```

Why bad:

```text
If a user has 10 orders and 5 payments, join creates 50 rows.
Both sums are inflated.
```

Correct:

```sql
WITH order_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS order_revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
),
payment_revenue AS (
  SELECT
    user_id,
    SUM(amount) AS payment_amount
  FROM payments
  WHERE payment_status = 'SUCCESS'
  GROUP BY user_id
)
SELECT
  COALESCE(o.user_id, p.user_id) AS user_id,
  o.order_revenue,
  p.payment_amount
FROM order_revenue o
FULL OUTER JOIN payment_revenue p
  ON o.user_id = p.user_id;
```

Interview line:

```text
When joining two fact tables, aggregate each fact to the common grain first.
```


## 25. Many-to-Many Joins

Many-to-many joins are dangerous unless intentionally modeled.

Example:

```text
students <-> courses
orders <-> promotions
users <-> experiments
products <-> tags
```

Usually solved with bridge table:

```sql
students(student_id)
courses(course_id)
student_courses(student_id, course_id)
```

SQL:

```sql
SELECT
  s.student_id,
  c.course_id
FROM students s
JOIN student_courses sc
  ON s.student_id = sc.student_id
JOIN courses c
  ON sc.course_id = c.course_id;
```

Danger:

```text
Joining students directly to courses without bridge logic creates invalid combinations.
```

Metric caution:

```text
Revenue by promotion can double count if an order has multiple promotions.
Need allocation rule.
```

Interview line:

```text
Many-to-many joins require a bridge table and often an allocation rule for metrics.
```


## 26. Join Explosion Detection

Join explosion means row count increases unexpectedly.

Before join:

```sql
SELECT COUNT(*) FROM orders;
```

After join:

```sql
SELECT COUNT(*)
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id;
```

If after > before:

```text
users has duplicate user_id rows
or join condition is incomplete
```

Find duplicate right keys:

```sql
SELECT
  user_id,
  COUNT(*) AS row_count
FROM users
GROUP BY user_id
HAVING COUNT(*) > 1;
```

Find affected left rows:

```sql
SELECT
  o.order_id,
  COUNT(*) AS joined_rows
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id
GROUP BY o.order_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
When row count increases unexpectedly after a many-to-one join, I check duplicate keys on the right side.
```


## 27. Deduplicate Before Join

Problem:

```text
users table has multiple rows per user_id.
Need latest user profile before joining orders.
```

SQL:

```sql
WITH ranked_users AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY updated_at DESC, ingested_at DESC
    ) AS rn
  FROM users
),
deduped_users AS (
  SELECT
    user_id,
    country,
    plan
  FROM ranked_users
  WHERE rn = 1
)
SELECT
  o.order_id,
  o.user_id,
  u.country,
  u.plan
FROM orders o
LEFT JOIN deduped_users u
  ON o.user_id = u.user_id;
```

Interview line:

```text
If the dimension is not unique at the join key, I deduplicate or select the correct snapshot before joining.
```


## 28. Orphan Records

Business question:

```text
Find orders whose user_id does not exist in users.
```

LEFT JOIN anti-join:

```sql
SELECT
  o.order_id,
  o.user_id
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id
WHERE u.user_id IS NULL;
```

NOT EXISTS:

```sql
SELECT
  o.order_id,
  o.user_id
FROM orders o
WHERE NOT EXISTS (
  SELECT 1
  FROM users u
  WHERE u.user_id = o.user_id
);
```

Exclude NULL if needed:

```sql
WHERE o.user_id IS NOT NULL
  AND NOT EXISTS (...)
```

Interview line:

```text
Orphan checks are anti-joins from fact table to dimension table.
```


## 29. Unmatched Dimension Records

Business question:

```text
Find users who have no orders.
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
);
```

Alternative:

```sql
SELECT
  u.user_id,
  u.signup_at
FROM users u
LEFT JOIN orders o
  ON u.user_id = o.user_id
WHERE o.user_id IS NULL;
```

Use cases:

```text
inactive users
products never sold
stores with no sales
campaigns with no conversions
accounts with no transactions
```

Interview line:

```text
Unmatched dimension analysis usually starts from the dimension and anti-joins to the fact.
```


## 30. Conversion Metrics with LEFT JOIN

Business question:

```text
What percentage of January signups made a purchase within 7 days?
```

Tables:

```sql
users(user_id, signup_at)
orders(order_id, user_id, order_time, order_status)
```

SQL:

```sql
WITH signup_users AS (
  SELECT
    user_id,
    signup_at
  FROM users
  WHERE signup_at >= DATE '2026-01-01'
    AND signup_at <  DATE '2026-02-01'
),
first_purchase AS (
  SELECT
    user_id,
    MIN(order_time) AS first_purchase_time
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
)
SELECT
  COUNT(*) AS signup_users,
  SUM(
    CASE
      WHEN fp.first_purchase_time >= su.signup_at
       AND fp.first_purchase_time <  su.signup_at + INTERVAL '7 days'
      THEN 1 ELSE 0
    END
  ) AS converted_users,
  SUM(
    CASE
      WHEN fp.first_purchase_time >= su.signup_at
       AND fp.first_purchase_time <  su.signup_at + INTERVAL '7 days'
      THEN 1 ELSE 0
    END
  ) * 1.0 / NULLIF(COUNT(*), 0) AS conversion_rate
FROM signup_users su
LEFT JOIN first_purchase fp
  ON su.user_id = fp.user_id;
```

Why LEFT JOIN:

```text
Denominator is all signup users, including users who never purchased.
```

Interview line:

```text
For conversion rates, use LEFT JOIN from denominator cohort to conversion events.
```


## 31. Retention Joins

Business question:

```text
Day-1 retention by signup date.
```

Tables:

```sql
users(user_id, signup_at)
events(user_id, event_time)
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
day1_retained AS (
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
  COUNT(DISTINCT r.user_id) * 1.0
    / NULLIF(COUNT(DISTINCT s.user_id), 0) AS day1_retention
FROM signup_cohort s
LEFT JOIN day1_retained r
  ON s.user_id = r.user_id
 AND s.signup_date = r.signup_date
GROUP BY s.signup_date
ORDER BY s.signup_date;
```

Interview line:

```text
Retention uses the original cohort as denominator, so the final join should preserve the cohort.
```


## 32. Funnel Joins

Business question:

```text
Find users who viewed a product and purchased within 24 hours.
```

Tables:

```sql
events(user_id, event_name, event_time)
```

SQL using EXISTS:

```sql
WITH product_views AS (
  SELECT
    user_id,
    event_time AS view_time
  FROM events
  WHERE event_name = 'product_view'
),
purchases AS (
  SELECT
    user_id,
    event_time AS purchase_time
  FROM events
  WHERE event_name = 'purchase'
)
SELECT DISTINCT
  v.user_id
FROM product_views v
WHERE EXISTS (
  SELECT 1
  FROM purchases p
  WHERE p.user_id = v.user_id
    AND p.purchase_time >= v.view_time
    AND p.purchase_time <  v.view_time + INTERVAL '24 hours'
);
```

Why EXISTS:

```text
A user may have many purchases after a view.
EXISTS avoids multiplying rows when only existence matters.
```

Interview line:

```text
For sequence existence questions, EXISTS can avoid row explosion from many event matches.
```


## 33. Source-Target Reconciliation Join

Business question:

```text
Find missing and mismatched records between source and target.
```

SQL:

```sql
WITH reconciled AS (
  SELECT
    COALESCE(s.id, t.id) AS id,
    s.amount AS source_amount,
    t.amount AS target_amount,
    CASE
      WHEN s.id IS NOT NULL AND t.id IS NULL THEN 'ONLY_IN_SOURCE'
      WHEN s.id IS NULL AND t.id IS NOT NULL THEN 'ONLY_IN_TARGET'
      WHEN s.amount <> t.amount THEN 'AMOUNT_MISMATCH'
      ELSE 'MATCH'
    END AS reconciliation_status
  FROM source_table s
  FULL OUTER JOIN target_table t
    ON s.id = t.id
)
SELECT *
FROM reconciled
WHERE reconciliation_status <> 'MATCH';
```

NULL-safe mismatch in PostgreSQL:

```sql
WHEN s.amount IS DISTINCT FROM t.amount THEN 'AMOUNT_MISMATCH'
```

Generic NULL-aware comparison:

```sql
WHEN (
  s.amount <> t.amount
  OR (s.amount IS NULL AND t.amount IS NOT NULL)
  OR (s.amount IS NOT NULL AND t.amount IS NULL)
) THEN 'AMOUNT_MISMATCH'
```

Interview line:

```text
Reconciliation joins should use FULL OUTER JOIN and NULL-aware comparisons.
```


## 34. Joining to Calendar Tables

Business question:

```text
Show daily revenue for every date, including zero-revenue dates.
```

Tables:

```sql
dim_calendar(calendar_date)
orders(order_time, order_status, total_amount)
```

SQL:

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

Why LEFT JOIN from calendar:

```text
calendar defines expected output dates
missing revenue days should show as zero
```

Interview line:

```text
When zero-activity dates must appear, start from a calendar table and left join actual metrics.
```


## 35. Joining Expected vs Actual Sets

Business question:

```text
Find missing store-date sales records.
```

Tables:

```sql
stores(store_id)
dim_calendar(calendar_date)
sales(store_id, sales_date)
```

SQL:

```sql
WITH expected_store_dates AS (
  SELECT
    s.store_id,
    c.calendar_date
  FROM stores s
  CROSS JOIN dim_calendar c
  WHERE c.calendar_date >= DATE '2026-01-01'
    AND c.calendar_date <  DATE '2026-02-01'
),
actual_store_dates AS (
  SELECT DISTINCT
    store_id,
    sales_date
  FROM sales
)
SELECT
  e.store_id,
  e.calendar_date AS missing_sales_date
FROM expected_store_dates e
LEFT JOIN actual_store_dates a
  ON e.store_id = a.store_id
 AND e.calendar_date = a.sales_date
WHERE a.sales_date IS NULL;
```

Interview line:

```text
Completeness checks often join expected combinations to actual records and filter missing actuals.
```


## 36. As-Of Join to Slowly Changing Dimension

Business question:

```text
Join each order to the user plan that was active at order_time.
```

Tables:

```sql
orders(order_id, user_id, order_time)
user_plan_history(user_id, plan, effective_from, effective_to)
```

SQL:

```sql
SELECT
  o.order_id,
  o.user_id,
  o.order_time,
  h.plan
FROM orders o
LEFT JOIN user_plan_history h
  ON o.user_id = h.user_id
 AND o.order_time >= h.effective_from
 AND (h.effective_to IS NULL OR o.order_time < h.effective_to);
```

Important assumption:

```text
Intervals are half-open: [effective_from, effective_to)
```

Validation for duplicate matches:

```sql
SELECT
  o.order_id,
  COUNT(*) AS matching_history_rows
FROM orders o
LEFT JOIN user_plan_history h
  ON o.user_id = h.user_id
 AND o.order_time >= h.effective_from
 AND (h.effective_to IS NULL OR o.order_time < h.effective_to)
GROUP BY o.order_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
As-of joins require non-overlapping effective intervals for each entity.
```


## 37. Detect SCD Join Problems

Common problems:

```text
multiple dimension rows match one fact row
no dimension row matches a fact row
overlapping effective intervals
gaps in dimension history
wrong inclusive/exclusive boundary
```

Find multiple matches:

```sql
SELECT
  o.order_id,
  COUNT(*) AS matches
FROM orders o
JOIN user_plan_history h
  ON o.user_id = h.user_id
 AND o.order_time >= h.effective_from
 AND (h.effective_to IS NULL OR o.order_time < h.effective_to)
GROUP BY o.order_id
HAVING COUNT(*) > 1;
```

Find no matches:

```sql
SELECT
  o.order_id,
  o.user_id,
  o.order_time
FROM orders o
LEFT JOIN user_plan_history h
  ON o.user_id = h.user_id
 AND o.order_time >= h.effective_from
 AND (h.effective_to IS NULL OR o.order_time < h.effective_to)
WHERE h.user_id IS NULL;
```

Interview line:

```text
For SCD joins, I validate both duplicate matches and missing matches.
```


## 38. Self Join

A self join joins a table to itself.

Business question:

```text
Find employees and their managers.
```

Table:

```sql
employees(employee_id, employee_name, manager_id)
```

SQL:

```sql
SELECT
  e.employee_id,
  e.employee_name,
  m.employee_id AS manager_id,
  m.employee_name AS manager_name
FROM employees e
LEFT JOIN employees m
  ON e.manager_id = m.employee_id;
```

Use cases:

```text
hierarchies
compare current row to another row
find overlapping intervals
find pairs
manager relationships
```

Caution:

```text
Self joins can be expensive and can create many pairs.
Use clear aliases.
```

Interview line:

```text
Self joins require clear aliases because the same table plays two roles.
```


## 39. Joining Consecutive Rows with LAG Instead of Self Join

Instead of self joining a table to previous row, use LAG.

Business question:

```text
Find gap between current and previous event per user.
```

Better:

```sql
SELECT
  user_id,
  event_time,
  LAG(event_time) OVER (
    PARTITION BY user_id
    ORDER BY event_time
  ) AS previous_event_time
FROM events;
```

Self join alternative is usually more complex.

Interview line:

```text
For previous/next row comparisons, window functions are usually cleaner than self joins.
```


## 40. Non-Equi Joins

A non-equi join uses conditions other than equality.

Example:

```text
As-of join using time range.
```

SQL:

```sql
SELECT
  o.order_id,
  h.plan
FROM orders o
LEFT JOIN user_plan_history h
  ON o.user_id = h.user_id
 AND o.order_time >= h.effective_from
 AND o.order_time < h.effective_to;
```

Other examples:

```text
join events to sessions where event_time between session_start and session_end
join orders to price bands
join transactions to exchange rates effective at transaction_time
```

Caution:

```text
Non-equi joins can be expensive.
Need indexes/partitioning and careful validation.
Can match multiple rows if intervals overlap.
```

Interview line:

```text
Range joins need validation because overlapping ranges can create multiple matches.
```


## 41. Join Events to Sessions

Business question:

```text
Attach session_id to each event where event_time falls inside session interval.
```

Tables:

```sql
events(user_id, event_time)
sessions(user_id, session_id, session_start, session_end)
```

SQL:

```sql
SELECT
  e.user_id,
  e.event_time,
  s.session_id
FROM events e
LEFT JOIN sessions s
  ON e.user_id = s.user_id
 AND e.event_time >= s.session_start
 AND e.event_time <  s.session_end;
```

Validation for multiple sessions:

```sql
SELECT
  e.user_id,
  e.event_time,
  COUNT(*) AS matching_sessions
FROM events e
LEFT JOIN sessions s
  ON e.user_id = s.user_id
 AND e.event_time >= s.session_start
 AND e.event_time <  s.session_end
GROUP BY e.user_id, e.event_time
HAVING COUNT(*) > 1;
```

Interview line:

```text
Event-to-session joins are interval joins and require non-overlapping sessions per user.
```


## 42. Joining Exchange Rates

Business question:

```text
Convert transaction amount to USD using exchange rate valid at transaction date.
```

Tables:

```sql
transactions(transaction_id, currency, amount, transaction_time)
exchange_rates(currency, rate_date, usd_rate)
```

If rates are daily:

```sql
SELECT
  t.transaction_id,
  t.amount,
  t.currency,
  r.usd_rate,
  t.amount * r.usd_rate AS amount_usd
FROM transactions t
LEFT JOIN exchange_rates r
  ON t.currency = r.currency
 AND CAST(t.transaction_time AS DATE) = r.rate_date;
```

If rates are effective intervals:

```sql
SELECT
  t.transaction_id,
  t.amount,
  t.currency,
  r.usd_rate,
  t.amount * r.usd_rate AS amount_usd
FROM transactions t
LEFT JOIN exchange_rates_history r
  ON t.currency = r.currency
 AND t.transaction_time >= r.effective_from
 AND (r.effective_to IS NULL OR t.transaction_time < r.effective_to);
```

Validation:

```text
Check missing rates and duplicate matching rates.
```

Interview line:

```text
Currency joins require date/effective-time alignment and missing-rate handling.
```


## 43. Join with Pre-Aggregated Metrics

Business question:

```text
Show each user with completed order count and support ticket count.
```

Bad detail-grain join:

```sql
SELECT
  u.user_id,
  COUNT(o.order_id) AS orders,
  COUNT(t.ticket_id) AS tickets
FROM users u
LEFT JOIN orders o
  ON u.user_id = o.user_id
LEFT JOIN tickets t
  ON u.user_id = t.user_id
GROUP BY u.user_id;
```

Why bad:

```text
If a user has 3 orders and 2 tickets, join creates 6 rows.
Counts become inflated.
```

Correct:

```sql
WITH order_counts AS (
  SELECT
    user_id,
    COUNT(DISTINCT order_id) AS completed_orders
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
),
ticket_counts AS (
  SELECT
    user_id,
    COUNT(DISTINCT ticket_id) AS tickets
  FROM tickets
  GROUP BY user_id
)
SELECT
  u.user_id,
  COALESCE(o.completed_orders, 0) AS completed_orders,
  COALESCE(t.tickets, 0) AS tickets
FROM users u
LEFT JOIN order_counts o
  ON u.user_id = o.user_id
LEFT JOIN ticket_counts t
  ON u.user_id = t.user_id;
```

Interview line:

```text
When joining multiple one-to-many facts to a dimension, aggregate each fact first to the dimension grain.
```


## 44. Join for Campaign ROI

Business question:

```text
Calculate campaign spend, acquired users, and revenue.
```

Tables:

```sql
campaigns(campaign_id, spend)
users(user_id, campaign_id)
orders(order_id, user_id, order_status, total_amount)
```

SQL:

```sql
WITH campaign_users AS (
  SELECT
    campaign_id,
    COUNT(DISTINCT user_id) AS acquired_users
  FROM users
  WHERE campaign_id IS NOT NULL
  GROUP BY campaign_id
),
campaign_revenue AS (
  SELECT
    u.campaign_id,
    SUM(o.total_amount) AS revenue,
    COUNT(DISTINCT o.order_id) AS orders
  FROM users u
  JOIN orders o
    ON u.user_id = o.user_id
  WHERE u.campaign_id IS NOT NULL
    AND o.order_status = 'COMPLETED'
  GROUP BY u.campaign_id
)
SELECT
  c.campaign_id,
  c.spend,
  COALESCE(cu.acquired_users, 0) AS acquired_users,
  COALESCE(cr.revenue, 0) AS revenue,
  (COALESCE(cr.revenue, 0) - c.spend) * 1.0 / NULLIF(c.spend, 0) AS roi
FROM campaigns c
LEFT JOIN campaign_users cu
  ON c.campaign_id = cu.campaign_id
LEFT JOIN campaign_revenue cr
  ON c.campaign_id = cr.campaign_id;
```

Interview line:

```text
For campaign metrics, aggregate user and revenue facts separately before joining to campaign grain.
```


## 45. Join for Product Attach Rate

Business question:

```text
What percentage of completed orders include an add-on product?
```

Tables:

```sql
orders(order_id, order_status)
order_items(order_id, product_id)
products(product_id, is_addon)
```

SQL:

```sql
WITH order_flags AS (
  SELECT
    o.order_id,
    MAX(CASE WHEN p.is_addon = true THEN 1 ELSE 0 END) AS has_addon
  FROM orders o
  JOIN order_items oi
    ON o.order_id = oi.order_id
  JOIN products p
    ON oi.product_id = p.product_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY o.order_id
)
SELECT
  COUNT(*) AS completed_orders,
  SUM(has_addon) AS orders_with_addon,
  SUM(has_addon) * 1.0 / NULLIF(COUNT(*), 0) AS addon_attach_rate
FROM order_flags;
```

Why order_flags:

```text
The metric is order-level, but order_items is item-level.
Collapse to order grain first.
```

Interview line:

```text
When a join moves to lower grain, create flags at the target grain before calculating rates.
```


## 46. Join for Product Category Revenue Share

Business question:

```text
Calculate revenue share by product category.
```

SQL:

```sql
WITH category_revenue AS (
  SELECT
    p.category,
    SUM(oi.quantity * oi.unit_price) AS revenue
  FROM orders o
  JOIN order_items oi
    ON o.order_id = oi.order_id
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

Interview line:

```text
Item-level category revenue is safe to calculate after joining order_items to products because the metric is category-item revenue.
```


## 47. Join for Orders Without Payments

Business question:

```text
Find completed orders without successful payment.
```

NOT EXISTS:

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

LEFT JOIN version:

```sql
SELECT
  o.order_id,
  o.user_id,
  o.order_time
FROM orders o
LEFT JOIN payments p
  ON o.order_id = p.order_id
 AND p.payment_status = 'SUCCESS'
WHERE o.order_status = 'COMPLETED'
  AND p.order_id IS NULL;
```

Interview line:

```text
Missing related records are anti-join problems.
```


## 48. Join for Products Never Sold

Business question:

```text
Find active products that never appeared in completed orders.
```

SQL:

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

Alternative:

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
  p.product_id,
  p.category
FROM products p
LEFT JOIN sold_products s
  ON p.product_id = s.product_id
WHERE p.is_active = true
  AND s.product_id IS NULL;
```

Interview line:

```text
Products never sold is a dimension anti-join against a distinct sold-product set.
```


## 49. Join for Latest Record from History

Business question:

```text
Join orders to latest user profile, not historical as-of profile.
```

Tables:

```sql
orders(order_id, user_id)
user_profile_history(user_id, country, plan, updated_at)
```

SQL:

```sql
WITH ranked_profiles AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY updated_at DESC
    ) AS rn
  FROM user_profile_history
),
current_profile AS (
  SELECT
    user_id,
    country,
    plan
  FROM ranked_profiles
  WHERE rn = 1
)
SELECT
  o.order_id,
  o.user_id,
  p.country,
  p.plan
FROM orders o
LEFT JOIN current_profile p
  ON o.user_id = p.user_id;
```

Important distinction:

```text
Latest profile is not the same as profile active at order time.
Use as-of join if historical correctness is required.
```

Interview line:

```text
Current dimension joins and as-of historical joins answer different business questions.
```


## 50. Join for Current Snapshot from SCD

Business question:

```text
Join orders to current user profile where is_current = true.
```

SQL:

```sql
WITH current_profile AS (
  SELECT
    user_id,
    country,
    plan
  FROM user_profile_history
  WHERE is_current = true
)
SELECT
  o.order_id,
  o.user_id,
  p.country,
  p.plan
FROM orders o
LEFT JOIN current_profile p
  ON o.user_id = p.user_id;
```

Validation:

```sql
SELECT
  user_id,
  COUNT(*) AS current_rows
FROM user_profile_history
WHERE is_current = true
GROUP BY user_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
If using is_current, validate that there is only one current row per entity.
```


## 51. Join for As-Of Price

Business question:

```text
Join order items to product price active at order time.
```

Tables:

```sql
order_items(order_id, product_id, quantity)
orders(order_id, order_time)
product_price_history(product_id, price, effective_from, effective_to)
```

SQL:

```sql
SELECT
  oi.order_id,
  oi.product_id,
  oi.quantity,
  p.price,
  oi.quantity * p.price AS item_revenue
FROM order_items oi
JOIN orders o
  ON oi.order_id = o.order_id
LEFT JOIN product_price_history p
  ON oi.product_id = p.product_id
 AND o.order_time >= p.effective_from
 AND (p.effective_to IS NULL OR o.order_time < p.effective_to);
```

Validation:

```sql
SELECT
  oi.order_id,
  oi.product_id,
  COUNT(*) AS matching_prices
FROM order_items oi
JOIN orders o
  ON oi.order_id = o.order_id
LEFT JOIN product_price_history p
  ON oi.product_id = p.product_id
 AND o.order_time >= p.effective_from
 AND (p.effective_to IS NULL OR o.order_time < p.effective_to)
GROUP BY oi.order_id, oi.product_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
As-of price joins require one valid price interval per product at the order time.
```


## 52. Join with Date Ranges

Business question:

```text
Attach campaign to order if order happened during campaign active window.
```

Tables:

```sql
orders(order_id, order_time)
campaigns(campaign_id, start_time, end_time)
```

SQL:

```sql
SELECT
  o.order_id,
  c.campaign_id
FROM orders o
LEFT JOIN campaigns c
  ON o.order_time >= c.start_time
 AND o.order_time <  c.end_time;
```

Danger:

```text
If multiple campaigns overlap, one order can match multiple campaigns.
Need attribution rule.
```

Validation:

```sql
SELECT
  o.order_id,
  COUNT(*) AS matching_campaigns
FROM orders o
LEFT JOIN campaigns c
  ON o.order_time >= c.start_time
 AND o.order_time <  c.end_time
GROUP BY o.order_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
Range joins can create multiple matches when intervals overlap, so attribution rules are required.
```


## 53. Join with Bridge Table

Business question:

```text
Calculate revenue by product tag.
Products can have multiple tags.
```

Tables:

```sql
order_items(order_id, product_id, quantity, unit_price)
product_tags(product_id, tag_id)
tags(tag_id, tag_name)
```

SQL:

```sql
SELECT
  t.tag_name,
  SUM(oi.quantity * oi.unit_price) AS attributed_revenue
FROM order_items oi
JOIN product_tags pt
  ON oi.product_id = pt.product_id
JOIN tags t
  ON pt.tag_id = t.tag_id
GROUP BY t.tag_name;
```

Caution:

```text
If a product has multiple tags, revenue is counted once per tag.
This is attributed revenue, not total revenue.
Need allocation if revenue shares must sum to total.
```

Allocation example:

```sql
WITH tag_counts AS (
  SELECT
    product_id,
    COUNT(*) AS tag_count
  FROM product_tags
  GROUP BY product_id
)
SELECT
  t.tag_name,
  SUM(oi.quantity * oi.unit_price / tc.tag_count) AS allocated_revenue
FROM order_items oi
JOIN product_tags pt
  ON oi.product_id = pt.product_id
JOIN tag_counts tc
  ON oi.product_id = tc.product_id
JOIN tags t
  ON pt.tag_id = t.tag_id
GROUP BY t.tag_name;
```

Interview line:

```text
Bridge-table joins can intentionally multiply rows, so metric allocation must be defined.
```


## 54. Join for Experiment Analysis

Business question:

```text
Calculate conversion rate by experiment variant.
```

Tables:

```sql
experiment_assignments(user_id, experiment_id, variant, assigned_at)
orders(user_id, order_time, order_status)
```

SQL:

```sql
WITH assignments AS (
  SELECT
    user_id,
    variant,
    assigned_at
  FROM experiment_assignments
  WHERE experiment_id = 'checkout_test'
),
user_conversion AS (
  SELECT
    a.user_id,
    a.variant,
    CASE
      WHEN EXISTS (
        SELECT 1
        FROM orders o
        WHERE o.user_id = a.user_id
          AND o.order_status = 'COMPLETED'
          AND o.order_time >= a.assigned_at
          AND o.order_time <  a.assigned_at + INTERVAL '7 days'
      )
      THEN 1 ELSE 0
    END AS converted
  FROM assignments a
)
SELECT
  variant,
  COUNT(*) AS assigned_users,
  SUM(converted) AS converted_users,
  SUM(converted) * 1.0 / NULLIF(COUNT(*), 0) AS conversion_rate
FROM user_conversion
GROUP BY variant;
```

Validation:

```text
Check one assignment per user per experiment.
```

SQL:

```sql
SELECT
  user_id,
  experiment_id,
  COUNT(*) AS assignments
FROM experiment_assignments
GROUP BY user_id, experiment_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
Experiment joins require assignment uniqueness and conversion events after assignment time.
```


## 55. Join for First-Touch Attribution

Business question:

```text
Attribute each user to their first campaign touch.
```

Tables:

```sql
campaign_touches(user_id, campaign_id, touch_time)
orders(user_id, order_time, total_amount)
```

SQL:

```sql
WITH ranked_touches AS (
  SELECT
    user_id,
    campaign_id,
    touch_time,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY touch_time, campaign_id
    ) AS rn
  FROM campaign_touches
),
first_touch AS (
  SELECT
    user_id,
    campaign_id,
    touch_time
  FROM ranked_touches
  WHERE rn = 1
),
user_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
)
SELECT
  f.campaign_id,
  COUNT(DISTINCT f.user_id) AS attributed_users,
  SUM(COALESCE(r.revenue, 0)) AS revenue
FROM first_touch f
LEFT JOIN user_revenue r
  ON f.user_id = r.user_id
GROUP BY f.campaign_id;
```

Interview line:

```text
Attribution joins require choosing the attribution row first, then joining metrics at user grain.
```


## 56. Join for Last-Touch Attribution

Business question:

```text
Attribute each order to the most recent campaign touch before order time.
```

Tables:

```sql
campaign_touches(user_id, campaign_id, touch_time)
orders(order_id, user_id, order_time, total_amount)
```

SQL:

```sql
WITH candidate_touches AS (
  SELECT
    o.order_id,
    o.user_id,
    o.order_time,
    o.total_amount,
    c.campaign_id,
    c.touch_time,
    ROW_NUMBER() OVER (
      PARTITION BY o.order_id
      ORDER BY c.touch_time DESC, c.campaign_id
    ) AS rn
  FROM orders o
  LEFT JOIN campaign_touches c
    ON o.user_id = c.user_id
   AND c.touch_time <= o.order_time
  WHERE o.order_status = 'COMPLETED'
)
SELECT
  order_id,
  user_id,
  order_time,
  total_amount,
  campaign_id
FROM candidate_touches
WHERE rn = 1;
```

Caution:

```text
If no touch exists, campaign_id will be NULL if LEFT JOIN preserved the order.
```

Interview line:

```text
Last-touch attribution is a range join plus ROW_NUMBER to choose the closest prior touch.
```


## 57. Join for Nearest Prior Record

Generic pattern:

```text
For each fact row, attach the latest dimension/event row before fact time.
```

SQL:

```sql
WITH candidates AS (
  SELECT
    f.fact_id,
    f.entity_id,
    f.fact_time,
    d.dimension_value,
    d.effective_time,
    ROW_NUMBER() OVER (
      PARTITION BY f.fact_id
      ORDER BY d.effective_time DESC
    ) AS rn
  FROM fact_table f
  LEFT JOIN dimension_events d
    ON f.entity_id = d.entity_id
   AND d.effective_time <= f.fact_time
)
SELECT *
FROM candidates
WHERE rn = 1;
```

Use cases:

```text
latest campaign touch before purchase
latest known location before event
latest risk score before transaction
latest account state before payment
```

Interview line:

```text
Nearest-prior joins use a range condition and ranking candidates per fact row.
```


## 58. Join for Latest Event After Trigger

Business question:

```text
For each signup, find first purchase after signup.
```

SQL:

```sql
WITH candidates AS (
  SELECT
    u.user_id,
    u.signup_at,
    o.order_id,
    o.order_time,
    ROW_NUMBER() OVER (
      PARTITION BY u.user_id
      ORDER BY o.order_time, o.order_id
    ) AS rn
  FROM users u
  LEFT JOIN orders o
    ON u.user_id = o.user_id
   AND o.order_status = 'COMPLETED'
   AND o.order_time >= u.signup_at
)
SELECT
  user_id,
  signup_at,
  order_id AS first_order_after_signup,
  order_time AS first_purchase_time
FROM candidates
WHERE rn = 1;
```

Caution:

```text
If no order exists, ROW_NUMBER still gives rn = 1 on NULL order fields in many databases because of LEFT JOIN output.
Handle converted flag separately if needed.
```

Interview line:

```text
First-after-trigger joins require preserving the trigger entity and ranking matching future events.
```


## 59. Join for Duplicate Detection Across Tables

Business question:

```text
Find records that appear in both source A and source B by natural key.
```

SQL:

```sql
SELECT
  a.business_key,
  a.source_value,
  b.source_value
FROM source_a a
JOIN source_b b
  ON a.business_key = b.business_key;
```

If both sources can have duplicates:

```sql
WITH a_keys AS (
  SELECT
    business_key,
    COUNT(*) AS a_count
  FROM source_a
  GROUP BY business_key
),
b_keys AS (
  SELECT
    business_key,
    COUNT(*) AS b_count
  FROM source_b
  GROUP BY business_key
)
SELECT
  COALESCE(a.business_key, b.business_key) AS business_key,
  a.a_count,
  b.b_count
FROM a_keys a
FULL OUTER JOIN b_keys b
  ON a.business_key = b.business_key
WHERE COALESCE(a.a_count, 0) > 1
   OR COALESCE(b.b_count, 0) > 1;
```

Interview line:

```text
When both sides can have duplicate keys, compare key-level counts before joining raw rows.
```


## 60. Join for Data Quality Summary

Business question:

```text
Summarize orders with missing users by day.
```

SQL:

```sql
SELECT
  CAST(o.order_time AS DATE) AS order_date,
  COUNT(*) AS total_orders,
  SUM(CASE WHEN u.user_id IS NULL THEN 1 ELSE 0 END) AS orders_missing_user,
  SUM(CASE WHEN u.user_id IS NULL THEN 1 ELSE 0 END) * 1.0
    / NULLIF(COUNT(*), 0) AS missing_user_rate
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id
GROUP BY CAST(o.order_time AS DATE)
ORDER BY order_date;
```

Interview line:

```text
Data quality join checks should report both counts and rates.
```


## 61. Join Performance Basics

Common join performance factors:

```text
input table size
join key cardinality
data distribution/skew
indexes
partition pruning
clustering/sorting
broadcast vs shuffle join
filter selectivity
statistics
join order
number of selected columns
```

General tips:

```text
filter early
select only needed columns
aggregate before join when possible
deduplicate dimension before join
avoid functions on join keys if they prevent index use
avoid joining raw fact tables unnecessarily
use partition/date filters
check execution plan
handle skewed keys
```

Bad:

```sql
ON LOWER(a.email) = LOWER(b.email)
```

Potential issue:

```text
function on join key may prevent index usage
```

Better:

```text
store normalized_email column
join on normalized_email
```

Interview line:

```text
For performance, I reduce data to the needed grain and filter early before joining large tables.
```


## 62. Broadcast vs Shuffle Join Concept

In distributed systems, joins often use:

```text
Broadcast join:
Small table copied to all workers.

Shuffle join:
Both tables redistributed by join key.

Sort-merge join:
Data sorted by join key and merged.

Hash join:
Hash table built on one side and probed by other side.
```

Interview-safe explanation:

```text
If one table is small, broadcasting it can avoid expensive shuffling. If both are large, the engine may shuffle by join key. Skewed keys can make some partitions much heavier than others.
```

Data Engineering relevance:

```text
large fact table joined to small dimension often benefits from broadcast
large fact to large fact join requires careful aggregation/filtering first
skewed keys like NULL or UNKNOWN can cause performance issues
```

Interview line:

```text
In distributed warehouses, I avoid large detail-grain joins when pre-aggregation can reduce shuffle volume.
```


## 63. Join Key Data Type Mismatch

Problem:

```text
orders.user_id is integer
users.user_id is string
```

Bad:

```sql
ON CAST(o.user_id AS VARCHAR) = u.user_id
```

Issues:

```text
can hurt performance
can hide bad data
can prevent index usage
can fail for invalid casts
```

Better:

```text
standardize data types in staging
validate invalid keys
join on clean typed columns
```

Validation:

```sql
SELECT user_id
FROM raw_users
WHERE user_id IS NOT NULL
  AND user_id !~ '^[0-9]+$';
```

Dialect note:

```text
regex syntax differs.
```

Interview line:

```text
Join keys should be standardized in staging instead of repeatedly casting during joins.
```


## 64. Join Key Normalization

Common normalization:

```text
trim whitespace
lowercase emails
standardize phone format
remove leading zeros only if business-safe
standardize country codes
normalize casing
convert timestamps to same timezone
```

Example:

```sql
WITH normalized_users AS (
  SELECT
    user_id,
    LOWER(TRIM(email)) AS normalized_email
  FROM users
),
normalized_events AS (
  SELECT
    event_id,
    LOWER(TRIM(email)) AS normalized_email
  FROM events
)
SELECT *
FROM normalized_events e
LEFT JOIN normalized_users u
  ON e.normalized_email = u.normalized_email;
```

Caution:

```text
Normalization can create false matches.
Example: emails may not be stable IDs in some systems.
```

Interview line:

```text
If join keys come from messy source systems, I normalize them in staging and validate match quality.
```


## 65. Join with Duplicate Natural Keys

Problem:

```text
users table has duplicate normalized_email.
events join to users by email.
```

Danger:

```text
events can multiply when one email maps to multiple users.
```

Detect:

```sql
WITH normalized_users AS (
  SELECT
    LOWER(TRIM(email)) AS normalized_email,
    COUNT(DISTINCT user_id) AS user_count
  FROM users
  WHERE email IS NOT NULL
  GROUP BY LOWER(TRIM(email))
)
SELECT *
FROM normalized_users
WHERE user_count > 1;
```

Fix options:

```text
join by stable user_id instead
resolve duplicate identities
choose latest verified user using ROW_NUMBER
quarantine ambiguous emails
```

Interview line:

```text
Natural keys like email can be non-unique, so I validate uniqueness before joining on them.
```


## 66. Join for Slowly Changing Dimension Current vs Historical

Two different questions:

```text
Current reporting:
Join fact to current dimension row.

Historical reporting:
Join fact to dimension row active when fact occurred.
```

Current join:

```sql
SELECT
  o.order_id,
  h.plan AS current_plan
FROM orders o
LEFT JOIN user_plan_history h
  ON o.user_id = h.user_id
 AND h.is_current = true;
```

Historical as-of join:

```sql
SELECT
  o.order_id,
  h.plan AS plan_at_order_time
FROM orders o
LEFT JOIN user_plan_history h
  ON o.user_id = h.user_id
 AND o.order_time >= h.effective_from
 AND (h.effective_to IS NULL OR o.order_time < h.effective_to);
```

Interview line:

```text
Current dimension join and historical as-of join answer different business questions, so I clarify which one is required.
```


## 67. Join for Snapshot Tables

Business question:

```text
Join daily account balance to account dimension on same snapshot date.
```

Tables:

```sql
account_balance_snapshot(account_id, snapshot_date, balance)
account_status_snapshot(account_id, snapshot_date, status)
```

SQL:

```sql
SELECT
  b.account_id,
  b.snapshot_date,
  b.balance,
  s.status
FROM account_balance_snapshot b
LEFT JOIN account_status_snapshot s
  ON b.account_id = s.account_id
 AND b.snapshot_date = s.snapshot_date;
```

Validation:

```sql
SELECT
  account_id,
  snapshot_date,
  COUNT(*) AS row_count
FROM account_status_snapshot
GROUP BY account_id, snapshot_date
HAVING COUNT(*) > 1;
```

Interview line:

```text
Snapshot joins often use entity plus snapshot date as a composite key.
```


## 68. Join for Daily Active Users by Country

Business question:

```text
Calculate DAU by country.
```

Tables:

```sql
events(user_id, event_time)
users(user_id, country)
```

SQL:

```sql
WITH daily_active AS (
  SELECT DISTINCT
    user_id,
    CAST(event_time AS DATE) AS activity_date
  FROM events
  WHERE user_id IS NOT NULL
),
deduped_users AS (
  SELECT
    user_id,
    country
  FROM users
)
SELECT
  da.activity_date,
  COALESCE(u.country, 'UNKNOWN') AS country,
  COUNT(DISTINCT da.user_id) AS active_users
FROM daily_active da
LEFT JOIN deduped_users u
  ON da.user_id = u.user_id
GROUP BY
  da.activity_date,
  COALESCE(u.country, 'UNKNOWN')
ORDER BY da.activity_date, country;
```

Why daily_active CTE:

```text
Deduplicates to one row per user-day before dimension join.
```

Interview line:

```text
For DAU by dimension, deduplicate user-day first and validate the dimension key is unique.
```


## 69. Join for Monthly Active Users by Plan

Business question:

```text
Calculate MAU by current plan.
```

SQL:

```sql
WITH monthly_active AS (
  SELECT DISTINCT
    user_id,
    DATE_TRUNC('month', event_time) AS activity_month
  FROM events
  WHERE user_id IS NOT NULL
),
current_plan AS (
  SELECT
    user_id,
    plan
  FROM user_plan_history
  WHERE is_current = true
)
SELECT
  ma.activity_month,
  COALESCE(cp.plan, 'UNKNOWN') AS plan,
  COUNT(DISTINCT ma.user_id) AS mau
FROM monthly_active ma
LEFT JOIN current_plan cp
  ON ma.user_id = cp.user_id
GROUP BY
  ma.activity_month,
  COALESCE(cp.plan, 'UNKNOWN')
ORDER BY ma.activity_month, plan;
```

Potential issue:

```text
Current plan may not be historical plan during activity month.
Clarify business requirement.
```

Interview line:

```text
When joining activity to plan, clarify current plan versus plan at activity time.
```


## 70. Join with Aggregated Dimension Attributes

Business question:

```text
Find users and their most recent support ticket date.
```

Tables:

```sql
users(user_id)
tickets(ticket_id, user_id, created_at)
```

SQL:

```sql
WITH last_ticket AS (
  SELECT
    user_id,
    MAX(created_at) AS last_ticket_at,
    COUNT(DISTINCT ticket_id) AS ticket_count
  FROM tickets
  GROUP BY user_id
)
SELECT
  u.user_id,
  lt.last_ticket_at,
  COALESCE(lt.ticket_count, 0) AS ticket_count
FROM users u
LEFT JOIN last_ticket lt
  ON u.user_id = lt.user_id;
```

Why aggregate first:

```text
Need one row per user before joining to users.
```

Interview line:

```text
If I need summary attributes from a one-to-many table, I aggregate that table to one row per entity before joining.
```


## 71. Join with Window Deduped Dimension

Business question:

```text
Join events to latest known user device.
```

SQL:

```sql
WITH ranked_devices AS (
  SELECT
    user_id,
    device_type,
    updated_at,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY updated_at DESC
    ) AS rn
  FROM user_devices
),
latest_device AS (
  SELECT
    user_id,
    device_type
  FROM ranked_devices
  WHERE rn = 1
)
SELECT
  e.event_id,
  e.user_id,
  e.event_name,
  d.device_type
FROM events e
LEFT JOIN latest_device d
  ON e.user_id = d.user_id;
```

Interview line:

```text
When a dimension has multiple rows per key, select the relevant row with a window function before joining.
```


## 72. Join Debugging Checklist

When join output is wrong, check:

```text
1. Is the join key correct?
2. Are key data types same?
3. Are keys normalized?
4. Are NULL keys present?
5. Is the right table unique on join key?
6. Is the left table unique at expected grain?
7. Did the join type preserve the right rows?
8. Did a WHERE filter break LEFT JOIN behavior?
9. Did the join change the grain?
10. Did a many-to-many relationship create row explosion?
11. Was aggregation needed before joining?
12. Are there unmatched records?
13. Are there duplicate matches?
14. Are date/range boundaries correct?
15. Are SCD intervals overlapping?
16. Are metrics inflated after join?
17. Are counts before/after join reasonable?
18. Is performance affected by functions/casts on join keys?
```

Interview line:

```text
I debug joins by checking keys, cardinality, row counts, and unmatched records before looking at the final metric.
```


## 73. Join Validation Queries

### Check right-side uniqueness

```sql
SELECT
  join_key,
  COUNT(*) AS row_count
FROM right_table
GROUP BY join_key
HAVING COUNT(*) > 1;
```

### Count before and after LEFT JOIN

```sql
SELECT COUNT(*) FROM left_table;

SELECT COUNT(*)
FROM left_table l
LEFT JOIN right_table r
  ON l.join_key = r.join_key;
```

### Find unmatched left rows

```sql
SELECT l.*
FROM left_table l
LEFT JOIN right_table r
  ON l.join_key = r.join_key
WHERE r.join_key IS NULL;
```

### Find duplicate matches per left key

```sql
SELECT
  l.primary_key,
  COUNT(*) AS joined_rows
FROM left_table l
LEFT JOIN right_table r
  ON l.join_key = r.join_key
GROUP BY l.primary_key
HAVING COUNT(*) > 1;
```

### Check NULL join keys

```sql
SELECT COUNT(*)
FROM left_table
WHERE join_key IS NULL;
```

Interview line:

```text
A good join answer includes validation queries, not only the final SELECT.
```


## 74. Join Edge Cases

Common edge cases:

```text
NULL join keys
duplicate dimension keys
duplicate fact keys
wrong join key
missing dimension rows
WHERE filter turns LEFT JOIN into INNER JOIN
date truncation mismatch
timezone mismatch
case-sensitive string keys
trailing spaces in keys
numeric vs string key mismatch
leading zeros in codes
many-to-many joins
range overlap creates duplicate matches
open-ended intervals
inclusive/exclusive date boundaries
multiple current dimension rows
late arriving dimension updates
fact table has orphan rows
bridge table duplicates
multiple payment attempts
multiple order items
multiple campaign touches
```

Interview line:

```text
Most join bugs are not syntax bugs; they are grain, cardinality, and data-quality bugs.
```


## 75. Common Join Mistakes

Common mistakes:

```text
not identifying table grain
using INNER JOIN when LEFT JOIN is needed
filtering right table in WHERE after LEFT JOIN
joining fact tables at detail grain
not checking right-side duplicate keys
using COUNT(*) after one-to-many join
calculating AOV after joining order_items
using DISTINCT to hide join explosion
joining on incomplete composite key
joining on dirty natural keys without normalization
not handling NULL keys
assuming email is unique
not validating SCD interval overlaps
using current dimension when historical dimension is needed
using historical dimension when current dimension is needed
not checking unmatched records
not using FULL OUTER JOIN for reconciliation
not aggregating before joining
```

Strict feedback:

```text
This query runs, but it is not interview-ready because the LEFT JOIN filter in WHERE removes non-converting users and changes the denominator.
```


## 76. Pattern Classification Drill

Classify each prompt.

```text
1. Get completed orders with user country.
2. Keep all orders even when user is missing.
3. Find users who made at least one order.
4. Find users with no completed orders.
5. Compare source and target transactions.
6. Create store-date expected combinations.
7. Find orders missing users.
8. Calculate signup-to-purchase conversion.
9. Calculate DAU by country.
10. Join orders to order_items for category revenue.
11. Calculate AOV after joining items.
12. Join two fact tables by user_id.
13. Join order to user plan active at order_time.
14. Join events to sessions by time range.
15. Find products never sold.
16. Join campaign touches to orders for last-touch attribution.
17. Join multiple one-to-many tables to users.
18. Find missing daily records.
19. Join transactions to exchange rates by date.
20. Join product tags for revenue by tag.
```

Expected classification:

```text
1. INNER or LEFT fact-to-dimension join depending missing user handling
2. LEFT JOIN
3. EXISTS semi-join
4. NOT EXISTS anti-join
5. FULL OUTER reconciliation join
6. CROSS JOIN expected grid
7. LEFT JOIN anti-join from orders to users
8. LEFT JOIN from signup denominator
9. dedupe user-day then LEFT JOIN dimension
10. join to item grain then aggregate
11. wrong unless aggregate to order grain first
12. aggregate each fact first, then join
13. SCD/as-of range join
14. interval/range join with validation
15. NOT EXISTS or anti-join
16. range join + ROW_NUMBER
17. aggregate each one-to-many table first
18. calendar anti-join
19. equality on currency + date/effective join
20. bridge table join with allocation caution
```

Passing standard:

```text
18/20 correct before timed join mocks.
```


## 77. High-ROI Join Topics

Practice these first.

| Topic | Candidate Must Explain |
|---|---|
| INNER JOIN | matched rows only |
| LEFT JOIN | preserve left denominator |
| FULL OUTER JOIN | reconciliation |
| CROSS JOIN | expected combinations |
| EXISTS | semi-join without row multiplication |
| NOT EXISTS | anti-join and NULL safety |
| cardinality | one-to-one, one-to-many, many-to-many |
| grain | row meaning before and after join |
| join explosion | duplicate matches inflate rows |
| aggregate before join | safe fact-to-fact metrics |
| fact-to-dimension | many-to-one validation |
| order/order_items | grain shift |
| SCD as-of join | interval join |
| calendar join | zero/missing date output |
| bridge table | many-to-many with allocation |
| left join filter trap | ON vs WHERE |
| null join keys | no match unless explicitly handled |
| validation | counts, unmatched, duplicate keys |


## 78. 7-Day Joins Plan

### Day 1: Join fundamentals

Problems:

```text
INNER JOIN
LEFT JOIN
FULL OUTER JOIN
CROSS JOIN
join type explanations
```

Focus:

```text
row preservation
output row behavior
```

### Day 2: Cardinality and grain

Problems:

```text
fact-to-dimension joins
one-to-many joins
many-to-many joins
join explosion detection
right-side uniqueness checks
```

Focus:

```text
grain
cardinality
row count validation
```

### Day 3: Semi and anti joins

Problems:

```text
users with orders
users without orders
products never sold
orders without payments
orphan fact records
```

Focus:

```text
EXISTS
NOT EXISTS
LEFT JOIN IS NULL
NULL safety
```

### Day 4: Business metric joins

Problems:

```text
conversion rate
retention
DAU by country
AOV
product attach rate
campaign ROI
```

Focus:

```text
denominator
aggregation grain
left joins
```

### Day 5: Data Engineering joins

Problems:

```text
source-target reconciliation
expected vs actual records
calendar joins
SCD as-of joins
exchange rate joins
```

Focus:

```text
FULL OUTER
calendar
range joins
validation
```

### Day 6: Advanced join risks

Problems:

```text
fact-to-fact joins
bridge table allocation
last-touch attribution
interval joins
natural key duplicates
```

Focus:

```text
many-to-many
pre-aggregation
ranking after joins
```

### Day 7: Mock and repair

Tasks:

```text
Run joins mock.
Review mistakes.
Repair weakest join topic.
Update progress.
```


## 79. 30-Day Joins Plan

### Week 1: Join basics

Focus:

```text
INNER
LEFT
FULL OUTER
CROSS
EXISTS
NOT EXISTS
NULL behavior
```

Exit:

```text
Candidate can choose correct join type and explain preserved rows.
```

### Week 2: Cardinality and business metrics

Focus:

```text
grain
one-to-many
many-to-one
join explosion
AOV
conversion
retention
active users by dimension
```

Exit:

```text
Candidate can prevent double counting in metrics.
```

### Week 3: Data Engineering joins

Focus:

```text
reconciliation
orphan records
calendar joins
expected vs actual
SCD as-of joins
range joins
snapshot joins
```

Exit:

```text
Candidate can solve DE validation and warehouse join cases.
```

### Week 4: Advanced joins and mocks

Focus:

```text
fact-to-fact joins
bridge tables
attribution
exchange rates
performance
debugging
mock interviews
```

Exit:

```text
Average mock score >= 4/5.
```


## 80. Mock Set 1: Join Fundamentals

Problems:

```text
1. Explain INNER JOIN vs LEFT JOIN.
2. Write a LEFT JOIN preserving all orders.
3. Write FULL OUTER reconciliation query.
4. Use CROSS JOIN to create expected store dates.
5. Explain NULL join key behavior.
```

Expected skills:

```text
join type choice
row preservation
basic SQL syntax
NULL handling
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains which rows are preserved.
```


## 81. Mock Set 2: Cardinality and Double Counting

Problems:

```text
1. Join orders to users safely.
2. Detect duplicate user_id in users.
3. Calculate AOV without item-level duplication.
4. Join orders and tickets counts per user.
5. Explain many-to-many bridge table risk.
```

Expected skills:

```text
grain
cardinality
pre-aggregation
row count validation
join explosion detection
```

Passing standard:

```text
Average score >= 4/5.
Candidate protects metrics from row multiplication.
```


## 82. Mock Set 3: Semi/Anti/Reconciliation Joins

Problems:

```text
1. Users with completed orders.
2. Users without completed orders.
3. Products never sold.
4. Orders without successful payment.
5. Source-target reconciliation.
```

Expected skills:

```text
EXISTS
NOT EXISTS
LEFT JOIN IS NULL
FULL OUTER JOIN
NULL-aware mismatch
```

Passing standard:

```text
Average score >= 4/5.
Candidate avoids NOT IN NULL trap and uses FULL OUTER for reconciliation.
```


## 83. Mock Set 4: Advanced DE Joins

Problems:

```text
1. As-of join orders to user plan history.
2. Attach exchange rate by transaction date.
3. Join events to sessions by interval.
4. Last-touch campaign attribution.
5. Detect SCD duplicate matches.
```

Expected skills:

```text
range joins
interval boundaries
ROW_NUMBER after join
SCD validation
missing/multiple matches
```

Passing standard:

```text
Average score >= 4/5.
Candidate validates range joins for duplicate matches.
```


## 84. Timed Drill Protocol

Use this timing protocol.

### Simple join problem

```text
10-15 minutes
```

### Business metric join

```text
20-35 minutes
```

### Advanced DE join

```text
35-45 minutes
```

Per drill:

```text
Minute 0-3:
Clarify goal, grain, and denominator.

Minute 3-6:
Choose join type and cardinality expectation.

Minute 6-25:
Write SQL with CTEs if needed.

Minute 25-35:
Add validation queries.

Minute 35-45:
Explain edge cases, performance, and production risk.
```

If candidate joins immediately without explaining grain:

```text
Stop and ask for table grain and expected cardinality.
```


## 85. Review Checklist

Review join answers using:

```text
1. Did candidate restate the business goal?
2. Did candidate identify left and right tables?
3. Did candidate state grain of each table?
4. Did candidate identify join key?
5. Did candidate identify cardinality?
6. Did candidate choose correct join type?
7. Did candidate explain preserved rows?
8. Did candidate protect denominator?
9. Did candidate avoid LEFT JOIN filter trap?
10. Did candidate check duplicate right keys?
11. Did candidate avoid fact-to-fact row explosion?
12. Did candidate aggregate before joining when needed?
13. Did candidate use EXISTS for existence checks?
14. Did candidate use NOT EXISTS for anti-joins?
15. Did candidate handle NULL join keys?
16. Did candidate handle composite keys?
17. Did candidate validate row counts?
18. Did candidate find unmatched records?
19. Did candidate explain performance?
20. Did candidate explain business impact of mistakes?
```

Verdict examples:

```text
Correct syntax but wrong denominator.
Good LEFT JOIN but right filter in WHERE breaks it.
Good fact-to-dimension join but no uniqueness validation.
Good reconciliation join.
Good as-of join but no interval overlap validation.
Interview-ready.
Strong.
```


## 86. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Confuses join types | Row preservation drills |
| No grain explanation | Table grain drills |
| No cardinality | Cardinality prediction drills |
| Wrong denominator | Conversion/retention LEFT JOIN drills |
| LEFT JOIN filter trap | ON vs WHERE drills |
| Join explosion | right-key uniqueness drills |
| Fact-to-fact double count | pre-aggregation drills |
| Weak anti-join | NOT EXISTS drills |
| Weak reconciliation | FULL OUTER JOIN drills |
| NULL key confusion | NULL behavior drills |
| Composite key missing | multi-column join drills |
| SCD join weak | as-of interval drills |
| Range join duplicates | overlap validation drills |
| Performance vague | filter/aggregate before join drills |
| No validation | row count/unmatched drills |

If weakness repeats:

```text
Use weakness-repair-mode.md.
```


## 87. Communication Scripts

### Grain script

```text
Before joining, I want to identify the grain of each table because the join can change row counts and corrupt metrics.
```

### Cardinality script

```text
Orders to users should be many-to-one, so users must be unique by user_id.
```

### LEFT JOIN script

```text
I will use LEFT JOIN because the left table defines the denominator and unmatched rows must remain.
```

### INNER JOIN script

```text
I will use INNER JOIN only if unmatched rows should be excluded from the result.
```

### FULL OUTER script

```text
For reconciliation, I use FULL OUTER JOIN so missing records from either side are visible.
```

### EXISTS script

```text
I will use EXISTS because I only need to check if a matching row exists and I do not want row multiplication.
```

### Anti-join script

```text
I prefer NOT EXISTS for anti-join logic because it avoids NOT IN NULL issues.
```

### Join explosion script

```text
If the row count increases unexpectedly, I check duplicate join keys on the right side and incomplete join conditions.
```

### Aggregation script

```text
Since both orders and tickets are one-to-many per user, I aggregate each to user grain before joining them.
```

### SCD script

```text
For historical correctness, I join using the fact timestamp between effective_from and effective_to, then validate one match per fact.
```


## 88. Candidate Self-Review Questions

After every join problem, candidate should answer:

```text
1. What is the business goal?
2. What is the left table?
3. What is the right table?
4. What is the grain of each table?
5. What is the join key?
6. Is the join key unique on either side?
7. What is the expected cardinality?
8. What join type preserves the correct rows?
9. What is the denominator?
10. Can this join multiply rows?
11. Should I aggregate before joining?
12. Should I deduplicate before joining?
13. Should this be EXISTS instead of JOIN?
14. Should this be NOT EXISTS instead of LEFT JOIN?
15. Are NULL join keys possible?
16. Is the join key composite?
17. Are date/range boundaries needed?
18. How do I validate unmatched rows?
19. How do I validate duplicate matches?
20. What business metric could be wrong if the join is wrong?
```

If candidate cannot answer these:

```text
The join solution is not interview-ready.
```


## 89. Maintenance Drills

After completing joins, maintain skill with:

```text
1 join type drill per week
1 cardinality/row count drill per week
1 anti/semi join drill per week
1 business metric join drill every 2 weeks
1 SCD/range join drill every 2 weeks
1 full join mock every month
```

Maintenance rotation:

```text
Week 1: INNER/LEFT/FULL/CROSS basics
Week 2: cardinality and double counting
Week 3: EXISTS/NOT EXISTS/reconciliation
Week 4: SCD/range/attribution/performance
```

If score drops below 4:

```text
Run weakness-repair-mode.md for failed topic.
```


## 90. Progress Tracking Template

Use this progress format.

```text
# SQL Joins Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

INNER JOIN:
LEFT JOIN:
FULL OUTER JOIN:
CROSS JOIN:
EXISTS:
NOT EXISTS:
NULL join keys:
Composite keys:
Grain identification:
Cardinality:
Join type choice:
Row preservation:
Left join filter trap:
Join explosion:
Deduplicate before join:
Aggregate before join:
Fact-to-dimension joins:
Fact-to-fact joins:
Order/order_items:
Calendar joins:
Reconciliation:
Orphan records:
SCD as-of joins:
Range joins:
Bridge tables:
Attribution joins:
Validation:
Performance:
Communication:

## Repeated Mistakes

-

## Repair Items

-

## Next Practice

Today:
This week:
Next mock:
```


## 91. Final Exit Test

Candidate passes SQL joins when they can solve/explain:

```text
1. INNER JOIN matched rows.
2. LEFT JOIN preserving denominator.
3. LEFT JOIN filter trap.
4. FULL OUTER JOIN reconciliation.
5. CROSS JOIN expected combinations.
6. EXISTS semi-join.
7. NOT EXISTS anti-join.
8. NOT IN NULL trap.
9. NULL join key behavior.
10. Composite join keys.
11. Join cardinality.
12. Join row count prediction.
13. Duplicate right-side key detection.
14. Join explosion debugging.
15. Deduplicate before join.
16. Fact-to-dimension join.
17. Order header to order items join.
18. AOV without double counting.
19. Fact-to-fact pre-aggregation.
20. Many-to-many bridge table join.
21. Orphan fact records.
22. Unmatched dimension records.
23. Conversion metric with LEFT JOIN.
24. Retention join preserving cohort.
25. Source-target reconciliation.
26. Calendar join for zero dates.
27. Expected vs actual completeness join.
28. SCD as-of join.
29. SCD duplicate match validation.
30. Range join to sessions.
31. Exchange rate date join.
32. Campaign ROI join.
33. Product attach rate join.
34. Last-touch attribution join.
35. Join performance reasoning.
```

Passing standard:

```text
Average score >= 4/5.
No wrong denominator.
No unvalidated many-to-one joins.
No blind joins without grain.
No fact-to-fact double counting.
No missing row count validation.
Can connect joins to business metric correctness.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles SCD joins, reconciliation, many-to-many allocation, attribution, performance, NULLs, and join debugging clearly under pressure.
```


## 92. Final Summary

SQL joins are one of the most important interview areas for Data Engineering roles.

They map directly to:

```text
warehouse transformations
fact-to-dimension modeling
business metrics
dashboard tables
data marts
source-target reconciliation
data-quality checks
orphan detection
expected-vs-actual completeness
SCD historical reporting
calendar-based reporting
campaign attribution
fact-to-fact metric integration
bridge table modeling
pipeline debugging
```

The candidate must master:

```text
INNER JOIN
LEFT JOIN
FULL OUTER JOIN
CROSS JOIN
EXISTS
NOT EXISTS
NULL join behavior
composite keys
grain
cardinality
row preservation
join explosion
deduplication before join
aggregation before join
fact-to-dimension joins
fact-to-fact joins
many-to-many bridges
reconciliation joins
calendar joins
SCD as-of joins
range joins
attribution joins
join validation
performance reasoning
```

The mentor must be strict:

```text
No grain explanation → not interview-ready.
No cardinality explanation → not interview-ready.
Wrong denominator → not interview-ready.
LEFT JOIN filter trap → not interview-ready.
Fact-to-fact double count → not interview-ready.
No row count validation → not interview-ready.
No duplicate key check → not interview-ready.
```

The goal is not just to write `JOIN`.

The goal is to combine tables safely without corrupting row counts, denominators, or business metrics.


## 93. Problem Card Appendix

### Card 1: INNER JOIN

Topic:

```text
matched rows
```

Core idea:

```text
Keep only rows with matches.
```

Data Engineering connection:

```text
Dimension filtering.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: LEFT JOIN

Topic:

```text
preserve left
```

Core idea:

```text
Keep all denominator rows.
```

Data Engineering connection:

```text
Conversion/retention.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: FULL OUTER JOIN

Topic:

```text
both sides
```

Core idea:

```text
Find missing on either side.
```

Data Engineering connection:

```text
Reconciliation.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: CROSS JOIN

Topic:

```text
all combinations
```

Core idea:

```text
Create expected grid.
```

Data Engineering connection:

```text
Completeness checks.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
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
Check related row existence.
```

Data Engineering connection:

```text
Users with orders.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
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
Find missing related rows.
```

Data Engineering connection:

```text
Orphan checks.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Composite Key Join

Topic:

```text
multi-column
```

Core idea:

```text
Match on entity/date.
```

Data Engineering connection:

```text
Snapshots.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Fact-Dimension Join

Topic:

```text
many-to-one
```

Core idea:

```text
Attach dimension attributes.
```

Data Engineering connection:

```text
Data marts.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Order-Item Join

Topic:

```text
one-to-many
```

Core idea:

```text
Move to item grain.
```

Data Engineering connection:

```text
Product analytics.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Fact-to-Fact Join

Topic:

```text
pre-aggregate
```

Core idea:

```text
Avoid many-to-many explosion.
```

Data Engineering connection:

```text
User metrics.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Bridge Join

Topic:

```text
many-to-many
```

Core idea:

```text
Connect entities with bridge.
```

Data Engineering connection:

```text
Tags/promotions.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: SCD As-Of Join

Topic:

```text
range join
```

Core idea:

```text
Join fact to historical dimension.
```

Data Engineering connection:

```text
Warehouse reporting.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Calendar Join

Topic:

```text
expected dates
```

Core idea:

```text
Keep zero/missing dates.
```

Data Engineering connection:

```text
Dashboards.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Orphan Check

Topic:

```text
anti-join
```

Core idea:

```text
Find fact rows missing dimension.
```

Data Engineering connection:

```text
Data quality.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Join Explosion

Topic:

```text
duplicate right keys
```

Core idea:

```text
Detect inflated rows.
```

Data Engineering connection:

```text
Debugging.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Attribution Join

Topic:

```text
range + rank
```

Core idea:

```text
Choose touch event.
```

Data Engineering connection:

```text
Marketing analytics.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Exchange Rate Join

Topic:

```text
date/range
```

Core idea:

```text
Convert currency.
```

Data Engineering connection:

```text
Finance data.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Session Interval Join

Topic:

```text
time range
```

Core idea:

```text
Attach events to sessions.
```

Data Engineering connection:

```text
Clickstream.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Natural Key Join

Topic:

```text
normalization
```

Core idea:

```text
Join email/code carefully.
```

Data Engineering connection:

```text
Source integration.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Validation

Topic:

```text
counts/unmatched
```

Core idea:

```text
Trust but verify join output.
```

Data Engineering connection:

```text
Production reliability.
```

Candidate must be able to explain:

```text
1. Left table and right table.
2. Grain of each table.
3. Join key.
4. Expected cardinality.
5. Preserved rows.
6. SQL pattern.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 94. Data Engineering Scenario Appendix

### Scenario 1: Orders by Country

Pattern:

```text
fact-to-dimension
```

Task:

```text
Join orders to users and avoid duplicate user keys.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: Signup Conversion

Pattern:

```text
LEFT JOIN denominator
```

Task:

```text
Preserve all signup users.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: Source Migration Check

Pattern:

```text
FULL OUTER JOIN
```

Task:

```text
Find missing and mismatched records.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: Daily Revenue Calendar

Pattern:

```text
calendar LEFT JOIN
```

Task:

```text
Show zero revenue dates.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: Orders Missing Users

Pattern:

```text
anti-join
```

Task:

```text
Find orphan order facts.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: Products Never Sold

Pattern:

```text
NOT EXISTS
```

Task:

```text
Find unsold dimension rows.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: AOV Bug

Pattern:

```text
grain shift
```

Task:

```text
Fix order_items join double counting.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: User Metrics

Pattern:

```text
fact pre-aggregation
```

Task:

```text
Join order and ticket counts safely.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: Current Profile Join

Pattern:

```text
dedupe dimension
```

Task:

```text
Join latest user profile.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: Historical Plan Join

Pattern:

```text
SCD as-of
```

Task:

```text
Join fact to active dimension interval.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: Exchange Rate Join

Pattern:

```text
date join
```

Task:

```text
Attach rate for transaction date.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Last-Touch Attribution

Pattern:

```text
range join + rank
```

Task:

```text
Choose latest campaign touch before order.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: Bridge Table Revenue

Pattern:

```text
many-to-many
```

Task:

```text
Explain allocation by tag.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Join Explosion Debug

Pattern:

```text
cardinality validation
```

Task:

```text
Find duplicate right-side keys.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: Expected Store Dates

Pattern:

```text
CROSS JOIN + anti-join
```

Task:

```text
Find missing store-day data.
```

Minimum expected answer:

```text
1. Identify grain.
2. Choose join type.
3. Explain preserved rows.
4. Write SQL or pseudocode.
5. Validate row count/unmatched/duplicates.
6. Explain business metric impact.
```

Passing score:

```text
4/5 or higher.
```


## 95. Drill Appendix

### Drill 1: Join Type Drill

Task:

```text
Given business question, choose INNER/LEFT/FULL/CROSS/EXISTS/NOT EXISTS.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Grain Drill

Task:

```text
State row grain before and after join.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Cardinality Drill

Task:

```text
Classify one-to-one, one-to-many, many-to-one, many-to-many.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Row Count Drill

Task:

```text
Predict whether join row count can increase/decrease.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: LEFT JOIN Trap Drill

Task:

```text
Move right-table filters from WHERE to ON.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: Duplicate Key Drill

Task:

```text
Find duplicate join keys on right table.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Join Explosion Drill

Task:

```text
Find left rows with multiple right matches.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Fact-to-Fact Drill

Task:

```text
Aggregate facts before joining.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: AOV Drill

Task:

```text
Avoid item-level duplication.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: EXISTS Drill

Task:

```text
Use semi-join instead of JOIN DISTINCT.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: NOT EXISTS Drill

Task:

```text
Use anti-join safely.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Reconciliation Drill

Task:

```text
Use FULL OUTER and status labels.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Calendar Drill

Task:

```text
Build expected dates and left join actuals.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: SCD Drill

Task:

```text
Join by effective interval and validate duplicate matches.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Range Join Drill

Task:

```text
Attach event to interval with boundary rules.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Bridge Drill

Task:

```text
Explain many-to-many allocation.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: NULL Drill

Task:

```text
Explain NULL join key behavior.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Natural Key Drill

Task:

```text
Normalize and validate email/code joins.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 19: Performance Drill

Task:

```text
Filter/aggregate before large joins.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 20: Validation Drill

Task:

```text
Write row count and unmatched checks.
```

Minimum passing answer:

```text
1. State grain.
2. State cardinality.
3. Choose join type.
4. Explain row preservation.
5. Provide validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 96. Quick Reference Cards

### Quick Card 1: INNER JOIN

Summary:

```text
Only matched rows remain.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 2: LEFT JOIN

Summary:

```text
All left rows remain.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 3: FULL OUTER JOIN

Summary:

```text
Rows from both sides remain.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 4: CROSS JOIN

Summary:

```text
Every combination of left and right.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 5: EXISTS

Summary:

```text
Keep left rows with at least one match.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 6: NOT EXISTS

Summary:

```text
Keep left rows with no match.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 7: Join key

Summary:

```text
Columns used to match rows.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 8: Cardinality

Summary:

```text
Expected match count relationship.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 9: Grain

Summary:

```text
What one row represents.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 10: Join explosion

Summary:

```text
Unexpected row multiplication.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 11: Fact-to-fact

Summary:

```text
Aggregate to common grain first.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 12: SCD as-of

Summary:

```text
Join fact timestamp to effective interval.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 13: Anti-join

Summary:

```text
Find missing related records.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 14: Semi-join

Summary:

```text
Existence check without row multiplication.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 15: Bridge table

Summary:

```text
Resolves many-to-many relationship.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 16: Validation

Summary:

```text
Counts, duplicates, unmatched keys.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```


## 97. SQL Joins FAQ

### FAQ 1: When should I use LEFT JOIN?

Answer:

```text
Use LEFT JOIN when the left table defines the denominator or all left rows must be preserved.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 2: When should I use INNER JOIN?

Answer:

```text
Use INNER JOIN when unmatched rows should be excluded from the result.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 3: Why can LEFT JOIN increase row count?

Answer:

```text
Because the right table can have multiple matches for one left row.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 4: Why is filtering right table in WHERE dangerous?

Answer:

```text
It can remove NULL unmatched rows and turn a LEFT JOIN into INNER JOIN behavior.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 5: When should I use EXISTS?

Answer:

```text
Use EXISTS when only existence matters and you do not need right-table attributes.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 6: When should I use FULL OUTER JOIN?

Answer:

```text
Use FULL OUTER JOIN for reconciliation where missing records on both sides matter.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 7: How do I prevent fact-to-fact double counting?

Answer:

```text
Aggregate each fact table to the common grain before joining.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 8: How do I validate joins?

Answer:

```text
Check row counts, duplicate join keys, unmatched rows, and duplicate matches per left key.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 9: How do I join to SCD history?

Answer:

```text
Join on entity key plus fact_time between effective_from and effective_to.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```

### FAQ 10: What causes join explosion?

Answer:

```text
Duplicate join keys, incomplete join conditions, or many-to-many relationships.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Business metric risk.
```


## 98. Additional Join Scenario Cards

### Scenario Card 1: Join users to orders for country revenue

Pattern:

```text
many-to-one LEFT JOIN
```

Key warning:

```text
Validate users.user_id uniqueness.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 2: Join order_items to products for category revenue

Pattern:

```text
many-to-one JOIN
```

Key warning:

```text
Metric is item grain.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 3: Join orders to payments for paid order status

Pattern:

```text
EXISTS/order flag
```

Key warning:

```text
Multiple payment attempts possible.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 4: Join accounts to transactions for active accounts

Pattern:

```text
LEFT JOIN aggregate
```

Key warning:

```text
Preserve accounts denominator.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 5: Join tickets to users by user_id

Pattern:

```text
many-to-one
```

Key warning:

```text
Check orphan tickets.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 6: Join product snapshots to calendar

Pattern:

```text
calendar LEFT JOIN
```

Key warning:

```text
Find missing product-day snapshots.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 7: Join user assignments to events

Pattern:

```text
experiment attribution
```

Key warning:

```text
Use assigned_at boundary.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 8: Join click events to sessions

Pattern:

```text
interval join
```

Key warning:

```text
Validate one session per event.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 9: Join orders to shipping table

Pattern:

```text
one-to-one or one-to-many
```

Key warning:

```text
Shipment split may create multiple rows.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 10: Join returns to orders

Pattern:

```text
LEFT JOIN from orders
```

Key warning:

```text
Preserve all orders for return rate.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 11: Join refunds to payments

Pattern:

```text
LEFT JOIN aggregate
```

Key warning:

```text
Multiple refunds possible.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 12: Join stores to regions

Pattern:

```text
dimension hierarchy
```

Key warning:

```text
Validate store_id uniqueness.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 13: Join products to suppliers

Pattern:

```text
many-to-one or many-to-many
```

Key warning:

```text
Supplier relationships may need bridge.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 14: Join customer identity tables

Pattern:

```text
natural key risk
```

Key warning:

```text
Normalize and validate duplicate emails.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 15: Join raw and clean tables

Pattern:

```text
reconciliation
```

Key warning:

```text
FULL OUTER by source id.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 16: Join CDC latest to target

Pattern:

```text
MERGE prep
```

Key warning:

```text
Deduplicate source first.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 17: Join event stream to user device

Pattern:

```text
latest/as-of
```

Key warning:

```text
Current vs historical device choice.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 18: Join daily metrics to targets

Pattern:

```text
entity-date composite
```

Key warning:

```text
Composite join key.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 19: Join payments to exchange rates

Pattern:

```text
currency-date
```

Key warning:

```text
Missing rates matter.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```

### Scenario Card 20: Join campaigns to calendar

Pattern:

```text
range/calendar
```

Key warning:

```text
Expand active campaign days.
```

Candidate must answer:

```text
1. What is the left table?
2. What is the right table?
3. What is the expected cardinality?
4. Which join type is safest?
5. What row count validation is required?
6. What metric could be corrupted?
```

Passing score:

```text
4/5 or higher.
```
