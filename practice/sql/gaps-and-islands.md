# SQL Gaps and Islands Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/sql/gaps-and-islands.md
```

This guide teaches and drills **gaps and islands problems in SQL for Data Engineering interviews**.

This is not a generic SQL syntax document. It is an interview-focused guide for candidates who need to detect consecutive sequences, missing values, continuous activity periods, streaks, active intervals, inactive gaps, missing partitions, subscription periods, status runs, consecutive login days, inventory stockout periods, sensor outage periods, and SLA breach intervals.

Gaps and islands are high-ROI because Data Engineering interviews often ask questions like:

- Find users active for 3 consecutive days.
- Find longest login streak per user.
- Find missing daily partitions.
- Find date ranges where a product was out of stock.
- Find continuous subscription periods.
- Merge overlapping intervals.
- Find gaps between orders.
- Find customers with no activity for more than 30 days.
- Find consecutive failed payments.
- Find uptime/downtime windows from status events.
- Find days where revenue data is missing.
- Find first/last date of each activity streak.
- Find employees with consecutive absence days.
- Find sessions from event gaps.
- Find islands of same status.
- Find time periods where inventory was zero.
- Find event streams where sequence numbers are missing.
- Find gaps in IDs.
- Find overlapping dimension effective-date intervals.
- Build current or historical active periods.

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

The purpose of this guide is to make the candidate strong at solving gaps and islands problems in SQL interviews.

The candidate should learn to answer:

```text
What is a gap?
What is an island?
How do I identify consecutive rows?
How do I group consecutive dates into ranges?
How do I find missing dates?
How do I find missing IDs?
How do I find active streaks?
How do I find longest streak per user?
How do I find gaps between events?
How do I split activity into sessions?
How do I merge overlapping intervals?
How do I detect overlapping SCD ranges?
How do I find status runs?
How do I find consecutive failures?
How do I handle duplicate dates before streak logic?
How do I handle missing calendar dates?
How do I use ROW_NUMBER for islands?
How do I use LAG for gaps?
How do I choose between row_number pattern and lag cumulative-sum pattern?
How do I validate gaps-and-islands output?
How do I explain dialect-specific date arithmetic?
```

A candidate is interview-ready only when they can:

```text
state the entity grain
deduplicate entity-date rows before streak logic
use ROW_NUMBER to build consecutive-date islands
use date - row_number technique
use LAG to compare current row to previous row
use cumulative SUM of break flags to build islands
detect missing values with calendar or sequence tables
merge overlapping intervals
detect gaps between intervals
handle same-day duplicates
handle timestamp vs date granularity
handle timezone assumptions
handle open-ended intervals
validate output ranges
explain business meaning clearly
```


## 2. Why Gaps and Islands Matter for Data Engineers

Gaps and islands problems appear in Data Engineering because data pipelines frequently deal with ordered sequences and time ranges.

Real Data Engineering examples:

```text
missing daily partitions in a warehouse table
consecutive user activity streaks
inactive customer gaps
continuous subscription periods
SCD effective-date interval validation
sensor outage periods
API sequence number gaps
inventory stockout ranges
payment failure streaks
campaign active date ranges
support SLA breach intervals
employee attendance streaks
service uptime and downtime periods
event sessionization
late-arriving date gaps
backfill completeness checks
```

Interviewers test this because it reveals:

```text
Can the candidate reason about ordered data?
Can they use window functions correctly?
Can they handle duplicates before sequence logic?
Can they translate business wording into SQL patterns?
Can they validate date ranges and missing intervals?
Can they explain time-bound edge cases?
Can they choose correct table grain?
```

Weak answer:

```text
Use GROUP BY date.
```

Strong answer:

```text
First I deduplicate to one row per entity per date, then use ROW_NUMBER partitioned by entity ordered by date. For consecutive dates, date minus row number stays constant, so I group by that value to form islands. Then I aggregate min/max date and count days per island, and validate output has non-overlapping ranges.
```

Interview line:

```text
Gaps and islands problems are mainly about ordering, grouping continuous sequences, and validating missing or broken periods.
```


## 3. Core Mental Model

A **gap** is a break in a sequence.

Examples:

```text
missing date in daily data
missing sequence number
inactive period between active periods
time difference greater than threshold
non-overlapping interval between two active intervals
```

An **island** is a continuous sequence.

Examples:

```text
consecutive active days
continuous subscription period
consecutive failed payment attempts
continuous stockout period
status run where state remains the same
session of events where gaps are less than 30 minutes
```

Most gaps-and-islands problems follow this flow:

```text
1. Choose entity.
2. Choose ordered column.
3. Normalize/deduplicate to correct grain.
4. Identify breaks.
5. Convert breaks into group IDs.
6. Aggregate each group into start/end/count.
7. Filter desired islands or gaps.
8. Validate output.
```

Two main SQL patterns:

```text
Pattern A:
date_or_number - ROW_NUMBER() creates a stable group key for consecutive values.

Pattern B:
LAG() finds breaks, then cumulative SUM() assigns island group IDs.
```

Core interview line:

```text
For simple consecutive dates/numbers, row_number difference is clean. For complex break rules, LAG plus cumulative SUM is more flexible.
```


## 4. Vocabulary

Important terms:

```text
Gap:
A missing or broken part of an ordered sequence.

Island:
A continuous run of ordered values.

Streak:
A consecutive island of activity or condition.

Consecutive:
Values follow each other without an unacceptable break.

Entity:
The object for which sequences are measured, such as user_id, product_id, account_id.

Grain:
What one row represents, such as user-day, product-day, event, interval.

Calendar table:
A table containing expected dates.

Sequence:
Ordered numeric or time-based values.

Break flag:
A 1/0 flag showing whether the current row starts a new island.

Island ID:
A generated group identifier for each island.

Open interval:
Interval with no known end date.

Overlapping interval:
Two intervals for same entity share time.

Adjacent interval:
One interval ends exactly when another begins.

Sessionization:
Grouping events into sessions based on time gaps.

Gaps-and-islands:
A class of SQL problems involving continuous ranges and missing ranges.
```


## 5. Standard Answer Framework

Use this framework for gaps-and-islands interview problems:

```text
1. Restate the business question.
2. Clarify entity grain:
   - per user?
   - per product?
   - per account?
   - global?
3. Clarify ordered field:
   - date?
   - timestamp?
   - sequence number?
   - effective interval?
4. Clarify consecutive rule:
   - exactly next day?
   - gap <= 30 minutes?
   - adjacent intervals merge?
   - missing weekends ignored?
5. Deduplicate to the correct grain.
6. Choose pattern:
   - ROW_NUMBER difference for simple consecutive values
   - LAG + cumulative SUM for complex break rules
   - calendar anti-join for missing dates
   - interval merge for overlapping ranges
7. Build islands or gaps.
8. Aggregate to start/end/count.
9. Filter longest/minimum/threshold if needed.
10. Validate:
   - no duplicate entity-date rows
   - no overlapping output islands
   - gap logic matches definition
11. Explain edge cases and dialect syntax.
```

Short version:

```text
Entity:
Grain:
Order:
Break rule:
Pattern:
SQL:
Validation:
Edge cases:
```

Strict rule:

```text
No gaps-and-islands answer is strong if the candidate does not define entity, order column, and break rule.
```


## 6. Scoring Rubric

Score each gaps-and-islands answer from 0 to 5.

### Score 0

No meaningful SQL or sequence reasoning.

### Score 1

Uses simple GROUP BY but cannot detect consecutive ranges.

### Score 2

Uses window functions partially but misses deduplication, partitioning, or break logic.

### Score 3

Mostly correct for simple cases but weak on duplicates, edge cases, or validation.

### Score 4

Interview-ready. Correct pattern, clear entity/grain, dedupe, grouping, aggregation, and validation.

### Score 5

Strong. Handles duplicates, timestamp/date granularity, custom gap thresholds, interval merging, missing calendars, SCD overlaps, performance, dialect differences, and production data-quality implications.

Do not give 4+ if:

```text
candidate does not define the entity
candidate ignores duplicate dates before streak logic
candidate does not partition by entity
candidate uses date arithmetic incorrectly
candidate cannot explain why date - row_number works
candidate cannot explain LAG break flag logic
candidate ignores missing calendar dates
candidate cannot handle ties
candidate cannot validate output ranges
candidate cannot explain edge cases
```


## 7. The Two Main Patterns

### Pattern 1: ROW_NUMBER difference

Use when:

```text
values are naturally consecutive
date increments by 1 day
numbers increment by 1
deduplicated grain exists
```

Example:

```sql
WITH user_days AS (
  SELECT DISTINCT
    user_id,
    CAST(event_time AS DATE) AS active_date
  FROM events
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
)
SELECT
  user_id,
  MIN(active_date) AS streak_start,
  MAX(active_date) AS streak_end,
  COUNT(*) AS streak_days
FROM (
  SELECT
    *,
    active_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
) x
GROUP BY user_id, island_key;
```

### Pattern 2: LAG + cumulative SUM

Use when:

```text
break rule is custom
gap threshold is 30 minutes
status changes define islands
interval adjacency/overlap matters
business rule is not simple +1 day
```

Example:

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
      WHEN previous_event_time IS NULL
        OR event_time > previous_event_time + INTERVAL '30 minutes'
      THEN 1 ELSE 0
    END AS new_session_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_session_flag) OVER (
      PARTITION BY user_id
      ORDER BY event_time
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS session_id
  FROM flagged
)
SELECT
  user_id,
  session_id,
  MIN(event_time) AS session_start,
  MAX(event_time) AS session_end,
  COUNT(*) AS events_in_session
FROM grouped
GROUP BY user_id, session_id;
```

Interview line:

```text
ROW_NUMBER difference is best for simple consecutive islands; LAG plus cumulative sum is best for custom break rules.
```


## 8. Date Arithmetic Dialect Notes

Date arithmetic differs across databases.

### PostgreSQL-style

```sql
active_date - rn * INTERVAL '1 day'
event_time + INTERVAL '30 minutes'
```

### SQL Server-style

```sql
DATEADD(day, -rn, active_date)
DATEADD(minute, 30, previous_event_time)
DATEDIFF(day, previous_date, active_date)
```

### BigQuery-style

```sql
DATE_SUB(active_date, INTERVAL rn DAY)
TIMESTAMP_ADD(previous_event_time, INTERVAL 30 MINUTE)
DATE_DIFF(active_date, previous_date, DAY)
```

### Snowflake-style

```sql
DATEADD(day, -rn, active_date)
DATEADD(minute, 30, previous_event_time)
DATEDIFF(day, previous_date, active_date)
```

Interview-safe statement:

```text
I will use PostgreSQL-style syntax for readability unless a specific SQL dialect is required.
```


## 9. Why date - row_number Works

Suppose a user was active on these dates:

```text
2026-01-01
2026-01-02
2026-01-03
2026-01-06
2026-01-07
```

Assign row numbers:

```text
date        rn
2026-01-01  1
2026-01-02  2
2026-01-03  3
2026-01-06  4
2026-01-07  5
```

Subtract rn days:

```text
date        rn   date - rn days
2026-01-01  1    2025-12-31
2026-01-02  2    2025-12-31
2026-01-03  3    2025-12-31

2026-01-06  4    2026-01-02
2026-01-07  5    2026-01-02
```

The stable value identifies each island.

```text
Island 1 key = 2025-12-31
Island 2 key = 2026-01-02
```

Then group by:

```text
user_id, island_key
```

Interview line:

```text
For consecutive dates, date minus row_number remains constant inside a streak and changes when a gap appears.
```


## 10. Deduplicate Before Streak Logic

This is one of the biggest interview mistakes.

Problem:

```text
A user can have many events on the same day.
If we calculate ROW_NUMBER directly on event rows, same-day duplicates break the streak logic.
```

Bad:

```sql
SELECT
  user_id,
  event_time,
  ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY event_time
  ) AS rn
FROM events;
```

Better:

```sql
WITH user_days AS (
  SELECT DISTINCT
    user_id,
    CAST(event_time AS DATE) AS active_date
  FROM events
  WHERE user_id IS NOT NULL
)
SELECT *
FROM user_days;
```

Then apply streak logic.

Interview line:

```text
For daily streaks, I first reduce the data to one row per user per active date.
```


## 11. Case 1: Users Active for At Least 3 Consecutive Days

Business question:

```text
Find users who were active for at least 3 consecutive days.
```

Table:

```sql
events(event_id, user_id, event_time)
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
WHERE streak_days >= 3
ORDER BY user_id, streak_start;
```

Key points:

```text
Deduplicate to one row per user/day.
Partition by user_id.
Use date - row_number island key.
Filter streak_days >= 3.
```

Interview line:

```text
This is the classic gaps-and-islands daily streak pattern.
```


## 12. Case 2: Longest Login Streak Per User

Business question:

```text
Find each user's longest consecutive login-day streak.
```

Table:

```sql
logins(user_id, login_time)
```

SQL:

```sql
WITH login_days AS (
  SELECT DISTINCT
    user_id,
    CAST(login_time AS DATE) AS login_date
  FROM logins
  WHERE user_id IS NOT NULL
),
numbered AS (
  SELECT
    user_id,
    login_date,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY login_date
    ) AS rn
  FROM login_days
),
islands AS (
  SELECT
    user_id,
    login_date,
    login_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
),
streaks AS (
  SELECT
    user_id,
    MIN(login_date) AS streak_start,
    MAX(login_date) AS streak_end,
    COUNT(*) AS streak_days
  FROM islands
  GROUP BY user_id, island_key
),
ranked_streaks AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY streak_days DESC, streak_end DESC, streak_start DESC
    ) AS rn
  FROM streaks
)
SELECT
  user_id,
  streak_start,
  streak_end,
  streak_days
FROM ranked_streaks
WHERE rn = 1
ORDER BY user_id;
```

Tie rule:

```text
If multiple longest streaks have same length, this keeps the most recent one.
```

If all tied longest streaks are required:

```text
Use RANK instead of ROW_NUMBER.
```

Interview line:

```text
Longest streak requires building islands first, then ranking islands per user.
```


## 13. Case 3: Missing Daily Partitions

Business question:

```text
Find dates in January 2026 with no records loaded into fact_orders.
```

Tables:

```sql
dim_calendar(calendar_date)
fact_orders(order_id, order_date)
```

SQL:

```sql
WITH expected_dates AS (
  SELECT calendar_date
  FROM dim_calendar
  WHERE calendar_date >= DATE '2026-01-01'
    AND calendar_date <  DATE '2026-02-01'
),
actual_dates AS (
  SELECT DISTINCT
    order_date
  FROM fact_orders
  WHERE order_date >= DATE '2026-01-01'
    AND order_date <  DATE '2026-02-01'
)
SELECT
  e.calendar_date AS missing_date
FROM expected_dates e
LEFT JOIN actual_dates a
  ON e.calendar_date = a.order_date
WHERE a.order_date IS NULL
ORDER BY missing_date;
```

Alternative with NOT EXISTS:

```sql
SELECT
  e.calendar_date AS missing_date
FROM expected_dates e
WHERE NOT EXISTS (
  SELECT 1
  FROM actual_dates a
  WHERE a.order_date = e.calendar_date
);
```

Interview line:

```text
Missing-date problems usually need an expected calendar table or generated date series.
```


## 14. Case 4: Group Missing Dates Into Gaps

Business question:

```text
Find continuous missing-date ranges in January 2026.
```

SQL:

```sql
WITH expected_dates AS (
  SELECT calendar_date
  FROM dim_calendar
  WHERE calendar_date >= DATE '2026-01-01'
    AND calendar_date <  DATE '2026-02-01'
),
actual_dates AS (
  SELECT DISTINCT order_date
  FROM fact_orders
  WHERE order_date >= DATE '2026-01-01'
    AND order_date <  DATE '2026-02-01'
),
missing_dates AS (
  SELECT
    e.calendar_date AS missing_date
  FROM expected_dates e
  LEFT JOIN actual_dates a
    ON e.calendar_date = a.order_date
  WHERE a.order_date IS NULL
),
numbered AS (
  SELECT
    missing_date,
    ROW_NUMBER() OVER (
      ORDER BY missing_date
    ) AS rn
  FROM missing_dates
),
islands AS (
  SELECT
    missing_date,
    missing_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  MIN(missing_date) AS gap_start,
  MAX(missing_date) AS gap_end,
  COUNT(*) AS missing_days
FROM islands
GROUP BY island_key
ORDER BY gap_start;
```

Interview line:

```text
First identify missing dates, then use the same islands pattern to group consecutive missing dates into ranges.
```


## 15. Case 5: Missing Sequence Numbers

Business question:

```text
Find missing event sequence numbers.
```

Tables:

```sql
expected_sequence(seq_num)
events(seq_num)
```

SQL:

```sql
WITH actual_sequence AS (
  SELECT DISTINCT seq_num
  FROM events
),
missing_sequence AS (
  SELECT
    e.seq_num
  FROM expected_sequence e
  LEFT JOIN actual_sequence a
    ON e.seq_num = a.seq_num
  WHERE a.seq_num IS NULL
)
SELECT *
FROM missing_sequence
ORDER BY seq_num;
```

Group missing sequence ranges:

```sql
WITH missing_sequence AS (...),
numbered AS (
  SELECT
    seq_num,
    ROW_NUMBER() OVER (ORDER BY seq_num) AS rn
  FROM missing_sequence
),
islands AS (
  SELECT
    seq_num,
    seq_num - rn AS island_key
  FROM numbered
)
SELECT
  MIN(seq_num) AS gap_start,
  MAX(seq_num) AS gap_end,
  COUNT(*) AS missing_count
FROM islands
GROUP BY island_key
ORDER BY gap_start;
```

Interview line:

```text
For consecutive integers, value - row_number is the numeric version of the date island key.
```


## 16. Case 6: Find Gaps Between User Events

Business question:

```text
Find gaps greater than 30 minutes between consecutive events for each user.
```

Table:

```sql
events(event_id, user_id, event_time)
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
)
SELECT
  user_id,
  previous_event_time AS gap_start,
  event_time AS gap_end,
  event_time - previous_event_time AS gap_duration
FROM ordered_events
WHERE previous_event_time IS NOT NULL
  AND event_time > previous_event_time + INTERVAL '30 minutes'
ORDER BY user_id, gap_start;
```

Interview line:

```text
LAG compares each row to the previous row and is the standard pattern for detecting gaps between events.
```


## 17. Case 7: Sessionize Events by 30-Minute Gap

Business question:

```text
Group user events into sessions where a new session starts after 30 minutes of inactivity.
```

Table:

```sql
events(event_id, user_id, event_time)
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
GROUP BY user_id, session_number
ORDER BY user_id, session_start;
```

Key idea:

```text
new_session_flag marks breaks.
Cumulative SUM converts break flags into island/session IDs.
```

Interview line:

```text
Sessionization is a gaps-and-islands problem using LAG and cumulative SUM.
```


## 18. Case 8: Consecutive Failed Payments

Business question:

```text
Find users with at least 3 consecutive failed payment attempts.
```

Table:

```sql
payment_attempts(payment_attempt_id, user_id, attempted_at, status)
```

SQL:

```sql
WITH ordered_attempts AS (
  SELECT
    user_id,
    payment_attempt_id,
    attempted_at,
    status,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY attempted_at, payment_attempt_id
    ) AS rn_all,
    ROW_NUMBER() OVER (
      PARTITION BY user_id, status
      ORDER BY attempted_at, payment_attempt_id
    ) AS rn_status
  FROM payment_attempts
),
status_islands AS (
  SELECT
    *,
    rn_all - rn_status AS island_key
  FROM ordered_attempts
),
failed_streaks AS (
  SELECT
    user_id,
    MIN(attempted_at) AS streak_start,
    MAX(attempted_at) AS streak_end,
    COUNT(*) AS failed_attempts
  FROM status_islands
  WHERE status = 'FAILED'
  GROUP BY user_id, island_key
)
SELECT *
FROM failed_streaks
WHERE failed_attempts >= 3
ORDER BY user_id, streak_start;
```

Why this works:

```text
The difference between total row number and status-specific row number stays constant while status remains the same.
```

Interview line:

```text
For consecutive same-status runs, row_number over all rows minus row_number over status creates status islands.
```


## 19. Case 9: Status Runs

Business question:

```text
Convert event status changes into continuous status runs.
```

Table:

```sql
device_status_events(device_id, event_time, status)
```

SQL:

```sql
WITH ordered AS (
  SELECT
    device_id,
    event_time,
    status,
    LAG(status) OVER (
      PARTITION BY device_id
      ORDER BY event_time
    ) AS previous_status
  FROM device_status_events
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_status IS NULL OR status <> previous_status
      THEN 1 ELSE 0
    END AS new_status_run_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_status_run_flag) OVER (
      PARTITION BY device_id
      ORDER BY event_time
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS status_run_id
  FROM flagged
)
SELECT
  device_id,
  status,
  MIN(event_time) AS run_start,
  MAX(event_time) AS last_event_time,
  COUNT(*) AS events_in_run
FROM grouped
GROUP BY device_id, status_run_id, status
ORDER BY device_id, run_start;
```

If you need run_end as next run start:

```sql
WITH runs AS (
  SELECT
    device_id,
    status,
    MIN(event_time) AS run_start
  FROM grouped
  GROUP BY device_id, status_run_id, status
)
SELECT
  device_id,
  status,
  run_start,
  LEAD(run_start) OVER (
    PARTITION BY device_id
    ORDER BY run_start
  ) AS run_end
FROM runs;
```

Interview line:

```text
Status-run islands are built by flagging status changes and cumulatively summing those flags.
```


## 20. Case 10: Inventory Stockout Periods

Business question:

```text
Find continuous date ranges where product inventory was zero.
```

Table:

```sql
inventory_snapshot(product_id, snapshot_date, inventory_quantity)
```

SQL:

```sql
WITH product_days AS (
  SELECT
    product_id,
    snapshot_date,
    inventory_quantity
  FROM inventory_snapshot
),
stockout_days AS (
  SELECT DISTINCT
    product_id,
    snapshot_date
  FROM product_days
  WHERE inventory_quantity = 0
),
numbered AS (
  SELECT
    product_id,
    snapshot_date,
    ROW_NUMBER() OVER (
      PARTITION BY product_id
      ORDER BY snapshot_date
    ) AS rn
  FROM stockout_days
),
islands AS (
  SELECT
    product_id,
    snapshot_date,
    snapshot_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  product_id,
  MIN(snapshot_date) AS stockout_start,
  MAX(snapshot_date) AS stockout_end,
  COUNT(*) AS stockout_days
FROM islands
GROUP BY product_id, island_key
ORDER BY product_id, stockout_start;
```

Validation:

```text
Check product_id, snapshot_date is unique before this logic.
```

Interview line:

```text
Stockout periods are islands of product-days where inventory_quantity = 0.
```


## 21. Case 11: Subscription Active Periods from Daily Activity

Business question:

```text
Given daily active subscription rows, group consecutive active days into active periods.
```

Table:

```sql
subscription_daily(subscription_id, active_date)
```

SQL:

```sql
WITH active_days AS (
  SELECT DISTINCT
    subscription_id,
    active_date
  FROM subscription_daily
),
numbered AS (
  SELECT
    subscription_id,
    active_date,
    ROW_NUMBER() OVER (
      PARTITION BY subscription_id
      ORDER BY active_date
    ) AS rn
  FROM active_days
),
islands AS (
  SELECT
    subscription_id,
    active_date,
    active_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  subscription_id,
  MIN(active_date) AS active_start,
  MAX(active_date) AS active_end,
  COUNT(*) AS active_days
FROM islands
GROUP BY subscription_id, island_key
ORDER BY subscription_id, active_start;
```

Interview line:

```text
When the input is daily state, active periods are consecutive active-date islands.
```


## 22. Case 12: Gaps Between Subscription Periods

Business question:

```text
For each user, find gaps between subscription periods.
```

Table:

```sql
subscriptions(user_id, subscription_id, started_at, ended_at)
```

SQL:

```sql
WITH ordered_periods AS (
  SELECT
    user_id,
    subscription_id,
    started_at,
    ended_at,
    LAG(ended_at) OVER (
      PARTITION BY user_id
      ORDER BY started_at, subscription_id
    ) AS previous_ended_at
  FROM subscriptions
)
SELECT
  user_id,
  previous_ended_at AS gap_start,
  started_at AS gap_end,
  started_at - previous_ended_at AS gap_duration
FROM ordered_periods
WHERE previous_ended_at IS NOT NULL
  AND started_at > previous_ended_at
ORDER BY user_id, gap_start;
```

Clarify:

```text
If ended_at is inclusive, gap may start ended_at + 1 day.
If ended_at is exclusive, gap starts ended_at.
```

Interview line:

```text
Interval gap logic depends on whether interval end is inclusive or exclusive.
```


## 23. Case 13: Merge Overlapping Intervals

Business question:

```text
Merge overlapping or adjacent subscription intervals per user.
```

Table:

```sql
subscriptions(user_id, started_at, ended_at)
```

PostgreSQL-style SQL:

```sql
WITH ordered AS (
  SELECT
    user_id,
    started_at,
    ended_at,
    MAX(ended_at) OVER (
      PARTITION BY user_id
      ORDER BY started_at, ended_at
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS previous_max_end
  FROM subscriptions
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_max_end IS NULL
        OR started_at > previous_max_end
      THEN 1 ELSE 0
    END AS new_island_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_island_flag) OVER (
      PARTITION BY user_id
      ORDER BY started_at, ended_at
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS island_id
  FROM flagged
)
SELECT
  user_id,
  MIN(started_at) AS merged_start,
  MAX(ended_at) AS merged_end
FROM grouped
GROUP BY user_id, island_id
ORDER BY user_id, merged_start;
```

Important:

```text
Use previous running max end, not only LAG(ended_at), because one long interval can cover several following intervals.
```

Interview line:

```text
For overlapping interval merge, compare start to the running maximum prior end, not just the immediately previous end.
```


## 24. Case 14: Detect Overlapping SCD Effective Intervals

Business question:

```text
Find user profile history rows where effective intervals overlap.
```

Table:

```sql
user_profile_history(user_id, effective_from, effective_to)
```

SQL:

```sql
WITH intervals AS (
  SELECT
    user_id,
    effective_from,
    COALESCE(effective_to, TIMESTAMP '9999-12-31') AS effective_to
  FROM user_profile_history
),
ordered AS (
  SELECT
    user_id,
    effective_from,
    effective_to,
    LAG(effective_to) OVER (
      PARTITION BY user_id
      ORDER BY effective_from, effective_to
    ) AS previous_effective_to
  FROM intervals
)
SELECT
  user_id,
  effective_from,
  effective_to,
  previous_effective_to
FROM ordered
WHERE previous_effective_to IS NOT NULL
  AND effective_from < previous_effective_to
ORDER BY user_id, effective_from;
```

Caution:

```text
This detects overlap with previous ordered interval.
For complex interval nesting, running max previous end is safer.
```

Running max version:

```sql
WITH intervals AS (...),
ordered AS (
  SELECT
    *,
    MAX(effective_to) OVER (
      PARTITION BY user_id
      ORDER BY effective_from, effective_to
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS previous_max_to
  FROM intervals
)
SELECT *
FROM ordered
WHERE previous_max_to IS NOT NULL
  AND effective_from < previous_max_to;
```

Interview line:

```text
SCD overlap detection protects as-of joins from matching multiple dimension rows.
```


## 25. Case 15: Find Non-Overlapping Gaps in SCD Intervals

Business question:

```text
Find gaps between user profile effective intervals.
```

Table:

```sql
user_profile_history(user_id, effective_from, effective_to)
```

SQL:

```sql
WITH intervals AS (
  SELECT
    user_id,
    effective_from,
    effective_to
  FROM user_profile_history
  WHERE effective_to IS NOT NULL
),
ordered AS (
  SELECT
    user_id,
    effective_from,
    effective_to,
    LAG(effective_to) OVER (
      PARTITION BY user_id
      ORDER BY effective_from
    ) AS previous_effective_to
  FROM intervals
)
SELECT
  user_id,
  previous_effective_to AS gap_start,
  effective_from AS gap_end
FROM ordered
WHERE previous_effective_to IS NOT NULL
  AND effective_from > previous_effective_to
ORDER BY user_id, gap_start;
```

Boundary clarification:

```text
If intervals are half-open [from, to), then effective_from = previous_effective_to is adjacent with no gap.
If intervals are inclusive, logic changes.
```

Interview line:

```text
SCD gaps and overlaps depend heavily on whether intervals are inclusive or half-open.
```


## 26. Case 16: Consecutive Order Months

Business question:

```text
Find customers who ordered in at least 3 consecutive months.
```

Table:

```sql
orders(order_id, user_id, order_time, order_status)
```

SQL:

```sql
WITH user_months AS (
  SELECT DISTINCT
    user_id,
    DATE_TRUNC('month', order_time) AS order_month
  FROM orders
  WHERE order_status = 'COMPLETED'
    AND user_id IS NOT NULL
),
numbered AS (
  SELECT
    user_id,
    order_month,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_month
    ) AS rn
  FROM user_months
),
islands AS (
  SELECT
    user_id,
    order_month,
    order_month - rn * INTERVAL '1 month' AS island_key
  FROM numbered
),
month_streaks AS (
  SELECT
    user_id,
    MIN(order_month) AS streak_start_month,
    MAX(order_month) AS streak_end_month,
    COUNT(*) AS consecutive_months
  FROM islands
  GROUP BY user_id, island_key
)
SELECT *
FROM month_streaks
WHERE consecutive_months >= 3
ORDER BY user_id, streak_start_month;
```

Dialect caution:

```text
Month arithmetic differs and can behave differently at month-end dates.
DATE_TRUNC to month avoids day-of-month issues.
```

Interview line:

```text
For monthly streaks, normalize to month start before applying row_number difference.
```


## 27. Case 17: Consecutive Weeks Active

Business question:

```text
Find users active for at least 4 consecutive weeks.
```

Table:

```sql
events(user_id, event_time)
```

SQL:

```sql
WITH user_weeks AS (
  SELECT DISTINCT
    user_id,
    DATE_TRUNC('week', event_time) AS active_week
  FROM events
  WHERE user_id IS NOT NULL
),
numbered AS (
  SELECT
    user_id,
    active_week,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY active_week
    ) AS rn
  FROM user_weeks
),
islands AS (
  SELECT
    user_id,
    active_week,
    active_week - rn * INTERVAL '1 week' AS island_key
  FROM numbered
),
week_streaks AS (
  SELECT
    user_id,
    MIN(active_week) AS streak_start_week,
    MAX(active_week) AS streak_end_week,
    COUNT(*) AS consecutive_weeks
  FROM islands
  GROUP BY user_id, island_key
)
SELECT *
FROM week_streaks
WHERE consecutive_weeks >= 4;
```

Clarification:

```text
Week start day differs by database/business definition.
```

Interview line:

```text
Weekly streaks require agreement on week boundary, such as Monday-start or Sunday-start.
```


## 28. Case 18: Inactive Users for More Than 30 Days Between Events

Business question:

```text
Find users who had a gap of more than 30 days between activities.
```

Table:

```sql
events(user_id, event_time)
```

SQL:

```sql
WITH user_activity_days AS (
  SELECT DISTINCT
    user_id,
    CAST(event_time AS DATE) AS activity_date
  FROM events
  WHERE user_id IS NOT NULL
),
ordered AS (
  SELECT
    user_id,
    activity_date,
    LAG(activity_date) OVER (
      PARTITION BY user_id
      ORDER BY activity_date
    ) AS previous_activity_date
  FROM user_activity_days
)
SELECT
  user_id,
  previous_activity_date,
  activity_date,
  activity_date - previous_activity_date AS inactive_gap_days
FROM ordered
WHERE previous_activity_date IS NOT NULL
  AND activity_date > previous_activity_date + INTERVAL '30 days'
ORDER BY user_id, previous_activity_date;
```

Interview line:

```text
Inactivity gaps are found with LAG and a threshold comparison.
```


## 29. Case 19: Dormant Users as of Analysis Date

Business question:

```text
Find users whose last activity was more than 30 days before analysis date.
```

Table:

```sql
events(user_id, event_time)
```

SQL:

```sql
WITH last_activity AS (
  SELECT
    user_id,
    MAX(CAST(event_time AS DATE)) AS last_activity_date
  FROM events
  WHERE user_id IS NOT NULL
  GROUP BY user_id
)
SELECT
  user_id,
  last_activity_date
FROM last_activity
WHERE last_activity_date < DATE '2026-02-01' - INTERVAL '30 days'
ORDER BY last_activity_date;
```

Difference from previous case:

```text
This checks gap from last activity to analysis date.
The previous case checks gaps between activities.
```

Interview line:

```text
Dormancy can mean current inactivity since last activity, not necessarily a gap between two past events.
```


## 30. Case 20: Consecutive Revenue Drop Days

Business question:

```text
Find periods where daily revenue decreased for at least 3 consecutive days.
```

Table:

```sql
daily_revenue(revenue_date, revenue)
```

SQL:

```sql
WITH with_previous AS (
  SELECT
    revenue_date,
    revenue,
    LAG(revenue) OVER (
      ORDER BY revenue_date
    ) AS previous_revenue
  FROM daily_revenue
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_revenue IS NOT NULL AND revenue < previous_revenue
      THEN 0 ELSE 1
    END AS new_run_flag
  FROM with_previous
),
grouped AS (
  SELECT
    *,
    SUM(new_run_flag) OVER (
      ORDER BY revenue_date
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS run_id
  FROM flagged
),
drop_runs AS (
  SELECT
    MIN(revenue_date) AS run_start,
    MAX(revenue_date) AS run_end,
    COUNT(*) AS days_in_run
  FROM grouped
  WHERE previous_revenue IS NOT NULL
    AND revenue < previous_revenue
  GROUP BY run_id
)
SELECT *
FROM drop_runs
WHERE days_in_run >= 3;
```

Caution:

```text
This counts days where revenue is lower than previous day.
Define whether first day of run should include the day before drop started.
```

Interview line:

```text
Trend-based islands use LAG to classify each row, then group consecutive rows where the condition holds.
```


## 31. Case 21: Consecutive Increasing Spend Months

Business question:

```text
Find customers with spend increasing for 3 consecutive months.
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
with_previous AS (
  SELECT
    user_id,
    order_month,
    spend,
    LAG(spend) OVER (
      PARTITION BY user_id
      ORDER BY order_month
    ) AS previous_spend
  FROM monthly_spend
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_spend IS NOT NULL AND spend > previous_spend
      THEN 0 ELSE 1
    END AS new_run_flag
  FROM with_previous
),
grouped AS (
  SELECT
    *,
    SUM(new_run_flag) OVER (
      PARTITION BY user_id
      ORDER BY order_month
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS run_id
  FROM flagged
),
increasing_runs AS (
  SELECT
    user_id,
    MIN(order_month) AS run_start_month,
    MAX(order_month) AS run_end_month,
    COUNT(*) AS increasing_month_count
  FROM grouped
  WHERE previous_spend IS NOT NULL
    AND spend > previous_spend
  GROUP BY user_id, run_id
)
SELECT *
FROM increasing_runs
WHERE increasing_month_count >= 3;
```

Caution:

```text
This assumes missing months are absent, not zero.
If missing months should be zero, build user-month calendar first.
```

Interview line:

```text
For monthly trend streaks, clarify whether missing months break the streak or count as zero.
```


## 32. Case 22: Uptime/Downtime Periods

Business question:

```text
Given service status events, derive downtime windows.
```

Table:

```sql
service_status_events(service_id, event_time, status)
```

SQL:

```sql
WITH ordered AS (
  SELECT
    service_id,
    event_time AS status_start,
    status,
    LEAD(event_time) OVER (
      PARTITION BY service_id
      ORDER BY event_time
    ) AS status_end
  FROM service_status_events
)
SELECT
  service_id,
  status_start AS downtime_start,
  status_end AS downtime_end
FROM ordered
WHERE status = 'DOWN'
ORDER BY service_id, downtime_start;
```

If consecutive same status events must be merged first:

```text
Use status-run pattern before deriving periods.
```

Interview line:

```text
Status events often represent state starting at event_time and ending at next event_time.
```


## 33. Case 23: Sensor Outage Periods

Business question:

```text
A sensor should send readings every minute. Find gaps greater than 5 minutes.
```

Table:

```sql
sensor_readings(sensor_id, reading_time)
```

SQL:

```sql
WITH ordered_readings AS (
  SELECT
    sensor_id,
    reading_time,
    LAG(reading_time) OVER (
      PARTITION BY sensor_id
      ORDER BY reading_time
    ) AS previous_reading_time
  FROM sensor_readings
)
SELECT
  sensor_id,
  previous_reading_time AS outage_start_after,
  reading_time AS outage_end_at,
  reading_time - previous_reading_time AS gap_duration
FROM ordered_readings
WHERE previous_reading_time IS NOT NULL
  AND reading_time > previous_reading_time + INTERVAL '5 minutes'
ORDER BY sensor_id, outage_start_after;
```

Interview line:

```text
Expected-frequency gaps are LAG comparisons against the allowed interval.
```


## 34. Case 24: Consecutive Absence Days

Business question:

```text
Find employees absent for at least 3 consecutive workdays.
```

Tables:

```sql
attendance(employee_id, attendance_date, status)
dim_calendar(calendar_date, is_workday)
```

SQL:

```sql
WITH absent_workdays AS (
  SELECT DISTINCT
    a.employee_id,
    a.attendance_date
  FROM attendance a
  JOIN dim_calendar c
    ON a.attendance_date = c.calendar_date
  WHERE a.status = 'ABSENT'
    AND c.is_workday = true
),
workday_numbers AS (
  SELECT
    calendar_date,
    ROW_NUMBER() OVER (
      ORDER BY calendar_date
    ) AS workday_num
  FROM dim_calendar
  WHERE is_workday = true
),
absent_numbered AS (
  SELECT
    a.employee_id,
    a.attendance_date,
    w.workday_num,
    ROW_NUMBER() OVER (
      PARTITION BY a.employee_id
      ORDER BY a.attendance_date
    ) AS rn
  FROM absent_workdays a
  JOIN workday_numbers w
    ON a.attendance_date = w.calendar_date
),
islands AS (
  SELECT
    employee_id,
    attendance_date,
    workday_num - rn AS island_key
  FROM absent_numbered
)
SELECT
  employee_id,
  MIN(attendance_date) AS absence_start,
  MAX(attendance_date) AS absence_end,
  COUNT(*) AS absent_workdays
FROM islands
GROUP BY employee_id, island_key
HAVING COUNT(*) >= 3;
```

Why workday_num:

```text
Calendar dates are not consecutive across weekends/holidays, so use consecutive workday sequence numbers.
```

Interview line:

```text
When weekends or holidays should be ignored, use a business calendar sequence instead of raw date arithmetic.
```


## 35. Case 25: Consecutive Business Days With No Orders

Business question:

```text
Find gaps of at least 2 consecutive business days with no orders.
```

Tables:

```sql
dim_calendar(calendar_date, is_business_day)
orders(order_date)
```

SQL:

```sql
WITH business_days AS (
  SELECT
    calendar_date,
    ROW_NUMBER() OVER (
      ORDER BY calendar_date
    ) AS business_day_num
  FROM dim_calendar
  WHERE is_business_day = true
),
order_days AS (
  SELECT DISTINCT
    order_date
  FROM orders
),
missing_business_days AS (
  SELECT
    b.calendar_date,
    b.business_day_num
  FROM business_days b
  LEFT JOIN order_days o
    ON b.calendar_date = o.order_date
  WHERE o.order_date IS NULL
),
numbered_missing AS (
  SELECT
    calendar_date,
    business_day_num,
    ROW_NUMBER() OVER (
      ORDER BY business_day_num
    ) AS rn
  FROM missing_business_days
),
islands AS (
  SELECT
    calendar_date,
    business_day_num - rn AS island_key
  FROM numbered_missing
)
SELECT
  MIN(calendar_date) AS gap_start,
  MAX(calendar_date) AS gap_end,
  COUNT(*) AS missing_business_days
FROM islands
GROUP BY island_key
HAVING COUNT(*) >= 2
ORDER BY gap_start;
```

Interview line:

```text
Business-day gaps require a calendar table with a business-day sequence.
```


## 36. Case 26: Consecutive Same Category Purchases

Business question:

```text
Find users who bought from the same category in 3 consecutive orders.
```

Tables:

```sql
orders(order_id, user_id, order_time)
order_items(order_id, product_id)
products(product_id, category)
```

Simplification:

```text
Assume each order has one primary category after aggregation.
```

SQL:

```sql
WITH order_categories AS (
  SELECT
    o.user_id,
    o.order_id,
    o.order_time,
    MIN(p.category) AS category
  FROM orders o
  JOIN order_items oi
    ON o.order_id = oi.order_id
  JOIN products p
    ON oi.product_id = p.product_id
  GROUP BY o.user_id, o.order_id, o.order_time
),
numbered AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_time, order_id
    ) AS rn_all,
    ROW_NUMBER() OVER (
      PARTITION BY user_id, category
      ORDER BY order_time, order_id
    ) AS rn_category
  FROM order_categories
),
islands AS (
  SELECT
    *,
    rn_all - rn_category AS island_key
  FROM numbered
)
SELECT
  user_id,
  category,
  MIN(order_time) AS streak_start,
  MAX(order_time) AS streak_end,
  COUNT(*) AS consecutive_orders
FROM islands
GROUP BY user_id, category, island_key
HAVING COUNT(*) >= 3;
```

Interview line:

```text
Consecutive same-value runs can be detected with rn_all minus rn_value.
```


## 37. Case 27: Consecutive Login Failures Before Success

Business question:

```text
Find login attempts where a user had 3 or more consecutive failures before a success.
```

Table:

```sql
login_attempts(user_id, attempt_time, status)
```

SQL:

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
runs AS (
  SELECT
    *,
    rn_all - rn_status AS run_key
  FROM numbered
),
failure_runs AS (
  SELECT
    user_id,
    run_key,
    MIN(attempt_time) AS failure_start,
    MAX(attempt_time) AS failure_end,
    COUNT(*) AS failure_count
  FROM runs
  WHERE status = 'FAILED'
  GROUP BY user_id, run_key
),
next_success AS (
  SELECT
    f.*,
    MIN(l.attempt_time) AS next_success_time
  FROM failure_runs f
  JOIN login_attempts l
    ON f.user_id = l.user_id
   AND l.status = 'SUCCESS'
   AND l.attempt_time > f.failure_end
  GROUP BY
    f.user_id,
    f.run_key,
    f.failure_start,
    f.failure_end,
    f.failure_count
)
SELECT *
FROM next_success
WHERE failure_count >= 3
ORDER BY user_id, failure_start;
```

Interview line:

```text
Same-status run grouping can identify consecutive failures, then a follow-up join can check what happened next.
```


## 38. Case 28: Missing IDs in an Auto-Increment Table

Business question:

```text
Find missing ID ranges in an orders table.
```

Table:

```sql
orders(order_id)
```

Approach using generated expected IDs:

```sql
WITH expected_ids AS (
  SELECT id
  FROM dim_numbers
  WHERE id BETWEEN (SELECT MIN(order_id) FROM orders)
               AND (SELECT MAX(order_id) FROM orders)
),
actual_ids AS (
  SELECT DISTINCT order_id AS id
  FROM orders
),
missing_ids AS (
  SELECT
    e.id
  FROM expected_ids e
  LEFT JOIN actual_ids a
    ON e.id = a.id
  WHERE a.id IS NULL
),
numbered AS (
  SELECT
    id,
    ROW_NUMBER() OVER (ORDER BY id) AS rn
  FROM missing_ids
),
islands AS (
  SELECT
    id,
    id - rn AS island_key
  FROM numbered
)
SELECT
  MIN(id) AS missing_start_id,
  MAX(id) AS missing_end_id,
  COUNT(*) AS missing_count
FROM islands
GROUP BY island_key
ORDER BY missing_start_id;
```

Caution:

```text
Missing auto-increment IDs can be normal due to rollbacks, deletes, or sequence caching.
```

Interview line:

```text
Missing surrogate IDs are not always data loss; I clarify whether gaps are meaningful.
```


## 39. Case 29: Longest Stockout Per Product

Business question:

```text
Find longest continuous stockout period per product.
```

SQL:

```sql
WITH stockout_days AS (
  SELECT DISTINCT
    product_id,
    snapshot_date
  FROM inventory_snapshot
  WHERE inventory_quantity = 0
),
numbered AS (
  SELECT
    product_id,
    snapshot_date,
    ROW_NUMBER() OVER (
      PARTITION BY product_id
      ORDER BY snapshot_date
    ) AS rn
  FROM stockout_days
),
islands AS (
  SELECT
    product_id,
    snapshot_date,
    snapshot_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
),
stockout_periods AS (
  SELECT
    product_id,
    MIN(snapshot_date) AS stockout_start,
    MAX(snapshot_date) AS stockout_end,
    COUNT(*) AS stockout_days
  FROM islands
  GROUP BY product_id, island_key
),
ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY product_id
      ORDER BY stockout_days DESC, stockout_end DESC
    ) AS rn
  FROM stockout_periods
)
SELECT *
FROM ranked
WHERE rn = 1
ORDER BY product_id;
```

Interview line:

```text
Longest island problems require two steps: create islands, then rank islands.
```


## 40. Case 30: Longest Inactivity Gap Per User

Business question:

```text
Find the longest gap between activities for each user.
```

SQL:

```sql
WITH user_days AS (
  SELECT DISTINCT
    user_id,
    CAST(event_time AS DATE) AS activity_date
  FROM events
  WHERE user_id IS NOT NULL
),
ordered AS (
  SELECT
    user_id,
    activity_date,
    LAG(activity_date) OVER (
      PARTITION BY user_id
      ORDER BY activity_date
    ) AS previous_activity_date
  FROM user_days
),
gaps AS (
  SELECT
    user_id,
    previous_activity_date,
    activity_date,
    activity_date - previous_activity_date AS gap_days
  FROM ordered
  WHERE previous_activity_date IS NOT NULL
),
ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY gap_days DESC, activity_date DESC
    ) AS rn
  FROM gaps
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Clarification:

```text
If you want missing inactive days between active dates, subtract 1 day from gap length.
```

Interview line:

```text
A gap between active dates includes endpoints unless you explicitly calculate missing inactive days between them.
```


## 41. Case 31: Find Periods With Zero Revenue

Business question:

```text
Find continuous calendar date ranges where daily revenue is zero.
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
    CAST(order_time AS DATE) AS revenue_date,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_status = 'COMPLETED'
    AND order_time >= DATE '2026-01-01'
    AND order_time <  DATE '2026-02-01'
  GROUP BY CAST(order_time AS DATE)
),
zero_revenue_days AS (
  SELECT
    c.calendar_date
  FROM calendar c
  LEFT JOIN daily_revenue d
    ON c.calendar_date = d.revenue_date
  WHERE COALESCE(d.revenue, 0) = 0
),
numbered AS (
  SELECT
    calendar_date,
    ROW_NUMBER() OVER (ORDER BY calendar_date) AS rn
  FROM zero_revenue_days
),
islands AS (
  SELECT
    calendar_date,
    calendar_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  MIN(calendar_date) AS zero_revenue_start,
  MAX(calendar_date) AS zero_revenue_end,
  COUNT(*) AS zero_revenue_days
FROM islands
GROUP BY island_key
ORDER BY zero_revenue_start;
```

Interview line:

```text
Zero-activity periods require expected calendar dates; absent fact rows and zero values must be handled explicitly.
```


## 42. Case 32: Consecutive SLA Breach Days

Business question:

```text
Find support teams with at least 3 consecutive days where SLA rate was below 90%.
```

Table:

```sql
daily_sla(team_id, sla_date, sla_rate)
```

SQL:

```sql
WITH breach_days AS (
  SELECT DISTINCT
    team_id,
    sla_date
  FROM daily_sla
  WHERE sla_rate < 0.90
),
numbered AS (
  SELECT
    team_id,
    sla_date,
    ROW_NUMBER() OVER (
      PARTITION BY team_id
      ORDER BY sla_date
    ) AS rn
  FROM breach_days
),
islands AS (
  SELECT
    team_id,
    sla_date,
    sla_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
),
breach_periods AS (
  SELECT
    team_id,
    MIN(sla_date) AS breach_start,
    MAX(sla_date) AS breach_end,
    COUNT(*) AS breach_days
  FROM islands
  GROUP BY team_id, island_key
)
SELECT *
FROM breach_periods
WHERE breach_days >= 3;
```

Interview line:

```text
Condition-based streaks are built by filtering to condition-true days and grouping consecutive dates.
```


## 43. Case 33: Consecutive Failed Jobs

Business question:

```text
Find pipelines with 2 or more consecutive failed runs.
```

Table:

```sql
pipeline_runs(pipeline_id, run_id, started_at, status)
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
runs AS (
  SELECT
    *,
    rn_all - rn_status AS island_key
  FROM numbered
),
failed_runs AS (
  SELECT
    pipeline_id,
    MIN(started_at) AS failure_streak_start,
    MAX(started_at) AS failure_streak_end,
    COUNT(*) AS consecutive_failures
  FROM runs
  WHERE status = 'FAILED'
  GROUP BY pipeline_id, island_key
)
SELECT *
FROM failed_runs
WHERE consecutive_failures >= 2;
```

Interview line:

```text
Consecutive job failures are same-status islands ordered by run time.
```


## 44. Case 34: Consecutive Late Arrivals

Business question:

```text
Find dates where data arrived late for at least 3 consecutive days.
```

Table:

```sql
partition_audit(partition_date, arrived_at, expected_by)
```

SQL:

```sql
WITH late_days AS (
  SELECT DISTINCT
    partition_date
  FROM partition_audit
  WHERE arrived_at > expected_by
),
numbered AS (
  SELECT
    partition_date,
    ROW_NUMBER() OVER (
      ORDER BY partition_date
    ) AS rn
  FROM late_days
),
islands AS (
  SELECT
    partition_date,
    partition_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  MIN(partition_date) AS late_start,
  MAX(partition_date) AS late_end,
  COUNT(*) AS late_days
FROM islands
GROUP BY island_key
HAVING COUNT(*) >= 3
ORDER BY late_start;
```

Interview line:

```text
Pipeline reliability streaks are also gaps-and-islands problems.
```


## 45. Case 35: Consecutive Negative Balances

Business question:

```text
Find accounts that had negative balance for at least 5 consecutive days.
```

Table:

```sql
account_balance_daily(account_id, balance_date, balance)
```

SQL:

```sql
WITH negative_days AS (
  SELECT DISTINCT
    account_id,
    balance_date
  FROM account_balance_daily
  WHERE balance < 0
),
numbered AS (
  SELECT
    account_id,
    balance_date,
    ROW_NUMBER() OVER (
      PARTITION BY account_id
      ORDER BY balance_date
    ) AS rn
  FROM negative_days
),
islands AS (
  SELECT
    account_id,
    balance_date,
    balance_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  account_id,
  MIN(balance_date) AS negative_start,
  MAX(balance_date) AS negative_end,
  COUNT(*) AS negative_days
FROM islands
GROUP BY account_id, island_key
HAVING COUNT(*) >= 5;
```

Interview line:

```text
Any consecutive condition over daily snapshots can use filter-to-condition plus row_number island pattern.
```


## 46. Case 36: Merge Adjacent Intervals Only

Business question:

```text
Merge intervals only if they overlap or touch exactly.
```

Table:

```sql
intervals(entity_id, start_time, end_time)
```

SQL:

```sql
WITH ordered AS (
  SELECT
    entity_id,
    start_time,
    end_time,
    MAX(end_time) OVER (
      PARTITION BY entity_id
      ORDER BY start_time, end_time
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS previous_max_end
  FROM intervals
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_max_end IS NULL
        OR start_time > previous_max_end
      THEN 1 ELSE 0
    END AS new_island_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_island_flag) OVER (
      PARTITION BY entity_id
      ORDER BY start_time, end_time
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS island_id
  FROM flagged
)
SELECT
  entity_id,
  MIN(start_time) AS merged_start,
  MAX(end_time) AS merged_end
FROM grouped
GROUP BY entity_id, island_id
ORDER BY entity_id, merged_start;
```

To require a gap to merge if gap <= 1 day:

```sql
CASE
  WHEN previous_max_end IS NULL
    OR start_time > previous_max_end + INTERVAL '1 day'
  THEN 1 ELSE 0
END
```

Interview line:

```text
Interval merge rules depend on whether adjacent intervals should be merged and what gap threshold is allowed.
```


## 47. Case 37: Find Gaps After Merging Intervals

Business question:

```text
After merging overlapping subscription periods, find inactive gaps.
```

Assume `merged_periods` output:

```sql
merged_periods(user_id, merged_start, merged_end)
```

SQL:

```sql
WITH ordered AS (
  SELECT
    user_id,
    merged_start,
    merged_end,
    LAG(merged_end) OVER (
      PARTITION BY user_id
      ORDER BY merged_start
    ) AS previous_merged_end
  FROM merged_periods
)
SELECT
  user_id,
  previous_merged_end AS gap_start,
  merged_start AS gap_end
FROM ordered
WHERE previous_merged_end IS NOT NULL
  AND merged_start > previous_merged_end
ORDER BY user_id, gap_start;
```

Interview line:

```text
For interval data, merge overlaps first, then calculate gaps between merged intervals.
```


## 48. Case 38: Campaign Active Islands

Business question:

```text
Given campaign daily spend, find continuous active spend periods.
Active means spend > 0.
```

Table:

```sql
campaign_daily_spend(campaign_id, spend_date, spend)
```

SQL:

```sql
WITH active_days AS (
  SELECT DISTINCT
    campaign_id,
    spend_date
  FROM campaign_daily_spend
  WHERE spend > 0
),
numbered AS (
  SELECT
    campaign_id,
    spend_date,
    ROW_NUMBER() OVER (
      PARTITION BY campaign_id
      ORDER BY spend_date
    ) AS rn
  FROM active_days
),
islands AS (
  SELECT
    campaign_id,
    spend_date,
    spend_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  campaign_id,
  MIN(spend_date) AS active_start,
  MAX(spend_date) AS active_end,
  COUNT(*) AS active_spend_days
FROM islands
GROUP BY campaign_id, island_key
ORDER BY campaign_id, active_start;
```

Interview line:

```text
Marketing campaign active periods can be built from consecutive days where spend is positive.
```


## 49. Case 39: Consecutive Low Inventory Days by Category

Business question:

```text
Find product categories with at least 7 consecutive days where any product in category had low inventory.
```

Tables:

```sql
inventory_snapshot(product_id, snapshot_date, inventory_quantity)
products(product_id, category)
```

SQL:

```sql
WITH category_low_days AS (
  SELECT DISTINCT
    p.category,
    i.snapshot_date
  FROM inventory_snapshot i
  JOIN products p
    ON i.product_id = p.product_id
  WHERE i.inventory_quantity < 10
),
numbered AS (
  SELECT
    category,
    snapshot_date,
    ROW_NUMBER() OVER (
      PARTITION BY category
      ORDER BY snapshot_date
    ) AS rn
  FROM category_low_days
),
islands AS (
  SELECT
    category,
    snapshot_date,
    snapshot_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  category,
  MIN(snapshot_date) AS low_inventory_start,
  MAX(snapshot_date) AS low_inventory_end,
  COUNT(*) AS low_inventory_days
FROM islands
GROUP BY category, island_key
HAVING COUNT(*) >= 7;
```

Interview line:

```text
When grouping at category-day grain, deduplicate product-level rows to category-day first.
```


## 50. Case 40: Detect Broken Event Ordering

Business question:

```text
Find users whose event sequence number has gaps.
```

Table:

```sql
events(user_id, sequence_number, event_time)
```

SQL:

```sql
WITH ordered AS (
  SELECT
    user_id,
    sequence_number,
    LAG(sequence_number) OVER (
      PARTITION BY user_id
      ORDER BY sequence_number
    ) AS previous_sequence_number
  FROM events
)
SELECT
  user_id,
  previous_sequence_number,
  sequence_number,
  sequence_number - previous_sequence_number - 1 AS missing_sequence_count
FROM ordered
WHERE previous_sequence_number IS NOT NULL
  AND sequence_number > previous_sequence_number + 1
ORDER BY user_id, previous_sequence_number;
```

Interview line:

```text
Sequence gaps can be detected directly with LAG without generating every expected number.
```


## 51. Case 41: Consecutive Days Above Threshold

Business question:

```text
Find sensors where temperature exceeded 80 for at least 4 consecutive days.
```

Table:

```sql
sensor_daily(sensor_id, reading_date, max_temperature)
```

SQL:

```sql
WITH hot_days AS (
  SELECT DISTINCT
    sensor_id,
    reading_date
  FROM sensor_daily
  WHERE max_temperature > 80
),
numbered AS (
  SELECT
    sensor_id,
    reading_date,
    ROW_NUMBER() OVER (
      PARTITION BY sensor_id
      ORDER BY reading_date
    ) AS rn
  FROM hot_days
),
islands AS (
  SELECT
    sensor_id,
    reading_date,
    reading_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  sensor_id,
  MIN(reading_date) AS hot_start,
  MAX(reading_date) AS hot_end,
  COUNT(*) AS hot_days
FROM islands
GROUP BY sensor_id, island_key
HAVING COUNT(*) >= 4;
```

Interview line:

```text
Threshold streaks use the same condition-filtered island pattern.
```


## 52. Case 42: Retention Streaks After Signup

Business question:

```text
For each user, find the first activity streak after signup.
```

Tables:

```sql
users(user_id, signup_at)
events(user_id, event_time)
```

SQL:

```sql
WITH user_days AS (
  SELECT DISTINCT
    e.user_id,
    CAST(e.event_time AS DATE) AS active_date
  FROM events e
  JOIN users u
    ON e.user_id = u.user_id
  WHERE e.event_time >= u.signup_at
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
),
ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY streak_start
    ) AS rn
  FROM streaks
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Interview line:

```text
Streak logic can be restricted to post-signup activity by filtering before island construction.
```


## 53. Case 43: First Gap After Signup

Business question:

```text
Find first inactivity gap of more than 7 days after signup activity starts.
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
ordered AS (
  SELECT
    user_id,
    active_date,
    LAG(active_date) OVER (
      PARTITION BY user_id
      ORDER BY active_date
    ) AS previous_active_date
  FROM user_days
),
gaps AS (
  SELECT
    user_id,
    previous_active_date,
    active_date,
    active_date - previous_active_date AS gap_days
  FROM ordered
  WHERE previous_active_date IS NOT NULL
    AND active_date > previous_active_date + INTERVAL '7 days'
),
ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY previous_active_date
    ) AS rn
  FROM gaps
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Interview line:

```text
First gap problems are LAG gap detection followed by ROW_NUMBER over gaps.
```


## 54. Case 44: Product Price Stable Periods

Business question:

```text
Find continuous periods where product price stayed the same.
```

Table:

```sql
product_price_daily(product_id, price_date, price)
```

SQL:

```sql
WITH ordered AS (
  SELECT
    product_id,
    price_date,
    price,
    LAG(price) OVER (
      PARTITION BY product_id
      ORDER BY price_date
    ) AS previous_price
  FROM product_price_daily
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_price IS NULL OR price <> previous_price
      THEN 1 ELSE 0
    END AS new_price_run_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_price_run_flag) OVER (
      PARTITION BY product_id
      ORDER BY price_date
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS price_run_id
  FROM flagged
)
SELECT
  product_id,
  price,
  MIN(price_date) AS stable_start,
  MAX(price_date) AS stable_end,
  COUNT(*) AS days_at_price
FROM grouped
GROUP BY product_id, price_run_id, price
ORDER BY product_id, stable_start;
```

Interview line:

```text
Stable-value periods are built by flagging value changes and grouping between changes.
```


## 55. Case 45: Merge User Sessions From Existing Session Intervals

Business question:

```text
Merge overlapping user sessions from multiple devices/sources.
```

Table:

```sql
session_intervals(user_id, session_start, session_end)
```

SQL:

```sql
WITH ordered AS (
  SELECT
    user_id,
    session_start,
    session_end,
    MAX(session_end) OVER (
      PARTITION BY user_id
      ORDER BY session_start, session_end
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS previous_max_end
  FROM session_intervals
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_max_end IS NULL
        OR session_start > previous_max_end
      THEN 1 ELSE 0
    END AS new_session_group_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_session_group_flag) OVER (
      PARTITION BY user_id
      ORDER BY session_start, session_end
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS merged_session_id
  FROM flagged
)
SELECT
  user_id,
  MIN(session_start) AS merged_session_start,
  MAX(session_end) AS merged_session_end
FROM grouped
GROUP BY user_id, merged_session_id;
```

Interview line:

```text
Overlapping session intervals should be merged using running max end, not simple LAG only.
```


## 56. Pattern: Consecutive Dates with ROW_NUMBER

Template:

```sql
WITH entity_days AS (
  SELECT DISTINCT
    entity_id,
    activity_date
  FROM source_table
),
numbered AS (
  SELECT
    entity_id,
    activity_date,
    ROW_NUMBER() OVER (
      PARTITION BY entity_id
      ORDER BY activity_date
    ) AS rn
  FROM entity_days
),
islands AS (
  SELECT
    entity_id,
    activity_date,
    activity_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  entity_id,
  MIN(activity_date) AS island_start,
  MAX(activity_date) AS island_end,
  COUNT(*) AS island_length
FROM islands
GROUP BY entity_id, island_key;
```

Use for:

```text
login streaks
active days
stockout periods
SLA breach days
negative balance days
zero revenue days
missing date ranges
```

Interview line:

```text
This template works after data is normalized to one row per entity per date.
```


## 57. Pattern: Consecutive Numbers with ROW_NUMBER

Template:

```sql
WITH values_deduped AS (
  SELECT DISTINCT
    entity_id,
    sequence_value
  FROM source_table
),
numbered AS (
  SELECT
    entity_id,
    sequence_value,
    ROW_NUMBER() OVER (
      PARTITION BY entity_id
      ORDER BY sequence_value
    ) AS rn
  FROM values_deduped
),
islands AS (
  SELECT
    entity_id,
    sequence_value,
    sequence_value - rn AS island_key
  FROM numbered
)
SELECT
  entity_id,
  MIN(sequence_value) AS sequence_start,
  MAX(sequence_value) AS sequence_end,
  COUNT(*) AS sequence_count
FROM islands
GROUP BY entity_id, island_key;
```

Use for:

```text
consecutive IDs
sequence numbers
invoice number ranges
batch numbers
page numbers
```

Interview line:

```text
For numeric sequences, value - row_number creates the island key.
```


## 58. Pattern: Custom Gap Threshold with LAG

Template:

```sql
WITH ordered AS (
  SELECT
    entity_id,
    event_time,
    LAG(event_time) OVER (
      PARTITION BY entity_id
      ORDER BY event_time
    ) AS previous_event_time
  FROM source_table
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_event_time IS NULL
        OR event_time > previous_event_time + INTERVAL '30 minutes'
      THEN 1 ELSE 0
    END AS new_island_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_island_flag) OVER (
      PARTITION BY entity_id
      ORDER BY event_time
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS island_id
  FROM flagged
)
SELECT
  entity_id,
  island_id,
  MIN(event_time) AS island_start,
  MAX(event_time) AS island_end,
  COUNT(*) AS row_count
FROM grouped
GROUP BY entity_id, island_id;
```

Use for:

```text
sessions
sensor outages
custom inactivity thresholds
API request bursts
event clusters
```

Interview line:

```text
When the allowed gap is not exactly one date/number step, LAG plus break flag is more flexible.
```


## 59. Pattern: Same-Status Islands

Template:

```sql
WITH numbered AS (
  SELECT
    entity_id,
    event_time,
    status,
    ROW_NUMBER() OVER (
      PARTITION BY entity_id
      ORDER BY event_time
    ) AS rn_all,
    ROW_NUMBER() OVER (
      PARTITION BY entity_id, status
      ORDER BY event_time
    ) AS rn_status
  FROM source_table
),
islands AS (
  SELECT
    *,
    rn_all - rn_status AS island_key
  FROM numbered
)
SELECT
  entity_id,
  status,
  MIN(event_time) AS status_start,
  MAX(event_time) AS status_end,
  COUNT(*) AS status_events
FROM islands
GROUP BY entity_id, status, island_key;
```

Use for:

```text
consecutive failures
status runs
same category purchase runs
pipeline failed-run streaks
same state records
```

Interview line:

```text
For consecutive same-value runs, subtract row_number over value from row_number over all rows.
```


## 60. Pattern: Missing Expected Values

Template:

```sql
WITH expected AS (
  SELECT expected_value
  FROM expected_values_table
),
actual AS (
  SELECT DISTINCT actual_value
  FROM actual_values_table
),
missing AS (
  SELECT
    e.expected_value
  FROM expected e
  LEFT JOIN actual a
    ON e.expected_value = a.actual_value
  WHERE a.actual_value IS NULL
)
SELECT *
FROM missing;
```

Use for:

```text
missing dates
missing partitions
missing sequence numbers
missing required event stages
missing product snapshots
```

Interview line:

```text
To find gaps, compare actual values to expected values; actual data alone cannot always reveal what should exist.
```


## 61. Pattern: Merge Overlapping Intervals

Template:

```sql
WITH ordered AS (
  SELECT
    entity_id,
    start_time,
    end_time,
    MAX(end_time) OVER (
      PARTITION BY entity_id
      ORDER BY start_time, end_time
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS previous_max_end
  FROM intervals
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_max_end IS NULL
        OR start_time > previous_max_end
      THEN 1 ELSE 0
    END AS new_island_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_island_flag) OVER (
      PARTITION BY entity_id
      ORDER BY start_time, end_time
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS island_id
  FROM flagged
)
SELECT
  entity_id,
  MIN(start_time) AS merged_start,
  MAX(end_time) AS merged_end
FROM grouped
GROUP BY entity_id, island_id;
```

Use for:

```text
subscription intervals
sessions
campaign periods
SCD ranges
availability periods
```

Interview line:

```text
Overlapping interval problems need running maximum end because overlaps can chain through multiple rows.
```


## 62. Pattern: Find Gaps Between Intervals

Template:

```sql
WITH ordered AS (
  SELECT
    entity_id,
    start_time,
    end_time,
    LAG(end_time) OVER (
      PARTITION BY entity_id
      ORDER BY start_time
    ) AS previous_end_time
  FROM merged_intervals
)
SELECT
  entity_id,
  previous_end_time AS gap_start,
  start_time AS gap_end
FROM ordered
WHERE previous_end_time IS NOT NULL
  AND start_time > previous_end_time;
```

Important:

```text
Merge intervals first if original intervals can overlap.
```

Interview line:

```text
For interval gaps, merge overlaps first, then use LAG on merged intervals.
```


## 63. Pattern: Detect Overlaps

Template using running max:

```sql
WITH ordered AS (
  SELECT
    entity_id,
    start_time,
    end_time,
    MAX(end_time) OVER (
      PARTITION BY entity_id
      ORDER BY start_time, end_time
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS previous_max_end
  FROM intervals
)
SELECT *
FROM ordered
WHERE previous_max_end IS NOT NULL
  AND start_time < previous_max_end;
```

Use for:

```text
SCD effective interval validation
subscription data validation
campaign overlap checks
resource booking conflicts
```

Interview line:

```text
Overlap detection checks whether a row starts before the maximum end of earlier intervals.
```


## 64. Pattern: Business Calendar Streaks

Use when weekends/holidays should not break streaks.

Template:

```sql
WITH business_days AS (
  SELECT
    calendar_date,
    ROW_NUMBER() OVER (
      ORDER BY calendar_date
    ) AS business_day_num
  FROM dim_calendar
  WHERE is_business_day = true
),
entity_business_days AS (
  SELECT DISTINCT
    e.entity_id,
    b.calendar_date,
    b.business_day_num
  FROM events e
  JOIN business_days b
    ON CAST(e.event_time AS DATE) = b.calendar_date
),
numbered AS (
  SELECT
    entity_id,
    calendar_date,
    business_day_num,
    ROW_NUMBER() OVER (
      PARTITION BY entity_id
      ORDER BY business_day_num
    ) AS rn
  FROM entity_business_days
),
islands AS (
  SELECT
    entity_id,
    calendar_date,
    business_day_num - rn AS island_key
  FROM numbered
)
SELECT
  entity_id,
  MIN(calendar_date) AS streak_start,
  MAX(calendar_date) AS streak_end,
  COUNT(*) AS business_days_in_streak
FROM islands
GROUP BY entity_id, island_key;
```

Interview line:

```text
Business-day streaks require a business calendar sequence, not raw date - row_number.
```


## 65. Pattern Selection Guide

Use this decision table.

| Problem Type | Best Pattern |
|---|---|
| consecutive dates | date - ROW_NUMBER |
| consecutive numbers | number - ROW_NUMBER |
| longest streak | build islands then rank |
| missing dates | calendar anti-join |
| missing date ranges | calendar anti-join then islands |
| time gap threshold | LAG + break flag |
| sessionization | LAG + cumulative SUM |
| same status runs | rn_all - rn_status or LAG status change |
| overlapping intervals | running max end + cumulative SUM |
| interval gaps | merge intervals then LAG |
| SCD overlap detection | running max previous end |
| business-day streaks | business calendar sequence |
| trend streaks | LAG metric + cumulative SUM |
| duplicate daily events | dedupe first |

Interview line:

```text
Pattern selection depends on whether the sequence is simple consecutive values, custom gaps, same-status runs, or intervals.
```


## 66. Validation Checklist

Validate gaps-and-islands output.

```text
1. Is input deduplicated to the correct grain?
2. Does each entity-date appear once?
3. Are dates/timestamps normalized correctly?
4. Is timezone handled?
5. Is the correct entity partition used?
6. Does the break rule match business definition?
7. Are islands non-overlapping?
8. Are island start <= island end?
9. Does island length match date count?
10. Are missing calendar dates included when expected?
11. Are weekends/holidays handled correctly if relevant?
12. Are open-ended intervals handled?
13. Are overlapping intervals merged before gap detection?
14. Are output rows unique by entity + island?
15. Are edge cases tested?
```

SQL duplicate input validation:

```sql
SELECT
  user_id,
  active_date,
  COUNT(*) AS row_count
FROM user_days
GROUP BY user_id, active_date
HAVING COUNT(*) > 1;
```

SQL output overlap validation concept:

```text
For each entity, check island_start <= previous island_end.
Should not happen after correct grouping.
```

Interview line:

```text
For streak problems, I validate the input grain first because duplicate dates can break row-number logic.
```


## 67. Edge Cases

Common edge cases:

```text
multiple events on same date
NULL entity_id
NULL date/time
timestamp vs date mismatch
timezone boundary changes activity date
missing calendar table
weekends and holidays
same timestamp ties
duplicate sequence values
out-of-order events
late-arriving events
open-ended intervals
overlapping intervals
adjacent intervals
inclusive vs exclusive end dates
single-row islands
first row has no previous row
last interval has no next row
months have variable lengths
DST/timezone changes
business days vs calendar days
valid repeated facts mistaken as duplicates
```

Interview line:

```text
Gaps-and-islands problems are easy to get wrong when date grain, duplicates, or interval boundaries are unclear.
```


## 68. Common Mistakes

Common mistakes:

```text
not deduplicating user-day before streak logic
not partitioning by entity
using event timestamp instead of date for daily streak
using raw date arithmetic when business days are required
using LAG when running max is needed for interval merging
detecting interval gaps before merging overlaps
treating same-day multiple events as multiple active days
forgetting tie-breaker in ORDER BY
not handling NULL dates
assuming weekends should break or not break without asking
using inclusive/exclusive interval logic incorrectly
not using calendar table for missing dates
summing streak lengths incorrectly
using GROUP BY user_id only and losing streak boundaries
assuming missing sequence IDs always mean data loss
```

Strict feedback:

```text
This is not interview-ready. You used ROW_NUMBER directly on events, so multiple events on the same day will break the consecutive-day streak calculation.
```


## 69. Performance Principles

Performance tips:

```text
filter date ranges early
select only needed columns
deduplicate to entity-date before windowing
partition windows by entity
avoid generating huge expected calendars without filters
use calendar/date dimension instead of recursive CTE for large ranges
pre-aggregate daily states when possible
cluster/partition by entity/date where available
avoid wide SELECT * in window CTEs
watch memory for large window partitions
validate with sampled outputs for huge data
```

Expensive patterns:

```text
large self-joins for interval overlap
recursive CTE over huge date ranges
window functions over unfiltered raw events
COUNT DISTINCT before filtering
cross join entity x calendar without constraints
```

Interview line:

```text
For large data, I reduce to the correct grain first and only then apply window functions.
```


## 70. SQL Dialect Translation Cheatsheet

### PostgreSQL-style daily island key

```sql
active_date - rn * INTERVAL '1 day'
```

### SQL Server-style daily island key

```sql
DATEADD(day, -rn, active_date)
```

### BigQuery-style daily island key

```sql
DATE_SUB(active_date, INTERVAL rn DAY)
```

### Snowflake-style daily island key

```sql
DATEADD(day, -rn, active_date)
```

### PostgreSQL 30-minute threshold

```sql
event_time > previous_event_time + INTERVAL '30 minutes'
```

### SQL Server 30-minute threshold

```sql
event_time > DATEADD(minute, 30, previous_event_time)
```

### BigQuery 30-minute threshold

```sql
event_time > TIMESTAMP_ADD(previous_event_time, INTERVAL 30 MINUTE)
```

Interview line:

```text
The logic is portable, but date arithmetic syntax changes by SQL dialect.
```


## 71. Practice Problem 1: Active Users for 5 Consecutive Days

Problem:

```text
Find users active for at least 5 consecutive calendar days.
```

Solution:

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
)
SELECT
  user_id,
  MIN(active_date) AS streak_start,
  MAX(active_date) AS streak_end,
  COUNT(*) AS streak_days
FROM islands
GROUP BY user_id, island_key
HAVING COUNT(*) >= 5;
```

Expected explanation:

```text
Deduplicate user-day first.
Use date - row_number island key.
Filter islands with length >= 5.
```


## 72. Practice Problem 2: Longest Consecutive Order Days

Problem:

```text
Find each customer's longest streak of days with completed orders.
```

Solution:

```sql
WITH order_days AS (
  SELECT DISTINCT
    user_id,
    CAST(order_time AS DATE) AS order_date
  FROM orders
  WHERE order_status = 'COMPLETED'
    AND user_id IS NOT NULL
),
numbered AS (
  SELECT
    user_id,
    order_date,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY order_date
    ) AS rn
  FROM order_days
),
islands AS (
  SELECT
    user_id,
    order_date,
    order_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
),
streaks AS (
  SELECT
    user_id,
    MIN(order_date) AS streak_start,
    MAX(order_date) AS streak_end,
    COUNT(*) AS streak_days
  FROM islands
  GROUP BY user_id, island_key
),
ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY streak_days DESC, streak_end DESC
    ) AS rn
  FROM streaks
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Expected explanation:

```text
Build streaks first, then rank streaks per user.
```


## 73. Practice Problem 3: Missing Sales Dates by Store

Problem:

```text
For each store, find dates where sales data is missing.
```

Tables:

```sql
dim_calendar(calendar_date)
stores(store_id)
sales(store_id, sales_date)
```

Solution:

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
  WHERE sales_date >= DATE '2026-01-01'
    AND sales_date <  DATE '2026-02-01'
)
SELECT
  e.store_id,
  e.calendar_date AS missing_sales_date
FROM expected_store_dates e
LEFT JOIN actual_store_dates a
  ON e.store_id = a.store_id
 AND e.calendar_date = a.sales_date
WHERE a.sales_date IS NULL
ORDER BY e.store_id, e.calendar_date;
```

Expected explanation:

```text
Expected set is store x calendar date.
Actual set is distinct store/date.
Missing set is anti-join.
```


## 74. Practice Problem 4: Group Missing Sales Dates

Problem:

```text
For each store, group missing sales dates into ranges.
```

Solution:

```sql
WITH missing_store_dates AS (
  -- use output from previous problem
  SELECT
    e.store_id,
    e.calendar_date AS missing_date
  FROM expected_store_dates e
  LEFT JOIN actual_store_dates a
    ON e.store_id = a.store_id
   AND e.calendar_date = a.sales_date
  WHERE a.sales_date IS NULL
),
numbered AS (
  SELECT
    store_id,
    missing_date,
    ROW_NUMBER() OVER (
      PARTITION BY store_id
      ORDER BY missing_date
    ) AS rn
  FROM missing_store_dates
),
islands AS (
  SELECT
    store_id,
    missing_date,
    missing_date - rn * INTERVAL '1 day' AS island_key
  FROM numbered
)
SELECT
  store_id,
  MIN(missing_date) AS missing_start,
  MAX(missing_date) AS missing_end,
  COUNT(*) AS missing_days
FROM islands
GROUP BY store_id, island_key
ORDER BY store_id, missing_start;
```

Expected explanation:

```text
After missing dates are identified, group consecutive missing dates with date - row_number.
```


## 75. Practice Problem 5: Sessionize Page Views

Problem:

```text
Create sessions from page views where a new session starts after 30 minutes of inactivity.
```

Solution:

```sql
WITH ordered AS (
  SELECT
    user_id,
    event_id,
    event_time,
    LAG(event_time) OVER (
      PARTITION BY user_id
      ORDER BY event_time, event_id
    ) AS previous_event_time
  FROM page_views
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_event_time IS NULL
        OR event_time > previous_event_time + INTERVAL '30 minutes'
      THEN 1 ELSE 0
    END AS new_session_flag
  FROM ordered
),
sessionized AS (
  SELECT
    *,
    SUM(new_session_flag) OVER (
      PARTITION BY user_id
      ORDER BY event_time, event_id
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS session_num
  FROM flagged
)
SELECT
  user_id,
  session_num,
  MIN(event_time) AS session_start,
  MAX(event_time) AS session_end,
  COUNT(*) AS page_views
FROM sessionized
GROUP BY user_id, session_num;
```

Expected explanation:

```text
LAG detects gaps.
Cumulative SUM creates session groups.
```


## 76. Practice Problem 6: Consecutive Failed Pipeline Runs

Problem:

```text
Find pipelines with at least 3 consecutive failed runs.
```

Solution:

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
  COUNT(*) AS failed_runs
FROM islands
WHERE status = 'FAILED'
GROUP BY pipeline_id, island_key
HAVING COUNT(*) >= 3;
```

Expected explanation:

```text
Consecutive same-status run pattern.
```


## 77. Practice Problem 7: Merge Overlapping Bookings

Problem:

```text
Merge overlapping room bookings by room_id.
```

Solution:

```sql
WITH ordered AS (
  SELECT
    room_id,
    booking_start,
    booking_end,
    MAX(booking_end) OVER (
      PARTITION BY room_id
      ORDER BY booking_start, booking_end
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS previous_max_end
  FROM bookings
),
flagged AS (
  SELECT
    *,
    CASE
      WHEN previous_max_end IS NULL
        OR booking_start > previous_max_end
      THEN 1 ELSE 0
    END AS new_island_flag
  FROM ordered
),
grouped AS (
  SELECT
    *,
    SUM(new_island_flag) OVER (
      PARTITION BY room_id
      ORDER BY booking_start, booking_end
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS island_id
  FROM flagged
)
SELECT
  room_id,
  MIN(booking_start) AS merged_start,
  MAX(booking_end) AS merged_end
FROM grouped
GROUP BY room_id, island_id
ORDER BY room_id, merged_start;
```

Expected explanation:

```text
Running max previous end handles chained overlaps.
```


## 78. Practice Problem 8: Detect Booking Conflicts

Problem:

```text
Find bookings that overlap previous booking for the same room.
```

Solution:

```sql
WITH ordered AS (
  SELECT
    room_id,
    booking_id,
    booking_start,
    booking_end,
    MAX(booking_end) OVER (
      PARTITION BY room_id
      ORDER BY booking_start, booking_end
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    ) AS previous_max_end
  FROM bookings
)
SELECT
  room_id,
  booking_id,
  booking_start,
  booking_end,
  previous_max_end
FROM ordered
WHERE previous_max_end IS NOT NULL
  AND booking_start < previous_max_end
ORDER BY room_id, booking_start;
```

Expected explanation:

```text
A booking overlaps if it starts before the max end time of earlier bookings.
```


## 79. Practice Problem 9: Missing Sequence Ranges Per Device

Problem:

```text
Find missing sequence number ranges per device.
```

Solution using LAG:

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

Expected explanation:

```text
When actual sequence numbers exist, LAG can directly report gaps without generating all missing numbers.
```


## 80. Practice Problem 10: Consecutive Workday Attendance

Problem:

```text
Find employees present for at least 10 consecutive workdays.
```

Solution:

```sql
WITH workdays AS (
  SELECT
    calendar_date,
    ROW_NUMBER() OVER (
      ORDER BY calendar_date
    ) AS workday_num
  FROM dim_calendar
  WHERE is_workday = true
),
present_days AS (
  SELECT DISTINCT
    a.employee_id,
    a.attendance_date,
    w.workday_num
  FROM attendance a
  JOIN workdays w
    ON a.attendance_date = w.calendar_date
  WHERE a.status = 'PRESENT'
),
numbered AS (
  SELECT
    employee_id,
    attendance_date,
    workday_num,
    ROW_NUMBER() OVER (
      PARTITION BY employee_id
      ORDER BY workday_num
    ) AS rn
  FROM present_days
),
islands AS (
  SELECT
    employee_id,
    attendance_date,
    workday_num - rn AS island_key
  FROM numbered
)
SELECT
  employee_id,
  MIN(attendance_date) AS present_start,
  MAX(attendance_date) AS present_end,
  COUNT(*) AS consecutive_workdays
FROM islands
GROUP BY employee_id, island_key
HAVING COUNT(*) >= 10;
```

Expected explanation:

```text
Use business-day sequence numbers when weekends should not break streaks.
```


## 81. Pattern Classification Drill

Classify each prompt.

```text
1. User active for 3 consecutive days.
2. Longest login streak per user.
3. Missing dates in daily table.
4. Missing date ranges.
5. Missing sequence numbers.
6. Events split into sessions by 30-minute gap.
7. Consecutive failed payments.
8. Device status runs.
9. Merge overlapping subscription intervals.
10. Find SCD interval overlaps.
11. Find gaps between subscriptions.
12. Consecutive business days absent.
13. Weekly active streaks.
14. Monthly order streaks.
15. Product stockout periods.
16. Longest inactivity gap.
17. Consecutive revenue drops.
18. Missing IDs in numeric sequence.
19. Same category consecutive orders.
20. Pipeline consecutive failures.
```

Expected classification:

```text
1. date - ROW_NUMBER island
2. islands then rank
3. calendar anti-join
4. calendar anti-join then date island
5. LAG or expected sequence anti-join
6. LAG + cumulative SUM
7. rn_all - rn_status
8. LAG status change + cumulative SUM
9. running max interval merge
10. running max previous end overlap detection
11. merge intervals then LAG gaps
12. business calendar sequence island
13. week-truncated date island
14. month-truncated date island
15. condition-filtered date island
16. LAG dates then rank gaps
17. LAG metric condition + islands
18. numeric value - ROW_NUMBER or LAG
19. rn_all - rn_category
20. same-status island
```

Passing standard:

```text
18/20 correct before timed gaps-and-islands mocks.
```


## 82. High-ROI Topics

Practice these first.

| Topic | Candidate Must Explain |
|---|---|
| row_number island key | date/value minus row_number |
| LAG gap detection | compare current to previous |
| cumulative sum grouping | turn break flags into island IDs |
| dedupe before streak | one row per entity/date |
| calendar table | expected dates and business days |
| missing date ranges | anti-join then islands |
| longest streak | islands then rank |
| status runs | same-value islands |
| sessionization | custom time gap threshold |
| interval merge | running max previous end |
| interval gaps | merge then LAG |
| SCD overlap | start < previous max end |
| business-day streak | workday sequence numbers |
| dialect syntax | date arithmetic differences |
| validation | input grain and non-overlap checks |


## 83. 7-Day Gaps and Islands Plan

### Day 1: Basic islands

Problems:

```text
consecutive active days
longest login streak
stockout periods
zero revenue days
SLA breach days
```

Focus:

```text
date - row_number
dedupe entity-date
island aggregation
```

### Day 2: Missing values and gaps

Problems:

```text
missing dates
missing date ranges
missing sequence numbers
missing IDs
missing business days
```

Focus:

```text
calendar/expected values
anti-join
numeric islands
```

### Day 3: LAG gap problems

Problems:

```text
event gaps
inactivity gaps
sensor outages
longest gap
first gap after signup
```

Focus:

```text
LAG
threshold comparison
ranking gaps
```

### Day 4: Sessionization and status runs

Problems:

```text
page view sessions
pipeline failure streaks
payment failure streaks
status runs
same category order streaks
```

Focus:

```text
break flags
cumulative SUM
rn_all - rn_status
```

### Day 5: Intervals

Problems:

```text
merge overlapping intervals
detect overlaps
find gaps between intervals
subscription periods
SCD interval validation
```

Focus:

```text
running max end
interval boundaries
open-ended intervals
```

### Day 6: Business calendar and advanced streaks

Problems:

```text
workday attendance
business-day missing orders
weekly active streaks
monthly order streaks
trend streaks
```

Focus:

```text
calendar sequence
week/month normalization
trend condition runs
```

### Day 7: Mock and repair

Tasks:

```text
Run gaps-and-islands mock.
Review mistakes.
Repair weakest topic.
Update progress.
```


## 84. 30-Day Gaps and Islands Plan

### Week 1: Consecutive values

Focus:

```text
daily streaks
numeric streaks
longest streaks
missing dates
missing sequences
```

Exit:

```text
Candidate can solve date/number islands with ROW_NUMBER.
```

### Week 2: Custom gaps and status runs

Focus:

```text
LAG
break flags
cumulative SUM
sessionization
status runs
failure streaks
```

Exit:

```text
Candidate can solve custom threshold and same-status island problems.
```

### Week 3: Interval logic

Focus:

```text
overlap detection
interval merging
interval gaps
SCD validation
subscription active periods
```

Exit:

```text
Candidate can handle interval-based gaps and islands.
```

### Week 4: Data Engineering production cases

Focus:

```text
missing partitions
business calendars
pipeline audit streaks
sensor gaps
data freshness gaps
performance
mock interviews
```

Exit:

```text
Average mock score >= 4/5.
```


## 85. Mock Set 1: Basic Islands

Problems:

```text
1. Users active for 3 consecutive days.
2. Longest login streak per user.
3. Product stockout periods.
4. Consecutive SLA breach days.
5. Consecutive order months.
```

Expected skills:

```text
dedupe entity-date
ROW_NUMBER
date - row_number
island aggregation
rank islands
```

Passing standard:

```text
Average score >= 4/5.
Candidate deduplicates to correct grain before windowing.
```


## 86. Mock Set 2: Gaps and Missing Values

Problems:

```text
1. Missing daily partitions.
2. Group missing dates into ranges.
3. Missing sequence numbers.
4. Missing business days.
5. Longest inactivity gap.
```

Expected skills:

```text
calendar anti-join
numeric LAG
business calendar sequence
gap ranking
```

Passing standard:

```text
Average score >= 4/5.
Candidate distinguishes actual data from expected data.
```


## 87. Mock Set 3: Sessionization and Status Runs

Problems:

```text
1. Sessionize events by 30-minute gap.
2. Consecutive failed payments.
3. Device status runs.
4. Consecutive failed pipeline runs.
5. Same category consecutive purchases.
```

Expected skills:

```text
LAG
break flag
cumulative SUM
rn_all - rn_status
same-value islands
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains break flag logic clearly.
```


## 88. Mock Set 4: Interval Problems

Problems:

```text
1. Merge overlapping subscription intervals.
2. Find gaps between merged intervals.
3. Detect SCD overlaps.
4. Find SCD gaps.
5. Merge overlapping sessions.
```

Expected skills:

```text
running max previous end
interval boundary clarity
open-ended intervals
LAG interval gaps
SCD validation
```

Passing standard:

```text
Average score >= 4/5.
Candidate uses running max for interval merging, not simple LAG only.
```


## 89. Timed Drill Protocol

Use this timing protocol.

### Simple streak problem

```text
10-20 minutes
```

### Missing dates / sessionization problem

```text
25-35 minutes
```

### Interval merge / SCD problem

```text
35-45 minutes
```

Per drill:

```text
Minute 0-3:
Clarify entity, grain, order column, and break rule.

Minute 3-6:
Choose pattern.

Minute 6-25:
Write SQL with CTEs.

Minute 25-35:
Validate duplicates, output ranges, and edge cases.

Minute 35-45:
Explain dialect, performance, and production concerns.
```

If candidate starts writing SQL without clarifying break rule:

```text
Stop and force them to define what counts as consecutive or a gap.
```


## 90. Review Checklist

Review gaps-and-islands answers using:

```text
1. Did candidate define entity?
2. Did candidate define grain?
3. Did candidate define ordered column?
4. Did candidate define consecutive/break rule?
5. Did candidate deduplicate input if needed?
6. Did candidate partition window functions correctly?
7. Did candidate order deterministically?
8. Did candidate choose ROW_NUMBER pattern correctly?
9. Did candidate choose LAG pattern correctly?
10. Did candidate use cumulative SUM correctly?
11. Did candidate use calendar/expected values for missing data?
12. Did candidate handle business days if relevant?
13. Did candidate handle timestamp vs date correctly?
14. Did candidate handle interval boundaries?
15. Did candidate use running max for overlapping intervals?
16. Did candidate aggregate islands correctly?
17. Did candidate rank longest streaks correctly?
18. Did candidate validate output?
19. Did candidate explain edge cases?
20. Did candidate explain dialect/performance considerations?
```

Verdict examples:

```text
Wrong grain.
Good pattern but missing dedupe.
Good streak query but no partition by user.
Good LAG query but wrong threshold.
Good interval answer but simple LAG fails chained overlaps.
Interview-ready.
Strong.
```


## 91. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| No entity/grain clarity | Entity-grain drills |
| Same-day duplicates break logic | Deduplicate entity-date drills |
| ROW_NUMBER confusion | date - row_number drills |
| Cannot explain island key | small table manual walkthroughs |
| LAG confusion | previous-row comparison drills |
| Cumulative SUM confusion | break-flag drills |
| Missing calendar problem | expected-vs-actual drills |
| Business day issue | calendar sequence drills |
| Same-status issue | rn_all - rn_status drills |
| Longest streak issue | island ranking drills |
| Interval merge wrong | running max end drills |
| Overlap detection weak | SCD interval drills |
| Inclusive/exclusive confusion | interval boundary drills |
| Dialect syntax issues | translation drills |
| No validation | input/output validation drills |

If weakness repeats:

```text
Use modes/weakness-repair-mode.md.
```


## 92. Communication Scripts

### Entity/grain script

```text
I will solve this at user-day grain, so first I deduplicate to one row per user per active date.
```

### Row-number script

```text
For consecutive dates, date minus row_number stays constant within a streak, so I group by that derived key.
```

### LAG script

```text
I use LAG to compare each event with the previous event and flag where the gap exceeds the allowed threshold.
```

### Cumulative SUM script

```text
After creating a new-island flag, cumulative SUM gives a stable island ID.
```

### Missing date script

```text
To find missing dates, I need an expected calendar and an anti-join against actual dates.
```

### Business-day script

```text
If weekends should not break the streak, I use a business calendar sequence instead of raw date arithmetic.
```

### Interval merge script

```text
For overlapping intervals, I compare each start to the running maximum previous end, because simple LAG can miss chained overlaps.
```

### Validation script

```text
I would validate that input has one row per entity/date and that output islands do not overlap for the same entity.
```


## 93. Candidate Self-Review Questions

After every gaps-and-islands problem, candidate should answer:

```text
1. What is the entity?
2. What is the input grain?
3. What is the output grain?
4. What column defines order?
5. What counts as consecutive?
6. What counts as a gap?
7. Are there duplicate dates/events?
8. Should I dedupe before windowing?
9. Is this date, number, status, or interval problem?
10. Should I use ROW_NUMBER or LAG?
11. Do I need cumulative SUM?
12. Do I need a calendar table?
13. Should weekends/holidays count?
14. Are timestamps converted to dates correctly?
15. Are intervals inclusive or exclusive?
16. Are open-ended intervals possible?
17. Are overlapping intervals possible?
18. How do I validate the result?
19. What is the dialect-specific syntax?
20. What performance issue could appear at scale?
```

If candidate cannot answer these:

```text
The gaps-and-islands solution is not interview-ready.
```


## 94. Maintenance Drills

After completing gaps and islands, maintain skill with:

```text
1 daily streak drill per week
1 missing date/sequence drill per week
1 LAG sessionization drill every 2 weeks
1 status-run drill every 2 weeks
1 interval merge/overlap drill every 2 weeks
1 full gaps-and-islands mock every month
```

Maintenance rotation:

```text
Week 1: date streaks and longest streaks
Week 2: missing dates and sequence gaps
Week 3: sessions and status runs
Week 4: intervals, SCD overlaps, business calendars
```

If score drops below 4:

```text
Run modes/weakness-repair-mode.md for failed topic.
```


## 95. Progress Tracking Template

Use this progress format.

```text
# SQL Gaps and Islands Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

Entity/grain clarification:
Deduplicate entity-date:
ROW_NUMBER island key:
Numeric islands:
Missing date detection:
Missing date ranges:
Missing sequence detection:
LAG gap detection:
Sessionization:
Cumulative SUM grouping:
Same-status islands:
Longest streak:
Business calendar streaks:
Weekly streaks:
Monthly streaks:
Condition streaks:
Trend streaks:
Interval gaps:
Interval merging:
SCD overlap detection:
Open-ended intervals:
Inclusive/exclusive boundaries:
Dialect translation:
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


## 96. Final Exit Test

Candidate passes gaps and islands when they can solve/explain:

```text
1. Users active for N consecutive days.
2. Longest login streak per user.
3. Missing daily partitions.
4. Missing date ranges.
5. Missing sequence numbers.
6. Missing sequence ranges.
7. Gaps between events.
8. Sessionization by 30-minute gap.
9. Consecutive failed payments.
10. Status runs.
11. Stockout periods.
12. Subscription active periods.
13. Gaps between subscription periods.
14. Merge overlapping intervals.
15. Detect SCD overlaps.
16. Find SCD interval gaps.
17. Consecutive order months.
18. Consecutive active weeks.
19. Business-day streaks.
20. Consecutive revenue drops.
21. Uptime/downtime windows.
22. Sensor outage gaps.
23. Consecutive absence days.
24. Same category consecutive purchases.
25. Missing IDs.
26. Longest stockout per product.
27. Longest inactivity gap per user.
28. Zero revenue periods.
29. Consecutive SLA breach days.
30. Consecutive failed pipeline runs.
31. Adjacent interval merge with threshold.
32. Gaps after merging intervals.
33. Stable price periods.
34. Business calendar sequence logic.
35. Date arithmetic dialect translation.
```

Passing standard:

```text
Average score >= 4/5.
No missing dedupe step.
No missing partition by entity.
No wrong interval merge pattern.
No undefined break rule.
No missing validation.
Can explain why the chosen pattern works.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles duplicates, business calendars, interval merging, SCD validation, sessionization, sequence gaps, performance, and dialect differences clearly under pressure.
```


## 97. Final Summary

Gaps and islands are core SQL interview problems for Data Engineering roles.

They map directly to:

```text
missing partition checks
data completeness validation
activity streaks
retention patterns
sessionization
status run detection
failure streaks
inventory stockout periods
subscription periods
SCD interval validation
sensor outage detection
pipeline reliability monitoring
business calendar logic
sequence integrity checks
```

The candidate must master:

```text
entity and grain clarification
deduplication before streaks
ROW_NUMBER islands
date - row_number logic
numeric value - row_number logic
LAG gap detection
break flags
cumulative SUM island IDs
same-status runs
calendar anti-joins
business calendar sequences
longest streak ranking
interval merging
overlap detection
gap detection after merge
inclusive/exclusive interval boundaries
dialect date arithmetic
output validation
```

The mentor must be strict:

```text
No entity/grain definition → not interview-ready.
No dedupe before daily streaks → not interview-ready.
No partition by entity → not interview-ready.
Cannot explain date - row_number → not interview-ready.
Uses simple LAG for chained interval merge → not interview-ready.
No calendar for missing dates → not interview-ready.
No validation → not interview-ready.
```

The goal is not to memorize one trick.

The goal is to identify the sequence type, choose the right pattern, write clean SQL, handle edge cases, and explain the result like a Data Engineer.


## 98. Problem Card Appendix

### Card 1: Daily Active Streak

Topic:

```text
date - row_number
```

Core idea:

```text
Group consecutive active dates.
```

Data Engineering connection:

```text
User engagement.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Longest Streak

Topic:

```text
islands then rank
```

Core idea:

```text
Find largest island per entity.
```

Data Engineering connection:

```text
Retention analysis.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Missing Dates

Topic:

```text
calendar anti-join
```

Core idea:

```text
Compare expected to actual dates.
```

Data Engineering connection:

```text
Pipeline completeness.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Missing Date Ranges

Topic:

```text
anti-join then islands
```

Core idea:

```text
Group missing dates into ranges.
```

Data Engineering connection:

```text
Data quality.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Sequence Gaps

Topic:

```text
LAG numbers
```

Core idea:

```text
Find breaks in sequence numbers.
```

Data Engineering connection:

```text
Event integrity.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Sessionization

Topic:

```text
LAG + cumulative SUM
```

Core idea:

```text
Group events by inactivity threshold.
```

Data Engineering connection:

```text
Clickstream analytics.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Same Status Runs

Topic:

```text
rn_all - rn_status
```

Core idea:

```text
Group consecutive equal statuses.
```

Data Engineering connection:

```text
Operational monitoring.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Failure Streak

Topic:

```text
status islands
```

Core idea:

```text
Find consecutive failures.
```

Data Engineering connection:

```text
Reliability.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Stockout Period

Topic:

```text
condition date islands
```

Core idea:

```text
Consecutive zero inventory days.
```

Data Engineering connection:

```text
Inventory analytics.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Business Day Streak

Topic:

```text
calendar sequence
```

Core idea:

```text
Ignore weekends/holidays.
```

Data Engineering connection:

```text
Attendance/SLA.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Monthly Streak

Topic:

```text
month-normalized islands
```

Core idea:

```text
Consecutive active months.
```

Data Engineering connection:

```text
Subscription/product analytics.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Event Gap

Topic:

```text
LAG timestamp
```

Core idea:

```text
Find large time gaps.
```

Data Engineering connection:

```text
Sensor/API monitoring.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Interval Merge

Topic:

```text
running max end
```

Core idea:

```text
Merge overlaps/chained overlaps.
```

Data Engineering connection:

```text
Subscriptions/sessions.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Interval Gap

Topic:

```text
merged intervals + LAG
```

Core idea:

```text
Find inactive gaps.
```

Data Engineering connection:

```text
Subscription analytics.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: SCD Overlap

Topic:

```text
running max previous end
```

Core idea:

```text
Detect invalid dimension intervals.
```

Data Engineering connection:

```text
Warehouse quality.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Zero Revenue Period

Topic:

```text
calendar + condition islands
```

Core idea:

```text
Find no-revenue ranges.
```

Data Engineering connection:

```text
Finance monitoring.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Uptime/Downtime

Topic:

```text
LEAD status boundary
```

Core idea:

```text
Convert status events to periods.
```

Data Engineering connection:

```text
Service monitoring.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Stable Price Period

Topic:

```text
LAG value change
```

Core idea:

```text
Group same price runs.
```

Data Engineering connection:

```text
Catalog analytics.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Pipeline Late Streak

Topic:

```text
condition streak
```

Core idea:

```text
Consecutive late partitions.
```

Data Engineering connection:

```text
Pipeline reliability.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Missing ID Ranges

Topic:

```text
numeric islands
```

Core idea:

```text
Find ID gaps.
```

Data Engineering connection:

```text
Audit checks.
```

Candidate must be able to explain:

```text
1. Entity and grain.
2. Ordered field.
3. Break/consecutive rule.
4. SQL pattern.
5. Edge case.
6. Validation check.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 99. Data Engineering Scenario Appendix

### Scenario 1: DAU Streak

Pattern:

```text
date islands
```

Task:

```text
Find users active for N consecutive days.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: Warehouse Missing Partitions

Pattern:

```text
calendar anti-join
```

Task:

```text
Find missing partitions and group into ranges.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: IoT Sensor Outage

Pattern:

```text
LAG threshold
```

Task:

```text
Find reading gaps above allowed frequency.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: Clickstream Sessions

Pattern:

```text
sessionization
```

Task:

```text
Create sessions from page views.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: Payment Failures

Pattern:

```text
same-status island
```

Task:

```text
Find consecutive failed attempts.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: Inventory Stockout

Pattern:

```text
condition date island
```

Task:

```text
Find stockout periods.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: SCD Corruption

Pattern:

```text
interval overlap
```

Task:

```text
Detect overlapping dimension intervals.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: Subscription Gaps

Pattern:

```text
interval gaps
```

Task:

```text
Find inactive time between subscriptions.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: Business-Day Absence

Pattern:

```text
calendar sequence
```

Task:

```text
Ignore weekends in absence streaks.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: Pipeline Reliability

Pattern:

```text
late/failure streak
```

Task:

```text
Find repeated failed or late pipeline runs.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: Revenue Monitoring

Pattern:

```text
zero-revenue islands
```

Task:

```text
Find no-revenue date ranges.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Device Status Runs

Pattern:

```text
status change flags
```

Task:

```text
Build uptime/downtime periods.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: Order Month Streak

Pattern:

```text
month islands
```

Task:

```text
Find consecutive ordering months.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Sequence Integrity

Pattern:

```text
numeric LAG
```

Task:

```text
Find missing event sequence ranges.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: Booking Conflict

Pattern:

```text
running max
```

Task:

```text
Detect overlapping room bookings.
```

Minimum expected answer:

```text
1. Clarify entity and grain.
2. Clarify break rule.
3. Choose pattern.
4. Write SQL or pseudocode.
5. Explain edge cases.
6. Explain validation.
```

Passing score:

```text
4/5 or higher.
```


## 100. Drill Appendix

### Drill 1: Manual Island Key Drill

Task:

```text
Given dates and row numbers, compute date - rn manually.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Dedup Drill

Task:

```text
Convert raw events to one row per entity/date.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Daily Streak Drill

Task:

```text
Find streaks of consecutive dates.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Longest Streak Drill

Task:

```text
Rank islands by length.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Missing Date Drill

Task:

```text
Use calendar anti-join.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: Missing Range Drill

Task:

```text
Group missing dates into islands.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Sequence Gap Drill

Task:

```text
Use LAG on sequence values.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Session Drill

Task:

```text
Use LAG and cumulative SUM.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Status Run Drill

Task:

```text
Use rn_all - rn_status.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Break Flag Drill

Task:

```text
Create new_island_flag from custom rule.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Business Calendar Drill

Task:

```text
Use workday sequence instead of raw dates.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Monthly Drill

Task:

```text
Normalize to month before streaking.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Trend Drill

Task:

```text
Use LAG metric and group condition runs.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Interval Merge Drill

Task:

```text
Use running max previous end.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Interval Gap Drill

Task:

```text
Merge first, then LAG.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: SCD Drill

Task:

```text
Detect overlaps and gaps.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Open Interval Drill

Task:

```text
Handle NULL end dates.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Dialect Drill

Task:

```text
Translate PostgreSQL syntax to SQL Server/BigQuery.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 19: Validation Drill

Task:

```text
Write duplicate input and output overlap checks.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 20: Performance Drill

Task:

```text
Reduce raw events before windowing.
```

Minimum passing answer:

```text
1. State entity and grain.
2. State ordered field.
3. State break rule.
4. Choose correct pattern.
5. Explain validation.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 101. Quick Reference Cards

### Quick Card 1: Gap

Summary:

```text
Missing or broken part of a sequence.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 2: Island

Summary:

```text
Continuous run of sequence values.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 3: ROW_NUMBER island

Summary:

```text
date/value minus row_number stays constant.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 4: LAG gap

Summary:

```text
Compare current row to previous row.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 5: Break flag

Summary:

```text
1 when a new island starts.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 6: Cumulative SUM

Summary:

```text
Turns break flags into island IDs.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 7: Calendar anti-join

Summary:

```text
Find missing expected dates.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 8: Business calendar

Summary:

```text
Use workday sequence for workday streaks.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 9: Status island

Summary:

```text
Group consecutive same-value runs.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 10: Running max end

Summary:

```text
Correct pattern for merging overlapping intervals.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 11: Interval gap

Summary:

```text
Gap between merged intervals.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 12: SCD overlap

Summary:

```text
Current start before previous max end.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 13: Sessionization

Summary:

```text
Events grouped by inactivity threshold.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```

### Quick Card 14: Dedup first

Summary:

```text
One row per entity/date before daily streaks.
```

Interview check:

```text
Give one SQL pattern and one Data Engineering use case.
```


## 102. Gaps and Islands FAQ

### FAQ 1: Why do we use date - row_number?

Answer:

```text
It creates a constant key for consecutive dates and changes when a gap appears.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 2: Why deduplicate before streak logic?

Answer:

```text
Multiple events on the same day create extra row numbers and break the island key.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 3: When should I use LAG instead of row_number?

Answer:

```text
Use LAG when the break rule is custom, such as 30-minute sessions or changing status.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 4: How do I find missing dates?

Answer:

```text
Compare expected calendar dates to actual dates using an anti-join.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 5: How do I group missing dates into ranges?

Answer:

```text
Find missing dates first, then apply the same row_number island pattern.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 6: How do I merge overlapping intervals?

Answer:

```text
Sort by start and compare each start to the running maximum previous end.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 7: Why not just use LAG end time for interval merge?

Answer:

```text
A long earlier interval can overlap multiple later intervals, so running max is safer.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 8: How do I handle weekends?

Answer:

```text
Use a business calendar with a consecutive business-day number.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 9: How do I handle monthly streaks?

Answer:

```text
Normalize timestamps to month start before applying row_number pattern.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```

### FAQ 10: What should I validate?

Answer:

```text
Input grain, duplicate dates, output ranges, non-overlap, and boundary rules.
```

Candidate should also explain:

```text
1. Example SQL pattern.
2. Edge case.
3. Validation query.
4. Production relevance.
```
