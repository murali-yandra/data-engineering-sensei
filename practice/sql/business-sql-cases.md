# Business SQL Cases Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/sql/business-sql-cases.md
```

This guide teaches and drills **business SQL case problems for Data Engineering interviews**.

This is not a generic SQL syntax document. It is an interview-focused guide for candidates who need to solve realistic business questions using SQL, explain assumptions, choose the right joins and aggregations, handle edge cases, validate outputs, and communicate trade-offs clearly.

Business SQL is high-ROI for Data Engineering interviews because interviewers often ask problems like:

- daily active users
- monthly active users
- retention
- churn
- funnel conversion
- cohort analysis
- revenue by customer
- average order value
- top customers
- repeat purchases
- rolling 7-day metrics
- month-over-month growth
- conversion rate
- first purchase date
- latest status per entity
- deduplication
- source-target reconciliation
- slowly changing dimension style snapshots
- missing events
- fraud/anomaly signals
- subscription metrics
- inventory metrics
- marketplace metrics
- ad campaign metrics
- support ticket SLAs
- data quality checks
- pipeline audit reports

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
- `modes/data-engineering-fundamentals-mode.md`
- `practice/sql`
- `practice/python/pandas-basics.md`
- `practice/system-design`
- `progress/CANDIDATE_PROFILE.md`
- `progress/CURRENT_STATE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Default interview standard if target companies are not provided:

```text
FAANG-style Data Engineering interview standard, scaled by candidate experience.
```


## 1. Purpose

The purpose of this guide is to make the candidate strong at solving business SQL cases in Data Engineering interviews.

The candidate should learn to answer:

```text
How do I convert a business question into SQL?
How do I clarify metric definitions?
How do I choose the grain of the query?
How do I avoid double counting?
How do I handle NULLs?
How do I handle duplicate records?
How do I calculate DAU, WAU, MAU?
How do I calculate retention?
How do I calculate churn?
How do I build cohorts?
How do I calculate funnel conversion?
How do I calculate rolling metrics?
How do I calculate growth rates?
How do I find first/last events?
How do I deduplicate latest records?
How do I reconcile source and target tables?
How do I validate query output?
How do I explain assumptions clearly?
```

A candidate is interview-ready only when they can:

```text
clarify metric definition before writing SQL
identify table grain
choose correct join type
avoid accidental row multiplication
use CTEs to structure logic
use GROUP BY correctly
use COUNT DISTINCT intentionally
use window functions for ranking/latest/rolling
use date functions safely
handle NULL and divide-by-zero
build reusable metric logic
validate row counts and duplicates
explain edge cases
explain performance considerations
communicate business interpretation
```


## 2. Why Business SQL Matters for Data Engineers

Data Engineers are often evaluated on whether they can turn raw event/fact/dimension data into reliable business metrics.

Real work examples:

```text
Build daily KPI table.
Debug why active users dropped.
Reconcile revenue between app and warehouse.
Calculate repeat purchase rate.
Build user retention table.
Track onboarding funnel conversion.
Calculate subscription churn.
Measure campaign ROI.
Find duplicate transaction records.
Identify missing daily partitions.
Create SLA metrics for support tickets.
Build customer lifetime value inputs.
Create slowly changing dimension snapshots.
Verify fact-to-dimension join quality.
```

Interviewers test business SQL because it reveals:

```text
Can the candidate understand metric definitions?
Can they reason about table grain?
Can they avoid double counting?
Can they handle messy data?
Can they use joins and windows correctly?
Can they validate outputs?
Can they communicate assumptions?
Can they write maintainable SQL?
```

Weak answer:

```text
Directly write a query without clarifying definitions.
```

Strong answer:

```text
Clarify the metric, identify the grain, filter to valid records, deduplicate if needed, aggregate at the correct level, handle edge cases like NULLs and divide-by-zero, then validate counts and explain assumptions.
```


## 3. Core Mental Model

Business SQL follows this flow:

```text
1. Understand the business question.
2. Define the metric precisely.
3. Identify input tables and table grain.
4. Identify filters and valid records.
5. Decide the output grain.
6. Build base CTEs.
7. Deduplicate if necessary.
8. Join dimensions carefully.
9. Aggregate at the correct level.
10. Use window functions where needed.
11. Handle NULLs and divide-by-zero.
12. Validate output.
13. Explain assumptions and edge cases.
```

Core interview line:

```text
Most SQL mistakes happen because the candidate does not clarify grain, join cardinality, or metric definition before writing the query.
```


## 4. Business SQL Vocabulary

Important terms:

```text
Metric:
A numeric business measurement such as revenue, active users, conversion rate.

Dimension:
Descriptive attribute such as country, plan, product, channel.

Fact table:
Table containing business events or measurements, such as orders or payments.

Dimension table:
Table containing descriptive entity data, such as users or products.

Grain:
What one row represents.

Event:
A user/system action at a point in time.

Cohort:
Group of users/entities sharing a starting event or period.

Retention:
Whether users return after a starting period.

Churn:
Whether users stop being active or subscribed.

Funnel:
Ordered sequence of steps users complete.

Conversion:
Percent of users/events moving from one stage to another.

Snapshot:
State of an entity at a point in time.

Deduplication:
Removing duplicate rows according to a business key.

Reconciliation:
Comparing two sources or tables for consistency.

Window function:
SQL function operating across related rows without collapsing them.

Rolling metric:
Metric over moving time window, such as rolling 7-day revenue.

SLA:
Service-level agreement, often time-to-resolution or response time.

Cardinality:
Relationship between tables in a join: one-to-one, one-to-many, many-to-one, many-to-many.
```


## 5. Standard Answer Framework

Use this framework for every business SQL interview problem:

```text
1. Restate the question in business terms.
2. Clarify:
   - metric definition
   - time range
   - timezone
   - valid event/status
   - output grain
   - duplicate handling
   - NULL handling
3. Identify table grain.
4. Identify primary keys and join keys.
5. Build a base CTE.
6. Filter to valid records.
7. Deduplicate if needed.
8. Aggregate at the required grain.
9. Use window functions if needed.
10. Handle divide-by-zero safely.
11. Return clean output columns.
12. Validate:
   - row counts
   - duplicate output keys
   - missing joins
   - metric reasonableness
13. Explain assumptions.
```

Short version:

```text
Definition:
Grain:
Filters:
Dedup:
Join:
Aggregate:
Validate:
Explain:
```

Strict rule:

```text
No business SQL answer is strong if the candidate does not clarify metric definition and table grain.
```


## 6. Scoring Rubric

Score each business SQL answer from 0 to 5.

### Score 0

No meaningful SQL or business reasoning.

### Score 1

Basic SELECT/GROUP BY attempt but unclear metric and likely wrong result.

### Score 2

Gets simple aggregation but misses edge cases, grain, or double counting.

### Score 3

Mostly correct query but weak assumptions, validation, NULL handling, or performance explanation.

### Score 4

Interview-ready. Correct logic, clean CTEs, good metric definition, proper joins/aggregation, and validation.

### Score 5

Strong. Handles edge cases, deduplication, join cardinality, windows, date boundaries, performance, data quality, and business interpretation.

Do not give 4+ if:

```text
candidate does not clarify metric definition
candidate ignores table grain
candidate joins facts to dimensions causing row multiplication
candidate uses COUNT(*) where COUNT DISTINCT is needed
candidate divides without NULLIF
candidate ignores duplicate events
candidate does not handle NULLs
candidate cannot explain date boundaries
candidate cannot validate output
candidate cannot explain assumptions
candidate writes unreadable nested SQL without structure
```


## 7. Common Tables Used in Business SQL Cases

Most business SQL cases use variations of these tables.

### users

```sql
users(
  user_id,
  signup_at,
  country,
  acquisition_channel,
  plan,
  is_test_user
)
```

### events

```sql
events(
  event_id,
  user_id,
  event_name,
  event_time,
  session_id,
  device_type
)
```

### orders

```sql
orders(
  order_id,
  user_id,
  order_time,
  order_status,
  total_amount,
  currency
)
```

### order_items

```sql
order_items(
  order_item_id,
  order_id,
  product_id,
  quantity,
  unit_price
)
```

### payments

```sql
payments(
  payment_id,
  order_id,
  user_id,
  payment_time,
  payment_status,
  amount
)
```

### subscriptions

```sql
subscriptions(
  subscription_id,
  user_id,
  plan,
  started_at,
  ended_at,
  status
)
```

### products

```sql
products(
  product_id,
  category,
  brand,
  price
)
```

### campaigns

```sql
campaigns(
  campaign_id,
  channel,
  start_date,
  end_date,
  spend
)
```

### tickets

```sql
tickets(
  ticket_id,
  user_id,
  created_at,
  first_response_at,
  resolved_at,
  priority,
  status
)
```

Interview line:

```text
Before writing SQL, I identify the grain of each table and whether joins are one-to-one, many-to-one, or one-to-many.
```


## 8. Date and Time Assumptions

Business metrics are time-sensitive.

Always clarify:

```text
Which timezone?
Which timestamp column?
Is the window inclusive or exclusive?
Are we grouping by event date or processing date?
Do late-arriving events exist?
Should test users be excluded?
Should cancelled/refunded orders be excluded?
```

Recommended window pattern:

```sql
WHERE event_time >= DATE '2026-01-01'
  AND event_time <  DATE '2026-02-01'
```

Why half-open windows:

```text
Avoids double counting boundary timestamps.
Works cleanly for daily/monthly windows.
```

Date grouping examples:

```sql
CAST(event_time AS DATE) AS event_date
```

or database-specific:

```sql
DATE_TRUNC('day', event_time) AS event_date
```

Interview line:

```text
I prefer half-open time windows because they avoid overlap between adjacent periods.
```


## 9. SQL Dialect Notes

Different databases have different syntax.

Common differences:

```text
DATE_TRUNC syntax differs.
DATEDIFF syntax differs.
INTERVAL syntax differs.
QUALIFY may not exist.
SAFE_DIVIDE may exist in BigQuery but not in SQL Server/Postgres.
LIMIT is not SQL Server syntax; SQL Server uses TOP or OFFSET/FETCH.
Boolean syntax differs.
```

Interview-safe approach:

```text
Use clear ANSI-style SQL when possible.
State dialect assumption if using dialect-specific functions.
```

Examples:

PostgreSQL-style:

```sql
DATE_TRUNC('month', order_time)
order_time + INTERVAL '7 days'
```

SQL Server-style:

```sql
DATEADD(day, 7, order_time)
DATEDIFF(day, signup_at, event_time)
SELECT TOP 10 ...
```

BigQuery-style:

```sql
DATE_TRUNC(DATE(order_time), MONTH)
SAFE_DIVIDE(numerator, denominator)
```

Interview line:

```text
I will assume PostgreSQL-style SQL unless the interviewer specifies a dialect, and I can translate functions if needed.
```


## 10. Safe Division

Avoid divide-by-zero.

General pattern:

```sql
numerator * 1.0 / NULLIF(denominator, 0)
```

Example:

```sql
converted_users * 1.0 / NULLIF(total_users, 0) AS conversion_rate
```

Optional percentage:

```sql
100.0 * converted_users / NULLIF(total_users, 0) AS conversion_pct
```

BigQuery:

```sql
SAFE_DIVIDE(converted_users, total_users) AS conversion_rate
```

Interview line:

```text
For ratios, I use NULLIF or SAFE_DIVIDE to avoid divide-by-zero and make empty-denominator behavior explicit.
```


## 11. COUNT, COUNT DISTINCT, and NULLs

Important differences:

```sql
COUNT(*) 
```

Counts rows.

```sql
COUNT(column)
```

Counts non-null values in column.

```sql
COUNT(DISTINCT user_id)
```

Counts unique non-null users.

Common business metric:

```sql
COUNT(DISTINCT user_id) AS active_users
```

Danger:

```sql
COUNT(*) after joining events to order_items can overcount because rows multiply.
```

Interview line:

```text
I choose COUNT DISTINCT when the metric is unique users/orders/sessions, and I check joins to avoid row multiplication.
```


## 12. CTE Structure

CTEs make business SQL readable.

Pattern:

```sql
WITH base_events AS (
  SELECT ...
  FROM events
  WHERE ...
),
deduped_events AS (
  SELECT ...
  FROM base_events
  WHERE ...
),
metric AS (
  SELECT ...
  FROM deduped_events
  GROUP BY ...
)
SELECT *
FROM metric;
```

Good CTE names:

```text
base_orders
valid_payments
deduped_events
daily_users
cohort_users
funnel_steps
final_metric
```

Bad CTE names:

```text
a
b
c
temp
x
```

Interview line:

```text
I use CTEs to separate filtering, deduplication, aggregation, and final calculation so the SQL is easier to review.
```


## 13. Case 1: Daily Active Users

Business question:

```text
Calculate daily active users for January 2026.
A user is active on a day if they performed any event that day.
```

Tables:

```sql
events(event_id, user_id, event_name, event_time)
```

Clarifications:

```text
Use event_time.
Group by event date.
Count distinct users.
Exclude NULL user_id.
Use half-open January window.
```

SQL:

```sql
WITH base_events AS (
  SELECT
    user_id,
    CAST(event_time AS DATE) AS event_date
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2026-02-01'
    AND user_id IS NOT NULL
)
SELECT
  event_date,
  COUNT(DISTINCT user_id) AS daily_active_users
FROM base_events
GROUP BY event_date
ORDER BY event_date;
```

Why this works:

```text
One user can have many events in a day, so COUNT DISTINCT user_id is required.
```

Edge cases:

```text
duplicate events
anonymous users
timezone
test users
late-arriving events
```

Validation:

```sql
SELECT event_date, COUNT(*) AS rows
FROM (
  SELECT CAST(event_time AS DATE) AS event_date
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2026-02-01'
) x
GROUP BY event_date;
```

Interview line:

```text
DAU is a distinct-user metric, not an event-count metric.
```


## 14. Case 2: Monthly Active Users

Business question:

```text
Calculate monthly active users for each month in 2026.
```

Tables:

```sql
events(event_id, user_id, event_name, event_time)
```

SQL:

```sql
WITH base_events AS (
  SELECT
    user_id,
    DATE_TRUNC('month', event_time) AS activity_month
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2027-01-01'
    AND user_id IS NOT NULL
)
SELECT
  activity_month,
  COUNT(DISTINCT user_id) AS monthly_active_users
FROM base_events
GROUP BY activity_month
ORDER BY activity_month;
```

Important:

```text
A user active on multiple days in the same month counts once for that month.
```

Common mistake:

```sql
SUM(daily_active_users)
```

Why wrong:

```text
Summing DAU over days overcounts users active on multiple days.
```

Interview line:

```text
MAU must be counted directly at monthly grain using distinct users, not by summing DAU.
```


## 15. Case 3: DAU/MAU Stickiness

Business question:

```text
Calculate DAU/MAU stickiness by month.
```

Definition:

```text
Average daily active users in a month divided by monthly active users.
```

SQL:

```sql
WITH daily_users AS (
  SELECT
    CAST(event_time AS DATE) AS event_date,
    DATE_TRUNC('month', event_time) AS activity_month,
    COUNT(DISTINCT user_id) AS dau
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2027-01-01'
    AND user_id IS NOT NULL
  GROUP BY
    CAST(event_time AS DATE),
    DATE_TRUNC('month', event_time)
),
monthly_users AS (
  SELECT
    DATE_TRUNC('month', event_time) AS activity_month,
    COUNT(DISTINCT user_id) AS mau
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2027-01-01'
    AND user_id IS NOT NULL
  GROUP BY DATE_TRUNC('month', event_time)
),
monthly_avg_dau AS (
  SELECT
    activity_month,
    AVG(dau) AS avg_dau
  FROM daily_users
  GROUP BY activity_month
)
SELECT
  m.activity_month,
  a.avg_dau,
  m.mau,
  a.avg_dau * 1.0 / NULLIF(m.mau, 0) AS dau_mau_stickiness
FROM monthly_users m
JOIN monthly_avg_dau a
  ON m.activity_month = a.activity_month
ORDER BY m.activity_month;
```

Edge case:

```text
If only days with events are included, average DAU excludes zero-activity days. Clarify whether calendar days with zero DAU should be included.
```

Interview line:

```text
For stickiness, clarify whether average DAU should include zero-activity calendar days.
```


## 16. Case 4: New Users by Day

Business question:

```text
Count new users by signup date.
```

Tables:

```sql
users(user_id, signup_at, is_test_user)
```

SQL:

```sql
SELECT
  CAST(signup_at AS DATE) AS signup_date,
  COUNT(DISTINCT user_id) AS new_users
FROM users
WHERE signup_at >= DATE '2026-01-01'
  AND signup_at <  DATE '2026-02-01'
  AND COALESCE(is_test_user, false) = false
GROUP BY CAST(signup_at AS DATE)
ORDER BY signup_date;
```

Clarifications:

```text
Are test/internal users excluded?
Is user_id unique in users?
Which timezone defines signup date?
```

Validation:

```sql
SELECT
  user_id,
  COUNT(*) AS row_count
FROM users
GROUP BY user_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
Even for a simple metric, I check whether the dimension table has one row per user.
```


## 17. Case 5: First Event Per User

Business question:

```text
Find each user's first event time and first event name.
```

Tables:

```sql
events(event_id, user_id, event_name, event_time)
```

SQL:

```sql
WITH ranked_events AS (
  SELECT
    user_id,
    event_name,
    event_time,
    event_id,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY event_time, event_id
    ) AS rn
  FROM events
  WHERE user_id IS NOT NULL
)
SELECT
  user_id,
  event_time AS first_event_time,
  event_name AS first_event_name
FROM ranked_events
WHERE rn = 1;
```

Why event_id tie-breaker:

```text
If two events have same event_time, output remains deterministic.
```

Common mistake:

```sql
SELECT user_id, MIN(event_time), event_name
FROM events
GROUP BY user_id, event_name;
```

Why wrong:

```text
It does not reliably return the event_name associated with the minimum timestamp.
```

Interview line:

```text
When I need attributes from the first row, I use ROW_NUMBER, not MIN timestamp plus random columns.
```


## 18. Case 6: Latest Status Per Order

Business question:

```text
Given order status history, return the latest status per order.
```

Tables:

```sql
order_status_history(order_id, status, status_time, status_event_id)
```

SQL:

```sql
WITH ranked_status AS (
  SELECT
    order_id,
    status,
    status_time,
    ROW_NUMBER() OVER (
      PARTITION BY order_id
      ORDER BY status_time DESC, status_event_id DESC
    ) AS rn
  FROM order_status_history
)
SELECT
  order_id,
  status AS latest_status,
  status_time AS latest_status_time
FROM ranked_status
WHERE rn = 1;
```

Edge cases:

```text
same status_time for multiple statuses
late-arriving status events
duplicate status events
cancelled/refunded status definitions
```

Interview line:

```text
Latest-record logic needs a deterministic tie-breaker.
```


## 19. Case 7: Revenue by Day

Business question:

```text
Calculate daily revenue from successful payments.
```

Tables:

```sql
payments(payment_id, order_id, user_id, payment_time, payment_status, amount)
```

SQL:

```sql
SELECT
  CAST(payment_time AS DATE) AS revenue_date,
  SUM(amount) AS revenue,
  COUNT(DISTINCT payment_id) AS successful_payments,
  COUNT(DISTINCT user_id) AS paying_users
FROM payments
WHERE payment_time >= DATE '2026-01-01'
  AND payment_time <  DATE '2026-02-01'
  AND payment_status = 'SUCCESS'
GROUP BY CAST(payment_time AS DATE)
ORDER BY revenue_date;
```

Clarifications:

```text
Use payment_time or order_time?
Include refunds?
Use gross or net revenue?
Currency conversion needed?
Are duplicate payment rows possible?
```

Interview line:

```text
Revenue definition must clarify successful payments, refunds, currency, and timestamp column.
```


## 20. Case 8: Net Revenue with Refunds

Business question:

```text
Calculate net revenue by day including successful payments and refunds.
```

Tables:

```sql
transactions(transaction_id, user_id, transaction_time, transaction_type, status, amount)
```

Assumption:

```text
transaction_type IN ('PAYMENT', 'REFUND')
successful payments add amount
successful refunds subtract amount
```

SQL:

```sql
SELECT
  CAST(transaction_time AS DATE) AS revenue_date,
  SUM(
    CASE
      WHEN transaction_type = 'PAYMENT' AND status = 'SUCCESS' THEN amount
      WHEN transaction_type = 'REFUND'  AND status = 'SUCCESS' THEN -amount
      ELSE 0
    END
  ) AS net_revenue
FROM transactions
WHERE transaction_time >= DATE '2026-01-01'
  AND transaction_time <  DATE '2026-02-01'
GROUP BY CAST(transaction_time AS DATE)
ORDER BY revenue_date;
```

Edge cases:

```text
refund amount sign may already be negative
partial refunds
refund date vs original order date
chargebacks
multi-currency
```

Interview line:

```text
Before subtracting refunds, I clarify whether refund amounts are stored positive or negative.
```


## 21. Case 9: Average Order Value

Business question:

```text
Calculate average order value by month.
```

Tables:

```sql
orders(order_id, user_id, order_time, order_status, total_amount)
```

Definition:

```text
AOV = total revenue from completed orders / number of completed orders.
```

SQL:

```sql
SELECT
  DATE_TRUNC('month', order_time) AS order_month,
  SUM(total_amount) AS revenue,
  COUNT(DISTINCT order_id) AS completed_orders,
  SUM(total_amount) * 1.0 / NULLIF(COUNT(DISTINCT order_id), 0) AS avg_order_value
FROM orders
WHERE order_time >= DATE '2026-01-01'
  AND order_time <  DATE '2027-01-01'
  AND order_status = 'COMPLETED'
GROUP BY DATE_TRUNC('month', order_time)
ORDER BY order_month;
```

Common mistake:

```sql
AVG(total_amount)
```

When AVG works:

```text
AVG(total_amount) works if orders has exactly one row per order and total_amount is already order-level.
```

When AVG may be wrong:

```text
If joined to order_items, each order can appear multiple times and AVG can be distorted.
```

Interview line:

```text
AOV must be calculated at order grain; joining to item grain can break it unless re-aggregated.
```


## 22. Case 10: Top Customers by Revenue

Business question:

```text
Find top 10 customers by completed order revenue.
```

Tables:

```sql
orders(order_id, user_id, order_time, order_status, total_amount)
```

SQL:

```sql
SELECT
  user_id,
  SUM(total_amount) AS revenue,
  COUNT(DISTINCT order_id) AS completed_orders
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY user_id
ORDER BY revenue DESC, user_id
LIMIT 10;
```

SQL Server version:

```sql
SELECT TOP 10
  user_id,
  SUM(total_amount) AS revenue,
  COUNT(DISTINCT order_id) AS completed_orders
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY user_id
ORDER BY revenue DESC, user_id;
```

Tie-breaker:

```text
Add user_id to ORDER BY for deterministic output.
```

Interview line:

```text
Top-N queries should include deterministic tie-breakers.
```


## 23. Case 11: Repeat Purchase Rate

Business question:

```text
What percentage of customers made at least two completed orders?
```

Tables:

```sql
orders(order_id, user_id, order_status, order_time)
```

SQL:

```sql
WITH customer_orders AS (
  SELECT
    user_id,
    COUNT(DISTINCT order_id) AS completed_orders
  FROM orders
  WHERE order_status = 'COMPLETED'
    AND user_id IS NOT NULL
  GROUP BY user_id
)
SELECT
  COUNT(*) AS purchasing_customers,
  SUM(CASE WHEN completed_orders >= 2 THEN 1 ELSE 0 END) AS repeat_customers,
  SUM(CASE WHEN completed_orders >= 2 THEN 1 ELSE 0 END) * 1.0
    / NULLIF(COUNT(*), 0) AS repeat_purchase_rate
FROM customer_orders;
```

Clarifications:

```text
Within what time period?
All-time repeat or period repeat?
Are cancelled/refunded orders excluded?
```

Interview line:

```text
Repeat purchase rate is customer-grain, so I first aggregate orders per customer.
```


## 24. Case 12: First Purchase Conversion

Business question:

```text
What percentage of signed-up users made a first purchase within 7 days of signup?
```

Tables:

```sql
users(user_id, signup_at)
orders(order_id, user_id, order_time, order_status)
```

SQL:

```sql
WITH first_purchase AS (
  SELECT
    user_id,
    MIN(order_time) AS first_purchase_time
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
),
signup_users AS (
  SELECT
    user_id,
    signup_at
  FROM users
  WHERE signup_at >= DATE '2026-01-01'
    AND signup_at <  DATE '2026-02-01'
)
SELECT
  COUNT(*) AS signed_up_users,
  SUM(
    CASE
      WHEN fp.first_purchase_time >= su.signup_at
       AND fp.first_purchase_time <  su.signup_at + INTERVAL '7 days'
      THEN 1 ELSE 0
    END
  ) AS purchased_within_7_days,
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

Clarifications:

```text
Signup cohort period?
Use completed orders only?
What about purchases before signup due to data bug?
```

Interview line:

```text
Conversion from signup to purchase must use users as denominator, so left join preserves non-purchasers.
```


## 25. Case 13: Day-1 Retention

Business question:

```text
For users who signed up on each date, what percentage were active the next day?
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
  WHERE signup_at >= DATE '2026-01-01'
    AND signup_at <  DATE '2026-02-01'
),
day1_active AS (
  SELECT DISTINCT
    s.user_id,
    s.signup_date
  FROM signup_cohort s
  JOIN events e
    ON s.user_id = e.user_id
   AND CAST(e.event_time AS DATE) = s.signup_date + INTERVAL '1 day'
)
SELECT
  s.signup_date,
  COUNT(DISTINCT s.user_id) AS cohort_users,
  COUNT(DISTINCT d.user_id) AS retained_day1_users,
  COUNT(DISTINCT d.user_id) * 1.0
    / NULLIF(COUNT(DISTINCT s.user_id), 0) AS day1_retention
FROM signup_cohort s
LEFT JOIN day1_active d
  ON s.user_id = d.user_id
 AND s.signup_date = d.signup_date
GROUP BY s.signup_date
ORDER BY s.signup_date;
```

Dialect note:

```text
Date + interval syntax differs across databases.
```

Interview line:

```text
Retention denominator is the original cohort, so I use a left join from cohort users to retained users.
```


## 26. Case 14: Retention Matrix

Business question:

```text
Build a cohort retention table by signup month and activity month number.
```

Tables:

```sql
users(user_id, signup_at)
events(user_id, event_time)
```

SQL:

```sql
WITH cohorts AS (
  SELECT
    user_id,
    DATE_TRUNC('month', signup_at) AS cohort_month
  FROM users
),
activity AS (
  SELECT DISTINCT
    user_id,
    DATE_TRUNC('month', event_time) AS activity_month
  FROM events
),
cohort_activity AS (
  SELECT
    c.cohort_month,
    a.activity_month,
    (
      EXTRACT(YEAR FROM a.activity_month) * 12 + EXTRACT(MONTH FROM a.activity_month)
      - EXTRACT(YEAR FROM c.cohort_month) * 12 - EXTRACT(MONTH FROM c.cohort_month)
    ) AS month_number,
    c.user_id
  FROM cohorts c
  JOIN activity a
    ON c.user_id = a.user_id
   AND a.activity_month >= c.cohort_month
),
cohort_sizes AS (
  SELECT
    cohort_month,
    COUNT(DISTINCT user_id) AS cohort_size
  FROM cohorts
  GROUP BY cohort_month
)
SELECT
  ca.cohort_month,
  ca.month_number,
  COUNT(DISTINCT ca.user_id) AS active_users,
  cs.cohort_size,
  COUNT(DISTINCT ca.user_id) * 1.0 / NULLIF(cs.cohort_size, 0) AS retention_rate
FROM cohort_activity ca
JOIN cohort_sizes cs
  ON ca.cohort_month = cs.cohort_month
GROUP BY
  ca.cohort_month,
  ca.month_number,
  cs.cohort_size
ORDER BY
  ca.cohort_month,
  ca.month_number;
```

Clarifications:

```text
Use signup month or first purchase month as cohort?
Is month 0 signup month activity?
Should inactive zero months be filled?
```

Interview line:

```text
Cohort retention requires stable cohort size as denominator and activity counted by offset period.
```


## 27. Case 15: Churned Subscribers

Business question:

```text
Count monthly subscription churn.
A user churns in a month if their subscription ended in that month.
```

Tables:

```sql
subscriptions(subscription_id, user_id, started_at, ended_at, status)
```

SQL:

```sql
SELECT
  DATE_TRUNC('month', ended_at) AS churn_month,
  COUNT(DISTINCT user_id) AS churned_users
FROM subscriptions
WHERE ended_at IS NOT NULL
  AND ended_at >= DATE '2026-01-01'
  AND ended_at <  DATE '2027-01-01'
GROUP BY DATE_TRUNC('month', ended_at)
ORDER BY churn_month;
```

Clarifications:

```text
Does ended_at always mean churn?
What about plan switch?
What about temporary pause?
What about users with multiple subscriptions?
Should voluntary and involuntary churn be separated?
```

Interview line:

```text
Churn definition must be clarified because ended subscription can mean cancellation, plan switch, pause, or failed billing.
```


## 28. Case 16: Monthly Churn Rate

Business question:

```text
Calculate monthly churn rate.
```

Definition:

```text
churn_rate = users churned during month / active subscribers at start of month
```

Tables:

```sql
subscriptions(subscription_id, user_id, started_at, ended_at)
```

SQL:

```sql
WITH months AS (
  SELECT DATE '2026-01-01' AS month_start
  UNION ALL SELECT DATE '2026-02-01'
  UNION ALL SELECT DATE '2026-03-01'
),
active_at_start AS (
  SELECT
    m.month_start,
    COUNT(DISTINCT s.user_id) AS active_users_start
  FROM months m
  JOIN subscriptions s
    ON s.started_at < m.month_start
   AND (s.ended_at IS NULL OR s.ended_at >= m.month_start)
  GROUP BY m.month_start
),
churned AS (
  SELECT
    m.month_start,
    COUNT(DISTINCT s.user_id) AS churned_users
  FROM months m
  JOIN subscriptions s
    ON s.ended_at >= m.month_start
   AND s.ended_at <  m.month_start + INTERVAL '1 month'
  GROUP BY m.month_start
)
SELECT
  a.month_start,
  a.active_users_start,
  COALESCE(c.churned_users, 0) AS churned_users,
  COALESCE(c.churned_users, 0) * 1.0 / NULLIF(a.active_users_start, 0) AS churn_rate
FROM active_at_start a
LEFT JOIN churned c
  ON a.month_start = c.month_start
ORDER BY a.month_start;
```

Clarifications:

```text
Need a calendar/month table in production.
Should users starting and ending within same month be included in denominator?
```

Interview line:

```text
Churn rate needs a denominator at start of period, not total users who ever subscribed.
```


## 29. Case 17: Funnel Conversion

Business question:

```text
Calculate conversion from page_view to add_to_cart to purchase.
```

Tables:

```sql
events(event_id, user_id, event_name, event_time)
```

SQL:

```sql
WITH user_steps AS (
  SELECT
    user_id,
    MIN(CASE WHEN event_name = 'page_view' THEN event_time END) AS page_view_time,
    MIN(CASE WHEN event_name = 'add_to_cart' THEN event_time END) AS add_to_cart_time,
    MIN(CASE WHEN event_name = 'purchase' THEN event_time END) AS purchase_time
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2026-02-01'
    AND event_name IN ('page_view', 'add_to_cart', 'purchase')
    AND user_id IS NOT NULL
  GROUP BY user_id
),
ordered_steps AS (
  SELECT
    user_id,
    page_view_time,
    CASE
      WHEN add_to_cart_time >= page_view_time THEN add_to_cart_time
    END AS valid_add_to_cart_time,
    CASE
      WHEN purchase_time >= add_to_cart_time
       AND add_to_cart_time >= page_view_time THEN purchase_time
    END AS valid_purchase_time
  FROM user_steps
)
SELECT
  COUNT(*) AS viewed_users,
  SUM(CASE WHEN valid_add_to_cart_time IS NOT NULL THEN 1 ELSE 0 END) AS add_to_cart_users,
  SUM(CASE WHEN valid_purchase_time IS NOT NULL THEN 1 ELSE 0 END) AS purchase_users,
  SUM(CASE WHEN valid_add_to_cart_time IS NOT NULL THEN 1 ELSE 0 END) * 1.0
    / NULLIF(COUNT(*), 0) AS view_to_cart_rate,
  SUM(CASE WHEN valid_purchase_time IS NOT NULL THEN 1 ELSE 0 END) * 1.0
    / NULLIF(SUM(CASE WHEN valid_add_to_cart_time IS NOT NULL THEN 1 ELSE 0 END), 0) AS cart_to_purchase_rate
FROM ordered_steps
WHERE page_view_time IS NOT NULL;
```

Clarifications:

```text
Must steps happen in order?
Within same session?
Within what time window?
User-level or session-level funnel?
```

Interview line:

```text
Funnel definitions require step ordering, entity grain, and time window clarity.
```


## 30. Case 18: Session-Level Funnel

Business question:

```text
Calculate session-level checkout funnel conversion.
```

Tables:

```sql
events(event_id, user_id, session_id, event_name, event_time)
```

SQL:

```sql
WITH session_steps AS (
  SELECT
    session_id,
    MIN(CASE WHEN event_name = 'product_view' THEN event_time END) AS product_view_time,
    MIN(CASE WHEN event_name = 'checkout_start' THEN event_time END) AS checkout_start_time,
    MIN(CASE WHEN event_name = 'purchase' THEN event_time END) AS purchase_time
  FROM events
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2026-02-01'
    AND session_id IS NOT NULL
    AND event_name IN ('product_view', 'checkout_start', 'purchase')
  GROUP BY session_id
)
SELECT
  COUNT(*) AS product_view_sessions,
  SUM(CASE WHEN checkout_start_time >= product_view_time THEN 1 ELSE 0 END) AS checkout_sessions,
  SUM(
    CASE
      WHEN purchase_time >= checkout_start_time
       AND checkout_start_time >= product_view_time
      THEN 1 ELSE 0
    END
  ) AS purchase_sessions,
  SUM(CASE WHEN checkout_start_time >= product_view_time THEN 1 ELSE 0 END) * 1.0
    / NULLIF(COUNT(*), 0) AS product_to_checkout_rate
FROM session_steps
WHERE product_view_time IS NOT NULL;
```

Interview line:

```text
Session-level funnels use session_id as grain, while user-level funnels use user_id as grain.
```


## 31. Case 19: Rolling 7-Day Revenue

Business question:

```text
Calculate rolling 7-day revenue by date.
```

Tables:

```sql
orders(order_id, order_time, order_status, total_amount)
```

SQL:

```sql
WITH daily_revenue AS (
  SELECT
    CAST(order_time AS DATE) AS order_date,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY CAST(order_time AS DATE)
)
SELECT
  order_date,
  revenue,
  SUM(revenue) OVER (
    ORDER BY order_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rolling_7_day_revenue
FROM daily_revenue
ORDER BY order_date;
```

Important edge case:

```text
This only includes dates that exist in daily_revenue. If missing calendar dates should count as zero, join to a calendar table first.
```

Calendar-safe pattern:

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
  GROUP BY CAST(order_time AS DATE)
)
SELECT
  c.calendar_date,
  COALESCE(d.revenue, 0) AS revenue,
  SUM(COALESCE(d.revenue, 0)) OVER (
    ORDER BY c.calendar_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rolling_7_day_revenue
FROM calendar c
LEFT JOIN daily_revenue d
  ON c.calendar_date = d.order_date
ORDER BY c.calendar_date;
```

Interview line:

```text
Rolling date metrics should include zero-activity dates when business expects calendar continuity.
```


## 32. Case 20: Month-over-Month Growth

Business question:

```text
Calculate month-over-month revenue growth.
```

Tables:

```sql
orders(order_id, order_time, order_status, total_amount)
```

SQL:

```sql
WITH monthly_revenue AS (
  SELECT
    DATE_TRUNC('month', order_time) AS order_month,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY DATE_TRUNC('month', order_time)
),
with_previous AS (
  SELECT
    order_month,
    revenue,
    LAG(revenue) OVER (ORDER BY order_month) AS previous_month_revenue
  FROM monthly_revenue
)
SELECT
  order_month,
  revenue,
  previous_month_revenue,
  revenue - previous_month_revenue AS revenue_change,
  (revenue - previous_month_revenue) * 1.0
    / NULLIF(previous_month_revenue, 0) AS mom_growth_rate
FROM with_previous
ORDER BY order_month;
```

Edge cases:

```text
first month has no previous month
previous month revenue zero
missing months need calendar table
```

Interview line:

```text
Growth rates need safe division and careful handling of missing or zero previous periods.
```


## 33. Case 21: Top Product per Category

Business question:

```text
Find the top-selling product by quantity in each category.
```

Tables:

```sql
order_items(order_id, product_id, quantity)
orders(order_id, order_status)
products(product_id, category)
```

SQL:

```sql
WITH product_sales AS (
  SELECT
    p.category,
    oi.product_id,
    SUM(oi.quantity) AS total_quantity
  FROM order_items oi
  JOIN orders o
    ON oi.order_id = o.order_id
  JOIN products p
    ON oi.product_id = p.product_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY
    p.category,
    oi.product_id
),
ranked AS (
  SELECT
    category,
    product_id,
    total_quantity,
    ROW_NUMBER() OVER (
      PARTITION BY category
      ORDER BY total_quantity DESC, product_id
    ) AS rn
  FROM product_sales
)
SELECT
  category,
  product_id,
  total_quantity
FROM ranked
WHERE rn = 1
ORDER BY category;
```

If ties should be included:

```sql
RANK() OVER (
  PARTITION BY category
  ORDER BY total_quantity DESC
) AS rnk
```

Then filter `rnk = 1`.

Interview line:

```text
Use ROW_NUMBER for one winner, RANK for all tied winners.
```


## 34. Case 22: Inventory Stockout Days

Business question:

```text
Count stockout days per product.
A product is stocked out on a day if inventory_quantity = 0.
```

Tables:

```sql
inventory_snapshot(product_id, snapshot_date, inventory_quantity)
```

SQL:

```sql
SELECT
  product_id,
  COUNT(*) AS stockout_days
FROM inventory_snapshot
WHERE snapshot_date >= DATE '2026-01-01'
  AND snapshot_date <  DATE '2026-02-01'
  AND inventory_quantity = 0
GROUP BY product_id
ORDER BY stockout_days DESC, product_id;
```

Clarifications:

```text
Is there exactly one snapshot per product per day?
What if snapshot missing?
Should missing snapshot count as unknown or stockout?
```

Validation:

```sql
SELECT
  product_id,
  snapshot_date,
  COUNT(*) AS rows_per_day
FROM inventory_snapshot
GROUP BY product_id, snapshot_date
HAVING COUNT(*) > 1;
```

Interview line:

```text
Snapshot metrics require validating that snapshot grain is one row per entity per snapshot date.
```


## 35. Case 23: Support Ticket First Response SLA

Business question:

```text
Calculate percentage of support tickets with first response within 24 hours.
```

Tables:

```sql
tickets(ticket_id, created_at, first_response_at, priority, status)
```

SQL:

```sql
SELECT
  priority,
  COUNT(*) AS tickets,
  SUM(
    CASE
      WHEN first_response_at IS NOT NULL
       AND first_response_at <= created_at + INTERVAL '24 hours'
      THEN 1 ELSE 0
    END
  ) AS responded_within_24h,
  SUM(
    CASE
      WHEN first_response_at IS NOT NULL
       AND first_response_at <= created_at + INTERVAL '24 hours'
      THEN 1 ELSE 0
    END
  ) * 1.0 / NULLIF(COUNT(*), 0) AS sla_rate
FROM tickets
WHERE created_at >= DATE '2026-01-01'
  AND created_at <  DATE '2026-02-01'
GROUP BY priority
ORDER BY priority;
```

Clarifications:

```text
Business hours or calendar hours?
Do auto-responses count?
Should closed-without-response count as failed SLA?
```

Interview line:

```text
SLA metrics require clarifying time basis and what counts as response.
```


## 36. Case 24: Time to Resolution

Business question:

```text
Calculate average ticket resolution time in hours by priority.
```

Tables:

```sql
tickets(ticket_id, created_at, resolved_at, priority, status)
```

SQL:

```sql
SELECT
  priority,
  COUNT(*) AS resolved_tickets,
  AVG(EXTRACT(EPOCH FROM (resolved_at - created_at)) / 3600.0) AS avg_resolution_hours
FROM tickets
WHERE created_at >= DATE '2026-01-01'
  AND created_at <  DATE '2026-02-01'
  AND resolved_at IS NOT NULL
GROUP BY priority
ORDER BY priority;
```

Dialect note:

```text
Timestamp difference syntax varies.
SQL Server would use DATEDIFF(hour, created_at, resolved_at).
```

Edge cases:

```text
resolved_at before created_at
reopened tickets
business hours vs calendar hours
outliers skewing average
median may be better
```

Interview line:

```text
For duration metrics, I check invalid negative durations and consider median/p95 in addition to average.
```


## 37. Case 25: Campaign ROI

Business question:

```text
Calculate revenue and ROI by campaign.
```

Tables:

```sql
campaigns(campaign_id, channel, spend)
users(user_id, campaign_id, signup_at)
orders(order_id, user_id, order_time, order_status, total_amount)
```

Definition:

```text
ROI = (revenue - spend) / spend
```

SQL:

```sql
WITH campaign_revenue AS (
  SELECT
    u.campaign_id,
    SUM(o.total_amount) AS revenue,
    COUNT(DISTINCT o.order_id) AS orders
  FROM users u
  JOIN orders o
    ON u.user_id = o.user_id
   AND o.order_status = 'COMPLETED'
  WHERE u.campaign_id IS NOT NULL
  GROUP BY u.campaign_id
)
SELECT
  c.campaign_id,
  c.channel,
  c.spend,
  COALESCE(r.revenue, 0) AS revenue,
  COALESCE(r.orders, 0) AS orders,
  (COALESCE(r.revenue, 0) - c.spend) * 1.0 / NULLIF(c.spend, 0) AS roi
FROM campaigns c
LEFT JOIN campaign_revenue r
  ON c.campaign_id = r.campaign_id
ORDER BY roi DESC;
```

Clarifications:

```text
Attribution window?
First-touch or last-touch?
Revenue within campaign period only?
Spend can be zero?
```

Interview line:

```text
Marketing ROI depends heavily on attribution definition and time window.
```


## 38. Case 26: User Acquisition Cost

Business question:

```text
Calculate cost per acquired user by campaign.
```

Tables:

```sql
campaigns(campaign_id, spend)
users(user_id, campaign_id, signup_at)
```

SQL:

```sql
WITH acquired_users AS (
  SELECT
    campaign_id,
    COUNT(DISTINCT user_id) AS users_acquired
  FROM users
  WHERE campaign_id IS NOT NULL
  GROUP BY campaign_id
)
SELECT
  c.campaign_id,
  c.spend,
  COALESCE(a.users_acquired, 0) AS users_acquired,
  c.spend * 1.0 / NULLIF(COALESCE(a.users_acquired, 0), 0) AS cost_per_acquired_user
FROM campaigns c
LEFT JOIN acquired_users a
  ON c.campaign_id = a.campaign_id;
```

Clarifications:

```text
Only users signed up during campaign active dates?
Exclude test users?
Spend currency?
```

Interview line:

```text
Cost per acquisition requires spend denominator and acquired-user definition alignment.
```


## 39. Case 27: Marketplace Buyer-Seller Metrics

Business question:

```text
For each month, count active buyers, active sellers, and GMV.
```

Tables:

```sql
orders(order_id, buyer_id, seller_id, order_time, status, gmv)
```

SQL:

```sql
SELECT
  DATE_TRUNC('month', order_time) AS order_month,
  COUNT(DISTINCT buyer_id) AS active_buyers,
  COUNT(DISTINCT seller_id) AS active_sellers,
  SUM(gmv) AS gmv,
  COUNT(DISTINCT order_id) AS orders
FROM orders
WHERE status = 'COMPLETED'
GROUP BY DATE_TRUNC('month', order_time)
ORDER BY order_month;
```

Clarifications:

```text
GMV before or after discounts/refunds?
Completed orders only?
Are buyer_id/seller_id always non-null?
```

Interview line:

```text
Marketplace metrics often have multiple entity roles, so buyer and seller distinct counts must be separate.
```


## 40. Case 28: Fraud Suspicion by Velocity

Business question:

```text
Find users with more than 5 orders in any 10-minute window.
```

Tables:

```sql
orders(order_id, user_id, order_time)
```

SQL using self join:

```sql
SELECT DISTINCT
  o1.user_id
FROM orders o1
JOIN orders o2
  ON o1.user_id = o2.user_id
 AND o2.order_time >= o1.order_time
 AND o2.order_time <  o1.order_time + INTERVAL '10 minutes'
GROUP BY
  o1.user_id,
  o1.order_time
HAVING COUNT(DISTINCT o2.order_id) > 5;
```

Performance note:

```text
Self joins can be expensive. In production, use window functions if supported or pre-aggregated time buckets depending exact definition.
```

Clarifications:

```text
Completed orders only?
Include cancelled attempts?
Use rolling exact 10-minute window or fixed time bucket?
```

Interview line:

```text
Velocity rules need exact rolling-window definition, and self joins may be expensive at scale.
```


## 41. Case 29: Duplicate Events

Business question:

```text
Find duplicate events by event_id.
```

Tables:

```sql
events(event_id, user_id, event_name, event_time, ingested_at)
```

SQL:

```sql
SELECT
  event_id,
  COUNT(*) AS duplicate_count,
  MIN(ingested_at) AS first_ingested_at,
  MAX(ingested_at) AS last_ingested_at
FROM events
GROUP BY event_id
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC, event_id;
```

Dedup keep latest ingestion:

```sql
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY event_id
      ORDER BY ingested_at DESC
    ) AS rn
  FROM events
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Interview line:

```text
Duplicate detection and deduplication require a stable event key and a keep rule.
```


## 42. Case 30: Source-Target Reconciliation

Business question:

```text
Compare source_transactions and warehouse_transactions by transaction_id.
Find only-in-source, only-in-target, and amount mismatches.
```

Tables:

```sql
source_transactions(transaction_id, amount)
warehouse_transactions(transaction_id, amount)
```

SQL:

```sql
WITH joined AS (
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
  FROM source_transactions s
  FULL OUTER JOIN warehouse_transactions w
    ON s.transaction_id = w.transaction_id
)
SELECT *
FROM joined
WHERE reconciliation_status <> 'MATCH'
ORDER BY reconciliation_status, transaction_id;
```

NULL-safe amount comparison may require dialect-specific logic.

PostgreSQL:

```sql
s.amount IS DISTINCT FROM w.amount
```

Interview line:

```text
Reconciliation needs full outer join so missing records on either side are detected.
```


## 43. Case 31: Missing Daily Partitions

Business question:

```text
Find dates in January 2026 where no orders were loaded.
```

Tables:

```sql
dim_calendar(calendar_date)
orders(order_id, order_time)
```

SQL:

```sql
WITH expected_dates AS (
  SELECT calendar_date
  FROM dim_calendar
  WHERE calendar_date >= DATE '2026-01-01'
    AND calendar_date <  DATE '2026-02-01'
),
order_dates AS (
  SELECT DISTINCT
    CAST(order_time AS DATE) AS order_date
  FROM orders
  WHERE order_time >= DATE '2026-01-01'
    AND order_time <  DATE '2026-02-01'
)
SELECT
  e.calendar_date AS missing_date
FROM expected_dates e
LEFT JOIN order_dates o
  ON e.calendar_date = o.order_date
WHERE o.order_date IS NULL
ORDER BY missing_date;
```

Interview line:

```text
Completeness checks usually require a calendar or expected-partition table.
```


## 44. Case 32: Data Quality Null Rate

Business question:

```text
Calculate null rate for important columns in orders.
```

Tables:

```sql
orders(order_id, user_id, order_time, total_amount)
```

SQL:

```sql
SELECT
  COUNT(*) AS total_rows,
  SUM(CASE WHEN order_id IS NULL THEN 1 ELSE 0 END) AS null_order_id,
  SUM(CASE WHEN user_id IS NULL THEN 1 ELSE 0 END) AS null_user_id,
  SUM(CASE WHEN order_time IS NULL THEN 1 ELSE 0 END) AS null_order_time,
  SUM(CASE WHEN total_amount IS NULL THEN 1 ELSE 0 END) AS null_total_amount,
  SUM(CASE WHEN user_id IS NULL THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(*), 0) AS null_user_id_rate
FROM orders;
```

Interview line:

```text
Data quality queries should report both counts and rates because rates are easier to compare across volume changes.
```


## 45. Case 33: Orphan Fact Records

Business question:

```text
Find orders whose user_id does not exist in users.
```

Tables:

```sql
orders(order_id, user_id)
users(user_id)
```

SQL:

```sql
SELECT
  o.order_id,
  o.user_id
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id
WHERE u.user_id IS NULL;
```

Count orphan rate:

```sql
SELECT
  COUNT(*) AS total_orders,
  SUM(CASE WHEN u.user_id IS NULL THEN 1 ELSE 0 END) AS orphan_orders,
  SUM(CASE WHEN u.user_id IS NULL THEN 1 ELSE 0 END) * 1.0
    / NULLIF(COUNT(*), 0) AS orphan_order_rate
FROM orders o
LEFT JOIN users u
  ON o.user_id = u.user_id;
```

Interview line:

```text
Fact-to-dimension orphan checks catch referential integrity issues in warehouse data.
```


## 46. Case 34: Slowly Changing Dimension Latest Row

Business question:

```text
Get current user profile from an SCD-style table.
```

Tables:

```sql
user_profile_history(user_id, country, plan, effective_from, effective_to, is_current)
```

Option 1:

```sql
SELECT
  user_id,
  country,
  plan,
  effective_from
FROM user_profile_history
WHERE is_current = true;
```

Option 2 if no reliable is_current:

```sql
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY effective_from DESC
    ) AS rn
  FROM user_profile_history
)
SELECT
  user_id,
  country,
  plan,
  effective_from
FROM ranked
WHERE rn = 1;
```

Validation:

```sql
SELECT user_id, COUNT(*) AS current_rows
FROM user_profile_history
WHERE is_current = true
GROUP BY user_id
HAVING COUNT(*) > 1;
```

Interview line:

```text
For current snapshot from history, validate that only one current row exists per entity.
```


## 47. Case 35: As-Of Join

Business question:

```text
Join orders to the user plan that was active at order_time.
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

Validation:

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
As-of joins require non-overlapping effective intervals; otherwise one fact can match multiple dimension rows.
```


## 48. Case 36: Active Subscription Snapshot

Business question:

```text
For each day, count active subscriptions.
```

Tables:

```sql
dim_calendar(calendar_date)
subscriptions(subscription_id, user_id, started_at, ended_at)
```

SQL:

```sql
SELECT
  c.calendar_date,
  COUNT(DISTINCT s.subscription_id) AS active_subscriptions,
  COUNT(DISTINCT s.user_id) AS active_users
FROM dim_calendar c
LEFT JOIN subscriptions s
  ON s.started_at <= c.calendar_date
 AND (s.ended_at IS NULL OR s.ended_at > c.calendar_date)
WHERE c.calendar_date >= DATE '2026-01-01'
  AND c.calendar_date <  DATE '2026-02-01'
GROUP BY c.calendar_date
ORDER BY c.calendar_date;
```

Clarifications:

```text
If subscription ends on a date, is it active that day?
Use started_at <= date and ended_at > date depending business definition.
```

Interview line:

```text
Snapshot active-state queries require clear inclusive/exclusive boundary definitions.
```


## 49. Case 37: Product Attach Rate

Business question:

```text
What percentage of orders include an add-on product?
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

Why order_flags CTE:

```text
Order_items is item grain. We must aggregate to order grain before calculating order-level attach rate.
```

Interview line:

```text
When measuring order-level rates from item-level tables, first collapse to order grain.
```


## 50. Case 38: Basket Size

Business question:

```text
Calculate average basket size by month.
Basket size = number of items per completed order.
```

Tables:

```sql
orders(order_id, order_time, order_status)
order_items(order_id, quantity)
```

SQL:

```sql
WITH order_item_counts AS (
  SELECT
    o.order_id,
    DATE_TRUNC('month', o.order_time) AS order_month,
    SUM(oi.quantity) AS items_in_order
  FROM orders o
  JOIN order_items oi
    ON o.order_id = oi.order_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY
    o.order_id,
    DATE_TRUNC('month', o.order_time)
)
SELECT
  order_month,
  AVG(items_in_order) AS avg_basket_size,
  COUNT(*) AS completed_orders
FROM order_item_counts
GROUP BY order_month
ORDER BY order_month;
```

Interview line:

```text
For basket size, aggregate item quantities to order grain first, then average across orders.
```


## 51. Case 39: Customer Lifetime Value Input

Business question:

```text
For each customer, calculate total revenue, first order date, last order date, and order count.
```

Tables:

```sql
orders(order_id, user_id, order_time, order_status, total_amount)
```

SQL:

```sql
SELECT
  user_id,
  SUM(total_amount) AS lifetime_revenue,
  COUNT(DISTINCT order_id) AS completed_orders,
  MIN(order_time) AS first_order_time,
  MAX(order_time) AS last_order_time
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY user_id;
```

Clarifications:

```text
Net or gross revenue?
Include refunds?
Currency conversion?
Use order_time or payment_time?
```

Interview line:

```text
CLV input must clarify revenue definition before aggregation.
```


## 52. Case 40: Dormant Users

Business question:

```text
Find users who were active before but had no activity in the last 30 days.
```

Tables:

```sql
events(user_id, event_time)
```

SQL:

```sql
WITH user_last_activity AS (
  SELECT
    user_id,
    MAX(event_time) AS last_activity_time
  FROM events
  WHERE user_id IS NOT NULL
  GROUP BY user_id
)
SELECT
  user_id,
  last_activity_time
FROM user_last_activity
WHERE last_activity_time < CURRENT_DATE - INTERVAL '30 days'
ORDER BY last_activity_time;
```

Clarifications:

```text
What does active mean?
Should newly signed-up never-active users count as dormant?
Use current_date or analysis date?
```

Interview line:

```text
Dormancy metrics need a clear analysis date and activity definition.
```


## 53. Case 41: Event Sequence Detection

Business question:

```text
Find users who viewed a product and then purchased within 24 hours.
```

Tables:

```sql
events(event_id, user_id, event_name, event_time)
```

SQL:

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
JOIN purchases p
  ON v.user_id = p.user_id
 AND p.purchase_time >= v.view_time
 AND p.purchase_time <  v.view_time + INTERVAL '24 hours';
```

Potential issue:

```text
A user with many views and purchases can create many joined rows.
```

Alternative:

```text
Aggregate to first qualifying purchase or use EXISTS.
```

EXISTS version:

```sql
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

Interview line:

```text
For sequence existence, EXISTS can avoid unnecessary row multiplication.
```


## 54. Case 42: Consecutive Active Days

Business question:

```text
Find users active for at least 3 consecutive days.
```

Tables:

```sql
events(user_id, event_time)
```

SQL:

```sql
WITH user_days AS (
  SELECT DISTINCT
    user_id,
    CAST(event_time AS DATE) AS active_date
  FROM events
  WHERE user_id IS NOT NULL
),
numbered AS (
  SELECT
    user_id,
    active_date,
    active_date - ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY active_date
    ) * INTERVAL '1 day' AS streak_group
  FROM user_days
),
streaks AS (
  SELECT
    user_id,
    MIN(active_date) AS streak_start,
    MAX(active_date) AS streak_end,
    COUNT(*) AS streak_days
  FROM numbered
  GROUP BY user_id, streak_group
)
SELECT *
FROM streaks
WHERE streak_days >= 3
ORDER BY user_id, streak_start;
```

Dialect note:

```text
Date arithmetic syntax varies. Some dialects require DATEADD.
```

Interview line:

```text
Consecutive-day problems often use date minus row_number to create streak groups.
```


## 55. Case 43: Percentile Response Time

Business question:

```text
Calculate p95 ticket resolution time by priority.
```

Tables:

```sql
tickets(ticket_id, priority, created_at, resolved_at)
```

PostgreSQL-style:

```sql
SELECT
  priority,
  PERCENTILE_CONT(0.95) WITHIN GROUP (
    ORDER BY EXTRACT(EPOCH FROM (resolved_at - created_at)) / 3600.0
  ) AS p95_resolution_hours
FROM tickets
WHERE resolved_at IS NOT NULL
GROUP BY priority;
```

Dialect note:

```text
Percentile functions vary across databases.
Approximate percentile may be used in big data warehouses.
```

Interview line:

```text
For latency/SLA metrics, percentiles are often more useful than averages because averages hide long-tail behavior.
```


## 56. Case 44: Revenue Contribution Percent

Business question:

```text
For each product category, calculate revenue and percent of total revenue.
```

Tables:

```sql
orders(order_id, order_status)
order_items(order_id, product_id, quantity, unit_price)
products(product_id, category)
```

SQL:

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

Interview line:

```text
Window aggregate SUM(revenue) OVER () gives total revenue without a separate join.
```


## 57. Case 45: Running Total Revenue

Business question:

```text
Calculate daily revenue and cumulative revenue.
```

Tables:

```sql
orders(order_id, order_time, order_status, total_amount)
```

SQL:

```sql
WITH daily_revenue AS (
  SELECT
    CAST(order_time AS DATE) AS order_date,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY CAST(order_time AS DATE)
)
SELECT
  order_date,
  revenue,
  SUM(revenue) OVER (
    ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS cumulative_revenue
FROM daily_revenue
ORDER BY order_date;
```

Interview line:

```text
Running totals are windowed sums over ordered aggregated data.
```


## 58. Case 46: Latest Successful Payment Per Order

Business question:

```text
Return latest successful payment for each order.
```

Tables:

```sql
payments(payment_id, order_id, payment_time, payment_status, amount)
```

SQL:

```sql
WITH ranked_payments AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY order_id
      ORDER BY payment_time DESC, payment_id DESC
    ) AS rn
  FROM payments
  WHERE payment_status = 'SUCCESS'
)
SELECT
  order_id,
  payment_id,
  payment_time,
  amount
FROM ranked_payments
WHERE rn = 1;
```

Interview line:

```text
Filter to successful payments before ranking if the business asks for latest successful payment.
```


## 59. Case 47: Customers With Increasing Monthly Spend

Business question:

```text
Find customers whose spend increased for three consecutive months.
```

Tables:

```sql
orders(order_id, user_id, order_time, order_status, total_amount)
```

SQL:

```sql
WITH monthly_spend AS (
  SELECT
    user_id,
    DATE_TRUNC('month', order_time) AS order_month,
    SUM(total_amount) AS spend
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id, DATE_TRUNC('month', order_time)
),
with_lags AS (
  SELECT
    user_id,
    order_month,
    spend,
    LAG(spend, 1) OVER (PARTITION BY user_id ORDER BY order_month) AS prev_spend,
    LAG(spend, 2) OVER (PARTITION BY user_id ORDER BY order_month) AS prev2_spend
  FROM monthly_spend
)
SELECT
  user_id,
  order_month,
  prev2_spend,
  prev_spend,
  spend
FROM with_lags
WHERE prev2_spend < prev_spend
  AND prev_spend < spend;
```

Caution:

```text
If missing months should count as zero, join to a calendar/customer-month table first.
```

Interview line:

```text
Trend logic must clarify whether missing periods are ignored or treated as zero.
```


## 60. Case 48: Cancelled Order Rate

Business question:

```text
Calculate cancelled order rate by month.
```

Tables:

```sql
orders(order_id, order_time, order_status)
```

SQL:

```sql
SELECT
  DATE_TRUNC('month', order_time) AS order_month,
  COUNT(DISTINCT order_id) AS total_orders,
  COUNT(DISTINCT CASE WHEN order_status = 'CANCELLED' THEN order_id END) AS cancelled_orders,
  COUNT(DISTINCT CASE WHEN order_status = 'CANCELLED' THEN order_id END) * 1.0
    / NULLIF(COUNT(DISTINCT order_id), 0) AS cancelled_order_rate
FROM orders
GROUP BY DATE_TRUNC('month', order_time)
ORDER BY order_month;
```

Clarifications:

```text
Include test orders?
Use created month or cancellation month?
Statuses final or historical?
```

Interview line:

```text
Status-rate metrics require knowing whether status is current state or event history.
```


## 61. Case 49: Payment Success Rate

Business question:

```text
Calculate payment success rate by payment method.
```

Tables:

```sql
payment_attempts(payment_attempt_id, user_id, payment_method, attempted_at, status)
```

SQL:

```sql
SELECT
  payment_method,
  COUNT(*) AS attempts,
  SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) AS successful_attempts,
  SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) * 1.0
    / NULLIF(COUNT(*), 0) AS success_rate
FROM payment_attempts
WHERE attempted_at >= DATE '2026-01-01'
  AND attempted_at <  DATE '2026-02-01'
GROUP BY payment_method
ORDER BY success_rate DESC;
```

Clarifications:

```text
Attempt-level or order-level success?
Retries can make attempt-level success lower than order-level success.
```

Interview line:

```text
Payment success rate must clarify attempt grain versus order grain.
```


## 62. Case 50: Order-Level Payment Success

Business question:

```text
Calculate order-level payment success rate.
An order is successful if it has at least one successful payment attempt.
```

Tables:

```sql
payment_attempts(payment_attempt_id, order_id, attempted_at, status)
```

SQL:

```sql
WITH order_payment_flags AS (
  SELECT
    order_id,
    MAX(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) AS has_success
  FROM payment_attempts
  WHERE attempted_at >= DATE '2026-01-01'
    AND attempted_at <  DATE '2026-02-01'
  GROUP BY order_id
)
SELECT
  COUNT(*) AS orders_with_attempts,
  SUM(has_success) AS successful_orders,
  SUM(has_success) * 1.0 / NULLIF(COUNT(*), 0) AS order_payment_success_rate
FROM order_payment_flags;
```

Interview line:

```text
If payment attempts are attempt-grain, collapse to order grain before calculating order-level success rate.
```


## 63. Case 51: Daily New vs Returning Users

Business question:

```text
For each day, count new users and returning active users.
```

Tables:

```sql
users(user_id, signup_at)
events(user_id, event_time)
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
user_signup AS (
  SELECT
    user_id,
    CAST(signup_at AS DATE) AS signup_date
  FROM users
)
SELECT
  da.activity_date,
  COUNT(DISTINCT CASE WHEN us.signup_date = da.activity_date THEN da.user_id END) AS new_active_users,
  COUNT(DISTINCT CASE WHEN us.signup_date < da.activity_date THEN da.user_id END) AS returning_active_users
FROM daily_active da
JOIN user_signup us
  ON da.user_id = us.user_id
GROUP BY da.activity_date
ORDER BY da.activity_date;
```

Clarifications:

```text
New active means signed up and active same day?
What about users with missing signup date?
```

Interview line:

```text
New vs returning classification requires comparing activity date to signup date at user-day grain.
```


## 64. Case 52: Activation Rate

Business question:

```text
What percentage of new users completed activation event within 3 days of signup?
```

Tables:

```sql
users(user_id, signup_at)
events(user_id, event_name, event_time)
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
activation AS (
  SELECT
    s.user_id,
    MIN(e.event_time) AS activation_time
  FROM signup_users s
  JOIN events e
    ON s.user_id = e.user_id
   AND e.event_name = 'activation_completed'
   AND e.event_time >= s.signup_at
   AND e.event_time <  s.signup_at + INTERVAL '3 days'
  GROUP BY s.user_id
)
SELECT
  COUNT(*) AS signup_users,
  COUNT(a.user_id) AS activated_users,
  COUNT(a.user_id) * 1.0 / NULLIF(COUNT(*), 0) AS activation_rate
FROM signup_users s
LEFT JOIN activation a
  ON s.user_id = a.user_id;
```

Interview line:

```text
Activation denominator is signup users, so use a left join from signups to activation events.
```


## 65. Case 53: Feature Adoption

Business question:

```text
For each feature, count users who used it at least once in the last 30 days.
```

Tables:

```sql
events(user_id, event_name, event_time)
```

SQL:

```sql
SELECT
  event_name AS feature_name,
  COUNT(DISTINCT user_id) AS adopted_users
FROM events
WHERE event_time >= CURRENT_DATE - INTERVAL '30 days'
  AND user_id IS NOT NULL
  AND event_name LIKE 'feature_%'
GROUP BY event_name
ORDER BY adopted_users DESC;
```

Clarifications:

```text
Which event names count as feature usage?
Active users denominator needed?
Adoption count or adoption rate?
```

Adoption rate version:

```sql
WITH active_users AS (
  SELECT DISTINCT user_id
  FROM events
  WHERE event_time >= CURRENT_DATE - INTERVAL '30 days'
),
feature_users AS (
  SELECT
    event_name,
    COUNT(DISTINCT user_id) AS feature_users
  FROM events
  WHERE event_time >= CURRENT_DATE - INTERVAL '30 days'
    AND event_name LIKE 'feature_%'
  GROUP BY event_name
)
SELECT
  f.event_name,
  f.feature_users,
  f.feature_users * 1.0 / NULLIF((SELECT COUNT(*) FROM active_users), 0) AS adoption_rate
FROM feature_users f;
```

Interview line:

```text
Feature adoption rate needs a denominator, usually active users in the same window.
```


## 66. Case 54: User Segmentation by Spend

Business question:

```text
Segment customers by lifetime spend.
```

Tables:

```sql
orders(order_id, user_id, order_status, total_amount)
```

SQL:

```sql
WITH customer_spend AS (
  SELECT
    user_id,
    SUM(total_amount) AS lifetime_spend
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
)
SELECT
  CASE
    WHEN lifetime_spend >= 10000 THEN 'HIGH'
    WHEN lifetime_spend >= 1000 THEN 'MEDIUM'
    ELSE 'LOW'
  END AS spend_segment,
  COUNT(*) AS customers,
  AVG(lifetime_spend) AS avg_lifetime_spend
FROM customer_spend
GROUP BY
  CASE
    WHEN lifetime_spend >= 10000 THEN 'HIGH'
    WHEN lifetime_spend >= 1000 THEN 'MEDIUM'
    ELSE 'LOW'
  END
ORDER BY customers DESC;
```

Interview line:

```text
Segmenting by spend requires first aggregating to customer grain.
```


## 67. Case 55: Active Users by Country

Business question:

```text
Calculate daily active users by country.
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
  WHERE event_time >= DATE '2026-01-01'
    AND event_time <  DATE '2026-02-01'
    AND user_id IS NOT NULL
)
SELECT
  da.activity_date,
  COALESCE(u.country, 'UNKNOWN') AS country,
  COUNT(DISTINCT da.user_id) AS active_users
FROM daily_active da
LEFT JOIN users u
  ON da.user_id = u.user_id
GROUP BY
  da.activity_date,
  COALESCE(u.country, 'UNKNOWN')
ORDER BY
  da.activity_date,
  country;
```

Why daily_active CTE:

```text
Deduplicates user-day before joining to users.
```

Validation:

```text
Ensure users has one row per user_id or join can duplicate active users.
```

Interview line:

```text
When adding dimensions to active-user metrics, validate dimension table uniqueness.
```


## 68. Case 56: Users With No Orders

Business question:

```text
Find users who signed up but never placed a completed order.
```

Tables:

```sql
users(user_id, signup_at)
orders(order_id, user_id, order_status)
```

SQL:

```sql
WITH completed_order_users AS (
  SELECT DISTINCT user_id
  FROM orders
  WHERE order_status = 'COMPLETED'
    AND user_id IS NOT NULL
)
SELECT
  u.user_id,
  u.signup_at
FROM users u
LEFT JOIN completed_order_users o
  ON u.user_id = o.user_id
WHERE o.user_id IS NULL;
```

Interview line:

```text
Anti-join patterns use LEFT JOIN ... WHERE right key IS NULL or NOT EXISTS.
```


## 69. Case 57: Products Never Sold

Business question:

```text
Find products that have never been sold in completed orders.
```

Tables:

```sql
products(product_id, category)
order_items(order_id, product_id)
orders(order_id, order_status)
```

SQL:

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
WHERE s.product_id IS NULL;
```

Interview line:

```text
Build a distinct sold-products set first, then anti-join from product dimension.
```


## 70. Case 58: Most Recent Login Device

Business question:

```text
Find each user's most recent login device.
```

Tables:

```sql
events(event_id, user_id, event_name, event_time, device_type)
```

SQL:

```sql
WITH ranked_logins AS (
  SELECT
    user_id,
    device_type,
    event_time,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY event_time DESC, event_id DESC
    ) AS rn
  FROM events
  WHERE event_name = 'login'
    AND user_id IS NOT NULL
)
SELECT
  user_id,
  device_type AS latest_login_device,
  event_time AS latest_login_time
FROM ranked_logins
WHERE rn = 1;
```

Interview line:

```text
Use ROW_NUMBER when retrieving attributes from the latest event row.
```


## 71. Case 59: Abandoned Cart Rate

Business question:

```text
Calculate cart abandonment rate.
A cart is abandoned if add_to_cart occurred but no purchase occurred in same session.
```

Tables:

```sql
events(user_id, session_id, event_name, event_time)
```

SQL:

```sql
WITH session_flags AS (
  SELECT
    session_id,
    MAX(CASE WHEN event_name = 'add_to_cart' THEN 1 ELSE 0 END) AS has_add_to_cart,
    MAX(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) AS has_purchase
  FROM events
  WHERE session_id IS NOT NULL
  GROUP BY session_id
)
SELECT
  SUM(CASE WHEN has_add_to_cart = 1 THEN 1 ELSE 0 END) AS cart_sessions,
  SUM(CASE WHEN has_add_to_cart = 1 AND has_purchase = 0 THEN 1 ELSE 0 END) AS abandoned_cart_sessions,
  SUM(CASE WHEN has_add_to_cart = 1 AND has_purchase = 0 THEN 1 ELSE 0 END) * 1.0
    / NULLIF(SUM(CASE WHEN has_add_to_cart = 1 THEN 1 ELSE 0 END), 0) AS abandonment_rate
FROM session_flags;
```

Clarifications:

```text
Same session or within time window?
Purchase after cart only?
Multiple carts per session?
```

Interview line:

```text
For session metrics, collapse events to session flags first.
```


## 72. Case 60: Data Freshness Check

Business question:

```text
Check whether the latest event data is fresh.
```

Tables:

```sql
events(event_id, event_time, ingested_at)
```

SQL:

```sql
SELECT
  MAX(event_time) AS latest_event_time,
  MAX(ingested_at) AS latest_ingested_at,
  CURRENT_TIMESTAMP - MAX(ingested_at) AS ingestion_lag
FROM events;
```

Threshold example:

```sql
SELECT
  CASE
    WHEN MAX(ingested_at) < CURRENT_TIMESTAMP - INTERVAL '2 hours'
    THEN 'STALE'
    ELSE 'FRESH'
  END AS freshness_status,
  MAX(ingested_at) AS latest_ingested_at
FROM events;
```

Interview line:

```text
Freshness checks should monitor ingestion time and sometimes source event time separately.
```


## 73. Performance Principles for Business SQL

Performance considerations:

```text
filter early
select only needed columns
aggregate before joining when possible
avoid joining at too-detailed grain when metric is higher grain
avoid unnecessary DISTINCT
watch COUNT DISTINCT cost
validate join cardinality
use partition/date filters
use indexes/clustering/partition pruning where available
avoid functions on partition columns if it prevents pruning
pre-aggregate large fact tables for dashboards
use approximate distinct only when acceptable
```

Good pattern:

```sql
WITH filtered_orders AS (
  SELECT order_id, user_id, order_time, total_amount
  FROM orders
  WHERE order_time >= DATE '2026-01-01'
    AND order_time <  DATE '2026-02-01'
    AND order_status = 'COMPLETED'
)
SELECT ...
FROM filtered_orders;
```

Interview line:

```text
I optimize business SQL by filtering early, aggregating at the right grain, and avoiding join-induced row explosion.
```


## 74. Business SQL Edge Cases

Common edge cases:

```text
duplicate event IDs
duplicate user dimension rows
orders with multiple payment attempts
orders with multiple item rows
refund amount sign ambiguity
multi-currency revenue
NULL user_id
test/internal users
cancelled/refunded statuses
late-arriving events
timezone differences
missing calendar dates
missing dimension rows
many-to-many joins
division by zero
first month no previous period
same timestamp ties
current state vs history table
active interval boundary inclusivity
cohort denominator changes
funnel step order ambiguity
session vs user grain ambiguity
```

Interview line:

```text
Business SQL requires edge-case thinking because metrics can be technically valid SQL but business-wrong.
```


## 75. Common Mistakes

Common mistakes:

```text
not clarifying metric definition
not identifying grain
using COUNT(*) instead of COUNT DISTINCT
summing DAU to get MAU
joining orders to order_items then calculating AOV incorrectly
using INNER JOIN when denominator requires LEFT JOIN
not handling NULL denominator
not filtering to valid statuses
not excluding test users
ignoring duplicate rows
using MIN timestamp with unrelated columns
not adding tie-breaker in ROW_NUMBER
not validating dimension uniqueness
not checking row counts before/after join
not using calendar table for missing dates
not handling timezone
not explaining assumptions
```

Strict feedback:

```text
This query may run, but it is not interview-ready because it can double-count revenue after joining order_items and does not define the output grain.
```


## 76. Pattern Classification Drill

Classify each prompt.

```text
1. Count users active each day.
2. Count users active in a month.
3. Find first event per user.
4. Find latest status per order.
5. Calculate percentage of users who purchased after signup.
6. Build retention by signup cohort.
7. Calculate rolling 7-day revenue.
8. Calculate month-over-month growth.
9. Find records missing from target.
10. Find duplicate events.
11. Calculate order-level add-on attach rate from item table.
12. Join orders to plan active at order time.
13. Find users with no orders.
14. Calculate top product per category.
15. Calculate churn rate.
16. Detect missing daily partitions.
17. Calculate payment success by attempt.
18. Calculate payment success by order.
19. Find users active 3 consecutive days.
20. Calculate p95 resolution time.
```

Expected classification:

```text
1. distinct user daily aggregation
2. distinct user monthly aggregation
3. ROW_NUMBER first row
4. ROW_NUMBER latest row
5. conversion with left join denominator
6. cohort analysis
7. rolling window sum
8. LAG growth calculation
9. full outer reconciliation
10. GROUP BY HAVING COUNT > 1
11. collapse item grain to order grain
12. as-of interval join
13. anti-join
14. rank within group
15. active-at-start denominator
16. calendar anti-join
17. attempt-grain rate
18. collapse attempts to order grain
19. gaps-and-islands
20. percentile aggregate
```

Passing standard:

```text
18/20 correct before timed business SQL mocks.
```


## 77. High-ROI Business SQL Topics

Practice these first.

| Topic | Must Know |
|---|---|
| metric definition | clarify denominator/numerator |
| grain | input/output row meaning |
| active users | COUNT DISTINCT user_id |
| revenue | status/refund/currency definition |
| first/latest | ROW_NUMBER |
| dedupe | partition by key order by timestamp |
| retention | cohort denominator |
| funnel | ordered steps and grain |
| churn | denominator at period start |
| rolling metrics | window over calendar dates |
| growth | LAG and safe division |
| top N | ROW_NUMBER/RANK |
| reconciliation | FULL OUTER JOIN |
| anti-join | LEFT JOIN IS NULL / NOT EXISTS |
| as-of join | effective date intervals |
| data quality | nulls, duplicates, orphan facts |
| safe division | NULLIF |
| date filters | half-open intervals |
| calendar table | missing dates/zero days |
| performance | filter early, aggregate before join |


## 78. 7-Day Business SQL Plan

### Day 1: Metric basics

Problems:

```text
DAU
MAU
new users
revenue by day
AOV
top customers
```

Focus:

```text
grain
COUNT DISTINCT
date filters
safe division
```

### Day 2: First/latest/dedupe

Problems:

```text
first event per user
latest status per order
latest payment per order
duplicate events
current SCD row
```

Focus:

```text
ROW_NUMBER
tie-breakers
dedupe rules
```

### Day 3: Conversion and funnels

Problems:

```text
first purchase conversion
activation rate
user funnel
session funnel
abandoned cart rate
```

Focus:

```text
denominator
left joins
step order
session vs user grain
```

### Day 4: Retention and churn

Problems:

```text
day-1 retention
retention matrix
churned subscribers
monthly churn rate
dormant users
```

Focus:

```text
cohorts
active state
period denominator
```

### Day 5: Windows and trends

Problems:

```text
rolling 7-day revenue
MoM growth
running total
top product per category
consecutive active days
```

Focus:

```text
window functions
calendar dates
ranking
LAG
```

### Day 6: Reconciliation and quality

Problems:

```text
source-target reconciliation
missing partitions
null rate
orphan facts
schema snapshot checks
```

Focus:

```text
full outer join
anti-join
data quality
validation
```

### Day 7: Mock and repair

Tasks:

```text
Run business SQL mock.
Review mistakes.
Repair weakest topic.
Update progress.
```


## 79. 30-Day Business SQL Plan

### Week 1: Core metric SQL

Focus:

```text
active users
revenue
orders
new users
AOV
top N
safe division
date filters
```

Exit:

```text
Candidate can solve basic business metrics correctly.
```

### Week 2: Windows and deduplication

Focus:

```text
ROW_NUMBER
RANK
LAG
running totals
rolling windows
latest records
dedupe
```

Exit:

```text
Candidate can solve first/latest/trend problems.
```

### Week 3: Product analytics

Focus:

```text
retention
cohorts
funnels
activation
churn
feature adoption
segmentation
```

Exit:

```text
Candidate can solve product/business analytics cases.
```

### Week 4: Data Engineering SQL

Focus:

```text
reconciliation
data quality
as-of joins
SCD
orphan facts
missing partitions
performance
mock interviews
```

Exit:

```text
Average mock score >= 4/5.
```


## 80. Mock Set 1: Core Business Metrics

Problems:

```text
1. Daily active users.
2. Monthly active users.
3. Revenue by day.
4. Average order value.
5. Top customers by revenue.
```

Expected skills:

```text
COUNT DISTINCT
GROUP BY
date filters
status filters
safe aggregation
```

Passing standard:

```text
Average score >= 4/5.
Candidate clarifies grain and metric definition.
```


## 81. Mock Set 2: Product Analytics

Problems:

```text
1. First purchase conversion within 7 days.
2. Day-1 retention.
3. Funnel conversion.
4. Activation rate.
5. Feature adoption rate.
```

Expected skills:

```text
cohorts
left joins
denominators
event ordering
COUNT DISTINCT
```

Passing standard:

```text
Average score >= 4/5.
Candidate preserves correct denominator and explains assumptions.
```


## 82. Mock Set 3: Windows and Time Series

Problems:

```text
1. Latest status per order.
2. Rolling 7-day revenue.
3. Month-over-month growth.
4. Top product per category.
5. Consecutive active days.
```

Expected skills:

```text
ROW_NUMBER
RANK
LAG
rolling windows
gaps-and-islands
calendar dates
```

Passing standard:

```text
Average score >= 4/5.
Candidate uses deterministic tie-breakers and handles missing periods.
```


## 83. Mock Set 4: Data Engineering SQL Cases

Problems:

```text
1. Source-target reconciliation.
2. Missing daily partitions.
3. Orphan fact records.
4. As-of join to active dimension row.
5. Data quality null/duplicate report.
```

Expected skills:

```text
FULL OUTER JOIN
anti-join
calendar table
effective interval join
data quality checks
join validation
```

Passing standard:

```text
Average score >= 4/5.
Candidate validates output and explains production relevance.
```


## 84. Timed Drill Protocol

Use this timing protocol.

### Simple metric

```text
10-20 minutes
```

### Product analytics case

```text
25-40 minutes
```

### Complex DE SQL case

```text
35-45 minutes
```

Per drill:

```text
Minute 0-3:
Clarify metric definition and grain.

Minute 3-6:
Identify tables, filters, joins, and edge cases.

Minute 6-25:
Write CTE-based SQL.

Minute 25-35:
Validate row counts, duplicates, denominator, join behavior.

Minute 35-45:
Explain assumptions, performance, and production concerns.
```

If candidate starts SQL without clarifying metric:

```text
Stop and force definition/grain clarification first.
```


## 85. Review Checklist

Review business SQL answers using:

```text
1. Did candidate clarify metric definition?
2. Did candidate identify input table grain?
3. Did candidate identify output grain?
4. Did candidate choose correct timestamp?
5. Did candidate use half-open date window?
6. Did candidate filter valid statuses?
7. Did candidate handle test/internal records if relevant?
8. Did candidate avoid double counting?
9. Did candidate use COUNT DISTINCT when needed?
10. Did candidate aggregate at correct grain before joining?
11. Did candidate use correct join type?
12. Did candidate preserve denominator with LEFT JOIN when needed?
13. Did candidate handle NULLs?
14. Did candidate avoid divide-by-zero?
15. Did candidate use window functions correctly?
16. Did candidate add deterministic tie-breakers?
17. Did candidate validate duplicates and row counts?
18. Did candidate explain edge cases?
19. Did candidate explain performance?
20. Did candidate communicate assumptions clearly?
```

Verdict examples:

```text
Runs but wrong denominator.
Correct aggregation but wrong grain.
Good metric but no edge cases.
Good SQL but no validation.
Good answer but dialect-specific without saying so.
Interview-ready.
Strong.
```


## 86. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| No metric clarification | Definition-first drills |
| Grain confusion | Fact/dimension grain drills |
| Double counting | Join cardinality drills |
| Wrong denominator | Conversion/retention drills |
| COUNT vs COUNT DISTINCT confusion | Active-user drills |
| Latest row mistakes | ROW_NUMBER drills |
| Growth calculation errors | LAG + safe division drills |
| Rolling window errors | Calendar + window drills |
| Funnel ordering errors | Ordered event drills |
| Retention denominator errors | Cohort drills |
| Churn denominator errors | Active-at-start drills |
| Reconciliation weak | FULL OUTER JOIN drills |
| Anti-join weak | LEFT JOIN IS NULL drills |
| As-of join weak | Effective interval drills |
| No validation | Data-quality checklist drills |
| Poor communication | Assumption summary drills |

If weakness repeats:

```text
Use weakness-repair-mode.md.
```


## 87. Communication Scripts

### Metric clarification script

```text
Before writing SQL, I want to confirm the metric definition, timestamp column, valid statuses, timezone, and output grain.
```

### Grain script

```text
This table is event-grain, but the metric is user-day grain, so I need to deduplicate to one row per user per day before aggregating.
```

### Join script

```text
I will use a left join because the denominator is all signup users, including users who did not purchase.
```

### Double-counting script

```text
Since order_items is item-grain, I will aggregate to order grain first before calculating order-level metrics.
```

### Window script

```text
I use ROW_NUMBER with a deterministic tie-breaker to get the latest row per entity.
```

### Retention script

```text
The cohort size is the denominator and should remain fixed for each cohort period.
```

### Reconciliation script

```text
I use a full outer join so records missing from either side are visible.
```

### Validation script

```text
After the query, I would validate row counts, duplicate output keys, missing joins, and whether the metric range is reasonable.
```


## 88. Candidate Self-Review Questions

After every business SQL problem, candidate should answer:

```text
1. What exactly is the metric?
2. What is the denominator?
3. What is the numerator?
4. What is the output grain?
5. What is the input table grain?
6. Which timestamp is used?
7. What is the time window?
8. What statuses are valid?
9. Are test users/orders excluded?
10. Are duplicates possible?
11. Can joins multiply rows?
12. Should denominator use LEFT JOIN?
13. Should COUNT DISTINCT be used?
14. Are NULLs handled?
15. Is divide-by-zero handled?
16. Are tie-breakers deterministic?
17. Are missing calendar dates needed?
18. How will output be validated?
19. What are the edge cases?
20. How would this scale in production?
```

If candidate cannot answer these:

```text
The business SQL solution is not interview-ready.
```


## 89. Maintenance Drills

After completing business SQL cases, maintain skill with:

```text
1 active-user/revenue drill per week
1 conversion/funnel drill per week
1 retention/churn drill every 2 weeks
1 window-function drill per week
1 reconciliation/data-quality drill every 2 weeks
1 full business SQL mock every month
```

Maintenance rotation:

```text
Week 1: DAU/MAU/revenue/AOV
Week 2: funnel/conversion/activation
Week 3: retention/churn/cohorts
Week 4: reconciliation/as-of/data quality/windows
```

If score drops below 4:

```text
Run weakness-repair-mode.md for failed topic.
```


## 90. Progress Tracking Template

Use this progress format.

```text
# Business SQL Cases Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

Metric clarification:
Grain identification:
Date filters:
COUNT DISTINCT:
Safe division:
DAU/MAU:
Revenue:
AOV:
Top N:
First/latest:
Deduplication:
Conversion:
Funnel:
Retention:
Cohorts:
Churn:
Rolling metrics:
MoM growth:
Ranking:
Reconciliation:
Anti-joins:
Data quality:
As-of joins:
SCD snapshots:
Calendar tables:
Join cardinality:
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

Candidate passes business SQL cases when they can solve/explain:

```text
1. Daily active users.
2. Monthly active users.
3. DAU/MAU stickiness.
4. New users by day.
5. First event per user.
6. Latest status per order.
7. Revenue by day.
8. Net revenue with refunds.
9. Average order value.
10. Top customers by revenue.
11. Repeat purchase rate.
12. First purchase conversion.
13. Day-1 retention.
14. Retention matrix.
15. Churned subscribers.
16. Monthly churn rate.
17. User funnel conversion.
18. Session funnel conversion.
19. Rolling 7-day revenue.
20. Month-over-month growth.
21. Top product per category.
22. Inventory stockout days.
23. SLA response rate.
24. Time to resolution.
25. Campaign ROI.
26. Acquisition cost.
27. Marketplace buyer/seller metrics.
28. Fraud velocity rule.
29. Duplicate events.
30. Source-target reconciliation.
31. Missing daily partitions.
32. Data quality null rate.
33. Orphan fact records.
34. Current SCD row.
35. As-of join.
36. Active subscription snapshot.
37. Product attach rate.
38. Basket size.
39. Customer lifetime input.
40. Dormant users.
41. Event sequence detection.
42. Consecutive active days.
43. Percentile response time.
44. Revenue contribution percent.
45. Running total revenue.
```

Passing standard:

```text
Average score >= 4/5.
No grain confusion.
No unvalidated denominator.
No unsafe division.
No double counting from joins.
No missing assumptions.
Can communicate business meaning clearly.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles edge cases, join cardinality, windows, cohorts, reconciliation, performance, and metric ambiguity under pressure.
```


## 92. Final Summary

Business SQL cases are one of the most important interview areas for Data Engineering roles.

They map directly to:

```text
KPI pipelines
dashboard tables
data marts
warehouse transformations
reconciliation jobs
data-quality checks
product analytics
marketing analytics
subscription analytics
marketplace analytics
support analytics
financial reporting
SCD snapshots
as-of joins
pipeline audits
```

The candidate must master:

```text
metric definition
grain
CTEs
date windows
COUNT DISTINCT
safe division
joins
aggregation
window functions
retention
churn
funnels
conversion
rolling metrics
growth rates
reconciliation
anti-joins
data quality
as-of joins
calendar tables
deduplication
performance
communication
```

The mentor must be strict:

```text
No metric clarification → not interview-ready.
No grain explanation → not interview-ready.
Double counting risk → not interview-ready.
Wrong denominator → not interview-ready.
No NULL/divide-by-zero handling → not interview-ready.
No validation → not interview-ready.
```

The goal is not to memorize SQL snippets.

The goal is to reliably translate business questions into correct, explainable, validated SQL.


## 93. Problem Card Appendix

### Card 1: DAU

Topic:

```text
distinct user-day
```

Core idea:

```text
Count distinct active users per date.
```

Data Engineering connection:

```text
Product usage KPI.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: MAU

Topic:

```text
distinct user-month
```

Core idea:

```text
Count distinct active users per month.
```

Data Engineering connection:

```text
Product usage KPI.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Revenue by Day

Topic:

```text
fact aggregation
```

Core idea:

```text
Sum successful payment/order amount.
```

Data Engineering connection:

```text
Finance KPI.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: AOV

Topic:

```text
order grain
```

Core idea:

```text
Revenue divided by completed orders.
```

Data Engineering connection:

```text
Commerce KPI.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Top Customers

Topic:

```text
groupby + top N
```

Core idea:

```text
Rank users by revenue.
```

Data Engineering connection:

```text
Customer analytics.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: First Event

Topic:

```text
ROW_NUMBER
```

Core idea:

```text
Get first event attributes.
```

Data Engineering connection:

```text
User journey.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Latest Status

Topic:

```text
ROW_NUMBER desc
```

Core idea:

```text
Get current state from history.
```

Data Engineering connection:

```text
Operational reporting.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Conversion

Topic:

```text
left join denominator
```

Core idea:

```text
Signup to purchase.
```

Data Engineering connection:

```text
Growth analytics.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Retention

Topic:

```text
cohort denominator
```

Core idea:

```text
Activity after signup.
```

Data Engineering connection:

```text
Product analytics.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Funnel

Topic:

```text
ordered events
```

Core idea:

```text
Step conversion.
```

Data Engineering connection:

```text
Product analytics.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Churn

Topic:

```text
active-at-start
```

Core idea:

```text
Ended subscriptions over starting active.
```

Data Engineering connection:

```text
Subscription analytics.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Rolling Revenue

Topic:

```text
window sum
```

Core idea:

```text
Moving 7-day revenue.
```

Data Engineering connection:

```text
Trend monitoring.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: MoM Growth

Topic:

```text
LAG
```

Core idea:

```text
Compare month to previous month.
```

Data Engineering connection:

```text
Executive reporting.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Top Product

Topic:

```text
rank per category
```

Core idea:

```text
Best seller per category.
```

Data Engineering connection:

```text
Merchandising.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Reconciliation

Topic:

```text
FULL OUTER JOIN
```

Core idea:

```text
Compare source and warehouse.
```

Data Engineering connection:

```text
DE validation.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Missing Partitions

Topic:

```text
calendar anti-join
```

Core idea:

```text
Find missing dates.
```

Data Engineering connection:

```text
Pipeline monitoring.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Orphan Facts

Topic:

```text
anti-join
```

Core idea:

```text
Find facts missing dimensions.
```

Data Engineering connection:

```text
Data quality.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: As-of Join

Topic:

```text
effective interval
```

Core idea:

```text
Join fact to historical dimension.
```

Data Engineering connection:

```text
SCD logic.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Attach Rate

Topic:

```text
collapse to order grain
```

Core idea:

```text
Order includes add-on.
```

Data Engineering connection:

```text
Commerce analytics.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Consecutive Days

Topic:

```text
gaps and islands
```

Core idea:

```text
Find streaks.
```

Data Engineering connection:

```text
Engagement analytics.
```

Candidate must be able to explain:

```text
1. Metric definition.
2. Input grain.
3. Output grain.
4. SQL pattern.
5. Edge cases.
6. Validation query/check.
7. Performance note.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 94. Data Engineering Scenario Appendix

### Scenario 1: Dashboard DAU Drop

Pattern:

```text
active users + validation
```

Task:

```text
Debug sudden drop in daily active users.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: Revenue Mismatch

Pattern:

```text
source-target reconciliation
```

Task:

```text
Find why finance source and warehouse differ.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: Funnel Dropoff

Pattern:

```text
ordered funnel
```

Task:

```text
Calculate where users drop in checkout.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: Cohort Retention

Pattern:

```text
cohort matrix
```

Task:

```text
Build retention table for signup cohorts.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: Subscription Churn

Pattern:

```text
active at start
```

Task:

```text
Calculate churn rate correctly.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: Campaign Performance

Pattern:

```text
ROI attribution
```

Task:

```text
Compute ROI by campaign.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: Duplicate Events

Pattern:

```text
dedupe
```

Task:

```text
Find and remove duplicate event rows.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: Late Status Updates

Pattern:

```text
latest row
```

Task:

```text
Find current order status from history.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: Historical Plan Join

Pattern:

```text
as-of join
```

Task:

```text
Join orders to plan at order time.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: Missing Daily Loads

Pattern:

```text
calendar anti-join
```

Task:

```text
Find dates with no data.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: Join Explosion

Pattern:

```text
cardinality
```

Task:

```text
Detect dimension duplicates before join.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Refund Handling

Pattern:

```text
net revenue
```

Task:

```text
Subtract refunds correctly.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: Support SLA

Pattern:

```text
duration metric
```

Task:

```text
Measure first response SLA.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Marketplace Metrics

Pattern:

```text
role-based distinct counts
```

Task:

```text
Count buyers and sellers separately.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: Fraud Velocity

Pattern:

```text
rolling window
```

Task:

```text
Find high-frequency order users.
```

Minimum expected answer:

```text
1. Clarify business definition.
2. Identify grain and tables.
3. Write SQL or pseudocode.
4. Explain edge cases.
5. Explain validation.
6. Explain production performance considerations.
```

Passing score:

```text
4/5 or higher.
```


## 95. Drill Appendix

### Drill 1: Definition Drill

Task:

```text
For each metric, state numerator, denominator, grain, and filters.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Grain Drill

Task:

```text
Identify table grain and output grain before writing SQL.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: COUNT Drill

Task:

```text
Choose COUNT, COUNT column, or COUNT DISTINCT.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Date Drill

Task:

```text
Write half-open date filters and date groupings.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Safe Division Drill

Task:

```text
Add NULLIF to all ratio metrics.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: First/Latest Drill

Task:

```text
Use ROW_NUMBER with tie-breaker.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Dedupe Drill

Task:

```text
Detect duplicates and keep latest by rule.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Join Drill

Task:

```text
Choose inner, left, full outer, or anti-join.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Cardinality Drill

Task:

```text
Predict row multiplication risk.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Aggregation Drill

Task:

```text
Aggregate to correct grain before final metric.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Conversion Drill

Task:

```text
Preserve denominator with left join.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Retention Drill

Task:

```text
Use cohort size denominator.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Funnel Drill

Task:

```text
Enforce step order and grain.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Churn Drill

Task:

```text
Use active-at-start denominator.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Rolling Drill

Task:

```text
Use calendar and window functions.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Growth Drill

Task:

```text
Use LAG and safe division.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Reconciliation Drill

Task:

```text
Use full outer join and status labels.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Data Quality Drill

Task:

```text
Null rate, duplicate, orphan fact checks.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 19: As-of Drill

Task:

```text
Join using effective_from/effective_to.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 20: Performance Drill

Task:

```text
Filter early and aggregate before joining.
```

Minimum passing answer:

```text
1. State business assumption.
2. State SQL pattern.
3. Write correct query or query skeleton.
4. Identify edge case.
5. State validation check.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 96. Quick Reference Cards

### Quick Card 1: DAU

Summary:

```text
COUNT DISTINCT user_id by activity date.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 2: MAU

Summary:

```text
COUNT DISTINCT user_id by activity month.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 3: AOV

Summary:

```text
Revenue / completed orders at order grain.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 4: Conversion

Summary:

```text
Converted entities / eligible denominator.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 5: Retention

Summary:

```text
Returned users / cohort users.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 6: Churn

Summary:

```text
Churned users / active users at period start.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 7: Funnel

Summary:

```text
Ordered step completion at user/session grain.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 8: First row

Summary:

```text
ROW_NUMBER order ascending.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 9: Latest row

Summary:

```text
ROW_NUMBER order descending.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 10: Top per group

Summary:

```text
ROW_NUMBER or RANK partitioned by group.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 11: Rolling metric

Summary:

```text
Window over ordered calendar dates.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 12: MoM growth

Summary:

```text
LAG previous period plus safe division.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 13: Reconciliation

Summary:

```text
FULL OUTER JOIN with status labels.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 14: Anti-join

Summary:

```text
LEFT JOIN right key IS NULL or NOT EXISTS.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 15: As-of join

Summary:

```text
fact time between effective_from/effective_to.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 16: Safe division

Summary:

```text
numerator / NULLIF(denominator, 0).
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 17: Calendar

Summary:

```text
Needed for missing dates and zero-activity periods.
```

Interview check:

```text
Give one SQL example and one edge case.
```

### Quick Card 18: Double counting

Summary:

```text
Aggregate to target grain before metric.
```

Interview check:

```text
Give one SQL example and one edge case.
```


## 97. Business SQL FAQ

### FAQ 1: Why not sum DAU to get MAU?

Answer:

```text
Users active on multiple days would be counted multiple times. Count distinct users at monthly grain.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 2: Why use LEFT JOIN for conversion?

Answer:

```text
The denominator includes users who did not convert, so they must be preserved.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 3: Why can joining order_items break AOV?

Answer:

```text
It changes order-grain rows into item-grain rows, causing repeated orders.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 4: Why use ROW_NUMBER instead of MIN timestamp?

Answer:

```text
ROW_NUMBER lets you return other columns from the same first/latest row.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 5: Why use FULL OUTER JOIN for reconciliation?

Answer:

```text
It detects missing records from both source and target.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 6: Why use calendar table?

Answer:

```text
It includes dates with zero events/orders and catches missing partitions.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 7: Why use NULLIF in ratios?

Answer:

```text
It prevents divide-by-zero errors and makes empty denominator behavior explicit.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 8: Why validate join cardinality?

Answer:

```text
Unexpected many-to-many joins can multiply rows and corrupt metrics.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 9: Why define timezone?

Answer:

```text
Daily/monthly grouping changes when timestamps cross timezone boundaries.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```

### FAQ 10: Why clarify status filters?

Answer:

```text
Business metrics usually include only valid/completed/successful states.
```

Candidate should also explain:

```text
1. What mistake this prevents.
2. How to validate the query.
3. What edge case can still exist.
```
