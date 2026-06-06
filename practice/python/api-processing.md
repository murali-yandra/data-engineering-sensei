# API Processing Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/python/api-processing.md
```

This guide teaches and drills **API processing for Data Engineering interviews using Python**.

This is not a generic REST API tutorial. It is an interview-focused guide for Data Engineering candidates who need to consume APIs, paginate data, handle rate limits, retry transient failures, process JSON safely, perform incremental syncs, design extraction logic, and explain production-grade API ingestion.

API processing is high-ROI for Data Engineering interviews because many real data pipelines ingest from:

- SaaS APIs
- internal microservice APIs
- payment APIs
- CRM APIs
- marketing APIs
- analytics APIs
- ticketing APIs
- banking APIs
- shipping/logistics APIs
- REST endpoints
- GraphQL endpoints
- webhook payloads
- paginated exports
- cursor-based feeds
- rate-limited endpoints
- unstable third-party integrations

Use this guide with:

- `docs/python-interview-guide.md`
- `docs/data-engineering-fundamentals.md`
- `docs/etl-elt-pipelines-guide.md`
- `docs/error-handling-playbook.md`
- `docs/cloud-data-platforms-guide.md`
- `docs/system-design-guide.md`
- `docs/assessment-rubric.md`
- `docs/communication-rubric.md`
- `modes/python-drill-mode.md`
- `modes/data-engineering-fundamentals-mode.md`
- `modes/project-deep-dive-mode.md`
- `modes/system-design-mode.md`
- `modes/interview-mode.md`
- `modes/review-mode.md`
- `modes/feedback-mode.md`
- `modes/weakness-repair-mode.md`
- `practice/python`
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

The purpose of this guide is to make the candidate strong at Python API ingestion and processing.

The candidate should learn to answer:

```text
How do I call an API safely in Python?
How do I handle HTTP status codes?
How do I parse JSON safely?
How do I paginate through an API?
How do I handle cursor pagination?
How do I handle offset pagination?
How do I handle next-page URLs?
How do I retry transient failures?
How do I avoid retrying permanent failures?
How do I respect rate limits?
How do I use exponential backoff?
How do I make extraction idempotent?
How do I perform incremental sync?
How do I checkpoint progress?
How do I process nested JSON records?
How do I flatten records?
How do I validate API records?
How do I write API data to files/tables?
How do I design a robust API ingestion pipeline?
How do I discuss this in a Data Engineering interview?
```

A candidate is interview-ready only when they can:

```text
write clean API client code
separate request, pagination, transform, and persistence logic
handle status codes intentionally
handle timeouts
handle retries with backoff
handle rate limits
handle pagination without infinite loops
parse nested JSON safely
validate required fields
collect invalid records separately
checkpoint incremental extraction
avoid duplicate records
explain idempotency
explain observability
explain API ingestion failure modes
explain trade-offs between batch API pulls, streaming, and webhooks
```


## 2. Why API Processing Matters for Data Engineers

Many Data Engineering jobs involve API ingestion.

Real examples:

```text
Pull transactions from payment processor API.
Pull tickets from Zendesk/Jira API.
Pull customer data from CRM API.
Pull campaign metrics from advertising API.
Pull warehouse costs from cloud billing API.
Pull exchange rates from financial API.
Pull shipment statuses from logistics API.
Pull experiment data from internal services.
Pull audit logs from security APIs.
Pull usage metrics from SaaS APIs.
Process webhook payloads from product events.
Sync paginated user records into a data warehouse.
```

Interviewers test API processing because it exposes practical engineering maturity:

```text
Can the candidate handle unreliable systems?
Can they avoid data loss?
Can they avoid duplicate loading?
Can they reason about retries and idempotency?
Can they manage pagination?
Can they process nested JSON?
Can they explain rate limiting?
Can they design incremental extraction?
Can they separate concerns in code?
```

A weak answer:

```text
requests.get(url).json()
```

A strong answer:

```text
Use a client with timeout, retries, pagination, rate-limit handling, validation, checkpointing, idempotent writes, metrics, and dead-letter handling.
```


## 3. Core Mental Model

API ingestion is not only making HTTP requests.

A production API extraction pipeline has stages:

```text
1. Configure endpoint, auth, parameters, and timeout.
2. Send request.
3. Handle HTTP status code.
4. Retry transient failures.
5. Respect rate limits.
6. Parse response body.
7. Validate response shape.
8. Extract records.
9. Paginate until complete.
10. Transform/flatten records.
11. Validate individual records.
12. Write valid records.
13. Store invalid records separately.
14. Checkpoint progress.
15. Emit metrics/logs.
16. Alert on failure or data-quality issues.
```

Core interview line:

```text
For API ingestion, correctness is not only about getting data once. It is about making the extraction repeatable, resumable, observable, and safe under partial failures.
```


## 4. API Processing Vocabulary

Important terms:

```text
Endpoint:
URL path where API resource is available.

HTTP method:
GET, POST, PUT, PATCH, DELETE.

Status code:
Numeric response result such as 200, 400, 401, 429, 500.

Request headers:
Metadata sent with request, often includes auth token.

Query parameters:
URL parameters such as page, limit, start_date, updated_after.

Payload/body:
Request body, usually JSON for POST/PATCH.

Pagination:
Fetching records across multiple pages.

Cursor:
Token returned by API to fetch next page.

Rate limit:
Maximum requests allowed per time window.

Retry:
Try request again after transient failure.

Backoff:
Increasing delay between retries.

Timeout:
Maximum time to wait for API response.

Checkpoint:
Saved progress marker for resumable extraction.

Idempotency:
Rerunning does not create incorrect duplicates or side effects.

Watermark:
Last successfully processed timestamp/id for incremental sync.

Dead-letter:
Storage for invalid/unprocessable records.
```


## 5. HTTP Methods for Data Engineers

Common HTTP methods:

| Method | Typical API Use | Data Engineering Example |
|---|---|---|
| GET | Read data | Fetch transactions/users/orders |
| POST | Create or query complex data | Submit export job / GraphQL query |
| PUT | Replace resource | Rare in ingestion |
| PATCH | Partial update | Rare in ingestion |
| DELETE | Delete resource | Rare in ingestion |

Most DE ingestion is:

```text
GET with query parameters
POST to start export job
POST for GraphQL queries
GET to poll export status
GET to download export file
```

Interview line:

```text
For extraction, most APIs use GET, but some analytics APIs use POST because filters are complex or payloads exceed URL limits.
```


## 6. HTTP Status Code Handling

Status codes should be handled intentionally.

### 2xx success

```text
200 OK
201 Created
202 Accepted
204 No Content
```

### 3xx redirect

Usually handled by HTTP client, but be aware.

### 4xx client errors

```text
400 Bad Request → request issue
401 Unauthorized → auth issue
403 Forbidden → permission issue
404 Not Found → wrong endpoint/resource missing
409 Conflict → state conflict
422 Unprocessable Entity → validation issue
429 Too Many Requests → rate limit
```

### 5xx server errors

```text
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

Retry policy:

```text
Retry: 408, 429, 500, 502, 503, 504
Usually do not retry: 400, 401, 403, 404, 422
```

Interview line:

```text
I retry transient failures like 429 and 5xx, but I do not blindly retry permanent 4xx errors because that can worsen load and hide bad requests.
```


## 7. Standard Answer Framework

Use this framework for API processing interview answers:

```text
1. Restate the API ingestion requirement.
2. Clarify API shape:
   - method
   - endpoint
   - auth
   - pagination
   - rate limits
   - response schema
   - incremental field
3. Explain request logic:
   - timeout
   - headers
   - params
4. Explain status-code handling.
5. Explain retries/backoff.
6. Explain pagination loop.
7. Explain response parsing.
8. Explain record validation.
9. Explain transformation/flattening.
10. Explain checkpointing/watermark.
11. Explain idempotent writes.
12. Explain error handling and dead-letter records.
13. Explain observability.
14. Write code or pseudocode.
15. Discuss edge cases and trade-offs.
```

Short version:

```text
Request:
Retry:
Pagination:
Parse:
Validate:
Persist:
Checkpoint:
Observe:
```

Strict rule:

```text
No API ingestion answer is complete without timeout, pagination, retries, and idempotency discussion.
```


## 8. Scoring Rubric

Score each API processing answer from 0 to 5.

### Score 0

No meaningful API processing answer.

### Score 1

Only calls API and prints JSON.

### Score 2

Can call API but lacks pagination, retries, or validation.

### Score 3

Handles pagination and basic errors but weak on idempotency, checkpointing, or observability.

### Score 4

Interview-ready. Has robust request handling, pagination, retries, validation, checkpointing, and clear code structure.

### Score 5

Strong. Covers edge cases, production failure modes, rate limits, idempotent loading, schema drift, observability, and scaling trade-offs.

Do not give 4+ if:

```text
candidate does not use timeout
candidate does not handle pagination
candidate retries all errors blindly
candidate ignores 429/rate limits
candidate cannot explain idempotency
candidate cannot explain checkpointing
candidate assumes response schema always valid
candidate cannot handle nested JSON safely
candidate has no invalid-record strategy
candidate cannot explain how to avoid duplicates
candidate has no logging/metrics
```


## 9. Python Libraries

Common Python libraries for API processing:

```text
requests:
Simple synchronous HTTP client.

httpx:
Modern HTTP client supporting sync and async.

aiohttp:
Async HTTP client for high-concurrency APIs.

urllib:
Standard library option, less ergonomic.

pydantic:
Data validation and parsing.

tenacity:
Retry library.

backoff:
Retry/backoff library.

json:
Standard JSON parsing.

datetime:
Timestamp parsing and watermarks.

logging:
Structured logs.

pathlib:
File paths for local persistence.

csv/parquet libraries:
Persistence depending output format.
```

Interview-safe default:

```text
Use requests for simple examples.
Mention httpx/aiohttp for high-concurrency API ingestion.
```

Important:

```text
Do not introduce async unless you can explain rate limits and backpressure.
```


## 10. Basic API Request Template

Basic request with timeout and error handling:

```python
import requests

def fetch_json(url, headers=None, params=None, timeout=30):
    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=timeout,
    )

    response.raise_for_status()
    return response.json()
```

This is acceptable for a simple starting point.

But for interviews, explain limitations:

```text
No retry.
No rate-limit handling.
No pagination.
No schema validation.
No checkpointing.
No observability.
```

Stronger interview wording:

```text
I would start with a small fetch function, then wrap it with retry, pagination, validation, and checkpointing for production ingestion.
```


## 11. Request Function with Status Handling

A better request function separates status handling.

```python
import requests

RETRYABLE_STATUS_CODES = {408, 429, 500, 502, 503, 504}

class ApiRequestError(Exception):
    pass

class RetryableApiError(ApiRequestError):
    pass

class NonRetryableApiError(ApiRequestError):
    pass

def get_json_once(url, headers=None, params=None, timeout=30):
    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=timeout,
    )

    if response.status_code in RETRYABLE_STATUS_CODES:
        raise RetryableApiError(
            f"Retryable status={response.status_code}, body={response.text[:500]}"
        )

    if response.status_code >= 400:
        raise NonRetryableApiError(
            f"Non-retryable status={response.status_code}, body={response.text[:500]}"
        )

    try:
        return response.json()
    except ValueError as exc:
        raise NonRetryableApiError("Response was not valid JSON") from exc
```

Interview points:

```text
Separate retryable and non-retryable errors.
Limit response body in error message to avoid huge logs.
Handle invalid JSON.
Use timeout.
```


## 12. Retry with Exponential Backoff

Retry is needed for transient failures.

Retryable cases:

```text
network timeout
connection reset
429 rate limit
500/502/503/504 server errors
```

Do not blindly retry:

```text
400 bad request
401 unauthorized
403 forbidden
404 not found
422 validation error
```

Manual retry template:

```python
import random
import time
import requests

RETRYABLE_STATUS_CODES = {408, 429, 500, 502, 503, 504}

class ApiError(Exception):
    pass

def fetch_with_retries(url, headers=None, params=None, max_attempts=4, timeout=30):
    last_error = None

    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=timeout,
            )

            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")

                if retry_after:
                    time.sleep(int(retry_after))
                else:
                    sleep_seconds = min(2 ** attempt, 60) + random.random()
                    time.sleep(sleep_seconds)

                last_error = ApiError("Rate limited")
                continue

            if response.status_code in RETRYABLE_STATUS_CODES:
                last_error = ApiError(f"Retryable status {response.status_code}")
                sleep_seconds = min(2 ** attempt, 60) + random.random()
                time.sleep(sleep_seconds)
                continue

            if response.status_code >= 400:
                raise ApiError(f"Non-retryable status {response.status_code}")

            return response.json()

        except (requests.Timeout, requests.ConnectionError) as exc:
            last_error = exc
            sleep_seconds = min(2 ** attempt, 60) + random.random()
            time.sleep(sleep_seconds)

    raise ApiError(f"Request failed after {max_attempts} attempts: {last_error}")
```

Interview line:

```text
I use bounded retries with exponential backoff and jitter so temporary issues are retried without causing a thundering herd.
```


## 13. Rate Limit Handling

Rate limits are common in APIs.

Signals:

```text
HTTP 429
Retry-After header
X-RateLimit-Limit
X-RateLimit-Remaining
X-RateLimit-Reset
API documentation
```

Good behavior:

```text
Respect Retry-After.
Use backoff with jitter.
Limit concurrency.
Persist checkpoint before waiting/failing.
Avoid infinite retry loops.
Expose metrics for rate-limit hits.
```

Bad behavior:

```text
Retry immediately in a tight loop.
Increase concurrency after 429.
Ignore Retry-After.
Fail entire pipeline without checkpoint.
```

Interview line:

```text
When I receive 429, I respect Retry-After if provided; otherwise I use capped exponential backoff with jitter and keep extraction resumable through checkpoints.
```


## 14. Timeout Handling

Always set timeouts.

Bad:

```python
requests.get(url)
```

Good:

```python
requests.get(url, timeout=30)
```

Why:

```text
Without a timeout, a pipeline task can hang indefinitely.
```

Timeout types:

```text
connect timeout:
Time to connect to server.

read timeout:
Time waiting for response data.
```

Requests supports tuple timeout:

```python
requests.get(url, timeout=(5, 30))
```

Meaning:

```text
connect timeout = 5 seconds
read timeout = 30 seconds
```

Interview line:

```text
I always set request timeouts because a hung API call should fail predictably and be retried or checkpointed.
```


## 15. Pagination Overview

APIs rarely return all records in one response.

Common pagination types:

```text
1. Page number pagination
2. Offset/limit pagination
3. Cursor pagination
4. Next URL pagination
5. Link header pagination
6. Time-window pagination
7. Export job pagination
```

Candidate must ask:

```text
How does the API paginate?
Where is the next page token?
What indicates end of data?
Is page size configurable?
Can records change during pagination?
Is ordering guaranteed?
Are duplicates possible across pages?
```

Interview line:

```text
I would not assume one response contains all data. I would implement pagination based on the API's documented next-page mechanism and protect against infinite loops.
```


## 16. Page Number Pagination

Page number pagination uses:

```text
page=1
page=2
page=3
```

Example response:

```json
{
  "data": [...],
  "page": 1,
  "total_pages": 10
}
```

Template:

```python
def fetch_page_number_api(base_url, headers=None, page_size=100):
    page = 1

    while True:
        payload = fetch_with_retries(
            base_url,
            headers=headers,
            params={"page": page, "page_size": page_size},
        )

        records = payload.get("data", [])

        if not records:
            break

        for record in records:
            yield record

        total_pages = payload.get("total_pages")

        if total_pages is not None and page >= total_pages:
            break

        page += 1
```

Risks:

```text
If data changes while paging, page numbers can skip or duplicate records.
Cursor pagination is usually safer.
```


## 17. Offset Pagination

Offset pagination uses:

```text
offset=0&limit=100
offset=100&limit=100
offset=200&limit=100
```

Template:

```python
def fetch_offset_api(base_url, headers=None, limit=100):
    offset = 0

    while True:
        payload = fetch_with_retries(
            base_url,
            headers=headers,
            params={"offset": offset, "limit": limit},
        )

        records = payload.get("data", [])

        if not records:
            break

        for record in records:
            yield record

        if len(records) < limit:
            break

        offset += limit
```

Risks:

```text
Large offsets can be slow.
Changing data during extraction can cause missing/duplicate records.
```

Interview line:

```text
Offset pagination is simple but can be unstable on changing datasets; cursor pagination is preferred when available.
```


## 18. Cursor Pagination

Cursor pagination uses a token returned by the API.

Example response:

```json
{
  "data": [...],
  "next_cursor": "abc123"
}
```

Template:

```python
def fetch_cursor_api(base_url, headers=None, page_size=100):
    cursor = None
    seen_cursors = set()

    while True:
        params = {"limit": page_size}

        if cursor:
            params["cursor"] = cursor

        payload = fetch_with_retries(
            base_url,
            headers=headers,
            params=params,
        )

        records = payload.get("data", [])

        for record in records:
            yield record

        next_cursor = payload.get("next_cursor")

        if not next_cursor:
            break

        if next_cursor in seen_cursors:
            raise RuntimeError(f"Pagination loop detected for cursor={next_cursor}")

        seen_cursors.add(next_cursor)
        cursor = next_cursor
```

Why cursor is preferred:

```text
More stable for changing datasets.
Often better performance.
Works naturally with ordered feeds.
```

Interview line:

```text
I prefer cursor pagination when available because it is usually safer than offset pagination for changing datasets.
```


## 19. Next URL Pagination

Some APIs return a full next page URL.

Example response:

```json
{
  "results": [...],
  "next": "https://api.example.com/items?page=2"
}
```

Template:

```python
def fetch_next_url_api(first_url, headers=None):
    url = first_url
    seen_urls = set()

    while url:
        if url in seen_urls:
            raise RuntimeError(f"Pagination loop detected for url={url}")

        seen_urls.add(url)

        payload = fetch_with_retries(url, headers=headers)
        records = payload.get("results", [])

        for record in records:
            yield record

        url = payload.get("next")
```

Interview points:

```text
Protect against next URL loops.
Do not accidentally drop headers/auth on next URL requests.
Check whether next is absolute or relative.
```


## 20. Link Header Pagination

Some APIs use HTTP Link headers.

Example:

```text
Link: <https://api.example.com/items?page=2>; rel="next"
```

In interviews, you can explain:

```text
I would parse the Link header to find rel="next" and continue until no next link exists.
```

Simplified parsing idea:

```python
def parse_next_link(link_header):
    if not link_header:
        return None

    parts = link_header.split(",")

    for part in parts:
        if 'rel="next"' in part:
            start = part.find("<") + 1
            end = part.find(">")
            return part[start:end]

    return None
```

Production note:

```text
Use a robust parser/library for complex Link headers.
```


## 21. Incremental Sync

Incremental sync fetches only new or changed data.

Common watermarks:

```text
updated_at
created_at
id
sequence_number
cursor
event_time
```

Basic incremental query:

```text
GET /transactions?updated_after=2025-01-01T00:00:00Z
```

Important design:

```text
Use high-watermark from successfully loaded data.
Store checkpoint only after successful write.
Use overlap/lookback window if API updates can arrive late.
Deduplicate by primary key and updated_at/version.
Use half-open boundaries if supported.
```

Risk:

```text
If you checkpoint before writing, data can be lost after a crash.
```

Interview line:

```text
For incremental sync, I checkpoint only after data is successfully persisted, and I make writes idempotent so reruns do not duplicate data.
```


## 22. Checkpointing

A checkpoint records extraction progress.

Examples:

```json
{
  "endpoint": "transactions",
  "last_successful_updated_at": "2025-01-01T00:00:00Z",
  "last_cursor": "abc123",
  "last_page": 42
}
```

Checkpoint storage:

```text
database table
object storage JSON file
workflow metadata store
Airflow variable/connection only for simple cases
state table in warehouse
```

Good checkpoint rules:

```text
Checkpoint after successful persistence.
Include endpoint/entity name.
Include extraction window.
Include run id.
Include record counts.
Keep previous checkpoint for rollback.
```

Bad checkpoint rules:

```text
Checkpoint before write.
Store only in local memory.
Overwrite checkpoint without audit trail.
Use current time as watermark without considering API lag.
```

Interview line:

```text
Checkpointing makes the pipeline resumable after partial failure.
```


## 23. Idempotency

Idempotency means rerunning the same job does not produce incorrect duplicate data or side effects.

For API ingestion, idempotency can be achieved by:

```text
upsert by primary key
merge by id + updated_at
write to staging table then merge
partition overwrite for fixed extraction window
deduplicate in target
include run_id and natural key
use idempotency keys for POST side effects
```

Example:

```text
If API page 5 was loaded and the task crashes before checkpoint, rerun may load page 5 again.
Idempotent writes prevent duplicates.
```

Interview line:

```text
I assume retries and reruns will happen, so the load step must be idempotent through upserts, merge keys, or partition overwrite.
```


## 24. JSON Processing Basics

APIs commonly return JSON.

JSON shapes:

```text
list of records
object with data list
object with nested fields
object with metadata and pagination
deeply nested records
```

Safe parsing:

```python
payload = response.json()
records = payload.get("data", [])
```

But do not blindly assume shape:

```python
if not isinstance(payload, dict):
    raise ValueError("Expected JSON object")

records = payload.get("data")

if not isinstance(records, list):
    raise ValueError("Expected data to be a list")
```

Interview line:

```text
I validate the response shape before processing records because APIs can return error payloads or schema changes even with a 200 status.
```


## 25. Safe Nested Field Access

Nested JSON often has missing fields.

Example:

```json
{
  "id": "txn_1",
  "customer": {
    "id": "cust_1",
    "address": {
      "country": "IN"
    }
  }
}
```

Helper:

```python
def get_nested(record, path, default=None):
    current = record

    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default

        current = current[key]

    return current
```

Usage:

```python
country = get_nested(record, ["customer", "address", "country"])
```

Interview line:

```text
I do not directly chain nested dictionary access unless fields are guaranteed; I use safe access and validation for required fields.
```


## 26. Flattening API Records

Flattening converts nested JSON into table-friendly records.

Example input:

```json
{
  "id": "txn_1",
  "amount": 100,
  "customer": {
    "id": "cust_1",
    "email": "a@example.com"
  }
}
```

Flattened output:

```json
{
  "transaction_id": "txn_1",
  "amount": 100,
  "customer_id": "cust_1",
  "customer_email": "a@example.com"
}
```

Code:

```python
def flatten_transaction(record):
    return {
        "transaction_id": record.get("id"),
        "amount": record.get("amount"),
        "currency": record.get("currency"),
        "created_at": record.get("created_at"),
        "customer_id": get_nested(record, ["customer", "id"]),
        "customer_email": get_nested(record, ["customer", "email"]),
    }
```

Important:

```text
Flattening should not silently drop required fields.
Validate after flattening.
```


## 27. Record Validation

Validate records before loading.

Example required fields:

```text
id
updated_at
amount
currency
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

Processing pattern:

```python
valid_rows = []
invalid_rows = []

for record in records:
    row = flatten_transaction(record)
    errors = validate_transaction(row)

    if errors:
        invalid_rows.append({"row": row, "errors": errors})
    else:
        valid_rows.append(row)
```

Interview line:

```text
I separate invalid records into a dead-letter path instead of crashing the whole batch for a small number of bad records, unless the error rate crosses a threshold.
```


## 28. Dead-Letter Records

A dead-letter store holds records that could not be processed.

Include:

```text
raw record
flattened row if available
error reasons
endpoint
run_id
timestamp
page/cursor
schema version if known
```

Why:

```text
debugging
reprocessing
auditability
data quality monitoring
vendor issue tracking
```

Do not:

```text
silently drop invalid records
only log invalid record count
store sensitive raw payloads without governance
```

Interview line:

```text
Invalid records should be captured with reasons and context so they can be fixed or replayed later.
```


## 29. Authentication Patterns

Common API authentication:

```text
API key in header
Bearer token
Basic auth
OAuth2 client credentials
OAuth2 refresh token
Signed requests
mTLS
```

Example bearer token:

```python
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
}
```

Security rules:

```text
Do not hardcode secrets.
Use secret manager or environment variables.
Never log tokens.
Rotate credentials.
Use least-privilege access.
```

Interview line:

```text
I would retrieve credentials from a secret manager or environment variable and avoid logging headers that contain tokens.
```


## 30. Environment Variables for Secrets

Simple local pattern:

```python
import os

def get_api_token():
    token = os.getenv("API_TOKEN")

    if not token:
        raise RuntimeError("API_TOKEN environment variable is missing")

    return token
```

Headers:

```python
headers = {
    "Authorization": f"Bearer {get_api_token()}",
    "Accept": "application/json",
}
```

Interview production note:

```text
For production, use a cloud secret manager or orchestration secret backend rather than plain environment variables when available.
```

Never do:

```python
token = "hardcoded_secret"
```


## 31. API Client Class Pattern

A client class keeps API logic organized.

```python
import requests
import time
import random

class ApiClient:
    RETRYABLE_STATUS_CODES = {408, 429, 500, 502, 503, 504}

    def __init__(self, base_url, token, timeout=30, max_attempts=4):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_attempts = max_attempts
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        })

    def get(self, path, params=None):
        url = f"{self.base_url}/{path.lstrip('/')}"

        for attempt in range(1, self.max_attempts + 1):
            response = self.session.get(
                url,
                params=params,
                timeout=self.timeout,
            )

            if response.status_code == 429:
                self._sleep_for_rate_limit(response, attempt)
                continue

            if response.status_code in self.RETRYABLE_STATUS_CODES:
                self._sleep_with_backoff(attempt)
                continue

            if response.status_code >= 400:
                raise RuntimeError(
                    f"Non-retryable API error: status={response.status_code}, body={response.text[:500]}"
                )

            return response.json()

        raise RuntimeError(f"API request failed after {self.max_attempts} attempts: {url}")

    def _sleep_for_rate_limit(self, response, attempt):
        retry_after = response.headers.get("Retry-After")

        if retry_after:
            time.sleep(int(retry_after))
        else:
            self._sleep_with_backoff(attempt)

    def _sleep_with_backoff(self, attempt):
        sleep_seconds = min(2 ** attempt, 60) + random.random()
        time.sleep(sleep_seconds)
```

Interview line:

```text
A client class centralizes auth, timeout, retries, status handling, and base URL construction.
```


## 32. Streaming Records with Generators

Generators are useful for pagination.

Instead of loading all pages into memory:

```python
def iter_records(client):
    cursor = None

    while True:
        params = {"limit": 100}

        if cursor:
            params["cursor"] = cursor

        payload = client.get("/items", params=params)
        records = payload.get("data", [])

        for record in records:
            yield record

        cursor = payload.get("next_cursor")

        if not cursor:
            break
```

Why:

```text
memory efficient
can process records page by page
can write batches incrementally
```

Interview line:

```text
I would use a generator or batch iterator so the pipeline does not need to hold the entire API result in memory.
```


## 33. Batch Writing Pattern

API records should often be written in batches.

Template:

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
for batch in batched(iter_records(client), batch_size=1000):
    write_batch(batch)
```

Why:

```text
avoid memory explosion
reduce write overhead
checkpoint after each successful batch/page
```

Interview line:

```text
I process and persist records in batches so large API extracts do not require loading everything into memory.
```


## 34. Writing JSON Lines

JSON Lines is a common raw landing format.

Each line is one JSON record.

```python
import json
from pathlib import Path

def write_jsonl(records, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False))
            file.write("\n")
```

Append mode for batch landing:

```python
def append_jsonl(records, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("a", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False))
            file.write("\n")
```

Interview line:

```text
I often land raw API responses as JSON Lines before transformation so replay and audit are possible.
```


## 35. Raw vs Clean Zones

A mature ingestion pattern:

```text
raw zone:
API response records as received, with metadata.

staging/bronze:
Parsed and lightly validated records.

clean/silver:
Flattened, typed, deduplicated records.

serving/gold:
Business-ready analytics tables.
```

Raw record metadata:

```text
run_id
endpoint
extracted_at
page_number
cursor
source_updated_at
raw_payload
```

Why raw landing matters:

```text
replay
debugging
schema drift analysis
audit
vendor dispute
backfill
```

Interview line:

```text
I prefer landing raw API data first, then transforming it, so extraction and transformation are decoupled and replayable.
```


## 36. Schema Drift

APIs can change.

Schema drift examples:

```text
new field appears
field disappears
field type changes
nested object becomes null
enum value changes
pagination key changes
error payload shape changes
```

Handling:

```text
validate required fields
allow optional fields
capture raw payload
track unknown fields if needed
alert on required-field missing rate
version transformation logic
use contracts where possible
```

Interview line:

```text
I assume API schemas can drift, so I validate required fields, keep raw payloads, and monitor invalid-record rates.
```


## 37. Deduplication

API ingestion can create duplicates.

Sources of duplicates:

```text
reruns
retry after partial write
same record appears on multiple pages
overlap lookback windows
API sends duplicate events
webhook redelivery
source updates during pagination
```

Dedup keys:

```text
id
id + updated_at
event_id
source_system + natural_key
hash of business fields
```

Example dedupe:

```python
def dedupe_by_id(records):
    latest = {}

    for record in records:
        record_id = record.get("id")

        if record_id is None:
            continue

        latest[record_id] = record

    return list(latest.values())
```

For latest by updated_at:

```python
def dedupe_latest_by_id(records):
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

Interview line:

```text
I make API ingestion idempotent by deduplicating or merging on stable source keys.
```


## 38. Incremental Sync with Lookback Window

APIs may deliver late updates.

Risk:

```text
If last watermark is 10:00 and a record updated at 09:59 arrives late, a strict updated_after=10:00 sync misses it.
```

Lookback strategy:

```text
query from last_watermark - lookback_duration
deduplicate/upsert by id + updated_at
advance checkpoint only after successful load
```

Pseudo-code:

```python
from datetime import timedelta

def compute_sync_start(last_watermark, lookback_minutes=10):
    return last_watermark - timedelta(minutes=lookback_minutes)
```

Interview line:

```text
I use a small overlap/lookback window for incremental APIs when late-arriving updates are possible, and rely on idempotent merge to remove duplicates.
```


## 39. API Extraction Function: End-to-End Skeleton

End-to-end skeleton:

```python
from datetime import datetime, timezone

def extract_endpoint(client, endpoint, checkpoint, write_batch, batch_size=1000):
    run_id = datetime.now(timezone.utc).isoformat()
    cursor = checkpoint.get("cursor")
    batch = []
    total_records = 0
    invalid_records = 0

    while True:
        params = {"limit": 100}

        if cursor:
            params["cursor"] = cursor

        payload = client.get(endpoint, params=params)

        records = payload.get("data", [])

        for raw_record in records:
            row = transform_record(raw_record)
            errors = validate_row(row)

            if errors:
                write_dead_letter(raw_record, row, errors, run_id)
                invalid_records += 1
                continue

            batch.append(row)

            if len(batch) >= batch_size:
                write_batch(batch)
                total_records += len(batch)
                batch = []

        next_cursor = payload.get("next_cursor")

        if batch:
            write_batch(batch)
            total_records += len(batch)
            batch = []

        checkpoint["cursor"] = next_cursor
        checkpoint["last_run_id"] = run_id
        checkpoint["total_records"] = total_records
        save_checkpoint(checkpoint)

        if not next_cursor:
            break

        cursor = next_cursor

    return {
        "run_id": run_id,
        "total_records": total_records,
        "invalid_records": invalid_records,
    }
```

Interview note:

```text
This skeleton shows separation of client, transform, validation, writing, and checkpointing.
```


## 40. Error Handling Strategy

API ingestion error categories:

```text
Request errors:
network timeout, connection error, DNS failure

HTTP errors:
429, 5xx, 4xx

Response errors:
invalid JSON, missing data key, unexpected schema

Record errors:
missing required field, bad type, invalid timestamp

Persistence errors:
write failure, constraint violation, warehouse unavailable

Checkpoint errors:
failed to save progress

Data quality errors:
too many invalid records, unexpected count drop
```

Handling strategy:

```text
Retry transient request/HTTP errors.
Fail fast for auth/config errors.
Dead-letter bad records.
Alert on high invalid rate.
Make persistence idempotent.
Checkpoint only after successful persistence.
Log enough context to debug.
```

Interview line:

```text
I separate infrastructure errors from data-quality errors because they require different handling.
```


## 41. Observability

API pipelines need observability.

Metrics:

```text
records_fetched
records_written
invalid_records
pages_fetched
request_count
retry_count
rate_limit_count
api_latency_ms
extract_duration_seconds
last_successful_watermark
duplicate_count
empty_page_count
schema_error_count
```

Logs:

```text
run_id
endpoint
page/cursor
status_code
attempt
record_count
checkpoint
error category
```

Alerts:

```text
pipeline failed
too many retries
too many 429s
invalid record rate above threshold
record count unexpectedly zero
watermark not advancing
API latency too high
schema validation failure
```

Interview line:

```text
I would emit metrics and structured logs so failures can be diagnosed without manually rerunning the pipeline.
```


## 42. API Ingestion Edge Cases

Common edge cases:

```text
empty response
missing data key
data key is not a list
invalid JSON
HTML error body with 200 status
pagination cursor repeats
next URL missing
empty page with next cursor
duplicate records across pages
record missing id
record missing updated_at
updated_at format changes
rate limit header missing
Retry-After is not numeric
API returns 202 async job accepted
export job never completes
token expires mid-run
partial page written then crash
checkpoint saved too early
timezone-naive timestamp
late-arriving updates
deleted records not returned
soft-deletes represented as status
API returns nested arrays
API returns huge payload
API response compressed
API changes schema
```

Strict interview line:

```text
A robust API pipeline assumes partial failure and inconsistent responses can happen.
```


## 43. Async API Processing

Async can increase throughput, but it is not always the right answer.

Use async when:

```text
many independent API calls
API latency dominates runtime
rate limits allow concurrency
I/O-bound extraction
```

Avoid async when:

```text
API is strict rate-limited
pagination is sequential cursor-based
candidate cannot explain concurrency control
write system cannot handle parallel load
ordering/checkpointing becomes unsafe
```

Interview line:

```text
I would start with a reliable synchronous implementation unless throughput requirements justify async. If using async, I would limit concurrency and still respect rate limits.
```

Mention:

```text
httpx.AsyncClient
aiohttp
asyncio.Semaphore
```

Do not overcomplicate unless asked.


## 44. Concurrency and Backpressure

Concurrency risks:

```text
hitting rate limits
out-of-order processing
duplicate writes
checkpoint race conditions
memory pressure
overloading downstream warehouse
```

Control mechanisms:

```text
bounded worker pool
semaphore
rate limiter
batch queue
backpressure from writer
per-endpoint concurrency limits
idempotent writes
centralized checkpointing
```

Interview line:

```text
Concurrency must be bounded. Faster API calls are not useful if they overwhelm the target system or break rate limits.
```


## 45. Webhooks vs Polling

API ingestion can be polling or webhooks.

### Polling

Pipeline calls API periodically.

Pros:

```text
simple
controlled schedule
easy backfill
works without public endpoint
```

Cons:

```text
latency between runs
rate-limit usage
may miss updates if incremental logic is wrong
```

### Webhooks

Source pushes events to your endpoint.

Pros:

```text
near real-time
less polling
source-driven updates
```

Cons:

```text
must expose endpoint
must verify signatures
must handle retries and duplicate delivery
must persist quickly
must support replay/backfill separately
```

Interview line:

```text
Even with webhooks, I would design idempotent processing because webhook delivery is often at-least-once.
```


## 46. Polling Export Job Pattern

Some APIs use async export jobs.

Flow:

```text
1. POST export request with filters.
2. Receive job_id.
3. Poll job status.
4. When complete, download file or pages.
5. Process file.
6. Save checkpoint.
```

Pseudo-code:

```python
def run_export(client, start_time, end_time):
    job = client.post("/exports", json={
        "start_time": start_time,
        "end_time": end_time,
    })

    job_id = job["job_id"]

    while True:
        status = client.get(f"/exports/{job_id}")

        if status["state"] == "complete":
            return status["download_url"]

        if status["state"] == "failed":
            raise RuntimeError(f"Export failed: {job_id}")

        time.sleep(30)
```

Interview point:

```text
Add max polling time, backoff, and idempotency for export job creation if supported.
```


## 47. GraphQL API Processing

GraphQL APIs often use POST with query body.

Example:

```python
def run_graphql_query(client, query, variables):
    payload = client.post("/graphql", json={
        "query": query,
        "variables": variables,
    })

    if "errors" in payload:
        raise RuntimeError(payload["errors"])

    return payload["data"]
```

GraphQL pagination often uses:

```text
edges
nodes
pageInfo
endCursor
hasNextPage
```

Interview line:

```text
For GraphQL, I would handle both HTTP errors and GraphQL-level errors in the response body.
```

Important:

```text
A GraphQL response can be HTTP 200 and still contain errors.
```


## 48. API Design for Testability

Good API processing code is testable.

Separate:

```text
HTTP client
pagination iterator
transformation logic
validation logic
persistence logic
checkpoint logic
```

Why:

```text
transform and validation can be unit tested without real API calls
pagination can be tested with fake responses
retry behavior can be mocked
```

Bad design:

```text
one huge function that fetches, transforms, writes, and checkpoints
```

Good design:

```text
fetch_page()
iter_pages()
transform_record()
validate_record()
write_batch()
save_checkpoint()
```

Interview line:

```text
I separate side effects from pure transformation logic so the pipeline is easier to test and maintain.
```


## 49. Mocking API Calls in Tests

Use mocking or fake clients.

Fake client example:

```python
class FakeClient:
    def __init__(self, responses):
        self.responses = responses
        self.calls = []

    def get(self, path, params=None):
        self.calls.append({"path": path, "params": params})
        return self.responses.pop(0)
```

Test cursor pagination:

```python
def test_cursor_pagination():
    client = FakeClient([
        {"data": [{"id": 1}], "next_cursor": "abc"},
        {"data": [{"id": 2}], "next_cursor": None},
    ])

    records = list(iter_cursor_records(client, "/items"))

    assert records == [{"id": 1}, {"id": 2}]
    assert len(client.calls) == 2
```

Interview line:

```text
I would unit test pagination, transformation, validation, retry decisions, and checkpoint behavior using fake clients or mocks.
```


## 50. Coding Problem: Fetch All Cursor Pages

Problem:

```text
Implement a function that fetches all records from a cursor-paginated API.
The client has get(path, params) and returns:
{
  "data": [...],
  "next_cursor": "..."
}
```

Solution:

```python
def fetch_all_cursor_records(client, path, page_size=100):
    cursor = None
    records = []
    seen_cursors = set()

    while True:
        params = {"limit": page_size}

        if cursor:
            params["cursor"] = cursor

        payload = client.get(path, params=params)
        page_records = payload.get("data", [])

        if not isinstance(page_records, list):
            raise ValueError("Expected data to be a list")

        records.extend(page_records)

        next_cursor = payload.get("next_cursor")

        if not next_cursor:
            break

        if next_cursor in seen_cursors:
            raise RuntimeError("Pagination loop detected")

        seen_cursors.add(next_cursor)
        cursor = next_cursor

    return records
```

Complexity:

```text
Time: O(n), where n is total records
Space: O(n), because all records are returned
```

Follow-up:

```text
Use a generator to avoid storing all records.
```


## 51. Coding Problem: Cursor Generator

Problem:

```text
Write a generator for cursor-paginated records.
```

Solution:

```python
def iter_cursor_records(client, path, page_size=100):
    cursor = None
    seen_cursors = set()

    while True:
        params = {"limit": page_size}

        if cursor:
            params["cursor"] = cursor

        payload = client.get(path, params=params)
        records = payload.get("data", [])

        if not isinstance(records, list):
            raise ValueError("Expected data to be a list")

        for record in records:
            yield record

        next_cursor = payload.get("next_cursor")

        if not next_cursor:
            break

        if next_cursor in seen_cursors:
            raise RuntimeError("Pagination loop detected")

        seen_cursors.add(next_cursor)
        cursor = next_cursor
```

Complexity:

```text
Time: O(n)
Space: O(number of seen cursors + one page)
```

Interview line:

```text
The generator version is more memory efficient because it yields one record at a time.
```


## 52. Coding Problem: Flatten Users API

Problem:

```text
Given API user records:
{
  "id": "u1",
  "name": "Murali",
  "profile": {
    "email": "x@example.com",
    "location": {"country": "IN"}
  }
}

Return flattened rows with:
user_id, name, email, country
```

Solution:

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

def flatten_user(record):
    return {
        "user_id": record.get("id"),
        "name": record.get("name"),
        "email": get_nested(record, ["profile", "email"]),
        "country": get_nested(record, ["profile", "location", "country"]),
    }
```

Validation:

```python
def validate_user(row):
    errors = []

    if not row.get("user_id"):
        errors.append("missing_user_id")

    if not row.get("email"):
        errors.append("missing_email")

    return errors
```

Complexity:

```text
Time: O(number of fields)
Space: O(1) per record
```


## 53. Coding Problem: Split Valid and Invalid Records

Problem:

```text
Given raw API records, flatten and split into valid and invalid rows.
```

Solution:

```python
def split_valid_invalid(records, flatten_fn, validate_fn):
    valid = []
    invalid = []

    for record in records:
        try:
            row = flatten_fn(record)
            errors = validate_fn(row)
        except Exception as exc:
            invalid.append({
                "raw_record": record,
                "errors": [f"transform_error:{exc}"],
            })
            continue

        if errors:
            invalid.append({
                "raw_record": record,
                "row": row,
                "errors": errors,
            })
        else:
            valid.append(row)

    return valid, invalid
```

Interview point:

```text
Record-level errors should not always fail the entire batch. But if invalid rate is too high, the pipeline should fail/alert.
```

Follow-up:

```text
Add invalid-rate threshold.
```


## 54. Coding Problem: Invalid Rate Threshold

Problem:

```text
Fail the batch if invalid records exceed max_invalid_ratio.
```

Solution:

```python
def enforce_invalid_threshold(valid, invalid, max_invalid_ratio=0.05):
    total = len(valid) + len(invalid)

    if total == 0:
        return

    invalid_ratio = len(invalid) / total

    if invalid_ratio > max_invalid_ratio:
        raise RuntimeError(
            f"Invalid record ratio too high: {invalid_ratio:.2%}"
        )
```

Interview line:

```text
I tolerate small record-level issues but fail fast when the invalid rate suggests schema drift or source-system problems.
```


## 55. Coding Problem: Deduplicate API Records

Problem:

```text
Given API records with id and updated_at, keep the latest record per id.
```

Solution:

```python
def dedupe_latest(records):
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

Complexity:

```text
Time: O(n)
Space: O(u), where u is unique ids
```

Follow-ups:

```text
Parse timestamps to datetime.
Tie-break using ingestion_time.
Handle deletes.
```


## 56. Coding Problem: Build Query Params for Incremental Sync

Problem:

```text
Build query parameters for incremental API extraction using updated_after and updated_before.
```

Solution:

```python
def build_incremental_params(start_time, end_time, page_size=100, cursor=None):
    params = {
        "updated_after": start_time.isoformat(),
        "updated_before": end_time.isoformat(),
        "limit": page_size,
    }

    if cursor:
        params["cursor"] = cursor

    return params
```

Interview point:

```text
Use explicit extraction windows instead of open-ended pulls when possible. It improves reproducibility and debugging.
```

Follow-up:

```text
How do you handle timezone?
```

Expected:

```text
Use timezone-aware UTC datetimes.
```


## 57. Coding Problem: Save and Load Checkpoint JSON

Problem:

```text
Save and load checkpoint from a JSON file.
```

Solution:

```python
import json
from pathlib import Path

def load_checkpoint(path):
    path = Path(path)

    if not path.exists():
        return {}

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

def save_checkpoint(path, checkpoint):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_suffix(path.suffix + ".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(checkpoint, file, indent=2, sort_keys=True)

    temp_path.replace(path)
```

Why temp file:

```text
Avoid partially written checkpoint if process crashes during write.
```

Interview line:

```text
For production, I would store checkpoints in durable shared storage or a database, but this shows the core idea.
```


## 58. Coding Problem: Resume Cursor Sync

Problem:

```text
Resume cursor-based sync from saved checkpoint.
Checkpoint contains last_cursor.
```

Solution:

```python
def sync_with_cursor_checkpoint(client, path, checkpoint, write_batch, page_size=100):
    cursor = checkpoint.get("last_cursor")
    total = 0

    while True:
        params = {"limit": page_size}

        if cursor:
            params["cursor"] = cursor

        payload = client.get(path, params=params)
        records = payload.get("data", [])

        write_batch(records)
        total += len(records)

        next_cursor = payload.get("next_cursor")

        checkpoint["last_cursor"] = next_cursor
        checkpoint["records_synced"] = checkpoint.get("records_synced", 0) + len(records)
        save_checkpoint("checkpoint.json", checkpoint)

        if not next_cursor:
            break

        cursor = next_cursor

    return total
```

Important warning:

```text
This assumes write_batch is idempotent. Otherwise, crash/retry can duplicate records.
```


## 59. Coding Problem: Retry Decision Function

Problem:

```text
Write a function that classifies whether a status code should be retried.
```

Solution:

```python
def should_retry_status(status_code):
    retryable = {408, 429, 500, 502, 503, 504}
    return status_code in retryable
```

Expanded:

```python
def classify_status(status_code):
    if status_code in {408, 429, 500, 502, 503, 504}:
        return "retryable"

    if 400 <= status_code < 500:
        return "non_retryable_client_error"

    if 200 <= status_code < 300:
        return "success"

    return "unknown"
```

Interview point:

```text
Retry decisions should be explicit and testable.
```


## 60. Coding Problem: Parse Retry-After

Problem:

```text
Parse Retry-After header safely.
For simplicity, handle integer seconds only.
```

Solution:

```python
def parse_retry_after(headers):
    value = headers.get("Retry-After")

    if not value:
        return None

    try:
        seconds = int(value)
    except ValueError:
        return None

    if seconds < 0:
        return None

    return seconds
```

Follow-up:

```text
Retry-After can also be an HTTP date.
```

Expected:

```text
Use email.utils.parsedate_to_datetime for HTTP date format if needed.
```


## 61. Data Engineering Custom Problem: Transactions API Sync

Problem:

```text
You need to sync transactions from a paginated API.
Each transaction has:
id, amount, currency, created_at, updated_at, customer.id

Requirements:
- cursor pagination
- retry transient failures
- flatten customer_id
- validate id, amount, currency, updated_at
- write valid rows
- dead-letter invalid rows
- checkpoint cursor
```

Expected design:

```text
ApiClient handles requests, timeout, retry, rate limits.
iter_cursor_records handles pagination.
flatten_transaction handles nested JSON.
validate_transaction returns errors.
write_batch persists idempotently.
write_dead_letter stores invalid records.
save_checkpoint runs after successful write.
```

Strong interview answer:

```text
I would also use a lookback window on updated_at and merge into target by transaction id to handle reruns and late updates.
```


## 62. Data Engineering Custom Problem: API Pagination Loop Bug

Problem:

```text
An API returns the same next_cursor repeatedly due to a vendor bug.
How do you prevent infinite loops?
```

Expected answer:

```text
Track seen cursors during a run.
Set max page limit.
Log endpoint and cursor.
Fail with a clear error.
Do not keep retrying forever.
```

Code idea:

```python
seen_cursors = set()

if next_cursor in seen_cursors:
    raise RuntimeError(f"Pagination loop detected: {next_cursor}")

seen_cursors.add(next_cursor)
```

Interview line:

```text
Pagination loops are a real production risk, so I guard against repeated cursors and maximum page counts.
```


## 63. Data Engineering Custom Problem: API Count Drop

Problem:

```text
Yesterday API sync fetched 1,000,000 records.
Today it fetched 0 records but API returned 200 OK.
What do you do?
```

Expected answer:

```text
Do not blindly treat 0 as success.
Check API status and response schema.
Check query parameters and checkpoint.
Check auth/permissions.
Check vendor incident/status.
Compare with historical counts.
Alert if count is unexpectedly low.
Do not advance watermark until verified.
Maybe fail pipeline if count anomaly exceeds threshold.
```

Interview line:

```text
A successful HTTP response is not the same as a successful data extraction.
```


## 64. Data Engineering Custom Problem: Token Expiry Mid-Run

Problem:

```text
API token expires during long extraction.
How should pipeline handle it?
```

Expected answer:

```text
Detect 401/expired-token error.
Refresh token if refresh mechanism exists.
Retry original request once after refresh.
Do not log token.
Fail clearly if refresh fails.
Store token securely.
```

Pseudo-flow:

```text
request → 401 token expired → refresh token → retry request → continue
```

Caution:

```text
Do not retry 401 forever.
```

Interview line:

```text
Auth errors are usually non-retryable unless there is a controlled token refresh path.
```


## 65. Data Engineering Custom Problem: Webhook Duplicate Delivery

Problem:

```text
A webhook provider retries events and may send duplicates.
How do you process safely?
```

Expected answer:

```text
Verify webhook signature.
Persist raw event quickly.
Use event_id as idempotency key.
Deduplicate before processing.
Return success after durable write.
Process asynchronously if heavy.
Keep dead-letter for invalid payloads.
Support replay/backfill from API if webhook misses events.
```

Interview line:

```text
Webhook processing should assume at-least-once delivery, so deduplication by event_id is mandatory.
```


## 66. Data Engineering Custom Problem: Deleted Records

Problem:

```text
API incremental sync only returns active records.
How do you handle deletes?
```

Expected answer depends on API support:

```text
If API has deleted_at/status field:
  sync soft deletes and update target status.

If API has deleted endpoint/change log:
  ingest deletes separately.

If API has full snapshot:
  compare snapshot to target and mark missing records as deleted.

If no delete support:
  document limitation and use periodic full reconciliation if possible.
```

Interview line:

```text
Incremental sync must account for deletes; otherwise the warehouse can retain stale records forever.
```


## 67. Data Engineering Custom Problem: API Schema Drift

Problem:

```text
API field amount changes from number to string.
What happens and how do you handle it?
```

Expected answer:

```text
Validation should catch type mismatch.
Invalid records go to dead-letter.
Alert on elevated invalid rate.
Keep raw payload for replay.
Update transformation to parse numeric strings if business-approved.
Backfill/reprocess dead-letter records after fix.
Add schema contract tests if possible.
```

Interview line:

```text
Schema drift should be detected by validation and monitoring, not discovered weeks later in dashboards.
```


## 68. Data Engineering Custom Problem: Large API Response

Problem:

```text
API can return millions of records.
How do you avoid memory issues?
```

Expected answer:

```text
Use pagination.
Process page by page.
Use generators.
Write batches.
Avoid records.extend(all_pages) for huge extracts.
Land raw data incrementally.
Checkpoint after successful page/batch.
Use streaming download for files.
```

Interview line:

```text
I would avoid loading all records into memory and process records in bounded batches.
```


## 69. Data Engineering Custom Problem: Partial Write Failure

Problem:

```text
Page 10 is fetched successfully, but warehouse write fails halfway.
What prevents data corruption?
```

Expected answer:

```text
Use transactional writes where possible.
Write to staging first.
Use idempotent merge/upsert.
Checkpoint only after successful write.
Use run_id and page metadata.
On rerun, reprocess page safely.
```

Interview line:

```text
Checkpointing and idempotent writes must be coordinated; otherwise partial failures cause data loss or duplicates.
```


## 70. Data Engineering Custom Problem: API Backfill

Problem:

```text
Backfill API data for the last 2 years without violating rate limits.
```

Expected answer:

```text
Split into time windows.
Process windows sequentially or with bounded concurrency.
Respect rate limits.
Checkpoint each window.
Use idempotent writes.
Store raw landing data by extraction window.
Monitor counts per window.
Retry transient failures.
Avoid massive open-ended query.
```

Interview line:

```text
For large backfills, I split the extraction into deterministic windows so each window is resumable and auditable.
```


## 71. API Processing Pattern Classification Drill

Classify each prompt.

```text
1. API returns next_cursor.
2. API returns page and total_pages.
3. API returns 429 with Retry-After.
4. API returns 500 randomly.
5. API returns 400 because parameter is wrong.
6. API response has data as a list.
7. API response is HTML error page with 200.
8. Token expires during extraction.
9. Need to fetch only updated records.
10. Need to avoid duplicate rows after rerun.
11. Webhook sends same event multiple times.
12. API has nested customer.id.
13. API deletes records but incremental endpoint only returns active records.
14. Page cursor repeats.
15. Need to ingest millions of records.
16. Need to write bad records somewhere.
17. API supports export job with 202 Accepted.
18. Need to test pagination without real API.
19. Need high throughput across 100 independent endpoints.
20. API data count drops from 1M to 0 unexpectedly.
```

Expected classification:

```text
1. cursor pagination
2. page number pagination
3. rate-limit handling
4. retry with backoff
5. non-retryable client error
6. response shape validation
7. content/schema validation
8. token refresh/auth handling
9. incremental sync/watermark
10. idempotent write/dedup/upsert
11. webhook idempotency
12. nested JSON flattening
13. delete handling/reconciliation
14. pagination loop guard
15. generator/batch processing
16. dead-letter records
17. async export job polling
18. fake client/mock tests
19. bounded concurrency
20. data quality anomaly/alert/no checkpoint advancement
```

Passing standard:

```text
18/20 correct before API mock interviews.
```


## 72. High-ROI API Interview Topics

Practice these topics first.

| Topic | What Candidate Must Explain |
|---|---|
| HTTP status codes | Retryable vs non-retryable |
| Timeouts | Why no timeout is dangerous |
| Retries | Exponential backoff, jitter, max attempts |
| Rate limits | 429, Retry-After, bounded concurrency |
| Pagination | page, offset, cursor, next URL |
| Cursor loops | seen cursors, max pages |
| Incremental sync | watermark, updated_at, lookback |
| Checkpointing | save only after successful write |
| Idempotency | upsert/merge/dedupe/partition overwrite |
| JSON parsing | response shape validation |
| Flattening | nested fields to table columns |
| Validation | required fields and type checks |
| Dead-letter | invalid record storage |
| Schema drift | raw landing, alerts, validation |
| Deletes | soft delete, changelog, snapshot compare |
| Webhooks | signature, idempotency, durable write |
| Export jobs | POST, poll, download |
| Observability | metrics, logs, alerts |
| Testing | fake clients, mock responses |
| Memory safety | generators and batch writes |


## 73. Practice Ladder

### Level 1: Basic requests and JSON

```text
fetch_json with timeout
status code handling
safe JSON parsing
nested field access
flatten user record
```

Exit:

```text
Candidate can safely request and parse API data.
```

### Level 2: Pagination

```text
page number pagination
offset pagination
cursor pagination
next URL pagination
pagination loop guard
```

Exit:

```text
Candidate can fetch all pages without infinite loops.
```

### Level 3: Reliability

```text
retryable status codes
exponential backoff
rate limit handling
timeout handling
token expiry
```

Exit:

```text
Candidate can handle unstable APIs.
```

### Level 4: Data correctness

```text
record validation
dead-letter records
deduplication
idempotent writes
checkpointing
incremental sync
```

Exit:

```text
Candidate can avoid data loss and duplicates.
```

### Level 5: Production design

```text
observability
schema drift
deletes
webhooks
async/export jobs
testing
backfills
```

Exit:

```text
Candidate can design production-grade API ingestion.
```


## 74. 7-Day API Processing Plan

### Day 1: HTTP basics

Problems:

```text
Write fetch_json with timeout.
Classify status codes.
Handle invalid JSON.
Build headers from environment token.
```

Focus:

```text
requests
timeout
status handling
auth
```

### Day 2: Pagination

Problems:

```text
Fetch page-number API.
Fetch offset API.
Fetch cursor API.
Fetch next URL API.
```

Focus:

```text
pagination loops
end conditions
memory safety
```

### Day 3: Retry and rate limits

Problems:

```text
Retry decision function.
Parse Retry-After.
Implement retry with backoff.
Handle 429.
```

Focus:

```text
retryable vs non-retryable
backoff
jitter
bounded attempts
```

### Day 4: JSON processing

Problems:

```text
Flatten users.
Flatten transactions.
Validate required fields.
Split valid/invalid records.
```

Focus:

```text
nested JSON
validation
dead-letter
schema drift
```

### Day 5: Incremental sync

Problems:

```text
Build incremental params.
Save/load checkpoint.
Resume cursor sync.
Dedupe latest by id.
```

Focus:

```text
watermark
lookback
checkpointing
idempotency
```

### Day 6: System design

Problems:

```text
Design transactions API pipeline.
Handle deletes.
Handle token expiry.
Handle large backfill.
Handle webhook duplicates.
```

Focus:

```text
production failure modes
observability
raw/staging/clean
```

### Day 7: Mock and repair

Tasks:

```text
Run API processing mock set.
Review mistakes.
Repair weakest topic.
Update progress.
```


## 75. 30-Day API Processing Plan

### Week 1: API fundamentals

Focus:

```text
HTTP methods
status codes
timeouts
auth
JSON parsing
safe nested access
```

Exit:

```text
Candidate can write safe request and parse functions.
```

### Week 2: Pagination and retries

Focus:

```text
cursor/page/offset pagination
retry/backoff
rate limits
Retry-After
pagination loop detection
```

Exit:

```text
Candidate can build reliable paginated extraction.
```

### Week 3: Data pipeline correctness

Focus:

```text
flattening
validation
dead-letter
checkpointing
incremental sync
idempotency
deduplication
```

Exit:

```text
Candidate can prevent data loss and duplicates.
```

### Week 4: Production design and mocks

Focus:

```text
observability
schema drift
deletes
webhooks
export jobs
async/concurrency
testing
backfills
```

Exit:

```text
Average mock score >= 4/5.
```


## 76. Mock Set 1: Python API Basics

Problems:

```text
1. Write fetch_json with timeout and status handling.
2. Build auth headers from environment variable.
3. Safely parse JSON response with data list.
4. Flatten nested user record.
5. Validate required fields.
```

Expected skills:

```text
requests
timeout
headers
JSON parsing
nested dict handling
validation
```

Passing standard:

```text
Average score >= 4/5.
Candidate does not hardcode secrets and does not ignore timeout.
```


## 77. Mock Set 2: Pagination and Retry

Problems:

```text
1. Fetch all cursor-paginated records.
2. Detect repeated cursor loop.
3. Implement retry decision function.
4. Parse Retry-After.
5. Explain 429 and 5xx handling.
```

Expected skills:

```text
cursor pagination
loop guard
retry classification
rate limits
backoff
```

Passing standard:

```text
Average score >= 4/5.
Candidate avoids infinite loops and blind retries.
```


## 78. Mock Set 3: Data Engineering API Pipeline

Problems:

```text
1. Design transactions API sync.
2. Implement flatten + validate + split valid/invalid.
3. Save/load checkpoint.
4. Explain idempotent loading.
5. Handle late-arriving updates with lookback.
```

Expected skills:

```text
pipeline design
checkpointing
dead-letter
upsert/dedup
watermark
lookback
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains why checkpointing before write is dangerous.
```


## 79. Mock Set 4: Production Failure Scenarios

Problems:

```text
1. API count drops from 1M to 0.
2. Token expires mid-run.
3. Webhook duplicate delivery.
4. API schema drift.
5. Partial write failure.
```

Expected skills:

```text
observability
auth refresh
idempotency
schema validation
transactional/idempotent writes
incident reasoning
```

Passing standard:

```text
Average score >= 4/5.
Candidate gives realistic production-safe answers.
```


## 80. Timed Drill Protocol

Use this timing protocol.

### API coding drill

```text
20-35 minutes
```

### API system-design drill

```text
35-45 minutes
```

### Production incident drill

```text
15-25 minutes
```

Per coding drill:

```text
Minute 0-3:
Clarify endpoint, auth, pagination, response shape.

Minute 3-6:
Define request/retry/pagination approach.

Minute 6-20:
Code core function.

Minute 20-25:
Add validation/error handling.

Minute 25-30:
Explain complexity and failure cases.
```

Per design drill:

```text
Minute 0-5:
Clarify source API constraints.

Minute 5-15:
Propose architecture.

Minute 15-25:
Discuss correctness: idempotency, checkpointing, dedupe.

Minute 25-35:
Discuss reliability and observability.

Minute 35-45:
Discuss scaling, backfill, deletes, schema drift.
```


## 81. Review Checklist

Review API processing answers using:

```text
1. Did candidate set timeout?
2. Did candidate handle status codes?
3. Did candidate distinguish retryable and non-retryable errors?
4. Did candidate respect 429/rate limits?
5. Did candidate use bounded retries?
6. Did candidate implement pagination correctly?
7. Did candidate prevent infinite pagination loops?
8. Did candidate validate response shape?
9. Did candidate parse nested JSON safely?
10. Did candidate validate required fields?
11. Did candidate handle invalid records?
12. Did candidate explain checkpointing?
13. Did candidate explain idempotency?
14. Did candidate avoid duplicate loading?
15. Did candidate discuss observability?
16. Did candidate handle schema drift?
17. Did candidate handle deletes/late updates if relevant?
18. Did candidate separate code concerns?
19. Did candidate mention tests/mocks?
20. Did candidate connect to DE pipeline design?
```

Verdict examples:

```text
Can call API but not production-ready.
Good pagination but no retry/rate-limit handling.
Good retry logic but no idempotency.
Good code but no checkpointing.
Good extraction but no validation/dead-letter.
Interview-ready.
Strong.
```


## 82. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| No timeout | Request safety drills |
| Retries every error | Retry classification drills |
| Ignores 429 | Rate-limit scenario drills |
| Pagination loop bug | Cursor loop guard drills |
| Loads all records into memory | Generator/batch writing drills |
| Unsafe nested JSON access | Flattening and validation drills |
| No dead-letter handling | Invalid-record split drills |
| No checkpointing | Resume sync drills |
| Checkpoints too early | Partial failure drills |
| No idempotency | Upsert/dedupe/merge drills |
| No schema drift strategy | Validation + raw landing drills |
| Cannot handle deletes | Delete handling scenario drills |
| No observability | Metrics/logging drill |
| No testing strategy | Fake client/mock drill |
| Overuses async | Concurrency/rate-limit drill |

If weakness repeats:

```text
Use weakness-repair-mode.md.
```


## 83. Communication Scripts

### Basic API script

```text
I would use a client function with timeout, auth headers, explicit status-code handling, JSON parsing, and clear exceptions.
```

### Retry script

```text
I retry transient failures like 429, 408, and 5xx with bounded exponential backoff and jitter. I do not blindly retry permanent 4xx errors.
```

### Pagination script

```text
I would implement pagination based on the API's documented mechanism and stop when there is no next cursor/page. I would also guard against repeated cursors to avoid infinite loops.
```

### Incremental sync script

```text
I would use updated_at or a cursor as a watermark, checkpoint only after successful persistence, and use a lookback window if late updates are possible.
```

### Idempotency script

```text
Because retries and reruns happen, writes must be idempotent through upsert, merge keys, partition overwrite, or deduplication.
```

### Validation script

```text
I validate both the response shape and individual records. Invalid records go to a dead-letter path with error reasons and raw payload context.
```

### Observability script

```text
I would emit metrics for records fetched, records written, retries, 429s, invalid records, duration, and watermark progress, with alerts for anomalies.
```


## 84. Candidate Self-Review Questions

After every API processing problem, candidate should answer:

```text
1. What is the endpoint and method?
2. How is authentication handled?
3. What timeout is used?
4. Which errors are retryable?
5. How are rate limits handled?
6. What pagination style is used?
7. What stops the pagination loop?
8. How is response shape validated?
9. How are nested fields parsed?
10. Which fields are required?
11. What happens to invalid records?
12. How is progress checkpointed?
13. When is checkpoint saved?
14. How are duplicates avoided?
15. What is the idempotency strategy?
16. What metrics/logs are emitted?
17. How are schema drift and deletes handled?
18. How would this be tested?
```

If candidate cannot answer these:

```text
The solution is not production-ready.
```


## 85. Maintenance Drills

After completing API processing, maintain skill with:

```text
1 pagination drill per week
1 retry/rate-limit drill per week
1 JSON flattening/validation drill per week
1 checkpoint/idempotency drill every 2 weeks
1 production failure scenario every 2 weeks
1 full API pipeline mock every month
```

Maintenance rotation:

```text
Week 1: cursor pagination + flattening
Week 2: retry/backoff + rate limits
Week 3: checkpointing + idempotent writes
Week 4: schema drift/delete/webhook scenario
```

If score drops below 4:

```text
Run weakness-repair-mode.md for failed topic.
```


## 86. Progress Tracking Template

Use this progress format.

```text
# API Processing Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Topic | Score | Time | Mistake | Next Action

## Topic Scores

HTTP basics:
Timeouts:
Status codes:
Retries:
Rate limits:
Pagination:
Cursor loop guard:
Incremental sync:
Checkpointing:
Idempotency:
Nested JSON:
Flattening:
Validation:
Dead-letter:
Deduplication:
Schema drift:
Deletes:
Webhooks:
Export jobs:
Observability:
Testing:
Production scenarios:

## Repeated Mistakes

-

## Repair Items

-

## Next Practice

Today:
This week:
Next mock:
```


## 87. Final Exit Test

Candidate passes API processing when they can solve/explain:

```text
1. fetch_json with timeout and status handling
2. retryable vs non-retryable status codes
3. retry with exponential backoff and jitter
4. rate-limit handling with Retry-After
5. page number pagination
6. offset pagination
7. cursor pagination
8. next URL pagination
9. pagination loop detection
10. safe nested JSON access
11. flatten nested records
12. validate records
13. split valid and invalid records
14. dead-letter invalid records
15. dedupe latest records
16. save/load checkpoint
17. resume cursor sync
18. incremental sync with watermark
19. lookback window for late updates
20. idempotent writes
21. schema drift handling
22. delete handling
23. token expiry
24. webhook duplicate delivery
25. export job polling
26. observability metrics and logs
27. API pipeline testing with fake client
28. full transactions API ingestion design
```

Passing standard:

```text
Average score >= 4/5.
No missing timeout.
No blind retries.
No missing pagination.
No unsafe checkpointing.
No idempotency gap.
No validation/dead-letter gap.
Can explain Data Engineering production relevance.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles production incidents and trade-offs clearly under pressure.
```


## 88. Final Summary

API processing is one of the most practical Python skills for Data Engineering interviews.

It maps directly to:

```text
SaaS ingestion
incremental sync
webhook processing
raw data landing
external API extraction
vendor integrations
pipeline reliability
data quality checks
backfills
schema drift handling
```

The candidate must master:

```text
requests/httpx basics
timeouts
status codes
retry/backoff
rate limits
pagination
cursor handling
incremental sync
checkpointing
idempotency
JSON parsing
nested flattening
validation
dead-letter records
deduplication
schema drift
delete handling
observability
testing
production incident reasoning
```

The mentor must be strict:

```text
No timeout → not interview-ready.
No pagination → not interview-ready.
Blind retries → not interview-ready.
Checkpoint before write → not interview-ready.
No idempotency → not interview-ready.
No validation/dead-letter → not interview-ready.
```

The goal is not to memorize `requests.get`.

The goal is to design API ingestion that is reliable, resumable, observable, and safe under real production failures.


## 89. Problem Card Appendix

### Card 1: Fetch JSON Safely

Category:

```text
Python
```

Primary topic:

```text
HTTP basics
```

Core idea:

```text
Use timeout, status handling, JSON parsing.
```

Data Engineering connection:

```text
Base API client function.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Retry Decision

Category:

```text
Python
```

Primary topic:

```text
Reliability
```

Core idea:

```text
Classify retryable vs non-retryable errors.
```

Data Engineering connection:

```text
Avoid blind retries.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Retry-After Parser

Category:

```text
Python
```

Primary topic:

```text
Rate limits
```

Core idea:

```text
Parse rate-limit wait time.
```

Data Engineering connection:

```text
Respect API limits.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Cursor Pagination

Category:

```text
Python
```

Primary topic:

```text
Pagination
```

Core idea:

```text
Fetch records using next_cursor.
```

Data Engineering connection:

```text
Sync SaaS records.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Cursor Generator

Category:

```text
Python
```

Primary topic:

```text
Memory safety
```

Core idea:

```text
Yield records page by page.
```

Data Engineering connection:

```text
Large API extraction.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Offset Pagination

Category:

```text
Python
```

Primary topic:

```text
Pagination
```

Core idea:

```text
Fetch offset/limit pages.
```

Data Engineering connection:

```text
Legacy API ingestion.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Next URL Pagination

Category:

```text
Python
```

Primary topic:

```text
Pagination
```

Core idea:

```text
Follow next URL until done.
```

Data Engineering connection:

```text
Django/DRF-style APIs.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Flatten User Record

Category:

```text
Python
```

Primary topic:

```text
JSON processing
```

Core idea:

```text
Extract nested fields safely.
```

Data Engineering connection:

```text
User/customer dimensions.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Validate Transaction

Category:

```text
Python
```

Primary topic:

```text
Data quality
```

Core idea:

```text
Check required fields.
```

Data Engineering connection:

```text
Clean API data.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Split Valid Invalid

Category:

```text
Python
```

Primary topic:

```text
Dead-letter
```

Core idea:

```text
Separate good and bad records.
```

Data Engineering connection:

```text
Robust ingestion.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Dedupe Latest

Category:

```text
Python
```

Primary topic:

```text
Idempotency
```

Core idea:

```text
Keep latest record per id.
```

Data Engineering connection:

```text
Rerun-safe loads.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Checkpoint JSON

Category:

```text
Python
```

Primary topic:

```text
Checkpointing
```

Core idea:

```text
Save/load progress safely.
```

Data Engineering connection:

```text
Resume sync after failure.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Incremental Params

Category:

```text
Python
```

Primary topic:

```text
Watermark
```

Core idea:

```text
Build updated_after/before params.
```

Data Engineering connection:

```text
Incremental extraction.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Resume Cursor Sync

Category:

```text
Python
```

Primary topic:

```text
Resumability
```

Core idea:

```text
Continue from checkpoint.
```

Data Engineering connection:

```text
Long extraction jobs.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Transactions API Design

Category:

```text
System design
```

Primary topic:

```text
End-to-end API ingestion
```

Core idea:

```text
Combine client, pagination, validation, checkpoint.
```

Data Engineering connection:

```text
Real DE pipeline.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Webhook Dedupe

Category:

```text
System design
```

Primary topic:

```text
Idempotency
```

Core idea:

```text
Handle duplicate webhook delivery.
```

Data Engineering connection:

```text
Near real-time ingestion.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Token Expiry

Category:

```text
Scenario
```

Primary topic:

```text
Auth reliability
```

Core idea:

```text
Refresh and retry safely.
```

Data Engineering connection:

```text
Long-running sync.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Schema Drift

Category:

```text
Scenario
```

Primary topic:

```text
Data quality
```

Core idea:

```text
Detect and handle type/field changes.
```

Data Engineering connection:

```text
Vendor API changes.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Delete Handling

Category:

```text
Scenario
```

Primary topic:

```text
Correctness
```

Core idea:

```text
Sync soft/hard deletes.
```

Data Engineering connection:

```text
Avoid stale warehouse rows.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Backfill API

Category:

```text
Scenario
```

Primary topic:

```text
Scale
```

Core idea:

```text
Split into windows and checkpoint.
```

Data Engineering connection:

```text
Historical reload.
```

Candidate must be able to explain:

```text
1. API assumption.
2. Failure mode.
3. Correct handling strategy.
4. Python implementation or pseudocode.
5. Edge cases.
6. Testing strategy.
7. Production relevance.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 90. Data Engineering Custom Scenario Appendix

### Scenario 1: Transactions API Sync

Pattern:

```text
cursor pagination + validation + checkpoint
```

Task:

```text
Sync transaction records reliably.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 2: Customer API Flattening

Pattern:

```text
nested JSON flattening
```

Task:

```text
Flatten customer.profile.address fields.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 3: Orders Incremental Sync

Pattern:

```text
updated_at watermark
```

Task:

```text
Fetch only changed orders.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 4: Vendor Rate Limit

Pattern:

```text
429 + Retry-After
```

Task:

```text
Respect API rate limits.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 5: API Backfill

Pattern:

```text
time-window extraction
```

Task:

```text
Backfill historical data safely.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 6: Webhook Events

Pattern:

```text
idempotent event processing
```

Task:

```text
Process duplicate webhook events safely.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 7: Export Job API

Pattern:

```text
POST + poll + download
```

Task:

```text
Process async export results.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 8: Deleted Users

Pattern:

```text
delete handling
```

Task:

```text
Keep target table aligned with source deletes.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 9: Schema Drift

Pattern:

```text
validation + raw landing
```

Task:

```text
Detect field/type changes.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 10: Count Anomaly

Pattern:

```text
observability
```

Task:

```text
Detect unexpected 0 record sync.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 11: Partial Write

Pattern:

```text
idempotency + checkpointing
```

Task:

```text
Recover from mid-page write failure.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 12: Token Refresh

Pattern:

```text
auth recovery
```

Task:

```text
Handle expired token once safely.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 13: Large Response

Pattern:

```text
generator + batch write
```

Task:

```text
Avoid memory overload.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 14: Invalid Payload

Pattern:

```text
dead-letter
```

Task:

```text
Capture malformed records.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```

### Scenario 15: Pagination Loop

Pattern:

```text
seen cursor guard
```

Task:

```text
Prevent infinite extraction loop.
```

Minimum expected answer:

```text
1. State the risk.
2. State the safe design.
3. Explain Python or pipeline implementation.
4. Explain observability.
5. Explain how to test it.
```

Passing score:

```text
4/5 or higher.
```


## 91. Drill Appendix

### Drill 1: Status Code Classification

Task:

```text
Classify 20 status-code scenarios as retryable or non-retryable.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Timeout Drill

Task:

```text
Rewrite unsafe requests.get calls to include timeouts and error handling.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Retry Drill

Task:

```text
Implement retry with bounded exponential backoff and jitter.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Rate Limit Drill

Task:

```text
Handle 429 with Retry-After and fallback backoff.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Pagination Drill

Task:

```text
Implement page, offset, cursor, and next URL pagination.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: Cursor Loop Drill

Task:

```text
Detect repeated cursor and max page count.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: JSON Shape Drill

Task:

```text
Validate response shape before processing.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Nested Flatten Drill

Task:

```text
Flatten nested users, transactions, and orders.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Validation Drill

Task:

```text
Validate required fields and split invalid records.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Dead-Letter Drill

Task:

```text
Design invalid record output with error context.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Checkpoint Drill

Task:

```text
Save/load checkpoint and explain when to update it.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Idempotency Drill

Task:

```text
Explain upsert, merge, dedupe, and partition overwrite.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Incremental Drill

Task:

```text
Design updated_at sync with lookback window.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Schema Drift Drill

Task:

```text
Respond to field type changes and missing fields.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Delete Drill

Task:

```text
Handle soft delete, delete endpoint, and snapshot compare.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Webhook Drill

Task:

```text
Process duplicate webhook delivery safely.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Backfill Drill

Task:

```text
Plan two-year API backfill under rate limits.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Testing Drill

Task:

```text
Use fake client to test pagination and validation.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 19: Observability Drill

Task:

```text
Define metrics, logs, and alerts for API ingestion.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 20: Full Mock

Task:

```text
Design end-to-end transactions API pipeline.
```

Minimum passing answer:

```text
1. State the API risk or requirement.
2. Explain safe handling.
3. Provide Python code or clear pseudocode.
4. Include edge cases.
5. Include Data Engineering production relevance.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 92. Quick Reference Cards

### Quick Card 1: Timeout

Summary:

```text
Always set timeout on HTTP calls.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 2: Retryable errors

Summary:

```text
Retry 408, 429, and 5xx with bounded backoff.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 3: Non-retryable errors

Summary:

```text
Do not blindly retry 400, 401, 403, 404, 422.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 4: Rate limit

Summary:

```text
Respect Retry-After and limit concurrency.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 5: Cursor pagination

Summary:

```text
Use next_cursor until absent; guard repeated cursors.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 6: Offset pagination

Summary:

```text
Use offset + limit; can be unstable for changing data.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 7: Incremental sync

Summary:

```text
Use watermark and checkpoint after successful persistence.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 8: Lookback

Summary:

```text
Query overlap window for late updates and dedupe.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 9: Idempotency

Summary:

```text
Use upsert/merge/dedupe/partition overwrite.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 10: Dead-letter

Summary:

```text
Store invalid records with raw payload and error reasons.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 11: Raw landing

Summary:

```text
Keep raw API data for replay and audit.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 12: Schema drift

Summary:

```text
Validate required fields and alert on invalid-rate changes.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 13: Deletes

Summary:

```text
Need soft delete, delete feed, or snapshot reconciliation.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 14: Webhooks

Summary:

```text
Assume at-least-once delivery and dedupe by event_id.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```

### Quick Card 15: Observability

Summary:

```text
Track records, retries, 429s, invalids, duration, watermark.
```

Interview check:

```text
Explain one coding example and one production failure scenario where this applies.
```
