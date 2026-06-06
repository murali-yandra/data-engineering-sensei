# Arrays and Strings Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/dsa/arrays-strings.md
```

This guide teaches and drills **arrays and strings for Data Engineering interviews**.

This is not a generic LeetCode dump. It is an interview-focused pattern guide for candidates preparing for Data Engineering roles where coding rounds test practical problem solving, clean implementation, edge cases, and communication.

Arrays and strings are high-ROI because they appear in:

- coding interviews
- Python data-processing tasks
- log parsing
- event stream processing
- duplicate detection
- deduplication
- frequency counting
- grouping
- top K preparation
- time-window logic
- validation
- parsing API records
- cleaning strings
- comparing datasets
- building pipeline utilities

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
- `progress/CANDIDATE_PROFILE.md`
- `progress/CURRENT_STATE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Default interview standard if target companies are not provided:

```text
FAANG-style Data Engineering coding standard, scaled by candidate experience.
```


## 1. Purpose

The purpose of this guide is to train the candidate to solve array and string questions using reusable patterns.

The candidate should learn to identify:

```text
When to use hash map.
When to use set.
When to sort.
When to use two pointers.
When to use sliding window.
When to use prefix sum.
When to scan once.
When to use in-place modification.
When to use stack-like string processing.
When to use frequency arrays.
When brute force is too slow.
```

A candidate is not interview-ready just because they memorized solutions.

A candidate is interview-ready when they can:

```text
understand the problem
ask clarifying questions
identify the pattern
explain brute force
optimize
write clean code
handle edge cases
explain complexity
connect the pattern to Data Engineering scenarios
handle follow-up variations
```


## 2. Why Arrays and Strings Matter for Data Engineers

Arrays and strings show up in Data Engineering interviews because they test foundational coding ability.

Real Data Engineering connections:

```text
Arrays/lists → records, events, files, batches, transactions.
Strings → logs, IDs, timestamps, CSV lines, API fields, merchant names.
Hash maps → grouping, counting, joining small lookup data.
Sets → deduplication and membership checks.
Sliding windows → rolling metrics, session windows, bounded event windows.
Prefix sums → cumulative metrics and fast range calculations.
Two pointers → sorted comparisons, merge-like data reconciliation.
Sorting → grouping, ordering, interval preparation, dedupe preparation.
String parsing → log processing and data cleaning.
```

Example interview translation:

```text
LeetCode: Longest Substring Without Repeating Characters.
Data Engineering: Find longest event sequence without duplicate event types in a session.
```

Example interview translation:

```text
LeetCode: Two Sum.
Data Engineering: Find two transactions that reconcile to a target adjustment.
```

Example interview translation:

```text
LeetCode: Valid Anagram.
Data Engineering: Compare normalized merchant names or signature strings.
```


## 3. Core Interview Rule

Before solving any array/string problem, the candidate must say:

```text
1. What is the input?
2. What is the output?
3. What constraints matter?
4. Can input contain empty values?
5. Can values repeat?
6. Is order important?
7. Do we need contiguous subarray/substring?
8. Do we need exact indices or values?
9. Can we modify input?
10. What time and space complexity is expected?
```

Then say:

```text
The brute force approach is...
The optimized pattern is...
The reason this pattern fits is...
```

Do not start coding silently.

Strict rule:

```text
No code before pattern and approach.
```


## 4. Standard Answer Framework

Use this framework in every coding answer:

```text
1. Restate the problem.
2. Clarify edge cases.
3. Give brute force.
4. Identify optimized pattern.
5. Explain the invariant/state.
6. Write code.
7. Dry run small example.
8. Explain edge cases.
9. Explain time complexity.
10. Explain space complexity.
11. Handle follow-up.
```

Short coding-round version:

```text
Problem:
Pattern:
Approach:
Code:
Complexity:
Edge cases:
```

Example:

```text
Pattern: sliding window with set.
Approach: expand right pointer, shrink left pointer while duplicate exists, track max length.
Time: O(n).
Space: O(k), where k is number of unique characters in the window.
```


## 5. Scoring Rubric

Score each array/string attempt from 0 to 5.

### Score 0

No meaningful attempt.

### Score 1

Very weak. Does not understand problem or writes unrelated code.

### Score 2

Brute force or partial solution only. Major edge cases fail.

### Score 3

Correct for common cases but weak explanation, edge cases, or complexity.

### Score 4

Interview-ready. Correct, clear, efficient, handles edge cases, explains complexity.

### Score 5

Strong. Clean solution, strong communication, handles follow-ups and variations.

Do not give 4+ if:

```text
candidate cannot explain why pattern fits
code works only for sample
time complexity is wrong
edge cases are ignored
solution is O(n²) when O(n) is expected
candidate uses list membership repeatedly when set/dict is needed
candidate cannot dry run their own code
```


## 6. Pattern Map

Arrays and strings patterns:

```text
1. Hash map / frequency counting
2. Set membership
3. Sorting
4. Two pointers
5. Fixed-size sliding window
6. Variable-size sliding window
7. Prefix sum
8. Kadane's algorithm
9. In-place array modification
10. Reverse/string builder
11. Palindrome checks
12. Character frequency array
13. Stack-like string processing
14. Matrix/grid basics
15. Merge sorted arrays
16. Difference arrays/basic range updates
17. Run-length/group scanning
18. Normalization/parsing
```

Pattern selection question:

```text
What do I need to remember while scanning?
```

Mapping:

```text
Need counts → hash map / Counter / frequency array.
Need membership → set.
Need sorted relationship → sort + two pointers.
Need contiguous subarray/substring → sliding window or prefix sum.
Need cumulative/range sum → prefix sum.
Need maximum contiguous sum → Kadane.
Need remove/overwrite in-place → two pointers.
Need compare characters → frequency array/hash map.
Need undo last char/operator → stack.
Need clean/normalize string → parsing and builder.
```


## 7. Data Engineering Pattern Translation

Use this translation table.

| DSA Pattern | Data Engineering Scenario |
|---|---|
| Hash map count | Count events by type |
| Set membership | Deduplicate event IDs |
| Two pointers | Compare two sorted ID lists |
| Sliding window | Rolling event window |
| Prefix sum | Cumulative metrics |
| Sorting | Sort records before grouping/ranking |
| In-place overwrite | Clean array of records |
| Frequency array | Character validation or fixed alphabet counts |
| String parsing | Parse logs or CSV-like lines |
| Stack | Validate nested expressions or path simplification |
| Kadane | Maximum anomaly window or max gain period |
| Merge sorted arrays | Merge sorted source and target IDs |
| Run-length scan | Compress repeated statuses/events |


## 8. Common Mistakes

Common mistakes in array/string interviews:

```text
Jumping to code without pattern.
Using nested loops when hash map works.
Using list membership inside loop.
Forgetting empty input.
Forgetting duplicates.
Forgetting negative numbers.
Using sliding window when numbers can be negative and invariant breaks.
Not shrinking variable window correctly.
Confusing subsequence and substring.
Confusing subarray and subset.
Sorting when indices must be preserved.
Losing original indices after sort.
Returning values when indices are required.
Using set when frequency is needed.
Using set when latest record/value is needed.
Off-by-one errors.
Wrong loop boundaries.
Incorrect space complexity.
No dry run.
No follow-up readiness.
```

Strict feedback example:

```text
This is not interview-ready. You solved the sample, but your approach is O(n²), and the problem has a clear hash map pattern.
```


## 9. Complexity Expectations

Candidate must know common complexity.

```text
Single scan: O(n)
Nested loop over array: O(n²)
Sorting: O(n log n)
Hash map lookup average: O(1)
Set lookup average: O(1)
Sliding window: O(n) when each pointer moves at most n times
Prefix sum build: O(n)
Range query after prefix: O(1)
String concatenation repeatedly in loop: can be inefficient in some languages
Building list and join for string: usually safer
```

Interview wording:

```text
Time complexity is O(n) because each element is processed once.
Space complexity is O(k), where k is the number of unique values stored in the map.
```

Do not say:

```text
Time is O(1)
```

when scanning input.


## 10. Edge Case Checklist

For arrays:

```text
empty array
one element
two elements
duplicates
all same values
negative numbers
zero values
large numbers
already sorted
reverse sorted
target not found
multiple valid answers
index vs value return
input modification allowed or not
```

For strings:

```text
empty string
single character
spaces
case sensitivity
punctuation
unicode vs ASCII
all same characters
all unique characters
palindrome with symbols
normalization rules
long string
```

For Data Engineering-flavored problems:

```text
missing ID
duplicate ID
None/null fields
bad timestamp
case-insensitive IDs
whitespace in merchant names
invalid log line
out-of-order records
late record
multiple records with same key
```


## 11. Pattern: Hash Map / Frequency Counting

### When to use

Use hash map when the problem needs:

```text
fast lookup
counts
grouping
mapping value to index
complement lookup
frequency comparison
remember previous values
avoid nested loop
```

Trigger words:

```text
count
frequency
duplicates
anagram
pair sum
group
first occurrence
last occurrence
seen before
```

### Mental model

```text
Scan once.
Store useful information in a dictionary.
Use it later in O(1) average time.
```

### Common Data Engineering uses

```text
count events by status
sum transaction amount by account
detect duplicate file names
map merchant_id to normalized merchant
track latest record per ID
join small lookup records in memory
```

### Interview line

```text
I use a hash map because I need fast lookup while scanning the array once.
```

### Mistakes

```text
using list for membership
using set when count is needed
forgetting to update count
forgetting duplicate handling
```


## 12. Problem: Two Sum

LeetCode:

```text
1. Two Sum
Difficulty: Easy
Pattern: Hash map
```

Problem:

```text
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
```

Approach:

```text
Scan nums.
For each number x, compute complement = target - x.
If complement was seen before, return previous index and current index.
Otherwise store x with current index.
```

Why hash map:

```text
We need fast lookup for complement.
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
duplicate values
negative numbers
no answer
same value cannot reuse same index unless appears twice
```

Data Engineering connection:

```text
Find two adjustment transactions that reconcile to a target difference.
```

Follow-ups:

```text
What if there are multiple valid answers?
What if input is sorted?
What if you need all pairs?
```


## 13. Problem: Contains Duplicate

LeetCode:

```text
217. Contains Duplicate
Difficulty: Easy
Pattern: Set membership
```

Approach:

```text
Use a set to track seen values.
If value already exists, duplicate is found.
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

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Detect duplicate event IDs, file names, transaction IDs, or primary keys.
```

Common mistake:

```text
Using a list for seen values causes O(n²) lookup.
```

Follow-up:

```text
How would you return duplicate values instead of True/False?
```


## 14. Problem: Valid Anagram

LeetCode:

```text
242. Valid Anagram
Difficulty: Easy
Pattern: Frequency counting
```

Approach:

```text
Two strings are anagrams if character counts match.
```

Code:

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
Space: O(k), where k is unique characters
```

Data Engineering connection:

```text
Compare normalized signature strings or detect same character composition after cleaning.
```

Follow-ups:

```text
What if uppercase/lowercase should be treated same?
What if spaces/punctuation should be ignored?
What if only lowercase English letters exist?
```


## 15. Problem: Group Anagrams

LeetCode:

```text
49. Group Anagrams
Difficulty: Medium
Pattern: Hash map grouping
```

Approach 1:

```text
Sort each word and use sorted word as key.
```

Code:

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
```

Complexity:

```text
Time: O(n * k log k), where k is average word length
Space: O(n * k)
```

Approach 2 for lowercase letters:

```text
Use 26-length frequency tuple as key.
```

Code:

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        counts = [0] * 26

        for char in word:
            counts[ord(char) - ord('a')] += 1

        groups[tuple(counts)].append(word)

    return list(groups.values())
```

Data Engineering connection:

```text
Group normalized merchant aliases or similar signature strings.
```

Follow-ups:

```text
What if Unicode characters exist?
What if case-insensitive grouping is needed?
What if order of groups matters?
```


## 16. Problem: First Unique Character in a String

LeetCode:

```text
387. First Unique Character in a String
Difficulty: Easy
Pattern: Frequency counting
```

Approach:

```text
Count characters.
Scan again and return first index with count 1.
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
Find first unique status/event marker in a sequence.
```

Common mistake:

```text
Returning character instead of index.
```


## 17. Problem: Majority Element

LeetCode:

```text
169. Majority Element
Difficulty: Easy
Pattern: Frequency counting / Boyer-Moore
```

Hash map approach:

```python
def majority_element(nums):
    threshold = len(nums) // 2
    counts = {}

    for value in nums:
        counts[value] = counts.get(value, 0) + 1

        if counts[value] > threshold:
            return value

    return None
```

Boyer-Moore approach:

```python
def majority_element(nums):
    candidate = None
    count = 0

    for value in nums:
        if count == 0:
            candidate = value

        count += 1 if value == candidate else -1

    return candidate
```

Complexity:

```text
Hash map: O(n) time, O(n) space
Boyer-Moore: O(n) time, O(1) space
```

Data Engineering connection:

```text
Find dominant category/status in a batch when majority is guaranteed.
```

Follow-up:

```text
What if majority is not guaranteed?
```


## 18. Pattern: Set Membership

### When to use

Use set when:

```text
only membership matters
need uniqueness
need fast existence check
need difference/intersection
```

Examples:

```text
contains duplicate
missing IDs
intersection of two lists
detect repeated event_id
find records not processed
```

### Data Engineering examples

```text
processed_files set
valid_statuses set
known_customer_ids set
seen_event_ids set
```

### Interview line

```text
A set is enough because I only need to know whether the value has appeared.
```

### Common mistake

```text
Using set when you need count, latest value, or associated metadata.
```


## 19. Problem: Intersection of Two Arrays

LeetCode:

```text
349. Intersection of Two Arrays
Difficulty: Easy
Pattern: Set
```

Approach:

```text
Convert one array to set.
Scan the other and collect values that exist in the set.
```

Code:

```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for value in nums2:
        if value in set1:
            result.add(value)

    return list(result)
```

Simpler:

```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```

Complexity:

```text
Time: O(n + m)
Space: O(n + m)
```

Data Engineering connection:

```text
Find IDs present in both source and target datasets.
```

Follow-up:

```text
What if duplicates should be preserved?
```


## 20. Problem: Intersection of Two Arrays II

LeetCode:

```text
350. Intersection of Two Arrays II
Difficulty: Easy
Pattern: Frequency counting
```

Key difference:

```text
Duplicates should be preserved according to minimum count.
```

Code:

```python
from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)
    result = []

    for value in nums2:
        if counts[value] > 0:
            result.append(value)
            counts[value] -= 1

    return result
```

Complexity:

```text
Time: O(n + m)
Space: O(min(n, m)) if counting smaller array
```

Data Engineering connection:

```text
Compare duplicated IDs or repeated events across two batches.
```

Common mistake:

```text
Using set intersection loses duplicate counts.
```


## 21. Pattern: Sorting

### When to use

Sorting helps when:

```text
order matters
need compare neighbors
need two pointers
need group equal values
need merge intervals
need top values if no heap needed
```

Trigger words:

```text
closest
smallest/largest
merge
overlap
compare pairs
same group
rank
```

### Complexity

```text
Sorting is usually O(n log n)
```

### Data Engineering uses

```text
sort records by timestamp
sort IDs before reconciliation
sort intervals before merging backfill windows
sort events before sessionization
sort values for percentile-like logic
```

### Mistake

```text
Sorting can lose original indices if not preserved.
```

If indices matter:

```text
sort pairs of (value, index)
```


## 22. Pattern: Two Pointers

### When to use

Use two pointers when:

```text
array/string is sorted
need pair from both ends
need compare left and right
need in-place compaction
need merge sorted arrays
need palindrome check
```

Trigger words:

```text
sorted array
pair sum
remove duplicates
reverse
palindrome
merge
```

### Mental model

```text
left pointer starts at beginning.
right pointer starts at end or another position.
Move pointer based on condition.
```

### Interview line

```text
Because the array is sorted, I can use two pointers and move left/right based on whether the sum is too small or too large.
```

### Common mistake

```text
Using two pointers on unsorted data without sorting or justification.
```


## 23. Problem: Two Sum II - Input Array Is Sorted

LeetCode:

```text
167. Two Sum II - Input Array Is Sorted
Difficulty: Medium
Pattern: Two pointers
```

Approach:

```text
Because array is sorted, use left and right pointers.
If sum is target, return.
If sum is too small, move left.
If sum is too large, move right.
```

Code:

```python
def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return []
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Find two sorted adjustment values that reconcile to target.
```

Follow-up:

```text
Why not use hash map?
```

Answer:

```text
Hash map works but uses O(n) space. Sorted input allows O(1) extra space.
```


## 24. Problem: Valid Palindrome

LeetCode:

```text
125. Valid Palindrome
Difficulty: Easy
Pattern: Two pointers / string normalization
```

Approach:

```text
Use left and right pointers.
Skip non-alphanumeric characters.
Compare lowercase characters.
```

Code:

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Normalize and compare identifiers or cleaned string fields.
```

Common mistakes:

```text
not skipping punctuation
case sensitivity
creating extra cleaned string when O(1) is requested
```


## 25. Problem: Reverse String

LeetCode:

```text
344. Reverse String
Difficulty: Easy
Pattern: Two pointers / in-place
```

Approach:

```text
Swap left and right until pointers meet.
```

Code:

```python
def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Interview point:

```text
The input is a list of characters, so modify in-place.
```

Follow-up:

```text
What if input is immutable string?
```


## 26. Problem: 3Sum

LeetCode:

```text
15. 3Sum
Difficulty: Medium
Pattern: Sorting + two pointers
```

Approach:

```text
Sort nums.
Fix one number.
Use two pointers to find pairs summing to negative fixed number.
Skip duplicates.
```

Code:

```python
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
```

Complexity:

```text
Time: O(n²)
Space: O(1) or O(n) depending sort implementation, excluding output
```

Data Engineering connection:

```text
Find triplets of adjustments that net to zero during reconciliation.
```

Common mistakes:

```text
not skipping duplicates
using same index twice
wrong pointer movement
```


## 27. Problem: Remove Duplicates from Sorted Array

LeetCode:

```text
26. Remove Duplicates from Sorted Array
Difficulty: Easy
Pattern: Two pointers / in-place overwrite
```

Approach:

```text
Since sorted, duplicates are adjacent.
Use write pointer to place next unique value.
```

Code:

```python
def remove_duplicates(nums):
    if not nums:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Compact sorted IDs or dedupe sorted records in-place.
```

Common mistake:

```text
Returning new array when problem asks in-place length.
```


## 28. Problem: Remove Element

LeetCode:

```text
27. Remove Element
Difficulty: Easy
Pattern: Two pointers / in-place overwrite
```

Approach:

```text
Use write pointer.
Copy values that are not equal to val.
```

Code:

```python
def remove_element(nums, val):
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1

    return write
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Filter invalid values in a mutable list-like batch.
```

Follow-up:

```text
What if order does not matter?
```


## 29. Problem: Move Zeroes

LeetCode:

```text
283. Move Zeroes
Difficulty: Easy
Pattern: Two pointers / stable overwrite
```

Approach:

```text
Move all non-zero values to front using write pointer.
Fill remaining with zero.
```

Code:

```python
def move_zeroes(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    for index in range(write, len(nums)):
        nums[index] = 0
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Move valid records forward and placeholders/null-equivalent values to end.
```

Common mistake:

```text
using repeated remove/append, causing inefficient behavior
```


## 30. Pattern: Sliding Window

Sliding window is used for contiguous subarrays or substrings.

There are two main types:

### Fixed-size window

Use when:

```text
window size k is given
```

Examples:

```text
maximum average subarray of size k
count events in every fixed window
```

### Variable-size window

Use when:

```text
need longest/shortest contiguous segment satisfying a condition
```

Examples:

```text
longest substring without repeating characters
minimum size subarray sum
longest substring with at most k distinct characters
```

Strict trigger:

```text
The problem must involve contiguous subarray/substring.
```

Common mistake:

```text
Using sliding window for non-contiguous subsequence/subset problems.
```


## 31. Sliding Window Mental Model

A sliding window keeps a left and right boundary.

```text
right expands the window
left shrinks the window
state tracks what is inside the window
```

General variable window skeleton:

```python
left = 0
state = {}

for right in range(len(items)):
    add items[right] to state

    while window is invalid:
        remove items[left] from state
        left += 1

    update answer
```

Key question:

```text
What condition makes the window invalid?
```

For longest substring without duplicate:

```text
invalid = current character already exists in window
```

For at most K distinct:

```text
invalid = distinct_count > k
```

For sum at least target with positive numbers:

```text
valid = current_sum >= target
```


## 32. Problem: Longest Substring Without Repeating Characters

LeetCode:

```text
3. Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Variable sliding window + set/map
```

Approach:

```text
Maintain a window with no duplicate characters.
Expand right.
If duplicate appears, shrink left until duplicate removed.
Track max length.
```

Code with set:

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

Optimized code with last seen index:

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

Common mistakes:

```text
moving left backward
not removing correctly from set
confusing substring with subsequence
```


## 33. Problem: Maximum Average Subarray I

LeetCode:

```text
643. Maximum Average Subarray I
Difficulty: Easy
Pattern: Fixed-size sliding window
```

Approach:

```text
Compute sum of first k.
Slide window by adding new element and removing old.
Track max sum.
```

Code:

```python
def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    best_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        best_sum = max(best_sum, window_sum)

    return best_sum / k
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Maximum average metric over fixed-size rolling windows.
```

Common mistakes:

```text
recomputing sum for every window O(nk)
off-by-one when removing nums[right-k]
```


## 34. Problem: Minimum Size Subarray Sum

LeetCode:

```text
209. Minimum Size Subarray Sum
Difficulty: Medium
Pattern: Variable sliding window for positive numbers
```

Important condition:

```text
This sliding window works because all numbers are positive.
```

Approach:

```text
Expand right and increase sum.
While sum >= target, update answer and shrink left.
```

Code:

```python
def min_sub_array_len(target, nums):
    left = 0
    current_sum = 0
    best = float("inf")

    for right, value in enumerate(nums):
        current_sum += value

        while current_sum >= target:
            best = min(best, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if best == float("inf") else best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Smallest consecutive event window whose total amount crosses threshold.
```

Follow-up:

```text
What if numbers can be negative?
```

Answer:

```text
This simple sliding window no longer works reliably; prefix sum/monotonic queue may be needed depending problem.
```


## 35. Problem: Permutation in String

LeetCode:

```text
567. Permutation in String
Difficulty: Medium
Pattern: Fixed-size sliding window + frequency count
```

Problem:

```text
Check if s2 contains any permutation of s1.
```

Approach:

```text
Window size is len(s1).
Compare character counts between s1 and current window in s2.
```

Code:

```python
from collections import Counter

def check_inclusion(s1, s2):
    window_size = len(s1)

    if window_size > len(s2):
        return False

    target = Counter(s1)
    window = Counter(s2[:window_size])

    if window == target:
        return True

    for right in range(window_size, len(s2)):
        entering = s2[right]
        leaving = s2[right - window_size]

        window[entering] += 1
        window[leaving] -= 1

        if window[leaving] == 0:
            del window[leaving]

        if window == target:
            return True

    return False
```

Complexity:

```text
Time: O(n * k) if Counter comparison considers k unique chars; O(n) for fixed alphabet
Space: O(k)
```

Data Engineering connection:

```text
Detect whether a fixed-size sequence contains same event composition as a target signature.
```

Common mistake:

```text
not deleting zero-count keys, causing Counter/dict comparison issues in manual implementation
```


## 36. Problem: Find All Anagrams in a String

LeetCode:

```text
438. Find All Anagrams in a String
Difficulty: Medium
Pattern: Fixed-size sliding window + frequency count
```

Approach:

```text
Use window of length len(p).
Track character counts.
When window count equals target count, record left index.
```

Code:

```python
from collections import Counter

def find_anagrams(s, p):
    k = len(p)

    if k > len(s):
        return []

    target = Counter(p)
    window = Counter(s[:k])
    result = []

    if window == target:
        result.append(0)

    for right in range(k, len(s)):
        entering = s[right]
        leaving = s[right - k]

        window[entering] += 1
        window[leaving] -= 1

        if window[leaving] == 0:
            del window[leaving]

        if window == target:
            result.append(right - k + 1)

    return result
```

Complexity:

```text
Time: O(n) for fixed alphabet, otherwise O(n * unique_chars comparison)
Space: O(k)
```

Data Engineering connection:

```text
Find positions where a sequence contains the same multiset of event codes.
```


## 37. Problem: Longest Repeating Character Replacement

LeetCode:

```text
424. Longest Repeating Character Replacement
Difficulty: Medium
Pattern: Variable sliding window + frequency
```

Core idea:

```text
Window is valid if window_length - max_frequency <= k.
```

Why:

```text
Characters not equal to the most frequent char can be replaced.
```

Code:

```python
from collections import defaultdict

def character_replacement(s, k):
    counts = defaultdict(int)
    left = 0
    max_count = 0
    best = 0

    for right, char in enumerate(s):
        counts[char] += 1
        max_count = max(max_count, counts[char])

        while (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(k), where k is unique chars
```

Data Engineering connection:

```text
Find longest period where at most k status corrections make all statuses consistent.
```

Common confusion:

```text
max_count may be stale, but the algorithm still works for finding max length.
```


## 38. Pattern: Prefix Sum

Prefix sum is used for cumulative totals and range calculations.

### When to use

```text
subarray sum
range sum
cumulative metrics
difference between positions
count subarrays with target sum
```

### Mental model

```text
prefix[i] = sum of elements before index i
sum from l to r = prefix[r + 1] - prefix[l]
```

### Data Engineering uses

```text
cumulative revenue
range-based metric checks
running counts
subarray anomaly detection
```

### Interview line

```text
Prefix sum lets me convert repeated range sum calculations into O(1) lookups after O(n) preprocessing.
```

### Important

For subarray sum equals k with negative numbers:

```text
Use prefix sum + hash map, not sliding window.
```


## 39. Problem: Range Sum Query - Immutable

LeetCode:

```text
303. Range Sum Query - Immutable
Difficulty: Easy
Pattern: Prefix sum
```

Approach:

```text
Precompute prefix sums.
sumRange(left, right) = prefix[right + 1] - prefix[left]
```

Code:

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]

        for value in nums:
            self.prefix.append(self.prefix[-1] + value)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

Complexity:

```text
Build: O(n)
Query: O(1)
Space: O(n)
```

Data Engineering connection:

```text
Precompute cumulative metrics for fast range queries.
```


## 40. Problem: Subarray Sum Equals K

LeetCode:

```text
560. Subarray Sum Equals K
Difficulty: Medium
Pattern: Prefix sum + hash map
```

Why not sliding window:

```text
Numbers can be negative, so sliding window cannot reliably shrink/grow based on sum.
```

Approach:

```text
Maintain running prefix sum.
If current_sum - k existed before, then a subarray ending here sums to k.
Store counts of prefix sums.
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
        result += prefix_counts[current_sum - k]
        prefix_counts[current_sum] += 1

    return result
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Count consecutive transaction windows that sum to a target adjustment.
```

Common mistakes:

```text
forgetting prefix_counts[0] = 1
using sliding window with negative numbers
storing only seen prefix sums as set instead of counts
```


## 41. Problem: Product of Array Except Self

LeetCode:

```text
238. Product of Array Except Self
Difficulty: Medium
Pattern: Prefix/suffix accumulation
```

Constraint:

```text
Do not use division.
```

Approach:

```text
result[i] = product of all values before i * product of all values after i.
```

Code:

```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
```

Complexity:

```text
Time: O(n)
Space: O(1) extra excluding output
```

Data Engineering connection:

```text
Compute per-record metric using all other records without recalculating full product each time.
```

Common mistakes:

```text
using division despite constraint
failing zeros
claiming output array counts as extra space when problem excludes it
```


## 42. Pattern: Kadane's Algorithm

Kadane's algorithm finds maximum sum contiguous subarray.

### When to use

```text
maximum subarray
best contiguous gain/loss period
maximum streak score
```

### Mental model

At each index:

```text
Either start new subarray here,
or extend previous subarray.
```

State:

```text
current_best_ending_here
global_best
```

Interview line:

```text
If the current running sum becomes worse than starting fresh at this element, I start a new subarray.
```


## 43. Problem: Maximum Subarray

LeetCode:

```text
53. Maximum Subarray
Difficulty: Medium
Pattern: Kadane
```

Code:

```python
def max_sub_array(nums):
    current = nums[0]
    best = nums[0]

    for value in nums[1:]:
        current = max(value, current + value)
        best = max(best, current)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Find max contiguous period of positive revenue change or anomaly score.
```

Edge cases:

```text
all negative numbers
one element
zeros
```

Common mistake:

```text
initializing best to 0 fails for all-negative input.
```


## 44. Pattern: String Building and Parsing

String problems often test careful scanning.

### When to use

```text
log parsing
cleaning text
normalizing strings
removing spaces
reversing words
parsing tokens
```

Rules:

```text
Use list builder then ''.join(list) when repeatedly constructing strings.
Be clear about whitespace handling.
Ask about case sensitivity and punctuation.
Avoid repeated expensive concatenation in tight loops when language makes it costly.
```

Data Engineering examples:

```text
parse log line
normalize merchant name
clean CSV-like field
extract domain from email
validate identifier format
```


## 45. Problem: Reverse Words in a String

LeetCode:

```text
151. Reverse Words in a String
Difficulty: Medium
Pattern: String parsing
```

Approach in Python:

```text
split handles extra spaces.
reverse words.
join with single spaces.
```

Code:

```python
def reverse_words(s):
    words = s.split()
    return " ".join(reversed(words))
```

Manual approach may be expected in some interviews.

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Normalize whitespace-delimited fields.
```

Follow-ups:

```text
What if you cannot use split?
What if string must be modified in-place as char array?
```


## 46. Problem: String Compression

LeetCode:

```text
443. String Compression
Difficulty: Medium
Pattern: Run-length scan + in-place write
```

Approach:

```text
Scan groups of same character.
Write character and count digits in-place.
Return write length.
```

Code:

```python
def compress(chars):
    write = 0
    read = 0

    while read < len(chars):
        char = chars[read]
        start = read

        while read < len(chars) and chars[read] == char:
            read += 1

        count = read - start
        chars[write] = char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write
```

Complexity:

```text
Time: O(n)
Space: O(1) extra
```

Data Engineering connection:

```text
Run-length compress repeated statuses or event codes.
```

Common mistakes:

```text
not writing multi-digit counts correctly
returning compressed string instead of length
```


## 47. Problem: Valid Parentheses

LeetCode:

```text
20. Valid Parentheses
Difficulty: Easy
Pattern: Stack / string processing
```

Approach:

```text
Push opening brackets.
For closing bracket, top of stack must match.
```

Code:

```python
def is_valid(s):
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Validate nested expressions, JSON-like structures, or simple formula syntax.
```

Common mistakes:

```text
not checking empty stack before pop
not checking leftover opening brackets
```


## 48. Problem: Backspace String Compare

LeetCode:

```text
844. Backspace String Compare
Difficulty: Easy
Pattern: Stack or two pointers
```

Stack approach:

```python
def backspace_compare(s, t):
    def build(text):
        stack = []

        for char in text:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return stack

    return build(s) == build(t)
```

Complexity:

```text
Time: O(n + m)
Space: O(n + m)
```

Two-pointer follow-up:

```text
Can you do O(1) extra space?
```

Data Engineering connection:

```text
Process stream of edit operations or correction markers.
```


## 49. Pattern: Matrix/Grid Basics

Some array questions use 2D arrays.

Core skills:

```text
iterate rows and columns
check boundaries
use visited set/matrix
move in four directions
transpose/rotate
spiral traversal
```

Data Engineering connection:

```text
matrix-like batches
grid-based data
table transformations
pivot-like thinking
```

Common mistakes:

```text
row/column confusion
off-by-one boundaries
modifying input when not allowed
not marking visited
```


## 50. Problem: Rotate Image

LeetCode:

```text
48. Rotate Image
Difficulty: Medium
Pattern: Matrix in-place transformation
```

Approach:

```text
Transpose matrix.
Reverse each row.
```

Code:

```python
def rotate(matrix):
    n = len(matrix)

    for row in range(n):
        for col in range(row + 1, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()
```

Complexity:

```text
Time: O(n²)
Space: O(1)
```

Data Engineering connection:

```text
Matrix transformation reasoning; less common for DE but useful for coding fundamentals.
```


## 51. Problem: Spiral Matrix

LeetCode:

```text
54. Spiral Matrix
Difficulty: Medium
Pattern: Matrix boundaries
```

Approach:

```text
Maintain top, bottom, left, right boundaries.
Traverse right, down, left, up.
Shrink boundaries.
```

Code:

```python
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

Complexity:

```text
Time: O(mn)
Space: O(1) extra excluding output
```

Common mistakes:

```text
not checking boundaries before reverse traversals
row/column confusion
```


## 52. Data Engineering Custom Problem: Deduplicate Event IDs

Problem:

```text
Given a list of event dictionaries, return valid events with duplicate event_id removed.
Keep first occurrence.
Return invalid_count for records missing event_id.
```

Example record:

```python
{"event_id": "e1", "user_id": "u1", "event_type": "click"}
```

Pattern:

```text
set membership
```

Code:

```python
def dedupe_events(events):
    seen = set()
    result = []
    invalid_count = 0

    for event in events:
        event_id = event.get("event_id")

        if event_id is None:
            invalid_count += 1
            continue

        if event_id in seen:
            continue

        seen.add(event_id)
        result.append(event)

    return result, invalid_count
```

Complexity:

```text
Time: O(n)
Space: O(u), where u is unique event IDs
```

Follow-up:

```text
What if requirement changes to keep latest event by event_time?
```

Expected:

```text
Use dictionary keyed by event_id and compare timestamps.
```


## 53. Data Engineering Custom Problem: Count Events by Type

Problem:

```text
Given events, return count by event_type.
Skip invalid records missing event_type and return invalid_count.
```

Pattern:

```text
hash map counting
```

Code:

```python
def count_events_by_type(events):
    counts = {}
    invalid_count = 0

    for event in events:
        event_type = event.get("event_type")

        if not event_type:
            invalid_count += 1
            continue

        counts[event_type] = counts.get(event_type, 0) + 1

    return counts, invalid_count
```

Complexity:

```text
Time: O(n)
Space: O(k), where k is number of event types
```

Follow-up:

```text
Return top 3 event types.
```

Expected:

```text
Sort counts or use heap depending scale.
```


## 54. Data Engineering Custom Problem: Latest Record Per ID

Problem:

```text
Given records with id and updated_at, keep latest record per id.
If updated_at ties, keep latest ingestion_time.
Return invalid records missing id or updated_at.
```

Pattern:

```text
hash map latest state
```

Code:

```python
def latest_records(records):
    latest_by_id = {}
    invalid = []

    for record in records:
        record_id = record.get("id")
        updated_at = record.get("updated_at")
        ingestion_time = record.get("ingestion_time")

        if record_id is None or updated_at is None:
            invalid.append({"record": record, "reason": "missing_id_or_updated_at"})
            continue

        if record_id not in latest_by_id:
            latest_by_id[record_id] = record
            continue

        current = latest_by_id[record_id]

        current_key = (
            current.get("updated_at"),
            current.get("ingestion_time"),
        )
        new_key = (
            updated_at,
            ingestion_time,
        )

        if new_key > current_key:
            latest_by_id[record_id] = record

    return list(latest_by_id.values()), invalid
```

Complexity:

```text
Time: O(n)
Space: O(u)
```

Interview point:

```text
A set is insufficient because we need to store and compare the current latest record.
```


## 55. Data Engineering Custom Problem: Missing Files

Problem:

```text
Given expected_files and processed_files, return expected files not processed.
```

Pattern:

```text
set difference
```

Code:

```python
def find_missing_files(expected_files, processed_files):
    processed = set(processed_files)
    missing = []

    for file_name in expected_files:
        if file_name not in processed:
            missing.append(file_name)

    return missing
```

Complexity:

```text
Time: O(n + m)
Space: O(m)
```

Follow-up:

```text
What if file names should be compared case-insensitively?
```

Expected:

```text
Normalize both sides before comparison.
```


## 56. Data Engineering Custom Problem: Normalize Merchant Names

Problem:

```text
Given merchant names, normalize by:
- trimming leading/trailing spaces
- converting to lowercase
- replacing multiple spaces with one space
- removing punctuation
Return normalized names.
```

Pattern:

```text
string parsing and normalization
```

Code:

```python
import string

def normalize_merchant_name(name):
    if name is None:
        return None

    punctuation = set(string.punctuation)
    cleaned_chars = []

    for char in name.strip().lower():
        if char not in punctuation:
            cleaned_chars.append(char)
        else:
            cleaned_chars.append(" ")

    normalized = " ".join("".join(cleaned_chars).split())
    return normalized
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Follow-ups:

```text
Should '&' become 'and'?
Should numbers be preserved?
How do you handle unicode characters?
How do you map aliases to canonical merchants?
```


## 57. Data Engineering Custom Problem: Parse Log Lines

Problem:

```text
Given log lines in the format:
timestamp service level message

Return count of ERROR logs by service.
Skip malformed lines and return invalid_count.
```

Example:

```text
2025-01-01T10:00:00Z payments ERROR timeout
```

Pattern:

```text
string parsing + hash map counting
```

Code:

```python
def count_errors_by_service(log_lines):
    counts = {}
    invalid_count = 0

    for line in log_lines:
        parts = line.split(maxsplit=3)

        if len(parts) < 4:
            invalid_count += 1
            continue

        timestamp, service, level, message = parts

        if level == "ERROR":
            counts[service] = counts.get(service, 0) + 1

    return counts, invalid_count
```

Complexity:

```text
Time: O(n * L), where L is average line length
Space: O(s), where s is number of services
```

Follow-up:

```text
Return top 3 services by ERROR count.
```


## 58. Data Engineering Custom Problem: Rolling Error Window

Problem:

```text
Given a list of numeric error counts per minute, find maximum total errors in any k-minute window.
```

Pattern:

```text
fixed-size sliding window
```

Code:

```python
def max_errors_in_window(error_counts, k):
    if k <= 0 or k > len(error_counts):
        return 0

    window_sum = sum(error_counts[:k])
    best = window_sum

    for right in range(k, len(error_counts)):
        window_sum += error_counts[right]
        window_sum -= error_counts[right - k]
        best = max(best, window_sum)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Follow-up:

```text
Return the window start index too.
```


## 59. Data Engineering Custom Problem: Longest Healthy Streak

Problem:

```text
Given a string of status codes where 'S' means success and 'F' means failure, find the longest window where at most k failures can be tolerated.
```

Pattern:

```text
variable sliding window
```

Code:

```python
def longest_healthy_streak(statuses, k):
    left = 0
    failures = 0
    best = 0

    for right, status in enumerate(statuses):
        if status == "F":
            failures += 1

        while failures > k:
            if statuses[left] == "F":
                failures -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Longest period with acceptable failure count.
```


## 60. Data Engineering Custom Problem: Source Target ID Reconciliation

Problem:

```text
Given source_ids and target_ids, return:
- ids missing in target
- extra ids in target
```

Pattern:

```text
set difference
```

Code:

```python
def reconcile_ids(source_ids, target_ids):
    source = set(source_ids)
    target = set(target_ids)

    missing_in_target = list(source - target)
    extra_in_target = list(target - source)

    return missing_in_target, extra_in_target
```

Complexity:

```text
Time: O(n + m)
Space: O(n + m)
```

Follow-up:

```text
What if duplicate IDs matter?
```

Expected:

```text
Use Counter instead of set.
```


## 61. Practice Ladder

Use this ladder for arrays and strings.

### Level 1: Foundation

```text
Contains Duplicate
Valid Anagram
Intersection of Two Arrays
Reverse String
Valid Palindrome
First Unique Character
```

### Level 2: Core interview patterns

```text
Two Sum
Two Sum II
Group Anagrams
Remove Duplicates from Sorted Array
Move Zeroes
Maximum Average Subarray I
```

### Level 3: Medium patterns

```text
Longest Substring Without Repeating Characters
Minimum Size Subarray Sum
Product of Array Except Self
Subarray Sum Equals K
3Sum
Find All Anagrams in a String
```

### Level 4: Strong interview readiness

```text
Longest Repeating Character Replacement
String Compression
Spiral Matrix
Rotate Image
Backspace String Compare
DE custom latest record / reconciliation / log parsing
```

Progression rule:

```text
Do not move to Level 3 until Level 1 and 2 can be solved with pattern explanation and complexity.
```


## 62. High-ROI LeetCode List

Practice these first.

| No. | Title | Difficulty | Pattern |
|---:|---|---|---|
| 1 | Two Sum | Easy | Hash map |
| 217 | Contains Duplicate | Easy | Set |
| 242 | Valid Anagram | Easy | Frequency |
| 49 | Group Anagrams | Medium | Hash map grouping |
| 125 | Valid Palindrome | Easy | Two pointers |
| 167 | Two Sum II - Input Array Is Sorted | Medium | Two pointers |
| 15 | 3Sum | Medium | Sort + two pointers |
| 26 | Remove Duplicates from Sorted Array | Easy | In-place two pointers |
| 27 | Remove Element | Easy | In-place two pointers |
| 283 | Move Zeroes | Easy | In-place two pointers |
| 3 | Longest Substring Without Repeating Characters | Medium | Sliding window |
| 643 | Maximum Average Subarray I | Easy | Fixed window |
| 209 | Minimum Size Subarray Sum | Medium | Variable window |
| 567 | Permutation in String | Medium | Window + frequency |
| 438 | Find All Anagrams in a String | Medium | Window + frequency |
| 424 | Longest Repeating Character Replacement | Medium | Window + frequency |
| 303 | Range Sum Query - Immutable | Easy | Prefix sum |
| 560 | Subarray Sum Equals K | Medium | Prefix sum + hash map |
| 238 | Product of Array Except Self | Medium | Prefix/suffix |
| 53 | Maximum Subarray | Medium | Kadane |
| 151 | Reverse Words in a String | Medium | String parsing |
| 443 | String Compression | Medium | Run-length + in-place |
| 20 | Valid Parentheses | Easy | Stack/string |
| 844 | Backspace String Compare | Easy | Stack/two pointers |
| 48 | Rotate Image | Medium | Matrix |
| 54 | Spiral Matrix | Medium | Matrix boundaries |


## 63. Pattern Classification Drill

Before solving, classify the pattern.

Questions:

```text
1. Find if an array contains duplicates.
2. Return indices of two numbers adding to target.
3. Group words that are anagrams.
4. Check if a string is palindrome ignoring punctuation.
5. Find longest substring without repeated characters.
6. Find maximum average of subarray of size k.
7. Count subarrays with sum k when negatives exist.
8. Remove duplicates from sorted array in-place.
9. Find top error service by count.
10. Find latest record per ID.
11. Compare source and target IDs.
12. Normalize merchant names.
13. Parse ERROR logs by service.
14. Find longest period with at most k failures.
15. Find product of array except self.
16. Find maximum contiguous sum.
17. Rotate square matrix.
18. Validate parentheses.
19. Compress repeated characters.
20. Find anagrams of p in s.
```

Expected pattern answers:

```text
1. Set
2. Hash map
3. Hash map grouping/frequency
4. Two pointers/string normalization
5. Variable sliding window
6. Fixed sliding window
7. Prefix sum + hash map
8. Two pointers/in-place
9. Hash map count
10. Hash map latest record
11. Set difference or Counter if duplicates matter
12. String parsing/normalization
13. String parsing + hash map counting
14. Variable sliding window
15. Prefix/suffix
16. Kadane
17. Matrix transpose + reverse
18. Stack
19. Run-length scan
20. Fixed sliding window + frequency
```

Passing standard:

```text
18/20 correct before moving to timed coding.
```


## 64. Timed Drill Protocol

Use this protocol for each timed problem.

```text
Minute 0-2:
Read problem, clarify input/output.

Minute 2-5:
Explain brute force and optimized pattern.

Minute 5-18:
Write code.

Minute 18-22:
Dry run with sample and edge case.

Minute 22-25:
Explain complexity and follow-up.
```

For easy problems:

```text
10-15 minutes
```

For medium problems:

```text
25-35 minutes
```

For hard variation:

```text
40-45 minutes
```

If candidate cannot identify pattern in 5 minutes:

```text
Stop and switch to pattern-mapper-mode.md or weakness-repair-mode.md.
```


## 65. Review Checklist

Review every solution with:

```text
1. Did candidate restate problem?
2. Did candidate identify pattern?
3. Was brute force explained?
4. Is optimized approach correct?
5. Is code syntactically clean?
6. Does code handle empty input?
7. Does code handle duplicates?
8. Does code handle edge cases?
9. Is time complexity correct?
10. Is space complexity correct?
11. Did candidate dry run?
12. Did candidate communicate clearly?
13. Did candidate handle follow-up?
14. Is there a Data Engineering connection?
```

Common review verdicts:

```text
Pattern correct, implementation weak.
Implementation correct, explanation weak.
Works for sample, fails edge cases.
Correct but not optimal.
Interview-ready.
Strong.
```


## 66. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Uses nested loops | Hash map/set classification drills |
| Cannot identify sliding window | Contiguous substring/subarray drills |
| Sliding window fails with negatives | Prefix sum vs window comparison |
| Forgets edge cases | Edge case checklist before code |
| Wrong complexity | Complexity explanation drills |
| Uses set when count needed | Dict/set/Counter classification |
| Cannot handle latest record | Latest-record cross-pattern repair |
| Off-by-one errors | Dry-run table and boundary drills |
| Cannot parse strings | Log parsing and normalization drills |
| Cannot explain | Communication structure drill |
| Memorizes solution | Variation drill with changed requirement |
```

If weakness repeats:

```text
Switch to weakness-repair-mode.md.
```


## 67. Arrays and Strings Mock Set 1: Easy

Use this mock for beginners.

Problems:

```text
1. Contains Duplicate
2. Valid Anagram
3. Valid Palindrome
4. Remove Element
5. Intersection of Two Arrays
```

Passing standard:

```text
4/5 average.
No O(n²) where O(n) is expected.
Correct edge cases.
```

Expected skills:

```text
set
hash map/frequency
two pointers
in-place write
string normalization
```


## 68. Arrays and Strings Mock Set 2: Core Medium

Use this mock for intermediate candidates.

Problems:

```text
1. Two Sum
2. Group Anagrams
3. Longest Substring Without Repeating Characters
4. Product of Array Except Self
5. Minimum Size Subarray Sum
```

Passing standard:

```text
4/5 average.
Candidate explains pattern before code.
Candidate explains complexity correctly.
```

Expected skills:

```text
hash map
grouping
sliding window
prefix/suffix
edge-case handling
```


## 69. Arrays and Strings Mock Set 3: Data Engineering Flavor

Use this mock for Data Engineering candidates.

Problems:

```text
1. Deduplicate event IDs, return invalid_count.
2. Count ERROR logs by service.
3. Keep latest record per ID.
4. Find missing source IDs in target.
5. Longest healthy streak with at most k failures.
```

Passing standard:

```text
4/5 average.
Candidate handles invalid records and explains DE relevance.
```

Expected skills:

```text
set
dict counting
dict latest-state
set difference
sliding window
```


## 70. Arrays and Strings Mock Set 4: Strong Candidate

Use this mock for strong candidates.

Problems:

```text
1. 3Sum
2. Subarray Sum Equals K
3. Find All Anagrams in a String
4. String Compression
5. Spiral Matrix
```

Passing standard:

```text
4/5 average.
Candidate handles duplicates, windows, prefix sums, in-place writes, and boundaries.
```

Expected skills:

```text
sort + two pointers
prefix sum + hash map
window + frequency
run-length scan
matrix boundaries
```


## 71. Daily Practice Plan: 7 Days

### Day 1: Hash map and set

Problems:

```text
Two Sum
Contains Duplicate
Valid Anagram
DE: Count events by type
```

### Day 2: Two pointers

Problems:

```text
Valid Palindrome
Two Sum II
Remove Duplicates from Sorted Array
Move Zeroes
```

### Day 3: Sliding window

Problems:

```text
Maximum Average Subarray I
Longest Substring Without Repeating Characters
Minimum Size Subarray Sum
DE: Longest healthy streak
```

### Day 4: Prefix and Kadane

Problems:

```text
Range Sum Query
Subarray Sum Equals K
Product of Array Except Self
Maximum Subarray
```

### Day 5: Strings

Problems:

```text
Reverse Words in a String
String Compression
Valid Parentheses
Backspace String Compare
DE: Normalize merchant names
```

### Day 6: Data Engineering custom

Problems:

```text
Deduplicate events
Latest record per ID
Missing files
Parse logs
Source-target ID reconciliation
```

### Day 7: Mock and repair

Tasks:

```text
Run Mock Set 2 or 3.
Review mistakes.
Repair weakest pattern.
Update progress.
```


## 72. 30-Day Arrays and Strings Plan

### Week 1: Foundation

Focus:

```text
hash map
set
frequency counting
two pointers
basic string normalization
```

Problems:

```text
Two Sum
Contains Duplicate
Valid Anagram
Intersection of Two Arrays
Valid Palindrome
Remove Element
Move Zeroes
```

Exit:

```text
Easy problems solved under 15 minutes with clean explanation.
```

### Week 2: Sliding window and prefix

Focus:

```text
fixed window
variable window
prefix sums
subarray logic
```

Problems:

```text
Maximum Average Subarray I
Longest Substring Without Repeating Characters
Minimum Size Subarray Sum
Permutation in String
Find All Anagrams
Subarray Sum Equals K
```

Exit:

```text
Candidate can explain window invariant and prefix map logic.
```

### Week 3: Medium array/string patterns

Focus:

```text
sorting + two pointers
prefix/suffix
Kadane
run-length
stack/string
```

Problems:

```text
3Sum
Product of Array Except Self
Maximum Subarray
String Compression
Valid Parentheses
Backspace String Compare
```

Exit:

```text
Candidate handles duplicates, edge cases, and complexity.
```

### Week 4: Data Engineering flavor and mocks

Focus:

```text
dedupe
log parsing
latest record
source-target reconciliation
rolling windows
mock interviews
```

Problems:

```text
DE custom problems
Mock Set 3
Mock Set 4
repair weakest pattern
```

Exit:

```text
Average mock score >= 4/5.
```


## 73. Progress Tracking Template

Update progress after practice.

```text
# Arrays and Strings Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Pattern | Difficulty | Score | Time | Mistake | Next Action

## Pattern Scores

Hash map:
Set:
Two pointers:
Sliding window:
Prefix sum:
Kadane:
String parsing:
Stack/string:
Matrix:

## Repeated Mistakes

-

## Repair Items

-

## Next Practice

Today:
This week:
Next mock:
```


## 74. Candidate Self-Review Questions

After every problem, candidate should answer:

```text
1. What pattern did I use?
2. Why did that pattern fit?
3. What was the brute force?
4. What made the optimized version better?
5. What edge case could break my code?
6. What is time complexity?
7. What is space complexity?
8. Could this appear in Data Engineering work?
9. What follow-up could interviewer ask?
10. Did I need hints?
```

If candidate cannot answer these:

```text
The problem is not fully learned.
```


## 75. Interview Communication Scripts

### Hash map script

```text
The brute force checks all pairs, which is O(n²). To optimize, I can scan once and store seen values in a hash map for O(1) average lookup.
```

### Set script

```text
I only need membership, not counts or associated values, so a set is enough.
```

### Sliding window script

```text
Because this asks for a contiguous substring/subarray, I can maintain a window with left and right pointers and update state as the window expands or shrinks.
```

### Prefix sum script

```text
I use prefix sums because subarray sums can be represented as differences between cumulative sums.
```

### Two pointers script

```text
Because the input is sorted, moving left or right gives me a deterministic way to adjust the sum.
```

### In-place script

```text
I use a read pointer to scan and a write pointer to overwrite valid values while keeping O(1) extra space.
```

### Data Engineering script

```text
This pattern is similar to processing records in a pipeline: scanning events once and storing only the state needed for dedupe, aggregation, or validation.
```


## 76. Maintenance Drills

After completing arrays and strings, maintain skill with:

```text
2 easy problems per week
2 medium problems per week
1 Data Engineering custom problem per week
1 pattern classification drill per week
1 timed mock every 2 weeks
```

Recommended maintenance rotation:

```text
Week 1: hash map + sliding window
Week 2: two pointers + prefix sum
Week 3: string parsing + stack
Week 4: DE custom + mixed mock
```

If score drops below 4:

```text
Run weakness-repair-mode.md for the failed pattern.
```


## 77. Final Exit Test

Candidate passes arrays and strings when they can solve:

```text
1. Two Sum
2. Valid Anagram
3. Group Anagrams
4. Valid Palindrome
5. Two Sum II
6. Longest Substring Without Repeating Characters
7. Minimum Size Subarray Sum
8. Subarray Sum Equals K
9. Product of Array Except Self
10. Maximum Subarray
11. String Compression
12. DE custom: latest record per ID
13. DE custom: parse logs and count errors
14. DE custom: source-target ID reconciliation
```

Passing standard:

```text
Average score >= 4/5.
No repeated O(n²) mistakes.
No missing complexity explanations.
No edge-case blindness.
No pattern confusion on hash map, set, two pointers, sliding window, and prefix sum.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles variations and explains Data Engineering relevance.
```


## 78. Final Summary

Arrays and strings are the foundation of coding interviews.

For Data Engineering candidates, they matter because they map directly to:

```text
records
events
logs
IDs
transactions
files
metrics
strings
timestamps
validation
deduplication
reconciliation
```

The candidate must not memorize isolated solutions.

The candidate must learn patterns:

```text
hash map
set
sorting
two pointers
sliding window
prefix sum
Kadane
string parsing
in-place overwrite
stack-like processing
matrix boundaries
```

The mentor must be strict:

```text
No pattern explanation → not interview-ready.
No complexity → not interview-ready.
No edge cases → not interview-ready.
Only sample passes → not interview-ready.
```

The goal is not to solve one problem.

The goal is to recognize the pattern behind many problems and explain it clearly under interview pressure.


## 79. Problem Card Appendix

### Card 1: Two Sum

LeetCode:

```text
1. Two Sum
Difficulty: Easy
```

Primary pattern:

```text
Hash map
```

Core idea:

```text
Fast complement lookup while scanning once.
```

Data Engineering connection:

```text
Find two transactions that match a target adjustment.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
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
Set
```

Core idea:

```text
Track seen values for duplicate detection.
```

Data Engineering connection:

```text
Detect duplicate event_id or transaction_id.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
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

Core idea:

```text
Compare character counts.
```

Data Engineering connection:

```text
Compare normalized signature strings.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Group Anagrams

LeetCode:

```text
49. Group Anagrams
Difficulty: Medium
```

Primary pattern:

```text
Hash map grouping
```

Core idea:

```text
Use sorted string or frequency tuple as key.
```

Data Engineering connection:

```text
Group merchant aliases by normalized signature.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
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
Frequency count
```

Core idea:

```text
Count then scan in original order.
```

Data Engineering connection:

```text
Find first unique event marker.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Intersection of Two Arrays

LeetCode:

```text
349. Intersection of Two Arrays
Difficulty: Easy
```

Primary pattern:

```text
Set intersection
```

Core idea:

```text
Use sets when duplicates do not matter.
```

Data Engineering connection:

```text
Find IDs present in both source and target.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Intersection of Two Arrays II

LeetCode:

```text
350. Intersection of Two Arrays II
Difficulty: Easy
```

Primary pattern:

```text
Counter
```

Core idea:

```text
Use counts when duplicates matter.
```

Data Engineering connection:

```text
Compare repeated IDs across batches.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Majority Element

LeetCode:

```text
169. Majority Element
Difficulty: Easy
```

Primary pattern:

```text
Counting / Boyer-Moore
```

Core idea:

```text
Find value appearing more than n/2.
```

Data Engineering connection:

```text
Find dominant status in a batch.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Two Sum II

LeetCode:

```text
167. Two Sum II
Difficulty: Medium
```

Primary pattern:

```text
Two pointers
```

Core idea:

```text
Sorted input allows O(1) extra space.
```

Data Engineering connection:

```text
Pair sorted adjustments.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Valid Palindrome

LeetCode:

```text
125. Valid Palindrome
Difficulty: Easy
```

Primary pattern:

```text
Two pointers
```

Core idea:

```text
Skip non-alphanumeric and compare lowercased chars.
```

Data Engineering connection:

```text
Normalize and validate identifiers.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Reverse String

LeetCode:

```text
344. Reverse String
Difficulty: Easy
```

Primary pattern:

```text
Two pointers
```

Core idea:

```text
Swap in place.
```

Data Engineering connection:

```text
In-place character transformation.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: 3Sum

LeetCode:

```text
15. 3Sum
Difficulty: Medium
```

Primary pattern:

```text
Sort + two pointers
```

Core idea:

```text
Fix one value, find pair with two pointers.
```

Data Engineering connection:

```text
Find triplets of adjustment records.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Remove Duplicates from Sorted Array

LeetCode:

```text
26. Remove Duplicates from Sorted Array
Difficulty: Easy
```

Primary pattern:

```text
In-place write
```

Core idea:

```text
Write each unique value once.
```

Data Engineering connection:

```text
Dedupe sorted IDs.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Remove Element

LeetCode:

```text
27. Remove Element
Difficulty: Easy
```

Primary pattern:

```text
In-place write
```

Core idea:

```text
Copy values not equal to target.
```

Data Engineering connection:

```text
Filter invalid sentinel values.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Move Zeroes

LeetCode:

```text
283. Move Zeroes
Difficulty: Easy
```

Primary pattern:

```text
In-place write
```

Core idea:

```text
Move non-zero values forward.
```

Data Engineering connection:

```text
Move valid records before placeholders.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Longest Substring Without Repeating Characters

LeetCode:

```text
3. Longest Substring Without Repeating Characters
Difficulty: Medium
```

Primary pattern:

```text
Sliding window
```

Core idea:

```text
Maintain duplicate-free window.
```

Data Engineering connection:

```text
Longest unique event-type streak.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Maximum Average Subarray I

LeetCode:

```text
643. Maximum Average Subarray I
Difficulty: Easy
```

Primary pattern:

```text
Fixed window
```

Core idea:

```text
Slide fixed window sum.
```

Data Engineering connection:

```text
Max rolling average metric.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Minimum Size Subarray Sum

LeetCode:

```text
209. Minimum Size Subarray Sum
Difficulty: Medium
```

Primary pattern:

```text
Variable window
```

Core idea:

```text
Positive numbers allow shrink while sum >= target.
```

Data Engineering connection:

```text
Smallest event window crossing threshold.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Permutation in String

LeetCode:

```text
567. Permutation in String
Difficulty: Medium
```

Primary pattern:

```text
Window + frequency
```

Core idea:

```text
Fixed window of target length with counts.
```

Data Engineering connection:

```text
Detect event signature permutation.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Find All Anagrams

LeetCode:

```text
438. Find All Anagrams
Difficulty: Medium
```

Primary pattern:

```text
Window + frequency
```

Core idea:

```text
Record all window starts matching counts.
```

Data Engineering connection:

```text
Find matching sequence signatures.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 21: Longest Repeating Character Replacement

LeetCode:

```text
424. Longest Repeating Character Replacement
Difficulty: Medium
```

Primary pattern:

```text
Window + frequency
```

Core idea:

```text
Window valid if length - max_count <= k.
```

Data Engineering connection:

```text
Longest period requiring at most k corrections.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 22: Range Sum Query

LeetCode:

```text
303. Range Sum Query
Difficulty: Easy
```

Primary pattern:

```text
Prefix sum
```

Core idea:

```text
Precompute cumulative sums.
```

Data Engineering connection:

```text
Fast range metric queries.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 23: Subarray Sum Equals K

LeetCode:

```text
560. Subarray Sum Equals K
Difficulty: Medium
```

Primary pattern:

```text
Prefix sum + map
```

Core idea:

```text
Count prior prefix sums current-k.
```

Data Engineering connection:

```text
Count consecutive adjustment windows.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 24: Product of Array Except Self

LeetCode:

```text
238. Product of Array Except Self
Difficulty: Medium
```

Primary pattern:

```text
Prefix/suffix
```

Core idea:

```text
Combine product before and after each index.
```

Data Engineering connection:

```text
Per-record product without full recomputation.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 25: Maximum Subarray

LeetCode:

```text
53. Maximum Subarray
Difficulty: Medium
```

Primary pattern:

```text
Kadane
```

Core idea:

```text
Start new or extend current subarray.
```

Data Engineering connection:

```text
Max contiguous anomaly/gain period.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 26: Reverse Words in a String

LeetCode:

```text
151. Reverse Words in a String
Difficulty: Medium
```

Primary pattern:

```text
String parsing
```

Core idea:

```text
Split, reverse, join.
```

Data Engineering connection:

```text
Normalize whitespace-delimited fields.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 27: String Compression

LeetCode:

```text
443. String Compression
Difficulty: Medium
```

Primary pattern:

```text
Run-length + in-place
```

Core idea:

```text
Scan groups and write compressed form.
```

Data Engineering connection:

```text
Compress repeated status/event codes.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 28: Valid Parentheses

LeetCode:

```text
20. Valid Parentheses
Difficulty: Easy
```

Primary pattern:

```text
Stack
```

Core idea:

```text
Match closing bracket with latest opening bracket.
```

Data Engineering connection:

```text
Validate nested expression syntax.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 29: Backspace String Compare

LeetCode:

```text
844. Backspace String Compare
Difficulty: Easy
```

Primary pattern:

```text
Stack/two pointers
```

Core idea:

```text
Simulate edits or scan backwards.
```

Data Engineering connection:

```text
Process correction markers.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 30: Rotate Image

LeetCode:

```text
48. Rotate Image
Difficulty: Medium
```

Primary pattern:

```text
Matrix
```

Core idea:

```text
Transpose then reverse rows.
```

Data Engineering connection:

```text
2D transformation reasoning.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 31: Spiral Matrix

LeetCode:

```text
54. Spiral Matrix
Difficulty: Medium
```

Primary pattern:

```text
Matrix boundaries
```

Core idea:

```text
Maintain shrinking boundaries.
```

Data Engineering connection:

```text
Boundary traversal discipline.
```

Candidate must be able to explain:

```text
1. Why this pattern fits.
2. Brute force approach.
3. Optimized approach.
4. Edge cases.
5. Time complexity.
6. Space complexity.
7. One follow-up variation.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 80. Drill Appendix

### Drill 1: Hash Map Lookup

Task:

```text
Solve Two Sum, then explain how same pattern applies to lookup enrichment.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Set Deduplication

Task:

```text
Solve Contains Duplicate, then dedupe event IDs with invalid_count.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Frequency Count

Task:

```text
Solve Valid Anagram, then count events by type.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
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
Solve Group Anagrams, then group merchant aliases.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Two Pointers

Task:

```text
Solve Two Sum II and Valid Palindrome.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: In-Place Write

Task:

```text
Solve Remove Element, Remove Duplicates, and Move Zeroes.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Sliding Window Fixed

Task:

```text
Solve Maximum Average Subarray I and rolling error window.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Sliding Window Variable

Task:

```text
Solve Longest Substring and longest healthy streak.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Prefix Sum

Task:

```text
Solve Range Sum Query and Subarray Sum Equals K.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Kadane

Task:

```text
Solve Maximum Subarray and explain all-negative edge case.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: String Parsing

Task:

```text
Solve Reverse Words, then parse logs by service.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Run-Length

Task:

```text
Solve String Compression and compress repeated statuses.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Stack String

Task:

```text
Solve Valid Parentheses and Backspace String Compare.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Matrix Boundaries

Task:

```text
Solve Spiral Matrix and explain boundary checks.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: DE Mixed

Task:

```text
Deduplicate events, keep latest records, reconcile IDs, parse logs, rolling window.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Pattern Classification

Task:

```text
Classify 20 prompts before coding.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Timed Mock

Task:

```text
Run 5 problems in 90 minutes with score and review.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 18: Weakness Repair

Task:

```text
Take lowest-scored pattern and solve 3 variations.
```

Minimum passing answer:

```text
1. State the pattern.
2. Explain brute force.
3. Explain optimized approach.
4. Write clean code.
5. Dry run an edge case.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```
