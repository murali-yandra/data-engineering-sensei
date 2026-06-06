# Testing, Logging, and Error Handling Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/python/testing-logging-errors.md
```

This guide teaches and drills **testing, logging, and error handling for Data Engineering interviews using Python**.

This is not a generic software-testing tutorial. It is an interview-focused guide for Data Engineering candidates who need to write reliable scripts, explain failure modes, test transformations, log useful pipeline information, handle bad records, recover from transient failures, and design interview-ready production behavior.

Testing, logging, and error handling are high-ROI because Data Engineering interviews often ask:

- How do you test an ETL transformation?
- How do you test a data pipeline?
- How do you handle bad records?
- How do you avoid silently dropping data?
- How do you log pipeline metrics?
- How do you debug failed jobs?
- How do you handle API failures?
- How do you handle file parsing errors?
- How do you handle SQL load failures?
- How do you handle retryable vs non-retryable errors?
- How do you test data quality rules?
- How do you test joins and aggregations?
- How do you test incremental sync?
- How do you make scripts idempotent?
- How do you alert on pipeline failures?
- How do you avoid logging secrets or PII?
- How do you explain production-grade behavior under partial failures?

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
- `practice/python/fundamentals.md`
- `practice/python/files-json-csv.md`
- `practice/python/data-scripting.md`
- `practice/python/api-processing.md`
- `practice/python/pandas-basics.md`
- `practice/sql`
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

The purpose of this guide is to make the candidate strong at practical reliability skills for Data Engineering interviews.

The candidate should learn to answer:

```text
How do I test transformation logic?
How do I test validation rules?
How do I test file parsing?
How do I test API pagination?
How do I test retry behavior?
How do I test incremental sync?
How do I test deduplication?
How do I test aggregation results?
How do I test joins and reconciliation?
How do I log pipeline progress?
How do I log useful errors without leaking sensitive data?
How do I handle malformed records?
How do I distinguish bad data from infrastructure failure?
How do I decide when to retry?
How do I avoid infinite retries?
How do I dead-letter invalid records?
How do I fail fast on schema drift?
How do I make failures debuggable?
How do I explain observability in interviews?
```

A candidate is interview-ready only when they can:

```text
write pure functions for transform and validation
write unit tests for functions
write integration-style tests for file/API flows
use pytest-style assertions
use temporary test files
use fake clients/mocks for external systems
test edge cases
test bad input
test idempotency
test checkpoint behavior
test retry classification
log structured context
avoid logging secrets and PII
capture invalid records with reasons
classify errors correctly
handle retryable errors with bounded backoff
fail fast for non-retryable errors
emit useful metrics and summary counts
explain production failure handling clearly
```


## 2. Why This Matters for Data Engineers

Data Engineering is not only writing code that works once.

Real pipelines fail because of:

```text
bad input files
schema drift
API downtime
rate limits
network timeouts
partial writes
duplicate deliveries
late-arriving data
missing partitions
wrong joins
bad date parsing
bad numeric parsing
warehouse load failures
permission issues
secret expiration
memory limits
orchestration retries
upstream contract changes
downstream table constraints
```

Interviewers test testing/logging/error handling because it shows engineering maturity:

```text
Can the candidate prevent silent data corruption?
Can they debug production issues?
Can they separate data-quality failures from system failures?
Can they make pipeline behavior observable?
Can they design safe retries?
Can they make scripts rerunnable?
Can they write testable code?
Can they communicate realistic production behavior?
```

Weak answer:

```text
I use try except and print errors.
```

Strong answer:

```text
I separate transformation logic for unit tests, validate data quality explicitly, log structured metrics, capture bad records with reasons, retry only transient errors with bounded backoff, checkpoint only after successful writes, and alert when error thresholds are exceeded.
```


## 3. Core Mental Model

Reliable data code has four layers:

```text
1. Correctness:
   The transformation produces expected output.

2. Validation:
   Bad data is detected intentionally.

3. Observability:
   Logs and metrics explain what happened.

4. Recovery:
   Failures are retried, resumed, or dead-lettered safely.
```

For every pipeline, ask:

```text
What can fail?
How will I detect it?
How will I log it?
Can I retry it?
Can I safely resume?
Can I avoid duplicates?
Can I avoid data loss?
Can I alert the right person?
Can I test this behavior?
```

Core interview line:

```text
A Data Engineering pipeline is production-ready only when correctness, validation, observability, and recovery behavior are designed together.
```


## 4. Vocabulary

Important terms:

```text
Unit test:
Test a small function in isolation.

Integration test:
Test multiple components together.

End-to-end test:
Test the complete flow from input to output.

Fixture:
Reusable test data or setup.

Mock:
Fake replacement for dependency.

Fake:
Simple in-memory implementation of a dependency.

Stub:
Simple fixed response object/function.

Assertion:
Statement that expected condition must be true.

Regression test:
Test that prevents a previous bug from returning.

Golden file:
Known expected output used for comparison.

Data-quality test:
Test checking business/data rules.

Schema test:
Test checking required columns/types.

Idempotency test:
Test verifying rerun does not corrupt/duplicate output.

Dead-letter:
Storage for invalid records with reasons.

Retryable error:
Transient error that may succeed later.

Non-retryable error:
Permanent/config/data error that should not be retried blindly.

Backoff:
Increasing wait between retries.

Jitter:
Randomized wait addition to avoid synchronized retries.

Structured log:
Log message with key-value context.

Metric:
Numeric measurement for monitoring.

Alert:
Notification when failure or anomaly happens.
```


## 5. Standard Interview Answer Framework

Use this framework for reliability questions:

```text
1. Restate the failure/risk.
2. Classify the error:
   - data-quality
   - schema
   - external dependency
   - infrastructure
   - code bug
   - configuration
3. Explain detection:
   - validation
   - assertions
   - metrics
   - row counts
   - logs
   - tests
4. Explain handling:
   - fail fast
   - retry
   - dead-letter
   - skip with threshold
   - rollback
   - checkpoint/resume
5. Explain observability:
   - run_id
   - input path
   - record counts
   - invalid counts
   - retries
   - status
   - duration
6. Explain testing:
   - unit tests
   - edge cases
   - mocks/fakes
   - integration tests
7. Explain production safety:
   - idempotency
   - no secret logging
   - alerting
   - auditability
```

Short version:

```text
Classify:
Detect:
Handle:
Log:
Test:
Recover:
```

Strict rule:

```text
No reliability answer is complete without error classification, logging context, retry policy, and test strategy.
```


## 6. Scoring Rubric

Score each testing/logging/error-handling answer from 0 to 5.

### Score 0

No meaningful answer.

### Score 1

Only says try/except or print statements.

### Score 2

Handles basic errors but lacks classification, tests, or observability.

### Score 3

Reasonable answer but weak on idempotency, retry policy, or data-quality handling.

### Score 4

Interview-ready. Explains tests, logs, error classes, bad records, retries, and recovery clearly.

### Score 5

Strong. Covers edge cases, partial failures, dead-letter design, structured logging, metrics, alerting, idempotency, checkpointing, mocks/fakes, and production trade-offs.

Do not give 4+ if:

```text
candidate uses bare except
candidate silently ignores errors
candidate logs secrets or full PII records
candidate retries all errors blindly
candidate has no max retry limit
candidate cannot distinguish bad data from system failure
candidate has no invalid-record strategy
candidate has no test strategy
candidate cannot test external dependencies
candidate cannot explain idempotency
candidate cannot explain what to log
candidate cannot explain alert thresholds
```


## 7. Testing Pyramid for Data Engineering

Data Engineering testing should include multiple levels.

```text
Unit tests:
Fast tests for pure functions.

Component tests:
Test parser + transform + validator together.

Integration tests:
Test file/API/database boundaries with fake or test resources.

Data-quality tests:
Validate expected data rules.

End-to-end tests:
Run a small pipeline from input to output.

Regression tests:
Lock fixes for bugs that already happened.

Contract tests:
Validate external schema expectations.

Smoke tests:
Quick checks that pipeline can start and basic dependencies work.
```

Recommended emphasis:

```text
More unit tests for transformation and validation.
Enough integration tests for I/O and external boundaries.
Targeted end-to-end tests for critical flows.
Continuous data-quality checks in production.
```

Interview line:

```text
I keep most logic in pure functions so unit tests are fast and reliable, then add integration tests around file/API/database boundaries.
```


## 8. What to Test in Data Pipelines

Test these areas:

```text
input schema
required fields
type conversions
date parsing
numeric parsing
string normalization
deduplication
latest-record logic
aggregation results
join correctness
unmatched keys
row counts
invalid records
dead-letter output
partition logic
checkpoint behavior
idempotency
retry classification
API pagination
file discovery
empty input
malformed input
duplicate input
late-arriving records
schema drift
```

Interview line:

```text
For data pipelines, I test both code logic and data assumptions because a pipeline can run successfully and still produce wrong data.
```


## 9. Pure Functions for Testability

Bad design:

```python
def process():
    # reads file
    # calls API
    # transforms
    # writes DB
    # logs
    # checkpoints
    pass
```

Hard to test because everything is mixed.

Good design:

```python
def transform_row(raw):
    ...

def validate_row(row):
    ...

def dedupe_rows(rows):
    ...

def write_output(path, rows):
    ...

def run_pipeline(input_path, output_path):
    rows = read_rows(input_path)
    clean_rows = [transform_row(row) for row in rows]
    write_output(output_path, clean_rows)
```

Why:

```text
transform_row can be tested without files
validate_row can be tested with small dictionaries
dedupe_rows can be tested with in-memory records
I/O functions can be tested separately
```

Interview line:

```text
I separate pure transformation logic from I/O so most behavior can be tested quickly and deterministically.
```


## 10. Basic pytest Style

Typical test structure:

```python
def test_transform_row_normalizes_fields():
    raw = {
        "id": "t1",
        "amount": "100",
        "currency": "inr",
    }

    result = transform_row(raw)

    assert result["transaction_id"] == "t1"
    assert result["currency"] == "INR"
```

Arrange, Act, Assert:

```text
Arrange:
Create input.

Act:
Call function.

Assert:
Check expected output.
```

Example:

```python
def test_validate_row_missing_amount():
    row = {"transaction_id": "t1", "amount": None}

    errors = validate_row(row)

    assert "missing_amount" in errors
```

Interview line:

```text
I write small tests using arrange-act-assert so failures are easy to understand.
```


## 11. Assertions

Assertions check expected behavior.

Common assertions:

```python
assert result == expected
assert len(rows) == 3
assert "missing_id" in errors
assert output["status"] == "SUCCESS"
assert not invalid_rows
assert isinstance(result, dict)
```

Approximate numeric check:

```python
assert abs(actual - expected) < 0.001
```

For exceptions:

```python
import pytest

def test_missing_required_column_fails():
    with pytest.raises(ValueError):
        validate_required_columns(["id"], ["id", "amount"])
```

Interview line:

```text
Tests should assert exact expected behavior, including failures and edge cases.
```


## 12. Test Naming

Good test names explain behavior.

Good:

```python
def test_transform_row_converts_currency_to_uppercase():
    ...

def test_validate_row_returns_error_for_missing_id():
    ...

def test_dedupe_keeps_latest_record_by_updated_at():
    ...
```

Bad:

```python
def test_1():
    ...

def test_function():
    ...
```

Naming pattern:

```text
test_<function>_<expected_behavior>_<condition>
```

Examples:

```text
test_parse_amount_returns_none_for_invalid_string
test_merge_orders_customers_reports_unmatched_customer
test_api_client_retries_503_but_not_400
```

Interview line:

```text
A good test name acts like documentation for the expected behavior.
```


## 13. Fixtures and Test Data

A fixture is reusable setup or data.

Simple constant fixture:

```python
VALID_TRANSACTION = {
    "id": "t1",
    "customer_id": "c1",
    "amount": "100.50",
    "currency": "INR",
}
```

pytest fixture:

```python
import pytest

@pytest.fixture
def valid_transaction():
    return {
        "id": "t1",
        "customer_id": "c1",
        "amount": "100.50",
        "currency": "INR",
    }
```

Use:

```python
def test_transform_transaction(valid_transaction):
    result = transform_transaction(valid_transaction)
    assert result["transaction_id"] == "t1"
```

Interview line:

```text
I keep test data small, explicit, and close to the rule being tested.
```


## 14. Parameterized Tests

Use parameterized tests to cover many cases.

```python
import pytest

@pytest.mark.parametrize(
    "raw_value, expected",
    [
        ("100", 100),
        ("0", 0),
        ("", None),
        (None, None),
        ("abc", None),
    ],
)
def test_parse_int(raw_value, expected):
    assert parse_int(raw_value) == expected
```

Benefits:

```text
less repeated code
many edge cases
clear input/output table
```

Interview line:

```text
Parameterized tests are useful for parsers and validators because they cover many edge cases compactly.
```


## 15. Testing Exceptions

Test expected exceptions.

```python
import pytest

def require_columns(columns, required):
    missing = set(required) - set(columns)

    if missing:
        raise ValueError(f"Missing columns: {missing}")
```

Test:

```python
def test_require_columns_raises_for_missing_column():
    with pytest.raises(ValueError, match="Missing columns"):
        require_columns(["id"], ["id", "amount"])
```

When to raise:

```text
schema missing
config invalid
file missing
auth missing
non-recoverable setup issue
programming error
```

When not to raise for every row:

```text
expected bad records in dirty input
validation errors better collected as invalid rows
```

Interview line:

```text
I raise exceptions for file-level or configuration-level failures, but collect row-level validation errors when bad records are expected.
```


## 16. Testing Invalid Records

Validation should produce explicit reasons.

Example function:

```python
def validate_transaction(row):
    errors = []

    if not row.get("transaction_id"):
        errors.append("missing_transaction_id")

    if row.get("amount") is None:
        errors.append("missing_amount")

    return errors
```

Tests:

```python
def test_validate_transaction_valid_row_returns_no_errors():
    row = {"transaction_id": "t1", "amount": 100}
    assert validate_transaction(row) == []

def test_validate_transaction_missing_id():
    row = {"transaction_id": "", "amount": 100}
    assert validate_transaction(row) == ["missing_transaction_id"]

def test_validate_transaction_missing_amount():
    row = {"transaction_id": "t1", "amount": None}
    assert validate_transaction(row) == ["missing_amount"]
```

Interview line:

```text
I test validation rules individually so each bad-data behavior is explicit.
```


## 17. Testing Transformations

Transformation test:

```python
from decimal import Decimal

def transform_transaction(raw):
    return {
        "transaction_id": raw.get("id"),
        "currency": raw.get("currency", "").strip().upper(),
        "amount": Decimal(str(raw["amount"])) if raw.get("amount") else None,
    }
```

Tests:

```python
def test_transform_transaction_normalizes_currency():
    raw = {"id": "t1", "currency": " inr ", "amount": "100"}
    result = transform_transaction(raw)

    assert result["currency"] == "INR"

def test_transform_transaction_maps_id():
    raw = {"id": "t1", "currency": "INR", "amount": "100"}
    result = transform_transaction(raw)

    assert result["transaction_id"] == "t1"
```

Interview line:

```text
Transformation tests should verify field mapping, type conversion, normalization, and missing-value behavior.
```


## 18. Testing Aggregations

Aggregation function:

```python
from collections import defaultdict
from decimal import Decimal

def total_by_customer(rows):
    totals = defaultdict(Decimal)

    for row in rows:
        customer_id = row.get("customer_id")
        amount = row.get("amount")

        if customer_id and amount is not None:
            totals[customer_id] += Decimal(str(amount))

    return dict(totals)
```

Test:

```python
def test_total_by_customer_sums_amounts():
    rows = [
        {"customer_id": "c1", "amount": "10"},
        {"customer_id": "c1", "amount": "15"},
        {"customer_id": "c2", "amount": "5"},
    ]

    result = total_by_customer(rows)

    assert result["c1"] == Decimal("25")
    assert result["c2"] == Decimal("5")
```

Edge tests:

```text
empty input
missing customer_id
missing amount
zero amount
negative amount if allowed
```

Interview line:

```text
For aggregation tests, I include multiple keys, duplicate keys, empty input, and missing values.
```


## 19. Testing Deduplication

Function:

```python
def keep_latest_by_id(rows):
    latest = {}

    for row in rows:
        row_id = row.get("id")
        updated_at = row.get("updated_at")

        if not row_id or not updated_at:
            continue

        existing = latest.get(row_id)

        if existing is None or updated_at > existing["updated_at"]:
            latest[row_id] = row

    return list(latest.values())
```

Test:

```python
def test_keep_latest_by_id():
    rows = [
        {"id": "1", "updated_at": "2026-01-01", "value": "old"},
        {"id": "1", "updated_at": "2026-01-02", "value": "new"},
        {"id": "2", "updated_at": "2026-01-01", "value": "only"},
    ]

    result = keep_latest_by_id(rows)
    by_id = {row["id"]: row for row in result}

    assert by_id["1"]["value"] == "new"
    assert by_id["2"]["value"] == "only"
```

Interview line:

```text
Deduplication tests must verify the chosen keep rule: first, last, latest, or fail.
```


## 20. Testing Joins and Reconciliation

Join logic should test matched and unmatched records.

Function idea:

```python
def join_orders_customers(orders, customers):
    customer_by_id = {customer["customer_id"]: customer for customer in customers}
    matched = []
    unmatched = []

    for order in orders:
        customer = customer_by_id.get(order.get("customer_id"))

        if customer is None:
            unmatched.append(order)
            continue

        enriched = dict(order)
        enriched["customer_name"] = customer.get("name")
        matched.append(enriched)

    return matched, unmatched
```

Test:

```python
def test_join_orders_customers_reports_unmatched():
    orders = [
        {"order_id": "o1", "customer_id": "c1"},
        {"order_id": "o2", "customer_id": "missing"},
    ]
    customers = [
        {"customer_id": "c1", "name": "A"},
    ]

    matched, unmatched = join_orders_customers(orders, customers)

    assert len(matched) == 1
    assert matched[0]["customer_name"] == "A"
    assert len(unmatched) == 1
    assert unmatched[0]["order_id"] == "o2"
```

Interview line:

```text
Join tests should include matched keys, unmatched keys, duplicate keys, and row-count expectations.
```


## 21. Testing File Processing with tmp_path

pytest provides `tmp_path` for temporary files.

Example:

```python
def test_read_jsonl_with_invalid_line(tmp_path):
    input_path = tmp_path / "events.jsonl"
    input_path.write_text('{"id": 1}\ninvalid-json\n', encoding="utf-8")

    rows = list(read_jsonl_with_invalids(input_path))

    assert rows[0]["_invalid"] is False
    assert rows[1]["_invalid"] is True
```

CSV example:

```python
def test_csv_to_jsonl_writes_output(tmp_path):
    input_path = tmp_path / "input.csv"
    output_path = tmp_path / "output.jsonl"
    invalid_path = tmp_path / "invalid.jsonl"

    input_path.write_text("id,amount\n1,100\n2,\n", encoding="utf-8")

    summary = csv_to_clean_jsonl(input_path, output_path, invalid_path)

    assert summary["valid_count"] == 1
    assert summary["invalid_count"] == 1
    assert output_path.exists()
    assert invalid_path.exists()
```

Interview line:

```text
I use temporary files to test file I/O without depending on local machine paths or polluting the repository.
```


## 22. Testing API Clients with Fakes

Do not call real APIs in unit tests.

Fake client:

```python
class FakeApiClient:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, path, params=None):
        self.calls.append({"path": path, "params": params})
        return self.responses.pop(0)
```

Test pagination:

```python
def test_cursor_pagination_fetches_all_pages():
    client = FakeApiClient([
        {"data": [{"id": 1}], "next_cursor": "abc"},
        {"data": [{"id": 2}], "next_cursor": None},
    ])

    records = list(iter_cursor_records(client, "/items"))

    assert records == [{"id": 1}, {"id": 2}]
    assert len(client.calls) == 2
```

Interview line:

```text
I use fake clients or mocks to test pagination and retry logic without depending on live APIs.
```


## 23. Testing Retry Classification

Retry classification function:

```python
def should_retry_status(status_code):
    return status_code in {408, 429, 500, 502, 503, 504}
```

Tests:

```python
import pytest

@pytest.mark.parametrize("status_code", [408, 429, 500, 502, 503, 504])
def test_retryable_status_codes(status_code):
    assert should_retry_status(status_code) is True

@pytest.mark.parametrize("status_code", [200, 201, 400, 401, 403, 404, 422])
def test_non_retryable_status_codes(status_code):
    assert should_retry_status(status_code) is False
```

Interview line:

```text
Retry decisions should be explicit and tested because blind retries can hide bugs or overload dependencies.
```


## 24. Testing Rate Limit Handling

Rate-limit behavior should be controlled and bounded.

Function:

```python
def parse_retry_after(headers):
    value = headers.get("Retry-After")

    if not value:
        return None

    try:
        seconds = int(value)
    except ValueError:
        return None

    return seconds if seconds >= 0 else None
```

Tests:

```python
def test_parse_retry_after_seconds():
    assert parse_retry_after({"Retry-After": "10"}) == 10

def test_parse_retry_after_missing():
    assert parse_retry_after({}) is None

def test_parse_retry_after_invalid():
    assert parse_retry_after({"Retry-After": "abc"}) is None

def test_parse_retry_after_negative():
    assert parse_retry_after({"Retry-After": "-1"}) is None
```

Interview line:

```text
I test rate-limit parsing because APIs often return missing or malformed headers.
```


## 25. Testing Checkpoints

Checkpoint function:

```python
import json
from pathlib import Path

def load_checkpoint(path):
    path = Path(path)

    if not path.exists():
        return {}

    return json.loads(path.read_text(encoding="utf-8"))

def save_checkpoint(path, checkpoint):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.write_text(json.dumps(checkpoint, sort_keys=True), encoding="utf-8")
    temp_path.replace(path)
```

Test:

```python
def test_save_and_load_checkpoint(tmp_path):
    path = tmp_path / "checkpoint.json"
    checkpoint = {"last_id": "100", "records": 50}

    save_checkpoint(path, checkpoint)

    assert load_checkpoint(path) == checkpoint
```

Important behavior to test:

```text
missing checkpoint returns default
checkpoint saved after successful write
checkpoint is not advanced before write
corrupted checkpoint fails clearly
```

Interview line:

```text
Checkpoint tests verify resumability and help prevent data loss after partial failures.
```


## 26. Testing Idempotency

Idempotency means rerunning does not create incorrect duplicates or corruption.

Example test:

```python
def test_processing_is_idempotent(tmp_path):
    input_path = tmp_path / "input.csv"
    output_path = tmp_path / "output.jsonl"

    input_path.write_text("id,amount\n1,100\n", encoding="utf-8")

    run_pipeline(input_path, output_path)
    first_output = output_path.read_text(encoding="utf-8")

    run_pipeline(input_path, output_path)
    second_output = output_path.read_text(encoding="utf-8")

    assert second_output == first_output
```

What to test:

```text
rerun same input
rerun after partial failure
same file delivered twice
checkpoint not advanced too early
upsert/merge does not duplicate records
partition overwrite replaces deterministically
```

Interview line:

```text
I test idempotency because orchestration systems can retry tasks, and retries must not duplicate or corrupt data.
```


## 27. Testing Logging

You can test logs with pytest caplog.

Function:

```python
import logging

logger = logging.getLogger(__name__)

def process_records(rows):
    valid_count = len(rows)
    logger.info("processed_records valid_count=%s", valid_count)
    return valid_count
```

Test:

```python
def test_process_records_logs_count(caplog):
    with caplog.at_level(logging.INFO):
        process_records([{"id": 1}, {"id": 2}])

    assert "processed_records" in caplog.text
    assert "valid_count=2" in caplog.text
```

Interview line:

```text
I can test critical logs when they are part of operational behavior, such as summary counts or failure classification.
```


## 28. Logging Basics

Use Python logging instead of print.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger(__name__)
```

Log levels:

```text
DEBUG:
Detailed diagnostic information.

INFO:
Normal pipeline progress.

WARNING:
Unexpected but recoverable issue.

ERROR:
Failure that prevents part/all of processing.

CRITICAL:
Severe failure requiring immediate attention.
```

Example:

```python
logger.info("pipeline_started input_path=%s run_id=%s", input_path, run_id)
logger.warning("invalid_records_detected count=%s", invalid_count)
logger.error("pipeline_failed error=%s", error)
```

Interview line:

```text
I use logging levels intentionally so normal progress, warnings, and failures are distinguishable.
```


## 29. Structured Logging

Structured logging means logs include machine-readable context.

Simple key-value style:

```python
logger.info(
    "batch_processed run_id=%s file=%s valid=%s invalid=%s",
    run_id,
    input_file,
    valid_count,
    invalid_count,
)
```

JSON-like style:

```python
logger.info(
    "batch_processed",
    extra={
        "run_id": run_id,
        "input_file": str(input_file),
        "valid_count": valid_count,
        "invalid_count": invalid_count,
    },
)
```

Useful context:

```text
run_id
job_name
task_name
input_path
output_path
source_system
table_name
partition_date
record_count
invalid_count
retry_count
duration_seconds
checkpoint
status
error_type
```

Interview line:

```text
I log structured context like run_id, input file, counts, and error category so failures can be debugged without rerunning blindly.
```


## 30. What to Log in Data Pipelines

Log these events:

```text
pipeline_started
input_discovered
schema_validated
batch_started
batch_completed
records_read
records_written
invalid_records_detected
dead_letter_written
retry_attempt
rate_limited
checkpoint_saved
pipeline_completed
pipeline_failed
```

Log these metrics:

```text
run_id
duration
rows_read
rows_written
invalid_rows
duplicate_rows
skipped_rows
retry_count
api_status_code
pages_fetched
files_processed
bytes_processed
last_watermark
```

Do not log:

```text
API tokens
passwords
full credit card numbers
full PII records
large payloads
secrets
private keys
authorization headers
```

Interview line:

```text
Good pipeline logs should answer what ran, what input was processed, how many records moved, what failed, and where to resume.
```


## 31. Avoid Logging Secrets and PII

Bad:

```python
logger.info("headers=%s", headers)
logger.error("bad_record=%s", raw_customer_record)
```

Why:

```text
headers may contain tokens
raw records may contain PII
logs are often widely accessible
```

Better:

```python
safe_record = {
    "record_id": record.get("id"),
    "error": "missing_amount",
}

logger.warning("invalid_record record_id=%s error=%s", safe_record["record_id"], safe_record["error"])
```

Redaction:

```python
SENSITIVE_FIELDS = {"email", "phone", "ssn", "token", "password", "authorization"}

def redact_record(record):
    return {
        key: "***REDACTED***" if key.lower() in SENSITIVE_FIELDS else value
        for key, value in record.items()
    }
```

Interview line:

```text
I log identifiers and error categories, not secrets or full sensitive records.
```


## 32. Error Classification

Classify errors before handling.

```text
Data-quality errors:
Bad/missing field values.

Schema errors:
Missing columns, wrong response shape, type drift.

External dependency errors:
API 5xx, timeout, rate limit, database unavailable.

Authentication/config errors:
Missing token, expired credentials, wrong permissions.

Infrastructure errors:
Disk full, network down, memory exceeded.

Code bugs:
TypeError, logic error, unexpected exception.

Business rule errors:
Invalid state transition, duplicate key when uniqueness required.
```

Handling differs:

```text
Data-quality:
dead-letter or fail threshold.

Schema:
fail fast and alert.

External transient:
retry with backoff.

Auth/config:
fail fast, do not retry forever.

Infrastructure:
retry if transient, alert if persistent.

Code bug:
fail fast, fix code.

Business rule:
fail or quarantine based on rule.
```

Interview line:

```text
Different errors require different handling; treating every error with one try/except is dangerous.
```


## 33. Exception Handling Principles

Good exception handling:

```text
catch specific exceptions
keep try block small
add context
do not swallow errors silently
re-raise when appropriate
separate row-level errors from job-level errors
retry only retryable failures
log enough to debug
avoid logging secrets
```

Bad:

```python
try:
    process_everything()
except Exception:
    pass
```

Better:

```python
try:
    amount = parse_amount(raw_amount)
except ValueError as exc:
    invalid_records.append({
        "record_id": record.get("id"),
        "error": "invalid_amount",
        "detail": str(exc),
    })
```

Interview line:

```text
I catch errors at the right boundary: row-level validation errors become invalid records, while job-level failures fail the task clearly.
```


## 34. Bare Except Is Dangerous

Bad:

```python
try:
    process(row)
except:
    pass
```

Problems:

```text
hides bugs
drops data silently
catches unexpected system-level exceptions
makes debugging impossible
can produce false successful jobs
```

Better:

```python
try:
    process(row)
except ValueError as exc:
    invalid_records.append({"row": row, "error": str(exc)})
```

Or:

```python
try:
    process(row)
except Exception as exc:
    logger.exception("unexpected_row_processing_error row_id=%s", row.get("id"))
    raise
```

Interview line:

```text
I avoid bare except because silent failure is worse than a visible pipeline failure.
```


## 35. Raising Meaningful Errors

Bad:

```python
raise Exception("bad")
```

Better:

```python
raise ValueError(f"Missing required columns: {missing_columns}")
```

Custom errors:

```python
class SchemaValidationError(Exception):
    pass

class DataQualityThresholdError(Exception):
    pass

class RetryableApiError(Exception):
    pass

class NonRetryableApiError(Exception):
    pass
```

Usage:

```python
if missing_columns:
    raise SchemaValidationError(f"Missing required columns: {sorted(missing_columns)}")
```

Interview line:

```text
Meaningful error types and messages make failures easier to classify, test, and alert on.
```


## 36. Row-Level vs Job-Level Errors

Row-level errors:

```text
missing amount
invalid currency
bad timestamp
malformed JSONL line
record-level schema issue
```

Handling:

```text
collect invalid record
write dead-letter
continue if below threshold
fail if invalid rate too high
```

Job-level errors:

```text
input file missing
required column missing
API auth failed
database unavailable
checkpoint write failed
output path not writable
```

Handling:

```text
fail task
retry if transient
alert if persistent
do not pretend success
```

Interview line:

```text
Expected dirty records can be dead-lettered, but job-level failures should fail the pipeline clearly.
```


## 37. Dead-Letter Design

Dead-letter records should include:

```text
run_id
source_system
input_file or endpoint
row_number or page/cursor
record_id if available
raw_record or redacted raw record
transformed_record if available
error_codes
error_message
created_at
schema_version if available
```

Example:

```python
dead_letter_record = {
    "run_id": run_id,
    "source": "transactions_csv",
    "row_number": row_number,
    "record_id": raw.get("id"),
    "errors": ["invalid_amount"],
    "raw": redact_record(raw),
}
```

Do not:

```text
silently drop invalid rows
only log invalid rows without storing them
store sensitive raw payloads without redaction/governance
mix invalid data with clean output
```

Interview line:

```text
Dead-letter output makes bad records auditable, debuggable, and replayable after fixes.
```


## 38. Invalid Rate Thresholds

A few invalid records may be acceptable.

Too many invalid records means source/schema issue.

```python
def enforce_invalid_threshold(valid_count, invalid_count, max_invalid_ratio=0.05):
    total = valid_count + invalid_count

    if total == 0:
        return

    invalid_ratio = invalid_count / total

    if invalid_ratio > max_invalid_ratio:
        raise DataQualityThresholdError(
            f"Invalid ratio too high: {invalid_ratio:.2%}; "
            f"valid={valid_count}; invalid={invalid_count}"
        )
```

Interview line:

```text
I can continue with small row-level errors, but fail the job when invalid rate crosses a threshold because that indicates upstream breakage.
```


## 39. Retry Policy

Retry only transient failures.

Retryable:

```text
network timeout
connection reset
HTTP 408
HTTP 429
HTTP 500
HTTP 502
HTTP 503
HTTP 504
temporary database unavailable
temporary cloud storage error
```

Usually non-retryable:

```text
bad request 400
unauthorized 401 without refresh path
forbidden 403
not found 404 for fixed endpoint/file
unprocessable entity 422
missing required column
invalid input file
bad SQL syntax
configuration error
```

Retry policy should include:

```text
max attempts
exponential backoff
jitter
timeout
retryable classification
logging each attempt
final failure after exhausted retries
```

Interview line:

```text
I retry transient dependency failures with bounded backoff and jitter, but I do not retry permanent data/config errors blindly.
```


## 40. Exponential Backoff with Jitter

Example:

```python
import random
import time

def sleep_with_backoff(attempt, base_seconds=1, max_seconds=60):
    sleep_seconds = min(base_seconds * (2 ** (attempt - 1)), max_seconds)
    sleep_seconds += random.random()
    time.sleep(sleep_seconds)
```

Why jitter:

```text
prevents many workers from retrying at exactly the same time
reduces thundering herd effect
```

Bounded retries:

```python
def retry_operation(operation, max_attempts=4):
    last_error = None

    for attempt in range(1, max_attempts + 1):
        try:
            return operation()
        except RetryableApiError as exc:
            last_error = exc
            sleep_with_backoff(attempt)

    raise RuntimeError(f"Operation failed after {max_attempts} attempts") from last_error
```

Interview line:

```text
Retries must be bounded; infinite retries can hang pipelines and hide incidents.
```


## 41. Timeouts

Always set timeouts for network calls.

Bad:

```python
requests.get(url)
```

Good:

```python
requests.get(url, timeout=30)
```

Better:

```python
requests.get(url, timeout=(5, 30))
```

Meaning:

```text
connect timeout = 5 seconds
read timeout = 30 seconds
```

Why:

```text
without timeout, tasks can hang indefinitely
orchestration slots can be blocked
pipeline can miss SLA
```

Interview line:

```text
I set timeouts because a hung dependency should fail predictably and be retried or alerted.
```


## 42. Partial Failure Handling

Partial failures are common.

Examples:

```text
page fetched but not written
batch partially written
checkpoint saved before write
output file half-written
API returns some pages then fails
database merge fails after staging write
worker dies mid-run
```

Safe design:

```text
write to staging/temp first
checkpoint only after successful write
use idempotent writes
use transactions when available
use run_id
record batch/page metadata
make reruns safe
validate output counts
```

Bad design:

```text
save checkpoint before writing output
append blindly every retry
delete input before output is committed
```

Interview line:

```text
Checkpointing and idempotent writes must be coordinated so partial failures do not cause data loss or duplicates.
```


## 43. Idempotency Error Handling

A pipeline step is idempotent when rerunning it does not corrupt output.

Strategies:

```text
overwrite deterministic output path
write temp then replace
upsert/merge by primary key
partition overwrite for fixed window
deduplicate by source key
use idempotency keys for side-effecting APIs
checkpoint after success
use run_id and audit tables
```

Testing:

```text
run same input twice
compare outputs
simulate failure before checkpoint
simulate failure after write before checkpoint
verify no duplicates
```

Interview line:

```text
Because retries happen, I design writes to be idempotent rather than hoping tasks never rerun.
```


## 44. Observability Metrics

Useful metrics:

```text
records_read
records_valid
records_invalid
records_written
files_processed
bytes_processed
duplicate_count
schema_error_count
json_decode_error_count
retry_count
rate_limit_count
api_request_count
api_latency_ms
batch_duration_seconds
pipeline_duration_seconds
last_successful_watermark
checkpoint_age
row_count_delta
null_rate
freshness_lag_minutes
```

Metric dimensions:

```text
job_name
task_name
run_id
source_system
table_name
partition_date
environment
status
error_type
```

Interview line:

```text
Metrics should allow operators to see volume, quality, latency, freshness, and failure patterns over time.
```


## 45. Alerting

Alert on:

```text
pipeline failure
repeated retries exhausted
invalid rate above threshold
schema drift
record count unexpectedly zero
record count drops sharply
freshness lag exceeds SLA
checkpoint not advancing
missing partition/file
duplicate count above threshold
API 429/5xx spike
database load failure
output row count mismatch
```

Avoid noisy alerts:

```text
alert on actionable issues
use thresholds
group related alerts
include run_id and failure context
route to correct owner
```

Interview line:

```text
I alert on actionable failures and data-quality anomalies, not every small warning.
```


## 46. Testing Logs, Metrics, and Alerts Conceptually

In interviews, you may not write full monitoring code.

But you should explain:

```text
What logs are emitted?
What metrics are collected?
What threshold triggers alert?
Who owns alert?
What context is included?
How false positives are avoided?
How issue is debugged?
```

Example:

```text
If today's row count is 0 but historical average is 1M, I would fail or quarantine the run, not advance watermark, log the anomaly, emit row_count_anomaly metric, and alert the pipeline owner.
```

Interview line:

```text
Observability should detect silent data issues, not only crashed jobs.
```


## 47. Error Handling for Files

File errors:

```text
file not found
permission denied
wrong encoding
empty file
missing header
extra columns
malformed CSV
invalid JSON
invalid JSONL line
file still being written
partial file
duplicate file
```

Handling:

```text
file missing:
fail or wait depending expected delivery

wrong encoding:
fail with clear error or support known encoding

missing header:
fail fast

malformed JSON file:
fail file-level

malformed JSONL line:
dead-letter line and continue if threshold allows

partial file:
use manifest/done marker/checksum
```

Interview line:

```text
For files, I validate file presence, schema, row counts, and parsing errors before treating ingestion as successful.
```


## 48. Error Handling for APIs

API errors:

```text
timeout
connection error
DNS failure
429 rate limit
5xx server error
invalid JSON response
unexpected schema
auth expired
pagination loop
empty response anomaly
duplicate records
late updates
```

Handling:

```text
timeout/5xx:
retry with backoff

429:
respect Retry-After

401:
refresh token if supported, otherwise fail

400/422:
non-retryable request issue

invalid JSON/schema:
fail or quarantine based on endpoint contract

pagination loop:
fail with cursor/page context

empty anomaly:
do not advance checkpoint until verified
```

Interview line:

```text
API ingestion needs timeout, bounded retries, rate-limit handling, schema validation, pagination guards, and checkpoint safety.
```


## 49. Error Handling for Databases/Warehouses

Database/warehouse errors:

```text
connection failure
timeout
deadlock
constraint violation
duplicate key
schema mismatch
permission denied
quota exceeded
load job failed
transaction rollback
partial staging load
```

Handling:

```text
connection timeout/deadlock:
retry if safe

constraint violation:
data-quality or dedupe issue

schema mismatch:
fail fast and alert

permission denied:
configuration/security issue

load failure:
preserve staging files/logs for replay

partial write:
use transaction/staging + merge
```

Interview line:

```text
For warehouse loads, I prefer staging plus validation plus atomic merge so partial failures do not corrupt final tables.
```


## 50. Error Handling for Orchestration

Orchestration issues:

```text
task retry
task timeout
dependency missing
upstream failed
downstream blocked
schedule overlap
backfill conflict
manual rerun
SLA miss
worker killed
```

Design:

```text
tasks should be idempotent
retries should be safe
checkpointing should be durable
late files should be handled
backfills should use deterministic windows
logs should include run_id/execution_date
alerts should include DAG/task/run
```

Interview line:

```text
In orchestrated pipelines, retries are normal, so every task should be safe to rerun.
```


## 51. Coding Problem: Validate Required Columns

Problem:

```text
Write a function that validates required columns exist.
Raise a clear exception if missing.
```

Solution:

```python
class SchemaValidationError(Exception):
    pass

def validate_required_columns(actual_columns, required_columns):
    missing = sorted(set(required_columns) - set(actual_columns))

    if missing:
        raise SchemaValidationError(f"Missing required columns: {missing}")
```

Tests:

```python
def test_validate_required_columns_passes():
    validate_required_columns(["id", "amount"], ["id"])

def test_validate_required_columns_fails():
    try:
        validate_required_columns(["id"], ["id", "amount"])
        assert False
    except SchemaValidationError as exc:
        assert "amount" in str(exc)
```

Interview point:

```text
Missing required columns are schema failures, not row-level invalid records.
```


## 52. Coding Problem: Split Valid and Invalid Rows

Problem:

```text
Split transaction rows into valid and invalid with error reasons.
```

Solution:

```python
def validate_transaction(row):
    errors = []

    if not row.get("id"):
        errors.append("missing_id")

    if row.get("amount") is None:
        errors.append("missing_amount")

    if not row.get("currency"):
        errors.append("missing_currency")

    return errors

def split_valid_invalid(rows):
    valid = []
    invalid = []

    for row_number, row in enumerate(rows, start=1):
        errors = validate_transaction(row)

        if errors:
            invalid.append({
                "row_number": row_number,
                "row": row,
                "errors": errors,
            })
        else:
            valid.append(row)

    return valid, invalid
```

Tests:

```python
def test_split_valid_invalid():
    rows = [
        {"id": "1", "amount": 100, "currency": "INR"},
        {"id": "", "amount": 100, "currency": "INR"},
    ]

    valid, invalid = split_valid_invalid(rows)

    assert len(valid) == 1
    assert len(invalid) == 1
    assert invalid[0]["errors"] == ["missing_id"]
```

Interview point:

```text
Invalid rows keep row number and reasons for debugging.
```


## 53. Coding Problem: Redact Sensitive Fields

Problem:

```text
Redact sensitive fields before logging/writing invalid records.
```

Solution:

```python
SENSITIVE_FIELDS = {"email", "phone", "ssn", "token", "password", "authorization"}

def redact_record(record):
    redacted = {}

    for key, value in record.items():
        if key.lower() in SENSITIVE_FIELDS:
            redacted[key] = "***REDACTED***"
        else:
            redacted[key] = value

    return redacted
```

Test:

```python
def test_redact_record():
    record = {"id": "1", "email": "a@example.com", "amount": 100}

    result = redact_record(record)

    assert result["email"] == "***REDACTED***"
    assert result["amount"] == 100
```

Interview point:

```text
Reliability includes safe diagnostics; debugging should not leak sensitive data.
```


## 54. Coding Problem: Retry Decision

Problem:

```text
Classify HTTP status codes as retryable or non-retryable.
```

Solution:

```python
def classify_http_status(status_code):
    if status_code in {408, 429, 500, 502, 503, 504}:
        return "retryable"

    if 200 <= status_code < 300:
        return "success"

    if 400 <= status_code < 500:
        return "non_retryable"

    return "unknown"
```

Tests:

```python
def test_classify_http_status_retryable():
    assert classify_http_status(503) == "retryable"

def test_classify_http_status_non_retryable():
    assert classify_http_status(400) == "non_retryable"

def test_classify_http_status_success:
    assert classify_http_status(200) == "success"
```

Interview point:

```text
Retry rules should be explicit and tested.
```


## 55. Coding Problem: Retry Wrapper

Problem:

```text
Write a bounded retry wrapper for retryable errors.
```

Solution:

```python
class RetryableError(Exception):
    pass

def retry(operation, max_attempts=3):
    last_error = None

    for attempt in range(1, max_attempts + 1):
        try:
            return operation()
        except RetryableError as exc:
            last_error = exc

    raise RuntimeError(f"Failed after {max_attempts} attempts") from last_error
```

Test:

```python
def test_retry_succeeds_after_failure():
    calls = {"count": 0}

    def operation():
        calls["count"] += 1

        if calls["count"] < 2:
            raise RetryableError("temporary")

        return "success"

    assert retry(operation, max_attempts=3) == "success"
    assert calls["count"] == 2
```

Interview point:

```text
Actual production retry should include backoff, jitter, timeout, and logging.
```


## 56. Coding Problem: Dead-Letter Writer

Problem:

```text
Write invalid records to JSONL.
```

Solution:

```python
import json
from pathlib import Path

def write_dead_letter(path, invalid_records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        for record in invalid_records:
            file.write(json.dumps(record, ensure_ascii=False, default=str))
            file.write("\n")
```

Test:

```python
def test_write_dead_letter(tmp_path):
    path = tmp_path / "invalid.jsonl"
    invalid = [{"row_number": 1, "errors": ["missing_id"]}]

    write_dead_letter(path, invalid)

    content = path.read_text(encoding="utf-8")
    assert "missing_id" in content
```

Interview point:

```text
Dead-letter output should be durable, structured, and replayable.
```


## 57. Coding Problem: Logging Summary

Problem:

```text
Log pipeline summary after processing.
```

Solution:

```python
import logging

logger = logging.getLogger(__name__)

def log_pipeline_summary(run_id, summary):
    logger.info(
        "pipeline_summary run_id=%s records_read=%s records_written=%s invalid_records=%s",
        run_id,
        summary.get("records_read"),
        summary.get("records_written"),
        summary.get("invalid_records"),
    )
```

Test with caplog:

```python
def test_log_pipeline_summary(caplog):
    summary = {
        "records_read": 10,
        "records_written": 9,
        "invalid_records": 1,
    }

    with caplog.at_level(logging.INFO):
        log_pipeline_summary("run-1", summary)

    assert "pipeline_summary" in caplog.text
    assert "records_read=10" in caplog.text
```

Interview point:

```text
Logs should include summary counts and run_id.
```


## 58. Coding Problem: Idempotent Output Write

Problem:

```text
Write output atomically to avoid partial files.
```

Solution:

```python
import json
from pathlib import Path

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

Test:

```python
def test_atomic_write_jsonl(tmp_path):
    path = tmp_path / "output.jsonl"
    records = [{"id": 1}]

    atomic_write_jsonl(path, records)

    assert path.exists()
    assert not path.with_suffix(".jsonl.tmp").exists()
    assert '"id": 1' in path.read_text(encoding="utf-8")
```

Interview point:

```text
Atomic writes prevent downstream readers from seeing half-written output.
```


## 59. Coding Problem: Pipeline Summary Function

Problem:

```text
Process rows and return summary counts.
```

Solution:

```python
def process_rows(rows):
    valid, invalid = split_valid_invalid(rows)

    summary = {
        "records_read": len(rows),
        "records_valid": len(valid),
        "records_invalid": len(invalid),
    }

    return valid, invalid, summary
```

Test:

```python
def test_process_rows_summary():
    rows = [
        {"id": "1", "amount": 100, "currency": "INR"},
        {"id": "", "amount": 100, "currency": "INR"},
    ]

    valid, invalid, summary = process_rows(rows)

    assert summary["records_read"] == 2
    assert summary["records_valid"] == 1
    assert summary["records_invalid"] == 1
```

Interview point:

```text
Summary counts are both testable and operationally useful.
```


## 60. Coding Problem: Schema Drift Detector

Problem:

```text
Detect missing required fields and unknown fields in records.
```

Solution:

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
            if record.get(field) in (None, ""):
                missing_required_counts[field] += 1

    return {
        "unknown_fields": dict(unknown_counts),
        "missing_required": dict(missing_required_counts),
    }
```

Test:

```python
def test_schema_drift_report():
    records = [
        {"id": "1", "amount": 100, "new_field": "x"},
        {"id": "", "amount": 200},
    ]

    result = schema_drift_report(
        records,
        expected_fields={"id", "amount"},
        required_fields={"id"},
    )

    assert result["unknown_fields"]["new_field"] == 1
    assert result["missing_required"]["id"] == 1
```

Interview point:

```text
Schema drift should be detected and surfaced, not silently ignored.
```


## 61. Testing Pattern Classification Drill

Classify each prompt.

```text
1. Test function that normalizes currency.
2. Test missing required CSV column.
3. Test malformed JSONL line.
4. Test API pagination without real API.
5. Test that 503 is retried.
6. Test that 400 is not retried.
7. Test rerun does not duplicate output.
8. Test checkpoint save/load.
9. Test file output in temporary directory.
10. Test logs include record counts.
11. Test invalid rows include reasons.
12. Test join reports unmatched customers.
13. Test aggregation total per customer.
14. Test duplicate IDs are detected.
15. Test missing partition dates.
16. Test schema drift unknown columns.
17. Test bad amount parsing.
18. Test PII redaction.
19. Test max retry exhaustion.
20. Test row count anomaly alert condition.
```

Expected classification:

```text
1. unit test transformation
2. schema exception test
3. JSONL invalid-line test
4. fake client/mock test
5. retry classification/wrapper test
6. non-retryable classification test
7. idempotency test
8. checkpoint test
9. tmp_path file test
10. caplog logging test
11. validation/dead-letter test
12. join/reconciliation test
13. aggregation unit test
14. duplicate detection test
15. partition completeness test
16. schema drift test
17. parser edge-case test
18. redaction/security test
19. retry exhaustion test
20. data-quality anomaly test
```

Passing standard:

```text
18/20 correct before reliability mock interviews.
```


## 62. Error Classification Drill

Classify each error.

```text
1. HTTP 503 from API.
2. HTTP 400 due to bad query parameter.
3. CSV missing amount column.
4. One row has amount=abc.
5. Database permission denied.
6. File does not exist.
7. API returns same cursor repeatedly.
8. Invalid JSONL line 103.
9. Pipeline writes page then crashes before checkpoint.
10. Token expired.
11. Warehouse deadlock.
12. Unknown new field appears in API response.
13. Record count drops from 1M to 0.
14. Duplicate primary keys in source.
15. Task killed by worker memory limit.
```

Expected classification:

```text
1. retryable external dependency
2. non-retryable request/config
3. schema error, fail fast
4. row-level data-quality error
5. permission/config, fail fast
6. file-level dependency error
7. pagination logic/vendor error, fail with context
8. row/line-level parsing error for JSONL
9. partial failure, needs idempotency/checkpoint safety
10. auth error, refresh if supported or fail
11. retryable database error if transaction safe
12. schema drift, alert/fail depending contract
13. data anomaly, do not advance checkpoint blindly
14. data-quality/key uniqueness issue
15. infrastructure/resource error
```

Passing standard:

```text
13/15 correct with handling strategy.
```


## 63. High-ROI Topics

Practice these first.

| Topic | Candidate Must Explain |
|---|---|
| unit tests | pure function testing |
| pytest basics | assertions, raises, fixtures |
| parameterized tests | parser/validator edge cases |
| tmp_path | file I/O tests |
| fake clients | API/dependency tests |
| caplog | testing logs |
| transformation tests | mapping/normalization |
| validation tests | error reasons |
| aggregation tests | totals/counts |
| dedupe tests | keep rule |
| join tests | matched/unmatched/cardinality |
| checkpoint tests | save/load/resume |
| idempotency tests | safe reruns |
| structured logging | run_id and counts |
| PII-safe logging | redaction |
| error classification | data vs system vs schema |
| retry policy | bounded backoff |
| dead-letter | invalid record storage |
| invalid threshold | fail on anomaly |
| observability | metrics and alerts |


## 64. Practice Ladder

### Level 1: Unit testing basics

```text
assertions
test naming
pytest raises
parameterized tests
pure function tests
```

Exit:

```text
Candidate can test transform/validate functions.
```

### Level 2: Data tests

```text
schema validation
invalid records
aggregation tests
dedupe tests
join tests
reconciliation tests
```

Exit:

```text
Candidate can test data correctness.
```

### Level 3: I/O and dependency tests

```text
tmp_path file tests
fake API clients
checkpoint tests
dead-letter tests
logging tests
```

Exit:

```text
Candidate can test pipeline boundaries.
```

### Level 4: Error handling

```text
error classification
retryable vs non-retryable
bounded retries
dead-letter strategy
threshold failures
partial failures
```

Exit:

```text
Candidate can handle realistic production failures.
```

### Level 5: Observability and production reasoning

```text
structured logs
metrics
alerts
idempotency
security-safe logs
incident debugging
```

Exit:

```text
Candidate can explain production reliability clearly.
```


## 65. 7-Day Plan

### Day 1: Unit testing fundamentals

Problems:

```text
Test normalize_currency.
Test parse_int.
Test validate_transaction.
Test transform_transaction.
Test exceptions with pytest.raises.
```

Focus:

```text
assertions
small pure functions
edge cases
```

### Day 2: Data correctness tests

Problems:

```text
Test aggregation by customer.
Test dedupe latest by id.
Test duplicate detection.
Test join unmatched records.
Test schema validation.
```

Focus:

```text
data correctness
keys
row counts
```

### Day 3: File tests

Problems:

```text
Test CSV parser with tmp_path.
Test JSONL invalid line.
Test dead-letter writer.
Test atomic output.
Test checkpoint save/load.
```

Focus:

```text
temporary files
I/O boundaries
```

### Day 4: API/dependency tests

Problems:

```text
Test cursor pagination with fake client.
Test retry classification.
Test Retry-After parser.
Test retry wrapper.
Test max retry exhaustion.
```

Focus:

```text
fakes
retry policy
dependency boundaries
```

### Day 5: Logging and observability

Problems:

```text
Test summary log with caplog.
Design structured logs.
Design pipeline metrics.
Design alert thresholds.
Redact PII.
```

Focus:

```text
logs
metrics
safe diagnostics
```

### Day 6: Error handling scenarios

Problems:

```text
Handle schema drift.
Handle count drop to zero.
Handle partial write.
Handle token expiry.
Handle malformed vendor file.
```

Focus:

```text
classification
recovery
idempotency
```

### Day 7: Mock and repair

Tasks:

```text
Run reliability mock.
Review mistakes.
Repair weakest topic.
Update progress.
```


## 66. 30-Day Plan

### Week 1: Testable Python

Focus:

```text
pure functions
pytest assertions
exceptions
fixtures
parameterized tests
```

Exit:

```text
Candidate can test transformations and validators.
```

### Week 2: Data pipeline tests

Focus:

```text
schema tests
file tests
aggregation tests
dedupe tests
join tests
reconciliation tests
```

Exit:

```text
Candidate can test common DE logic.
```

### Week 3: Reliability and error handling

Focus:

```text
retry logic
dead-letter
checkpoints
idempotency
partial failures
dependency fakes
```

Exit:

```text
Candidate can test and explain recovery behavior.
```

### Week 4: Observability and mock interviews

Focus:

```text
structured logging
metrics
alerts
PII-safe logs
incident scenarios
production trade-offs
```

Exit:

```text
Average mock score >= 4/5.
```


## 67. Mock Set 1: Testing Basics

Problems:

```text
1. Write tests for parse_int.
2. Write tests for transform_transaction.
3. Write tests for validate_transaction.
4. Test missing required column raises error.
5. Parameterize invalid amount cases.
```

Expected skills:

```text
assertions
pytest.raises
parameterization
pure function testing
```

Passing standard:

```text
Average score >= 4/5.
Candidate covers success and failure cases.
```


## 68. Mock Set 2: Data Pipeline Tests

Problems:

```text
1. Test aggregation total by customer.
2. Test latest record per ID.
3. Test join unmatched customers.
4. Test duplicate ID detection.
5. Test source-target reconciliation.
```

Expected skills:

```text
aggregation correctness
dedupe rule
join behavior
row-count checks
reconciliation logic
```

Passing standard:

```text
Average score >= 4/5.
Candidate tests edge cases, not only happy path.
```


## 69. Mock Set 3: I/O and Dependency Tests

Problems:

```text
1. Test JSONL invalid-line handling with tmp_path.
2. Test CSV clean/invalid outputs.
3. Test API pagination with fake client.
4. Test checkpoint save/load.
5. Test atomic output write.
```

Expected skills:

```text
tmp_path
fake clients
file assertions
checkpoint testing
idempotent output
```

Passing standard:

```text
Average score >= 4/5.
Candidate avoids real external dependencies in unit tests.
```


## 70. Mock Set 4: Logging and Error Handling

Problems:

```text
1. Design logs for an API ingestion pipeline.
2. Classify retryable vs non-retryable failures.
3. Design dead-letter structure.
4. Handle invalid-rate threshold breach.
5. Explain partial write recovery.
```

Expected skills:

```text
structured logging
error classification
dead-letter design
threshold failure
idempotency
checkpoint safety
```

Passing standard:

```text
Average score >= 4/5.
Candidate gives realistic production-safe answers.
```


## 71. Timed Drill Protocol

Use this timing protocol.

### Unit test drill

```text
10-20 minutes
```

### Pipeline test drill

```text
25-40 minutes
```

### Reliability scenario

```text
30-45 minutes
```

Per drill:

```text
Minute 0-3:
Clarify function/pipeline behavior.

Minute 3-6:
Identify success, failure, and edge cases.

Minute 6-25:
Write tests or design handling.

Minute 25-35:
Add observability and recovery discussion.

Minute 35-45:
Explain trade-offs and production safety.
```

If candidate only tests happy path:

```text
Stop and ask for failure and edge-case tests.
```


## 72. Review Checklist

Review reliability answers using:

```text
1. Did candidate separate pure logic from I/O?
2. Did candidate test success and failure cases?
3. Did candidate test edge cases?
4. Did candidate use clear assertions?
5. Did candidate test exceptions when relevant?
6. Did candidate avoid real external calls in unit tests?
7. Did candidate use fakes/mocks appropriately?
8. Did candidate test bad input?
9. Did candidate test invalid records with reasons?
10. Did candidate test aggregations and joins?
11. Did candidate test idempotency?
12. Did candidate test checkpoint behavior?
13. Did candidate classify errors correctly?
14. Did candidate distinguish retryable/non-retryable?
15. Did candidate avoid bare except?
16. Did candidate design useful logs?
17. Did candidate avoid logging secrets/PII?
18. Did candidate define metrics and alerts?
19. Did candidate handle partial failures?
20. Did candidate connect answer to Data Engineering production?
```

Verdict examples:

```text
Only happy-path tests.
Good tests but no error classification.
Good logging but unsafe PII exposure.
Good retry idea but no max limit.
Good error handling but no idempotency.
Interview-ready.
Strong.
```


## 73. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Only happy-path tests | Edge-case test drills |
| Cannot test exceptions | pytest.raises drills |
| Cannot test files | tmp_path drills |
| Calls real API in tests | fake client drills |
| No invalid-record tests | validation/dead-letter drills |
| No join tests | matched/unmatched/cardinality drills |
| No idempotency tests | rerun tests |
| No checkpoint tests | save/load/resume drills |
| Uses print | logging drills |
| Logs secrets | redaction drills |
| Bare except | specific exception drills |
| Retries everything | retry classification drills |
| No max retries | bounded retry drills |
| No dead-letter design | invalid record storage drills |
| No metrics/alerts | observability drills |
| Partial failure confusion | checkpoint/idempotency drills |

If weakness repeats:

```text
Use modes/weakness-repair-mode.md.
```


## 74. Communication Scripts

### Testing script

```text
I would keep transformation and validation logic in pure functions, then unit test success cases, edge cases, and invalid inputs.
```

### File test script

```text
For file processing, I would use temporary files in tests and verify clean output, invalid output, row counts, and malformed input behavior.
```

### API test script

```text
I would not call the real API in unit tests. I would use a fake client to test pagination, retries, and error classification.
```

### Logging script

```text
I would log structured context like run_id, input file, records read/written, invalid count, retry count, checkpoint, and duration.
```

### Error handling script

```text
I classify errors first. Transient dependency errors can be retried, data-quality errors go to dead-letter or fail threshold, and schema/config errors fail fast.
```

### Retry script

```text
I retry only retryable failures with bounded exponential backoff and jitter. I do not retry permanent 4xx, schema, or config errors blindly.
```

### Dead-letter script

```text
Invalid records should be written to a dead-letter path with row/page context, record id, redacted raw data, and error reasons.
```

### Idempotency script

```text
Because tasks can retry, writes must be idempotent and checkpoints should advance only after successful persistence.
```


## 75. Candidate Self-Review Questions

After every reliability problem, candidate should answer:

```text
1. What behavior am I testing?
2. What is the happy path?
3. What are the edge cases?
4. What are the failure cases?
5. Is this unit, integration, or end-to-end?
6. Can this be tested without external dependencies?
7. Do I need a fake or mock?
8. What data-quality rules must be tested?
9. What row counts should be validated?
10. What logs should exist?
11. What metrics should exist?
12. What should trigger alert?
13. Is the error retryable?
14. Is there a max retry limit?
15. What happens to invalid records?
16. Is output idempotent?
17. When is checkpoint saved?
18. What secrets/PII must not be logged?
19. What would happen during partial failure?
20. How would production operators debug this?
```

If candidate cannot answer these:

```text
The reliability design is not interview-ready.
```


## 76. Maintenance Drills

After completing testing/logging/errors, maintain skill with:

```text
1 unit test drill per week
1 validation/dead-letter drill per week
1 file/API fake dependency drill every 2 weeks
1 retry/error classification drill every 2 weeks
1 logging/observability drill every 2 weeks
1 full reliability mock every month
```

Maintenance rotation:

```text
Week 1: pure function tests + validators
Week 2: file tests + invalid output
Week 3: API fake client + retry classification
Week 4: observability + partial failure scenarios
```

If score drops below 4:

```text
Run modes/weakness-repair-mode.md for failed topic.
```


## 77. Progress Tracking Template

Use this progress format.

```text
# Testing, Logging, and Error Handling Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

Unit testing:
Assertions:
pytest raises:
Parameterized tests:
Fixtures:
tmp_path:
Fake clients:
Mocking:
Transform tests:
Validation tests:
Aggregation tests:
Dedup tests:
Join tests:
File tests:
API tests:
Checkpoint tests:
Idempotency tests:
Logging basics:
Structured logging:
PII-safe logging:
caplog:
Error classification:
Retry policy:
Backoff/jitter:
Dead-letter:
Invalid threshold:
Partial failure:
Metrics:
Alerts:
Incident reasoning:

## Repeated Mistakes

-

## Repair Items

-

## Next Practice

Today:
This week:
Next mock:
```


## 78. Final Exit Test

Candidate passes testing/logging/errors when they can solve/explain:

```text
1. Unit test a transform function.
2. Unit test a validation function.
3. Test parser edge cases with parameterized tests.
4. Test exceptions using pytest.raises.
5. Test file processing using tmp_path.
6. Test JSONL invalid-line handling.
7. Test dead-letter output.
8. Test aggregation results.
9. Test deduplication keep rule.
10. Test join matched/unmatched behavior.
11. Test source-target reconciliation.
12. Test API pagination with fake client.
13. Test retry classification.
14. Test rate-limit parsing.
15. Test checkpoint save/load.
16. Test idempotent rerun behavior.
17. Test logs with caplog conceptually or practically.
18. Design structured logs for a pipeline.
19. Explain what metrics to emit.
20. Explain what alerts to create.
21. Classify data-quality vs schema vs dependency failures.
22. Explain retryable vs non-retryable errors.
23. Explain bounded backoff and jitter.
24. Explain row-level vs job-level errors.
25. Design dead-letter record structure.
26. Enforce invalid-rate threshold.
27. Avoid logging secrets and PII.
28. Handle partial write failure.
29. Explain checkpoint safety.
30. Explain production incident debugging.
```

Passing standard:

```text
Average score >= 4/5.
No bare except.
No silent bad-row dropping.
No blind retries.
No unsafe PII logging.
No missing test strategy.
No missing idempotency/checkpoint explanation.
Can connect reliability behavior to Data Engineering interviews.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles tests, logs, metrics, alerts, retries, dead-letter, partial failure, and production trade-offs clearly under pressure.
```


## 79. Final Summary

Testing, logging, and error handling are core reliability skills for Data Engineering interviews.

They map directly to:

```text
ETL script reliability
API ingestion reliability
file processing reliability
data-quality checks
pipeline observability
warehouse load safety
backfill safety
orchestration retry safety
production debugging
incident response
schema drift handling
dead-letter processing
idempotent reruns
```

The candidate must master:

```text
unit testing
pytest assertions
pytest.raises
parameterized tests
fixtures
tmp_path
fake clients
transformation tests
validation tests
aggregation tests
dedupe tests
join tests
checkpoint tests
idempotency tests
logging basics
structured logging
PII-safe logs
error classification
retry policies
bounded backoff
timeouts
dead-letter design
invalid thresholds
metrics
alerts
partial failure recovery
production incident reasoning
```

The mentor must be strict:

```text
Bare except → not interview-ready.
Print-only debugging → not interview-ready.
No invalid-record strategy → not interview-ready.
Blind retries → not interview-ready.
No test strategy → not interview-ready.
No structured logs/metrics → not interview-ready.
No idempotency/checkpoint safety → not interview-ready.
```

The goal is not to memorize pytest or logging syntax.

The goal is to design Data Engineering code that is correct, observable, recoverable, secure, and safe under real production failures.


## 80. Problem Card Appendix

### Card 1: Test Transform Function

Topic:

```text
unit testing
```

Core idea:

```text
Verify field mapping and normalization.
```

Data Engineering connection:

```text
Raw-to-clean ETL.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Test Validator

Topic:

```text
unit testing
```

Core idea:

```text
Verify invalid reasons.
```

Data Engineering connection:

```text
Data-quality rules.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Test Parser Edge Cases

Topic:

```text
parameterized tests
```

Core idea:

```text
Cover invalid numeric/date values.
```

Data Engineering connection:

```text
Dirty data handling.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Test Required Columns

Topic:

```text
exception test
```

Core idea:

```text
Fail on schema missing.
```

Data Engineering connection:

```text
Schema contract.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Test JSONL Bad Line

Topic:

```text
tmp_path
```

Core idea:

```text
Malformed line becomes invalid record.
```

Data Engineering connection:

```text
Raw landing.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Test Dead Letter

Topic:

```text
file output
```

Core idea:

```text
Invalid records written with reasons.
```

Data Engineering connection:

```text
Replay/debugging.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Test Aggregation

Topic:

```text
data correctness
```

Core idea:

```text
Totals and counts are correct.
```

Data Engineering connection:

```text
Metrics pipeline.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Test Latest Record

Topic:

```text
dedupe
```

Core idea:

```text
Keep latest by updated_at.
```

Data Engineering connection:

```text
Incremental sync.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Test Join Unmatched

Topic:

```text
reconciliation
```

Core idea:

```text
Detect missing dimension keys.
```

Data Engineering connection:

```text
Fact enrichment.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Test API Pagination

Topic:

```text
fake client
```

Core idea:

```text
Fetch all pages without real API.
```

Data Engineering connection:

```text
SaaS ingestion.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Test Retry Policy

Topic:

```text
error classification
```

Core idea:

```text
Retry 5xx/429 not 400.
```

Data Engineering connection:

```text
Dependency resilience.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Test Checkpoint

Topic:

```text
resumability
```

Core idea:

```text
Save/load progress.
```

Data Engineering connection:

```text
Partial failure recovery.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Test Idempotency

Topic:

```text
rerun safety
```

Core idea:

```text
Same input twice gives same output.
```

Data Engineering connection:

```text
Orchestrator retries.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Test Logging

Topic:

```text
caplog
```

Core idea:

```text
Summary counts in logs.
```

Data Engineering connection:

```text
Observability.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Redaction Test

Topic:

```text
security
```

Core idea:

```text
PII/secrets masked.
```

Data Engineering connection:

```text
Safe diagnostics.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Invalid Threshold

Topic:

```text
data quality
```

Core idea:

```text
Fail when bad rows exceed threshold.
```

Data Engineering connection:

```text
Schema drift detection.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Partial Failure

Topic:

```text
recovery
```

Core idea:

```text
Checkpoint only after write.
```

Data Engineering connection:

```text
No data loss.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Metrics Design

Topic:

```text
observability
```

Core idea:

```text
Define counters/gauges.
```

Data Engineering connection:

```text
Monitoring.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Alert Design

Topic:

```text
operations
```

Core idea:

```text
Actionable alert thresholds.
```

Data Engineering connection:

```text
Incident response.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Incident Scenario

Topic:

```text
debugging
```

Core idea:

```text
Use logs/metrics/checkpoints to diagnose.
```

Data Engineering connection:

```text
Production support.
```

Candidate must be able to explain:

```text
1. What behavior is tested or handled.
2. Why this matters in data pipelines.
3. Code or pseudocode.
4. Edge cases.
5. Failure mode.
6. Logging/metrics if relevant.
7. Production safety note.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 81. Data Engineering Scenario Appendix

### Scenario 1: Malformed Vendor File

Pattern:

```text
file parsing + schema validation
```

Task:

```text
Handle missing header and invalid rows.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: API Outage

Pattern:

```text
retry + alert
```

Task:

```text
Retry transient errors and fail after max attempts.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: Rate Limit Spike

Pattern:

```text
429 + Retry-After
```

Task:

```text
Respect rate limits and emit metrics.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: Warehouse Load Failure

Pattern:

```text
staging + idempotency
```

Task:

```text
Avoid partial final-table corruption.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: Duplicate Event Delivery

Pattern:

```text
idempotency
```

Task:

```text
Deduplicate by event_id and test rerun.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: Late Updates

Pattern:

```text
lookback + dedupe
```

Task:

```text
Avoid missing late-arriving records.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: Schema Drift

Pattern:

```text
contract test + alert
```

Task:

```text
Detect missing/new fields.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: Count Drop to Zero

Pattern:

```text
anomaly detection
```

Task:

```text
Do not advance watermark blindly.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: PII in Bad Records

Pattern:

```text
redaction
```

Task:

```text
Safely capture invalid records.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: Checkpoint Corruption

Pattern:

```text
checkpoint validation
```

Task:

```text
Fail clearly and avoid bad resume.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: Join Explosion

Pattern:

```text
cardinality validation
```

Task:

```text
Prevent many-to-many row multiplication.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Bad Date Parsing

Pattern:

```text
validation
```

Task:

```text
Coerce, detect, and dead-letter invalid timestamps.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: Invalid Rate Breach

Pattern:

```text
threshold failure
```

Task:

```text
Fail if bad records exceed allowed ratio.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Manual Rerun

Pattern:

```text
idempotent output
```

Task:

```text
Safe rerun after failed task.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: Debug Production Failure

Pattern:

```text
logs + metrics
```

Task:

```text
Use run_id, counts, and error categories.
```

Minimum expected answer:

```text
1. Classify the error.
2. Explain detection.
3. Explain handling.
4. Explain logging/metrics.
5. Explain tests.
6. Explain recovery/idempotency.
```

Passing score:

```text
4/5 or higher.
```


## 82. Drill Appendix

### Drill 1: Assertion Drill

Task:

```text
Write clear assertions for transform outputs.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Exception Drill

Task:

```text
Test schema errors with pytest.raises.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Parameterization Drill

Task:

```text
Test parser edge cases with multiple inputs.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Fixture Drill

Task:

```text
Create reusable valid/invalid test records.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: tmp_path Drill

Task:

```text
Test file read/write behavior with temporary files.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: Fake Client Drill

Task:

```text
Test API pagination and retry behavior.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: caplog Drill

Task:

```text
Verify critical logs include counts/run_id.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Validation Drill

Task:

```text
Test invalid records include error reasons.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Aggregation Drill

Task:

```text
Test totals, counts, and empty input.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Dedupe Drill

Task:

```text
Test first/last/latest keep rules.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Join Drill

Task:

```text
Test matched/unmatched/duplicate key behavior.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Checkpoint Drill

Task:

```text
Test save/load and resume logic.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Idempotency Drill

Task:

```text
Run same input twice and compare outputs.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Retry Drill

Task:

```text
Classify and test retryable vs non-retryable errors.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Backoff Drill

Task:

```text
Explain bounded exponential backoff with jitter.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Dead-Letter Drill

Task:

```text
Design and test invalid-record output.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Threshold Drill

Task:

```text
Fail when invalid ratio is too high.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Redaction Drill

Task:

```text
Mask sensitive fields before logs/dead-letter.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 19: Metrics Drill

Task:

```text
Define metrics for a pipeline.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 20: Incident Drill

Task:

```text
Debug a failed pipeline using logs and metrics.
```

Minimum passing answer:

```text
1. Identify behavior.
2. Write test/design/code.
3. Cover success and failure cases.
4. Explain edge cases.
5. Explain DE production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 83. Quick Reference Cards

### Quick Card 1: unit test

Summary:

```text
Test one function in isolation.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 2: integration test

Summary:

```text
Test multiple components or I/O boundary.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 3: fixture

Summary:

```text
Reusable test setup/data.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 4: mock/fake

Summary:

```text
Replace external dependency in tests.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 5: pytest.raises

Summary:

```text
Assert expected exception.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 6: tmp_path

Summary:

```text
Temporary filesystem for tests.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 7: caplog

Summary:

```text
Capture and assert logs.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 8: dead-letter

Summary:

```text
Invalid records with context and reasons.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 9: retryable

Summary:

```text
Transient errors that may succeed later.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 10: non-retryable

Summary:

```text
Permanent/config/data errors.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 11: backoff

Summary:

```text
Increasing wait between retries.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 12: jitter

Summary:

```text
Randomness to avoid retry storms.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 13: idempotency

Summary:

```text
Safe rerun without duplicates/corruption.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 14: checkpoint

Summary:

```text
Saved progress after successful work.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 15: structured logs

Summary:

```text
Logs with run_id/counts/context.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 16: metrics

Summary:

```text
Numeric pipeline measurements.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 17: alerts

Summary:

```text
Actionable notifications on failure/anomaly.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```

### Quick Card 18: PII redaction

Summary:

```text
Mask sensitive fields in diagnostics.
```

Interview check:

```text
Give one code example and one Data Engineering production example.
```


## 84. Interview FAQ

### FAQ 1: Should I catch all exceptions?

Answer:

```text
No. Catch specific exceptions at the right boundary. Re-raise unexpected errors with context.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 2: Should invalid records fail the whole job?

Answer:

```text
Sometimes. A few can go to dead-letter, but high invalid rate should fail or alert.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 3: Should I retry every failed API call?

Answer:

```text
No. Retry transient failures only, with max attempts and backoff.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 4: Should logs include raw records?

Answer:

```text
Usually no. Log identifiers, counts, and error categories. Redact sensitive fields.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 5: How do I test API code?

Answer:

```text
Use fake clients or mocks. Do not call live APIs in unit tests.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 6: How do I test file code?

Answer:

```text
Use tmp_path and small test files.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 7: How do I test idempotency?

Answer:

```text
Run the same input twice and assert output does not change or duplicate.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 8: How do I test checkpointing?

Answer:

```text
Save/load checkpoint and simulate failure before/after checkpoint.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 9: What should I log?

Answer:

```text
run_id, input, output, counts, invalids, retries, checkpoint, duration, and error category.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```

### FAQ 10: What should trigger alert?

Answer:

```text
Failures, schema drift, invalid-rate breach, zero/unusual record count, missing partitions, freshness lag.
```

Candidate should also explain:

```text
1. Why this matters.
2. What can go wrong.
3. How to test it.
4. How to observe it in production.
```
