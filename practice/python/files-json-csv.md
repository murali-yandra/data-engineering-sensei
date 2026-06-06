# Files, JSON, and CSV Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/python/files-json-csv.md
```

This guide teaches and drills **Python file handling, JSON, JSONL, and CSV processing for Data Engineering interviews**.

This is not a generic Python file-I/O tutorial. It is an interview-focused guide for candidates who need to read raw files, parse structured and semi-structured data, validate records, write deterministic outputs, handle malformed rows, process large files safely, and explain practical production trade-offs.

Files, JSON, and CSV are high-ROI because Data Engineering interviews often ask you to:

- read a CSV file
- write a CSV file
- parse JSON
- process JSONL
- handle invalid JSON lines
- convert CSV to JSONL
- convert JSONL to CSV
- flatten nested JSON
- explode nested arrays
- validate required columns
- handle missing values
- handle malformed CSV rows
- process huge files line by line
- create file manifests
- compare two files
- count rows
- detect duplicate IDs
- detect missing headers
- normalize column names
- write output atomically
- avoid partial files
- avoid memory-heavy scripts
- explain file encodings, delimiters, newlines, and bad data
- design file ingestion pipelines

Use this guide with:

- `docs/python-interview-guide.md`
- `docs/data-engineering-fundamentals.md`
- `docs/etl-elt-pipelines-guide.md`
- `docs/error-handling-playbook.md`
- `docs/assessment-rubric.md`
- `docs/communication-rubric.md`
- `modes/python-drill-mode.md`
- `modes/data-engineering-fundamentals-mode.md`
- `modes/interview-mode.md`
- `modes/review-mode.md`
- `modes/feedback-mode.md`
- `modes/weakness-repair-mode.md`
- `practice/python/data-scripting.md`
- `practice/python/api-processing.md`
- `practice/dsa/hashmaps.md`
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

The purpose of this guide is to make the candidate strong at file, JSON, JSONL, and CSV processing in Python.

The candidate should learn to answer:

```text
How do I read a file safely?
How do I write a file safely?
How do I process a large file without loading all data into memory?
How do I use pathlib?
How do I use context managers?
How do I read CSV with headers?
How do I write CSV with deterministic columns?
How do I handle missing CSV columns?
How do I handle quoted commas?
How do I handle blank lines?
How do I parse JSON?
How do I process JSONL line by line?
How do I handle invalid JSON lines?
How do I flatten nested JSON?
How do I explode arrays into child rows?
How do I convert CSV to JSONL?
How do I convert JSONL to CSV?
How do I validate records?
How do I write invalid rows separately?
How do I create a file manifest?
How do I compare files?
How do I avoid partial output files?
How do I explain memory and complexity?
How does this map to Data Engineering pipelines?
```

A candidate is interview-ready only when they can:

```text
use pathlib correctly
use with-open context managers
set encoding explicitly
read files line by line
read CSV with csv.DictReader
write CSV with csv.DictWriter
read and write JSON
read and write JSONL
handle invalid JSON lines
handle missing or extra CSV columns
validate required fields
split valid and invalid records
flatten nested dictionaries
explode nested arrays
write deterministic output
write output atomically
avoid silent data loss
explain edge cases
explain time and space complexity
connect file handling to ingestion pipelines
```


## 2. Why Files, JSON, and CSV Matter for Data Engineers

File processing is one of the most common Data Engineering tasks.

Real examples:

```text
Read a vendor CSV export.
Read a raw JSON API dump.
Read JSONL events from object storage.
Convert raw CSV to clean JSONL.
Convert nested JSON to warehouse-ready flat rows.
Load CSV files into staging tables.
Validate required file columns.
Detect duplicate records before loading.
Generate file-level metrics.
Build a file manifest for audit.
Compare today's export with yesterday's export.
Find missing daily files.
Handle malformed rows from upstream systems.
Land bad records into a dead-letter file.
Write clean data to partitioned folders.
```

Interviewers test file handling because it reveals practical engineering maturity:

```text
Can the candidate process dirty data?
Can they avoid memory issues?
Can they structure code cleanly?
Can they validate records?
Can they handle file-level edge cases?
Can they write deterministic output?
Can they explain production-safe ingestion?
```

Weak answer:

```text
open file, read all, assume clean data, print result.
```

Strong answer:

```text
Use pathlib, context managers, explicit encoding, streaming reads, csv/json libraries, validation, dead-letter output, atomic writes, and summary metrics.
```


## 3. Core Mental Model

File ingestion usually has this flow:

```text
1. Locate files.
2. Open file safely.
3. Parse records.
4. Validate file-level structure.
5. Validate record-level fields.
6. Transform records.
7. Write valid output.
8. Write invalid output.
9. Produce summary metrics.
10. Close files safely.
```

For production-grade scripts, add:

```text
atomic output writes
idempotency
logging
file manifests
schema checks
bad-row tracking
row counts
deduplication
checkpointing if processing many files
```

Core interview line:

```text
For file processing, correctness is not only reading the file. It is safely parsing, validating, transforming, writing, and preserving enough context to debug bad records.
```


## 4. File Processing Vocabulary

Important terms:

```text
File path:
Location of file on disk or mounted storage.

Directory:
Folder containing files.

Extension:
Suffix such as .csv, .json, .jsonl.

Encoding:
How text bytes are decoded, commonly UTF-8.

Newline:
Line ending representation.

Delimiter:
CSV separator, commonly comma, pipe, or tab.

Header:
First row containing column names.

Record:
One logical row/object/event.

Schema:
Expected columns or JSON fields.

Malformed row:
Row that cannot be parsed or fails expected format.

Dead-letter file:
Output file containing invalid records and error reasons.

Manifest:
File inventory with path, size, modified time, row count, checksum if needed.

Atomic write:
Write to temp file then rename to final path.

Streaming:
Processing data incrementally instead of loading everything.

JSON:
One JSON object/array document.

JSONL:
One JSON object per line.

CSV:
Delimited tabular text file.
```


## 5. Standard Answer Framework

Use this framework for file/JSON/CSV interview answers:

```text
1. Restate input and output.
2. Clarify file format:
   - CSV
   - JSON
   - JSONL
   - text
3. Clarify data size.
4. Clarify schema:
   - required columns
   - optional columns
   - nested fields
5. Clarify invalid-row behavior:
   - skip
   - fail
   - write dead-letter
6. Clarify output:
   - CSV
   - JSON
   - JSONL
   - summary metrics
7. Explain file reading strategy.
8. Explain parsing strategy.
9. Explain validation strategy.
10. Explain transformation strategy.
11. Explain writing strategy.
12. Explain edge cases.
13. Explain time and space complexity.
14. Explain production improvements.
```

Short version:

```text
Input:
Parser:
Validation:
Transform:
Output:
Bad records:
Memory:
Complexity:
Production notes:
```

Strict rule:

```text
No file processing answer is strong if it ignores malformed rows, missing fields, file size, and output safety.
```


## 6. Scoring Rubric

Score each file/JSON/CSV attempt from 0 to 5.

### Score 0

No meaningful file-processing answer.

### Score 1

Reads file or prints data only. No validation, no structure.

### Score 2

Works for clean small files but fails dirty data or large files.

### Score 3

Handles common cases but weak on invalid rows, schema checks, or memory.

### Score 4

Interview-ready. Uses safe file handling, parsing libraries, validation, deterministic output, and complexity explanation.

### Score 5

Strong. Handles malformed records, streaming, atomic writes, idempotency, schema drift, dead-letter files, manifests, logging, and production edge cases.

Do not give 4+ if:

```text
candidate does not use context manager
candidate does not specify encoding
candidate reads huge file into memory without discussion
candidate manually splits CSV by comma instead of csv module
candidate silently drops bad records
candidate does not validate required columns
candidate cannot explain JSON vs JSONL
candidate cannot handle nested JSON safely
candidate writes partial output directly to final path without discussing risk
candidate cannot explain memory complexity
candidate cannot connect to DE ingestion
```


## 7. Python Standard Library Tools

Use these standard library tools first:

```text
pathlib.Path:
Path manipulation and file discovery.

csv:
CSV parsing and writing.

json:
JSON and JSONL parsing/writing.

datetime:
Timestamp parsing and manifest modified times.

collections.Counter:
Counts and frequencies.

collections.defaultdict:
Grouping and aggregations.

hashlib:
File checksums and row hashes.

tempfile:
Temporary files for safe writes.

logging:
Operational logs.

argparse:
Command-line scripts.

itertools:
Iterator utilities.

os:
Some lower-level file operations, but pathlib is preferred.
```

Interview-safe line:

```text
For interview coding, I use standard library tools unless pandas or a distributed framework is explicitly allowed.
```


## 8. Pathlib Basics

Use `pathlib.Path` for path handling.

```python
from pathlib import Path

path = Path("data/raw/input.csv")

print(path.name)        # input.csv
print(path.suffix)      # .csv
print(path.stem)        # input
print(path.parent)      # data/raw
```

Create parent directory:

```python
output_path = Path("data/clean/output.jsonl")
output_path.parent.mkdir(parents=True, exist_ok=True)
```

Check existence:

```python
if not path.exists():
    raise FileNotFoundError(path)
```

Find files:

```python
csv_files = sorted(Path("data/raw").rglob("*.csv"))
```

Interview line:

```text
I use pathlib because it makes path manipulation clearer and more cross-platform than manual string concatenation.
```


## 9. Context Managers

Always use context managers for files.

Good:

```python
from pathlib import Path

with Path("input.txt").open("r", encoding="utf-8") as file:
    for line in file:
        process(line)
```

Why:

```text
file closes automatically
safe if exception occurs
cleaner code
less resource leakage
```

Bad:

```python
file = open("input.txt")
data = file.read()
# forgot close
```

Interview line:

```text
I use `with` so the file handle is closed even if parsing fails.
```


## 10. Encoding and Newline Rules

Always be explicit about encoding for text files.

```python
path.open("r", encoding="utf-8")
```

For CSV, include `newline=""`:

```python
path.open("r", encoding="utf-8", newline="")
```

Why `newline=""` for csv:

```text
It lets the csv module handle newline conventions correctly.
```

Common encodings:

```text
utf-8
utf-8-sig
latin-1
cp1252
```

When to use utf-8-sig:

```text
CSV has UTF-8 BOM at beginning of first header column.
```

Interview line:

```text
I default to UTF-8 and handle BOM or vendor-specific encodings explicitly when needed.
```


## 11. Reading Text Files Line by Line

For large text files, read line by line.

```python
from pathlib import Path

def read_non_empty_lines(path):
    path = Path(path)

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            yield line_number, line
```

Why:

```text
bounded memory
can track line numbers
can skip blank lines
can write invalid-line context
```

Avoid for huge files:

```python
lines = file.readlines()
```

Interview line:

```text
For large files, I stream records and keep only necessary state in memory.
```


## 12. Writing Text Files

Write text safely:

```python
from pathlib import Path

def write_lines(path, lines):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            file.write("\n")
```

Append mode:

```python
def append_lines(path, lines):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            file.write("\n")
```

Caution:

```text
Append mode can create duplicate output if a script is rerun.
Use append only when intentionally building a log-like file.
```

Interview line:

```text
For deterministic pipeline outputs, I usually overwrite a temp file and atomically replace the final file instead of blindly appending.
```


## 13. CSV Basics

CSV means comma-separated values, but real CSV can include:

```text
quoted commas
escaped quotes
blank fields
newlines inside quoted values
different delimiters
BOM in header
missing columns
extra columns
```

Do not parse CSV with:

```python
line.split(",")
```

Why:

```text
It fails on quoted commas and escaped values.
```

Use:

```python
import csv
```

Interview line:

```text
I use Python's csv module instead of manual splitting because CSV has quoting and escaping rules.
```


## 14. Reading CSV with DictReader

Use `csv.DictReader`.

```python
import csv
from pathlib import Path

def read_csv_rows(path):
    path = Path(path)

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            row["_row_number"] = row_number
            yield row
```

Why start at 2:

```text
line 1 is header
first data row is line 2
```

Benefits:

```text
column names are explicit
validation is easier
less fragile than positional indexes
```

Interview line:

```text
I preserve row numbers so invalid records can be traced back to the source file.
```


## 15. Validating CSV Headers

Validate required columns before processing.

```python
def validate_csv_headers(actual_headers, required_headers):
    actual = set(actual_headers or [])
    required = set(required_headers)

    missing = sorted(required - actual)

    if missing:
        raise ValueError(f"Missing required CSV columns: {missing}")
```

Reader with header validation:

```python
def read_csv_rows_with_required_headers(path, required_headers):
    path = Path(path)

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        validate_csv_headers(reader.fieldnames, required_headers)

        for row_number, row in enumerate(reader, start=2):
            row["_row_number"] = row_number
            yield row
```

Interview line:

```text
I validate headers before processing because missing columns usually indicate schema drift or wrong input file.
```


## 16. Handling Extra CSV Columns

Extra CSV columns may be acceptable or dangerous depending on the use case.

Options:

```text
ignore extra columns
include extra columns in raw output
alert/report unknown columns
fail if unknown columns exist
```

Detect unknown columns:

```python
def detect_unknown_columns(actual_headers, expected_headers):
    actual = set(actual_headers or [])
    expected = set(expected_headers)
    return sorted(actual - expected)
```

Strict schema validation:

```python
def validate_csv_schema(actual_headers, required_headers, allowed_headers):
    validate_csv_headers(actual_headers, required_headers)

    unknown = detect_unknown_columns(actual_headers, allowed_headers)

    if unknown:
        raise ValueError(f"Unknown CSV columns: {unknown}")
```

Interview line:

```text
For ingestion, I usually fail or alert on missing required columns, and I either tolerate or report extra columns depending on schema contract.
```


## 17. Writing CSV with DictWriter

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

Why explicit fieldnames:

```text
deterministic output schema
deterministic column order
extra fields do not accidentally leak
```

Handling extra fields:

```python
writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
```

Interview line:

```text
I explicitly define output fieldnames so downstream systems receive a stable schema.
```


## 18. CSV Dialects and Delimiters

Not all CSV files use commas.

Examples:

```text
comma: ,
pipe: |
tab: \t
semicolon: ;
```

Read pipe-delimited file:

```python
reader = csv.DictReader(file, delimiter="|")
```

Read tab-delimited file:

```python
reader = csv.DictReader(file, delimiter="\t")
```

CSV sniffer:

```python
def sniff_dialect(sample):
    return csv.Sniffer().sniff(sample)
```

Caution:

```text
Sniffer can be wrong on small or messy samples.
For production, prefer explicit delimiter from source contract.
```

Interview line:

```text
I would not assume comma delimiter if the source contract says pipe or tab-delimited.
```


## 19. CSV Missing Values

CSV missing values are usually empty strings.

Example:

```csv
id,amount,currency
1,100,INR
2,,USD
```

Normalize empty strings:

```python
def normalize_empty_strings(row):
    return {
        key: (None if value == "" else value)
        for key, value in row.items()
    }
```

Use:

```python
row = normalize_empty_strings(row)
```

Interview line:

```text
I normalize empty strings to None before validation so missing values are handled consistently.
```


## 20. CSV Row-Level Validation

Example transaction validation:

```python
from decimal import Decimal, InvalidOperation

def parse_decimal(value):
    if value in (None, ""):
        return None

    try:
        return Decimal(str(value))
    except InvalidOperation:
        return None

def transform_csv_transaction(raw):
    row = normalize_empty_strings(raw)

    return {
        "transaction_id": row.get("id"),
        "customer_id": row.get("customer_id"),
        "amount": parse_decimal(row.get("amount")),
        "currency": row.get("currency"),
        "created_at": row.get("created_at"),
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
```

Interview line:

```text
Parsing and validation are separate: parsing converts types, validation decides whether the row is acceptable.
```


## 21. CSV Bad Records Pattern

Split valid and invalid CSV rows.

```python
def process_csv_with_invalids(input_path, required_headers):
    valid = []
    invalid = []

    for raw in read_csv_rows_with_required_headers(input_path, required_headers):
        row_number = raw.pop("_row_number", None)

        try:
            row = transform_csv_transaction(raw)
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

    return valid, invalid
```

Interview line:

```text
I do not silently skip bad rows; I preserve row number, raw row, and error reasons.
```


## 22. JSON Basics

JSON can represent:

```text
object/dict
array/list
string
number
boolean
null
nested objects
nested arrays
```

Read JSON file:

```python
import json
from pathlib import Path

def read_json(path):
    path = Path(path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
```

Write JSON file:

```python
def write_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2, sort_keys=True)
```

Interview line:

```text
JSON files are not always stream-friendly if they contain one giant array; JSONL is better for large record streams.
```


## 23. JSON Shape Validation

Validate JSON shape before processing.

Example expected shape:

```json
{
  "data": [
    {"id": "1"},
    {"id": "2"}
  ]
}
```

Validator:

```python
def extract_data_list(payload):
    if not isinstance(payload, dict):
        raise ValueError("Expected top-level JSON object")

    records = payload.get("data")

    if not isinstance(records, list):
        raise ValueError("Expected 'data' to be a list")

    return records
```

Why:

```text
API/error/export files can have unexpected shape.
```

Interview line:

```text
I validate the top-level JSON shape before assuming where records live.
```


## 24. JSON Decode Errors

Handle invalid JSON file:

```python
import json

def read_json_safe(path):
    try:
        return read_json(path)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON file: {path}; error={exc}") from exc
```

Common causes:

```text
trailing comma
single quotes
unescaped characters
partial file
HTML error page saved as .json
multiple JSON objects without array
```

Interview line:

```text
Invalid JSON is a file-level failure for normal JSON, but for JSONL I can often isolate the bad line and continue.
```


## 25. JSONL Basics

JSONL means one JSON object per line.

Example:

```json
{"id": 1, "event": "login"}
{"id": 2, "event": "purchase"}
```

Benefits:

```text
streamable
append-friendly
one bad line can be isolated
good for logs/events
common raw landing format
easy to split/compress
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

            yield line_number, json.loads(line)
```

Interview line:

```text
For large record datasets, JSONL is often more practical than one giant JSON array because it supports streaming.
```


## 26. Reading JSONL Safely

Safe JSONL reader that does not crash on one bad line:

```python
import json
from pathlib import Path

def read_jsonl_with_invalids(path):
    path = Path(path)

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            raw_line = line.rstrip("\n")

            if not raw_line.strip():
                continue

            try:
                record = json.loads(raw_line)
            except json.JSONDecodeError as exc:
                yield {
                    "_invalid": True,
                    "_line_number": line_number,
                    "_raw": raw_line,
                    "_errors": [f"json_decode_error:{exc}"],
                }
                continue

            yield {
                "_invalid": False,
                "_line_number": line_number,
                "record": record,
            }
```

Interview line:

```text
For JSONL, I can treat malformed lines as record-level invalids and continue, while capturing line number and raw content.
```


## 27. Writing JSONL

Write JSONL:

```python
import json
from pathlib import Path

def write_jsonl(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, default=str))
            file.write("\n")
```

Append JSONL:

```python
def append_jsonl(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, default=str))
            file.write("\n")
```

Caution:

```text
Append mode can create duplicates on rerun.
```

Interview line:

```text
I write one JSON object per line and use default=str only when I intentionally accept string conversion for non-JSON-native types like Decimal or datetime.
```


## 28. JSON vs JSONL Decision Table

| Requirement | Prefer |
|---|---|
| Small config file | JSON |
| One object with metadata | JSON |
| Large event dataset | JSONL |
| Append records over time | JSONL |
| Isolate malformed record | JSONL |
| Human-readable nested object | JSON |
| Stream processing | JSONL |
| Raw landing for records | JSONL |
| API response saved as-is | JSON |
| Logs/events | JSONL |

Interview line:

```text
JSON is good for small structured documents, while JSONL is better for large record streams and raw event landing.
```


## 29. Safe Nested JSON Access

Nested JSON can have missing objects.

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

Usage:

```python
customer_id = get_nested(order, ["customer", "id"])
country = get_nested(order, ["shipping_address", "country"])
```

Why:

```text
record["customer"]["id"] fails if customer is missing or null.
```

Interview line:

```text
I use safe nested access for raw JSON because optional nested objects are common in real data.
```


## 30. Flattening Nested JSON

Example input:

```json
{
  "id": "o1",
  "customer": {
    "id": "c1",
    "email": "a@example.com"
  },
  "shipping": {
    "country": "IN"
  }
}
```

Flatten:

```python
def flatten_order(order):
    return {
        "order_id": order.get("id"),
        "customer_id": get_nested(order, ["customer", "id"]),
        "customer_email": get_nested(order, ["customer", "email"]),
        "shipping_country": get_nested(order, ["shipping", "country"]),
    }
```

Validation after flattening:

```python
def validate_order(row):
    errors = []

    if not row.get("order_id"):
        errors.append("missing_order_id")

    if not row.get("customer_id"):
        errors.append("missing_customer_id")

    return errors
```

Interview line:

```text
I flatten nested JSON into explicit output columns, then validate the flattened record.
```


## 31. Exploding Nested Arrays

Nested arrays usually become child rows.

Input:

```json
{
  "id": "order_1",
  "items": [
    {"sku": "A", "quantity": 2},
    {"sku": "B", "quantity": 1}
  ]
}
```

Explode:

```python
def explode_order_items(order):
    order_id = order.get("id")
    items = order.get("items") or []

    rows = []

    for index, item in enumerate(items):
        rows.append({
            "order_id": order_id,
            "line_number": index + 1,
            "sku": item.get("sku"),
            "quantity": item.get("quantity"),
        })

    return rows
```

Why line_number:

```text
preserves item order
can help form stable child key
```

Interview line:

```text
For nested arrays, I create a child dataset with parent_id and line_number instead of forcing arrays into one flat row.
```


## 32. Recursive Dictionary Flattening

Generic flatten function:

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

Example:

```python
flatten_dict({"a": {"b": 1}, "c": 2})
# {"a_b": 1, "c": 2}
```

Caution:

```text
Generic flattening can produce unstable schemas.
Nested arrays need special handling.
Explicit flattening is usually better for production tables.
```

Interview line:

```text
Generic flattening is useful for exploration, but for warehouse tables I prefer explicit mappings and validation.
```


## 33. CSV to JSONL Conversion

Problem:

```text
Convert CSV rows to JSONL records.
```

Code:

```python
def csv_to_jsonl(input_csv_path, output_jsonl_path, required_headers):
    count = 0

    rows = read_csv_rows_with_required_headers(input_csv_path, required_headers)

    output_path = Path(output_jsonl_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as output_file:
        for raw in rows:
            row_number = raw.pop("_row_number", None)
            row = normalize_empty_strings(raw)
            row["_source_row_number"] = row_number

            output_file.write(json.dumps(row, ensure_ascii=False, default=str))
            output_file.write("\n")
            count += 1

    return {"records_written": count}
```

Interview line:

```text
CSV to JSONL conversion is straightforward, but I still validate headers and preserve row number for traceability.
```


## 34. CSV to Clean JSONL with Invalid Output

More realistic conversion:

```python
def csv_to_clean_jsonl(input_csv_path, clean_jsonl_path, invalid_jsonl_path, required_headers):
    valid_count = 0
    invalid_count = 0

    clean_path = Path(clean_jsonl_path)
    invalid_path = Path(invalid_jsonl_path)
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    invalid_path.parent.mkdir(parents=True, exist_ok=True)

    with clean_path.open("w", encoding="utf-8") as clean_file, invalid_path.open("w", encoding="utf-8") as invalid_file:
        for raw in read_csv_rows_with_required_headers(input_csv_path, required_headers):
            row_number = raw.pop("_row_number", None)

            try:
                row = transform_csv_transaction(raw)
                errors = validate_transaction(row)
            except Exception as exc:
                invalid = {
                    "row_number": row_number,
                    "raw": raw,
                    "errors": [f"transform_error:{exc}"],
                }
                invalid_file.write(json.dumps(invalid, ensure_ascii=False, default=str) + "\n")
                invalid_count += 1
                continue

            if errors:
                invalid = {
                    "row_number": row_number,
                    "raw": raw,
                    "row": row,
                    "errors": errors,
                }
                invalid_file.write(json.dumps(invalid, ensure_ascii=False, default=str) + "\n")
                invalid_count += 1
            else:
                clean_file.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
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
This streaming version is memory-safe and preserves bad rows for debugging.
```


## 35. JSONL to CSV Conversion

Problem:

```text
Convert JSONL records to CSV with fixed columns.
```

Code:

```python
def jsonl_to_csv(input_jsonl_path, output_csv_path, fieldnames):
    output_path = Path(output_csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    invalid_count = 0

    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()

        for item in read_jsonl_with_invalids(input_jsonl_path):
            if item["_invalid"]:
                invalid_count += 1
                continue

            record = item["record"]
            writer.writerow({
                field: record.get(field)
                for field in fieldnames
            })
            count += 1

    return {
        "records_written": count,
        "invalid_count": invalid_count,
    }
```

Interview line:

```text
When converting JSONL to CSV, I project to fixed fieldnames so the CSV schema is stable.
```


## 36. JSON Array to JSONL

Problem:

```text
Convert a JSON file containing an array of records into JSONL.
```

Code:

```python
def json_array_to_jsonl(input_json_path, output_jsonl_path):
    payload = read_json(input_json_path)

    if not isinstance(payload, list):
        raise ValueError("Expected JSON array")

    write_jsonl(output_jsonl_path, payload)

    return {"records_written": len(payload)}
```

Caution:

```text
This loads the entire JSON array into memory.
For huge files, prefer source JSONL or streaming parser.
```

Interview line:

```text
A giant JSON array is not memory-friendly with standard json.load; JSONL is preferred for large data.
```


## 37. JSON Object Data Field to JSONL

Problem:

```text
Input JSON:
{
  "data": [records],
  "metadata": {...}
}
Write data records to JSONL.
```

Code:

```python
def json_data_field_to_jsonl(input_json_path, output_jsonl_path):
    payload = read_json(input_json_path)
    records = extract_data_list(payload)
    write_jsonl(output_jsonl_path, records)

    return {"records_written": len(records)}
```

Interview point:

```text
Always validate where the records live in the JSON structure.
```


## 38. File Manifest Basics

A file manifest records metadata about files.

Common fields:

```text
path
file_name
extension
size_bytes
modified_time
row_count
checksum
```

Basic manifest:

```python
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
            "file_name": path.name,
            "extension": path.suffix,
            "size_bytes": stat.st_size,
            "modified_time": datetime.fromtimestamp(
                stat.st_mtime,
                tz=timezone.utc,
            ).isoformat(),
        })

    return manifest
```

Interview line:

```text
A manifest helps audit what files were processed and detect missing or changed files.
```


## 39. Counting File Rows

Count rows by file type.

Text line count:

```python
def count_lines(path):
    count = 0

    with Path(path).open("r", encoding="utf-8") as file:
        for _ in file:
            count += 1

    return count
```

CSV data row count:

```python
def count_csv_data_rows(path):
    count = 0

    with Path(path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for _ in reader:
            count += 1

    return count
```

JSONL valid/invalid count:

```python
def count_jsonl_records(path):
    valid = 0
    invalid = 0

    for item in read_jsonl_with_invalids(path):
        if item["_invalid"]:
            invalid += 1
        else:
            valid += 1

    return {
        "valid": valid,
        "invalid": invalid,
    }
```

Interview line:

```text
Row counts are basic but important ingestion audit metrics.
```


## 40. File Checksums

Checksums help detect file changes.

```python
import hashlib

def file_sha256(path, chunk_size=1024 * 1024):
    path = Path(path)
    digest = hashlib.sha256()

    with path.open("rb") as file:
        while True:
            chunk = file.read(chunk_size)

            if not chunk:
                break

            digest.update(chunk)

    return digest.hexdigest()
```

Why read binary chunks:

```text
works for any file type
bounded memory
consistent hash
```

Use cases:

```text
detect duplicate files
detect changed files
audit file delivery
verify downloads
```

Interview line:

```text
For large files, I compute checksum in chunks so memory usage stays bounded.
```


## 41. Enhanced File Manifest

Manifest with row counts and checksum:

```python
def build_enhanced_manifest(base_dir, pattern="*"):
    rows = []

    for path in sorted(Path(base_dir).rglob(pattern)):
        if not path.is_file():
            continue

        stat = path.stat()
        row = {
            "path": str(path),
            "file_name": path.name,
            "extension": path.suffix,
            "size_bytes": stat.st_size,
            "sha256": file_sha256(path),
        }

        if path.suffix.lower() == ".csv":
            row["record_count"] = count_csv_data_rows(path)
        elif path.suffix.lower() == ".jsonl":
            counts = count_jsonl_records(path)
            row["valid_jsonl_records"] = counts["valid"]
            row["invalid_jsonl_records"] = counts["invalid"]
        else:
            row["line_count"] = count_lines(path)

        rows.append(row)

    return rows
```

Caution:

```text
Checksums and row counts require reading full files, which can be expensive for huge datasets.
```

Interview line:

```text
I balance manifest detail against runtime cost; checksums are useful but expensive for very large files.
```


## 42. Comparing File Manifests

Compare old and new manifests.

```python
def compare_file_manifests(old_manifest, new_manifest):
    old_by_path = {row["path"]: row for row in old_manifest}
    new_by_path = {row["path"]: row for row in new_manifest}

    old_paths = set(old_by_path)
    new_paths = set(new_by_path)

    added = sorted(new_paths - old_paths)
    removed = sorted(old_paths - new_paths)
    changed = []

    for path in sorted(old_paths & new_paths):
        old = old_by_path[path]
        new = new_by_path[path]

        if (
            old.get("size_bytes") != new.get("size_bytes")
            or old.get("sha256") != new.get("sha256")
        ):
            changed.append(path)

    return {
        "added": added,
        "removed": removed,
        "changed": changed,
    }
```

Interview line:

```text
Manifest comparison is useful for detecting late file changes, missing deliveries, and duplicate processing risk.
```


## 43. Atomic File Writes

Atomic write pattern:

```text
write temp file
close temp file
replace final file
```

JSON atomic write:

```python
def atomic_write_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_suffix(path.suffix + ".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2, sort_keys=True, default=str)

    temp_path.replace(path)
```

Text atomic write:

```python
def atomic_write_text(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_suffix(path.suffix + ".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        file.write(text)

    temp_path.replace(path)
```

Interview line:

```text
Atomic writes prevent downstream consumers from reading half-written files.
```


## 44. Atomic CSV Write

Atomic CSV write:

```python
def atomic_write_csv(path, rows, fieldnames):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_suffix(path.suffix + ".tmp")

    with temp_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()

        for row in rows:
            writer.writerow(row)

    temp_path.replace(path)
```

Caution:

```text
If writing huge output, keep rows as an iterable/generator instead of materializing all rows.
```

Interview line:

```text
I can combine streaming output with atomic replace by writing to a temp file first.
```


## 45. Atomic JSONL Write

Atomic JSONL write:

```python
def atomic_write_jsonl(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_suffix(path.suffix + ".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, default=str))
            file.write("\n")

    temp_path.replace(path)
```

Interview line:

```text
For idempotent file outputs, I write the full output to a temporary file and replace final output only after successful completion.
```


## 46. Idempotency for File Scripts

Idempotent file script strategies:

```text
write deterministic output path
overwrite output atomically
avoid blind append
include run metadata separately
deduplicate by stable key
write one partition per run/date
use manifest to track processed files
checkpoint only after successful output
```

Bad:

```text
open output in append mode every run without dedupe
```

Good:

```text
write output/date=2026-01-01/data.jsonl.tmp
then replace output/date=2026-01-01/data.jsonl
```

Interview line:

```text
A file script should be safe to rerun after failure without producing duplicate or partial output.
```


## 47. File Discovery

Find files by pattern:

```python
def find_files(base_dir, pattern):
    return sorted(
        path for path in Path(base_dir).rglob(pattern)
        if path.is_file()
    )
```

Examples:

```python
csv_files = find_files("data/raw", "*.csv")
jsonl_files = find_files("data/raw", "*.jsonl")
all_files = find_files("data/raw", "*")
```

Filter by modified time:

```python
def find_files_modified_after(base_dir, pattern, cutoff_timestamp):
    result = []

    for path in find_files(base_dir, pattern):
        if path.stat().st_mtime > cutoff_timestamp:
            result.append(path)

    return result
```

Interview line:

```text
File discovery should be deterministic, so I sort file paths before processing.
```


## 48. Processing Multiple Files

Process files one by one.

```python
def process_files(paths, process_one_file):
    summaries = []

    for path in sorted(paths):
        summary = process_one_file(path)
        summaries.append({
            "path": str(path),
            **summary,
        })

    return summaries
```

Why sorted:

```text
deterministic processing order
easier debugging
stable output
```

Interview line:

```text
When processing many files, I return per-file summaries so one bad file can be isolated.
```


## 49. Checkpoint Processed Files

Checkpoint processed files.

```python
def load_processed_files(checkpoint_path):
    path = Path(checkpoint_path)

    if not path.exists():
        return set()

    payload = read_json(path)
    return set(payload.get("processed_files", []))

def save_processed_files(checkpoint_path, processed_files):
    atomic_write_json(checkpoint_path, {
        "processed_files": sorted(processed_files),
    })

def process_files_with_checkpoint(input_paths, checkpoint_path, process_one_file):
    processed = load_processed_files(checkpoint_path)
    summaries = []

    for path in sorted(input_paths):
        path_str = str(path)

        if path_str in processed:
            continue

        summary = process_one_file(path)
        summaries.append({"path": path_str, **summary})

        processed.add(path_str)
        save_processed_files(checkpoint_path, processed)

    return summaries
```

Important:

```text
Save checkpoint after successful processing, not before.
```

Interview line:

```text
Checkpointing makes multi-file processing resumable after partial failure.
```


## 50. Handling Repeated CSV Headers

Vendor files sometimes repeat headers in the middle.

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
Known vendor file quirks should be handled explicitly and documented, not accidentally ignored.
```


## 51. Handling Footer Rows

Vendor files may contain footer rows.

Example:

```csv
id,amount
1,100
2,200
TOTAL,300
```

Footer detector:

```python
def is_footer_row(row):
    values = list(row.values())

    if not values:
        return False

    first_value = values[0]

    if first_value is None:
        return False

    return str(first_value).strip().upper() in {"TOTAL", "END", "EOF"}
```

Usage:

```python
for row in read_csv_rows(path):
    if is_footer_row(row):
        continue

    process(row)
```

Interview line:

```text
Footer rows are file-level metadata, not data records, so I detect and handle them separately.
```


## 52. Handling BOM in CSV Headers

Sometimes first header includes BOM:

```text
\ufeffid
```

Use encoding:

```python
path.open("r", encoding="utf-8-sig", newline="")
```

Reader:

```python
def read_csv_rows_utf8_sig(path):
    with Path(path).open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            row["_row_number"] = row_number
            yield row
```

Interview line:

```text
If the first column name looks wrong, I check for UTF-8 BOM and use utf-8-sig.
```


## 53. Normalizing Column Names

Normalize column names.

```python
import re

def normalize_column_name(name):
    name = name.strip()
    name = re.sub(r"[^0-9a-zA-Z]+", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_").lower()
```

Normalize row keys:

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

Interview line:

```text
I normalize column names carefully and detect collisions so two original columns do not collapse into one silently.
```


## 54. Projecting Records to Fixed Schema

Project record to fixed fieldnames.

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
stable output schema
ignore unexpected fields intentionally
missing fields become None
```

Interview line:

```text
Projection helps keep output schema deterministic even when raw input has extra fields.
```


## 55. Schema Drift Report

Detect unknown and missing fields.

```python
from collections import Counter

def schema_drift_report(records, expected_fields, required_fields):
    expected = set(expected_fields)
    required = set(required_fields)

    unknown_counts = Counter()
    missing_required_counts = Counter()

    for record in records:
        actual = set(record.keys())

        for field in actual - expected:
            unknown_counts[field] += 1

        for field in required:
            if field not in record or record.get(field) in (None, ""):
                missing_required_counts[field] += 1

    return {
        "unknown_fields": dict(unknown_counts),
        "missing_required": dict(missing_required_counts),
    }
```

Interview line:

```text
Schema drift should be reported through metrics or alerts, not discovered only after downstream queries fail.
```


## 56. Comparing Two CSV Files by ID

Compare IDs in two CSV files.

```python
def read_id_set_from_csv(path, id_column="id"):
    ids = set()

    for row in read_csv_rows(path):
        record_id = row.get(id_column)

        if record_id:
            ids.add(record_id)

    return ids

def compare_csv_ids(source_csv, target_csv, id_column="id"):
    source_ids = read_id_set_from_csv(source_csv, id_column)
    target_ids = read_id_set_from_csv(target_csv, id_column)

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
For huge sorted files, use a streaming two-pointer comparison.
```

Interview line:

```text
Set-based comparison is simple and fast, but memory-heavy for very large files.
```


## 57. Streaming Sorted CSV Comparison

If two CSV files are sorted by ID, compare without storing all IDs.

```python
def iter_sorted_ids_from_csv(path, id_column="id"):
    for row in read_csv_rows(path):
        record_id = row.get(id_column)

        if record_id:
            yield record_id

def compare_sorted_csv_ids(source_csv, target_csv, id_column="id"):
    source_iter = iter(iter_sorted_ids_from_csv(source_csv, id_column))
    target_iter = iter(iter_sorted_ids_from_csv(target_csv, id_column))

    source_id = next(source_iter, None)
    target_id = next(target_iter, None)

    only_source = []
    only_target = []
    both = []

    while source_id is not None and target_id is not None:
        if source_id == target_id:
            both.append(source_id)
            source_id = next(source_iter, None)
            target_id = next(target_iter, None)
        elif source_id < target_id:
            only_source.append(source_id)
            source_id = next(source_iter, None)
        else:
            only_target.append(target_id)
            target_id = next(target_iter, None)

    while source_id is not None:
        only_source.append(source_id)
        source_id = next(source_iter, None)

    while target_id is not None:
        only_target.append(target_id)
        target_id = next(target_iter, None)

    return {
        "only_in_source": only_source,
        "only_in_target": only_target,
        "in_both": both,
    }
```

Complexity:

```text
Time: O(n + m)
Space: O(output)
```

Interview line:

```text
If both files are sorted, a streaming two-pointer comparison avoids loading all IDs into memory.
```


## 58. Row Hashes for Change Detection

Generate stable row hash.

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
detect changed rows
dedupe when no updated_at exists
compare extracts
audit transformations
```

Interview line:

```text
A stable hash over normalized selected fields can detect changes, but a natural key is still needed to identify the row.
```


## 59. Detect Inserts, Updates, Deletes Between JSONL Files

Problem:

```text
Compare old and new JSONL records by id.
Detect inserts, updates, deletes.
```

Code:

```python
def load_jsonl_by_key(path, key_field):
    by_key = {}

    for item in read_jsonl_with_invalids(path):
        if item["_invalid"]:
            continue

        record = item["record"]
        key = record.get(key_field)

        if key:
            by_key[key] = record

    return by_key

def detect_jsonl_changes(old_path, new_path, key_field, compare_fields):
    old_by_key = load_jsonl_by_key(old_path, key_field)
    new_by_key = load_jsonl_by_key(new_path, key_field)

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

Complexity:

```text
Time: O(n + m)
Space: O(n + m)
```

Interview line:

```text
This is a simplified file-based CDC/change-detection pattern.
```


## 60. Redacting Sensitive Fields

Do not blindly write sensitive raw records to invalid files.

```python
PII_FIELDS = {"email", "phone", "ssn", "address", "name"}

def redact_record(record):
    redacted = {}

    for key, value in record.items():
        if key.lower() in PII_FIELDS:
            redacted[key] = "***REDACTED***"
        else:
            redacted[key] = value

    return redacted
```

Recursive version:

```python
def redact_nested(value):
    if isinstance(value, dict):
        result = {}

        for key, child in value.items():
            if key.lower() in PII_FIELDS:
                result[key] = "***REDACTED***"
            else:
                result[key] = redact_nested(child)

        return result

    if isinstance(value, list):
        return [redact_nested(item) for item in value]

    return value
```

Interview line:

```text
Bad-record handling must still respect privacy and logging rules.
```


## 61. Logging for File Scripts

Use logging for file scripts.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)
```

Example:

```python
def log_summary(summary):
    logger.info(
        "file_processing_summary valid=%s invalid=%s output=%s",
        summary.get("valid_count"),
        summary.get("invalid_count"),
        summary.get("output_path"),
    )
```

Useful metrics:

```text
input_file
output_file
rows_read
rows_written
invalid_rows
duplicate_rows
start_time
end_time
duration
schema_errors
json_decode_errors
```

Avoid logging:

```text
secrets
full PII records
huge payloads
```

Interview line:

```text
I log counts and context, not sensitive raw data.
```


## 62. Command-Line File Script

Use argparse for script inputs.

```python
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--invalid-output")
    parser.add_argument("--format", choices=["csv", "json", "jsonl"], required=True)
    return parser.parse_args()
```

Main pattern:

```python
def main():
    args = parse_args()

    if args.format == "csv":
        summary = process_csv_file(args.input, args.output, args.invalid_output)
    elif args.format == "jsonl":
        summary = process_jsonl_file(args.input, args.output, args.invalid_output)
    else:
        summary = process_json_file(args.input, args.output)

    log_summary(summary)

if __name__ == "__main__":
    main()
```

Interview line:

```text
Using argparse makes the script reusable across environments without changing code.
```


## 63. Testing File Logic

Keep pure functions testable.

Test transformation without files:

```python
def test_transform_csv_transaction():
    raw = {
        "id": "t1",
        "customer_id": "c1",
        "amount": "100.50",
        "currency": "inr",
        "created_at": "2026-01-01T00:00:00Z",
    }

    row = transform_csv_transaction(raw)

    assert row["transaction_id"] == "t1"
    assert str(row["amount"]) == "100.50"
```

Test JSONL reader using temp files:

```python
def test_read_jsonl_with_invalids(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text('{"id": 1}\ninvalid\n', encoding="utf-8")

    rows = list(read_jsonl_with_invalids(path))

    assert rows[0]["_invalid"] is False
    assert rows[1]["_invalid"] is True
```

Interview line:

```text
I isolate parsing, transformation, and validation so most behavior can be tested with small fixtures.
```


## 64. Common File Edge Cases

File-level edge cases:

```text
file missing
empty file
empty directory
permission denied
invalid path
wrong extension
wrong encoding
UTF-8 BOM
huge file
partial file
duplicate file
file delivered twice
file still being written
header missing
header repeated in body
footer row
different delimiter
quoted commas
blank lines
extra columns
missing columns
duplicate column names
invalid JSON
invalid JSONL line
nested object missing
array where object expected
object where list expected
```

Data Engineering edge cases:

```text
late file arrival
same file name with changed content
daily partition missing
source sends corrected file
upstream schema drift
bad rows exceed threshold
PII in invalid output
multiple writers to same output path
rerun after partial failure
```


## 65. Common Mistakes

Common mistakes:

```text
using open without with
not specifying encoding
using line.split(",") for CSV
loading huge file into memory
assuming headers exist
assuming all rows are clean
silently skipping invalid rows
using bare except
not preserving row numbers
not writing invalid records
not validating JSON shape
not distinguishing JSON and JSONL
not handling nested missing fields
writing output directly to final path without atomicity
using append mode accidentally
not sorting files before processing
not explaining memory complexity
not testing with malformed input
```

Strict feedback:

```text
This is not interview-ready. You manually split CSV by comma and silently skip bad rows, so the script will fail on real vendor files and hide data-quality issues.
```


## 66. Coding Problem: Count Rows in CSV

Problem:

```text
Given a CSV file with header, count data rows.
```

Solution:

```python
def count_csv_rows(path):
    count = 0

    with Path(path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for _ in reader:
            count += 1

    return count
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Follow-up:

```text
What if the file has repeated header rows or footer rows?
```

Expected:

```text
Skip known non-data rows explicitly.
```


## 67. Coding Problem: Validate CSV Required Columns

Problem:

```text
Given CSV path and required columns, return missing columns.
```

Solution:

```python
def missing_csv_columns(path, required_columns):
    with Path(path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        headers = set(reader.fieldnames or [])

    return sorted(set(required_columns) - headers)
```

Complexity:

```text
Time: O(h), where h is number of headers
Space: O(h)
```

Interview line:

```text
Header validation should happen before row processing.
```


## 68. Coding Problem: Read CSV and Normalize Headers

Problem:

```text
Read CSV and normalize headers to snake_case.
```

Solution:

```python
def read_csv_with_normalized_headers(path):
    with Path(path).open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV missing header")

        normalized_headers = [normalize_column_name(name) for name in reader.fieldnames]

        if len(set(normalized_headers)) != len(normalized_headers):
            raise ValueError("Header collision after normalization")

        for row_number, row in enumerate(reader, start=2):
            normalized_row = {}

            for original, normalized in zip(reader.fieldnames, normalized_headers):
                normalized_row[normalized] = row.get(original)

            normalized_row["_row_number"] = row_number
            yield normalized_row
```

Interview line:

```text
Header normalization must detect collisions to avoid silent data loss.
```


## 69. Coding Problem: CSV Summary Report

Problem:

```text
Return total rows, missing id count, duplicate id count.
```

Solution:

```python
from collections import Counter

def csv_id_quality_report(path, id_column="id"):
    total_rows = 0
    missing_id_count = 0
    id_counts = Counter()

    for row in read_csv_rows(path):
        total_rows += 1
        record_id = row.get(id_column)

        if not record_id:
            missing_id_count += 1
        else:
            id_counts[record_id] += 1

    duplicate_id_count = sum(1 for count in id_counts.values() if count > 1)

    return {
        "total_rows": total_rows,
        "missing_id_count": missing_id_count,
        "duplicate_id_count": duplicate_id_count,
    }
```

Complexity:

```text
Time: O(n)
Space: O(u)
```


## 70. Coding Problem: Read JSON Data Array

Problem:

```text
Read JSON file and return records under data key.
```

Solution:

```python
def read_json_data_records(path):
    payload = read_json(path)
    return extract_data_list(payload)
```

Edge cases:

```text
top-level is list instead of object
data key missing
data is not list
invalid JSON
```

Interview line:

```text
I validate JSON shape before iterating records.
```


## 71. Coding Problem: Write Invalid JSONL Lines Separately

Problem:

```text
Read input JSONL. Write valid records to valid.jsonl and invalid lines to invalid.jsonl.
```

Solution:

```python
def split_valid_invalid_jsonl(input_path, valid_path, invalid_path):
    valid_count = 0
    invalid_count = 0

    valid_path = Path(valid_path)
    invalid_path = Path(invalid_path)
    valid_path.parent.mkdir(parents=True, exist_ok=True)
    invalid_path.parent.mkdir(parents=True, exist_ok=True)

    with valid_path.open("w", encoding="utf-8") as valid_file, invalid_path.open("w", encoding="utf-8") as invalid_file:
        for item in read_jsonl_with_invalids(input_path):
            if item["_invalid"]:
                invalid_file.write(json.dumps(item, ensure_ascii=False) + "\n")
                invalid_count += 1
            else:
                valid_file.write(json.dumps(item["record"], ensure_ascii=False, default=str) + "\n")
                valid_count += 1

    return {
        "valid_count": valid_count,
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(n)
Space: O(1)
```


## 72. Coding Problem: Flatten JSONL Orders

Problem:

```text
Read orders.jsonl, write flat orders.csv.
```

Solution:

```python
def flatten_orders_jsonl_to_csv(input_path, output_csv_path):
    fieldnames = [
        "order_id",
        "customer_id",
        "customer_email",
        "shipping_country",
    ]

    output_path = Path(output_csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    written = 0
    invalid = 0

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in read_jsonl_with_invalids(input_path):
            if item["_invalid"]:
                invalid += 1
                continue

            row = flatten_order(item["record"])
            writer.writerow(row)
            written += 1

    return {
        "written": written,
        "invalid": invalid,
    }
```

Interview line:

```text
This combines JSONL streaming, nested flattening, and deterministic CSV output.
```


## 73. Coding Problem: Explode Order Items to CSV

Problem:

```text
Read orders.jsonl and write order_items.csv.
```

Solution:

```python
def explode_order_items_jsonl_to_csv(input_path, output_csv_path):
    fieldnames = ["order_id", "line_number", "sku", "quantity"]

    output_path = Path(output_csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    item_count = 0
    invalid_count = 0

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in read_jsonl_with_invalids(input_path):
            if item["_invalid"]:
                invalid_count += 1
                continue

            order = item["record"]

            for row in explode_order_items(order):
                writer.writerow(project_record(row, fieldnames))
                item_count += 1

    return {
        "item_count": item_count,
        "invalid_count": invalid_count,
    }
```

Interview line:

```text
Nested arrays become child rows with parent key and line number.
```


## 74. Coding Problem: Detect Duplicate IDs in JSONL

Problem:

```text
Read JSONL and return duplicate id counts.
```

Solution:

```python
from collections import Counter

def duplicate_ids_in_jsonl(path, id_field="id"):
    counts = Counter()
    invalid_count = 0

    for item in read_jsonl_with_invalids(path):
        if item["_invalid"]:
            invalid_count += 1
            continue

        record_id = item["record"].get(id_field)

        if record_id:
            counts[record_id] += 1

    duplicates = {
        record_id: count
        for record_id, count in counts.items()
        if count > 1
    }

    return {
        "duplicates": duplicates,
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(n)
Space: O(u)
```


## 75. Coding Problem: Merge JSONL Files

Problem:

```text
Merge many JSONL files into one, preserving valid records and writing invalid lines separately.
```

Solution:

```python
def merge_jsonl_files(input_paths, output_path, invalid_path):
    output_path = Path(output_path)
    invalid_path = Path(invalid_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    invalid_path.parent.mkdir(parents=True, exist_ok=True)

    valid_count = 0
    invalid_count = 0

    with output_path.open("w", encoding="utf-8") as out, invalid_path.open("w", encoding="utf-8") as bad:
        for input_path in sorted(input_paths):
            for item in read_jsonl_with_invalids(input_path):
                if item["_invalid"]:
                    item["file"] = str(input_path)
                    bad.write(json.dumps(item, ensure_ascii=False) + "\n")
                    invalid_count += 1
                else:
                    out.write(json.dumps(item["record"], ensure_ascii=False, default=str) + "\n")
                    valid_count += 1

    return {
        "valid_count": valid_count,
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(total lines)
Space: O(1)
```


## 76. Coding Problem: Split CSV by Date

Problem:

```text
Read CSV and write JSONL files partitioned by event_date.
```

Simple approach:

```python
def csv_to_jsonl_partitions(input_csv_path, output_base_dir, date_column="event_date"):
    output_base_dir = Path(output_base_dir)
    files = {}
    counts = {}

    try:
        for row in read_csv_rows(input_csv_path):
            event_date = row.get(date_column) or "__missing__"
            path = output_base_dir / f"{date_column}={event_date}" / "data.jsonl"
            path.parent.mkdir(parents=True, exist_ok=True)

            file = files.get(path)

            if file is None:
                file = path.open("a", encoding="utf-8")
                files[path] = file

            file.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
            counts[str(path)] = counts.get(str(path), 0) + 1
    finally:
        for file in files.values():
            file.close()

    return counts
```

Caution:

```text
Many partitions can open too many file handles.
For production, limit open writers or use a framework.
```

Interview line:

```text
Partitioned writing is useful, but open-file management matters at scale.
```


## 77. Coding Problem: Build Manifest for CSV Folder

Problem:

```text
Build manifest for all CSV files in a folder with row counts and size.
```

Solution:

```python
def csv_folder_manifest(base_dir):
    rows = []

    for path in find_files(base_dir, "*.csv"):
        stat = path.stat()

        rows.append({
            "path": str(path),
            "file_name": path.name,
            "size_bytes": stat.st_size,
            "row_count": count_csv_data_rows(path),
        })

    return rows
```

Write manifest:

```python
def write_manifest_csv(manifest, output_path):
    fieldnames = ["path", "file_name", "size_bytes", "row_count"]
    write_csv_rows(output_path, manifest, fieldnames)
```

Interview line:

```text
A manifest provides file-level auditability before and after ingestion.
```


## 78. Coding Problem: Find Missing Daily Files

Problem:

```text
Expected files:
data_YYYY-MM-DD.csv for each date in range.
Return missing dates.
```

Solution:

```python
from datetime import date, timedelta

def iter_dates(start_date, end_date):
    current = start_date

    while current <= end_date:
        yield current
        current += timedelta(days=1)

def find_missing_daily_files(base_dir, start_date, end_date):
    base_dir = Path(base_dir)
    missing = []

    for current in iter_dates(start_date, end_date):
        expected_path = base_dir / f"data_{current.isoformat()}.csv"

        if not expected_path.exists():
            missing.append(current.isoformat())

    return missing
```

Data Engineering connection:

```text
Daily file delivery checks are common pipeline quality checks.
```


## 79. Coding Problem: Validate JSONL Required Fields

Problem:

```text
Read JSONL and write records missing required fields to invalid file.
```

Solution:

```python
def validate_required_fields(record, required_fields):
    errors = []

    for field in required_fields:
        if record.get(field) in (None, ""):
            errors.append(f"missing_{field}")

    return errors

def validate_jsonl_required_fields(input_path, valid_path, invalid_path, required_fields):
    valid_count = 0
    invalid_count = 0

    with Path(valid_path).open("w", encoding="utf-8") as valid_file, Path(invalid_path).open("w", encoding="utf-8") as invalid_file:
        for item in read_jsonl_with_invalids(input_path):
            if item["_invalid"]:
                invalid_file.write(json.dumps(item, ensure_ascii=False) + "\n")
                invalid_count += 1
                continue

            record = item["record"]
            errors = validate_required_fields(record, required_fields)

            if errors:
                invalid_file.write(json.dumps({
                    "line_number": item["_line_number"],
                    "record": record,
                    "errors": errors,
                }, ensure_ascii=False, default=str) + "\n")
                invalid_count += 1
            else:
                valid_file.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
                valid_count += 1

    return {
        "valid_count": valid_count,
        "invalid_count": invalid_count,
    }
```

Interview line:

```text
This validates both JSON syntax and record schema.
```


## 80. Coding Problem: Convert JSONL to Aggregated CSV

Problem:

```text
Read JSONL transactions and write CSV totals by customer_id.
```

Solution:

```python
from collections import defaultdict
from decimal import Decimal

def aggregate_jsonl_transactions_to_csv(input_path, output_csv_path):
    totals = defaultdict(Decimal)
    invalid_count = 0

    for item in read_jsonl_with_invalids(input_path):
        if item["_invalid"]:
            invalid_count += 1
            continue

        record = item["record"]
        customer_id = record.get("customer_id")
        amount = parse_decimal(record.get("amount"))

        if not customer_id or amount is None:
            invalid_count += 1
            continue

        totals[customer_id] += amount

    rows = [
        {"customer_id": customer_id, "total_amount": str(total)}
        for customer_id, total in sorted(totals.items())
    ]

    write_csv_rows(output_csv_path, rows, ["customer_id", "total_amount"])

    return {
        "customers": len(rows),
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(n + u log u)
Space: O(u)
```


## 81. Pattern Classification Drill

Classify each prompt.

```text
1. CSV has quoted commas.
2. CSV has missing required column.
3. JSONL has one malformed line.
4. JSON file contains {"data": [...]}.
5. JSONL needs to be converted to CSV.
6. Nested customer.address.country is optional.
7. Order has items array.
8. Need to process 100GB file.
9. Output should not be partially visible.
10. Script rerun should not duplicate data.
11. File header starts with weird invisible character.
12. Need to detect changed files.
13. Need to count rows in all CSV files.
14. Need to compare source.csv and target.csv.
15. Need to write invalid rows with line numbers.
16. Need to detect unknown columns.
17. Need to normalize column names.
18. Need to write one file per event_date.
19. Need to avoid logging emails.
20. Need to test parser with fake file.
```

Expected classification:

```text
1. csv module, not split
2. header validation
3. JSONL invalid-line handling
4. JSON shape validation
5. JSONL reader + CSV DictWriter
6. safe nested access
7. explode nested array
8. streaming/chunked processing
9. atomic write
10. idempotent output/dedupe
11. utf-8-sig/BOM handling
12. manifest/checksum
13. file discovery + row counts
14. set diff or sorted streaming diff
15. dead-letter invalid output
16. schema drift/unknown field report
17. column normalization with collision detection
18. partitioned writing
19. PII redaction
20. unit tests/temp file fixtures
```

Passing standard:

```text
18/20 correct before timed file-processing mocks.
```


## 82. High-ROI File/JSON/CSV Topics

Practice these first.

| Topic | What Candidate Must Explain |
|---|---|
| pathlib | safer path handling |
| context managers | automatic file closing |
| encoding | UTF-8 and BOM handling |
| line-by-line reading | memory safety |
| csv.DictReader | read CSV by headers |
| csv.DictWriter | deterministic CSV output |
| delimiter handling | comma/pipe/tab files |
| required headers | schema validation |
| missing values | empty string to None |
| JSON parsing | json.load/json.dump |
| JSON shape validation | expected object/list/data key |
| JSONL parsing | one JSON object per line |
| invalid JSONL lines | isolate bad lines |
| flattening | nested dict to columns |
| exploding arrays | parent/child outputs |
| conversion | CSV ↔ JSONL |
| manifests | file audit |
| checksums | detect changes |
| atomic writes | avoid partial output |
| idempotency | safe reruns |
| dead-letter | invalid rows with reasons |


## 83. Practice Ladder

### Level 1: File basics

```text
Pathlib basics
Read text line by line
Write lines
Find files by extension
Count file lines
```

Exit:

```text
Candidate uses pathlib, context managers, and explicit encoding.
```

### Level 2: CSV basics

```text
Read CSV with DictReader
Validate headers
Normalize missing values
Write CSV with DictWriter
Handle pipe-delimited CSV
```

Exit:

```text
Candidate never manually splits CSV by comma.
```

### Level 3: JSON and JSONL

```text
Read JSON
Validate JSON shape
Read JSONL safely
Write JSONL
Split valid/invalid JSONL
```

Exit:

```text
Candidate can explain JSON vs JSONL clearly.
```

### Level 4: Transform and convert

```text
CSV to JSONL
JSONL to CSV
Flatten nested JSON
Explode arrays
Project fixed schema
```

Exit:

```text
Candidate can convert realistic file formats.
```

### Level 5: Production file processing

```text
Atomic writes
File manifests
Checksums
Compare manifests
Checkpoint processed files
Schema drift report
PII redaction
```

Exit:

```text
Candidate can discuss production-grade ingestion.
```


## 84. 7-Day Files/JSON/CSV Plan

### Day 1: File foundations

Problems:

```text
Read text line by line.
Write lines.
Find files recursively.
Count lines.
Build basic file manifest.
```

Focus:

```text
pathlib
context managers
encoding
streaming
```

### Day 2: CSV basics

Problems:

```text
Read CSV with DictReader.
Validate required columns.
Write CSV with fieldnames.
Handle missing values.
Handle pipe-delimited files.
```

Focus:

```text
csv module
headers
delimiters
schema
```

### Day 3: JSON basics

Problems:

```text
Read JSON.
Validate data field.
Write JSON.
Flatten nested object.
Safe nested access.
```

Focus:

```text
json module
shape validation
nested fields
```

### Day 4: JSONL basics

Problems:

```text
Read JSONL.
Handle invalid JSONL lines.
Write JSONL.
Split valid and invalid JSONL.
Count valid/invalid records.
```

Focus:

```text
streaming
line numbers
bad-line handling
```

### Day 5: Format conversion

Problems:

```text
CSV to JSONL.
CSV to clean JSONL with invalid output.
JSONL to CSV.
JSON array to JSONL.
Explode order items.
```

Focus:

```text
conversion
projection
dead-letter
```

### Day 6: Production file handling

Problems:

```text
Atomic CSV write.
Atomic JSONL write.
File checksum.
Enhanced manifest.
Compare manifests.
```

Focus:

```text
idempotency
audit
partial output prevention
```

### Day 7: Mock and repair

Tasks:

```text
Run Mock Set 3 or 4.
Review mistakes.
Repair weakest topic.
Update progress.
```


## 85. 30-Day Files/JSON/CSV Plan

### Week 1: Safe file handling

Focus:

```text
pathlib
context managers
encoding
line-by-line reading
file discovery
basic manifests
```

Exit:

```text
Candidate can safely open, read, write, and discover files.
```

### Week 2: CSV mastery

Focus:

```text
DictReader
DictWriter
headers
delimiters
missing values
BOM
repeated headers
footers
```

Exit:

```text
Candidate can process messy CSV files safely.
```

### Week 3: JSON and JSONL mastery

Focus:

```text
JSON shape validation
JSONL streaming
invalid lines
nested flattening
arrays
format conversion
```

Exit:

```text
Candidate can process semi-structured files safely.
```

### Week 4: Production-grade file ingestion

Focus:

```text
atomic writes
idempotency
manifests
checksums
schema drift
PII redaction
checkpointing
large-file trade-offs
```

Exit:

```text
Average mock score >= 4/5.
```


## 86. Mock Set 1: File Basics

Problems:

```text
1. Read a text file line by line with line numbers.
2. Find all CSV files under a folder.
3. Count rows in each CSV file.
4. Write summary JSON atomically.
5. Explain encoding and context managers.
```

Expected skills:

```text
pathlib
with-open
encoding
streaming
atomic output
```

Passing standard:

```text
Average score >= 4/5.
Candidate does not use unsafe open/read-all patterns without justification.
```


## 87. Mock Set 2: CSV Processing

Problems:

```text
1. Read CSV with required header validation.
2. Normalize empty strings to None.
3. Convert CSV to clean JSONL.
4. Write invalid rows to invalid.jsonl.
5. Handle UTF-8 BOM or pipe delimiter.
```

Expected skills:

```text
csv.DictReader
csv.DictWriter
header validation
missing values
dead-letter
delimiter/encoding handling
```

Passing standard:

```text
Average score >= 4/5.
Candidate never manually splits CSV by comma.
```


## 88. Mock Set 3: JSON and JSONL

Problems:

```text
1. Validate JSON object with data list.
2. Read JSONL and isolate bad lines.
3. Flatten nested order JSON.
4. Explode order items into child rows.
5. Convert JSONL to CSV with fixed fieldnames.
```

Expected skills:

```text
json module
shape validation
JSONL streaming
nested access
array explosion
schema projection
```

Passing standard:

```text
Average score >= 4/5.
Candidate handles invalid JSONL without losing line context.
```


## 89. Mock Set 4: Production File Ingestion

Problems:

```text
1. Build enhanced file manifest with checksum.
2. Compare old and new manifests.
3. Write JSONL atomically.
4. Checkpoint processed files.
5. Redact PII in invalid output.
```

Expected skills:

```text
manifest
checksums
atomic writes
idempotency
checkpointing
privacy-safe dead-letter
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains production trade-offs and failure handling.
```


## 90. Timed Drill Protocol

Use this timing protocol.

### Simple file problem

```text
10-20 minutes
```

### CSV/JSONL conversion problem

```text
25-40 minutes
```

### Production ingestion scenario

```text
35-45 minutes
```

Per coding drill:

```text
Minute 0-3:
Clarify input format, output format, and data size.

Minute 3-6:
Clarify schema and invalid-record behavior.

Minute 6-25:
Code parser, validation, and writer.

Minute 25-35:
Add edge cases and summary counts.

Minute 35-45:
Explain complexity, memory usage, and production safety.
```

If candidate manually splits CSV by comma:

```text
Stop and repair immediately using csv module.
```


## 91. Review Checklist

Review file/JSON/CSV answers using:

```text
1. Did candidate clarify file format?
2. Did candidate clarify data size?
3. Did candidate use pathlib?
4. Did candidate use context managers?
5. Did candidate specify encoding?
6. Did candidate avoid reading huge files into memory?
7. Did candidate use csv module for CSV?
8. Did candidate validate CSV headers?
9. Did candidate handle missing/extra columns?
10. Did candidate explain JSON vs JSONL?
11. Did candidate handle invalid JSON/JSONL?
12. Did candidate preserve line/row number for invalid records?
13. Did candidate validate required fields?
14. Did candidate write invalid records separately?
15. Did candidate flatten nested JSON safely?
16. Did candidate write deterministic output schema?
17. Did candidate discuss atomic writes?
18. Did candidate discuss idempotency/reruns?
19. Did candidate explain time complexity?
20. Did candidate explain space complexity?
21. Did candidate mention logging/summary metrics?
22. Did candidate connect to DE ingestion?
```

Verdict examples:

```text
Works only for clean files.
Good CSV reading but no header validation.
Good JSONL parsing but no invalid-line output.
Good conversion but memory-heavy.
Good code but no production safety.
Interview-ready.
Strong.
```


## 92. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Uses open without with | Context manager drills |
| Reads all lines unnecessarily | Streaming drills |
| Manually splits CSV | csv module drills |
| No header validation | Required header drills |
| Missing values mishandled | Empty string normalization drills |
| JSON vs JSONL confusion | Format comparison drills |
| Invalid JSONL crashes script | Bad-line isolation drills |
| Unsafe nested access | get_nested drills |
| Array flattening confusion | Parent-child explode drills |
| No invalid output | Dead-letter drills |
| No line numbers | Row/line context drills |
| Partial output risk | Atomic write drills |
| Rerun duplicates | Idempotency drills |
| No file audit | Manifest drills |
| Logs PII | Redaction drills |

If weakness repeats:

```text
Use modes/weakness-repair-mode.md.
```


## 93. Communication Scripts

### File reading script

```text
I would use pathlib and a with-open context manager with explicit UTF-8 encoding, and stream the file line by line if it can be large.
```

### CSV script

```text
I would use csv.DictReader instead of splitting on commas, validate required headers first, preserve row numbers, normalize missing values, and write invalid rows separately.
```

### JSON script

```text
I would parse the JSON file with json.load, validate the expected top-level shape, and only then extract records.
```

### JSONL script

```text
I would process JSONL line by line, parse each line independently, and write malformed lines to an invalid output with line numbers.
```

### Flattening script

```text
For nested JSON, I use safe nested access and create explicit flattened output fields. Arrays become child rows with parent_id and line_number.
```

### Atomic write script

```text
I write to a temporary file first and replace the final output only after the full write succeeds, so downstream jobs never read partial files.
```

### Production script

```text
For production, I would add manifesting, row counts, invalid-record metrics, schema checks, logging, idempotent outputs, and PII-safe dead-letter handling.
```


## 94. Candidate Self-Review Questions

After every files/JSON/CSV problem, candidate should answer:

```text
1. What is the file format?
2. Is the file small or large?
3. Can I stream it?
4. What encoding should I use?
5. Does the file have headers?
6. What columns/fields are required?
7. What happens to extra fields?
8. What happens to missing fields?
9. What happens to malformed rows?
10. Do I preserve row/line numbers?
11. What output format is required?
12. Is output schema deterministic?
13. Is output written atomically?
14. Is the script idempotent?
15. What should be logged?
16. Could PII appear in invalid records?
17. What is time complexity?
18. What is space complexity?
19. How would I test this?
20. What Data Engineering pipeline does this resemble?
```

If candidate cannot answer these:

```text
The solution is not production-ready.
```


## 95. Maintenance Drills

After completing files/JSON/CSV, maintain skill with:

```text
1 CSV drill per week
1 JSONL drill per week
1 nested JSON flattening drill every 2 weeks
1 file manifest/checksum drill every 2 weeks
1 atomic write/idempotency drill every 2 weeks
1 full file-ingestion mock every month
```

Maintenance rotation:

```text
Week 1: CSV header validation + conversion
Week 2: JSONL invalid-line handling + flattening
Week 3: manifests + checksums + comparison
Week 4: atomic writes + checkpoint + PII-safe invalid output
```

If score drops below 4:

```text
Run modes/weakness-repair-mode.md for failed topic.
```


## 96. Progress Tracking Template

Use this progress format.

```text
# Files, JSON, and CSV Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

Pathlib:
Context managers:
Encoding:
Text streaming:
CSV DictReader:
CSV DictWriter:
CSV header validation:
CSV delimiters:
CSV missing values:
BOM handling:
JSON parsing:
JSON shape validation:
JSONL reading:
JSONL invalid handling:
JSONL writing:
Nested JSON access:
Flattening:
Exploding arrays:
CSV to JSONL:
JSONL to CSV:
File manifests:
Checksums:
Manifest comparison:
Atomic writes:
Idempotency:
Checkpoint files:
Schema drift:
PII redaction:
Testing:
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

Candidate passes files/JSON/CSV when they can solve/explain:

```text
1. Use pathlib for paths.
2. Read text files line by line.
3. Write text output safely.
4. Read CSV using DictReader.
5. Write CSV using DictWriter.
6. Validate CSV required columns.
7. Handle missing CSV values.
8. Handle pipe/tab delimiter.
9. Handle UTF-8 BOM.
10. Skip repeated CSV headers.
11. Skip footer rows.
12. Read JSON file.
13. Validate JSON shape.
14. Write JSON file.
15. Read JSONL line by line.
16. Handle invalid JSONL lines.
17. Write JSONL.
18. Explain JSON vs JSONL.
19. Use safe nested JSON access.
20. Flatten nested JSON.
21. Explode nested arrays.
22. Convert CSV to JSONL.
23. Convert CSV to clean JSONL with invalid output.
24. Convert JSONL to CSV.
25. Build file manifest.
26. Count file rows.
27. Compute file checksum.
28. Compare manifests.
29. Write output atomically.
30. Checkpoint processed files.
31. Detect schema drift.
32. Redact PII in invalid records.
33. Explain time and space complexity.
34. Explain production file-ingestion design.
```

Passing standard:

```text
Average score >= 4/5.
No manual CSV splitting.
No unsafe file handling.
No silent bad-row dropping.
No memory-unsafe approach without discussion.
No partial-output risk ignored.
Can connect to Data Engineering ingestion.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles messy vendor files, JSONL invalid lines, production idempotency, manifests, PII, and large-file trade-offs clearly.
```


## 98. Final Summary

Files, JSON, JSONL, and CSV processing are core Python skills for Data Engineering interviews.

They map directly to:

```text
vendor file ingestion
raw data landing
JSON API dumps
event logs
CSV exports
file validation
dead-letter handling
schema drift detection
file manifests
reconciliation
partition checks
format conversion
production utility scripts
```

The candidate must master:

```text
pathlib
context managers
encoding
line-by-line streaming
csv.DictReader
csv.DictWriter
header validation
delimiter handling
missing-value handling
json.load/json.dump
JSON shape validation
JSONL parsing
invalid JSONL handling
safe nested access
flattening
exploding arrays
CSV/JSONL conversion
file manifests
checksums
atomic writes
idempotency
dead-letter files
PII redaction
testing
```

The mentor must be strict:

```text
Manual CSV splitting → not interview-ready.
No context manager → not interview-ready.
No header validation → not interview-ready.
Silent invalid-row dropping → not interview-ready.
No memory discussion → not interview-ready.
No atomic write/idempotency discussion for outputs → not interview-ready.
```

The goal is not to memorize file syntax.

The goal is to safely process real-world files that are large, messy, schema-changing, and operationally risky.


## 99. Problem Card Appendix

### Card 1: Read Text Lines

Category:

```text
File basics
```

Core idea:

```text
Stream lines with line numbers.
```

Data Engineering connection:

```text
Log and raw file processing.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Write Text Lines

Category:

```text
File basics
```

Core idea:

```text
Write output with context manager.
```

Data Engineering connection:

```text
Simple output files.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Find Files

Category:

```text
Pathlib
```

Core idea:

```text
rglob sorted patterns.
```

Data Engineering connection:

```text
File discovery.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Read CSV

Category:

```text
CSV
```

Core idea:

```text
DictReader.
```

Data Engineering connection:

```text
Vendor CSV ingestion.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Write CSV

Category:

```text
CSV
```

Core idea:

```text
DictWriter with fieldnames.
```

Data Engineering connection:

```text
Clean tabular output.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Validate CSV Headers

Category:

```text
CSV schema
```

Core idea:

```text
Required-column checks.
```

Data Engineering connection:

```text
Schema contract.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: CSV Missing Values

Category:

```text
CSV cleaning
```

Core idea:

```text
Empty string to None.
```

Data Engineering connection:

```text
Validation consistency.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: CSV Delimiter

Category:

```text
CSV dialect
```

Core idea:

```text
Pipe/tab delimiter handling.
```

Data Engineering connection:

```text
Vendor formats.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Read JSON

Category:

```text
JSON
```

Core idea:

```text
json.load.
```

Data Engineering connection:

```text
Config/API dump.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Validate JSON Shape

Category:

```text
JSON
```

Core idea:

```text
Object/list/data key validation.
```

Data Engineering connection:

```text
Safe extraction.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Read JSONL

Category:

```text
JSONL
```

Core idea:

```text
Line-by-line JSON parsing.
```

Data Engineering connection:

```text
Event streams.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Invalid JSONL

Category:

```text
JSONL
```

Core idea:

```text
Bad-line isolation.
```

Data Engineering connection:

```text
Robust raw landing.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Write JSONL

Category:

```text
JSONL
```

Core idea:

```text
One object per line.
```

Data Engineering connection:

```text
Clean raw output.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Flatten JSON

Category:

```text
Nested JSON
```

Core idea:

```text
Safe nested fields.
```

Data Engineering connection:

```text
Warehouse flattening.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Explode Arrays

Category:

```text
Nested arrays
```

Core idea:

```text
Parent-child rows.
```

Data Engineering connection:

```text
Order items/events.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: CSV to JSONL

Category:

```text
Conversion
```

Core idea:

```text
Format conversion.
```

Data Engineering connection:

```text
Raw-to-clean pipeline.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: JSONL to CSV

Category:

```text
Conversion
```

Core idea:

```text
Project fixed columns.
```

Data Engineering connection:

```text
Warehouse-ready output.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: File Manifest

Category:

```text
Audit
```

Core idea:

```text
Path, size, modified time.
```

Data Engineering connection:

```text
Ingestion audit.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Checksum

Category:

```text
Audit
```

Core idea:

```text
sha256 in chunks.
```

Data Engineering connection:

```text
Change detection.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Atomic Write

Category:

```text
Reliability
```

Core idea:

```text
Temp then replace.
```

Data Engineering connection:

```text
No partial output.
```

Candidate must be able to explain:

```text
1. File format assumption.
2. Python implementation.
3. Bad-data behavior.
4. Memory behavior.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. Production improvement.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 100. Data Engineering Scenario Appendix

### Scenario 1: Vendor CSV Ingestion

Pattern:

```text
CSV header validation + row validation
```

Task:

```text
Read vendor file, clean rows, dead-letter bad rows.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: Raw JSONL Events

Pattern:

```text
JSONL streaming
```

Task:

```text
Process event records with invalid line isolation.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: CSV to Clean JSONL

Pattern:

```text
format conversion
```

Task:

```text
Convert row records to JSONL with validation.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: JSONL to Warehouse CSV

Pattern:

```text
projection
```

Task:

```text
Project JSON records to fixed CSV schema.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: Nested Order Export

Pattern:

```text
flatten + explode
```

Task:

```text
Create orders and order_items outputs.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: File Delivery Audit

Pattern:

```text
manifest
```

Task:

```text
Track delivered files, size, row counts.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: Changed File Detection

Pattern:

```text
checksum
```

Task:

```text
Detect changed files between runs.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: Missing Daily Files

Pattern:

```text
date range + path check
```

Task:

```text
Find missing expected file deliveries.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: Schema Drift Alert

Pattern:

```text
field comparison
```

Task:

```text
Detect unknown/missing columns.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: PII-Safe Dead Letter

Pattern:

```text
redaction
```

Task:

```text
Write invalid rows safely.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: Atomic Partition Output

Pattern:

```text
temp + replace
```

Task:

```text
Avoid partial files in partition output.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Checkpointed File Processing

Pattern:

```text
processed-files state
```

Task:

```text
Resume multi-file processing.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: Huge File Processing

Pattern:

```text
streaming
```

Task:

```text
Avoid reading all rows into memory.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Malformed JSONL Recovery

Pattern:

```text
line-level dead-letter
```

Task:

```text
Continue after bad line.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: BOM/Delimiter Vendor Issue

Pattern:

```text
encoding/dialect handling
```

Task:

```text
Fix common vendor CSV quirks.
```

Minimum expected answer:

```text
1. State file assumptions.
2. State validation rules.
3. Provide Python code or pseudocode.
4. Explain edge cases.
5. Explain production-safe handling.
```

Passing score:

```text
4/5 or higher.
```


## 101. Drill Appendix

### Drill 1: Pathlib Drill

Task:

```text
Find, inspect, and create file paths with pathlib.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Context Manager Drill

Task:

```text
Rewrite unsafe open/read code using with-open.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: CSV DictReader Drill

Task:

```text
Read rows with row numbers and validate headers.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: CSV DictWriter Drill

Task:

```text
Write deterministic CSV with fixed fieldnames.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Delimiter Drill

Task:

```text
Read comma, pipe, and tab-delimited files.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: BOM Drill

Task:

```text
Handle utf-8-sig header issue.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Missing Values Drill

Task:

```text
Normalize empty strings and validate required fields.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: JSON Shape Drill

Task:

```text
Validate object, array, and data-list structures.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: JSONL Drill

Task:

```text
Read JSONL and isolate invalid lines.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Flatten Drill

Task:

```text
Flatten nested customer/order objects.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Explode Drill

Task:

```text
Explode nested arrays into child rows.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Conversion Drill

Task:

```text
Convert CSV to JSONL and JSONL to CSV.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Manifest Drill

Task:

```text
Build file manifest with size and row count.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Checksum Drill

Task:

```text
Compute SHA256 in chunks.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Compare Drill

Task:

```text
Compare manifests and CSV IDs.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Atomic Write Drill

Task:

```text
Write JSON/CSV/JSONL atomically.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Checkpoint Drill

Task:

```text
Track processed files across runs.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Schema Drift Drill

Task:

```text
Detect unknown/missing fields.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
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
Redact sensitive fields in invalid output.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
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
Build robust CSV ingestion with clean and invalid outputs.
```

Minimum passing answer:

```text
1. State input/output.
2. Use correct Python library.
3. Handle bad data.
4. Preserve file/row context where relevant.
5. Explain complexity and memory usage.
6. Mention production improvement.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 102. Quick Reference Cards

### Quick Card 1: pathlib

Summary:

```text
Use Path for paths and rglob for discovery.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 2: context manager

Summary:

```text
Use with-open so files close safely.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 3: encoding

Summary:

```text
Use UTF-8; use utf-8-sig for BOM issues.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 4: CSV

Summary:

```text
Use csv.DictReader/DictWriter, not split.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 5: CSV headers

Summary:

```text
Validate required headers before processing.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 6: CSV output

Summary:

```text
Use explicit fieldnames for deterministic schema.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 7: JSON

Summary:

```text
Use json.load/dump and validate shape.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 8: JSONL

Summary:

```text
One JSON object per line; streamable.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 9: Invalid JSONL

Summary:

```text
Capture line number, raw line, and error.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 10: Nested JSON

Summary:

```text
Use safe get_nested access.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 11: Arrays

Summary:

```text
Explode arrays to child rows.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 12: Conversion

Summary:

```text
Project records to fixed output schema.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 13: Manifest

Summary:

```text
Track path, size, modified time, row count.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 14: Checksum

Summary:

```text
Read binary chunks for large files.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 15: Atomic write

Summary:

```text
Write temp file then replace final file.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 16: Idempotency

Summary:

```text
Avoid blind append; deterministic output paths.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 17: Dead-letter

Summary:

```text
Write invalid records with reasons.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```

### Quick Card 18: PII

Summary:

```text
Redact sensitive fields before logging/writing invalids.
```

Interview check:

```text
Explain one coding example and one Data Engineering production example where this applies.
```
