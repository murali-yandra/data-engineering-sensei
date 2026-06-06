# Data Scripting Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/python/data-scripting.md
```

This guide teaches and drills **Python data scripting for Data Engineering interviews**.

This is not a generic Python basics document. It is an interview-focused guide for candidates who need to write practical scripts that read files, validate records, transform data, handle bad input, process large datasets safely, write outputs, create reusable functions, and explain production-grade scripting decisions.

Data scripting is high-ROI for Data Engineering interviews because many rounds include:

- parse a CSV/JSON/log file
- clean records
- validate required fields
- aggregate by key
- deduplicate records
- find latest record per ID
- flatten nested JSON
- group and summarize data
- write a small ETL script
- process large files line by line
- handle malformed rows
- calculate metrics from logs
- convert raw records to clean records
- implement idempotent local processing
- design script structure with functions and tests
- explain memory and performance trade-offs
- handle date/time parsing
- handle command-line arguments
- make scripts safe, debuggable, and reusable

Use this guide with:

- `docs/python-interview-guide.md`
- `docs/data-engineering-fundamentals.md`
- `docs/etl-elt-pipelines-guide.md`
- `docs/error-handling-playbook.md`
- `docs/assessment-rubric.md`
- `docs/communication-rubric.md`
- `modes/python-drill-mode.md`
- `modes/data-engineering-fundamentals-mode.md`
- `modes/project-deep-dive-mode.md`
- `modes/interview-mode.md`
- `modes/review-mode.md`
- `modes/feedback-mode.md`
- `modes/weakness-repair-mode.md`
- `practice/python/api-processing.md`
- `practice/dsa/hashmaps.md`
- `practice/dsa/two-pointers-sliding-window.md`
- `practice/dsa/sorting-binary-search.md`
- `progress/CANDIDATE_PROFILE.md`
- `progress/CURRENT_STATE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Default interview standard if target companies are not provided:

```text
FAANG-style Data Engineering interview standard, scaled by candidate experience.
```


## 1. Purpose

The purpose of this guide is to make the candidate strong at Python data scripting for interviews.

The candidate should learn to answer:

```text
How do I write a clean script that reads data, transforms it, validates it, and writes output?
How do I process files without loading everything into memory?
How do I handle malformed rows?
How do I aggregate records by key?
How do I deduplicate records?
How do I keep latest record per ID?
How do I flatten nested JSON?
How do I parse dates safely?
How do I design reusable functions?
How do I structure a script for testing?
How do I log useful information?
How do I handle errors without hiding data-quality issues?
How do I make scripts idempotent?
How do I explain time and space complexity?
How do I connect scripting to real Data Engineering pipelines?
```

A candidate is interview-ready only when they can:

```text
write readable Python functions
separate input/output from transformation logic
process CSV, JSON, JSONL, and log-like data
validate records and collect invalid rows
aggregate by key using dictionaries/defaultdict/Counter
deduplicate using stable keys
parse and normalize timestamps
handle missing/invalid fields
stream large files line by line
write deterministic output
use pathlib instead of fragile string paths
use context managers for files
add basic logging
write simple tests or testable functions
explain memory trade-offs
connect scripts to ETL/ELT pipeline behavior
```


## 2. Why Data Scripting Matters for Data Engineers

Python data scripting appears in real Data Engineering work almost every day.

Real examples:

```text
Read raw CSV export and convert to clean JSONL.
Parse application logs and count error events.
Find top customers by transaction amount.
Deduplicate event records by event_id.
Keep latest user profile by updated_at.
Validate data before loading into warehouse.
Split valid and invalid rows.
Flatten nested API JSON into tabular rows.
Generate file-level summary metrics.
Compare two extracts.
Create small migration scripts.
Create one-time backfill scripts.
Create reconciliation scripts.
Clean malformed vendor files.
Convert local proof-of-concept logic into pipeline code.
```

Interviewers test scripting because it reveals practical skill:

```text
Can the candidate write production-readable code?
Can they handle dirty data?
Can they avoid memory problems?
Can they explain correctness?
Can they structure transformations cleanly?
Can they handle edge cases?
Can they reason about data quality?
```

Weak scripting answer:

```text
Read everything, assume all fields exist, print result.
```

Strong scripting answer:

```text
Stream input, validate rows, transform safely, collect invalid records with reasons, write outputs atomically, log counts, and make the logic testable.
```


## 3. Core Mental Model

A data script usually follows this flow:

```text
1. Read input.
2. Parse raw records.
3. Validate required fields.
4. Transform records.
5. Aggregate/deduplicate/filter if needed.
6. Write output.
7. Write invalid records separately.
8. Emit summary metrics.
9. Exit with clear success/failure.
```

A strong script separates concerns:

```text
read_csv_rows()
parse_row()
validate_row()
transform_row()
aggregate_rows()
write_jsonl()
main()
```

Do not put everything into one giant loop unless the problem is tiny.

Core interview line:

```text
I separate pure transformation logic from file I/O so the code is easier to test, debug, and reuse in a pipeline.
```


## 4. Python Data Scripting Vocabulary

Important terms:

```text
Record:
One logical data item, often a row or JSON object.

Field:
A value inside a record.

Schema:
Expected set of fields and types.

Validation:
Checking whether a record satisfies required rules.

Transformation:
Converting raw input to clean output.

Aggregation:
Combining records by key to calculate metrics.

Deduplication:
Removing duplicates based on a key or rule.

Idempotency:
Rerunning script does not create incorrect duplicate output.

Checkpoint:
Saved progress for resumable processing.

Dead-letter:
Output for invalid records.

Streaming:
Processing input incrementally instead of loading all data.

Batch:
A group of records processed/written together.

Atomic write:
Write to temp file first, then rename to final path.

Backfill:
Historical data processing.

Reconciliation:
Comparing two datasets for differences.
```


## 5. Standard Answer Framework

Use this framework for data scripting interview answers:

```text
1. Restate input and output.
2. Clarify file format:
   - CSV
   - JSON
   - JSONL
   - text logs
   - nested JSON
3. Clarify data size.
4. Clarify required fields and validation rules.
5. Clarify duplicate handling.
6. Clarify error handling:
   - skip bad rows
   - fail fast
   - dead-letter invalid records
7. Explain approach.
8. Write testable functions.
9. Use safe file handling.
10. Explain edge cases.
11. Explain time complexity.
12. Explain space complexity.
13. Explain production improvements:
   - logging
   - metrics
   - atomic writes
   - idempotency
   - tests
```

Short version:

```text
Input:
Validation:
Transform:
Aggregate/dedupe:
Output:
Error handling:
Complexity:
Production notes:
```

Strict rule:

```text
No data script is interview-ready if it assumes every row is clean unless the interviewer explicitly says so.
```


## 6. Scoring Rubric

Score each data scripting attempt from 0 to 5.

### Score 0

No meaningful script or explanation.

### Score 1

Only reads input and prints output. No validation or structure.

### Score 2

Basic script works for clean data but fails malformed rows or edge cases.

### Score 3

Handles common cases but weak on structure, memory, logging, or invalid data.

### Score 4

Interview-ready. Clean functions, validation, error handling, correct logic, and complexity explanation.

### Score 5

Strong. Production-aware: streaming, atomic writes, idempotency, tests, observability, data-quality handling, and clear trade-offs.

Do not give 4+ if:

```text
candidate loads huge files into memory without discussion
candidate uses bare except
candidate does not use context managers for files
candidate directly indexes optional fields without validation
candidate silently drops bad records
candidate cannot explain dedupe key
candidate cannot explain time/space complexity
candidate writes everything in one untestable block
candidate has no edge-case handling
candidate cannot connect script to DE pipelines
```


## 7. Core Python Tools

Useful Python tools for data scripting:

```text
pathlib.Path:
Safe path handling.

csv:
Read/write CSV files.

json:
Parse/write JSON and JSONL.

datetime:
Parse and normalize timestamps.

collections.Counter:
Counting frequencies.

collections.defaultdict:
Grouping and aggregation.

dataclasses:
Structured records when useful.

typing:
Function signatures and readability.

logging:
Operational logs.

argparse:
Command-line arguments.

tempfile:
Safe temporary files.

itertools:
Efficient iteration utilities.

decimal.Decimal:
Exact decimal money calculations.
```

Interview-safe default:

```text
Use standard library first unless the problem explicitly allows pandas or PySpark.
```

Important:

```text
For interviews, pure Python scripting is often expected because it shows fundamentals.
```


## 8. File Handling Rules

Good file handling:

```python
from pathlib import Path

path = Path("input.csv")

with path.open("r", encoding="utf-8") as file:
    for line in file:
        process(line)
```

Why:

```text
context manager closes file automatically
encoding is explicit
pathlib is cross-platform friendly
line-by-line processing saves memory
```

Avoid:

```python
file = open("input.csv")
data = file.read()
# no close
```

Avoid for large files:

```python
lines = file.readlines()
```

Interview line:

```text
For large files, I stream line by line rather than loading the entire file into memory.
```


## 9. CSV Reading

Use Python's `csv.DictReader` for CSV rows.

```python
import csv
from pathlib import Path

def read_csv_rows(path):
    path = Path(path)

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row
```

Why DictReader:

```text
records are dictionaries keyed by column name
easier validation
less fragile than positional indices
```

Edge cases:

```text
missing header
extra columns
missing values
quoted commas
empty file
duplicate column names
different encoding
```

Interview line:

```text
I prefer DictReader for data scripts because column names make validation and transformation clearer.
```


## 10. CSV Writing

Use `csv.DictWriter`.

```python
import csv
from pathlib import Path

def write_csv_rows(path, rows, fieldnames):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            writer.writerow(row)
```

Important:

```text
Use newline="" with csv module.
Define fieldnames explicitly for deterministic column order.
Create parent directories if needed.
```

Interview line:

```text
I define output fieldnames explicitly so output schema and column order are deterministic.
```


## 11. JSON and JSONL

### JSON

One complete JSON object or array.

```python
import json

with open("data.json", "r", encoding="utf-8") as file:
    payload = json.load(file)
```

### JSONL

One JSON object per line.

```json
{"id": 1, "name": "A"}
{"id": 2, "name": "B"}
```

Read JSONL:

```python
import json
from pathlib import Path

def read_jsonl(path):
    path = Path(path)

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                yield {
                    "_invalid": True,
                    "_line_number": line_number,
                    "_error": str(exc),
                    "_raw": line,
                }
```

JSONL is good for data engineering because:

```text
streamable
append-friendly
works well for raw landing
one bad line does not break entire file if handled carefully
```


## 12. JSONL Writing

Write JSONL:

```python
import json
from pathlib import Path

def write_jsonl(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False))
            file.write("\n")
```

Append JSONL:

```python
def append_jsonl(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False))
            file.write("\n")
```

Interview line:

```text
JSONL is useful for raw and invalid records because it handles one record per line and can be processed incrementally.
```


## 13. Log Parsing Basics

Logs are often semi-structured.

Example log:

```text
2026-01-01T10:00:00Z INFO service=payments event=charge_success amount=100
```

Simple parser:

```python
def parse_key_value_log(line):
    parts = line.strip().split()

    if len(parts) < 3:
        return None

    record = {
        "timestamp": parts[0],
        "level": parts[1],
    }

    for token in parts[2:]:
        if "=" not in token:
            continue

        key, value = token.split("=", 1)
        record[key] = value

    return record
```

Edge cases:

```text
values with spaces
quoted values
missing level
malformed timestamp
different log formats
multi-line logs
```

Interview line:

```text
For real logs, I would prefer structured JSON logs, but if given key-value text logs, I would parse defensively and capture malformed lines.
```


## 14. Validation Strategy

Validation checks whether a row is usable.

Common validations:

```text
required field exists
field is not empty
numeric field can be parsed
timestamp field can be parsed
enum field is allowed
id is stable
amount is non-negative
currency has expected format
record type is known
```

Validation function:

```python
def validate_transaction(row):
    errors = []

    if not row.get("transaction_id"):
        errors.append("missing_transaction_id")

    if row.get("amount") is None:
        errors.append("missing_amount")

    if not row.get("currency"):
        errors.append("missing_currency")

    if not row.get("created_at"):
        errors.append("missing_created_at")

    return errors
```

Interview line:

```text
Validation should return explicit error reasons, not just True or False, so invalid rows can be debugged.
```


## 15. Transform Strategy

Transformation converts raw row into clean shape.

Example:

```python
from decimal import Decimal

def transform_transaction(raw):
    return {
        "transaction_id": raw.get("id"),
        "customer_id": raw.get("customer_id"),
        "amount": Decimal(raw["amount"]) if raw.get("amount") else None,
        "currency": raw.get("currency", "").upper(),
        "created_at": raw.get("created_at"),
    }
```

Good transformation:

```text
explicit output fields
safe missing-field handling
normalizes types
does not silently invent required values
keeps raw invalid records if transform fails
```

Bad transformation:

```python
amount = float(raw["amount"])
```

Why:

```text
float is risky for money
KeyError if amount missing
ValueError if malformed
```

Interview line:

```text
For money, I prefer Decimal over float to avoid precision issues.
```


## 16. Splitting Valid and Invalid Records

Pattern:

```python
def split_valid_invalid(records, transform_fn, validate_fn):
    valid = []
    invalid = []

    for index, raw in enumerate(records):
        try:
            row = transform_fn(raw)
            errors = validate_fn(row)
        except Exception as exc:
            invalid.append({
                "row_number": index + 1,
                "raw": raw,
                "errors": [f"transform_error:{exc}"],
            })
            continue

        if errors:
            invalid.append({
                "row_number": index + 1,
                "raw": raw,
                "row": row,
                "errors": errors,
            })
        else:
            valid.append(row)

    return valid, invalid
```

Important:

```text
This catches transform errors but still records raw input and reason.
```

Do not:

```text
bare except and continue silently
```

Interview line:

```text
I keep invalid records with error reasons so data-quality issues can be fixed and replayed.
```


## 17. Invalid Record Threshold

Sometimes a few invalid rows can be tolerated.

But a high invalid rate indicates source/schema issue.

```python
def enforce_invalid_threshold(valid_count, invalid_count, max_invalid_ratio=0.05):
    total = valid_count + invalid_count

    if total == 0:
        return

    invalid_ratio = invalid_count / total

    if invalid_ratio > max_invalid_ratio:
        raise RuntimeError(
            f"Invalid ratio too high: {invalid_ratio:.2%}; "
            f"valid={valid_count}, invalid={invalid_count}"
        )
```

Interview line:

```text
I can tolerate a small number of bad rows, but if the invalid rate crosses a threshold, I fail the job because it likely means schema drift or upstream breakage.
```


## 18. Date and Timestamp Parsing

Use timezone-aware timestamps when possible.

Basic parsing:

```python
from datetime import datetime, timezone

def parse_iso_timestamp(value):
    if not value:
        return None

    normalized = value.replace("Z", "+00:00")
    return datetime.fromisoformat(normalized)
```

Normalize to UTC:

```python
def to_utc_iso(dt):
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    return dt.astimezone(timezone.utc).isoformat()
```

Caution:

```text
Naive datetime can cause timezone bugs.
String comparison works only if timestamps are consistently formatted.
Date parsing should be explicit.
```

Interview line:

```text
For data pipelines, I normalize timestamps to UTC and use half-open windows where possible.
```


## 19. Numeric Parsing

Numeric fields from files often arrive as strings.

Safe int parsing:

```python
def parse_int(value):
    if value is None or value == "":
        return None

    try:
        return int(value)
    except ValueError:
        return None
```

Safe Decimal parsing:

```python
from decimal import Decimal, InvalidOperation

def parse_decimal(value):
    if value is None or value == "":
        return None

    try:
        return Decimal(str(value))
    except InvalidOperation:
        return None
```

Why Decimal for money:

```text
Decimal avoids binary floating-point precision issues.
```

Interview line:

```text
I parse numeric values explicitly and treat parsing failure as a validation error, not as zero.
```


## 20. Aggregation with defaultdict

Aggregate by key.

Example: total amount by customer.

```python
from collections import defaultdict
from decimal import Decimal

def total_amount_by_customer(transactions):
    totals = defaultdict(Decimal)

    for txn in transactions:
        customer_id = txn.get("customer_id")
        amount = txn.get("amount")

        if customer_id is None or amount is None:
            continue

        totals[customer_id] += Decimal(str(amount))

    return dict(totals)
```

Complexity:

```text
Time: O(n)
Space: O(u), where u is unique customers
```

Interview line:

```text
A dictionary/defaultdict is the natural structure for group-by style aggregation in Python.
```


## 21. Counting with Counter

Use Counter for frequencies.

```python
from collections import Counter

def count_events_by_type(events):
    counts = Counter()

    for event in events:
        event_type = event.get("event_type")

        if event_type:
            counts[event_type] += 1

    return counts
```

Top N:

```python
def top_event_types(events, n):
    counts = count_events_by_type(events)
    return counts.most_common(n)
```

Complexity:

```text
Time: O(n)
Space: O(u)
```

Interview line:

```text
Counter is useful when the task is frequency counting, such as top error types or status counts.
```


## 22. Grouping Records

Group records by a key.

```python
from collections import defaultdict

def group_by_customer(transactions):
    groups = defaultdict(list)

    for txn in transactions:
        customer_id = txn.get("customer_id")

        if customer_id is None:
            continue

        groups[customer_id].append(txn)

    return dict(groups)
```

Caution:

```text
Grouping stores all records in memory.
For very large data, aggregate incrementally or sort/group externally.
```

Interview line:

```text
Grouping by key is simple with defaultdict(list), but it can be memory-heavy if the dataset is huge.
```


## 23. Deduplication by Key

Deduplicate by stable key.

Keep first occurrence:

```python
def dedupe_keep_first(records, key_name):
    seen = set()
    result = []

    for record in records:
        key = record.get(key_name)

        if key is None or key in seen:
            continue

        seen.add(key)
        result.append(record)

    return result
```

Keep last occurrence:

```python
def dedupe_keep_last(records, key_name):
    by_key = {}

    for record in records:
        key = record.get(key_name)

        if key is None:
            continue

        by_key[key] = record

    return list(by_key.values())
```

Interview line:

```text
I first clarify whether duplicate handling means keep first, keep last, keep latest by timestamp, or fail on duplicates.
```


## 24. Latest Record Per ID

Common DE task:

```text
Given records with id and updated_at, keep latest record per id.
```

Code:

```python
def latest_record_by_id(records):
    latest = {}

    for record in records:
        record_id = record.get("id")
        updated_at = record.get("updated_at")

        if record_id is None or updated_at is None:
            continue

        existing = latest.get(record_id)

        if existing is None or updated_at > existing.get("updated_at"):
            latest[record_id] = record

    return list(latest.values())
```

Important:

```text
This assumes updated_at strings are comparable in consistent ISO format.
For safety, parse to datetime.
```

Safer version:

```python
def latest_record_by_id_with_parser(records, parse_time):
    latest = {}

    for record in records:
        record_id = record.get("id")
        updated_at = parse_time(record.get("updated_at"))

        if record_id is None or updated_at is None:
            continue

        existing = latest.get(record_id)

        if existing is None or updated_at > existing["_parsed_updated_at"]:
            copied = dict(record)
            copied["_parsed_updated_at"] = updated_at
            latest[record_id] = copied

    for record in latest.values():
        record.pop("_parsed_updated_at", None)

    return list(latest.values())
```

Interview line:

```text
For latest-record logic, I need a deterministic tie-breaker if updated_at is equal.
```


## 25. Sorting Records

Sort records by one or more keys.

```python
def sort_transactions(transactions):
    return sorted(
        transactions,
        key=lambda row: (row["customer_id"], row["created_at"], row["transaction_id"]),
    )
```

Descending numeric sort:

```python
def top_transactions_by_amount(transactions, n):
    return sorted(
        transactions,
        key=lambda row: row["amount"],
        reverse=True,
    )[:n]
```

Tie-breakers:

```python
def sort_by_amount_desc_id_asc(records):
    return sorted(records, key=lambda row: (-row["amount"], row["id"]))
```

Interview line:

```text
I make tie-breakers explicit so output is deterministic.
```


## 26. Top N Without Sorting Everything

For small N and large input, use heap.

```python
import heapq

def top_n_by_amount(records, n):
    heap = []

    for record in records:
        amount = record.get("amount")
        record_id = record.get("id")

        if amount is None or record_id is None:
            continue

        item = (amount, record_id, record)

        if len(heap) < n:
            heapq.heappush(heap, item)
        elif amount > heap[0][0]:
            heapq.heapreplace(heap, item)

    return [
        record
        for amount, record_id, record in sorted(heap, key=lambda x: (-x[0], x[1]))
    ]
```

Complexity:

```text
Time: O(n log k)
Space: O(k)
```

Interview line:

```text
If I only need top K and K is small, a heap avoids sorting the whole dataset.
```


## 27. Flatten Nested JSON

Flatten nested records.

Helper:

```python
def get_nested(record, path, default=None):
    current = record

    for key in path:
        if not isinstance(current, dict):
            return default

        current = current.get(key)

        if current is None:
            return default

    return current
```

Example:

```python
def flatten_order(order):
    return {
        "order_id": order.get("id"),
        "created_at": order.get("created_at"),
        "customer_id": get_nested(order, ["customer", "id"]),
        "customer_email": get_nested(order, ["customer", "email"]),
        "shipping_country": get_nested(order, ["shipping_address", "country"]),
        "total_amount": order.get("total_amount"),
    }
```

Interview line:

```text
I use safe nested access because API/file records often have missing nested objects.
```


## 28. Exploding Nested Arrays

Nested arrays often represent one-to-many relationships.

Example:

```json
{
  "order_id": "o1",
  "items": [
    {"sku": "A", "qty": 2},
    {"sku": "B", "qty": 1}
  ]
}
```

Explode:

```python
def explode_order_items(order):
    order_id = order.get("order_id") or order.get("id")
    items = order.get("items") or []

    rows = []

    for index, item in enumerate(items):
        rows.append({
            "order_id": order_id,
            "line_number": index + 1,
            "sku": item.get("sku"),
            "quantity": item.get("qty"),
        })

    return rows
```

Interview line:

```text
When flattening nested arrays, I usually create a child table with parent_id and line_number to preserve relationships.
```


## 29. Memory-Safe Processing

Bad for huge files:

```python
rows = list(read_csv_rows("huge.csv"))
```

Better:

```python
for row in read_csv_rows("huge.csv"):
    process(row)
```

Batch processing:

```python
def batched(iterable, batch_size):
    batch = []

    for item in iterable:
        batch.append(item)

        if len(batch) >= batch_size:
            yield batch
            batch = []

    if batch:
        yield batch
```

Usage:

```python
for batch in batched(read_csv_rows("huge.csv"), 1000):
    write_batch(batch)
```

Interview line:

```text
For large data, I stream and batch records instead of loading the entire dataset.
```


## 30. Atomic Writes

Atomic write pattern:

```text
write to temporary file
flush/close
rename temp file to final path
```

Code:

```python
import json
from pathlib import Path

def atomic_write_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_suffix(path.suffix + ".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, sort_keys=True)

    temp_path.replace(path)
```

Why:

```text
If script crashes during write, final output is not left half-written.
```

Interview line:

```text
I use atomic writes for local output/checkpoints so downstream steps do not read partial files.
```


## 31. Idempotent Script Design

A script is idempotent when rerunning does not corrupt output.

Strategies:

```text
overwrite deterministic output path
write to temp then replace
dedupe by stable key
upsert into target
partition overwrite for fixed date
include run_id in output metadata
avoid appending blindly unless designed
```

Bad:

```text
append output every run without dedupe
```

Good:

```text
write output for date=2026-01-01 to temp path, validate, then replace final partition file
```

Interview line:

```text
I make scripts rerunnable by writing deterministic outputs and avoiding blind appends.
```


## 32. Logging Basics

Use logging instead of print for scripts.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)

def process():
    logger.info("started_processing")
    logger.info("records_processed=%s invalid_records=%s", 100, 2)
```

Useful logs:

```text
input path
output path
record counts
invalid counts
dedupe counts
start/end time
duration
error category
```

Avoid logging:

```text
secrets
full PII-heavy records
huge payloads
```

Interview line:

```text
I log counts and context, not sensitive raw data.
```


## 33. Command-Line Arguments

Use argparse for reusable scripts.

```python
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--invalid-output", required=True)
    parser.add_argument("--max-invalid-ratio", type=float, default=0.05)
    return parser.parse_args()
```

Main:

```python
def main():
    args = parse_args()
    run_pipeline(
        input_path=args.input,
        output_path=args.output,
        invalid_output_path=args.invalid_output,
        max_invalid_ratio=args.max_invalid_ratio,
    )

if __name__ == "__main__":
    main()
```

Interview line:

```text
I use argparse so the script can run in different environments without code changes.
```


## 34. Testable Function Structure

Bad:

```python
with open("input.csv") as f:
    # parse, transform, aggregate, write everything here
```

Good:

```python
def transform_row(raw):
    ...

def validate_row(row):
    ...

def process_rows(rows):
    ...

def read_csv_rows(path):
    ...

def write_jsonl(path, records):
    ...

def main():
    ...
```

Why:

```text
transform_row and validate_row can be unit tested without files
process_rows can be tested with small in-memory lists
file I/O is isolated
```

Interview line:

```text
I isolate pure functions from I/O so most logic can be unit tested easily.
```


## 35. Basic Unit Test Examples

Simple tests without external dependencies:

```python
def test_parse_int_valid():
    assert parse_int("10") == 10

def test_parse_int_invalid():
    assert parse_int("abc") is None

def test_validate_transaction_missing_id():
    row = {"transaction_id": "", "amount": "10", "currency": "INR"}
    errors = validate_transaction(row)
    assert "missing_transaction_id" in errors

def test_latest_record_by_id():
    records = [
        {"id": "1", "updated_at": "2026-01-01T00:00:00Z", "value": "old"},
        {"id": "1", "updated_at": "2026-01-02T00:00:00Z", "value": "new"},
    ]
    result = latest_record_by_id(records)
    assert result[0]["value"] == "new"
```

Interview line:

```text
I would test parsing, validation, transformation, deduplication, and edge cases separately.
```


## 36. Common Data Scripting Edge Cases

Common edge cases:

```text
empty file
file missing
missing header
extra columns
missing required field
blank lines
invalid JSON line
malformed CSV row
numeric field contains comma
amount is negative
amount is empty
timestamp is invalid
timezone missing
duplicate id
same id same updated_at
different casing in enum
unexpected enum value
nested field missing
nested object is null
large file
partial output from previous run
permission error writing output
invalid output path
encoding issue
invalid ratio too high
```

Data Engineering-specific edge cases:

```text
late-arriving data
out-of-order records
soft deletes
schema drift
duplicate source files
partial reruns
file delivered twice
upstream sends footer row
header row repeated in middle
PII in invalid records
```


## 37. Common Mistakes

Common mistakes:

```text
using readlines() for large files
using pandas when pure Python was requested
using float for money
hardcoding file paths
not specifying encoding
not using context managers
silently skipping invalid rows
using bare except
catching all errors and continuing
not logging counts
not validating output
not handling empty input
not checking required fields
not making output deterministic
appending blindly on rerun
mixing I/O and business logic
not explaining memory complexity
```

Strict feedback:

```text
This is not interview-ready. Your script works only for clean data and silently drops malformed rows, so it would hide production data-quality issues.
```


## 38. Coding Problem: CSV to Clean JSONL

Problem:

```text
Read transactions.csv with columns:
id, customer_id, amount, currency, created_at

Write valid transactions to clean.jsonl.
Write invalid rows with reasons to invalid.jsonl.
```

Solution:

```python
import csv
import json
from pathlib import Path
from decimal import Decimal, InvalidOperation

def parse_decimal(value):
    if value is None or value == "":
        return None

    try:
        return Decimal(str(value))
    except InvalidOperation:
        return None

def transform_transaction(raw):
    return {
        "transaction_id": raw.get("id"),
        "customer_id": raw.get("customer_id"),
        "amount": parse_decimal(raw.get("amount")),
        "currency": raw.get("currency", "").upper(),
        "created_at": raw.get("created_at"),
    }

def validate_transaction(row):
    errors = []

    if not row.get("transaction_id"):
        errors.append("missing_transaction_id")

    if not row.get("customer_id"):
        errors.append("missing_customer_id")

    if row.get("amount") is None:
        errors.append("invalid_amount")

    if not row.get("currency"):
        errors.append("missing_currency")

    if not row.get("created_at"):
        errors.append("missing_created_at")

    return errors

def read_csv_rows(path):
    with Path(path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row_number, row in enumerate(reader, start=2):
            row["_row_number"] = row_number
            yield row

def write_jsonl(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, default=str))
            file.write("\n")

def convert_transactions(input_path, output_path, invalid_path):
    valid = []
    invalid = []

    for raw in read_csv_rows(input_path):
        row_number = raw.pop("_row_number")

        try:
            row = transform_transaction(raw)
            errors = validate_transaction(row)
        except Exception as exc:
            invalid.append({
                "row_number": row_number,
                "raw": raw,
                "errors": [f"transform_error:{exc}"],
            })
            continue

        if errors:
            invalid.append({
                "row_number": row_number,
                "raw": raw,
                "row": row,
                "errors": errors,
            })
        else:
            valid.append(row)

    write_jsonl(output_path, valid)
    write_jsonl(invalid_path, invalid)

    return {
        "valid_count": len(valid),
        "invalid_count": len(invalid),
    }
```

Complexity:

```text
Time: O(n)
Space: O(n) in this version because valid/invalid lists are held in memory.
```

Follow-up:

```text
Make it streaming by writing records as they are processed.
```


## 39. Coding Problem: Streaming CSV to JSONL

Problem:

```text
Modify CSV-to-JSONL conversion to avoid storing all rows in memory.
```

Solution:

```python
def convert_transactions_streaming(input_path, output_path, invalid_path):
    valid_count = 0
    invalid_count = 0

    output_path = Path(output_path)
    invalid_path = Path(invalid_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    invalid_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as valid_file, invalid_path.open("w", encoding="utf-8") as invalid_file:
        for raw in read_csv_rows(input_path):
            row_number = raw.pop("_row_number")

            try:
                row = transform_transaction(raw)
                errors = validate_transaction(row)
            except Exception as exc:
                invalid_record = {
                    "row_number": row_number,
                    "raw": raw,
                    "errors": [f"transform_error:{exc}"],
                }
                invalid_file.write(json.dumps(invalid_record, ensure_ascii=False, default=str) + "\n")
                invalid_count += 1
                continue

            if errors:
                invalid_record = {
                    "row_number": row_number,
                    "raw": raw,
                    "row": row,
                    "errors": errors,
                }
                invalid_file.write(json.dumps(invalid_record, ensure_ascii=False, default=str) + "\n")
                invalid_count += 1
            else:
                valid_file.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
                valid_count += 1

    return {
        "valid_count": valid_count,
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(n)
Space: O(1) excluding output files
```

Interview line:

```text
The streaming version is better for large files because it does not store all valid and invalid rows in memory.
```


## 40. Coding Problem: Count Error Logs

Problem:

```text
Given log lines, count ERROR logs by service.
Log format:
timestamp level service=<service> message=<message>
```

Solution:

```python
from collections import Counter

def parse_log_line(line):
    parts = line.strip().split()

    if len(parts) < 3:
        return None

    record = {
        "timestamp": parts[0],
        "level": parts[1],
    }

    for token in parts[2:]:
        if "=" in token:
            key, value = token.split("=", 1)
            record[key] = value

    return record

def count_error_logs_by_service(lines):
    counts = Counter()
    invalid_count = 0

    for line in lines:
        record = parse_log_line(line)

        if record is None:
            invalid_count += 1
            continue

        if record.get("level") == "ERROR":
            service = record.get("service")

            if service:
                counts[service] += 1
            else:
                invalid_count += 1

    return {
        "error_counts": dict(counts),
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(n * tokens_per_line)
Space: O(u), unique services
```

Data Engineering connection:

```text
This is a classic log summary script.
```


## 41. Coding Problem: Top Customers by Spend

Problem:

```text
Given transaction records, return top K customers by total spend.
```

Solution:

```python
from collections import defaultdict
from decimal import Decimal

def top_customers_by_spend(transactions, k):
    totals = defaultdict(Decimal)

    for txn in transactions:
        customer_id = txn.get("customer_id")
        amount = txn.get("amount")

        if customer_id is None or amount is None:
            continue

        totals[customer_id] += Decimal(str(amount))

    ranked = sorted(totals.items(), key=lambda item: (-item[1], item[0]))

    return [
        {"customer_id": customer_id, "total_spend": total}
        for customer_id, total in ranked[:k]
    ]
```

Complexity:

```text
Time: O(n + u log u), where u is unique customers
Space: O(u)
```

Follow-up:

```text
If k is small and u is huge, use heap for O(u log k).
```


## 42. Coding Problem: Latest User Profile

Problem:

```text
Given user profile records with user_id and updated_at, keep latest profile per user.
```

Solution:

```python
def latest_user_profiles(records):
    latest = {}

    for record in records:
        user_id = record.get("user_id")
        updated_at = record.get("updated_at")

        if not user_id or not updated_at:
            continue

        existing = latest.get(user_id)

        if existing is None:
            latest[user_id] = record
            continue

        if updated_at > existing.get("updated_at"):
            latest[user_id] = record
        elif updated_at == existing.get("updated_at"):
            # deterministic tie-breaker: keep record with larger ingestion_time if present
            if record.get("ingestion_time", "") > existing.get("ingestion_time", ""):
                latest[user_id] = record

    return list(latest.values())
```

Complexity:

```text
Time: O(n)
Space: O(u)
```

Interview point:

```text
Clarify tie-breaker for same updated_at.
```


## 43. Coding Problem: Compare Two CSV Extracts

Problem:

```text
Given source.csv and target.csv with primary key id, find:
- ids only in source
- ids only in target
- ids in both
```

Solution using sets:

```python
def read_ids_from_csv(path, id_column="id"):
    ids = set()

    for row in read_csv_rows(path):
        value = row.get(id_column)

        if value:
            ids.add(value)

    return ids

def compare_extract_ids(source_path, target_path):
    source_ids = read_ids_from_csv(source_path)
    target_ids = read_ids_from_csv(target_path)

    return {
        "only_in_source": sorted(source_ids - target_ids),
        "only_in_target": sorted(target_ids - source_ids),
        "in_both": sorted(source_ids & target_ids),
    }
```

Complexity:

```text
Time: O(n + m)
Space: O(n + m)
```

Follow-up:

```text
If files are huge and sorted by id, use streaming two-pointer comparison to reduce memory.
```


## 44. Coding Problem: Flatten Orders and Items

Problem:

```text
Given JSONL orders, write:
- orders.jsonl
- order_items.jsonl

Each order has nested items array.
```

Solution:

```python
def flatten_order(order):
    return {
        "order_id": order.get("id"),
        "customer_id": get_nested(order, ["customer", "id"]),
        "created_at": order.get("created_at"),
        "total_amount": order.get("total_amount"),
    }

def flatten_order_items(order):
    order_id = order.get("id")
    items = order.get("items") or []

    rows = []

    for index, item in enumerate(items):
        rows.append({
            "order_id": order_id,
            "line_number": index + 1,
            "sku": item.get("sku"),
            "quantity": item.get("quantity"),
            "unit_price": item.get("unit_price"),
        })

    return rows

def process_orders(records):
    order_rows = []
    item_rows = []

    for order in records:
        order_rows.append(flatten_order(order))
        item_rows.extend(flatten_order_items(order))

    return order_rows, item_rows
```

Data Engineering point:

```text
Nested arrays usually become child tables with parent key and line number.
```


## 45. Coding Problem: Sessionize Events

Problem:

```text
Given events sorted by user_id and event_time, assign session number.
New session starts when user changes or gap between events exceeds timeout_seconds.
```

Solution:

```python
from datetime import datetime

def parse_iso_timestamp(value):
    if not value:
        return None

    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def sessionize_events(events, timeout_seconds):
    result = []
    current_user = None
    last_event_time = None
    session_number = 0

    for event in events:
        user_id = event.get("user_id")
        event_time = parse_iso_timestamp(event.get("event_time"))

        if user_id is None or event_time is None:
            continue

        if user_id != current_user:
            current_user = user_id
            session_number = 1
            last_event_time = event_time
        else:
            gap = (event_time - last_event_time).total_seconds()

            if gap > timeout_seconds:
                session_number += 1

            last_event_time = event_time

        enriched = dict(event)
        enriched["session_number"] = session_number
        result.append(enriched)

    return result
```

Assumption:

```text
Input is sorted by user_id and event_time.
```

Complexity:

```text
Time: O(n)
Space: O(n) for output
```

Follow-up:

```text
If input is not sorted, sort first by (user_id, event_time).
```


## 46. Coding Problem: File Summary Metrics

Problem:

```text
Read a CSV and return summary:
- total rows
- valid rows
- invalid rows
- unique customers
- total amount
```

Solution:

```python
from decimal import Decimal

def summarize_transactions(path):
    total_rows = 0
    valid_rows = 0
    invalid_rows = 0
    unique_customers = set()
    total_amount = Decimal("0")

    for raw in read_csv_rows(path):
        total_rows += 1
        row = transform_transaction(raw)
        errors = validate_transaction(row)

        if errors:
            invalid_rows += 1
            continue

        valid_rows += 1
        unique_customers.add(row["customer_id"])
        total_amount += row["amount"]

    return {
        "total_rows": total_rows,
        "valid_rows": valid_rows,
        "invalid_rows": invalid_rows,
        "unique_customers": len(unique_customers),
        "total_amount": str(total_amount),
    }
```

Complexity:

```text
Time: O(n)
Space: O(u), unique customers
```


## 47. Coding Problem: Detect Duplicate IDs

Problem:

```text
Given records, return duplicate IDs and their counts.
```

Solution:

```python
from collections import Counter

def duplicate_id_counts(records):
    counts = Counter()

    for record in records:
        record_id = record.get("id")

        if record_id:
            counts[record_id] += 1

    return {
        record_id: count
        for record_id, count in counts.items()
        if count > 1
    }
```

Complexity:

```text
Time: O(n)
Space: O(u)
```

Follow-up:

```text
Return line numbers for duplicates.
```

Solution direction:

```text
Use defaultdict(list) mapping id to row_numbers.
```


## 48. Coding Problem: Duplicate IDs with Row Numbers

Solution:

```python
from collections import defaultdict

def duplicate_ids_with_rows(records):
    rows_by_id = defaultdict(list)

    for index, record in enumerate(records, start=1):
        record_id = record.get("id")

        if record_id:
            rows_by_id[record_id].append(index)

    return {
        record_id: rows
        for record_id, rows in rows_by_id.items()
        if len(rows) > 1
    }
```

Complexity:

```text
Time: O(n)
Space: O(u + d), where d is duplicate row references
```

Data Engineering connection:

```text
Useful for data-quality reports before loading.
```


## 49. Coding Problem: Normalize Enum Values

Problem:

```text
Normalize status values:
success, Success, SUCCESS → SUCCESS
failed, Fail, FAILURE → FAILED
unknown values should become None and produce validation error.
```

Solution:

```python
STATUS_MAP = {
    "success": "SUCCESS",
    "succeeded": "SUCCESS",
    "failed": "FAILED",
    "fail": "FAILED",
    "failure": "FAILED",
    "pending": "PENDING",
}

def normalize_status(value):
    if value is None:
        return None

    key = value.strip().lower()
    return STATUS_MAP.get(key)
```

Validation:

```python
def validate_status(row):
    errors = []

    if row.get("status") is None:
        errors.append("invalid_status")

    return errors
```

Interview line:

```text
I normalize known variants but do not silently map unknown values to a fake category.
```


## 50. Coding Problem: Data Quality Rules

Problem:

```text
Given transaction rows, return data-quality metrics:
- missing_id_count
- invalid_amount_count
- invalid_currency_count
- duplicate_id_count
```

Solution:

```python
from collections import Counter

def data_quality_report(rows):
    metrics = Counter()
    id_counts = Counter()

    for row in rows:
        transaction_id = row.get("transaction_id")

        if not transaction_id:
            metrics["missing_id_count"] += 1
        else:
            id_counts[transaction_id] += 1

        if row.get("amount") is None:
            metrics["invalid_amount_count"] += 1

        currency = row.get("currency")

        if currency not in {"INR", "USD", "target marketR", "GBP"}:
            metrics["invalid_currency_count"] += 1

    metrics["duplicate_id_count"] = sum(
        1 for count in id_counts.values() if count > 1
    )

    return dict(metrics)
```

Complexity:

```text
Time: O(n)
Space: O(u)
```


## 51. Coding Problem: Merge Small Files

Problem:

```text
Given multiple JSONL files, merge them into one output JSONL.
Skip blank lines.
Collect invalid JSON lines.
```

Solution:

```python
import json
from pathlib import Path

def merge_jsonl_files(input_paths, output_path, invalid_path):
    output_path = Path(output_path)
    invalid_path = Path(invalid_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    invalid_path.parent.mkdir(parents=True, exist_ok=True)

    valid_count = 0
    invalid_count = 0

    with output_path.open("w", encoding="utf-8") as out, invalid_path.open("w", encoding="utf-8") as bad:
        for input_path in input_paths:
            input_path = Path(input_path)

            with input_path.open("r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()

                    if not line:
                        continue

                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as exc:
                        invalid = {
                            "file": str(input_path),
                            "line_number": line_number,
                            "error": str(exc),
                            "raw": line,
                        }
                        bad.write(json.dumps(invalid, ensure_ascii=False) + "\n")
                        invalid_count += 1
                        continue

                    out.write(json.dumps(record, ensure_ascii=False) + "\n")
                    valid_count += 1

    return {
        "valid_count": valid_count,
        "invalid_count": invalid_count,
    }
```

Data Engineering connection:

```text
Small-file merge is a common operational script, but in distributed systems this may be handled by Spark/warehouse tools.
```


## 52. Coding Problem: Generate Reconciliation Report

Problem:

```text
Given source totals and target totals by customer_id, identify mismatches.
```

Solution:

```python
def reconcile_totals(source_totals, target_totals):
    all_customers = set(source_totals) | set(target_totals)
    mismatches = []

    for customer_id in sorted(all_customers):
        source_value = source_totals.get(customer_id, 0)
        target_value = target_totals.get(customer_id, 0)

        if source_value != target_value:
            mismatches.append({
                "customer_id": customer_id,
                "source_total": source_value,
                "target_total": target_value,
                "difference": source_value - target_value,
            })

    return mismatches
```

Complexity:

```text
Time: O(u log u) due to sorted output
Space: O(u)
```

Interview point:

```text
Sorted output helps make reports deterministic and easy to diff.
```


## 53. Coding Problem: Detect Missing Dates

Problem:

```text
Given processed date strings and expected start/end date inclusive, return missing dates.
```

Solution:

```python
from datetime import date, timedelta

def date_range(start_date, end_date):
    current = start_date

    while current <= end_date:
        yield current
        current += timedelta(days=1)

def missing_dates(processed_dates, start_date, end_date):
    processed = set(processed_dates)
    missing = []

    for current in date_range(start_date, end_date):
        current_str = current.isoformat()

        if current_str not in processed:
            missing.append(current_str)

    return missing
```

Complexity:

```text
Time: O(d + n), where d is number of expected dates
Space: O(n)
```

Data Engineering connection:

```text
Find missing daily partitions.
```


## 54. Coding Problem: Partition Files by Date

Problem:

```text
Given records with event_date, write them into output files by event_date.
```

Simple in-memory grouping:

```python
from collections import defaultdict

def partition_records_by_date(records):
    by_date = defaultdict(list)

    for record in records:
        event_date = record.get("event_date")

        if event_date:
            by_date[event_date].append(record)

    return dict(by_date)
```

Writing:

```python
def write_partitions(base_path, partitions):
    base_path = Path(base_path)

    for event_date, records in partitions.items():
        output_path = base_path / f"event_date={event_date}" / "data.jsonl"
        write_jsonl(output_path, records)
```

Caution:

```text
In-memory grouping may be heavy for many records.
For huge data, stream into limited writers or use a processing framework.
```


## 55. Coding Problem: Streaming Partition Writer

Problem:

```text
Write records to partition files without storing all records in memory.
```

Simplified code:

```python
import json
from pathlib import Path

class PartitionWriter:
    def __init__(self, base_path, partition_field):
        self.base_path = Path(base_path)
        self.partition_field = partition_field
        self.files = {}

    def write(self, record):
        partition_value = record.get(self.partition_field)

        if not partition_value:
            partition_value = "__missing__"

        path = self.base_path / f"{self.partition_field}={partition_value}" / "data.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)

        file = self.files.get(path)

        if file is None:
            file = path.open("a", encoding="utf-8")
            self.files[path] = file

        file.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")

    def close(self):
        for file in self.files.values():
            file.close()

        self.files.clear()
```

Usage:

```python
writer = PartitionWriter("output", "event_date")

try:
    for record in records:
        writer.write(record)
finally:
    writer.close()
```

Caution:

```text
If many partitions are open, this can exceed file descriptor limits. In production, manage open writers carefully.
```


## 56. Coding Problem: Find Top Error Services from JSONL

Problem:

```text
Read JSONL logs and return top K services by ERROR count.
```

Solution:

```python
from collections import Counter

def top_error_services_from_jsonl(path, k):
    counts = Counter()
    invalid_count = 0

    for record in read_jsonl(path):
        if record.get("_invalid"):
            invalid_count += 1
            continue

        if record.get("level") == "ERROR":
            service = record.get("service")

            if service:
                counts[service] += 1
            else:
                invalid_count += 1

    return {
        "top_services": counts.most_common(k),
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(n + u log k) depending Counter.most_common implementation
Space: O(u)
```


## 57. Coding Problem: Convert Wide to Long

Problem:

```text
Input row:
{"date": "2026-01-01", "clicks": 10, "views": 100}

Output rows:
{"date": "2026-01-01", "metric": "clicks", "value": 10}
{"date": "2026-01-01", "metric": "views", "value": 100}
```

Solution:

```python
def wide_to_long(row, id_fields, metric_fields):
    output = []

    base = {
        field: row.get(field)
        for field in id_fields
    }

    for metric in metric_fields:
        output.append({
            **base,
            "metric": metric,
            "value": row.get(metric),
        })

    return output
```

Data Engineering connection:

```text
Useful for normalizing metric exports.
```


## 58. Coding Problem: Long to Wide

Problem:

```text
Input rows:
{"date": "2026-01-01", "metric": "clicks", "value": 10}
{"date": "2026-01-01", "metric": "views", "value": 100}

Output:
{"date": "2026-01-01", "clicks": 10, "views": 100}
```

Solution:

```python
def long_to_wide(rows, id_field, metric_field="metric", value_field="value"):
    output = {}

    for row in rows:
        key = row.get(id_field)
        metric = row.get(metric_field)

        if key is None or metric is None:
            continue

        if key not in output:
            output[key] = {id_field: key}

        output[key][metric] = row.get(value_field)

    return list(output.values())
```

Complexity:

```text
Time: O(n)
Space: O(u * metrics)
```


## 59. Coding Problem: Safe Schema Projection

Problem:

```text
Project records to a fixed schema, using None for missing optional fields.
```

Solution:

```python
def project_record(record, fieldnames):
    return {
        field: record.get(field)
        for field in fieldnames
    }

def project_records(records, fieldnames):
    for record in records:
        yield project_record(record, fieldnames)
```

Why:

```text
Output schema is deterministic.
Extra fields are ignored intentionally.
Missing fields are explicit as None.
```

Interview line:

```text
Projection makes output schema stable even if raw input has extra fields.
```


## 60. Coding Problem: Schema Drift Detector

Problem:

```text
Given expected fields and actual records, report unknown fields and missing required fields.
```

Solution:

```python
from collections import Counter

def schema_drift_report(records, expected_fields, required_fields):
    expected = set(expected_fields)
    required = set(required_fields)

    unknown_field_counts = Counter()
    missing_required_counts = Counter()

    for record in records:
        actual = set(record.keys())

        for field in actual - expected:
            unknown_field_counts[field] += 1

        for field in required:
            if field not in record or record.get(field) in (None, ""):
                missing_required_counts[field] += 1

    return {
        "unknown_fields": dict(unknown_field_counts),
        "missing_required": dict(missing_required_counts),
    }
```

Complexity:

```text
Time: O(n * fields_per_record)
Space: O(number of distinct fields)
```


## 61. Coding Problem: Incremental File Filter

Problem:

```text
Given records with updated_at, return records updated after a watermark.
Assume timestamps are consistent ISO strings.
```

Solution:

```python
def filter_updated_after(records, watermark):
    for record in records:
        updated_at = record.get("updated_at")

        if updated_at and updated_at > watermark:
            yield record
```

Safer with datetime parser:

```python
def filter_updated_after_parsed(records, watermark_dt, parse_time):
    for record in records:
        updated_dt = parse_time(record.get("updated_at"))

        if updated_dt and updated_dt > watermark_dt:
            yield record
```

Interview point:

```text
String timestamp comparison is safe only when format is consistent and timezone-normalized.
```


## 62. Coding Problem: Checkpoint Local Script

Problem:

```text
Process files one by one and save checkpoint of processed filenames.
```

Solution:

```python
import json
from pathlib import Path

def load_processed_files(checkpoint_path):
    path = Path(checkpoint_path)

    if not path.exists():
        return set()

    with path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    return set(payload.get("processed_files", []))

def save_processed_files(checkpoint_path, processed_files):
    atomic_write_json(checkpoint_path, {
        "processed_files": sorted(processed_files),
    })

def process_files_with_checkpoint(input_paths, checkpoint_path, process_file):
    processed = load_processed_files(checkpoint_path)

    for path in input_paths:
        path_str = str(path)

        if path_str in processed:
            continue

        process_file(path)

        processed.add(path_str)
        save_processed_files(checkpoint_path, processed)
```

Interview line:

```text
Checkpoint after successful file processing, not before.
```


## 63. Coding Problem: Find Files by Extension

Problem:

```text
Find all .csv files under a directory recursively.
```

Solution:

```python
from pathlib import Path

def find_files_by_extension(base_dir, extension):
    base_dir = Path(base_dir)

    return sorted(base_dir.rglob(f"*{extension}"))
```

Example:

```python
csv_files = find_files_by_extension("data/raw", ".csv")
```

Interview point:

```text
pathlib makes path handling cleaner and cross-platform.
```


## 64. Coding Problem: File Manifest

Problem:

```text
Create manifest for files:
path, size_bytes, modified_time
```

Solution:

```python
from pathlib import Path
from datetime import datetime, timezone

def build_file_manifest(base_dir, pattern="*"):
    base_dir = Path(base_dir)
    manifest = []

    for path in sorted(base_dir.rglob(pattern)):
        if not path.is_file():
            continue

        stat = path.stat()

        manifest.append({
            "path": str(path),
            "size_bytes": stat.st_size,
            "modified_time": datetime.fromtimestamp(
                stat.st_mtime,
                tz=timezone.utc,
            ).isoformat(),
        })

    return manifest
```

Data Engineering connection:

```text
File manifests are useful for ingestion audits and detecting missing/changed files.
```


## 65. Coding Problem: Compare File Manifests

Problem:

```text
Given old and new file manifests, detect added, removed, and changed files.
Changed means same path but different size_bytes.
```

Solution:

```python
def compare_manifests(old_manifest, new_manifest):
    old_by_path = {row["path"]: row for row in old_manifest}
    new_by_path = {row["path"]: row for row in new_manifest}

    old_paths = set(old_by_path)
    new_paths = set(new_by_path)

    added = sorted(new_paths - old_paths)
    removed = sorted(old_paths - new_paths)

    changed = []

    for path in sorted(old_paths & new_paths):
        if old_by_path[path].get("size_bytes") != new_by_path[path].get("size_bytes"):
            changed.append(path)

    return {
        "added": added,
        "removed": removed,
        "changed": changed,
    }
```

Complexity:

```text
Time: O(n + m)
Space: O(n + m)
```


## 66. Coding Problem: Redact PII Fields

Problem:

```text
Given records, redact fields like email and phone before logging/writing invalid records.
```

Solution:

```python
PII_FIELDS = {"email", "phone", "ssn", "address"}

def redact_record(record):
    redacted = {}

    for key, value in record.items():
        if key.lower() in PII_FIELDS:
            redacted[key] = "***REDACTED***"
        else:
            redacted[key] = value

    return redacted
```

Nested version direction:

```text
Use recursive traversal if nested PII fields exist.
```

Interview line:

```text
Invalid record handling must consider sensitive data; do not blindly log raw PII.
```


## 67. Coding Problem: Recursive Flatten Dictionary

Problem:

```text
Flatten nested dictionary:
{"a": {"b": 1}, "c": 2}
→ {"a_b": 1, "c": 2}
```

Solution:

```python
def flatten_dict(record, parent_key="", separator="_"):
    flattened = {}

    for key, value in record.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key

        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key, separator))
        else:
            flattened[new_key] = value

    return flattened
```

Caution:

```text
Nested arrays require separate handling; blindly flattening arrays can produce messy columns.
```


## 68. Coding Problem: Normalize Column Names

Problem:

```text
Normalize column names to lowercase snake_case.
```

Solution:

```python
import re

def normalize_column_name(name):
    name = name.strip()
    name = re.sub(r"[^0-9a-zA-Z]+", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_").lower()
```

Example:

```python
normalize_column_name("Customer ID")  # customer_id
normalize_column_name("Amount($)")    # amount
```

Data Engineering connection:

```text
Consistent column names reduce downstream SQL and warehouse issues.
```


## 69. Coding Problem: Rename Record Keys

Problem:

```text
Normalize keys for each record.
```

Solution:

```python
def normalize_record_keys(record):
    return {
        normalize_column_name(key): value
        for key, value in record.items()
    }
```

Caution:

```text
Different original columns can collapse to the same normalized name.
Example: "A-B" and "A B" both become "a_b".
Detect collisions if needed.
```

Collision-safe version:

```python
def normalize_record_keys_safe(record):
    normalized = {}

    for key, value in record.items():
        new_key = normalize_column_name(key)

        if new_key in normalized:
            raise ValueError(f"Column name collision after normalization: {new_key}")

        normalized[new_key] = value

    return normalized
```


## 70. Coding Problem: Row Hash

Problem:

```text
Generate stable hash for a record based on selected fields.
```

Solution:

```python
import hashlib
import json

def stable_row_hash(record, fields):
    payload = {
        field: record.get(field)
        for field in fields
    }

    encoded = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()
```

Use cases:

```text
change detection
dedupe when no natural key
audit comparisons
slowly changing dimension checks
```

Interview line:

```text
Hashing selected normalized fields can help detect changes, but a stable business key is preferable when available.
```


## 71. Coding Problem: Change Detection

Problem:

```text
Given old and new records by id, detect inserts, updates, and deletes.
```

Solution:

```python
def detect_changes(old_records, new_records, key_field, compare_fields):
    old_by_key = {row[key_field]: row for row in old_records if row.get(key_field)}
    new_by_key = {row[key_field]: row for row in new_records if row.get(key_field)}

    old_keys = set(old_by_key)
    new_keys = set(new_by_key)

    inserts = sorted(new_keys - old_keys)
    deletes = sorted(old_keys - new_keys)
    updates = []

    for key in sorted(old_keys & new_keys):
        old_hash = stable_row_hash(old_by_key[key], compare_fields)
        new_hash = stable_row_hash(new_by_key[key], compare_fields)

        if old_hash != new_hash:
            updates.append(key)

    return {
        "inserts": inserts,
        "updates": updates,
        "deletes": deletes,
    }
```

Data Engineering connection:

```text
This is a simplified CDC/change-detection script.
```


## 72. Coding Problem: Generate SQL Insert Statements

Problem:

```text
Generate simple SQL INSERT statements from rows.
```

Safer note:

```text
In production, use parameterized queries or bulk loaders.
String-generated SQL is risky if executed directly.
```

Interview-safe function for script output only:

```python
def sql_quote(value):
    if value is None:
        return "NULL"

    if isinstance(value, (int, float)):
        return str(value)

    escaped = str(value).replace("'", "''")
    return f"'{escaped}'"

def generate_insert_statement(table_name, row, columns):
    values = ", ".join(sql_quote(row.get(column)) for column in columns)
    column_list = ", ".join(columns)

    return f"INSERT INTO {table_name} ({column_list}) VALUES ({values});"
```

Interview line:

```text
I would avoid executing generated SQL strings directly; parameterized inserts or warehouse bulk load are safer.
```


## 73. Coding Problem: Build Batch SQL Values

Problem:

```text
Build multi-row VALUES section for small seed scripts.
```

Solution:

```python
def generate_insert_many(table_name, rows, columns):
    if not rows:
        return ""

    column_list = ", ".join(columns)
    values_lines = []

    for row in rows:
        values = ", ".join(sql_quote(row.get(column)) for column in columns)
        values_lines.append(f"({values})")

    values_sql = ",\n".join(values_lines)

    return f"INSERT INTO {table_name} ({column_list}) VALUES\n{values_sql};"
```

Caution:

```text
For large loads, do not generate huge INSERT statements. Use bulk loading.
```


## 74. Coding Problem: Config-Driven Transformation

Problem:

```text
Map input fields to output fields using config.
```

Config:

```python
FIELD_MAP = {
    "id": "transaction_id",
    "customer": "customer_id",
    "amount": "amount",
}
```

Solution:

```python
def map_fields(raw, field_map):
    output = {}

    for source_field, target_field in field_map.items():
        output[target_field] = raw.get(source_field)

    return output
```

Use case:

```text
vendor files with different column names
simple reusable mapping scripts
```

Interview line:

```text
For many similar files, config-driven field mapping can reduce duplicate code, but validation still needs to be explicit.
```


## 75. Coding Problem: Multi-File Processing Summary

Problem:

```text
Process multiple files and return per-file summary plus total summary.
```

Solution:

```python
def process_multiple_files(paths, process_one_file):
    summaries = []
    total_valid = 0
    total_invalid = 0

    for path in paths:
        summary = process_one_file(path)
        summaries.append({
            "path": str(path),
            **summary,
        })

        total_valid += summary.get("valid_count", 0)
        total_invalid += summary.get("invalid_count", 0)

    return {
        "files": summaries,
        "total_valid": total_valid,
        "total_invalid": total_invalid,
    }
```

Interview line:

```text
A per-file summary is useful for audit and debugging because one bad file can be isolated.
```


## 76. Coding Problem: Detect Header Repeated in CSV Body

Problem:

```text
Some vendor CSV files repeat the header row in the middle.
Skip repeated header rows.
```

Solution:

```python
def read_csv_rows_skip_repeated_header(path):
    path = Path(path)

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames or []

        for row_number, row in enumerate(reader, start=2):
            is_repeated_header = all(
                row.get(field) == field
                for field in fieldnames
            )

            if is_repeated_header:
                continue

            row["_row_number"] = row_number
            yield row
```

Interview line:

```text
Vendor files often contain operational artifacts like repeated headers or footers, so scripts should handle known file quirks explicitly.
```


## 77. Coding Problem: Detect Footer Row

Problem:

```text
Vendor CSV contains footer row:
TOTAL,1000
Skip footer and capture total if needed.
```

Solution idea:

```python
def is_footer_row(row):
    first_value = next(iter(row.values()), "")

    if first_value is None:
        return False

    return str(first_value).strip().upper() == "TOTAL"
```

Usage:

```python
for row in read_csv_rows(path):
    if is_footer_row(row):
        continue

    process(row)
```

Interview point:

```text
Footer handling should be explicit and documented, not accidental.
```


## 78. Coding Problem: Safe Division in Metrics

Problem:

```text
Calculate success_rate = success_count / total_count.
Avoid divide-by-zero.
```

Solution:

```python
def safe_divide(numerator, denominator, default=None):
    if denominator in (0, None):
        return default

    return numerator / denominator
```

Usage:

```python
def calculate_success_rate(row):
    success = row.get("success_count", 0)
    total = row.get("total_count", 0)

    return safe_divide(success, total, default=0)
```

Interview line:

```text
Metric scripts should handle zero denominators explicitly instead of crashing or returning misleading values.
```


## 79. Coding Problem: Rolling Daily Counts

Problem:

```text
Given records with event_date, count records per date.
Return dates sorted ascending.
```

Solution:

```python
from collections import Counter

def daily_counts(records):
    counts = Counter()

    for record in records:
        event_date = record.get("event_date")

        if event_date:
            counts[event_date] += 1

    return [
        {"event_date": event_date, "count": counts[event_date]}
        for event_date in sorted(counts)
    ]
```

Complexity:

```text
Time: O(n + d log d)
Space: O(d)
```


## 80. Coding Problem: Running Total by Date

Problem:

```text
Given daily counts sorted by date, add running_total.
```

Solution:

```python
def add_running_total(daily_rows):
    running_total = 0
    output = []

    for row in daily_rows:
        running_total += row.get("count", 0)
        enriched = dict(row)
        enriched["running_total"] = running_total
        output.append(enriched)

    return output
```

Data Engineering connection:

```text
Simple metric enrichment often appears in reporting scripts.
```


## 81. Data Scripting Pattern Classification Drill

Classify each prompt.

```text
1. Count events by event_type.
2. Keep latest row per customer_id.
3. Read huge JSONL file without memory issue.
4. Flatten nested customer.address.country.
5. Split valid and invalid rows.
6. Detect duplicate transaction IDs.
7. Convert records with items array into item rows.
8. Compare source and target IDs.
9. Generate file manifest.
10. Detect missing daily partitions.
11. Normalize column names.
12. Create row hash from selected fields.
13. Detect inserted/updated/deleted records.
14. Calculate top 10 customers by spend.
15. Write output safely without partial file.
16. Fail if invalid rows exceed 5%.
17. Convert wide metrics to long format.
18. Handle repeated CSV header in body.
19. Parse key-value logs.
20. Redact email before writing invalid records.
```

Expected classification:

```text
1. Counter/frequency
2. dedupe latest by key
3. streaming line-by-line
4. nested JSON flattening
5. validation/dead-letter
6. Counter/defaultdict row tracking
7. explode nested array
8. set diff or sorted two-pointer diff
9. pathlib/stat manifest
10. date range + set
11. regex/string normalization
12. stable hash
13. change detection by key/hash
14. aggregation + sorting/heap
15. atomic write
16. invalid threshold
17. reshape/pivot-like transform
18. vendor file cleanup
19. log parsing
20. PII-safe invalid handling
```

Passing standard:

```text
18/20 correct before timed data scripting mocks.
```


## 82. High-ROI Python Data Scripting Topics

Practice these first.

| Topic | What Candidate Must Explain |
|---|---|
| File I/O | pathlib, context managers, encoding |
| CSV | DictReader, DictWriter, newline |
| JSONL | streamable read/write |
| Validation | required fields, error reasons |
| Dead-letter | invalid records with context |
| Transform | clean output schema |
| Aggregation | defaultdict, Counter |
| Deduplication | keep first/last/latest |
| Timestamps | parse and normalize UTC |
| Numeric parsing | Decimal for money |
| Streaming | avoid loading huge files |
| Atomic writes | temp file then replace |
| Logging | counts and context |
| CLI args | argparse |
| Tests | pure functions and small fixtures |
| Flattening | nested dicts and arrays |
| Reconciliation | compare extracts |
| Data quality | duplicate/missing/invalid counts |
| Idempotency | deterministic output |
| PII | redact sensitive fields |


## 83. Practice Ladder

### Level 1: File basics

```text
read CSV rows
write CSV rows
read JSONL
write JSONL
find files by extension
```

Exit:

```text
Candidate uses pathlib, context managers, and explicit encoding.
```

### Level 2: Validation and transformation

```text
transform transaction row
validate required fields
split valid/invalid records
invalid threshold
normalize enum values
```

Exit:

```text
Candidate handles dirty data intentionally.
```

### Level 3: Aggregation and dedupe

```text
count events
top customers by spend
latest record per ID
duplicate ID report
daily counts
```

Exit:

```text
Candidate can implement group-by/dedupe in pure Python.
```

### Level 4: Nested and file operations

```text
flatten nested JSON
explode order items
merge JSONL files
build file manifest
compare manifests
```

Exit:

```text
Candidate can process realistic semi-structured data.
```

### Level 5: Production scripting

```text
streaming CSV conversion
atomic writes
checkpoint files
schema drift report
change detection
PII redaction
CLI structure
tests
```

Exit:

```text
Candidate can discuss production-safe data scripts.
```


## 84. 7-Day Data Scripting Plan

### Day 1: File handling

Problems:

```text
Read CSV rows.
Write CSV rows.
Read JSONL.
Write JSONL.
Find CSV files recursively.
```

Focus:

```text
pathlib
context managers
encoding
streaming
```

### Day 2: Validation and transformation

Problems:

```text
Transform transaction row.
Validate transaction row.
Split valid/invalid records.
Invalid threshold.
Normalize statuses.
```

Focus:

```text
dirty data
error reasons
dead-letter
```

### Day 3: Aggregation and dedupe

Problems:

```text
Count event types.
Top customers by spend.
Latest user profile.
Duplicate IDs with row numbers.
Daily counts.
```

Focus:

```text
Counter
defaultdict
dedupe rules
tie-breakers
```

### Day 4: Nested data

Problems:

```text
Flatten order.
Explode order items.
Recursive flatten dictionary.
Wide to long.
Long to wide.
```

Focus:

```text
nested JSON
one-to-many
schema projection
```

### Day 5: Reconciliation and manifests

Problems:

```text
Compare two CSV extracts.
Build file manifest.
Compare manifests.
Detect missing dates.
Detect changes by hash.
```

Focus:

```text
sets
hashing
change detection
audits
```

### Day 6: Production script design

Problems:

```text
Streaming CSV to JSONL.
Atomic write.
Checkpoint local script.
Argparse CLI.
Logging summary metrics.
```

Focus:

```text
memory
idempotency
reruns
testability
```

### Day 7: Mock and repair

Tasks:

```text
Run Mock Set 3 or 4.
Review mistakes.
Repair weakest scripting topic.
Update progress.
```


## 85. 30-Day Data Scripting Plan

### Week 1: Python file and record basics

Focus:

```text
CSV
JSONL
pathlib
context managers
safe parsing
```

Exit:

```text
Candidate can read/write common file formats cleanly.
```

### Week 2: Data quality and transformation

Focus:

```text
validation
dead-letter
type parsing
timestamp parsing
normalization
invalid thresholds
```

Exit:

```text
Candidate can process dirty files without hiding bad rows.
```

### Week 3: Aggregation, dedupe, and reconciliation

Focus:

```text
Counter
defaultdict
latest record
top N
set differences
manifest comparison
change detection
```

Exit:

```text
Candidate can implement common DE utility scripts.
```

### Week 4: Production-grade scripting

Focus:

```text
streaming
atomic writes
checkpointing
idempotency
logging
CLI
testing
PII redaction
schema drift
```

Exit:

```text
Average mock score >= 4/5.
```


## 86. Mock Set 1: Data Scripting Basics

Problems:

```text
1. Read CSV rows with DictReader.
2. Write JSONL output.
3. Transform transaction row.
4. Validate required fields.
5. Count event types.
```

Expected skills:

```text
file I/O
json/csv
basic transformation
validation
Counter
```

Passing standard:

```text
Average score >= 4/5.
Candidate uses context managers and explicit error handling.
```


## 87. Mock Set 2: Aggregation and Dedupe

Problems:

```text
1. Top customers by spend.
2. Latest record per ID.
3. Duplicate IDs with row numbers.
4. Daily counts sorted by date.
5. Reconciliation report for source vs target totals.
```

Expected skills:

```text
defaultdict
Counter
dedupe rules
sorting tie-breakers
set/dict comparison
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains time/space complexity.
```


## 88. Mock Set 3: Realistic Data Processing

Problems:

```text
1. CSV to clean JSONL with invalid JSONL.
2. Flatten orders and order items.
3. Compare two CSV extracts by ID.
4. Detect missing daily partitions.
5. Generate file manifest and compare manifests.
```

Expected skills:

```text
ETL script structure
dead-letter
nested JSON
sets
date handling
file metadata
```

Passing standard:

```text
Average score >= 4/5.
Candidate handles dirty data and deterministic output.
```


## 89. Mock Set 4: Production Scripting

Problems:

```text
1. Streaming CSV to JSONL without storing all rows.
2. Atomic output write.
3. Checkpoint processed files.
4. Schema drift report.
5. Redact PII fields before invalid record output.
```

Expected skills:

```text
memory-safe processing
idempotency
checkpointing
schema validation
PII handling
production reasoning
```

Passing standard:

```text
Average score >= 4/5.
Candidate gives production-safe trade-offs.
```


## 90. Timed Drill Protocol

Use this timing protocol.

### Simple scripting problem

```text
15-25 minutes
```

### Medium ETL scripting problem

```text
30-45 minutes
```

### Production scenario

```text
20-30 minutes
```

Per coding drill:

```text
Minute 0-3:
Clarify input, output, schema, and invalid-row behavior.

Minute 3-6:
Define functions and data structures.

Minute 6-25:
Code core logic.

Minute 25-35:
Add validation, edge cases, and summary counts.

Minute 35-45:
Explain complexity, memory, and production improvements.
```

If candidate writes one giant untestable script:

```text
Stop and ask them to refactor into functions.
```


## 91. Review Checklist

Review data scripting answers using:

```text
1. Did candidate clarify input format?
2. Did candidate clarify output format?
3. Did candidate handle missing/invalid fields?
4. Did candidate use context managers?
5. Did candidate specify encoding?
6. Did candidate avoid loading huge files unnecessarily?
7. Did candidate separate I/O from transformation?
8. Did candidate return invalid rows with reasons?
9. Did candidate avoid bare except?
10. Did candidate use correct data structures?
11. Did candidate explain dedupe/aggregation keys?
12. Did candidate handle timestamps/numbers safely?
13. Did candidate produce deterministic output?
14. Did candidate discuss idempotency?
15. Did candidate discuss atomic writes/checkpointing if relevant?
16. Did candidate include logging/summary metrics?
17. Did candidate explain complexity?
18. Did candidate mention testing?
19. Did candidate consider PII/security if logging invalids?
20. Did candidate connect script to DE pipeline?
```

Verdict examples:

```text
Works for clean data only.
Good logic but memory-unsafe.
Good transformation but no invalid handling.
Good code but no idempotency.
Good script but untestable structure.
Interview-ready.
Strong.
```


## 92. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Reads whole file unnecessarily | Streaming file drills |
| No validation | Required-field validation drills |
| Silently skips bad rows | Dead-letter drills |
| Bare except | Specific exception handling drills |
| Float for money | Decimal parsing drills |
| Timestamp bugs | UTC datetime parsing drills |
| No dedupe rule | Keep first/last/latest drills |
| Wrong aggregation key | Group-by key drills |
| Nested JSON errors | Safe get_nested drills |
| Memory-heavy grouping | Streaming/aggregation trade-off drills |
| Non-deterministic output | Sorting/tie-breaker drills |
| No idempotency | Atomic write/rerun drills |
| One giant script | Function decomposition drills |
| No tests | Pure function unit-test drills |
| Logs PII | Redaction drills |

If weakness repeats:

```text
Use modes/weakness-repair-mode.md.
```


## 93. Communication Scripts

### File processing script

```text
I would stream the file using a context manager and explicit encoding, parse each row, validate it, transform valid rows, and write invalid rows separately with error reasons.
```

### Validation script

```text
I do not assume source data is clean. I validate required fields and types, and I track invalid rows instead of silently dropping them.
```

### Aggregation script

```text
This is a group-by problem, so I use a dictionary/defaultdict keyed by the grouping field and update the aggregate in one pass.
```

### Deduplication script

```text
First I clarify the dedupe rule: keep first, keep last, or keep latest by timestamp. Then I use a dictionary keyed by the stable ID.
```

### Streaming script

```text
For large files, I process records line by line or in batches so memory usage stays bounded.
```

### Idempotency script

```text
I make the script rerunnable by writing deterministic outputs, using temp files plus atomic rename, and avoiding blind appends.
```

### Production script

```text
For production, I would add logging, summary metrics, invalid-record output, atomic writes, and tests for parsing, validation, transformation, and edge cases.
```


## 94. Candidate Self-Review Questions

After every data scripting problem, candidate should answer:

```text
1. What is the input format?
2. What is the output format?
3. What fields are required?
4. What fields are optional?
5. What validation is needed?
6. What happens to invalid records?
7. Is the file large?
8. Do I need streaming?
9. What is the dedupe/aggregation key?
10. Do I need deterministic output order?
11. How are timestamps parsed?
12. How are numeric values parsed?
13. What should be logged?
14. Is the script idempotent?
15. How would I test this?
16. What is time complexity?
17. What is space complexity?
18. What Data Engineering pipeline does this resemble?
```

If candidate cannot answer these:

```text
The script is not production-ready.
```


## 95. Maintenance Drills

After completing data scripting, maintain skill with:

```text
1 CSV/JSONL drill per week
1 validation/dead-letter drill per week
1 aggregation/dedupe drill per week
1 nested JSON flattening drill every 2 weeks
1 reconciliation/manifest drill every 2 weeks
1 production scripting scenario every month
```

Maintenance rotation:

```text
Week 1: CSV to JSONL + validation
Week 2: aggregation + latest record
Week 3: nested flattening + reconciliation
Week 4: streaming + atomic write + checkpoint
```

If score drops below 4:

```text
Run modes/weakness-repair-mode.md for failed topic.
```


## 96. Progress Tracking Template

Use this progress format.

```text
# Data Scripting Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

File I/O:
CSV:
JSONL:
Log parsing:
Validation:
Dead-letter:
Transformations:
Numeric parsing:
Timestamp parsing:
Aggregation:
Counter:
Deduplication:
Latest record:
Nested JSON flattening:
Exploding arrays:
Reconciliation:
Manifests:
Missing dates:
Atomic writes:
Checkpointing:
Idempotency:
Logging:
CLI args:
Testing:
PII redaction:
Production reasoning:

## Repeated Mistakes

-

## Repair Items

-

## Next Practice

Today:
This week:
Next mock:
```


## 97. Final Exit Test

Candidate passes data scripting when they can solve/explain:

```text
1. Read CSV rows with DictReader.
2. Write CSV with deterministic fieldnames.
3. Read JSONL line by line.
4. Write JSONL.
5. Parse key-value logs.
6. Validate required fields.
7. Split valid and invalid records.
8. Enforce invalid-rate threshold.
9. Parse Decimal money values.
10. Parse timezone-aware timestamps.
11. Aggregate totals by key.
12. Count event frequencies.
13. Keep latest record per ID.
14. Detect duplicate IDs with row numbers.
15. Flatten nested JSON.
16. Explode nested arrays.
17. Convert CSV to clean JSONL.
18. Stream large file processing.
19. Compare two extracts.
20. Generate reconciliation report.
21. Detect missing dates.
22. Build file manifest.
23. Compare manifests.
24. Normalize column names.
25. Detect schema drift.
26. Redact PII.
27. Write output atomically.
28. Checkpoint processed files.
29. Build argparse CLI.
30. Explain tests and production improvements.
```

Passing standard:

```text
Average score >= 4/5.
No silent invalid-row dropping.
No memory-unsafe approach without discussion.
No untestable giant script.
No missing complexity explanation.
Can connect scripting to DE pipeline work.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles production safety, idempotency, PII, schema drift, and large-file trade-offs clearly.
```


## 98. Final Summary

Data scripting is one of the most practical Python skills for Data Engineering interviews.

It maps directly to:

```text
file ingestion
data cleaning
validation
dead-letter handling
aggregation
deduplication
reconciliation
manifest creation
partition checks
log analysis
schema drift detection
one-time backfills
pipeline utility scripts
```

The candidate must master:

```text
pathlib
context managers
csv.DictReader
csv.DictWriter
json/jsonl
safe parsing
validation
dead-letter rows
Counter/defaultdict
deduplication
latest-record logic
timestamp parsing
Decimal numeric parsing
nested JSON flattening
streaming processing
atomic writes
logging
argparse
testing
idempotency
PII-safe handling
```

The mentor must be strict:

```text
No validation → not interview-ready.
Silent bad-row drop → not interview-ready.
Memory unsafe for large files → not interview-ready.
No complexity → not interview-ready.
No production reasoning → not interview-ready.
```

The goal is not to memorize file-reading syntax.

The goal is to write practical, safe, testable Python scripts that can survive real-world dirty data.


## 99. Problem Card Appendix

### Card 1: Read CSV Rows

Category:

```text
CSV
```

Primary pattern:

```text
DictReader
```

Core idea:

```text
Stream rows as dictionaries.
```

Data Engineering connection:

```text
Vendor file ingestion.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Write CSV Rows

Category:

```text
CSV
```

Primary pattern:

```text
DictWriter
```

Core idea:

```text
Write deterministic schema.
```

Data Engineering connection:

```text
Clean export output.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Read JSONL

Category:

```text
JSONL
```

Primary pattern:

```text
Line-by-line parse
```

Core idea:

```text
Handle invalid JSON lines.
```

Data Engineering connection:

```text
Raw event files.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Write JSONL

Category:

```text
JSONL
```

Primary pattern:

```text
One record per line
```

Core idea:

```text
Streamable output.
```

Data Engineering connection:

```text
Raw/invalid landing.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Parse Logs

Category:

```text
Logs
```

Primary pattern:

```text
Key-value parsing
```

Core idea:

```text
Extract level/service/event.
```

Data Engineering connection:

```text
Log summaries.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Validate Transaction

Category:

```text
Validation
```

Primary pattern:

```text
Required fields
```

Core idea:

```text
Return explicit error reasons.
```

Data Engineering connection:

```text
Data quality.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Split Valid Invalid

Category:

```text
Dead-letter
```

Primary pattern:

```text
Separate records
```

Core idea:

```text
Keep raw + errors.
```

Data Engineering connection:

```text
Robust loading.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Top Customers

Category:

```text
Aggregation
```

Primary pattern:

```text
defaultdict
```

Core idea:

```text
Total spend by customer.
```

Data Engineering connection:

```text
Business metrics.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Count Events

Category:

```text
Counting
```

Primary pattern:

```text
Counter
```

Core idea:

```text
Frequency by event type.
```

Data Engineering connection:

```text
Telemetry analysis.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Latest Record

Category:

```text
Deduplication
```

Primary pattern:

```text
Dictionary by id
```

Core idea:

```text
Keep latest updated_at.
```

Data Engineering connection:

```text
Profile sync.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Duplicate IDs

Category:

```text
Data quality
```

Primary pattern:

```text
Counter/defaultdict
```

Core idea:

```text
Detect duplicate keys.
```

Data Engineering connection:

```text
Load validation.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Flatten JSON

Category:

```text
Nested data
```

Primary pattern:

```text
get_nested
```

Core idea:

```text
Extract nested fields.
```

Data Engineering connection:

```text
API/file flattening.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Explode Items

Category:

```text
Nested arrays
```

Primary pattern:

```text
Child rows
```

Core idea:

```text
Create one row per item.
```

Data Engineering connection:

```text
Order line table.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Compare Extracts

Category:

```text
Reconciliation
```

Primary pattern:

```text
set diff
```

Core idea:

```text
Find only-source/target.
```

Data Engineering connection:

```text
Source-target checks.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Missing Dates

Category:

```text
Partitions
```

Primary pattern:

```text
date range + set
```

Core idea:

```text
Find missing partitions.
```

Data Engineering connection:

```text
Daily pipeline audit.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: File Manifest

Category:

```text
File ops
```

Primary pattern:

```text
path.stat
```

Core idea:

```text
Track path/size/mtime.
```

Data Engineering connection:

```text
Ingestion audit.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Schema Drift

Category:

```text
Validation
```

Primary pattern:

```text
expected vs actual fields
```

Core idea:

```text
Report unknown/missing fields.
```

Data Engineering connection:

```text
Source changes.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Atomic Write

Category:

```text
Reliability
```

Primary pattern:

```text
temp then replace
```

Core idea:

```text
Avoid partial output.
```

Data Engineering connection:

```text
Idempotent scripts.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Checkpoint Files

Category:

```text
Resumability
```

Primary pattern:

```text
processed file set
```

Core idea:

```text
Resume after failure.
```

Data Engineering connection:

```text
Batch ingestion.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: PII Redaction

Category:

```text
Security
```

Primary pattern:

```text
field masking
```

Core idea:

```text
Avoid sensitive logs.
```

Data Engineering connection:

```text
Safe dead-letter handling.
```

Candidate must be able to explain:

```text
1. Input and output shape.
2. Validation and error handling.
3. Python implementation.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 100. Data Engineering Custom Scenario Appendix

### Scenario 1: CSV to Clean JSONL

Pattern:

```text
file conversion + validation
```

Task:

```text
Convert raw vendor CSV into clean JSONL and invalid JSONL.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: Streaming Conversion

Pattern:

```text
memory-safe processing
```

Task:

```text
Convert huge file without storing all rows.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: Top Error Services

Pattern:

```text
log parsing + Counter
```

Task:

```text
Summarize ERROR logs by service.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: Latest Profiles

Pattern:

```text
dedupe latest by key
```

Task:

```text
Keep most recent profile per user.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: Orders and Items

Pattern:

```text
flatten + explode
```

Task:

```text
Create parent and child rows.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: Source Target Diff

Pattern:

```text
reconciliation
```

Task:

```text
Compare extracts by primary key.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: Missing Partitions

Pattern:

```text
date range + set
```

Task:

```text
Find missing daily partitions.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: Manifest Diff

Pattern:

```text
file audit
```

Task:

```text
Detect added/removed/changed files.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: Change Detection

Pattern:

```text
row hash
```

Task:

```text
Detect inserts, updates, deletes.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: Schema Drift Report

Pattern:

```text
field validation
```

Task:

```text
Detect unknown/missing fields.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: PII-Safe Dead Letter

Pattern:

```text
redaction
```

Task:

```text
Mask sensitive fields in invalid output.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Checkpointed Processing

Pattern:

```text
resumability
```

Task:

```text
Process files once and resume after failure.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: Argparse Script

Pattern:

```text
CLI design
```

Task:

```text
Make script configurable by input/output paths.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Atomic Output

Pattern:

```text
idempotency
```

Task:

```text
Write temp then replace final output.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: Data Quality Report

Pattern:

```text
metrics
```

Task:

```text
Calculate missing/invalid/duplicate counts.
```

Minimum expected answer:

```text
1. State the input assumptions.
2. State the safe processing design.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production considerations.
```

Passing score:

```text
4/5 or higher.
```


## 101. Drill Appendix

### Drill 1: CSV Drill

Task:

```text
Read CSV, validate rows, write clean and invalid outputs.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: JSONL Drill

Task:

```text
Read JSONL line by line and handle invalid JSON.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Validation Drill

Task:

```text
Create validators with explicit error reasons.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Dead-Letter Drill

Task:

```text
Write invalid records with row number and reasons.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Aggregation Drill

Task:

```text
Compute totals and counts by key.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: Dedup Drill

Task:

```text
Keep first, last, and latest record per ID.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Timestamp Drill

Task:

```text
Parse ISO timestamps and normalize UTC.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Decimal Drill

Task:

```text
Parse money safely and reject invalid amounts.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Nested JSON Drill

Task:

```text
Flatten nested objects and explode arrays.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Reconciliation Drill

Task:

```text
Compare two extracts using sets or sorted scan.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Manifest Drill

Task:

```text
Generate and compare file manifests.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Schema Drift Drill

Task:

```text
Report unknown and missing required fields.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Streaming Drill

Task:

```text
Rewrite in-memory script to streaming script.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Atomic Write Drill

Task:

```text
Write output through temp file and replace.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Checkpoint Drill

Task:

```text
Process files with processed-file checkpoint.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Logging Drill

Task:

```text
Add useful counts and context logs.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: CLI Drill

Task:

```text
Add argparse parameters to script.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Testing Drill

Task:

```text
Write tests for transform, validate, and dedupe functions.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 19: PII Drill

Task:

```text
Redact sensitive fields before logging invalid records.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 20: Full Mock

Task:

```text
Build CSV-to-JSONL ETL with summary and invalid threshold.
```

Minimum passing answer:

```text
1. State input/output.
2. State validation rules.
3. Write clean, testable Python.
4. Handle invalid records.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 102. Quick Reference Cards

### Quick Card 1: File I/O

Summary:

```text
Use pathlib, context managers, and explicit encoding.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 2: CSV read

Summary:

```text
Use csv.DictReader for named columns.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 3: CSV write

Summary:

```text
Use DictWriter with explicit fieldnames.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 4: JSONL

Summary:

```text
One JSON object per line; good for streaming.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 5: Validation

Summary:

```text
Return explicit error reasons.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 6: Dead-letter

Summary:

```text
Store raw record, row number, and errors.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 7: Aggregation

Summary:

```text
Use defaultdict or Counter.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 8: Deduplication

Summary:

```text
Clarify keep first, last, or latest.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 9: Latest record

Summary:

```text
Use id + updated_at with deterministic tie-breaker.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 10: Timestamps

Summary:

```text
Normalize to timezone-aware UTC.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 11: Money

Summary:

```text
Use Decimal instead of float.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 12: Streaming

Summary:

```text
Process row by row for large files.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 13: Atomic write

Summary:

```text
Write temp file then replace.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 14: Idempotency

Summary:

```text
Avoid blind append; write deterministic outputs.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 15: Testing

Summary:

```text
Separate pure functions from file I/O.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```
