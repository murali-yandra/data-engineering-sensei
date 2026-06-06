# SQL Window Functions Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/sql/window-functions.md
```

This guide teaches and drills **SQL window functions for Data Engineering interviews**.

This is not a generic SQL syntax note. It is an interview-focused guide for candidates who need to solve ranking, deduplication, latest record, first record, running totals, moving averages, previous/next row comparison, gaps and islands, sessionization, cumulative metrics, percent-of-total, top-N per group, cohort analysis, SCD preparation, CDC current-state logic, and business analytics questions.

Window functions are high-ROI because Data Engineering interviews often ask:

- Find the latest row per user.
- Deduplicate records by business key.
- Find top 3 products per category.
- Calculate running revenue by day.
- Calculate 7-day moving average.
- Compare current month revenue to previous month revenue.
- Calculate user order number.
- Find first purchase per customer.
- Find users with consecutive activity days.
- Sessionize events by 30-minute gap.
- Find duplicate source rows before MERGE.
- Build current state from CDC events.
- Calculate percent of total revenue.
- Calculate conversion funnel step order.
- Detect status changes.
- Find gaps between events.
- Rank customers by revenue.
- Find second highest salary or second latest event.
- Validate SCD current records.
- Explain why filtering window results needs CTE/QUALIFY.

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
- `practice/sql/joins.md`
- `practice/sql/query-optimization.md`
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

The purpose of this guide is to make the candidate strong at SQL window functions for Data Engineering interviews.

The candidate should learn to answer:

```text
What is a window function?
What is the difference between GROUP BY and window functions?
What does PARTITION BY do?
What does ORDER BY inside OVER do?
What is a window frame?
When should I use ROW_NUMBER?
When should I use RANK?
When should I use DENSE_RANK?
When should I use LAG and LEAD?
How do I get latest row per key?
How do I deduplicate records?
How do I calculate running totals?
How do I calculate moving averages?
How do I calculate percent of total?
How do I find top N per group?
How do I compare current row to previous row?
How do I build streaks and sessions?
How do I filter window function results?
How do I optimize window function queries?
```

A candidate is interview-ready only when they can:

```text
explain window functions without jargon
distinguish GROUP BY from window functions
use PARTITION BY correctly
use ORDER BY correctly
choose ROW_NUMBER vs RANK vs DENSE_RANK
use LAG and LEAD for previous/next row logic
use SUM/AVG/COUNT as window aggregates
define running total and moving window frames
deduplicate with ROW_NUMBER and deterministic tie-breakers
filter window results using CTE/subquery/QUALIFY
solve top-N per group
solve first/latest row per entity
solve percent-of-total
solve cumulative metrics
solve retention/session/streak style problems
handle NULLs and ties intentionally
validate output grain and duplicate keys
explain performance trade-offs
```


## 2. Why Window Functions Matter for Data Engineers

Window functions are used heavily in Data Engineering because many pipeline and analytics problems require row-level detail plus group-level context.

They let you answer questions like:

```text
What is this user's latest record?
What is this order's rank within the customer?
What was the previous event before this event?
What is the running total through this date?
What is each category's share of total revenue?
Which records should survive deduplication?
Where did a session start?
Where did a status change?
What is the first purchase after signup?
What is the 7-day moving average?
```

Window functions are important because they avoid common bad patterns:

```text
self joins for previous row
correlated subqueries for group comparisons
messy nested queries for ranking
JOIN + GROUP BY that loses row-level detail
DISTINCT hiding duplicate logic
```

Weak answer:

```text
Use row_number.
```

Strong answer:

```text
I will use ROW_NUMBER partitioned by the business key and ordered by updated_at descending plus ingested_at descending as a tie-breaker. Then I will filter rn = 1 in a CTE to keep one deterministic latest row per key.
```

Interview line:

```text
Window functions are how SQL keeps row-level detail while adding group-aware calculations.
```


## 3. Core Mental Model

A window function looks across a set of related rows while keeping every row visible.

Basic shape:

```sql
function_name(...) OVER (
  PARTITION BY group_columns
  ORDER BY ordering_columns
  ROWS BETWEEN ... AND ...
)
```

Think of it as:

```text
PARTITION BY:
Which group of rows should this row compare against?

ORDER BY:
In what order should rows be evaluated inside that group?

Frame:
Which rows around the current row should be included?
```

Example:

```sql
SELECT
  user_id,
  order_id,
  order_time,
  ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY order_time
  ) AS user_order_number
FROM orders;
```

Meaning:

```text
For each user, order their orders by time and assign 1, 2, 3, ...
```

Core interview line:

```text
PARTITION BY defines the group, ORDER BY defines the sequence, and the window function calculates a value while preserving row-level output.
```


## 4. Vocabulary

Important terms:

```text
Window function:
A function that computes over a related set of rows while preserving individual rows.

OVER:
Clause that defines the window.

PARTITION BY:
Splits rows into groups for the window function.

ORDER BY:
Defines row order inside each partition.

Window frame:
Limits which rows in the ordered partition are included.

Current row:
The row currently being evaluated.

Peer rows:
Rows tied on ORDER BY values.

ROW_NUMBER:
Assigns unique sequence numbers.

RANK:
Assigns same rank to ties and skips rank numbers.

DENSE_RANK:
Assigns same rank to ties without rank gaps.

LAG:
Reads a value from a previous row.

LEAD:
Reads a value from a future row.

FIRST_VALUE:
Reads first value in a window.

LAST_VALUE:
Reads last value in a window. Requires frame awareness.

NTILE:
Splits rows into buckets.

CUME_DIST:
Cumulative distribution.

PERCENT_RANK:
Relative rank between 0 and 1.

QUALIFY:
Dialect feature that filters window results directly.

Frame:
ROWS/RANGE boundary definition for aggregate windows.
```


## 5. Standard Answer Framework

Use this framework for every window-function problem:

```text
1. Restate the business question.
2. Identify output grain.
3. Identify partition/entity.
4. Identify ordering column.
5. Identify tie-breaker.
6. Choose function:
   - ROW_NUMBER
   - RANK
   - DENSE_RANK
   - LAG/LEAD
   - SUM/AVG/COUNT
   - FIRST_VALUE/LAST_VALUE
   - NTILE
7. Define frame if using running/moving aggregate.
8. Write query with CTE if filtering window output.
9. Validate row counts and duplicates.
10. Explain edge cases:
   - ties
   - NULLs
   - missing dates
   - duplicate timestamps
   - frame behavior
11. Explain performance:
   - filter first
   - reduce columns
   - reduce rows before sort
```

Short version:

```text
Grain:
Partition:
Order:
Tie-breaker:
Function:
Frame:
Filter method:
Validation:
```

Strict rule:

```text
No window-function answer is strong if the candidate cannot explain partition, order, and tie-breaker.
```


## 6. Scoring Rubric

Score each window-function answer from 0 to 5.

### Score 0

No meaningful SQL or window function reasoning.

### Score 1

Uses a window function randomly without explaining partition/order.

### Score 2

Can write simple ROW_NUMBER but misses tie-breakers, filtering, or grain.

### Score 3

Mostly correct but weak on frames, NULLs, duplicates, or validation.

### Score 4

Interview-ready. Correct function choice, partition, order, tie-breaker, CTE/QUALIFY filtering, and validation.

### Score 5

Strong. Handles ranking, dedupe, latest/first, running/moving aggregates, LAG/LEAD, gaps/islands, sessionization, frames, SCD/CDC use cases, performance, and dialect differences.

Do not give 4+ if:

```text
candidate does not define output grain
candidate does not define PARTITION BY
candidate does not define ORDER BY
candidate misses deterministic tie-breaker
candidate filters window alias in WHERE incorrectly
candidate uses RANK when exactly one row is required
candidate uses ROW_NUMBER when all tied rows are required
candidate uses LAST_VALUE without understanding frame
candidate ignores duplicate input rows
candidate cannot validate output uniqueness
candidate cannot explain performance cost of sorting
```


## 7. GROUP BY vs Window Functions

GROUP BY reduces rows.

Example:

```sql
SELECT
  user_id,
  COUNT(*) AS order_count
FROM orders
GROUP BY user_id;
```

Output grain:

```text
one row per user
```

Window function preserves rows.

Example:

```sql
SELECT
  order_id,
  user_id,
  COUNT(*) OVER (
    PARTITION BY user_id
  ) AS user_order_count
FROM orders;
```

Output grain:

```text
one row per order
```

Use GROUP BY when:

```text
you need one row per group
```

Use window function when:

```text
you need row-level detail plus group-level calculation
```

Interview line:

```text
GROUP BY collapses rows; window functions add group context without collapsing rows.
```


## 8. OVER Clause Anatomy

Window function anatomy:

```sql
SUM(total_amount) OVER (
  PARTITION BY user_id
  ORDER BY order_time
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_user_revenue
```

Parts:

```text
SUM(total_amount):
Function being applied.

PARTITION BY user_id:
Restart calculation for each user.

ORDER BY order_time:
Calculate in order of time.

ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW:
Include all previous rows and current row.
```

If PARTITION BY is missing:

```text
the whole result set is one partition
```

If ORDER BY is missing:

```text
order-dependent functions like ROW_NUMBER are not deterministic
aggregate window functions calculate over entire partition
```

Interview line:

```text
The OVER clause defines the group, sequence, and frame used by the window function.
```


## 9. PARTITION BY

PARTITION BY is like grouping for window functions, but it does not collapse rows.

Example:

```sql
SELECT
  user_id,
  order_id,
  total_amount,
  SUM(total_amount) OVER (
    PARTITION BY user_id
  ) AS user_total_revenue
FROM orders;
```

Meaning:

```text
For every order row, show the user's total revenue.
```

Common partitions:

```text
user_id
customer_id
product_id
category
account_id
order_id
session_id
pipeline_id
experiment_id
metric_date
country
```

Common mistake:

```text
missing PARTITION BY when ranking per group
```

Bad:

```sql
ROW_NUMBER() OVER (ORDER BY order_time)
```

This gives global row numbers, not per-user row numbers.

Good:

```sql
ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY order_time
)
```

Interview line:

```text
PARTITION BY decides where the window calculation restarts.
```


## 10. ORDER BY Inside OVER

ORDER BY inside OVER defines sequence inside each partition.

Example:

```sql
ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY order_time DESC
) AS latest_order_rank
```

Common use cases:

```text
latest row
first row
running total
previous/next row
top N
deduplication
streak logic
```

Tie issue:

```text
If two rows have the same order_time, result may be nondeterministic.
```

Better:

```sql
ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY order_time DESC, order_id DESC
) AS rn
```

Interview line:

```text
ORDER BY should be deterministic when choosing one row, so I add tie-breakers.
```


## 11. Window Frames

Window frames define which rows around the current row are included.

Common running total frame:

```sql
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

Example:

```sql
SUM(revenue) OVER (
  ORDER BY revenue_date
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_revenue
```

Common moving average frame:

```sql
ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
```

Example:

```sql
AVG(revenue) OVER (
  ORDER BY revenue_date
  ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
) AS seven_day_moving_avg
```

Important:

```text
ROW_NUMBER, RANK, DENSE_RANK usually do not need an explicit frame.
LAG and LEAD usually do not need a frame.
Aggregate windows often need clear frames.
LAST_VALUE often behaves unexpectedly without explicit frame.
```

Interview line:

```text
For running and moving aggregates, I define the window frame explicitly to avoid default-frame surprises.
```


## 12. ROWS vs RANGE

ROWS counts physical rows.

Example:

```sql
ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
```

Meaning:

```text
current row plus previous 6 rows
```

RANGE is value-based around ORDER BY values.

Example:

```sql
RANGE BETWEEN INTERVAL '6 days' PRECEDING AND CURRENT ROW
```

Meaning:

```text
rows within 6 days of current date/time
```

Caution:

```text
RANGE behavior and syntax vary by database.
RANGE includes peer rows with same ORDER BY value.
ROWS is usually easier and more predictable for interviews.
```

If there are missing dates:

```text
ROWS 6 PRECEDING does not mean previous 6 calendar days.
It means previous 6 rows.
```

Interview line:

```text
ROWS is row-count based; RANGE is value-distance based, so I choose based on whether I need row-based or time-based logic.
```


## 13. ROW_NUMBER

ROW_NUMBER assigns a unique sequence number inside each partition.

Example:

```sql
SELECT
  user_id,
  order_id,
  order_time,
  ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY order_time
  ) AS order_number
FROM orders;
```

Use when:

```text
keep exactly one row per group
deduplicate
latest row
first row
top N with deterministic tie-breaker
```

Important:

```text
ROW_NUMBER breaks ties arbitrarily unless ORDER BY has tie-breakers.
```

Latest row:

```sql
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY updated_at DESC, ingested_at DESC
    ) AS rn
  FROM user_profiles
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Interview line:

```text
ROW_NUMBER is for selecting exactly one row per partition, so tie-breakers matter.
```


## 14. RANK

RANK assigns same rank to ties and skips numbers after ties.

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

If revenues are:

```text
100, 100, 80
```

Ranks:

```text
1, 1, 3
```

Use when:

```text
ties should share rank
rank gaps are acceptable
all tied top records should be included
```

Top tied products:

```sql
WITH ranked AS (
  SELECT
    *,
    RANK() OVER (
      PARTITION BY category
      ORDER BY revenue DESC
    ) AS rnk
  FROM product_revenue
)
SELECT *
FROM ranked
WHERE rnk = 1;
```

Interview line:

```text
RANK is useful when ties should be preserved and rank gaps are acceptable.
```


## 15. DENSE_RANK

DENSE_RANK assigns same rank to ties without skipping numbers.

If values are:

```text
100, 100, 80
```

Dense ranks:

```text
1, 1, 2
```

Example:

```sql
SELECT
  category,
  product_id,
  revenue,
  DENSE_RANK() OVER (
    PARTITION BY category
    ORDER BY revenue DESC
  ) AS dense_revenue_rank
FROM product_revenue;
```

Use when:

```text
ties should share rank
rank levels should not have gaps
need top N distinct values/groups
```

Example:

```sql
WITH ranked AS (
  SELECT
    *,
    DENSE_RANK() OVER (
      PARTITION BY category
      ORDER BY revenue DESC
    ) AS drnk
  FROM product_revenue
)
SELECT *
FROM ranked
WHERE drnk <= 3;
```

Meaning:

```text
top 3 distinct revenue levels per category
```

Interview line:

```text
DENSE_RANK gives consecutive rank levels even when ties exist.
```


## 16. ROW_NUMBER vs RANK vs DENSE_RANK

Decision table:

| Need | Use |
|---|---|
| Keep exactly one row | ROW_NUMBER |
| Deduplicate to one survivor | ROW_NUMBER |
| Top N rows with deterministic tie-break | ROW_NUMBER |
| Preserve all tied winners | RANK |
| Competition ranking with gaps | RANK |
| Top N distinct value levels | DENSE_RANK |
| Ranking without gaps | DENSE_RANK |

Example:

```text
Scores: 100, 100, 80
```

Result:

```text
ROW_NUMBER: 1, 2, 3
RANK:       1, 1, 3
DENSE_RANK: 1, 1, 2
```

Interview line:

```text
ROW_NUMBER chooses one row; RANK and DENSE_RANK preserve ties.
```


## 17. NTILE

NTILE splits ordered rows into buckets.

Example:

```sql
SELECT
  user_id,
  revenue,
  NTILE(4) OVER (
    ORDER BY revenue DESC
  ) AS revenue_quartile
FROM user_revenue;
```

Use cases:

```text
quartiles
deciles
bucketing customers by spend
rough percentile grouping
```

Caution:

```text
NTILE creates buckets by row count, not exact value ranges.
Ties can be split across buckets.
```

Interview line:

```text
NTILE is useful for rough bucket assignment, but it can split tied values across buckets.
```


## 18. LAG

LAG gets a value from a previous row.

Example:

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

Use cases:

```text
previous event
previous order
previous status
month-over-month comparison
gap detection
sessionization
status change detection
```

With default:

```sql
LAG(revenue, 1, 0) OVER (
  ORDER BY revenue_date
) AS previous_revenue
```

Meaning:

```text
look back 1 row; if missing, use 0
```

Interview line:

```text
LAG is the standard function for comparing the current row to the previous row in an ordered sequence.
```


## 19. LEAD

LEAD gets a value from a future row.

Example:

```sql
SELECT
  user_id,
  event_time,
  LEAD(event_time) OVER (
    PARTITION BY user_id
    ORDER BY event_time
  ) AS next_event_time
FROM events;
```

Use cases:

```text
next event
next status change
interval end time
time until next action
session end boundary
SCD effective_to creation
```

Example: create effective_to from next effective_from:

```sql
SELECT
  user_id,
  plan,
  effective_from,
  LEAD(effective_from) OVER (
    PARTITION BY user_id
    ORDER BY effective_from
  ) AS effective_to
FROM user_plan_changes;
```

Interview line:

```text
LEAD is useful for deriving interval end boundaries from the next row's start time.
```


## 20. FIRST_VALUE

FIRST_VALUE returns first value in the window.

Example:

```sql
SELECT
  user_id,
  order_id,
  order_time,
  FIRST_VALUE(order_id) OVER (
    PARTITION BY user_id
    ORDER BY order_time
  ) AS first_order_id
FROM orders;
```

Use cases:

```text
first purchase ID
first status
first campaign touch
first plan
baseline value
```

Caution:

```text
If you only need one row per user, ROW_NUMBER + filter may be clearer.
FIRST_VALUE repeats the first value on every row.
```

Interview line:

```text
FIRST_VALUE is useful when I need to keep all rows but also show the first value in the partition.
```


## 21. LAST_VALUE

LAST_VALUE can be tricky because of default frames.

Potential surprise:

```sql
LAST_VALUE(status) OVER (
  PARTITION BY user_id
  ORDER BY event_time
) AS last_status
```

Many databases default the frame to end at current row, so LAST_VALUE may return the current row's status, not the final status of the partition.

Safer:

```sql
LAST_VALUE(status) OVER (
  PARTITION BY user_id
  ORDER BY event_time
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) AS final_status
```

Alternative for latest row:

```sql
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY event_time DESC
    ) AS rn
  FROM events
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Interview line:

```text
LAST_VALUE requires explicit frame awareness; for latest-row selection, ROW_NUMBER is often clearer.
```


## 22. SUM as Window Function

SUM can calculate totals, running totals, and percent-of-total denominators.

Total per user on each row:

```sql
SELECT
  order_id,
  user_id,
  total_amount,
  SUM(total_amount) OVER (
    PARTITION BY user_id
  ) AS user_total_amount
FROM orders;
```

Running total:

```sql
SELECT
  order_date,
  revenue,
  SUM(revenue) OVER (
    ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_revenue
FROM daily_revenue;
```

Percent of total:

```sql
SELECT
  category,
  revenue,
  revenue * 1.0 / NULLIF(SUM(revenue) OVER (), 0) AS revenue_share
FROM category_revenue;
```

Interview line:

```text
SUM as a window function lets me calculate group totals while keeping row-level detail.
```


## 23. AVG as Window Function

AVG can calculate group average or moving average.

User average order amount on each order row:

```sql
SELECT
  order_id,
  user_id,
  total_amount,
  AVG(total_amount) OVER (
    PARTITION BY user_id
  ) AS user_avg_order_amount
FROM orders;
```

7-row moving average:

```sql
SELECT
  revenue_date,
  revenue,
  AVG(revenue) OVER (
    ORDER BY revenue_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS moving_avg_7_rows
FROM daily_revenue;
```

Caution:

```text
7 rows is not always 7 calendar days if dates are missing.
Use a calendar table when calendar continuity matters.
```

Interview line:

```text
Moving averages require clear frame definition and careful handling of missing dates.
```


## 24. COUNT as Window Function

COUNT can calculate group size without collapsing rows.

Example:

```sql
SELECT
  user_id,
  order_id,
  COUNT(*) OVER (
    PARTITION BY user_id
  ) AS user_order_count
FROM orders;
```

Duplicate group size:

```sql
SELECT
  transaction_id,
  record_id,
  COUNT(*) OVER (
    PARTITION BY transaction_id
  ) AS duplicate_group_size
FROM transactions;
```

Use cases:

```text
duplicate detection metadata
group size
orders per user on each row
number of events in session
validation flags
```

Interview line:

```text
COUNT as a window function is useful when I need group size while preserving individual rows.
```


## 25. Filtering Window Function Results

Most SQL dialects do not allow filtering a window alias directly in WHERE.

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

Correct with CTE:

```sql
WITH ranked AS (
  SELECT
    user_id,
    order_id,
    order_time,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time DESC
    ) AS rn
  FROM orders
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Some warehouses support QUALIFY:

```sql
SELECT
  user_id,
  order_id,
  order_time
FROM orders
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY order_time DESC
) = 1;
```

Interview line:

```text
If QUALIFY is unavailable, I calculate window results in a CTE and filter in the outer query.
```


## 26. SQL Logical Order and Windows

Logical query processing order explains why window aliases cannot usually be used in WHERE.

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

Window functions are evaluated after WHERE.

Therefore:

```text
WHERE cannot filter on rn alias from SELECT.
```

Correct pattern:

```text
CTE/subquery computes rn.
Outer query filters rn.
```

Interview line:

```text
Window functions are evaluated after WHERE, so I use a CTE or QUALIFY to filter their results.
```


## 27. Deterministic Ordering

Whenever a window function chooses one row, ORDER BY must be deterministic.

Bad:

```sql
ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY updated_at DESC
) AS rn
```

Problem:

```text
If two records have same updated_at, the chosen row may be arbitrary.
```

Better:

```sql
ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY updated_at DESC, ingested_at DESC, record_id DESC
) AS rn
```

Common tie-breakers:

```text
ingested_at
record_id
source_sequence_number
version_number
event_id
load_file
row_number_in_file
status priority
created_at
```

Interview line:

```text
For production deduplication or latest-row logic, I add tie-breakers so the result is deterministic.
```


## 28. Case 1: Latest Row Per User

Business question:

```text
Get the latest profile row per user.
```

SQL:

```sql
WITH ranked_profiles AS (
  SELECT
    user_id,
    country,
    plan,
    updated_at,
    ingested_at,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY updated_at DESC, ingested_at DESC
    ) AS rn
  FROM user_profiles
  WHERE user_id IS NOT NULL
)
SELECT
  user_id,
  country,
  plan,
  updated_at
FROM ranked_profiles
WHERE rn = 1;
```

Key points:

```text
PARTITION BY user_id.
ORDER BY latest business update time.
Tie-break with ingestion time.
Filter rn = 1 in outer query.
```

Validation:

```sql
WITH latest AS (
  -- query above
)
SELECT
  user_id,
  COUNT(*) AS row_count
FROM latest
GROUP BY user_id
HAVING COUNT(*) > 1;
```

Expected:

```text
no rows
```

Interview line:

```text
Latest-row queries should use ROW_NUMBER with deterministic tie-breakers.
```


## 29. Case 2: First Purchase Per User

Business question:

```text
Find each user's first completed purchase.
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
      ORDER BY order_time ASC, order_id ASC
    ) AS rn
  FROM orders
  WHERE order_status = 'COMPLETED'
    AND user_id IS NOT NULL
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
MIN(order_time) does not safely return order_id and amount from the same row.
```

Interview line:

```text
Use ROW_NUMBER when you need columns from the first row, not just the minimum timestamp.
```


## 30. Case 3: Deduplicate Events

Business question:

```text
Deduplicate raw events by event_id, keeping the latest ingested record.
```

SQL:

```sql
WITH ranked_events AS (
  SELECT
    event_id,
    user_id,
    event_name,
    event_time,
    payload,
    ingested_at,
    ROW_NUMBER() OVER (
      PARTITION BY event_id
      ORDER BY ingested_at DESC
    ) AS rn,
    COUNT(*) OVER (
      PARTITION BY event_id
    ) AS duplicate_group_size
  FROM raw_events
  WHERE event_id IS NOT NULL
)
SELECT
  event_id,
  user_id,
  event_name,
  event_time,
  payload,
  ingested_at,
  duplicate_group_size
FROM ranked_events
WHERE rn = 1;
```

Why include COUNT:

```text
It preserves duplicate audit information on the kept row.
```

Interview line:

```text
Deduplication with window functions requires a business key and a deterministic keep rule.
```


## 31. Case 4: Top 3 Products Per Category

Business question:

```text
Find top 3 products by revenue within each category.
```

SQL:

```sql
WITH product_revenue AS (
  SELECT
    p.category,
    oi.product_id,
    SUM(oi.quantity * oi.unit_price) AS revenue
  FROM order_items oi
  JOIN orders o
    ON oi.order_id = o.order_id
  JOIN products p
    ON oi.product_id = p.product_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY p.category, oi.product_id
),
ranked_products AS (
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
FROM ranked_products
WHERE rn <= 3
ORDER BY category, rn;
```

If ties should be included:

```text
Use RANK instead of ROW_NUMBER.
```

Interview line:

```text
For top-N per group, aggregate to the ranking grain first, then rank within each group.
```


## 32. Case 5: Running Daily Revenue

Business question:

```text
Calculate running revenue by date.
```

SQL:

```sql
WITH daily_revenue AS (
  SELECT
    CAST(order_time AS DATE) AS revenue_date,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY CAST(order_time AS DATE)
)
SELECT
  revenue_date,
  revenue,
  SUM(revenue) OVER (
    ORDER BY revenue_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_revenue
FROM daily_revenue
ORDER BY revenue_date;
```

Key points:

```text
Aggregate to daily grain first.
Apply running sum over daily rows.
Use explicit frame.
```

Interview line:

```text
Running totals should usually be computed after aggregating to the reporting grain.
```


## 33. Case 6: Running Revenue Per User

Business question:

```text
For each completed order, show user's running lifetime revenue up to that order.
```

SQL:

```sql
SELECT
  user_id,
  order_id,
  order_time,
  total_amount,
  SUM(total_amount) OVER (
    PARTITION BY user_id
    ORDER BY order_time, order_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_user_revenue
FROM orders
WHERE order_status = 'COMPLETED'
ORDER BY user_id, order_time;
```

Tie-breaker:

```text
order_id ensures deterministic order if two orders have same order_time.
```

Interview line:

```text
A running total needs partition, order, and explicit frame.
```


## 34. Case 7: 7-Day Moving Average

Business question:

```text
Calculate 7-day moving average of revenue.
```

SQL with calendar-complete daily rows:

```sql
WITH daily_revenue AS (
  SELECT
    c.calendar_date AS revenue_date,
    COALESCE(SUM(o.total_amount), 0) AS revenue
  FROM dim_calendar c
  LEFT JOIN orders o
    ON CAST(o.order_time AS DATE) = c.calendar_date
   AND o.order_status = 'COMPLETED'
  WHERE c.calendar_date >= DATE '2026-01-01'
    AND c.calendar_date <  DATE '2026-02-01'
  GROUP BY c.calendar_date
)
SELECT
  revenue_date,
  revenue,
  AVG(revenue) OVER (
    ORDER BY revenue_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS moving_avg_7_day
FROM daily_revenue
ORDER BY revenue_date;
```

Why calendar matters:

```text
If missing dates are absent, ROWS 6 PRECEDING means previous 6 rows, not previous 6 calendar days.
```

Interview line:

```text
For calendar-day moving averages, I build a complete date series first.
```


## 35. Case 8: Month-over-Month Revenue Change

Business question:

```text
Calculate monthly revenue and previous month revenue.
```

SQL:

```sql
WITH monthly_revenue AS (
  SELECT
    DATE_TRUNC('month', order_time) AS revenue_month,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY DATE_TRUNC('month', order_time)
),
with_previous AS (
  SELECT
    revenue_month,
    revenue,
    LAG(revenue) OVER (
      ORDER BY revenue_month
    ) AS previous_month_revenue
  FROM monthly_revenue
)
SELECT
  revenue_month,
  revenue,
  previous_month_revenue,
  revenue - previous_month_revenue AS revenue_change,
  (revenue - previous_month_revenue) * 1.0
    / NULLIF(previous_month_revenue, 0) AS revenue_growth_rate
FROM with_previous
ORDER BY revenue_month;
```

Caution:

```text
If missing months should count as zero, build a month calendar first.
```

Interview line:

```text
LAG is the standard way to compare current period metrics with previous period metrics.
```


## 36. Case 9: Percent of Total Revenue

Business question:

```text
Calculate each category's revenue share of total revenue.
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

Key idea:

```text
SUM(revenue) OVER () gives total revenue over all category rows.
```

Interview line:

```text
Percent-of-total is often easiest with an aggregate CTE plus SUM(...) OVER ().
```


## 37. Case 10: Percent of Parent Total

Business question:

```text
Calculate product revenue share within each category.
```

SQL:

```sql
WITH product_revenue AS (
  SELECT
    p.category,
    oi.product_id,
    SUM(oi.quantity * oi.unit_price) AS revenue
  FROM order_items oi
  JOIN orders o
    ON oi.order_id = o.order_id
  JOIN products p
    ON oi.product_id = p.product_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY p.category, oi.product_id
)
SELECT
  category,
  product_id,
  revenue,
  revenue * 1.0 / NULLIF(
    SUM(revenue) OVER (PARTITION BY category),
    0
  ) AS category_revenue_share
FROM product_revenue;
```

Interview line:

```text
Partitioned window totals calculate share within each parent group.
```


## 38. Case 11: Orders Above User Average

Business question:

```text
Find orders whose amount is above the user's average order amount.
```

SQL:

```sql
WITH orders_with_avg AS (
  SELECT
    order_id,
    user_id,
    total_amount,
    AVG(total_amount) OVER (
      PARTITION BY user_id
    ) AS user_avg_order_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT
  order_id,
  user_id,
  total_amount,
  user_avg_order_amount
FROM orders_with_avg
WHERE total_amount > user_avg_order_amount;
```

Why window helps:

```text
Keeps order-level detail while adding user-level average.
```

Interview line:

```text
Window AVG is a clean replacement for correlated subqueries when comparing rows to group averages.
```


## 39. Case 12: Duplicate Group Audit

Business question:

```text
Report duplicate transaction groups and keep latest row.
```

SQL:

```sql
WITH enriched AS (
  SELECT
    transaction_id,
    record_id,
    amount,
    status,
    updated_at,
    ROW_NUMBER() OVER (
      PARTITION BY transaction_id
      ORDER BY updated_at DESC, record_id DESC
    ) AS rn,
    COUNT(*) OVER (
      PARTITION BY transaction_id
    ) AS duplicate_group_size,
    MIN(updated_at) OVER (
      PARTITION BY transaction_id
    ) AS first_seen_at,
    MAX(updated_at) OVER (
      PARTITION BY transaction_id
    ) AS last_seen_at
  FROM transactions
  WHERE transaction_id IS NOT NULL
)
SELECT
  transaction_id,
  record_id,
  amount,
  status,
  duplicate_group_size,
  first_seen_at,
  last_seen_at
FROM enriched
WHERE rn = 1;
```

Interview line:

```text
Window functions can dedupe while preserving useful duplicate audit metadata.
```


## 40. Case 13: Create SCD Effective To with LEAD

Business question:

```text
Given user plan change events, create effective_from and effective_to intervals.
```

Table:

```sql
user_plan_changes(user_id, plan, changed_at)
```

SQL:

```sql
SELECT
  user_id,
  plan,
  changed_at AS effective_from,
  LEAD(changed_at) OVER (
    PARTITION BY user_id
    ORDER BY changed_at
  ) AS effective_to
FROM user_plan_changes;
```

Meaning:

```text
Each row is active until the next change.
Last row has NULL effective_to, meaning currently active/open-ended.
```

Caution:

```text
If multiple changes have same changed_at, add tie-breaker.
```

Interview line:

```text
LEAD is commonly used to turn change events into effective-date intervals.
```


## 41. Case 14: Detect Status Changes

Business question:

```text
Find rows where a device status changed from previous status.
```

SQL:

```sql
WITH with_previous AS (
  SELECT
    device_id,
    event_time,
    status,
    LAG(status) OVER (
      PARTITION BY device_id
      ORDER BY event_time
    ) AS previous_status
  FROM device_status_events
)
SELECT
  device_id,
  event_time,
  previous_status,
  status
FROM with_previous
WHERE previous_status IS NULL
   OR status <> previous_status;
```

Use cases:

```text
uptime/downtime transitions
pipeline state changes
subscription status changes
account status changes
```

Interview line:

```text
LAG lets me compare each row's status with the previous status to detect transitions.
```


## 42. Case 15: Sessionization with LAG and SUM

Business question:

```text
Group user events into sessions where a new session starts after 30 minutes of inactivity.
```

SQL:

```sql
WITH ordered_events AS (
  SELECT
    user_id,
    event_id,
    event_time,
    LAG(event_time) OVER (
      PARTITION BY user_id
      ORDER BY event_time, event_id
    ) AS previous_event_time
  FROM events
  WHERE user_id IS NOT NULL
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_event_time IS NULL
        OR event_time > previous_event_time + INTERVAL '30 minutes'
      THEN 1 ELSE 0
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
  session_number,
  MIN(event_time) AS session_start,
  MAX(event_time) AS session_end,
  COUNT(*) AS event_count
FROM sessionized
GROUP BY user_id, session_number;
```

Interview line:

```text
Sessionization uses LAG to detect breaks and cumulative SUM to assign session IDs.
```


## 43. Case 16: Consecutive Activity Days

Business question:

```text
Find users active for at least 3 consecutive days.
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
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY active_date
    ) AS rn
  FROM user_days
),
islands AS (
  SELECT
    user_id,
    active_date,
    active_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
),
streaks AS (
  SELECT
    user_id,
    MIN(active_date) AS streak_start,
    MAX(active_date) AS streak_end,
    COUNT(*) AS streak_days
  FROM islands
  GROUP BY user_id, island_key
)
SELECT *
FROM streaks
WHERE streak_days >= 3;
```

Interview line:

```text
Daily streaks require deduplicating to user-day grain before applying ROW_NUMBER.
```


## 44. Case 17: Same-Status Runs

Business question:

```text
Find consecutive failed pipeline run streaks.
```

SQL:

```sql
WITH numbered AS (
  SELECT
    pipeline_id,
    run_id,
    started_at,
    status,
    ROW_NUMBER() OVER (
      PARTITION BY pipeline_id
      ORDER BY started_at, run_id
    ) AS rn_all,
    ROW_NUMBER() OVER (
      PARTITION BY pipeline_id, status
      ORDER BY started_at, run_id
    ) AS rn_status
  FROM pipeline_runs
),
islands AS (
  SELECT
    *,
    rn_all - rn_status AS island_key
  FROM numbered
)
SELECT
  pipeline_id,
  MIN(started_at) AS failure_start,
  MAX(started_at) AS failure_end,
  COUNT(*) AS consecutive_failures
FROM islands
WHERE status = 'FAILED'
GROUP BY pipeline_id, island_key
HAVING COUNT(*) >= 2;
```

Interview line:

```text
For consecutive same-value runs, rn_all minus rn_value remains constant within each run.
```


## 45. Case 18: Current State from CDC

Business question:

```text
Build current state from CDC records.
```

Table:

```sql
cdc_orders(order_id, operation, status, amount, source_updated_at, sequence_number)
```

SQL:

```sql
WITH ranked_cdc AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY order_id
      ORDER BY source_updated_at DESC, sequence_number DESC
    ) AS rn
  FROM cdc_orders
),
latest AS (
  SELECT *
  FROM ranked_cdc
  WHERE rn = 1
)
SELECT
  order_id,
  status,
  amount,
  source_updated_at
FROM latest
WHERE operation <> 'DELETE';
```

Important:

```text
Rank all operations first, then filter DELETE.
Filtering DELETE before ranking can resurrect old deleted records.
```

Interview line:

```text
CDC current-state logic uses ROW_NUMBER over source ordering and handles deletes after selecting the latest operation.
```


## 46. Case 19: Previous and Next Event Time

Business question:

```text
For each event, show previous and next event time for that user.
```

SQL:

```sql
SELECT
  user_id,
  event_id,
  event_time,
  LAG(event_time) OVER (
    PARTITION BY user_id
    ORDER BY event_time, event_id
  ) AS previous_event_time,
  LEAD(event_time) OVER (
    PARTITION BY user_id
    ORDER BY event_time, event_id
  ) AS next_event_time
FROM events;
```

Use cases:

```text
time since previous event
time until next event
gap detection
sessionization
behavior sequence analysis
```

Interview line:

```text
LAG and LEAD are the cleanest way to compare a row with its neighboring rows in time order.
```


## 47. Case 20: Time Between Orders

Business question:

```text
Calculate days since previous completed order per user.
```

SQL:

```sql
WITH ordered_orders AS (
  SELECT
    user_id,
    order_id,
    order_time,
    LAG(order_time) OVER (
      PARTITION BY user_id
      ORDER BY order_time, order_id
    ) AS previous_order_time
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT
  user_id,
  order_id,
  order_time,
  previous_order_time,
  order_time - previous_order_time AS time_since_previous_order
FROM ordered_orders;
```

Caution:

```text
Date/time difference syntax varies by database.
```

Interview line:

```text
Time-between-events questions are LAG problems.
```


## 48. Case 21: Customer Order Number

Business question:

```text
Assign each completed order a customer order number.
```

SQL:

```sql
SELECT
  user_id,
  order_id,
  order_time,
  ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY order_time, order_id
  ) AS customer_order_number
FROM orders
WHERE order_status = 'COMPLETED';
```

Use cases:

```text
first order
second order
repeat purchase analysis
customer lifecycle
```

Find second order:

```sql
WITH numbered AS (
  SELECT
    user_id,
    order_id,
    order_time,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time, order_id
    ) AS order_number
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT *
FROM numbered
WHERE order_number = 2;
```

Interview line:

```text
ROW_NUMBER is ideal for lifecycle numbering inside each entity.
```


## 49. Case 22: First Purchase After Signup

Business question:

```text
Find each user's first completed purchase after signup.
```

SQL:

```sql
WITH candidate_orders AS (
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
FROM candidate_orders
WHERE rn = 1;
```

Caution:

```text
For users with no order, LEFT JOIN still produces one NULL order row in many databases and rn = 1.
Use converted flag if needed.
```

Interview line:

```text
First-after-event problems use a filtered join plus ROW_NUMBER over candidate future events.
```


## 50. Case 23: Last Touch Attribution

Business question:

```text
Attribute each order to the most recent campaign touch before order time.
```

SQL:

```sql
WITH candidates AS (
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
FROM candidates
WHERE rn = 1;
```

Interview line:

```text
Last-touch attribution uses a range join and ROW_NUMBER to choose the closest prior touch.
```


## 51. Case 24: Top Revenue Customer Per Country

Business question:

```text
Find top revenue customer per country.
```

SQL:

```sql
WITH customer_revenue AS (
  SELECT
    u.country,
    o.user_id,
    SUM(o.total_amount) AS revenue
  FROM orders o
  JOIN users u
    ON o.user_id = u.user_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY u.country, o.user_id
),
ranked AS (
  SELECT
    country,
    user_id,
    revenue,
    ROW_NUMBER() OVER (
      PARTITION BY country
      ORDER BY revenue DESC, user_id
    ) AS rn
  FROM customer_revenue
)
SELECT
  country,
  user_id,
  revenue
FROM ranked
WHERE rn = 1;
```

If tied customers should be included:

```text
Use RANK instead of ROW_NUMBER.
```

Interview line:

```text
Top-per-group requires aggregating to group/entity grain first, then ranking.
```


## 52. Case 25: Revenue Deciles

Business question:

```text
Bucket customers into revenue deciles.
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
  revenue,
  NTILE(10) OVER (
    ORDER BY revenue DESC
  ) AS revenue_decile
FROM customer_revenue;
```

Caution:

```text
NTILE buckets by row count, not exact revenue ranges.
```

Interview line:

```text
NTILE is useful for bucketing entities after aggregating to the entity grain.
```


## 53. Case 26: Median-Like Ranking

Business question:

```text
Rank users by revenue and identify percentile-like position.
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
  revenue,
  PERCENT_RANK() OVER (
    ORDER BY revenue
  ) AS percent_rank_value,
  CUME_DIST() OVER (
    ORDER BY revenue
  ) AS cumulative_distribution
FROM customer_revenue;
```

Use cautiously:

```text
Exact percentile/median functions vary by database.
PERCENT_RANK and CUME_DIST have specific statistical meanings.
```

Interview line:

```text
Percentile-style window functions are useful, but I clarify exact percentile requirements and database support.
```


## 54. Case 27: Running Conversion Rate

Business question:

```text
Calculate cumulative signup-to-purchase conversion rate by signup date.
```

SQL:

```sql
WITH daily_signup_conversion AS (
  SELECT
    signup_date,
    COUNT(*) AS signups,
    SUM(converted_flag) AS converted
  FROM user_signup_conversion
  GROUP BY signup_date
),
running AS (
  SELECT
    signup_date,
    signups,
    converted,
    SUM(signups) OVER (
      ORDER BY signup_date
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_signups,
    SUM(converted) OVER (
      ORDER BY signup_date
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_converted
  FROM daily_signup_conversion
)
SELECT
  signup_date,
  cumulative_signups,
  cumulative_converted,
  cumulative_converted * 1.0 / NULLIF(cumulative_signups, 0) AS cumulative_conversion_rate
FROM running;
```

Interview line:

```text
For cumulative rates, calculate cumulative numerator and denominator separately, then divide.
```


## 55. Case 28: Rolling 7-Day Active Users Warning

Business question:

```text
Calculate rolling 7-day active users.
```

Important warning:

```text
COUNT(DISTINCT user_id) with rolling date windows is not simply summing daily distinct users, because users can appear on multiple days.
```

Correct concept:

```text
For each report date, count distinct users active between report_date - 6 and report_date.
```

Possible query:

```sql
WITH calendar AS (
  SELECT calendar_date
  FROM dim_calendar
  WHERE calendar_date >= DATE '2026-01-01'
    AND calendar_date <  DATE '2026-02-01'
),
user_days AS (
  SELECT DISTINCT
    user_id,
    event_date
  FROM events
  WHERE event_date >= DATE '2025-12-26'
    AND event_date <  DATE '2026-02-01'
)
SELECT
  c.calendar_date,
  COUNT(DISTINCT u.user_id) AS rolling_7_day_active_users
FROM calendar c
LEFT JOIN user_days u
  ON u.event_date >= c.calendar_date - INTERVAL '6 days'
 AND u.event_date <= c.calendar_date
GROUP BY c.calendar_date
ORDER BY c.calendar_date;
```

Interview line:

```text
Rolling distinct metrics are harder than rolling sums because distinct users can repeat across days.
```


## 56. Case 29: Cumulative Distinct Warning

Business question:

```text
Calculate cumulative distinct users over time.
```

Wrong:

```sql
SUM(daily_active_users) OVER (
  ORDER BY activity_date
) AS cumulative_users
```

Why wrong:

```text
Same user can be active on multiple days.
Daily distinct counts are not additive.
```

Correct concept:

```text
Find each user's first active date, then count users whose first active date is <= report date.
```

SQL:

```sql
WITH first_activity AS (
  SELECT
    user_id,
    MIN(event_date) AS first_active_date
  FROM events
  WHERE user_id IS NOT NULL
  GROUP BY user_id
),
daily_new_users AS (
  SELECT
    first_active_date AS activity_date,
    COUNT(*) AS new_users
  FROM first_activity
  GROUP BY first_active_date
)
SELECT
  activity_date,
  SUM(new_users) OVER (
    ORDER BY activity_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS cumulative_distinct_users
FROM daily_new_users
ORDER BY activity_date;
```

Interview line:

```text
Cumulative distinct counts need first-seen logic; summing daily distinct counts is wrong.
```


## 57. Case 30: Detect Gaps Between Events

Business question:

```text
Find user event gaps greater than 1 hour.
```

SQL:

```sql
WITH ordered_events AS (
  SELECT
    user_id,
    event_id,
    event_time,
    LAG(event_time) OVER (
      PARTITION BY user_id
      ORDER BY event_time, event_id
    ) AS previous_event_time
  FROM events
)
SELECT
  user_id,
  previous_event_time AS gap_start,
  event_time AS gap_end,
  event_time - previous_event_time AS gap_duration
FROM ordered_events
WHERE previous_event_time IS NOT NULL
  AND event_time > previous_event_time + INTERVAL '1 hour';
```

Interview line:

```text
Gap detection is a direct LAG comparison problem.
```


## 58. Case 31: Detect Missing Sequence Numbers

Business question:

```text
Find sequence gaps per device.
```

SQL:

```sql
WITH ordered AS (
  SELECT
    device_id,
    sequence_num,
    LAG(sequence_num) OVER (
      PARTITION BY device_id
      ORDER BY sequence_num
    ) AS previous_sequence_num
  FROM device_events
)
SELECT
  device_id,
  previous_sequence_num + 1 AS missing_start,
  sequence_num - 1 AS missing_end,
  sequence_num - previous_sequence_num - 1 AS missing_count
FROM ordered
WHERE previous_sequence_num IS NOT NULL
  AND sequence_num > previous_sequence_num + 1;
```

Interview line:

```text
Numeric sequence gaps can be detected with LAG and a difference check.
```


## 59. Case 32: Latest Successful Payment Per Order

Business question:

```text
For each order, keep the latest successful payment attempt.
```

SQL:

```sql
WITH ranked_payments AS (
  SELECT
    order_id,
    payment_id,
    payment_time,
    amount,
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

Caution:

```text
If failed attempts matter for metrics, do not filter them out before calculating attempt-level measures.
```

Interview line:

```text
Filter to eligible rows before ranking when the survivor must satisfy a condition.
```


## 60. Case 33: Payment Attempt Number

Business question:

```text
Number payment attempts per order.
```

SQL:

```sql
SELECT
  order_id,
  payment_id,
  payment_time,
  payment_status,
  ROW_NUMBER() OVER (
    PARTITION BY order_id
    ORDER BY payment_time, payment_id
  ) AS payment_attempt_number
FROM payments;
```

Use cases:

```text
first attempt success
retry analysis
failure before success
payment funnel
```

Interview line:

```text
Attempt numbering is a ROW_NUMBER lifecycle pattern inside each business entity.
```


## 61. Case 34: Failed Attempts Before Success

Business question:

```text
For each successful payment, count failed attempts before it for the same order.
```

SQL:

```sql
WITH attempts AS (
  SELECT
    order_id,
    payment_id,
    payment_time,
    payment_status,
    SUM(CASE WHEN payment_status = 'FAILED' THEN 1 ELSE 0 END) OVER (
      PARTITION BY order_id
      ORDER BY payment_time, payment_id
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS failed_attempts_before
  FROM payments
)
SELECT
  order_id,
  payment_id,
  payment_time,
  failed_attempts_before
FROM attempts
WHERE payment_status = 'SUCCESS';
```

Interview line:

```text
Window frames can count prior events before the current event.
```


## 62. Case 35: Running Balance

Business question:

```text
Calculate running account balance from transactions.
```

SQL:

```sql
SELECT
  account_id,
  transaction_id,
  transaction_time,
  amount,
  SUM(amount) OVER (
    PARTITION BY account_id
    ORDER BY transaction_time, transaction_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_balance
FROM account_transactions
ORDER BY account_id, transaction_time;
```

Caution:

```text
If there is an opening balance, add it to the running sum.
If transaction order can tie, use deterministic sequence.
```

Interview line:

```text
Running balance is a partitioned running SUM with deterministic transaction ordering.
```


## 63. Case 36: Inventory Running Quantity

Business question:

```text
Calculate inventory quantity over time from inventory movements.
```

SQL:

```sql
SELECT
  product_id,
  movement_id,
  movement_time,
  quantity_delta,
  SUM(quantity_delta) OVER (
    PARTITION BY product_id
    ORDER BY movement_time, movement_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS inventory_quantity
FROM inventory_movements;
```

Interview line:

```text
Inventory movement tables often use running SUM to derive stock level over time.
```


## 64. Case 37: Compare Source and Target Row Counts Over Time

Business question:

```text
Compare daily source row count to previous day count.
```

SQL:

```sql
WITH daily_counts AS (
  SELECT
    load_date,
    COUNT(*) AS row_count
  FROM source_table
  GROUP BY load_date
),
with_previous AS (
  SELECT
    load_date,
    row_count,
    LAG(row_count) OVER (
      ORDER BY load_date
    ) AS previous_day_row_count
  FROM daily_counts
)
SELECT
  load_date,
  row_count,
  previous_day_row_count,
  row_count - previous_day_row_count AS row_count_change
FROM with_previous;
```

Interview line:

```text
LAG is useful for pipeline monitoring and day-over-day data-quality checks.
```


## 65. Case 38: Detect Anomaly by Moving Average

Business question:

```text
Flag days where revenue is less than 50% of 7-day moving average.
```

SQL:

```sql
WITH daily_revenue AS (
  SELECT
    revenue_date,
    revenue
  FROM mart.daily_revenue
),
with_moving_avg AS (
  SELECT
    revenue_date,
    revenue,
    AVG(revenue) OVER (
      ORDER BY revenue_date
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7_day
  FROM daily_revenue
)
SELECT
  revenue_date,
  revenue,
  moving_avg_7_day
FROM with_moving_avg
WHERE revenue < moving_avg_7_day * 0.5;
```

Caution:

```text
For robust anomaly detection, production logic may need seasonality, weekday effects, and outlier handling.
```

Interview line:

```text
Moving-window metrics can support simple monitoring, but production anomaly detection may need more context.
```


## 66. Case 39: Last Non-Null Value Concept

Business question:

```text
Forward-fill last known value over time.
```

Important:

```text
Syntax differs by database.
Some support IGNORE NULLS.
Some do not.
```

Example if IGNORE NULLS is supported:

```sql
LAST_VALUE(value IGNORE NULLS) OVER (
  PARTITION BY entity_id
  ORDER BY event_time
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS last_known_value
```

Portable approach may require:

```text
more complex grouping
self join
recursive logic
warehouse-specific functions
```

Interview line:

```text
Forward-fill is a window-function problem, but implementation depends heavily on database support for IGNORE NULLS.
```


## 67. Case 40: Multiple Window Functions Together

Business question:

```text
For each order, show order number, previous order time, and running revenue.
```

SQL:

```sql
SELECT
  user_id,
  order_id,
  order_time,
  total_amount,
  ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY order_time, order_id
  ) AS order_number,
  LAG(order_time) OVER (
    PARTITION BY user_id
    ORDER BY order_time, order_id
  ) AS previous_order_time,
  SUM(total_amount) OVER (
    PARTITION BY user_id
    ORDER BY order_time, order_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_user_revenue
FROM orders
WHERE order_status = 'COMPLETED';
```

Optimization note:

```text
Multiple windows with same PARTITION BY and ORDER BY can often be computed efficiently together by the optimizer.
```

Interview line:

```text
When multiple window functions use the same partition and order, the query stays readable and may share sorting work.
```


## 68. Window Function Optimization

Window functions often require sorting.

Optimization checklist:

```text
filter rows before window
select only needed columns
pre-aggregate before window when ranking aggregated metrics
deduplicate before streak windows
use deterministic but minimal ORDER BY
avoid unnecessary PARTITION BY columns
avoid windowing raw event tables when summary grain is enough
partition data physically when supported
cluster/sort by common partition/order keys when useful
```

Bad:

```sql
SELECT
  *,
  ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY event_time DESC
  ) AS rn
FROM raw_events;
```

Better:

```sql
WITH filtered_events AS (
  SELECT
    event_id,
    user_id,
    event_time
  FROM raw_events
  WHERE event_date >= DATE '2026-01-01'
    AND event_date <  DATE '2026-02-01'
)
SELECT
  *,
  ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY event_time DESC, event_id DESC
  ) AS rn
FROM filtered_events;
```

Interview line:

```text
To optimize windows, reduce the input before the sort.
```


## 69. Window Functions and NULLs

NULL behavior depends on function and database.

Examples:

```text
ORDER BY column with NULLs may put NULL first or last depending on database.
LAG returns NULL for first row unless default is provided.
Aggregate windows usually ignore NULL values like regular aggregates.
FIRST_VALUE can return NULL if first value is NULL.
LAST_VALUE can return NULL if last value in frame is NULL.
```

Make NULL ordering explicit where supported:

```sql
ORDER BY updated_at DESC NULLS LAST
```

Alternative:

```sql
ORDER BY
  CASE WHEN updated_at IS NULL THEN 1 ELSE 0 END,
  updated_at DESC
```

Interview line:

```text
For window functions, I handle NULLs intentionally, especially in ordering and first/last value logic.
```


## 70. Window Functions and Ties

Ties affect ranking and row selection.

If two rows have same ordering value:

```text
ROW_NUMBER chooses one based on remaining order or arbitrary order.
RANK gives same rank and skips next rank.
DENSE_RANK gives same rank without gap.
```

Tie-safe latest row:

```sql
ROW_NUMBER() OVER (
  PARTITION BY entity_id
  ORDER BY updated_at DESC, ingested_at DESC, record_id DESC
) AS rn
```

Expose tied latest rows:

```sql
RANK() OVER (
  PARTITION BY entity_id
  ORDER BY updated_at DESC
) AS rnk
```

Interview line:

```text
If ties are meaningful, I use RANK; if exactly one row is needed, I use ROW_NUMBER with tie-breakers.
```


## 71. Window Functions and Data Grain

Window functions do not fix wrong grain.

Bad:

```sql
SELECT
  order_id,
  SUM(total_amount) OVER (
    PARTITION BY user_id
  ) AS user_revenue
FROM orders o
JOIN order_items oi
  ON o.order_id = oi.order_id;
```

Problem:

```text
order rows are multiplied by item rows before window sum.
```

Better:

```sql
WITH completed_orders AS (
  SELECT
    order_id,
    user_id,
    total_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT
  order_id,
  user_id,
  total_amount,
  SUM(total_amount) OVER (
    PARTITION BY user_id
  ) AS user_revenue
FROM completed_orders;
```

Interview line:

```text
Window functions operate on the rows produced by FROM/JOIN, so input grain must be correct first.
```


## 72. Window Functions in Data Engineering Pipelines

Common pipeline uses:

```text
deduplicate staging records before MERGE
build current snapshot from CDC
create SCD effective_to using LEAD
calculate data quality row count changes
detect duplicate business keys
sessionize event streams
detect late-arriving gaps
find latest source record per key
rank source candidates by priority
build cumulative metrics
detect first-seen/new entities
```

Example staging dedupe before MERGE:

```sql
WITH ranked_source AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY business_key
      ORDER BY updated_at DESC, ingested_at DESC
    ) AS rn
  FROM source_staging
)
SELECT *
FROM ranked_source
WHERE rn = 1;
```

Interview line:

```text
In pipelines, window functions often enforce one-row-per-key rules before loading final tables.
```


## 73. Window Functions for Data Quality

Examples:

### Duplicate group size

```sql
COUNT(*) OVER (
  PARTITION BY business_key
) AS duplicate_group_size
```

### Previous row count

```sql
LAG(row_count) OVER (
  ORDER BY load_date
) AS previous_row_count
```

### Rank latest DQ run

```sql
ROW_NUMBER() OVER (
  PARTITION BY table_name, partition_date
  ORDER BY run_completed_at DESC
) AS rn
```

### Running failure count

```sql
SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) OVER (
  PARTITION BY pipeline_id
  ORDER BY run_time
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS cumulative_failures
```

Interview line:

```text
Window functions are useful for DQ monitoring because they compare current records to group history or previous runs.
```


## 74. Dialect Notes

Window function support is broadly available, but syntax differs.

### QUALIFY

Supported in some warehouses:

```sql
SELECT *
FROM orders
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY order_time DESC
) = 1;
```

Portable CTE version:

```sql
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time DESC
    ) AS rn
  FROM orders
)
SELECT *
FROM ranked
WHERE rn = 1;
```

### Date arithmetic

PostgreSQL-style:

```sql
event_time + INTERVAL '30 minutes'
```

SQL Server-style:

```sql
DATEADD(minute, 30, event_time)
```

BigQuery-style:

```sql
TIMESTAMP_ADD(event_time, INTERVAL 30 MINUTE)
```

Interview line:

```text
I use portable CTE syntax unless the interviewer specifies a warehouse that supports QUALIFY.
```


## 75. Common Window Function Mistakes

Common mistakes:

```text
missing PARTITION BY
wrong PARTITION BY
missing ORDER BY
nondeterministic ORDER BY
filtering window alias in WHERE
using ROW_NUMBER when ties should be preserved
using RANK when exactly one row is needed
not aggregating before ranking
not deduplicating before streak logic
using LAST_VALUE without explicit frame
using ROWS 6 PRECEDING when 7 calendar days are required but dates are missing
windowing after a join that changed grain
assuming daily distinct counts can be summed cumulatively
forgetting NULL ordering
using SELECT * in large window queries
not validating one row per key after dedupe
```

Strict feedback:

```text
This is not interview-ready. You used ROW_NUMBER to choose the latest row but did not include a tie-breaker, so the survivor can be nondeterministic.
```


## 76. Pattern Selection Guide

| Problem Type | Recommended Window Pattern |
|---|---|
| latest row per key | ROW_NUMBER DESC |
| first row per key | ROW_NUMBER ASC |
| deduplication | ROW_NUMBER by business key |
| keep tied winners | RANK |
| top N per group | ROW_NUMBER or RANK |
| top N distinct values | DENSE_RANK |
| previous row comparison | LAG |
| next row comparison | LEAD |
| effective_to from changes | LEAD |
| running total | SUM with unbounded preceding frame |
| moving average | AVG with preceding frame |
| percent of total | SUM(...) OVER () |
| percent of group | SUM(...) OVER (PARTITION BY group) |
| duplicate group size | COUNT(*) OVER (PARTITION BY key) |
| sessionization | LAG + cumulative SUM |
| status runs | rn_all - rn_status or LAG + SUM |
| streaks | ROW_NUMBER island key |
| bucketing | NTILE |


## 77. Review Checklist

Review every window-function answer using:

```text
1. Did candidate identify output grain?
2. Did candidate identify partition key?
3. Did candidate identify ordering column?
4. Did candidate include deterministic tie-breaker?
5. Did candidate choose correct function?
6. Did candidate define frame when needed?
7. Did candidate filter window result correctly?
8. Did candidate handle ties intentionally?
9. Did candidate handle NULLs intentionally?
10. Did candidate aggregate before ranking if needed?
11. Did candidate deduplicate before streak logic?
12. Did candidate avoid changing grain accidentally?
13. Did candidate validate output uniqueness?
14. Did candidate explain SQL dialect if relevant?
15. Did candidate explain performance cost?
```

Interview line:

```text
A window function answer is correct only if partition, order, frame, and filter timing are all correct.
```


## 78. Validation Queries

### Validate dedupe output has one row per key

```sql
SELECT
  business_key,
  COUNT(*) AS row_count
FROM deduped_output
GROUP BY business_key
HAVING COUNT(*) > 1;
```

### Validate ranked top-N does not exceed N per group

```sql
SELECT
  category,
  COUNT(*) AS output_rows
FROM top_products
GROUP BY category
HAVING COUNT(*) > 3;
```

### Validate duplicate input before streak logic

```sql
SELECT
  user_id,
  active_date,
  COUNT(*) AS row_count
FROM user_days
GROUP BY user_id, active_date
HAVING COUNT(*) > 1;
```

### Validate running total final value

```sql
SELECT MAX(running_revenue) FROM running_revenue_output;
SELECT SUM(revenue) FROM daily_revenue;
```

These should match for a full date range.

Interview line:

```text
Window-function outputs should be validated with grain and metric checks.
```


## 79. Practice Problem 1: Latest Login Per User

Problem:

```text
Find the latest login event per user.
```

Solution:

```sql
WITH ranked_logins AS (
  SELECT
    user_id,
    event_id,
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
  event_id,
  event_time AS latest_login_time
FROM ranked_logins
WHERE rn = 1;
```

Expected explanation:

```text
Partition by user.
Order latest first.
Tie-break with event_id.
Filter rn = 1 in outer query.
```


## 80. Practice Problem 2: Second Purchase Per User

Problem:

```text
Find each user's second completed purchase.
```

Solution:

```sql
WITH numbered_orders AS (
  SELECT
    user_id,
    order_id,
    order_time,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time, order_id
    ) AS order_number
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT
  user_id,
  order_id,
  order_time
FROM numbered_orders
WHERE order_number = 2;
```

Expected explanation:

```text
ROW_NUMBER creates user purchase sequence.
Second purchase is order_number = 2.
```


## 81. Practice Problem 3: Top 5 Customers by Month

Problem:

```text
Find top 5 customers by revenue for each month.
```

Solution:

```sql
WITH monthly_customer_revenue AS (
  SELECT
    DATE_TRUNC('month', order_time) AS order_month,
    user_id,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY DATE_TRUNC('month', order_time), user_id
),
ranked AS (
  SELECT
    order_month,
    user_id,
    revenue,
    ROW_NUMBER() OVER (
      PARTITION BY order_month
      ORDER BY revenue DESC, user_id
    ) AS rn
  FROM monthly_customer_revenue
)
SELECT *
FROM ranked
WHERE rn <= 5
ORDER BY order_month, rn;
```

Expected explanation:

```text
Aggregate to month/customer first, then rank within month.
```


## 82. Practice Problem 4: Running Order Count

Problem:

```text
For each user order, show running completed order count.
```

Solution:

```sql
SELECT
  user_id,
  order_id,
  order_time,
  COUNT(*) OVER (
    PARTITION BY user_id
    ORDER BY order_time, order_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_completed_orders
FROM orders
WHERE order_status = 'COMPLETED';
```

Expected explanation:

```text
COUNT over ordered partition gives running count.
```


## 83. Practice Problem 5: Previous Status

Problem:

```text
For every account status event, show previous status.
```

Solution:

```sql
SELECT
  account_id,
  status_time,
  status,
  LAG(status) OVER (
    PARTITION BY account_id
    ORDER BY status_time
  ) AS previous_status
FROM account_status_events;
```

Expected explanation:

```text
LAG reads previous row in account time order.
```


## 84. Practice Problem 6: Status Change Rows

Problem:

```text
Return only rows where account status changed.
```

Solution:

```sql
WITH with_previous AS (
  SELECT
    account_id,
    status_time,
    status,
    LAG(status) OVER (
      PARTITION BY account_id
      ORDER BY status_time
    ) AS previous_status
  FROM account_status_events
)
SELECT *
FROM with_previous
WHERE previous_status IS NULL
   OR status <> previous_status;
```

Expected explanation:

```text
A status change occurs when current status differs from previous status.
```


## 85. Practice Problem 7: Daily Revenue Share by Country

Problem:

```text
For each day, calculate each country's share of daily revenue.
```

Solution:

```sql
WITH daily_country_revenue AS (
  SELECT
    CAST(o.order_time AS DATE) AS revenue_date,
    u.country,
    SUM(o.total_amount) AS revenue
  FROM orders o
  JOIN users u
    ON o.user_id = u.user_id
  WHERE o.order_status = 'COMPLETED'
  GROUP BY CAST(o.order_time AS DATE), u.country
)
SELECT
  revenue_date,
  country,
  revenue,
  revenue * 1.0 / NULLIF(
    SUM(revenue) OVER (PARTITION BY revenue_date),
    0
  ) AS daily_revenue_share
FROM daily_country_revenue;
```

Expected explanation:

```text
Partition total by revenue_date.
```


## 86. Practice Problem 8: Deduplicate API Records

Problem:

```text
API records have duplicate id. Keep latest source updated_at.
```

Solution:

```sql
WITH ranked AS (
  SELECT
    id,
    payload,
    source_updated_at,
    ingested_at,
    ROW_NUMBER() OVER (
      PARTITION BY id
      ORDER BY source_updated_at DESC, ingested_at DESC
    ) AS rn
  FROM api_raw_records
  WHERE id IS NOT NULL
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Expected explanation:

```text
Use source update time first, ingestion time as tie-breaker.
```


## 87. Practice Problem 9: 3-Day Moving Average

Problem:

```text
Calculate 3-day moving average of daily orders.
```

Solution:

```sql
WITH daily_orders AS (
  SELECT
    order_date,
    COUNT(*) AS orders
  FROM fact_orders_daily
  GROUP BY order_date
)
SELECT
  order_date,
  orders,
  AVG(orders) OVER (
    ORDER BY order_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS moving_avg_3_day
FROM daily_orders;
```

Expected explanation:

```text
ROWS 2 PRECEDING plus current row gives 3 rows.
Need calendar-complete rows if exact 3 calendar days are required.
```


## 88. Practice Problem 10: Build Effective Intervals

Problem:

```text
Create effective_to for customer tier changes.
```

Solution:

```sql
SELECT
  customer_id,
  tier,
  changed_at AS effective_from,
  LEAD(changed_at) OVER (
    PARTITION BY customer_id
    ORDER BY changed_at
  ) AS effective_to
FROM customer_tier_changes;
```

Expected explanation:

```text
Next change start becomes current row's end.
```


## 89. Practice Problem 11: Orders Greater Than Previous Order

Problem:

```text
Find orders where amount is greater than the user's previous completed order amount.
```

Solution:

```sql
WITH with_previous AS (
  SELECT
    user_id,
    order_id,
    order_time,
    total_amount,
    LAG(total_amount) OVER (
      PARTITION BY user_id
      ORDER BY order_time, order_id
    ) AS previous_order_amount
  FROM orders
  WHERE order_status = 'COMPLETED'
)
SELECT *
FROM with_previous
WHERE previous_order_amount IS NOT NULL
  AND total_amount > previous_order_amount;
```

Expected explanation:

```text
LAG gets previous order amount at user order sequence.
```


## 90. Practice Problem 12: User Revenue Quartiles

Problem:

```text
Place users into 4 revenue buckets.
```

Solution:

```sql
WITH user_revenue AS (
  SELECT
    user_id,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
  GROUP BY user_id
)
SELECT
  user_id,
  revenue,
  NTILE(4) OVER (
    ORDER BY revenue DESC
  ) AS revenue_quartile
FROM user_revenue;
```

Expected explanation:

```text
Aggregate to user grain first, then bucket users by revenue.
```


## 91. Practice Problem 13: Consecutive Failed Logins

Problem:

```text
Find users with at least 3 consecutive failed login attempts.
```

Solution:

```sql
WITH numbered AS (
  SELECT
    user_id,
    attempt_time,
    status,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY attempt_time
    ) AS rn_all,
    ROW_NUMBER() OVER (
      PARTITION BY user_id, status
      ORDER BY attempt_time
    ) AS rn_status
  FROM login_attempts
),
islands AS (
  SELECT
    *,
    rn_all - rn_status AS island_key
  FROM numbered
)
SELECT
  user_id,
  MIN(attempt_time) AS failure_start,
  MAX(attempt_time) AS failure_end,
  COUNT(*) AS failed_attempts
FROM islands
WHERE status = 'FAILED'
GROUP BY user_id, island_key
HAVING COUNT(*) >= 3;
```

Expected explanation:

```text
Same-status consecutive runs use rn_all - rn_status.
```


## 92. Practice Problem 14: Order Revenue Percentile Rank

Problem:

```text
For each order, calculate its percentile rank by amount.
```

Solution:

```sql
SELECT
  order_id,
  total_amount,
  PERCENT_RANK() OVER (
    ORDER BY total_amount
  ) AS amount_percent_rank
FROM orders
WHERE order_status = 'COMPLETED';
```

Expected explanation:

```text
PERCENT_RANK gives relative rank from 0 to 1.
Clarify exact percentile requirements.
```


## 93. Practice Problem 15: Latest Successful Run Per Pipeline

Problem:

```text
Find latest successful pipeline run per pipeline.
```

Solution:

```sql
WITH ranked AS (
  SELECT
    pipeline_id,
    run_id,
    started_at,
    completed_at,
    ROW_NUMBER() OVER (
      PARTITION BY pipeline_id
      ORDER BY completed_at DESC, run_id DESC
    ) AS rn
  FROM pipeline_runs
  WHERE status = 'SUCCESS'
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Expected explanation:

```text
Filter to successful runs before latest-success ranking.
```


## 94. Pattern Classification Drill

Classify each prompt.

```text
1. Latest row per user.
2. First purchase per user.
3. Deduplicate by transaction_id.
4. Top 3 products per category.
5. Keep all tied top products.
6. Monthly revenue compared to previous month.
7. Create effective_to from next change.
8. Running total revenue.
9. 7-day moving average.
10. Revenue share by category.
11. Orders above user average.
12. Sessionize events by 30-minute gap.
13. Consecutive failed statuses.
14. Duplicate group size.
15. Customer revenue deciles.
16. Detect status change.
17. Find second purchase.
18. Cumulative distinct users.
19. Rolling distinct active users.
20. Latest CDC record excluding deletes.
```

Expected classification:

```text
1. ROW_NUMBER DESC
2. ROW_NUMBER ASC
3. ROW_NUMBER + COUNT OVER
4. ROW_NUMBER after aggregation
5. RANK
6. LAG
7. LEAD
8. SUM with unbounded preceding frame
9. AVG with preceding frame + calendar caution
10. SUM OVER total
11. AVG OVER partition
12. LAG + cumulative SUM
13. rn_all - rn_status
14. COUNT OVER partition
15. NTILE
16. LAG status
17. ROW_NUMBER = 2
18. first-seen + running SUM, not sum daily distinct
19. date range distinct count, not simple window sum
20. ROW_NUMBER over CDC order then filter DELETE
```

Passing standard:

```text
18/20 correct before timed window-function mocks.
```


## 95. High-ROI Window Function Topics

Practice these first.

| Topic | Candidate Must Explain |
|---|---|
| PARTITION BY | where calculation restarts |
| ORDER BY | row sequence inside partition |
| frame | rows included in aggregate window |
| ROW_NUMBER | exactly one row / sequence |
| RANK | ties with gaps |
| DENSE_RANK | ties without gaps |
| LAG | previous row |
| LEAD | next row |
| running total | SUM frame |
| moving average | AVG frame |
| percent total | SUM OVER |
| dedupe | ROW_NUMBER + tie-breaker |
| latest row | ROW_NUMBER DESC |
| first row | ROW_NUMBER ASC |
| sessionization | LAG + cumulative SUM |
| streaks | ROW_NUMBER island key |
| filtering | CTE or QUALIFY |
| validation | output grain and uniqueness |


## 96. 7-Day Window Functions Plan

### Day 1: Window fundamentals

Problems:

```text
PARTITION BY
ORDER BY
GROUP BY vs window
ROW_NUMBER basics
filtering window output
```

Focus:

```text
mental model
syntax
logical order
```

### Day 2: Ranking

Problems:

```text
latest row
first row
top N per group
ties with RANK
DENSE_RANK
NTILE
```

Focus:

```text
ROW_NUMBER vs RANK vs DENSE_RANK
```

### Day 3: LAG and LEAD

Problems:

```text
previous order
next event
status change
month-over-month
effective_to
gap detection
```

Focus:

```text
previous/next row comparisons
```

### Day 4: Aggregate windows

Problems:

```text
running total
moving average
percent of total
group totals
running conversion
running balance
```

Focus:

```text
frames
ROWS vs RANGE
```

### Day 5: Data Engineering use cases

Problems:

```text
deduplication
CDC current state
staging before MERGE
duplicate audit
latest successful pipeline run
DQ row count changes
```

Focus:

```text
pipeline reliability
```

### Day 6: Advanced patterns

Problems:

```text
sessionization
gaps and islands
same-status runs
rolling distinct warning
cumulative distinct warning
last-touch attribution
```

Focus:

```text
multi-step window logic
```

### Day 7: Mock and repair

Tasks:

```text
Run window function mock.
Review mistakes.
Repair weakest topic.
Update progress.
```


## 97. 30-Day Window Functions Plan

### Week 1: Core ranking

Focus:

```text
ROW_NUMBER
RANK
DENSE_RANK
latest/first
top-N
filtering with CTE
```

Exit:

```text
Candidate can solve latest, first, dedupe, and top-N problems.
```

### Week 2: LAG/LEAD and aggregates

Focus:

```text
previous/next row
running totals
moving averages
percent total
frames
```

Exit:

```text
Candidate can solve time-series and comparison problems.
```

### Week 3: Data Engineering patterns

Focus:

```text
dedupe
CDC
SCD effective intervals
pipeline monitoring
duplicate audit
running balances
```

Exit:

```text
Candidate can use windows in production-style pipeline SQL.
```

### Week 4: Advanced and mocks

Focus:

```text
sessionization
streaks
same-status runs
rolling distinct pitfalls
optimization
dialect differences
mock interviews
```

Exit:

```text
Average mock score >= 4/5.
```


## 98. Mock Set 1: Ranking and Deduplication

Problems:

```text
1. Latest row per user.
2. First order per user.
3. Deduplicate transactions by transaction_id.
4. Top 3 products per category.
5. Preserve tied top customers.
```

Expected skills:

```text
ROW_NUMBER
RANK
tie-breakers
CTE filtering
grain validation
```

Passing standard:

```text
Average score >= 4/5.
Candidate includes deterministic tie-breakers where needed.
```


## 99. Mock Set 2: LAG and LEAD

Problems:

```text
1. Previous order amount per user.
2. Month-over-month revenue change.
3. Create effective_to from change events.
4. Detect status changes.
5. Find gaps greater than 1 hour.
```

Expected skills:

```text
LAG
LEAD
ordered partitions
date/time difference
NULL first/last row handling
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains previous/next row logic clearly.
```


## 100. Mock Set 3: Aggregate Windows

Problems:

```text
1. Running daily revenue.
2. Running account balance.
3. 7-day moving average.
4. Revenue share by category.
5. Running conversion rate.
```

Expected skills:

```text
SUM OVER
AVG OVER
explicit frames
partitioned totals
safe division
```

Passing standard:

```text
Average score >= 4/5.
Candidate defines frames for running/moving calculations.
```


## 101. Mock Set 4: Data Engineering Windows

Problems:

```text
1. CDC current state from change events.
2. Staging dedupe before MERGE.
3. Duplicate group audit metadata.
4. Latest successful pipeline run.
5. DQ row count change from previous day.
```

Expected skills:

```text
ROW_NUMBER
COUNT OVER
LAG
tie-breakers
pipeline semantics
```

Passing standard:

```text
Average score >= 4/5.
Candidate handles production edge cases and validation.
```


## 102. Mock Set 5: Advanced Patterns

Problems:

```text
1. Sessionize events by inactivity gap.
2. Users active for 3 consecutive days.
3. Consecutive failed login attempts.
4. Last-touch attribution.
5. Explain why rolling distinct users is hard.
```

Expected skills:

```text
LAG + cumulative SUM
ROW_NUMBER island key
rn_all - rn_status
range join + ROW_NUMBER
distinct-count reasoning
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains multi-step patterns without guessing.
```


## 103. Timed Drill Protocol

Use this timing protocol.

### Simple window problem

```text
10-15 minutes
```

### Medium analytics window problem

```text
20-30 minutes
```

### Advanced DE window problem

```text
35-45 minutes
```

Per drill:

```text
Minute 0-3:
Clarify output grain, partition, order, and tie-breaker.

Minute 3-6:
Choose window function and frame.

Minute 6-20:
Write SQL.

Minute 20-30:
Add validation and edge cases.

Minute 30-45:
Explain optimization and production concerns.
```

If candidate writes a window function without PARTITION BY/ORDER BY explanation:

```text
Stop and force them to explain partition and order before continuing.
```


## 104. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Does not know PARTITION BY | partition drills |
| Does not know ORDER BY | ordering drills |
| Missing tie-breaker | deterministic ranking drills |
| ROW_NUMBER/RANK confusion | ranking comparison drills |
| Filters rn in WHERE | CTE/QUALIFY drills |
| LAST_VALUE confusion | frame drills |
| Running total confusion | explicit frame drills |
| Moving average confusion | ROWS vs calendar drills |
| LAG confusion | previous-row drills |
| LEAD confusion | next-row drills |
| Dedupe weak | ROW_NUMBER dedupe drills |
| Top-N weak | aggregate then rank drills |
| Streak weak | gaps-and-islands drills |
| Session weak | LAG + SUM drills |
| Rolling distinct wrong | distinct-count reasoning drills |
| Performance weak | reduce input before window drills |
| No validation | output grain validation drills |

If weakness repeats:

```text
Use weakness-repair-mode.md.
```


## 105. Communication Scripts

### Partition script

```text
I partition by user_id because the calculation should restart for each user.
```

### Order script

```text
I order by event_time and event_id so the sequence is deterministic.
```

### ROW_NUMBER script

```text
I use ROW_NUMBER because I need exactly one survivor row per key.
```

### RANK script

```text
I use RANK because tied values should all be preserved.
```

### LAG script

```text
I use LAG to compare the current row to the previous row in the same entity's timeline.
```

### LEAD script

```text
I use LEAD to derive the end time of the current interval from the next row's start time.
```

### Frame script

```text
For running total, I use ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW.
```

### Filtering script

```text
Since WHERE cannot usually filter a window alias, I calculate the window result in a CTE and filter in the outer query.
```

### Validation script

```text
I validate the output by checking one row per business key and comparing key metrics before and after.
```

### Performance script

```text
Window functions often sort data, so I filter and reduce columns before applying them.
```


## 106. Candidate Self-Review Questions

After every window-function problem, candidate should answer:

```text
1. What is the output grain?
2. What rows should remain?
3. What is the partition key?
4. What is the order key?
5. Is the order deterministic?
6. What tie-breaker is needed?
7. Which window function fits?
8. Do I need a frame?
9. Should I use ROW_NUMBER, RANK, or DENSE_RANK?
10. Should I use LAG or LEAD?
11. Am I filtering window output correctly?
12. Should I aggregate before applying the window?
13. Did a join change the grain before the window?
14. Are NULLs handled?
15. Are ties handled?
16. Are missing dates relevant?
17. Does the database support QUALIFY?
18. How do I validate output?
19. How do I optimize the query?
20. What edge case would break this?
```

If candidate cannot answer these:

```text
The window-function solution is not interview-ready.
```


## 107. Maintenance Drills

After completing window functions, maintain skill with:

```text
1 ROW_NUMBER/dedupe drill per week
1 top-N/ranking drill per week
1 LAG/LEAD drill every 2 weeks
1 running/moving aggregate drill every 2 weeks
1 sessionization/streak drill every 2 weeks
1 full window-function mock every month
```

Maintenance rotation:

```text
Week 1: latest/first/dedupe/top-N
Week 2: LAG/LEAD/status changes/effective intervals
Week 3: running totals/moving averages/percent total
Week 4: sessionization/streaks/CDC/optimization
```

If score drops below 4:

```text
Run weakness-repair-mode.md for failed topic.
```


## 108. Progress Tracking Template

Use this progress format.

```text
# SQL Window Functions Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

Window mental model:
GROUP BY vs window:
PARTITION BY:
ORDER BY:
Window frames:
ROWS vs RANGE:
ROW_NUMBER:
RANK:
DENSE_RANK:
NTILE:
LAG:
LEAD:
FIRST_VALUE:
LAST_VALUE:
SUM OVER:
AVG OVER:
COUNT OVER:
Filtering window outputs:
QUALIFY:
Tie-breakers:
NULL handling:
Latest row:
First row:
Deduplication:
Top N per group:
Running totals:
Moving averages:
Percent of total:
Previous/next comparisons:
Status changes:
Sessionization:
Gaps and islands:
CDC current state:
SCD intervals:
Performance:
Validation:
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


## 109. Final Exit Test

Candidate passes SQL window functions when they can solve/explain:

```text
1. GROUP BY vs window function difference.
2. OVER clause anatomy.
3. PARTITION BY.
4. ORDER BY inside OVER.
5. Window frames.
6. ROWS vs RANGE.
7. ROW_NUMBER.
8. RANK.
9. DENSE_RANK.
10. NTILE.
11. LAG.
12. LEAD.
13. FIRST_VALUE.
14. LAST_VALUE and frame issue.
15. SUM OVER.
16. AVG OVER.
17. COUNT OVER.
18. Filtering window outputs with CTE.
19. QUALIFY when supported.
20. Latest row per key.
21. First row per key.
22. Deduplication with tie-breakers.
23. Top N per group.
24. Tied top records.
25. Running total.
26. Moving average.
27. Percent of total.
28. Percent of parent total.
29. Orders above user average.
30. Duplicate group audit.
31. Effective_to with LEAD.
32. Status change detection.
33. Sessionization.
34. Consecutive activity streaks.
35. Same-status runs.
36. CDC current state.
37. Previous/next event.
38. Running balance.
39. Rolling distinct caveat.
40. Cumulative distinct caveat.
41. Window optimization.
42. Window validation.
```

Passing standard:

```text
Average score >= 4/5.
No missing partition/order explanation.
No filtering window alias in WHERE.
No missing tie-breakers for ROW_NUMBER survivor logic.
No LAST_VALUE frame mistake.
No rolling distinct misunderstanding.
Can validate output grain and correctness.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles ranking, dedupe, time-series metrics, frames, LAG/LEAD, sessionization, gaps/islands, CDC/SCD, distinct-count caveats, optimization, and validation clearly under pressure.
```


## 110. Final Summary

SQL window functions are core to Data Engineering interviews.

They map directly to:

```text
deduplication
latest snapshot creation
CDC current state
SCD interval construction
top-N business rankings
running financial metrics
moving averages
conversion and retention metrics
status change detection
sessionization
streak analysis
data-quality monitoring
duplicate audit reporting
pipeline reliability checks
```

The candidate must master:

```text
PARTITION BY
ORDER BY
window frames
ROW_NUMBER
RANK
DENSE_RANK
NTILE
LAG
LEAD
FIRST_VALUE
LAST_VALUE
SUM/AVG/COUNT OVER
filtering with CTE/QUALIFY
tie-breakers
NULL handling
running totals
moving averages
percent of total
latest/first rows
deduplication
top-N per group
sessionization
gaps and islands
CDC/SCD patterns
performance optimization
validation
```

The mentor must be strict:

```text
No partition explanation → not interview-ready.
No order explanation → not interview-ready.
No tie-breaker → not interview-ready.
Wrong ROW_NUMBER/RANK choice → not interview-ready.
Filtering rn in WHERE → not interview-ready.
LAST_VALUE without frame awareness → not interview-ready.
Rolling distinct logic wrong → not interview-ready.
No validation → not interview-ready.
```

The goal is not to memorize syntax.

The goal is to identify the entity, sequence, tie-breaking rule, frame, and output grain, then write window SQL that is correct, deterministic, explainable, and scalable.


## 111. Problem Card Appendix

### Card 1: Latest Row

Topic:

```text
ROW_NUMBER DESC
```

Core idea:

```text
Keep most recent row per key.
```

Data Engineering connection:

```text
Current snapshots.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: First Row

Topic:

```text
ROW_NUMBER ASC
```

Core idea:

```text
Keep earliest row per key.
```

Data Engineering connection:

```text
First purchase.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Deduplication

Topic:

```text
ROW_NUMBER + COUNT
```

Core idea:

```text
Keep survivor and audit duplicates.
```

Data Engineering connection:

```text
Staging before MERGE.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Top N

Topic:

```text
ROW_NUMBER/RANK
```

Core idea:

```text
Rank entities within group.
```

Data Engineering connection:

```text
Product/customer rankings.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Tied Winners

Topic:

```text
RANK
```

Core idea:

```text
Preserve equal top values.
```

Data Engineering connection:

```text
Fair ranking.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Dense Ranking

Topic:

```text
DENSE_RANK
```

Core idea:

```text
Rank distinct value levels.
```

Data Engineering connection:

```text
Top N distinct tiers.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Previous Row

Topic:

```text
LAG
```

Core idea:

```text
Compare to prior event.
```

Data Engineering connection:

```text
Gaps/status changes.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Next Row

Topic:

```text
LEAD
```

Core idea:

```text
Compare to next event.
```

Data Engineering connection:

```text
Intervals/SCD.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Running Total

Topic:

```text
SUM frame
```

Core idea:

```text
Cumulative metric.
```

Data Engineering connection:

```text
Revenue/balance.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Moving Average

Topic:

```text
AVG frame
```

Core idea:

```text
Rolling metric.
```

Data Engineering connection:

```text
Monitoring.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Percent Total

Topic:

```text
SUM OVER
```

Core idea:

```text
Share of total.
```

Data Engineering connection:

```text
Category revenue.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Duplicate Audit

Topic:

```text
COUNT OVER
```

Core idea:

```text
Group size on each row.
```

Data Engineering connection:

```text
DQ reporting.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Effective Intervals

Topic:

```text
LEAD
```

Core idea:

```text
Next start becomes current end.
```

Data Engineering connection:

```text
SCD Type 2.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Sessionization

Topic:

```text
LAG + SUM
```

Core idea:

```text
Assign session groups.
```

Data Engineering connection:

```text
Clickstream.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Daily Streak

Topic:

```text
ROW_NUMBER island
```

Core idea:

```text
Consecutive active dates.
```

Data Engineering connection:

```text
Retention.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Status Runs

Topic:

```text
rn_all - rn_status
```

Core idea:

```text
Consecutive same status.
```

Data Engineering connection:

```text
Failures.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: CDC Current State

Topic:

```text
ROW_NUMBER source order
```

Core idea:

```text
Latest operation per key.
```

Data Engineering connection:

```text
CDC pipelines.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Running Balance

Topic:

```text
SUM over account
```

Core idea:

```text
Balance over time.
```

Data Engineering connection:

```text
Finance.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Deciles

Topic:

```text
NTILE
```

Core idea:

```text
Bucket entities.
```

Data Engineering connection:

```text
Segmentation.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Validation

Topic:

```text
grain checks
```

Core idea:

```text
Confirm output correctness.
```

Data Engineering connection:

```text
Production safety.
```

Candidate must be able to explain:

```text
1. Output grain.
2. Partition key.
3. Order key.
4. Tie-breaker.
5. Function choice.
6. Frame if needed.
7. Validation query.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 112. Data Engineering Scenario Appendix

### Scenario 1: API Duplicate Records

Pattern:

```text
ROW_NUMBER
```

Task:

```text
Keep latest record by source updated_at.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: CDC Current Orders

Pattern:

```text
ROW_NUMBER
```

Task:

```text
Pick latest operation and exclude deletes.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: User Plan History

Pattern:

```text
LEAD
```

Task:

```text
Create effective_to intervals.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: DAU Trend

Pattern:

```text
LAG
```

Task:

```text
Compare row count to previous day.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: Revenue Dashboard

Pattern:

```text
SUM/AVG windows
```

Task:

```text
Running totals and moving averages.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: Product Rankings

Pattern:

```text
ROW_NUMBER/RANK
```

Task:

```text
Top products per category.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: Payment Attempts

Pattern:

```text
ROW_NUMBER/LAG
```

Task:

```text
Attempt number and previous result.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: Pipeline Failures

Pattern:

```text
same-status islands
```

Task:

```text
Consecutive failed runs.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: Clickstream Sessions

Pattern:

```text
LAG + cumulative SUM
```

Task:

```text
Sessionize events.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: Customer Lifecycle

Pattern:

```text
ROW_NUMBER
```

Task:

```text
First, second, nth purchase.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: Marketing Attribution

Pattern:

```text
ROW_NUMBER after range join
```

Task:

```text
Choose latest prior touch.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Inventory Movement

Pattern:

```text
running SUM
```

Task:

```text
Compute stock level.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: SCD Validation

Pattern:

```text
LAG/running windows
```

Task:

```text
Find interval issues.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Data Quality Audit

Pattern:

```text
COUNT/LAG
```

Task:

```text
Duplicate groups and day-over-day changes.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: Revenue Share

Pattern:

```text
SUM OVER
```

Task:

```text
Share of total or parent total.
```

Minimum expected answer:

```text
1. Clarify grain.
2. Define partition/order.
3. Choose function.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```


## 113. Drill Appendix

### Drill 1: Partition Drill

Task:

```text
Given a problem, identify PARTITION BY columns.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Order Drill

Task:

```text
Given a problem, identify ORDER BY and tie-breakers.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: ROW_NUMBER Drill

Task:

```text
Keep latest and first rows.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: RANK Drill

Task:

```text
Preserve tied winners.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Dense Rank Drill

Task:

```text
Top N distinct value levels.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: LAG Drill

Task:

```text
Compare current row to previous row.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: LEAD Drill

Task:

```text
Create end dates from next start date.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Running Sum Drill

Task:

```text
Calculate cumulative revenue.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Moving Average Drill

Task:

```text
Calculate moving average with explicit frame.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Percent Total Drill

Task:

```text
Calculate share using SUM OVER.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Dedupe Drill

Task:

```text
Deduplicate staging records by business key.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Top N Drill

Task:

```text
Top N per group after aggregation.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Session Drill

Task:

```text
LAG and cumulative SUM for sessions.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Streak Drill

Task:

```text
ROW_NUMBER island key.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Status Run Drill

Task:

```text
rn_all minus rn_status.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: CDC Drill

Task:

```text
Latest operation per key.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Frame Drill

Task:

```text
Fix LAST_VALUE and running total frames.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: NULL Drill

Task:

```text
Handle NULL ordering and first/last values.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 19: Optimization Drill

Task:

```text
Reduce input before windowing.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 20: Validation Drill

Task:

```text
Check output uniqueness and totals.
```

Minimum passing answer:

```text
1. State output grain.
2. State partition.
3. State order/tie-breaker.
4. Choose correct window function.
5. State validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 114. Quick Reference Cards

### Quick Card 1: Window function

Summary:

```text
Group-aware calculation that preserves rows.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 2: PARTITION BY

Summary:

```text
Where calculation restarts.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 3: ORDER BY

Summary:

```text
Sequence inside partition.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 4: Frame

Summary:

```text
Rows included in aggregate window.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 5: ROW_NUMBER

Summary:

```text
Unique sequence; one survivor.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 6: RANK

Summary:

```text
Ties share rank, gaps appear.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 7: DENSE_RANK

Summary:

```text
Ties share rank, no gaps.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 8: NTILE

Summary:

```text
Bucket rows by count.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 9: LAG

Summary:

```text
Previous row value.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 10: LEAD

Summary:

```text
Next row value.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 11: FIRST_VALUE

Summary:

```text
First value in frame.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 12: LAST_VALUE

Summary:

```text
Last value in frame; frame-sensitive.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 13: SUM OVER

Summary:

```text
Total/running total/share denominator.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 14: AVG OVER

Summary:

```text
Group/moving average.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 15: COUNT OVER

Summary:

```text
Group size without collapsing rows.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 16: QUALIFY

Summary:

```text
Filter window results in supported dialects.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 17: CTE filter

Summary:

```text
Portable way to filter window results.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```

### Quick Card 18: Tie-breaker

Summary:

```text
Makes row selection deterministic.
```

Interview check:

```text
Give one SQL example and one Data Engineering use case.
```


## 115. Window Functions FAQ

### FAQ 1: What is a window function?

Answer:

```text
A function that calculates over related rows while preserving individual rows.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 2: How is it different from GROUP BY?

Answer:

```text
GROUP BY collapses rows; window functions keep rows and add group-aware values.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 3: When do I use ROW_NUMBER?

Answer:

```text
When you need sequence numbers or exactly one row per partition.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 4: When do I use RANK?

Answer:

```text
When tied values should share rank and all tied winners may be kept.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 5: Why do I need tie-breakers?

Answer:

```text
To make ROW_NUMBER survivor selection deterministic.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 6: Why can't I filter rn in WHERE?

Answer:

```text
WHERE is evaluated before SELECT window aliases; use CTE/subquery or QUALIFY.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 7: What does LAG do?

Answer:

```text
It returns a value from a previous row in the ordered partition.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 8: What does LEAD do?

Answer:

```text
It returns a value from a later row in the ordered partition.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 9: Why is LAST_VALUE tricky?

Answer:

```text
Default frames often end at current row, so explicit frame may be needed.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```

### FAQ 10: How do I optimize window functions?

Answer:

```text
Filter/project/pre-aggregate before windowing to reduce sorting work.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Performance consideration.
```


## 116. Additional Mini Scenario Cards

### Mini Scenario 1: Latest profile is nondeterministic

Recommended direction:

```text
Add tie-breakers to ROW_NUMBER ORDER BY.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 2: Top 3 excludes tied products

Recommended direction:

```text
Use RANK if ties should be preserved.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 3: Running total wrong after item join

Recommended direction:

```text
Fix input grain before applying SUM OVER.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 4: Moving average skips missing dates

Recommended direction:

```text
Build complete calendar before ROWS-based average.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 5: LAST_VALUE returns current row

Recommended direction:

```text
Use explicit UNBOUNDED FOLLOWING frame or ROW_NUMBER DESC.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 6: DAU cumulative count inflated

Recommended direction:

```text
Use first-seen logic, not SUM daily distinct.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 7: Rolling active users wrong

Recommended direction:

```text
Use date range distinct count, not sum of daily users.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 8: Window query slow

Recommended direction:

```text
Filter and project before window; aggregate before ranking.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 9: Dedup keeps wrong CDC row

Recommended direction:

```text
Order by source timestamp and sequence, not ingestion alone.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 10: Filtering rn fails

Recommended direction:

```text
Use CTE or QUALIFY.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 11: Duplicate events break streak

Recommended direction:

```text
Deduplicate to user-day before ROW_NUMBER island.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 12: Session count too high

Recommended direction:

```text
Check threshold rule and deterministic event ordering.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 13: Status run wrong

Recommended direction:

```text
Use rn_all - rn_status or LAG status changes.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 14: Rank by raw rows wrong

Recommended direction:

```text
Aggregate to product/category revenue before ranking.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 15: NULL timestamps chosen as latest

Recommended direction:

```text
Add NULL handling in ORDER BY.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 16: Ties hidden by ROW_NUMBER

Recommended direction:

```text
Use RANK to expose tied latest rows for review.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 17: Effective_to wrong with same timestamp

Recommended direction:

```text
Add sequence/tie-breaker to LEAD order.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 18: Payment attempt count wrong

Recommended direction:

```text
Partition by order_id, not user_id.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 19: Revenue share denominator wrong

Recommended direction:

```text
Partition SUM OVER by parent group when needed.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```

### Mini Scenario 20: CTE not optimized

Recommended direction:

```text
Check engine behavior; use QUALIFY or materialize if helpful.
```

Candidate must explain:

```text
1. Why the original logic is wrong.
2. Correct partition/order/frame.
3. Correct function choice.
4. Validation check.
5. Performance consideration.
```

Passing score:

```text
4/5 or higher.
```
