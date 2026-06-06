# Hash Maps Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/dsa/hashmaps.md
```

This guide teaches and drills **hash maps for Data Engineering interviews**.

This is not a generic dictionary tutorial. It is an interview-focused pattern guide for candidates preparing for Data Engineering roles where coding rounds test fast lookup, counting, grouping, deduplication, indexing, prefix-sum memory, and record-processing skills.

Hash maps are one of the highest-ROI coding patterns because they appear in:

- LeetCode-style coding rounds
- Python record-processing questions
- SQL-like grouping logic written in Python
- log processing
- event counting
- deduplication
- latest-record selection
- join/enrichment simulation
- API response processing
- transaction reconciliation
- anomaly counting
- source-target comparison
- duplicate detection
- prefix-sum subarray problems
- sliding-window frequency problems
- top K frequency problems
- grouping and bucketing
- lookup tables
- in-memory indexes

Use this guide with:

- `docs/dsa-for-data-engineers.md`
- `docs/python-interview-guide.md`
- `docs/leetcode-practice-map.md`
- `docs/assessment-rubric.md`
- `docs/communication-rubric.md`
- `modes/dsa-drill-mode.md`
- `modes/python-drill-mode.md`
- `modes/pattern-mapper-mode.md`
- `modes/tutor-mode.md`
- `modes/review-mode.md`
- `modes/feedback-mode.md`
- `modes/weakness-repair-mode.md`
- `modes/interview-mode.md`
- `practice/dsa/arrays-strings.md`
- `practice/dsa/bfs-dfs-basics.md`
- `progress/CANDIDATE_PROFILE.md`
- `progress/CURRENT_STATE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Default interview standard if target companies are not provided:

```text
FAANG-style Data Engineering coding standard, scaled by candidate experience.
```


## 1. Purpose

The purpose of this guide is to make the candidate strong at the hash map pattern.

The candidate should learn to answer:

```text
When do I need a hash map?
When is a set enough?
When do I need Counter?
When do I need defaultdict?
When do I need value → index mapping?
When do I need key → aggregate mapping?
When do I need key → latest record mapping?
When do I need prefix sum → count mapping?
When do I need grouping?
When do I need two maps?
When should I not use a hash map?
What is the time and space complexity?
What edge cases can break the solution?
How does this map to Data Engineering work?
```

A candidate is interview-ready only when they can:

```text
recognize hash map trigger clues
explain brute force and optimization
choose dict/set/Counter/defaultdict correctly
write clean Python
handle duplicates
handle missing keys
handle invalid records
explain complexity
dry run map state
handle follow-up variations
connect the pattern to Data Engineering scenarios
```


## 2. Why Hash Maps Matter for Data Engineers

Hash maps are everywhere in Data Engineering coding interviews.

Data Engineering examples:

```text
Count events by event_type.
Count errors by service.
Deduplicate event_id values.
Find duplicate transaction_id values.
Keep latest record by primary key.
Join records with a small lookup table.
Group transactions by account_id.
Sum amount by user_id.
Find missing IDs between source and target.
Compare source and target duplicate counts.
Apply CDC changes to current state.
Parse logs and count status codes.
Track seen files in a batch.
Build merchant normalization lookup.
Detect repeated API records.
Compute top K categories after counting.
Track prefix sums for cumulative transaction windows.
```

Interviewers ask hash map problems because they reveal whether the candidate can replace expensive nested loops with efficient state tracking.

Weak candidate behavior:

```text
For every record, loop through every other record.
```

Strong candidate behavior:

```text
Build a hash map once, then use O(1) average lookups while scanning.
```


## 3. Core Mental Model

A hash map is a key-value memory structure.

```text
key → value
```

Examples:

```text
event_type → count
user_id → total_amount
transaction_id → latest_transaction_record
file_name → processed_status
customer_id → customer_profile
prefix_sum → count_seen_so_far
word_signature → list_of_words
```

Core question:

```text
What do I need to remember while scanning?
```

Mapping answers:

```text
Need count → dict or Counter.
Need membership only → set.
Need group list → defaultdict(list).
Need sum by key → dict/defaultdict(int).
Need latest record → dict keyed by ID.
Need index lookup → dict value → index.
Need frequency comparison → Counter or dict counts.
Need repeated prefix sums → dict prefix_sum → count.
Need original object by ID → dict ID → object.
```

Interview line:

```text
I use a hash map because I need fast lookup or aggregation by key while scanning the data once.
```


## 4. Hash Map vs Set vs Counter vs defaultdict

### dict

Use when you need:

```text
key → value
```

Examples:

```text
user_id → total_amount
value → index
record_id → latest_record
```

### set

Use when you only need:

```text
membership / uniqueness
```

Examples:

```text
seen_event_ids
processed_files
valid_statuses
```

### Counter

Use when you need:

```text
frequency counts
```

Examples:

```text
event_type counts
character counts
error code counts
```

### defaultdict

Use when you need convenient defaults.

Examples:

```text
defaultdict(int) for sums/counts
defaultdict(list) for grouping
defaultdict(set) for graph adjacency or unique groups
```

Strict rule:

```text
Use the simplest structure that preserves the information required.
```

Common mistake:

```text
Using set for latest record per ID. A set only remembers existence, not the latest value.
```


## 5. Standard Answer Framework

Use this framework for every hash map problem:

```text
1. Restate the problem.
2. Identify what needs fast lookup/count/grouping.
3. Explain brute force.
4. State why brute force is slow.
5. Define hash map key.
6. Define hash map value.
7. Explain scan/update logic.
8. Write code.
9. Dry run map state.
10. Explain edge cases.
11. Explain time complexity.
12. Explain space complexity.
13. Handle follow-up.
```

Short version:

```text
Key:
Value:
When updated:
When checked:
Result:
Complexity:
```

Example:

```text
For Two Sum:
Key = number seen earlier.
Value = index of that number.
Check = target - current exists.
Update = store current number after check.
```

Strict rule:

```text
No hash map code before defining key and value.
```


## 6. Scoring Rubric

Score each hash map attempt from 0 to 5.

### Score 0

No meaningful attempt.

### Score 1

Does not understand hash map use.

### Score 2

Uses hash map partially but wrong key/value or broken logic.

### Score 3

Correct for common cases but weak edge cases, explanation, or complexity.

### Score 4

Interview-ready. Correct key/value, clean code, edge cases, and complexity.

### Score 5

Strong. Handles variations, communicates clearly, and connects to Data Engineering scenarios.

Do not give 4+ if:

```text
candidate cannot define key and value
candidate uses list membership inside loop
candidate uses set when counts or latest values are needed
candidate cannot handle duplicates
candidate forgets missing key handling
candidate fails edge cases
candidate gives wrong complexity
candidate cannot dry run map state
```


## 7. Complexity Rules

Hash map operations are usually:

```text
insert: O(1) average
lookup: O(1) average
delete: O(1) average
```

Common complexities:

```text
single scan with hash map: O(n) time, O(n) space
two arrays with hash map: O(n + m) time
counting unique values: O(n) time, O(k) space
sorting after counting: O(k log k), where k is number of unique keys
top K with heap: O(n + k log u) or O(u log k), depending approach
prefix sum hash map: O(n) time, O(n) space
```

Interview wording:

```text
Time is O(n) because I scan the input once and each dictionary lookup/update is O(1) average.
Space is O(k), where k is the number of unique keys stored.
```

Important:

```text
Worst-case hash map operations can degrade with extreme collisions, but interviews usually expect average-case O(1).
```

Do not say:

```text
Space is O(1)
```

if the map can store up to n unique keys.


## 8. Edge Case Checklist

Hash map edge cases:

```text
empty input
one element
duplicates
negative numbers
zero values
same value used twice
missing key
None/null key
case sensitivity
whitespace normalization
duplicate records with different payloads
same timestamp tie
invalid record missing ID
large number of unique keys
mutable objects as keys
order requirements
target not found
multiple valid answers
```

Data Engineering-specific edge cases:

```text
missing event_id
duplicate transaction_id
same record_id with newer updated_at
same updated_at tie requiring ingestion_time
bad timestamp
case-insensitive merchant names
invalid log line
file name duplicate
source has duplicates but target does not
target has extra IDs
API sends same record in two pages
CDC update before insert
CDC delete for unknown key
```


## 9. Pattern Map

Hash map patterns:

```text
1. Fast lookup / complement lookup
2. Membership with set
3. Frequency counting
4. Grouping by key
5. Index mapping
6. Latest record by key
7. Aggregation by key
8. Prefix sum memory
9. Sliding window frequency map
10. Two-map comparison
11. Source-target reconciliation
12. In-memory join/enrichment
13. Top K after counting
14. Bucket/group signature
15. State machine by key
16. CDC current-state application
17. Duplicate conflict detection
18. First/last occurrence tracking
19. Bijective mapping
20. Cache / LRU basics
```

Pattern selection rule:

```text
If the problem says "for each item, find/check/count/group something seen before", think hash map.
```


## 10. Common Mistakes

Common hash map mistakes:

```text
Using nested loops instead of hash map.
Using list membership instead of set/dict.
Checking after inserting when same index cannot be reused.
Overwriting index when first index must be preserved.
Not handling duplicates.
Using set when count is needed.
Using Counter but forgetting negative counts.
Not deleting zero counts in sliding window.
Using mutable list/dict as dictionary key.
Forgetting to initialize default.
Using defaultdict(list) but appending wrong object.
Wrong key selection.
Wrong output grain.
No invalid record handling.
No complexity explanation.
No dry run.
```

Strict feedback:

```text
This is not interview-ready. You used a dictionary, but the key/value design is wrong, so the solution fails duplicates.
```


## 11. Pattern: Fast Lookup / Complement Lookup

### When to use

Use this pattern when:

```text
you need to find a matching value quickly
you need to avoid nested pair checks
you need complement = target - current
you need check if current has appeared before
```

Trigger phrases:

```text
two numbers
pair sum
complement
seen before
find matching record
avoid O(n²)
```

### Template

```python
def find_pair(items, target):
    seen = {}

    for index, value in enumerate(items):
        needed = target - value

        if needed in seen:
            return [seen[needed], index]

        seen[value] = index

    return []
```

### Data Engineering connection

```text
Find two transactions that sum to a reconciliation adjustment.
Match debit and credit records.
Find a previous event that pairs with current event.
```

### Key interview point

```text
Check complement before inserting current value so the same index is not reused.
```


## 12. Problem: Two Sum

LeetCode:

```text
1. Two Sum
Difficulty: Easy
Pattern: Hash map complement lookup
```

Problem:

```text
Given nums and target, return indices of two numbers such that they add up to target.
```

Approach:

```text
Scan nums.
For current value, compute complement = target - value.
If complement is already in map, return previous index and current index.
Otherwise store current value → index.
```

Code:

```python
def two_sum(nums, target):
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in seen:
            return [seen[complement], index]

        seen[value] = index

    return []
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Edge cases:

```text
negative numbers
duplicate values
same value needed twice
no solution
multiple solutions
```

Data Engineering connection:

```text
Find two transactions that reconcile to a target adjustment amount.
```

Common mistake:

```text
Store current value before checking complement. That can reuse the same index when target = 2 * value.
```

Follow-ups:

```text
What if input is sorted?
What if you need all pairs?
What if duplicate pairs should be unique?
```


## 13. Problem: Two Sum All Pairs

Custom variation:

```text
Return all unique value pairs that sum to target.
```

Pattern:

```text
Hash map/set + duplicate control
```

Code:

```python
def two_sum_all_unique_pairs(nums, target):
    seen = set()
    pairs = set()

    for value in nums:
        complement = target - value

        if complement in seen:
            pair = tuple(sorted((value, complement)))
            pairs.add(pair)

        seen.add(value)

    return [list(pair) for pair in pairs]
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Find unique debit/credit amount pairs that match a target adjustment.
```

Follow-up:

```text
What if you need index pairs, not value pairs?
```

Expected:

```text
Use value → list of indices or scan with counts depending requirement.
```


## 14. Pattern: Set Membership

A set is a hash map-like structure for membership only.

### Use set when

```text
you only need to know if value was seen
you need uniqueness
you need fast membership
you need set difference/intersection
```

Examples:

```text
contains duplicate
missing IDs
processed files
valid statuses
known users
```

Template:

```python
def has_duplicate(items):
    seen = set()

    for item in items:
        if item in seen:
            return True

        seen.add(item)

    return False
```

Interview line:

```text
A set is enough because I only need membership, not counts or associated values.
```

Common mistake:

```text
Using a set when the requirement says keep latest record or count occurrences.
```


## 15. Problem: Contains Duplicate

LeetCode:

```text
217. Contains Duplicate
Difficulty: Easy
Pattern: Set membership
```

Code:

```python
def contains_duplicate(nums):
    seen = set()

    for value in nums:
        if value in seen:
            return True

        seen.add(value)

    return False
```

Alternative:

```python
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Detect duplicate event IDs, transaction IDs, file names, or primary keys.
```

Common mistake:

```text
Using a list as seen creates O(n²) behavior.
```

Follow-up:

```text
Return the duplicate values.
```

Code:

```python
def duplicate_values(nums):
    seen = set()
    duplicates = set()

    for value in nums:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return list(duplicates)
```


## 16. Problem: Happy Number

LeetCode:

```text
202. Happy Number
Difficulty: Easy
Pattern: Set cycle detection
```

Problem:

```text
Repeatedly replace number by sum of squares of digits.
Return true if it reaches 1, false if it cycles.
```

Code:

```python
def is_happy(n):
    seen = set()

    def next_number(value):
        total = 0

        while value > 0:
            digit = value % 10
            total += digit * digit
            value //= 10

        return total

    while n != 1:
        if n in seen:
            return False

        seen.add(n)
        n = next_number(n)

    return True
```

Complexity:

```text
Time: Usually treated as O(log n) per transformation, bounded sequence for interview.
Space: O(k), number of seen values before cycle/reaching 1.
```

Data Engineering connection:

```text
Detect repeated state in iterative transformations.
```

Common mistake:

```text
No seen set, causing infinite loop on cycles.
```


## 17. Pattern: Frequency Counting

### When to use

Use frequency counting when:

```text
problem asks count/frequency
need compare two multisets
need top K frequent
need first unique
need duplicates with counts
need anagram check
```

### Template with dict

```python
def count_values(items):
    counts = {}

    for item in items:
        counts[item] = counts.get(item, 0) + 1

    return counts
```

### Template with Counter

```python
from collections import Counter

counts = Counter(items)
```

### Data Engineering examples

```text
count events by type
count error codes by service
count transactions per account
count files by date
count API statuses
```

Interview line:

```text
I need counts, so a set is not enough. I will use a dictionary or Counter.
```


## 18. Problem: Valid Anagram

LeetCode:

```text
242. Valid Anagram
Difficulty: Easy
Pattern: Frequency counting
```

Approach:

```text
Two strings are anagrams when their character counts match.
```

Counter code:

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

Manual code:

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts:
            return False

        counts[char] -= 1

        if counts[char] < 0:
            return False

    return True
```

Complexity:

```text
Time: O(n)
Space: O(k), where k is number of unique characters
```

Data Engineering connection:

```text
Compare normalized signature strings or canonicalized labels.
```

Follow-ups:

```text
What if case-insensitive?
What if spaces and punctuation should be ignored?
What if only lowercase English letters are allowed?
```


## 19. Problem: Ransom Note

LeetCode:

```text
383. Ransom Note
Difficulty: Easy
Pattern: Frequency counting
```

Problem:

```text
Can ransomNote be constructed from magazine letters?
Each magazine character can be used once.
```

Code:

```python
from collections import Counter

def can_construct(ransom_note, magazine):
    available = Counter(magazine)

    for char in ransom_note:
        if available[char] == 0:
            return False

        available[char] -= 1

    return True
```

Complexity:

```text
Time: O(n + m)
Space: O(k)
```

Data Engineering connection:

```text
Check whether available resources/events can satisfy a requested set of required tokens.
```

Common mistake:

```text
Using set loses counts. If magazine has one 'a' and ransom needs two 'a's, set is wrong.
```


## 20. Problem: First Unique Character in a String

LeetCode:

```text
387. First Unique Character in a String
Difficulty: Easy
Pattern: Frequency counting + order scan
```

Code:

```python
from collections import Counter

def first_uniq_char(s):
    counts = Counter(s)

    for index, char in enumerate(s):
        if counts[char] == 1:
            return index

    return -1
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Find first event/status that occurs exactly once in a sequence.
```

Common mistake:

```text
Using map iteration order instead of scanning original string when first position matters.
```


## 21. Problem: Find All Duplicates by Count

Custom variation:

```text
Return all values that appear more than once.
```

Pattern:

```text
Frequency counting
```

Code:

```python
def find_duplicates(items):
    counts = {}

    for item in items:
        counts[item] = counts.get(item, 0) + 1

    result = []

    for item, count in counts.items():
        if count > 1:
            result.append(item)

    return result
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Return duplicate primary keys in a batch.
```

Follow-up:

```text
Return duplicate values with counts.
```

Code:

```python
def duplicate_counts(items):
    counts = {}

    for item in items:
        counts[item] = counts.get(item, 0) + 1

    return {item: count for item, count in counts.items() if count > 1}
```


## 22. Pattern: Grouping by Key

Grouping means:

```text
key → list of records/items
```

Use when:

```text
group anagrams
group transactions by account
group logs by service
group records by date
group files by partition
group API records by endpoint
```

Template:

```python
from collections import defaultdict

def group_by_key(records):
    groups = defaultdict(list)

    for record in records:
        key = record["key"]
        groups[key].append(record)

    return dict(groups)
```

Interview line:

```text
I use defaultdict(list) because each key maps to a list of items in that group.
```

Common mistake:

```text
Using dict[key] = record and overwriting previous records instead of appending.
```


## 23. Problem: Group Anagrams

LeetCode:

```text
49. Group Anagrams
Difficulty: Medium
Pattern: Hash map grouping by signature
```

Approach:

```text
Words that are anagrams share the same sorted-character signature.
Group by that signature.
```

Code:

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        signature = "".join(sorted(word))
        groups[signature].append(word)

    return list(groups.values())
```

Alternative for lowercase English letters:

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        counts = [0] * 26

        for char in word:
            counts[ord(char) - ord("a")] += 1

        groups[tuple(counts)].append(word)

    return list(groups.values())
```

Complexity:

```text
Sorted signature: O(n * k log k)
Frequency tuple: O(n * k)
Space: O(n * k)
```

Data Engineering connection:

```text
Group merchant aliases or normalized labels by signature.
```

Follow-ups:

```text
What if unicode characters exist?
What if case-insensitive?
What if output order matters?
```


## 24. Data Engineering Custom Problem: Group Transactions by Account

Problem:

```text
Given transaction records, group valid transactions by account_id.
Return invalid_count for records missing account_id.
```

Pattern:

```text
defaultdict(list)
```

Code:

```python
from collections import defaultdict

def group_transactions_by_account(transactions):
    groups = defaultdict(list)
    invalid_count = 0

    for transaction in transactions:
        account_id = transaction.get("account_id")

        if account_id is None:
            invalid_count += 1
            continue

        groups[account_id].append(transaction)

    return dict(groups), invalid_count
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Interview point:

```text
This is GROUP BY-like logic in Python, but the value is a list of records.
```

Follow-up:

```text
Instead of list, return total amount per account.
```

Expected:

```text
Use account_id → running total.
```


## 25. Pattern: Aggregation by Key

Aggregation by key means:

```text
key → aggregate value
```

Common aggregates:

```text
count
sum
min
max
latest
earliest
average components
```

Template for sum:

```python
from collections import defaultdict

def sum_by_key(records):
    totals = defaultdict(float)

    for record in records:
        key = record["key"]
        amount = record["amount"]
        totals[key] += amount

    return dict(totals)
```

Data Engineering examples:

```text
revenue by customer
spend by category
error count by service
transactions by account
bytes processed by pipeline
records loaded by table
```

Interview line:

```text
I will use a dictionary keyed by the grouping column and update the running aggregate for each record.
```


## 26. Data Engineering Custom Problem: Sum Amount by User

Problem:

```text
Given transactions, return total amount per user_id.
Skip invalid records missing user_id or amount and return invalid_count.
```

Pattern:

```text
Hash map aggregation
```

Code:

```python
from collections import defaultdict

def sum_amount_by_user(transactions):
    totals = defaultdict(float)
    invalid_count = 0

    for transaction in transactions:
        user_id = transaction.get("user_id")
        amount = transaction.get("amount")

        if user_id is None or amount is None:
            invalid_count += 1
            continue

        totals[user_id] += amount

    return dict(totals), invalid_count
```

Complexity:

```text
Time: O(n)
Space: O(u), where u is unique users
```

Follow-ups:

```text
How do you handle amount as string?
How do you handle invalid negative amounts?
How do you return average amount per user?
```


## 27. Data Engineering Custom Problem: Average Amount by Category

Problem:

```text
Given transactions with category and amount, return average amount per category.
```

Pattern:

```text
Hash map with sum and count
```

Code:

```python
from collections import defaultdict

def average_amount_by_category(transactions):
    totals = defaultdict(float)
    counts = defaultdict(int)

    for transaction in transactions:
        category = transaction.get("category")
        amount = transaction.get("amount")

        if category is None or amount is None:
            continue

        totals[category] += amount
        counts[category] += 1

    averages = {}

    for category in totals:
        averages[category] = totals[category] / counts[category]

    return averages
```

Complexity:

```text
Time: O(n + k)
Space: O(k)
```

Interview point:

```text
Average requires both sum and count, not only one value.
```


## 28. Pattern: Index Mapping

Index mapping means:

```text
value → index
```

Use when:

```text
need return indices
need remember first occurrence
need compute distance between duplicates
need find previous position
need reconstruct path/order
```

Examples:

```text
Two Sum
first occurrence of character
minimum distance between repeated IDs
longest substring last seen index
```

Template:

```python
first_index = {}

for index, value in enumerate(items):
    if value not in first_index:
        first_index[value] = index
```

Important:

```text
If first occurrence matters, do not overwrite.
If latest occurrence matters, overwrite intentionally.
```

Interview line:

```text
The value maps to its index because the output requires positions, not just values.
```


## 29. Problem: First Occurrence and Last Occurrence

Custom problem:

```text
Given a list of IDs, return first and last index for each ID.
```

Pattern:

```text
Hash map index tracking
```

Code:

```python
def first_last_indices(ids):
    positions = {}

    for index, record_id in enumerate(ids):
        if record_id not in positions:
            positions[record_id] = [index, index]
        else:
            positions[record_id][1] = index

    return positions
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Find first and latest occurrence of transaction IDs in a batch.
```

Common mistake:

```text
Overwriting first index accidentally.
```


## 30. Problem: Isomorphic Strings

LeetCode:

```text
205. Isomorphic Strings
Difficulty: Easy
Pattern: Two hash maps / bijection
```

Problem:

```text
Characters in s can be replaced to get t.
Each character must map to exactly one character and no two characters may map to same character.
```

Approach:

```text
Need mapping s → t and t → s to enforce one-to-one relationship.
```

Code:

```python
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for a, b in zip(s, t):
        if a in s_to_t and s_to_t[a] != b:
            return False

        if b in t_to_s and t_to_s[b] != a:
            return False

        s_to_t[a] = b
        t_to_s[b] = a

    return True
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Validate one-to-one mapping between source codes and normalized codes.
```

Common mistake:

```text
Using only one map allows two source characters to map to same target character.
```


## 31. Problem: Word Pattern

LeetCode:

```text
290. Word Pattern
Difficulty: Easy
Pattern: Two hash maps / bijection
```

Problem:

```text
Pattern characters must map one-to-one to words.
```

Code:

```python
def word_pattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word and char_to_word[char] != word:
            return False

        if word in word_to_char and word_to_char[word] != char:
            return False

        char_to_word[char] = word
        word_to_char[word] = char

    return True
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Validate stable mapping between event code pattern and event names.
```


## 32. Pattern: Latest Record by Key

Latest record by key is a very important Data Engineering pattern.

Use when:

```text
dedupe records by ID
keep latest update
apply API updates
apply CDC changes
current state table
latest status per transaction
latest customer profile
```

State:

```text
record_id → latest_record
```

Comparison key:

```text
updated_at
event_time
ingestion_time
sequence_number
version
```

Template:

```python
def latest_by_id(records):
    latest = {}

    for record in records:
        record_id = record["id"]
        timestamp = record["updated_at"]

        if record_id not in latest:
            latest[record_id] = record
            continue

        if timestamp > latest[record_id]["updated_at"]:
            latest[record_id] = record

    return list(latest.values())
```

Interview line:

```text
A set is not enough because I need to store the current best/latest record for each key.
```


## 33. Data Engineering Custom Problem: Keep Latest Event Per ID

Problem:

```text
Given events with event_id, event_time, and ingestion_time, keep latest event per event_id.
If event_time ties, use ingestion_time as tie-breaker.
Return invalid records missing event_id or event_time.
```

Pattern:

```text
Hash map latest record by key
```

Code:

```python
def keep_latest_event_per_id(events):
    latest = {}
    invalid = []

    for event in events:
        event_id = event.get("event_id")
        event_time = event.get("event_time")
        ingestion_time = event.get("ingestion_time")

        if event_id is None or event_time is None:
            invalid.append({"record": event, "reason": "missing_event_id_or_event_time"})
            continue

        new_key = (event_time, ingestion_time)

        if event_id not in latest:
            latest[event_id] = event
            continue

        current = latest[event_id]
        current_key = (
            current.get("event_time"),
            current.get("ingestion_time"),
        )

        if new_key > current_key:
            latest[event_id] = event

    return list(latest.values()), invalid
```

Complexity:

```text
Time: O(n)
Space: O(u), where u is unique event IDs
```

Follow-ups:

```text
What if timestamps are strings?
What if ingestion_time is missing?
What if duplicate event_id has different payload but same timestamp?
```


## 34. Data Engineering Custom Problem: Latest Transaction Status

Problem:

```text
Given transaction status events:
transaction_id, status, updated_at

Return current status per transaction_id.
```

Pattern:

```text
Hash map latest state
```

Code:

```python
def current_transaction_status(events):
    latest = {}

    for event in events:
        transaction_id = event.get("transaction_id")
        updated_at = event.get("updated_at")

        if transaction_id is None or updated_at is None:
            continue

        if transaction_id not in latest:
            latest[transaction_id] = event
        elif updated_at > latest[transaction_id]["updated_at"]:
            latest[transaction_id] = event

    return {
        transaction_id: event["status"]
        for transaction_id, event in latest.items()
    }
```

Complexity:

```text
Time: O(n)
Space: O(u)
```

Data Engineering connection:

```text
Current-state table from status events.
```

Follow-up:

```text
What if updates can arrive out of order?
```

Answer:

```text
Compare updated_at or sequence number, not arrival order.
```


## 35. Pattern: Prefix Sum + Hash Map

Prefix sum + hash map is a key medium-level pattern.

Use when:

```text
subarray sum equals k
count subarrays with target sum
numbers can be negative
need remember previous cumulative sums
```

Core equation:

```text
sum(i..j) = prefix[j] - prefix[i - 1]
```

If:

```text
current_prefix - previous_prefix = k
```

Then:

```text
previous_prefix = current_prefix - k
```

State:

```text
prefix_sum → count_seen
```

Template:

```python
from collections import defaultdict

def count_subarrays_with_sum(nums, k):
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1

    current = 0
    result = 0

    for value in nums:
        current += value
        result += prefix_counts[current - k]
        prefix_counts[current] += 1

    return result
```

Important:

```text
prefix_counts[0] = 1 handles subarrays starting at index 0.
```


## 36. Problem: Subarray Sum Equals K

LeetCode:

```text
560. Subarray Sum Equals K
Difficulty: Medium
Pattern: Prefix sum + hash map
```

Code:

```python
from collections import defaultdict

def subarray_sum(nums, k):
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1

    current_sum = 0
    result = 0

    for value in nums:
        current_sum += value
        needed = current_sum - k
        result += prefix_counts[needed]
        prefix_counts[current_sum] += 1

    return result
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Why not sliding window:

```text
If numbers can be negative, sliding window cannot reliably shrink/grow based on sum.
```

Data Engineering connection:

```text
Count consecutive transaction windows that sum to a reconciliation target.
```

Common mistakes:

```text
forgetting prefix_counts[0] = 1
using set instead of count map
updating current prefix before checking needed in the wrong variation
assuming positive numbers only
```


## 37. Problem: Continuous Subarray Sum

LeetCode:

```text
523. Continuous Subarray Sum
Difficulty: Medium
Pattern: Prefix sum remainder + hash map
```

Problem:

```text
Check if there is a subarray of at least length 2 whose sum is multiple of k.
```

Core idea:

```text
If two prefix sums have same remainder mod k, the subarray between them sums to multiple of k.
```

Code:

```python
def check_subarray_sum(nums, k):
    remainder_first_index = {0: -1}
    current_sum = 0

    for index, value in enumerate(nums):
        current_sum += value
        remainder = current_sum % k

        if remainder in remainder_first_index:
            if index - remainder_first_index[remainder] >= 2:
                return True
        else:
            remainder_first_index[remainder] = index

    return False
```

Complexity:

```text
Time: O(n)
Space: O(min(n, k)) for positive k
```

Data Engineering connection:

```text
Detect if a consecutive batch total aligns with a periodic multiple/checkpoint.
```

Common mistake:

```text
Overwriting first index. We need earliest index to maximize length.
```


## 38. Problem: Contiguous Array

LeetCode:

```text
525. Contiguous Array
Difficulty: Medium
Pattern: Prefix balance + hash map
```

Problem:

```text
Given binary array, find max length of contiguous subarray with equal number of 0 and 1.
```

Core idea:

```text
Treat 0 as -1 and 1 as +1.
If same balance appears twice, subarray between has equal 0s and 1s.
```

Code:

```python
def find_max_length(nums):
    first_index = {0: -1}
    balance = 0
    best = 0

    for index, value in enumerate(nums):
        balance += 1 if value == 1 else -1

        if balance in first_index:
            best = max(best, index - first_index[balance])
        else:
            first_index[balance] = index

    return best
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Find longest balanced period between two statuses, such as success/failure if encoded.
```

Common mistake:

```text
Overwriting first occurrence of a balance.
```


## 39. Pattern: Sliding Window + Frequency Map

Sliding window + hash map is used for substring/subarray problems where the window has counts.

Use when:

```text
contiguous substring/subarray
need count distinct
need no duplicates
need at most K distinct
need anagram/permutation in window
need replacement count
```

State:

```text
char/value → count inside current window
```

Template:

```python
from collections import defaultdict

def variable_window(items, k):
    counts = defaultdict(int)
    left = 0
    best = 0

    for right, value in enumerate(items):
        counts[value] += 1

        while window_is_invalid(counts, k):
            left_value = items[left]
            counts[left_value] -= 1

            if counts[left_value] == 0:
                del counts[left_value]

            left += 1

        best = max(best, right - left + 1)

    return best
```

Common mistake:

```text
Not deleting zero-count keys, causing distinct count to be wrong.
```


## 40. Problem: Longest Substring Without Repeating Characters

LeetCode:

```text
3. Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Sliding window + set/hash map
```

Set version:

```python
def length_of_longest_substring(s):
    seen = set()
    left = 0
    best = 0

    for right, char in enumerate(s):
        while char in seen:
            seen.remove(s[left])
            left += 1

        seen.add(char)
        best = max(best, right - left + 1)

    return best
```

Last-seen map version:

```python
def length_of_longest_substring(s):
    last_seen = {}
    left = 0
    best = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Longest sequence of events in a session without repeated event type.
```

Common mistake:

```text
Moving left backward when using last_seen map.
```


## 41. Problem: Longest Substring with At Most K Distinct Characters

LeetCode:

```text
340. Longest Substring with At Most K Distinct Characters
Difficulty: Medium
Pattern: Sliding window + frequency map
```

Code:

```python
from collections import defaultdict

def length_of_longest_substring_k_distinct(s, k):
    if k == 0:
        return 0

    counts = defaultdict(int)
    left = 0
    best = 0

    for right, char in enumerate(s):
        counts[char] += 1

        while len(counts) > k:
            left_char = s[left]
            counts[left_char] -= 1

            if counts[left_char] == 0:
                del counts[left_char]

            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Longest event sequence with at most K event types.
```

Common mistake:

```text
Not deleting zero counts, so len(counts) stays too large.
```


## 42. Problem: Fruit Into Baskets

LeetCode:

```text
904. Fruit Into Baskets
Difficulty: Medium
Pattern: Sliding window + at most 2 distinct values
```

Same as:

```text
Longest subarray with at most 2 distinct values.
```

Code:

```python
from collections import defaultdict

def total_fruit(fruits):
    counts = defaultdict(int)
    left = 0
    best = 0

    for right, fruit in enumerate(fruits):
        counts[fruit] += 1

        while len(counts) > 2:
            left_fruit = fruits[left]
            counts[left_fruit] -= 1

            if counts[left_fruit] == 0:
                del counts[left_fruit]

            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(1), because at most 3 keys temporarily
```

Data Engineering connection:

```text
Longest contiguous event window containing at most two event categories.
```


## 43. Problem: Minimum Window Substring

LeetCode:

```text
76. Minimum Window Substring
Difficulty: Hard
Pattern: Sliding window + frequency map
```

Problem:

```text
Find minimum substring of s containing all characters from t with required counts.
```

Code:

```python
from collections import Counter, defaultdict

def min_window(s, t):
    if not s or not t:
        return ""

    required = Counter(t)
    window = defaultdict(int)

    have = 0
    need = len(required)

    left = 0
    best_length = float("inf")
    best_range = (0, 0)

    for right, char in enumerate(s):
        window[char] += 1

        if char in required and window[char] == required[char]:
            have += 1

        while have == need:
            current_length = right - left + 1

            if current_length < best_length:
                best_length = current_length
                best_range = (left, right)

            left_char = s[left]
            window[left_char] -= 1

            if left_char in required and window[left_char] < required[left_char]:
                have -= 1

            left += 1

    if best_length == float("inf"):
        return ""

    start, end = best_range
    return s[start:end + 1]
```

Complexity:

```text
Time: O(n + m)
Space: O(k)
```

Data Engineering connection:

```text
Find smallest contiguous log segment containing all required event types.
```

Common mistakes:

```text
tracking unique chars but ignoring required counts
shrinking window before recording answer
```


## 44. Pattern: Two-Map Comparison

Use two maps when comparing relationships, frequencies, or bijections.

Examples:

```text
isomorphic strings
word pattern
anagram comparison
source-target counts
schema field comparison
```

Types:

```text
map A → B and map B → A
Counter(source) vs Counter(target)
field_name → type in source vs target
```

Data Engineering examples:

```text
validate source code to target code mapping is one-to-one
compare source and target duplicate counts
compare schema field types
compare expected vs actual files
```

Interview line:

```text
One map is not enough because I must enforce both directions of the relationship.
```


## 45. Data Engineering Custom Problem: Source-Target Count Reconciliation

Problem:

```text
Given source_ids and target_ids, return:
- missing_in_target
- extra_in_target
- count_mismatches for IDs with different duplicate counts
```

Pattern:

```text
Counter comparison
```

Code:

```python
from collections import Counter

def reconcile_id_counts(source_ids, target_ids):
    source_counts = Counter(source_ids)
    target_counts = Counter(target_ids)

    all_ids = set(source_counts) | set(target_counts)

    missing_in_target = []
    extra_in_target = []
    count_mismatches = {}

    for record_id in all_ids:
        source_count = source_counts.get(record_id, 0)
        target_count = target_counts.get(record_id, 0)

        if source_count > 0 and target_count == 0:
            missing_in_target.append(record_id)
        elif source_count == 0 and target_count > 0:
            extra_in_target.append(record_id)
        elif source_count != target_count:
            count_mismatches[record_id] = {
                "source_count": source_count,
                "target_count": target_count,
            }

    return {
        "missing_in_target": missing_in_target,
        "extra_in_target": extra_in_target,
        "count_mismatches": count_mismatches,
    }
```

Complexity:

```text
Time: O(n + m)
Space: O(u), where u is unique IDs across both
```

Interview point:

```text
Set comparison is not enough when duplicate counts matter.
```


## 46. Data Engineering Custom Problem: Schema Comparison

Problem:

```text
Given source schema and target schema as dictionaries:
field_name → data_type

Return missing fields, extra fields, and type mismatches.
```

Pattern:

```text
Hash map comparison
```

Code:

```python
def compare_schemas(source_schema, target_schema):
    source_fields = set(source_schema)
    target_fields = set(target_schema)

    missing_in_target = list(source_fields - target_fields)
    extra_in_target = list(target_fields - source_fields)

    type_mismatches = {}

    for field in source_fields & target_fields:
        if source_schema[field] != target_schema[field]:
            type_mismatches[field] = {
                "source_type": source_schema[field],
                "target_type": target_schema[field],
            }

    return {
        "missing_in_target": missing_in_target,
        "extra_in_target": extra_in_target,
        "type_mismatches": type_mismatches,
    }
```

Complexity:

```text
Time: O(n + m)
Space: O(n + m)
```

Data Engineering connection:

```text
Schema validation before loading API/file data to target.
```


## 47. Pattern: In-Memory Join / Enrichment

Use a hash map to simulate a small lookup join.

Use when:

```text
one dataset is small enough to fit in memory
you need enrich records by ID
you need avoid nested loop join
```

State:

```text
lookup_id → lookup_record
```

Template:

```python
def enrich_records(facts, dimensions):
    lookup = {}

    for dimension in dimensions:
        lookup[dimension["id"]] = dimension

    enriched = []

    for fact in facts:
        dimension = lookup.get(fact["id"])

        if dimension is None:
            continue

        enriched.append({**fact, **dimension})

    return enriched
```

Data Engineering connection:

```text
Join transactions with merchant/category lookup in Python.
```

Interview line:

```text
I build a lookup dictionary from the smaller dataset, then scan the larger dataset once.
```


## 48. Data Engineering Custom Problem: Enrich Orders with Customers

Problem:

```text
Given orders and customers, enrich each order with customer segment.
Skip orders with unknown customer_id and return missing_customer_count.
```

Pattern:

```text
Hash map lookup join
```

Code:

```python
def enrich_orders_with_customer_segment(orders, customers):
    customer_lookup = {}

    for customer in customers:
        customer_id = customer.get("customer_id")

        if customer_id is not None:
            customer_lookup[customer_id] = customer

    enriched = []
    missing_customer_count = 0

    for order in orders:
        customer_id = order.get("customer_id")
        customer = customer_lookup.get(customer_id)

        if customer is None:
            missing_customer_count += 1
            continue

        enriched_order = dict(order)
        enriched_order["customer_segment"] = customer.get("segment")
        enriched.append(enriched_order)

    return enriched, missing_customer_count
```

Complexity:

```text
Time: O(o + c)
Space: O(c)
```

Follow-ups:

```text
What if customers have duplicate customer_id?
What if one customer has multiple segments over time?
What if the lookup dataset is too large for memory?
```

Expected:

```text
Duplicate key handling, SCD/as-of join logic, or database/distributed join.
```


## 49. Pattern: Top K After Counting

Top K frequency problems usually start with a hash map.

Steps:

```text
1. Count frequencies with hash map.
2. Select top K by sorting or heap.
```

Options:

### Sort

```text
Simple.
O(u log u), where u = unique values.
```

### Heap

```text
Better when k is small and u is large.
O(u log k).
```

### Bucket sort

```text
Can be O(n) for frequency problems.
```

Interview line:

```text
The hash map gives counts. Then I can sort or use a heap depending on constraints.
```


## 50. Problem: Top K Frequent Elements

LeetCode:

```text
347. Top K Frequent Elements
Difficulty: Medium
Pattern: Frequency map + heap/sort/bucket
```

Sort approach:

```python
from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [value for value, count in sorted_items[:k]]
```

Complexity:

```text
Time: O(n + u log u)
Space: O(u)
```

Heap approach:

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    counts = Counter(nums)
    heap = []

    for value, count in counts.items():
        heapq.heappush(heap, (count, value))

        if len(heap) > k:
            heapq.heappop(heap)

    return [value for count, value in heap]
```

Complexity:

```text
Time: O(n + u log k)
Space: O(u + k)
```

Bucket approach:

```python
from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for value, count in counts.items():
        buckets[count].append(value)

    result = []

    for frequency in range(len(buckets) - 1, -1, -1):
        for value in buckets[frequency]:
            result.append(value)

            if len(result) == k:
                return result

    return result
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Top K services by error count, merchants by transaction count, event types by frequency.
```


## 51. Problem: Sort Characters By Frequency

LeetCode:

```text
451. Sort Characters By Frequency
Difficulty: Medium
Pattern: Frequency map + sorting
```

Code:

```python
from collections import Counter

def frequency_sort(s):
    counts = Counter(s)
    parts = []

    for char, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        parts.append(char * count)

    return "".join(parts)
```

Complexity:

```text
Time: O(n + k log k)
Space: O(n + k)
```

Data Engineering connection:

```text
Sort categories/status codes by frequency for report/debug summary.
```

Common mistake:

```text
Sorting original characters without aggregating frequency first.
```


## 52. Data Engineering Custom Problem: Top Error Services

Problem:

```text
Given log records with service and level, return top k services by ERROR count.
Skip invalid records missing service or level.
```

Pattern:

```text
Hash map count + top K
```

Code:

```python
from collections import Counter
import heapq

def top_error_services(logs, k):
    counts = Counter()
    invalid_count = 0

    for log in logs:
        service = log.get("service")
        level = log.get("level")

        if service is None or level is None:
            invalid_count += 1
            continue

        if level == "ERROR":
            counts[service] += 1

    top = heapq.nlargest(k, counts.items(), key=lambda item: item[1])

    return {
        "top_services": top,
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(n + u log k)
Space: O(u)
```

Follow-ups:

```text
How do you break ties?
How do you handle streaming logs?
How do you return results sorted by count desc and service asc?
```


## 53. Pattern: First / Last / Earliest / Latest Occurrence

Use hash maps for occurrence tracking.

### First occurrence

```text
Do not overwrite.
```

```python
if value not in first_index:
    first_index[value] = index
```

### Last occurrence

```text
Overwrite every time.
```

```python
last_index[value] = index
```

### Earliest timestamp

```text
Keep minimum.
```

### Latest timestamp

```text
Keep maximum.
```

Data Engineering examples:

```text
first event per user
latest event per user
first file arrival by partition
latest status by transaction
earliest error by service
```

Interview line:

```text
Whether I overwrite depends on whether first or latest occurrence matters.
```


## 54. Problem: Longest Consecutive Sequence

LeetCode:

```text
128. Longest Consecutive Sequence
Difficulty: Medium
Pattern: Hash set sequence starts
```

Problem:

```text
Find length of longest consecutive elements sequence.
Must run in O(n).
```

Approach:

```text
Put all numbers in set.
Only start counting at numbers where num - 1 is not present.
Then count forward.
```

Code:

```python
def longest_consecutive(nums):
    values = set(nums)
    best = 0

    for value in values:
        if value - 1 not in values:
            current = value
            length = 1

            while current + 1 in values:
                current += 1
                length += 1

            best = max(best, length)

    return best
```

Complexity:

```text
Time: O(n) average
Space: O(n)
```

Data Engineering connection:

```text
Find longest consecutive sequence of processed partition dates or batch IDs.
```

Common mistake:

```text
Starting sequence count from every number causes O(n²) in worst case.
```


## 55. Problem: Longest Consecutive Processed Dates

Custom variation:

```text
Given processed day numbers, return longest consecutive processed streak.
```

Pattern:

```text
Set sequence start
```

Code:

```python
def longest_processed_streak(days):
    day_set = set(days)
    best = 0

    for day in day_set:
        if day - 1 not in day_set:
            current = day
            streak = 1

            while current + 1 in day_set:
                current += 1
                streak += 1

            best = max(best, streak)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Check longest consecutive successful pipeline run streak.
```


## 56. Pattern: State Machine by Key

Sometimes each key has a state.

Examples:

```text
transaction_id → current_status
order_id → latest_lifecycle_state
file_name → processing_status
customer_id → active/inactive
CDC primary_key → current_record
```

Template:

```python
def apply_events(events):
    state = {}

    for event in events:
        key = event["id"]
        action = event["action"]

        if action == "delete":
            state.pop(key, None)
        else:
            state[key] = event

    return state
```

Important:

```text
If events can arrive out of order, use sequence_number or updated_at to decide whether to apply.
```

Data Engineering connection:

```text
CDC and event-sourced current state.
```


## 57. Data Engineering Custom Problem: Apply CDC Events

Problem:

```text
Given CDC events with:
id, op, updated_at, payload

op can be INSERT, UPDATE, DELETE.
Return current state by id.
Ignore older events if a newer updated_at already exists.
```

Pattern:

```text
Hash map current state by key
```

Code:

```python
def apply_cdc_events(events):
    state = {}
    latest_timestamp = {}

    for event in events:
        record_id = event.get("id")
        op = event.get("op")
        updated_at = event.get("updated_at")

        if record_id is None or op is None or updated_at is None:
            continue

        if record_id in latest_timestamp and updated_at < latest_timestamp[record_id]:
            continue

        latest_timestamp[record_id] = updated_at

        if op == "DELETE":
            state.pop(record_id, None)
        elif op in {"INSERT", "UPDATE"}:
            state[record_id] = event.get("payload", {})
        else:
            continue

    return state
```

Complexity:

```text
Time: O(n)
Space: O(u)
```

Follow-ups:

```text
What if two events have same updated_at?
What if sequence_number is available?
What if update arrives before insert?
What if deletes should be soft deletes?
```

Interview point:

```text
CDC is not append-only; current state requires operation handling.
```


## 58. Pattern: Duplicate Conflict Detection

Duplicate detection is not always simple.

Types:

```text
exact duplicate
same ID same payload
same ID different payload
same business key different ID
same ID older timestamp
same ID same timestamp different payload
```

Hash map helps by storing:

```text
id → first payload
id → latest payload
id → list of conflicting payloads
id → hash of payload
```

Data Engineering use:

```text
detect duplicate event IDs with conflicting payloads
detect transaction ID collision
detect API duplicate records across pages
```

Interview line:

```text
I would distinguish harmless duplicate retries from conflicting duplicates with different payloads.
```


## 59. Data Engineering Custom Problem: Duplicate Event Conflicts

Problem:

```text
Given events with event_id and payload, identify event_ids that appear with different payloads.
```

Pattern:

```text
Hash map ID → payload signature
```

Code:

```python
def find_conflicting_event_duplicates(events):
    seen_payload = {}
    conflicts = {}

    for event in events:
        event_id = event.get("event_id")
        payload = event.get("payload")

        if event_id is None:
            continue

        payload_signature = repr(sorted(payload.items())) if isinstance(payload, dict) else repr(payload)

        if event_id not in seen_payload:
            seen_payload[event_id] = payload_signature
        elif seen_payload[event_id] != payload_signature:
            conflicts[event_id] = {
                "first_payload_signature": seen_payload[event_id],
                "conflicting_payload_signature": payload_signature,
            }

    return conflicts
```

Complexity:

```text
Time: O(n * p log p) depending payload signature creation
Space: O(u)
```

Follow-ups:

```text
How would you create stable hash for nested payloads?
How would you store all conflicting examples?
How would you quarantine conflicts?
```


## 60. Pattern: Bucket / Signature Grouping

Signature grouping means converting an item into a canonical key.

Examples:

```text
sorted word → anagram group
frequency tuple → anagram group
normalized merchant name → merchant group
schema field set → schema signature
payload hash → duplicate group
```

Template:

```python
from collections import defaultdict

def group_by_signature(items):
    groups = defaultdict(list)

    for item in items:
        signature = make_signature(item)
        groups[signature].append(item)

    return groups
```

Data Engineering examples:

```text
group merchant aliases
group similar schemas
group duplicate payloads
group records by normalized business key
```

Interview line:

```text
The main decision is designing a signature that captures equality for this problem.
```


## 61. Data Engineering Custom Problem: Group Merchant Aliases

Problem:

```text
Given merchant names, normalize them and group aliases.
Normalization:
- lowercase
- strip spaces
- collapse spaces
- remove punctuation
```

Pattern:

```text
Signature grouping
```

Code:

```python
from collections import defaultdict
import string

def normalize_name(name):
    punctuation = set(string.punctuation)
    chars = []

    for char in name.strip().lower():
        if char in punctuation:
            chars.append(" ")
        else:
            chars.append(char)

    return " ".join("".join(chars).split())

def group_merchant_aliases(names):
    groups = defaultdict(list)

    for name in names:
        if name is None:
            continue

        signature = normalize_name(name)
        groups[signature].append(name)

    return dict(groups)
```

Complexity:

```text
Time: O(n * L), where L is average name length
Space: O(n * L)
```

Follow-ups:

```text
Should '&' become 'and'?
Should private limited / pvt ltd be standardized?
How do you handle fuzzy matching?
```

Interview point:

```text
Hash map grouping works only after defining a reliable normalization/signature.
```


## 62. Pattern: Cache / LRU Basics

Hash maps are used in cache problems.

Core idea:

```text
key → node/value
```

For LRU cache, hash map alone is not enough.

Need:

```text
hash map for O(1) lookup
doubly linked list or OrderedDict for recency order
```

Interview line:

```text
A hash map gives O(1) key lookup, but LRU also needs O(1) recency updates, so we pair it with an ordered structure.
```

This is less common for Data Engineering interviews than counting/grouping, but useful for FAANG-style coding rounds.


## 63. Problem: LRU Cache

LeetCode:

```text
146. LRU Cache
Difficulty: Medium
Pattern: Hash map + ordered structure
```

Python OrderedDict solution:

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

Complexity:

```text
get: O(1)
put: O(1)
space: O(capacity)
```

Data Engineering connection:

```text
Cache small lookup tables, API responses, or metadata with eviction policy.
```

Follow-up:

```text
Implement without OrderedDict using doubly linked list + dict.
```


## 64. Python Hash Map Tools

Python tools:

### dict

```python
counts = {}
counts[key] = counts.get(key, 0) + 1
```

### set

```python
seen = set()
seen.add(value)
```

### Counter

```python
from collections import Counter
counts = Counter(items)
```

### defaultdict

```python
from collections import defaultdict
groups = defaultdict(list)
totals = defaultdict(float)
```

### OrderedDict

```python
from collections import OrderedDict
```

Used for LRU-style ordered key behavior.

### dict comprehension

```python
lookup = {record["id"]: record for record in records}
```

Use carefully:

```text
If duplicate IDs exist, later records overwrite earlier records.
```


## 65. Python Gotchas

Python hash map gotchas:

```text
dict preserves insertion order in modern Python, but do not rely on ordering unless relevant and allowed.
list and dict are mutable and cannot be used as keys.
tuple can be used as key if all elements are hashable.
Counter returns 0 for missing keys.
defaultdict creates missing keys when accessed.
dict.get(key) returns None by default.
Using dict[key] without checking can raise KeyError.
```

Example issue:

```python
groups = defaultdict(list)
if groups["missing"]:
    ...
```

This creates key `"missing"`.

Better when checking existence:

```python
if "missing" in groups:
    ...
```

Interview point:

```text
Use get/defaultdict intentionally, not blindly.
```


## 66. Hashable Key Rules

Dictionary keys must be hashable.

Hashable examples:

```text
int
str
float
tuple of hashable values
frozenset
```

Not hashable:

```text
list
dict
set
```

If you need list-like key:

```python
key = tuple(my_list)
```

If you need dict-like payload signature:

```python
key = tuple(sorted(my_dict.items()))
```

For nested dictionaries:

```text
Need stable serialization or recursive normalization.
```

Interview example:

```text
For group anagrams using character counts, use tuple(counts), not list(counts), because lists are not hashable.
```


## 67. Hash Map Dry Run Style

When explaining, show map state.

Example: Two Sum

```text
nums = [2, 7, 11, 15], target = 9

index 0, value 2:
complement = 7, not seen
seen = {2: 0}

index 1, value 7:
complement = 2, seen
return [0, 1]
```

Example: Count events

```text
events = click, view, click

counts after click:
{click: 1}

after view:
{click: 1, view: 1}

after click:
{click: 2, view: 1}
```

Interview line:

```text
I will dry run the dictionary state to verify the update order.
```


## 68. Pattern Classification Drill

Classify each prompt.

```text
1. Return indices of two numbers that sum to target.
2. Check if array has duplicate values.
3. Count events by event_type.
4. Group transactions by account_id.
5. Keep latest record per customer_id.
6. Compare source and target IDs including duplicate counts.
7. Check if two strings are anagrams.
8. Find top 3 services by error count.
9. Count subarrays with sum k.
10. Longest substring without duplicate characters.
11. Validate one-to-one mapping between codes and names.
12. Enrich orders with customer segment.
13. Apply CDC insert/update/delete events.
14. Find conflicting duplicates by event_id.
15. Group merchant aliases by normalized name.
16. Find longest consecutive processed dates.
17. Return first unique character.
18. Find missing files from expected list.
19. Compare source schema and target schema.
20. Implement LRU cache.
```

Expected patterns:

```text
1. complement lookup hash map
2. set membership
3. frequency counting
4. defaultdict(list) grouping
5. latest record by key
6. Counter comparison
7. frequency count / Counter
8. count + top K
9. prefix sum + hash map
10. sliding window + set/map
11. two-map bijection
12. in-memory join lookup
13. state by key
14. duplicate conflict detection
15. signature grouping
16. set sequence starts
17. frequency count + order scan
18. set difference
19. map/set comparison
20. hash map + ordered structure
```

Passing standard:

```text
18/20 correct before timed hash map mocks.
```


## 69. High-ROI LeetCode List

Practice these first.

| No. | Title | Difficulty | Pattern |
|---:|---|---|---|
| 1 | Two Sum | Easy | Complement lookup |
| 217 | Contains Duplicate | Easy | Set membership |
| 242 | Valid Anagram | Easy | Frequency count |
| 383 | Ransom Note | Easy | Frequency count |
| 387 | First Unique Character in a String | Easy | Frequency + order |
| 49 | Group Anagrams | Medium | Group by signature |
| 205 | Isomorphic Strings | Easy | Two-map bijection |
| 290 | Word Pattern | Easy | Two-map bijection |
| 349 | Intersection of Two Arrays | Easy | Set |
| 350 | Intersection of Two Arrays II | Easy | Counter |
| 347 | Top K Frequent Elements | Medium | Count + heap/sort/bucket |
| 451 | Sort Characters By Frequency | Medium | Count + sort |
| 128 | Longest Consecutive Sequence | Medium | Set sequence starts |
| 560 | Subarray Sum Equals K | Medium | Prefix sum + map |
| 523 | Continuous Subarray Sum | Medium | Prefix remainder map |
| 525 | Contiguous Array | Medium | Prefix balance map |
| 3 | Longest Substring Without Repeating Characters | Medium | Sliding window + set/map |
| 340 | Longest Substring with At Most K Distinct Characters | Medium | Window + frequency map |
| 904 | Fruit Into Baskets | Medium | Window + frequency map |
| 76 | Minimum Window Substring | Hard | Window + frequency map |
| 146 | LRU Cache | Medium | Hash map + ordered structure |


## 70. Practice Ladder

### Level 1: Foundation

```text
Contains Duplicate
Valid Anagram
Ransom Note
First Unique Character
Intersection of Two Arrays
```

Exit:

```text
Candidate can use set, dict, Counter correctly.
```

### Level 2: Core hash map

```text
Two Sum
Group Anagrams
Isomorphic Strings
Word Pattern
Intersection of Two Arrays II
```

Exit:

```text
Candidate can define key/value and handle duplicates.
```

### Level 3: Medium patterns

```text
Top K Frequent Elements
Longest Consecutive Sequence
Subarray Sum Equals K
Contiguous Array
Sort Characters By Frequency
```

Exit:

```text
Candidate can combine hash maps with sorting, prefix sums, and sets.
```

### Level 4: Sliding window maps

```text
Longest Substring Without Repeating Characters
Longest Substring with At Most K Distinct
Fruit Into Baskets
Minimum Window Substring
```

Exit:

```text
Candidate can maintain frequency map while expanding/shrinking window.
```

### Level 5: Data Engineering custom

```text
Deduplicate event IDs
Count events by type
Latest record per ID
Source-target reconciliation
Apply CDC events
In-memory join enrichment
Log top K errors
Schema comparison
```

Exit:

```text
Candidate can apply hash maps to realistic Data Engineering record-processing tasks.
```


## 71. 7-Day Hash Map Plan

### Day 1: Set and basic dict

Problems:

```text
Contains Duplicate
Intersection of Two Arrays
Missing files custom
Duplicate values custom
```

Focus:

```text
membership
uniqueness
set difference
O(1) average lookup
```

### Day 2: Frequency counting

Problems:

```text
Valid Anagram
Ransom Note
First Unique Character
Count events by type custom
```

Focus:

```text
counts
Counter
dict.get
order scan after counting
```

### Day 3: Lookup and grouping

Problems:

```text
Two Sum
Group Anagrams
Group transactions by account
Enrich orders with customers
```

Focus:

```text
key/value design
grouping
lookup join
```

### Day 4: Latest and reconciliation

Problems:

```text
Latest record per ID
Latest transaction status
Source-target count reconciliation
Schema comparison
```

Focus:

```text
state by key
Counter comparison
record validation
```

### Day 5: Prefix sum maps

Problems:

```text
Subarray Sum Equals K
Continuous Subarray Sum
Contiguous Array
```

Focus:

```text
prefix sum
first index preservation
count map
```

### Day 6: Top K and set sequences

Problems:

```text
Top K Frequent Elements
Sort Characters By Frequency
Longest Consecutive Sequence
Top error services custom
```

Focus:

```text
count first
sort/heap/bucket
sequence starts
```

### Day 7: Mock and repair

Tasks:

```text
Run Hash Map Mock Set 2 or 3.
Review mistakes.
Repair weakest pattern.
Update progress.
```


## 72. 30-Day Hash Map Plan

### Week 1: Foundation

Focus:

```text
dict
set
Counter
defaultdict
key/value design
basic complexity
```

Problems:

```text
Two Sum
Contains Duplicate
Valid Anagram
Ransom Note
First Unique Character
Intersection
```

Exit:

```text
Easy hash map problems solved under 15 minutes.
```

### Week 2: Grouping and Data Engineering tasks

Focus:

```text
grouping
aggregation
latest record
lookup enrichment
source-target comparison
```

Problems:

```text
Group Anagrams
Group transactions
Sum by user
Latest record per ID
Enrich orders
Reconcile ID counts
```

Exit:

```text
Candidate can solve Python record-processing tasks with invalid record handling.
```

### Week 3: Medium LeetCode patterns

Focus:

```text
top K
prefix sum hash map
longest consecutive sequence
bijection
```

Problems:

```text
Top K Frequent
Subarray Sum Equals K
Continuous Subarray Sum
Contiguous Array
Longest Consecutive
Isomorphic Strings
Word Pattern
```

Exit:

```text
Candidate can explain prefix-sum map and count-vs-set differences.
```

### Week 4: Sliding windows, CDC, and mocks

Focus:

```text
sliding window frequency maps
CDC current state
duplicate conflicts
mock interviews
weakness repair
```

Problems:

```text
Longest Substring Without Repeating
At Most K Distinct
Minimum Window Substring
Apply CDC Events
Duplicate Event Conflicts
Hash Map Mock Set 4
```

Exit:

```text
Average mock score >= 4/5.
```


## 73. Hash Map Mock Set 1: Beginner

Problems:

```text
1. Contains Duplicate
2. Valid Anagram
3. Ransom Note
4. First Unique Character
5. Missing Files custom
```

Expected skills:

```text
set
Counter
dict counting
set difference
basic edge cases
```

Passing standard:

```text
Average score >= 4/5.
No list membership inside loops.
Correct complexity.
```


## 74. Hash Map Mock Set 2: Core

Problems:

```text
1. Two Sum
2. Group Anagrams
3. Isomorphic Strings
4. Intersection of Two Arrays II
5. Sum Amount by User custom
```

Expected skills:

```text
complement lookup
signature grouping
two-map bijection
Counter with duplicates
aggregation by key
```

Passing standard:

```text
Average score >= 4/5.
Candidate defines hash map key and value before coding.
```


## 75. Hash Map Mock Set 3: Data Engineering Flavor

Problems:

```text
1. Count ERROR logs by service.
2. Keep latest event per event_id.
3. Source-target count reconciliation.
4. Enrich orders with customer segment.
5. Apply CDC events to current state.
```

Expected skills:

```text
Counter
latest state map
Counter comparison
lookup join
state machine by key
invalid record handling
```

Passing standard:

```text
Average score >= 4/5.
Candidate handles invalid records and DE-specific edge cases.
```


## 76. Hash Map Mock Set 4: Strong Candidate

Problems:

```text
1. Top K Frequent Elements
2. Longest Consecutive Sequence
3. Subarray Sum Equals K
4. Minimum Window Substring
5. Duplicate Event Conflicts custom
```

Expected skills:

```text
frequency + top K
set sequence starts
prefix sum + count map
sliding window frequency
payload conflict detection
```

Passing standard:

```text
Average score >= 4/5.
Candidate handles follow-ups and explains trade-offs.
```


## 77. Timed Drill Protocol

Use this timing protocol.

### Easy hash map problem

```text
10-15 minutes
```

### Medium hash map problem

```text
25-35 minutes
```

### Hard sliding-window/hash-map problem

```text
40-45 minutes
```

Per problem:

```text
Minute 0-2:
Restate and clarify.

Minute 2-5:
Define key and value.

Minute 5-8:
Explain brute force and optimized hash map idea.

Minute 8-22:
Code.

Minute 22-26:
Dry run map state.

Minute 26-30:
Complexity and follow-up.
```

If candidate cannot define key/value:

```text
Stop and switch to tutor-mode.md or weakness-repair-mode.md.
```


## 78. Review Checklist

Review each hash map solution with:

```text
1. Did candidate identify hash map trigger?
2. Did candidate define key?
3. Did candidate define value?
4. Did candidate explain brute force?
5. Did candidate explain why hash map improves it?
6. Did candidate choose dict/set/Counter/defaultdict correctly?
7. Did candidate handle duplicates?
8. Did candidate handle missing keys?
9. Did candidate handle invalid records if DE-style?
10. Did candidate avoid O(n²)?
11. Did candidate dry run map state?
12. Did candidate explain time complexity?
13. Did candidate explain space complexity?
14. Did candidate handle follow-up?
15. Did candidate connect to Data Engineering?
```

Verdict examples:

```text
Correct pattern, wrong key.
Correct key, wrong value.
Set used but counts needed.
Works but misses duplicates.
Good LeetCode answer but weak DE invalid-record handling.
Interview-ready.
Strong.
```


## 79. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Uses nested loops | Complement/membership classification drills |
| Uses list membership | Set/dict lookup repair |
| Cannot define key/value | Key-value design drills |
| Uses set when count needed | Set vs Counter drills |
| Uses set when latest needed | Latest-record repair |
| Forgets duplicate handling | Duplicate edge-case drills |
| Overwrites first index | First occurrence drills |
| Prefix sum confusion | Prefix map visual drills |
| Window map zero-count bug | Sliding window frequency repair |
| No invalid record handling | DE custom record-processing drills |
| Wrong complexity | Complexity explanation drills |
| Cannot connect to DE | Data Engineering custom drills |
| Top K confusion | Count-first then rank drills |
| Two-map bijection confusion | Isomorphic/word pattern repair |

If weakness repeats:

```text
Use weakness-repair-mode.md.
```


## 80. Communication Scripts

### Hash map lookup script

```text
The brute force checks every pair, which is O(n²). I can optimize by storing previously seen values in a hash map, so each complement lookup is O(1) average.
```

### Frequency script

```text
I need counts, so a set is not enough. I will use a dictionary or Counter to track how many times each value appears.
```

### Grouping script

```text
The key is the grouping attribute and the value is a list of records in that group, so defaultdict(list) fits.
```

### Latest record script

```text
I will map each ID to the latest record seen so far and replace it only when the new record has a newer timestamp or sequence number.
```

### Prefix sum script

```text
I will track how many times each prefix sum has occurred. If current_sum - k was seen before, then a subarray ending here has sum k.
```

### Data Engineering script

```text
This is the same pattern as grouping or deduplicating records in a pipeline: scan once and maintain state keyed by business ID.
```


## 81. Candidate Self-Review Questions

After every hash map problem, candidate should answer:

```text
1. What made this a hash map problem?
2. What is the key?
3. What is the value?
4. When do I check the map?
5. When do I update the map?
6. Why is a set not enough, if it is not enough?
7. Why is Counter useful, if used?
8. What happens with duplicates?
9. What happens with missing/invalid input?
10. What is time complexity?
11. What is space complexity?
12. What Data Engineering scenario uses the same pattern?
```

If candidate cannot answer these:

```text
The problem is not fully learned.
```


## 82. Maintenance Drills

After completing hash maps, maintain skill with:

```text
1 easy hash map problem per week
1 medium hash map problem per week
1 Data Engineering custom hash map problem per week
1 prefix-sum map problem every 2 weeks
1 sliding-window map problem every 2 weeks
1 top K problem every 2 weeks
```

Maintenance rotation:

```text
Week 1: set + frequency
Week 2: grouping + latest record
Week 3: prefix sum + top K
Week 4: sliding window + DE mock
```

If score drops below 4:

```text
Run weakness-repair-mode.md for failed pattern.
```


## 83. Progress Tracking Template

Use this progress format.

```text
# Hash Maps Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Pattern | Difficulty | Score | Time | Mistake | Next Action

## Pattern Scores

Set membership:
Frequency counting:
Complement lookup:
Grouping:
Aggregation:
Latest record:
Index mapping:
Two-map comparison:
Prefix sum map:
Sliding window map:
Top K after counting:
In-memory join:
CDC state:
Duplicate conflict detection:

## Repeated Mistakes

-

## Repair Items

-

## Next Practice

Today:
This week:
Next mock:
```


## 84. Final Exit Test

Candidate passes hash maps when they can solve:

```text
1. Two Sum
2. Contains Duplicate
3. Valid Anagram
4. Ransom Note
5. First Unique Character
6. Group Anagrams
7. Isomorphic Strings
8. Top K Frequent Elements
9. Longest Consecutive Sequence
10. Subarray Sum Equals K
11. Contiguous Array
12. Longest Substring Without Repeating Characters
13. Minimum Window Substring
14. DE custom: count events by type
15. DE custom: latest record per ID
16. DE custom: source-target count reconciliation
17. DE custom: enrich orders with customers
18. DE custom: apply CDC events
19. DE custom: duplicate event conflicts
20. DE custom: schema comparison
```

Passing standard:

```text
Average score >= 4/5.
No list membership inside large loops.
No key/value confusion.
No set-vs-count confusion.
No missing duplicate handling.
No missing complexity explanations.
Can explain Data Engineering relevance.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles variations and pressure follow-ups.
```


## 85. Final Summary

Hash maps are one of the most important patterns for Data Engineering interviews.

They map directly to:

```text
counts
groups
dedupe
lookup joins
latest state
reconciliation
prefix sums
window frequencies
top K
CDC state
schema comparison
log aggregation
API record processing
```

The candidate must master:

```text
dict
set
Counter
defaultdict
key-value design
frequency counting
grouping
latest record
prefix sum maps
sliding window maps
top K after counting
two-map comparison
in-memory joins
Data Engineering edge cases
```

The mentor must be strict:

```text
No key/value explanation → not interview-ready.
No complexity → not interview-ready.
Wrong data structure → not interview-ready.
Only sample passes → not interview-ready.
No duplicate handling → not interview-ready.
```

The goal is not to memorize dictionary syntax.

The goal is to recognize what state must be remembered while scanning and use the correct hash-based structure to solve efficiently.


## 86. Problem Card Appendix

### Card 1: Two Sum

LeetCode:

```text
1. Two Sum
Difficulty: Easy
```

Primary pattern:

```text
Complement lookup
```

Key/value or state:

```text
value → index
```

Data Engineering connection:

```text
Find two transactions matching target adjustment.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Contains Duplicate

LeetCode:

```text
217. Contains Duplicate
Difficulty: Easy
```

Primary pattern:

```text
Set membership
```

Key/value or state:

```text
seen values
```

Data Engineering connection:

```text
Detect duplicate event IDs.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Valid Anagram

LeetCode:

```text
242. Valid Anagram
Difficulty: Easy
```

Primary pattern:

```text
Frequency count
```

Key/value or state:

```text
char → count
```

Data Engineering connection:

```text
Compare normalized signatures.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Ransom Note

LeetCode:

```text
383. Ransom Note
Difficulty: Easy
```

Primary pattern:

```text
Frequency count
```

Key/value or state:

```text
char → available count
```

Data Engineering connection:

```text
Check resource/token availability.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: First Unique Character

LeetCode:

```text
387. First Unique Character
Difficulty: Easy
```

Primary pattern:

```text
Frequency + order scan
```

Key/value or state:

```text
char → count
```

Data Engineering connection:

```text
Find first unique status/event marker.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Group Anagrams

LeetCode:

```text
49. Group Anagrams
Difficulty: Medium
```

Primary pattern:

```text
Signature grouping
```

Key/value or state:

```text
signature → words
```

Data Engineering connection:

```text
Group merchant aliases.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Isomorphic Strings

LeetCode:

```text
205. Isomorphic Strings
Difficulty: Easy
```

Primary pattern:

```text
Two-map bijection
```

Key/value or state:

```text
s→t and t→s
```

Data Engineering connection:

```text
Validate one-to-one code mapping.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Word Pattern

LeetCode:

```text
290. Word Pattern
Difficulty: Easy
```

Primary pattern:

```text
Two-map bijection
```

Key/value or state:

```text
pattern→word and word→pattern
```

Data Engineering connection:

```text
Validate event pattern mapping.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Intersection of Two Arrays

LeetCode:

```text
349. Intersection of Two Arrays
Difficulty: Easy
```

Primary pattern:

```text
Set
```

Key/value or state:

```text
set intersection
```

Data Engineering connection:

```text
Find IDs in both source and target.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Intersection of Two Arrays II

LeetCode:

```text
350. Intersection of Two Arrays II
Difficulty: Easy
```

Primary pattern:

```text
Counter
```

Key/value or state:

```text
value → count
```

Data Engineering connection:

```text
Compare duplicates across batches.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Top K Frequent Elements

LeetCode:

```text
347. Top K Frequent Elements
Difficulty: Medium
```

Primary pattern:

```text
Count + rank
```

Key/value or state:

```text
value → frequency
```

Data Engineering connection:

```text
Top services/merchants/events.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Sort Characters By Frequency

LeetCode:

```text
451. Sort Characters By Frequency
Difficulty: Medium
```

Primary pattern:

```text
Count + sort
```

Key/value or state:

```text
char → count
```

Data Engineering connection:

```text
Frequency report ordering.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Longest Consecutive Sequence

LeetCode:

```text
128. Longest Consecutive Sequence
Difficulty: Medium
```

Primary pattern:

```text
Set sequence starts
```

Key/value or state:

```text
all values set
```

Data Engineering connection:

```text
Longest processed partition streak.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Subarray Sum Equals K

LeetCode:

```text
560. Subarray Sum Equals K
Difficulty: Medium
```

Primary pattern:

```text
Prefix sum map
```

Key/value or state:

```text
prefix_sum → count
```

Data Engineering connection:

```text
Count transaction windows summing to target.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Continuous Subarray Sum

LeetCode:

```text
523. Continuous Subarray Sum
Difficulty: Medium
```

Primary pattern:

```text
Prefix remainder map
```

Key/value or state:

```text
remainder → first index
```

Data Engineering connection:

```text
Find periodic multiple windows.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Contiguous Array

LeetCode:

```text
525. Contiguous Array
Difficulty: Medium
```

Primary pattern:

```text
Prefix balance map
```

Key/value or state:

```text
balance → first index
```

Data Engineering connection:

```text
Find balanced binary status window.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Longest Substring Without Repeating Characters

LeetCode:

```text
3. Longest Substring Without Repeating Characters
Difficulty: Medium
```

Primary pattern:

```text
Window set/map
```

Key/value or state:

```text
char → last index or set
```

Data Engineering connection:

```text
Longest unique event sequence.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: At Most K Distinct

LeetCode:

```text
340. At Most K Distinct
Difficulty: Medium
```

Primary pattern:

```text
Window frequency map
```

Key/value or state:

```text
char → count
```

Data Engineering connection:

```text
Longest sequence with K event types.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Fruit Into Baskets

LeetCode:

```text
904. Fruit Into Baskets
Difficulty: Medium
```

Primary pattern:

```text
Window frequency map
```

Key/value or state:

```text
value → count
```

Data Engineering connection:

```text
At most 2 category window.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Minimum Window Substring

LeetCode:

```text
76. Minimum Window Substring
Difficulty: Hard
```

Primary pattern:

```text
Window frequency map
```

Key/value or state:

```text
char → count required/current
```

Data Engineering connection:

```text
Smallest log segment containing required events.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 21: LRU Cache

LeetCode:

```text
146. LRU Cache
Difficulty: Medium
```

Primary pattern:

```text
Hash map + ordered structure
```

Key/value or state:

```text
key → value/node
```

Data Engineering connection:

```text
Metadata/API cache with eviction.
```

Candidate must be able to explain:

```text
1. Why this is a hash map/set problem.
2. What the key is.
3. What the value is.
4. When the map is checked.
5. When the map is updated.
6. Edge cases.
7. Time complexity.
8. Space complexity.
9. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 87. Data Engineering Custom Problem Card Appendix

### Custom Card 1: Count Events by Type

State:

```text
event_type → count
```

Task:

```text
Count event frequencies and invalid records.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 2: Deduplicate Event IDs

State:

```text
seen_event_ids set
```

Task:

```text
Keep first event and skip duplicate event_id.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 3: Latest Event Per ID

State:

```text
event_id → latest_event
```

Task:

```text
Keep latest event using event_time and ingestion_time.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 4: Sum Amount by User

State:

```text
user_id → total_amount
```

Task:

```text
Aggregate transaction amount by user.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 5: Average Amount by Category

State:

```text
category → sum/count
```

Task:

```text
Compute grouped average.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 6: Group Transactions by Account

State:

```text
account_id → list[transaction]
```

Task:

```text
Group records by account.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 7: Missing Files

State:

```text
processed_files set
```

Task:

```text
Find expected files not processed.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 8: Source-Target Reconciliation

State:

```text
ID → count
```

Task:

```text
Find missing/extra/count mismatch IDs.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 9: Schema Comparison

State:

```text
field → type
```

Task:

```text
Compare source and target schema.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 10: Enrich Orders

State:

```text
customer_id → customer_record
```

Task:

```text
Lookup join from customers to orders.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 11: Top Error Services

State:

```text
service → error_count
```

Task:

```text
Find top K services by ERROR logs.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 12: Apply CDC Events

State:

```text
id → current_state
```

Task:

```text
Apply insert/update/delete events.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 13: Duplicate Event Conflicts

State:

```text
event_id → payload_signature
```

Task:

```text
Find duplicate IDs with conflicting payload.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 14: Group Merchant Aliases

State:

```text
normalized_name → aliases
```

Task:

```text
Group merchant names by normalized signature.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 15: Longest Processed Streak

State:

```text
set of days
```

Task:

```text
Find longest consecutive processed day numbers.
```

Minimum expected answer:

```text
1. Define input and output.
2. Define hash map key/state.
3. Handle invalid records if relevant.
4. Write O(n) or O(n + m) Python solution.
5. Explain time and space complexity.
6. Explain how this appears in a real pipeline.
```

Passing score:

```text
4/5 or higher.
```


## 88. Drill Appendix

### Drill 1: Set Membership

Task:

```text
Solve Contains Duplicate, Missing Files, and duplicate event_id detection.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Frequency Counting

Task:

```text
Solve Valid Anagram, Ransom Note, and count events by type.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Complement Lookup

Task:

```text
Solve Two Sum and two-sum-all-unique-pairs variation.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Grouping

Task:

```text
Solve Group Anagrams and group transactions by account.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Aggregation

Task:

```text
Sum amount by user and average amount by category.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: Latest State

Task:

```text
Keep latest event per ID and latest transaction status.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Two-Map Bijection

Task:

```text
Solve Isomorphic Strings and Word Pattern.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Counter Comparison

Task:

```text
Solve Intersection II and source-target count reconciliation.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Top K

Task:

```text
Solve Top K Frequent and top error services.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Prefix Sum Map

Task:

```text
Solve Subarray Sum Equals K, Continuous Subarray Sum, Contiguous Array.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Sliding Window Map

Task:

```text
Solve Longest Substring, At Most K Distinct, Minimum Window.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: In-Memory Join

Task:

```text
Enrich orders with customer lookup.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: CDC State

Task:

```text
Apply CDC events and handle delete/update edge cases.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Conflict Detection

Task:

```text
Find duplicate event IDs with different payloads.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Signature Grouping

Task:

```text
Group anagrams and merchant aliases.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Cache Basics

Task:

```text
Implement LRU Cache using OrderedDict.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Pattern Classification

Task:

```text
Classify 20 prompts before coding.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Timed Mock

Task:

```text
Run 5 problems in 90 minutes and review.
```

Minimum passing answer:

```text
1. State why hash map/set is useful.
2. Define key and value/state.
3. Explain brute force.
4. Write clean Python.
5. Dry run map state.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 89. Quick Reference Cards

### Quick Card 1: dict

Summary:

```text
Use for key → value mapping.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 2: set

Summary:

```text
Use for membership/uniqueness only.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 3: Counter

Summary:

```text
Use for frequency counts.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 4: defaultdict(list)

Summary:

```text
Use for grouping records/items by key.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 5: defaultdict(int/float)

Summary:

```text
Use for running counts or sums.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 6: Complement lookup

Summary:

```text
Check target-current before storing current.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 7: First occurrence

Summary:

```text
Do not overwrite existing index.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 8: Latest occurrence

Summary:

```text
Overwrite or compare timestamp intentionally.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 9: Prefix sum map

Summary:

```text
Store prefix_sum → count or first index.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 10: Sliding window map

Summary:

```text
Update counts when expanding and shrinking.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 11: Zero counts

Summary:

```text
Delete zero-count keys when distinct count matters.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 12: Top K

Summary:

```text
Count first, then sort/heap/bucket.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 13: In-memory join

Summary:

```text
Build lookup from smaller dataset.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 14: CDC state

Summary:

```text
Use ID → current record and handle DELETE.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 15: Bijection

Summary:

```text
Use two maps to enforce one-to-one mapping.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```
