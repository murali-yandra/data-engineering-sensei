# Two Pointers and Sliding Window Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/dsa/two-pointers-sliding-window.md
```

This guide teaches and drills **two pointers and sliding window patterns for Data Engineering interviews**.

This is not a generic array tutorial. It is an interview-focused guide for Data Engineering candidates who need to solve pair matching, sorted scans, deduplication, range windows, streaming windows, substring constraints, event-time windows, fixed-size windows, variable-size windows, and efficient O(n) scans.

Two pointers and sliding window are high-ROI because they appear in:

- coding interviews
- SQL-like ordered scans
- sorted source-target reconciliation
- deduplication after sorting
- pair matching
- partition gap checks
- session/event sequence problems
- contiguous subarray problems
- substring problems
- fixed-size rolling calculations
- variable-size constraint windows
- event-time window processing
- rate-limit windows
- streaming event windows
- telemetry window analysis
- transaction window analysis
- API pagination/range comparison
- sorted merge comparisons
- finding longest/shortest contiguous segments
- reducing O(n²) nested loops to O(n)

Use this guide with:

- `docs/dsa-for-data-engineers.md`
- `docs/python-interview-guide.md`
- `docs/leetcode-practice-map.md`
- `docs/data-engineering-fundamentals.md`
- `docs/etl-elt-pipelines-guide.md`
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
- `practice/dsa/hashmaps.md`
- `practice/dsa/stack-queue.md`
- `practice/dsa/sorting-binary-search.md`
- `practice/dsa/intervals.md`
- `progress/CANDIDATE_PROFILE.md`
- `progress/CURRENT_STATE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Default interview standard if target companies are not provided:

```text
FAANG-style Data Engineering coding standard, scaled by candidate experience.
```


## 1. Purpose

The purpose of this guide is to make the candidate strong at two pointers and sliding window patterns.

The candidate should learn to answer:

```text
When should I use two pointers?
When should I sort first?
When does two pointers work only on sorted input?
When should I use fast and slow pointers?
When should I use left and right window pointers?
When is the window fixed-size?
When is the window variable-size?
When do I shrink the window?
When do I expand the window?
When do I need a hash map inside the window?
When do I need a running sum?
When do I need a deque instead?
How do I handle duplicates?
How do I handle negative numbers?
How do I connect this to Data Engineering windows and event streams?
```

A candidate is interview-ready only when they can:

```text
identify two-pointer trigger clues
identify sliding-window trigger clues
choose fixed vs variable window
choose sorted two pointers vs hash map
write clean O(n) scans
handle duplicates and boundaries
avoid nested loops where possible
explain why pointer movement is safe
handle positive-only and negative-number differences
use frequency maps inside windows
handle event-time windows
dry run pointer movement
explain complexity
connect the pattern to Data Engineering scenarios
```


## 2. Why These Patterns Matter for Data Engineers

Two pointers and sliding window are extremely practical for Data Engineering.

Data Engineering examples:

```text
Compare sorted source and target IDs.
Find missing IDs between two sorted streams.
Deduplicate sorted event IDs.
Merge or compare ordered event logs.
Match debit and credit amounts in sorted transaction lists.
Find continuous event window with total amount under limit.
Find longest session with at most K event types.
Find smallest log segment containing all required event types.
Compute rolling row-count sums over fixed windows.
Compute rolling average latency over last K runs.
Find max consecutive successful pipeline runs.
Find longest streak of acceptable data-quality scores.
Find number of requests in recent time range.
Find transactions in a contiguous time window.
Find first/last valid segment under SLA constraints.
Find users with repeated events inside a window.
```

Interviewers ask these patterns because they show whether the candidate can reason about contiguous data, sorted scans, and efficient state updates.


## 3. Core Mental Model: Two Pointers

Two pointers means using two indices to scan data efficiently.

Common pointer types:

```text
left and right from both ends
slow and fast from same side
read and write pointer
pointer over array A and pointer over array B
```

Use two pointers when:

```text
input is sorted
you need pair matching
you need remove/compact in-place
you need compare two sorted lists
you need reverse or partition
you need merge-like scan
```

Classic example:

```text
sorted nums = [1, 2, 4, 7, 11]
target = 9

left = 0, right = 4
sum = 1 + 11 = 12 too high → move right left
sum = 1 + 7 = 8 too low → move left right
sum = 2 + 7 = 9 found
```

Interview line:

```text
Two pointers work here because sorted order tells me which pointer movement can increase or decrease the current value.
```


## 4. Core Mental Model: Sliding Window

Sliding window is a contiguous range inside an array/string/stream.

Window:

```text
[left, right]
```

or half-open:

```text
[left, right)
```

Use sliding window when:

```text
problem asks about contiguous subarray
problem asks about substring
problem asks about consecutive events
problem asks longest/shortest segment
problem asks fixed-size rolling metric
problem asks at most/at least/exactly K constraint
```

Window operations:

```text
expand right
update state with new item
while invalid, shrink left
update answer when valid
```

Generic variable window:

```python
left = 0

for right in range(len(items)):
    add items[right] to window

    while window_is_invalid:
        remove items[left] from window
        left += 1

    update answer
```

Interview line:

```text
Sliding window fits because the answer depends on a contiguous segment, and I can update the segment state incrementally instead of recomputing from scratch.
```


## 5. Fixed-Size vs Variable-Size Window

### Fixed-size window

Use when:

```text
window length is exactly K
rolling sum of K elements
maximum average of K elements
number of windows of size K
anagram/permutation of fixed pattern length
```

Template:

```python
window_sum = 0

for right, value in enumerate(nums):
    window_sum += value

    if right >= k:
        window_sum -= nums[right - k]

    if right >= k - 1:
        update_answer(window_sum)
```

### Variable-size window

Use when:

```text
longest substring with at most K distinct
minimum subarray length with sum at least target
longest subarray under constraint
smallest window containing all required chars
```

Template:

```python
left = 0

for right, value in enumerate(nums):
    add(value)

    while condition_is_invalid_or_ready_to_shrink:
        remove(nums[left])
        left += 1

    update_answer()
```

Strict rule:

```text
If the window size is given as exactly K, start with fixed-size window.
If the problem asks longest/shortest satisfying a constraint, start with variable-size window.
```


## 6. Positive Numbers vs Negative Numbers Warning

Sliding window with sum constraints often depends on positivity.

Works well when:

```text
all numbers are positive
all numbers are non-negative
adding right never decreases sum
removing left never increases sum
```

Example:

```text
minimum length subarray with sum >= target
```

If numbers can be negative:

```text
simple sliding window may fail
```

Why:

```text
Adding a negative value can decrease sum.
Removing a negative value can increase sum.
The monotonic behavior needed for shrinking is broken.
```

Alternative patterns when negatives exist:

```text
prefix sum + hash map
prefix sum + monotonic deque
dynamic programming
balanced tree depending problem
```

Interview line:

```text
I can use a standard sliding window only because all values are positive/non-negative. If negatives are allowed, this approach may not be valid.
```


## 7. Standard Answer Framework

Use this framework for every two-pointer/sliding-window problem:

```text
1. Restate the problem.
2. Clarify contiguous vs non-contiguous.
3. Clarify sorted vs unsorted.
4. Clarify positive/negative numbers.
5. Clarify duplicates and output format.
6. Explain brute force.
7. Identify pattern:
   - two pointers from ends
   - fast/slow pointers
   - read/write in-place
   - two sorted lists
   - fixed-size sliding window
   - variable-size sliding window
   - frequency map inside window
8. Define pointer meaning.
9. Define window state.
10. Define expand rule.
11. Define shrink/move rule.
12. Write code.
13. Dry run pointer movement.
14. Explain edge cases.
15. Explain time and space complexity.
16. Connect to Data Engineering scenario.
```

Short version:

```text
Pointers:
State:
Move condition:
Answer update:
Complexity:
Edge cases:
```

Strict rule:

```text
No pointer code before explaining why moving that pointer is safe.
```


## 8. Scoring Rubric

Score each two-pointer/sliding-window attempt from 0 to 5.

### Score 0

No meaningful attempt.

### Score 1

Does not understand pointer/window idea.

### Score 2

Partial approach but wrong pointer movement or broken edge cases.

### Score 3

Works for common cases but weak on duplicates, boundaries, or explanation.

### Score 4

Interview-ready. Correct pointer/window logic, edge cases, and complexity.

### Score 5

Strong. Handles variants, proves movement safety, and connects to DE scenarios.

Do not give 4+ if:

```text
candidate cannot explain pointer movement
candidate uses nested loops when O(n) is expected
candidate uses sliding window when negative numbers break it
candidate forgets to shrink window
candidate updates answer in wrong place
candidate has off-by-one window length bugs
candidate fails duplicates
candidate cannot distinguish fixed vs variable window
candidate cannot explain time complexity
candidate cannot connect to Data Engineering use cases
```


## 9. Complexity Rules

Common complexities:

```text
Two pointers scan: O(n)
Two pointers after sorting: O(n log n) due to sort
Two sorted lists comparison: O(n + m)
Fast/slow in-place compaction: O(n)
Fixed-size sliding window: O(n)
Variable-size sliding window: O(n) when each pointer moves forward at most n times
Sliding window with frequency map: O(n) average
Minimum window substring: O(n + m)
```

Space:

```text
Basic two pointers: O(1)
In-place compaction: O(1)
Frequency window: O(k) or O(unique chars)
Output list: O(output)
Sorted copy: O(n)
```

Why variable sliding window is O(n):

```text
right moves from 0 to n-1 once.
left also moves from 0 to n-1 at most once.
Total pointer movement is O(n), not O(n²).
```

Interview wording:

```text
Although there is a nested while loop, each element is added once and removed once, so the total time is O(n).
```


## 10. Edge Case Checklist

Two-pointer edge cases:

```text
empty array
one element
two elements
duplicates
all duplicates
negative values
target not found
multiple valid answers
original indices required
input not sorted
k = 0
k > n
left crosses right
same element reused accidentally
```

Sliding-window edge cases:

```text
empty string/array
window size k = 0
window size k = 1
k > n
all valid
none valid
all same characters
all unique characters
duplicates in window
negative values in sum problems
zero values
target impossible
minimum window not found
frequency count goes to zero
left/right off-by-one
```

Data Engineering-specific edge cases:

```text
events out of order
timestamps equal
window boundary inclusive/exclusive
late-arriving events
duplicate event IDs
missing event_time
invalid amount
timezone-normalization
empty batch
partition list not sorted
source/target duplicates
```


## 11. Pattern Map

Two-pointer and sliding-window patterns:

```text
1. Opposite-direction two pointers.
2. Same-direction fast/slow pointers.
3. Read/write pointer for in-place compaction.
4. Two sorted lists comparison.
5. Merge-like scan.
6. Pair sum in sorted array.
7. 3Sum after sorting.
8. Palindrome check.
9. Reverse in-place.
10. Remove duplicates from sorted array.
11. Move zeros.
12. Container with most water.
13. Trapping rain water.
14. Fixed-size sliding window sum/average.
15. Variable-size longest valid window.
16. Variable-size shortest valid window.
17. Window with frequency map.
18. At most K distinct.
19. Exactly K via atMost(K) - atMost(K-1).
20. Minimum window substring.
21. Permutation/anagram fixed window.
22. Time-based event window.
23. Rolling metrics.
24. Source-target sorted reconciliation.
25. Session/event sequence analysis.
```

Pattern selection:

```text
Sorted pair matching → opposite two pointers.
In-place remove/compact → fast/slow or read/write.
Contiguous substring/subarray → sliding window.
Fixed length K → fixed window.
Longest/shortest with condition → variable window.
Need counts in window → hash map + sliding window.
Need max/min in window → monotonic deque.
```


## 12. Common Mistakes

Common mistakes:

```text
Using sliding window for non-contiguous subsequence problem.
Using two pointers from ends on unsorted data without sorting.
Sorting and losing original indices.
Reusing same element twice.
Skipping duplicate handling in 3Sum.
Moving wrong pointer in sorted pair problems.
Forgetting to update answer before/after shrinking correctly.
Using while when if is enough in fixed window.
Using if when while is needed in variable window.
Not deleting zero-count keys from frequency map.
Assuming sliding sum works with negative numbers.
Off-by-one in window length.
Returning wrong length when no valid window exists.
Not handling k > n.
Not clarifying inclusive/exclusive time windows.
```

Strict feedback:

```text
This is not interview-ready. You used sliding window for a sum problem without confirming all numbers are non-negative, so the shrink logic is not guaranteed correct.
```


## 13. Pattern: Opposite-Direction Two Pointers

Use when:

```text
array is sorted
need pair matching
need maximize/minimize with two ends
need compare smallest and largest
```

Template:

```python
left = 0
right = len(nums) - 1

while left < right:
    current = compute(nums[left], nums[right])

    if current == target:
        return answer
    elif current < target:
        left += 1
    else:
        right -= 1
```

Why it works:

```text
Sorted order tells us how moving a pointer changes the value.
Moving left right increases value.
Moving right left decreases value.
```

Data Engineering connection:

```text
Match two sorted transaction amounts to a target reconciliation amount.
```


## 14. Problem: Two Sum II

LeetCode:

```text
167. Two Sum II - Input Array Is Sorted
Difficulty: Medium
Pattern: Opposite two pointers
```

Code:

```python
def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]

        if total < target:
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

Edge cases:

```text
negative numbers
duplicates
target not found
one-based index output
```

Data Engineering connection:

```text
Find two sorted adjustment amounts that match a reconciliation target.
```

Common mistake:

```text
Using left <= right and allowing the same element to be used twice.
```


## 15. Data Engineering Custom Problem: Match Debit Credit Amounts

Problem:

```text
Given sorted positive debit amounts and credit amounts, find one pair whose sum equals target.
Return indices [debit_index, credit_index], or [].
```

Pattern:

```text
Two pointers across two sorted arrays
```

Code:

```python
def match_debit_credit(debits, credits, target):
    i = 0
    j = len(credits) - 1

    while i < len(debits) and j >= 0:
        total = debits[i] + credits[j]

        if total == target:
            return [i, j]

        if total < target:
            i += 1
        else:
            j -= 1

    return []
```

Complexity:

```text
Time: O(n + m)
Space: O(1)
```

Follow-ups:

```text
Return all pairs.
Handle duplicate amounts.
Return closest pair if exact match does not exist.
```


## 16. Pattern: Palindrome Two Pointers

Use two pointers from ends when comparing symmetric positions.

Template:

```python
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        return False

    left += 1
    right -= 1

return True
```

Variants:

```text
ignore non-alphanumeric
case-insensitive
allow one deletion
compare normalized tokens
```

Data Engineering connection:

```text
Validate symmetric identifiers, normalized strings, or simple token integrity checks.
```


## 17. Problem: Valid Palindrome

LeetCode:

```text
125. Valid Palindrome
Difficulty: Easy
Pattern: Two pointers
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

Edge cases:

```text
empty string
only punctuation
mixed case
numbers
spaces
```

Data Engineering connection:

```text
Normalize and compare string tokens without building a separate cleaned string.
```


## 18. Problem: Valid Palindrome II

LeetCode:

```text
680. Valid Palindrome II
Difficulty: Easy
Pattern: Two pointers with one deletion
```

Code:

```python
def valid_palindrome(s):
    def is_range_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return (
                is_range_palindrome(left + 1, right)
                or is_range_palindrome(left, right - 1)
            )

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
Tolerant string comparison where one bad character may be ignored.
```

Common mistake:

```text
Greedily deleting only left or only right without checking both possibilities.
```


## 19. Pattern: Fast and Slow Pointers

Fast and slow pointers move through the same sequence at different speeds.

Use for:

```text
linked list cycle detection
middle of linked list
remove nth node from end
in-place compaction
cycle detection in iterative process
```

Classic cycle detection:

```text
slow moves 1 step
fast moves 2 steps
if they meet, cycle exists
```

Data Engineering analogy:

```text
Detect repeated state in iterative process, though hash set is often clearer for arbitrary states.
```

Interview line:

```text
Fast/slow pointers are useful when relative movement reveals structure, such as cycle or middle position.
```


## 20. Problem: Linked List Cycle

LeetCode:

```text
141. Linked List Cycle
Difficulty: Easy
Pattern: Fast and slow pointers
```

Code:

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Conceptually similar to detecting cycles in state transitions, but graph cycle detection is more common for DE pipeline DAGs.
```


## 21. Problem: Middle of the Linked List

LeetCode:

```text
876. Middle of the Linked List
Difficulty: Easy
Pattern: Fast and slow pointers
```

Code:

```python
def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Interview point:

```text
When fast reaches the end, slow is at the middle.
```

Data Engineering connection:

```text
Less direct, but reinforces pointer movement and single-pass logic.
```


## 22. Pattern: Read/Write Pointer for In-Place Compaction

Use read/write pointers when:

```text
remove duplicates in-place
remove a value in-place
move zeros
compact valid records
rewrite array without extra list
```

State:

```text
read pointer scans every item
write pointer marks where next kept item should go
```

Template:

```python
write = 0

for read in range(len(nums)):
    if should_keep(nums[read]):
        nums[write] = nums[read]
        write += 1

return write
```

Data Engineering connection:

```text
Compact valid records in a batch while preserving order.
```

Interview line:

```text
The read pointer scans all items, and the write pointer only advances when I keep an item.
```


## 23. Problem: Remove Duplicates from Sorted Array

LeetCode:

```text
26. Remove Duplicates from Sorted Array
Difficulty: Easy
Pattern: Read/write pointer
```

Code:

```python
def remove_duplicates(nums):
    if not nums:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Edge cases:

```text
empty array
all duplicates
no duplicates
single element
```

Data Engineering connection:

```text
Deduplicate sorted event IDs in-place while preserving first occurrence.
```

Common mistake:

```text
Comparing nums[read] to nums[read - 1] can work for this problem, but comparing to nums[write - 1] is more robust for write-state thinking.
```


## 24. Problem: Remove Element

LeetCode:

```text
27. Remove Element
Difficulty: Easy
Pattern: Read/write pointer
```

Code preserving order:

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

Alternative when order does not matter:

```python
def remove_element(nums, val):
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1

    return left
```

Data Engineering connection:

```text
Compact a batch by removing invalid marker records.
```


## 25. Problem: Move Zeroes

LeetCode:

```text
283. Move Zeroes
Difficulty: Easy
Pattern: Read/write pointer
```

Code:

```python
def move_zeroes(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Data Engineering connection:

```text
Move valid/non-zero metrics to the front while preserving their relative order.
```

Common mistake:

```text
Using repeated remove/append operations, causing O(n²).
```


## 26. Data Engineering Custom Problem: Compact Valid Records

Problem:

```text
Given records, compact valid records to the front in-place.
A valid record has non-null id and event_time.
Return count of valid records.
```

Pattern:

```text
Read/write pointer
```

Code:

```python
def compact_valid_records(records):
    write = 0

    for read in range(len(records)):
        record = records[read]

        if record.get("id") is not None and record.get("event_time") is not None:
            records[write] = record
            write += 1

    return write
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

After call:

```text
records[:valid_count] contains valid records.
```

Follow-ups:

```text
Preserve invalid records too?
Return invalid count?
Avoid mutating input?
```


## 27. Pattern: Two Sorted Lists Comparison

Use two pointers when comparing sorted lists.

Trigger phrases:

```text
source and target sorted IDs
find missing IDs
intersection of sorted arrays
merge sorted arrays
compare two sorted streams
```

Algorithm idea:

```text
i over A
j over B

if A[i] == B[j]:
    both advance
elif A[i] < B[j]:
    A item missing from B or belongs before
    i advances
else:
    B item extra or belongs before
    j advances
```

Complexity:

```text
O(n + m)
```

Data Engineering connection:

```text
Source-target reconciliation without hash maps when both datasets are sorted.
```


## 28. Problem: Intersection of Two Arrays II Sorted Variant

LeetCode:

```text
350. Intersection of Two Arrays II
Difficulty: Easy
Pattern: Sort + two pointers or Counter
```

Two-pointer code:

```python
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return result
```

Complexity:

```text
Time: O(n log n + m log m)
Space: O(output) excluding sort
```

If already sorted:

```text
Time: O(n + m)
```

Data Engineering connection:

```text
Find matching IDs between sorted source and target exports.
```


## 29. Data Engineering Custom Problem: Reconcile Sorted IDs

Problem:

```text
Given sorted source_ids and target_ids, return:
- missing_in_target
- extra_in_target
- matched
Assume IDs may be duplicated and duplicates matter.
```

Pattern:

```text
Two sorted lists comparison
```

Code:

```python
def reconcile_sorted_ids(source_ids, target_ids):
    i = 0
    j = 0
    missing = []
    extra = []
    matched = []

    while i < len(source_ids) and j < len(target_ids):
        if source_ids[i] == target_ids[j]:
            matched.append(source_ids[i])
            i += 1
            j += 1
        elif source_ids[i] < target_ids[j]:
            missing.append(source_ids[i])
            i += 1
        else:
            extra.append(target_ids[j])
            j += 1

    while i < len(source_ids):
        missing.append(source_ids[i])
        i += 1

    while j < len(target_ids):
        extra.append(target_ids[j])
        j += 1

    return {
        "matched": matched,
        "missing_in_target": missing,
        "extra_in_target": extra,
    }
```

Complexity:

```text
Time: O(n + m)
Space: O(output)
```

Follow-ups:

```text
What if IDs are not sorted?
What if duplicates should be ignored?
What if IDs are strings with case differences?
```

Expected:

```text
Sort first, use set if duplicates ignored, normalize IDs if needed.
```


## 30. Pattern: 3Sum / K-Sum After Sorting

3Sum uses sorting plus two pointers.

Why sort:

```text
Allows duplicate skipping.
Allows two-pointer pair search.
```

High-level:

```text
For each fixed index i:
  skip duplicate fixed values
  run two-sum with left=i+1 and right=n-1
  skip duplicate left/right values after finding answer
```

Data Engineering connection:

```text
Find triplets of transaction adjustments that net to zero or match a target.
```

Interview line:

```text
Sorting lets me avoid duplicate triplets and use two pointers for the remaining pair.
```


## 31. Problem: 3Sum

LeetCode:

```text
15. 3Sum
Difficulty: Medium
Pattern: Sort + two pointers
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
Space: O(1) extra excluding output, depending sort
```

Common mistakes:

```text
not skipping duplicate fixed value
not skipping duplicate left/right after match
using same index twice
```

Data Engineering connection:

```text
Find unique transaction triplets that net to zero.
```


## 32. Problem: 3Sum Closest

LeetCode:

```text
16. 3Sum Closest
Difficulty: Medium
Pattern: Sort + two pointers
```

Code:

```python
def three_sum_closest(nums, target):
    nums.sort()
    best = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(total - target) < abs(best - target):
                best = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return target

    return best
```

Complexity:

```text
Time: O(n²)
Space: O(1) extra
```

Data Engineering connection:

```text
Find three adjustment values closest to reconciliation target.
```


## 33. Pattern: Container / Max Area

Some two-pointer problems use geometric or boundary logic.

Container With Most Water:

```text
area = min(height[left], height[right]) * width
```

Move pointer with smaller height because:

```text
The width will shrink no matter what.
To possibly improve area, we need a taller boundary.
Moving taller side cannot help while shorter side remains the limit.
```

Interview line:

```text
I move the smaller height pointer because the smaller side limits the current area.
```

Data Engineering connection:

```text
Less direct, but tests proof-based pointer movement.
```


## 34. Problem: Container With Most Water

LeetCode:

```text
11. Container With Most Water
Difficulty: Medium
Pattern: Opposite two pointers
```

Code:

```python
def max_area(height):
    left = 0
    right = len(height) - 1
    best = 0

    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width
        best = max(best, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Common mistake:

```text
Moving the larger pointer without justification.
```


## 35. Pattern: Trapping Rain Water

Trapping Rain Water can use two pointers.

Idea:

```text
Water at a position depends on min(max_left, max_right) - height.
```

Two-pointer method:

```text
Keep left_max and right_max.
Move the side with smaller height/max boundary.
```

Data Engineering connection:

```text
Less direct, but tests advanced two-pointer reasoning and boundary accumulation.
```


## 36. Problem: Trapping Rain Water

LeetCode:

```text
42. Trapping Rain Water
Difficulty: Hard
Pattern: Two pointers
```

Code:

```python
def trap(height):
    if not height:
        return 0

    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Common mistake:

```text
Trying to compute water without knowing a valid boundary.
```


## 37. Pattern: Fixed-Size Sliding Window

Use fixed-size window when the length is exactly K.

Trigger phrases:

```text
subarray of size k
substring of length k
rolling average over k items
maximum sum of k consecutive elements
count windows of length k
```

Template:

```python
def fixed_window(nums, k):
    if k <= 0 or k > len(nums):
        return None

    window_sum = 0
    best = float("-inf")

    for right, value in enumerate(nums):
        window_sum += value

        if right >= k:
            window_sum -= nums[right - k]

        if right >= k - 1:
            best = max(best, window_sum)

    return best
```

Data Engineering connection:

```text
Rolling K-run sum, average, or metric.
```


## 38. Problem: Maximum Average Subarray I

LeetCode:

```text
643. Maximum Average Subarray I
Difficulty: Easy
Pattern: Fixed-size sliding window
```

Code:

```python
def find_max_average(nums, k):
    window_sum = 0
    best_sum = float("-inf")

    for right, value in enumerate(nums):
        window_sum += value

        if right >= k:
            window_sum -= nums[right - k]

        if right >= k - 1:
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
Find maximum average latency, row count, or throughput over K consecutive runs.
```

Common mistake:

```text
Recomputing each K-window sum from scratch, causing O(nk).
```


## 39. Data Engineering Custom Problem: Rolling K-Run Error Sum

Problem:

```text
Given error counts per pipeline run, return maximum total errors over any K consecutive runs.
```

Pattern:

```text
Fixed-size sliding window
```

Code:

```python
def max_k_run_error_sum(error_counts, k):
    if k <= 0 or k > len(error_counts):
        return 0

    window_sum = 0
    best = 0

    for right, count in enumerate(error_counts):
        window_sum += count

        if right >= k:
            window_sum -= error_counts[right - k]

        if right >= k - 1:
            best = max(best, window_sum)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Follow-ups:

```text
Return start/end index of the best window.
Return average instead of sum.
Handle missing counts.
```


## 40. Pattern: Fixed Window with Frequency Map

Use when:

```text
window length is fixed
need character counts
need check permutation/anagram
need compare pattern frequency
```

Examples:

```text
Permutation in String
Find All Anagrams in a String
```

State:

```text
required counts
window counts
left/right fixed length
```

Important:

```text
Remove left character when window exceeds pattern length.
```

Data Engineering connection:

```text
Find event sequences containing exactly the required set of event types in a fixed-length window.
```


## 41. Problem: Permutation in String

LeetCode:

```text
567. Permutation in String
Difficulty: Medium
Pattern: Fixed-size sliding window + frequency map
```

Code:

```python
from collections import Counter

def check_inclusion(s1, s2):
    k = len(s1)

    if k > len(s2):
        return False

    required = Counter(s1)
    window = Counter()

    for right, char in enumerate(s2):
        window[char] += 1

        if right >= k:
            left_char = s2[right - k]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

        if window == required:
            return True

    return False
```

Complexity:

```text
Time: O(n * alphabet_compare) or O(n) if alphabet size is fixed
Space: O(k)
```

Data Engineering connection:

```text
Check whether any fixed-length event window contains exactly a required multiset of event types.
```

Common mistake:

```text
Not deleting zero-count keys, causing Counter/dict comparison issues in manual map implementations.
```


## 42. Problem: Find All Anagrams in a String

LeetCode:

```text
438. Find All Anagrams in a String
Difficulty: Medium
Pattern: Fixed-size sliding window + frequency map
```

Code:

```python
from collections import Counter

def find_anagrams(s, p):
    k = len(p)

    if k > len(s):
        return []

    required = Counter(p)
    window = Counter()
    result = []

    for right, char in enumerate(s):
        window[char] += 1

        if right >= k:
            left_char = s[right - k]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

        if window == required:
            result.append(right - k + 1)

    return result
```

Complexity:

```text
Time: O(n) for fixed alphabet
Space: O(k)
```

Data Engineering connection:

```text
Find fixed-length event windows matching a required event-type pattern.
```


## 43. Pattern: Variable Window - Longest Valid Window

Use when:

```text
find longest subarray/substring satisfying condition
condition becomes invalid when too much is included
```

Template:

```python
left = 0
best = 0

for right, value in enumerate(items):
    add(value)

    while window_is_invalid:
        remove(items[left])
        left += 1

    best = max(best, right - left + 1)
```

Examples:

```text
longest substring without repeating chars
longest substring with at most K distinct
max consecutive ones after flipping K zeros
longest subarray with sum <= target for positive numbers
```

Data Engineering connection:

```text
Find longest event sequence satisfying quality/variety/error constraints.
```


## 44. Problem: Longest Substring Without Repeating Characters

LeetCode:

```text
3. Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Variable sliding window + set/map
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
Space: O(k), unique chars
```

Data Engineering connection:

```text
Find longest event sequence without repeating event type.
```


## 45. Problem: Longest Substring with At Most K Distinct Characters

LeetCode:

```text
340. Longest Substring with At Most K Distinct Characters
Difficulty: Medium
Pattern: Variable sliding window + frequency map
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
Find longest session containing at most K event types.
```

Common mistake:

```text
Forgetting to delete zero-count keys, so len(counts) is wrong.
```


## 46. Problem: Fruit Into Baskets

LeetCode:

```text
904. Fruit Into Baskets
Difficulty: Medium
Pattern: At most 2 distinct sliding window
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
Space: O(1), at most 3 keys temporarily
```

Data Engineering connection:

```text
Find longest event window containing at most two event categories.
```


## 47. Data Engineering Custom Problem: Longest Session with K Event Types

Problem:

```text
Given event_types in order, return length of longest contiguous session containing at most K distinct event types.
```

Pattern:

```text
Variable sliding window + frequency map
```

Code:

```python
from collections import defaultdict

def longest_session_at_most_k_event_types(event_types, k):
    if k <= 0:
        return 0

    counts = defaultdict(int)
    left = 0
    best = 0

    for right, event_type in enumerate(event_types):
        counts[event_type] += 1

        while len(counts) > k:
            left_type = event_types[left]
            counts[left_type] -= 1

            if counts[left_type] == 0:
                del counts[left_type]

            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Follow-ups:

```text
Return actual window.
Use timestamps and max session duration.
Ignore null event types.
```


## 48. Pattern: Variable Window - Shortest Valid Window

Use when:

```text
find minimum length subarray/substring satisfying condition
```

Template:

```python
left = 0
best = infinity

for right, value in enumerate(items):
    add(value)

    while window_is_valid:
        best = min(best, right - left + 1)
        remove(items[left])
        left += 1
```

Examples:

```text
minimum size subarray sum
minimum window substring
smallest log segment containing required events
```

Important:

```text
Update answer before shrinking because current window is valid.
```

Data Engineering connection:

```text
Find smallest contiguous event segment that contains all required event types.
```


## 49. Problem: Minimum Size Subarray Sum

LeetCode:

```text
209. Minimum Size Subarray Sum
Difficulty: Medium
Pattern: Variable sliding window, positive numbers
```

Problem:

```text
Given positive integers and target, find minimal length of subarray with sum >= target.
```

Code:

```python
def min_sub_array_len(target, nums):
    left = 0
    window_sum = 0
    best = float("inf")

    for right, value in enumerate(nums):
        window_sum += value

        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if best == float("inf") else best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Critical assumption:

```text
nums are positive. If negatives exist, this standard sliding window is not valid.
```

Data Engineering connection:

```text
Find shortest consecutive transaction segment whose total amount reaches a threshold.
```


## 50. Data Engineering Custom Problem: Shortest Error Window

Problem:

```text
Given non-negative error counts per minute, find shortest consecutive window with total errors >= threshold.
```

Pattern:

```text
Variable sliding window with non-negative numbers
```

Code:

```python
def shortest_error_window(error_counts, threshold):
    left = 0
    total = 0
    best = float("inf")

    for right, count in enumerate(error_counts):
        total += count

        while total >= threshold:
            best = min(best, right - left + 1)
            total -= error_counts[left]
            left += 1

    return 0 if best == float("inf") else best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Follow-ups:

```text
What if error deltas can be negative?
Return window indices.
Use timestamps instead of minute buckets.
```

Expected:

```text
If values can be negative, use prefix-sum/deque or another approach.
```


## 51. Problem: Minimum Window Substring

LeetCode:

```text
76. Minimum Window Substring
Difficulty: Hard
Pattern: Variable sliding window + frequency map
```

Problem:

```text
Find the minimum substring of s that contains all characters of t with required counts.
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
Find smallest contiguous log segment containing all required event types or markers.
```

Common mistakes:

```text
tracking unique presence but ignoring required counts
shrinking before recording answer
not updating have when count falls below requirement
```


## 52. Data Engineering Custom Problem: Smallest Log Segment with Required Events

Problem:

```text
Given event_types in order and required event types with counts, return smallest contiguous segment indices containing all required counts.
Return [] if impossible.
```

Pattern:

```text
Minimum window with frequency map
```

Code:

```python
from collections import Counter, defaultdict

def smallest_log_segment(event_types, required_events):
    required = Counter(required_events)
    window = defaultdict(int)
    have = 0
    need = len(required)

    left = 0
    best_length = float("inf")
    best = []

    for right, event_type in enumerate(event_types):
        window[event_type] += 1

        if event_type in required and window[event_type] == required[event_type]:
            have += 1

        while have == need:
            length = right - left + 1

            if length < best_length:
                best_length = length
                best = [left, right]

            left_type = event_types[left]
            window[left_type] -= 1

            if left_type in required and window[left_type] < required[left_type]:
                have -= 1

            left += 1

    return best
```

Complexity:

```text
Time: O(n + m)
Space: O(k)
```

Follow-ups:

```text
Return segment values.
Use timestamps.
Ignore invalid/null event types.
```


## 53. Pattern: Exactly K via At Most K

Many exactly-K subarray problems can be solved using:

```text
exactly K = atMost(K) - atMost(K - 1)
```

This works when counting subarrays with a property like:

```text
exactly K distinct values
exactly K odd numbers
exactly K different event types
```

At most K template:

```python
def at_most_k(items, k):
    if k < 0:
        return 0

    left = 0
    result = 0
    state = {}

    for right, value in enumerate(items):
        add(value)

        while invalid:
            remove(items[left])
            left += 1

        result += right - left + 1

    return result
```

Why add `right - left + 1`:

```text
All subarrays ending at right and starting from left..right are valid.
```


## 54. Problem: Subarrays with K Different Integers

LeetCode:

```text
992. Subarrays with K Different Integers
Difficulty: Hard
Pattern: exactly K = atMost(K) - atMost(K-1)
```

Code:

```python
from collections import defaultdict

def subarrays_with_k_distinct(nums, k):
    def at_most(limit):
        if limit < 0:
            return 0

        counts = defaultdict(int)
        left = 0
        total = 0

        for right, value in enumerate(nums):
            counts[value] += 1

            while len(counts) > limit:
                left_value = nums[left]
                counts[left_value] -= 1

                if counts[left_value] == 0:
                    del counts[left_value]

                left += 1

            total += right - left + 1

        return total

    return at_most(k) - at_most(k - 1)
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Count contiguous event windows with exactly K event types.
```

Common mistake:

```text
Trying to directly maintain exactly K and missing multiple valid starts.
```


## 55. Data Engineering Custom Problem: Count Windows with Exactly K Event Types

Problem:

```text
Given event_types, count contiguous windows with exactly K distinct event types.
```

Pattern:

```text
atMost(K) - atMost(K - 1)
```

Code:

```python
from collections import defaultdict

def count_windows_exactly_k_event_types(event_types, k):
    def at_most(limit):
        if limit < 0:
            return 0

        counts = defaultdict(int)
        left = 0
        total = 0

        for right, event_type in enumerate(event_types):
            counts[event_type] += 1

            while len(counts) > limit:
                left_type = event_types[left]
                counts[left_type] -= 1

                if counts[left_type] == 0:
                    del counts[left_type]

                left += 1

            total += right - left + 1

        return total

    return at_most(k) - at_most(k - 1)
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Follow-ups:

```text
Count exactly K error events instead of event types.
Use a timestamp-based window.
Return sample windows.
```


## 56. Pattern: Max Consecutive Ones / Flip K

Use sliding window when:

```text
can flip at most K zeros
need longest valid window
```

State:

```text
zero_count inside window
```

Valid condition:

```text
zero_count <= k
```

Template:

```text
expand right
if value is zero, zero_count += 1
while zero_count > k, shrink left
update best length
```

Data Engineering connection:

```text
Find longest streak of successful or acceptable runs allowing up to K failures.
```


## 57. Problem: Max Consecutive Ones III

LeetCode:

```text
1004. Max Consecutive Ones III
Difficulty: Medium
Pattern: Variable sliding window
```

Code:

```python
def longest_ones(nums, k):
    left = 0
    zeros = 0
    best = 0

    for right, value in enumerate(nums):
        if value == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1

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
Find longest run of successful pipeline runs allowing up to K failures.
```


## 58. Problem: Longest Repeating Character Replacement

LeetCode:

```text
424. Longest Repeating Character Replacement
Difficulty: Medium
Pattern: Variable sliding window + max frequency
```

Problem:

```text
Find longest substring that can become all same char after at most k replacements.
```

Code:

```python
from collections import defaultdict

def character_replacement(s, k):
    counts = defaultdict(int)
    left = 0
    best = 0
    max_count = 0

    for right, char in enumerate(s):
        counts[char] += 1
        max_count = max(max_count, counts[char])

        while (right - left + 1) - max_count > k:
            left_char = s[left]
            counts[left_char] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(k), unique chars
```

Important:

```text
max_count may be stale, but this still works because it only delays shrinking and best is updated for windows that are potentially valid under historical max.
```

Data Engineering connection:

```text
Find longest event segment that can be normalized to one dominant event type after at most K corrections.
```


## 59. Data Engineering Custom Problem: Longest Successful Run with K Failures

Problem:

```text
Given pipeline results as 1 success and 0 failure, return longest consecutive run if up to K failures can be ignored/fixed.
```

Pattern:

```text
Max consecutive ones with K flips
```

Code:

```python
def longest_success_streak_with_k_failures(results, k):
    left = 0
    failures = 0
    best = 0

    for right, result in enumerate(results):
        if result == 0:
            failures += 1

        while failures > k:
            if results[left] == 0:
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

Follow-ups:

```text
Return window indices.
Use statuses like SUCCESS/FAILED instead of 1/0.
Use time duration instead of count of runs.
```


## 60. Pattern: Sliding Window with Product

Use sliding window when:

```text
all numbers are positive
product constraint is monotonic with expanding/shrinking
```

Example:

```text
number of subarrays with product less than k
```

Important:

```text
If k <= 1 and all values are positive integers, no product can be less than k.
```

Data Engineering connection:

```text
Less common, but tests multiplicative window logic.
```


## 61. Problem: Subarray Product Less Than K

LeetCode:

```text
713. Subarray Product Less Than K
Difficulty: Medium
Pattern: Variable sliding window
```

Code:

```python
def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    product = 1
    left = 0
    total = 0

    for right, value in enumerate(nums):
        product *= value

        while product >= k:
            product //= nums[left]
            left += 1

        total += right - left + 1

    return total
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Common mistake:

```text
Forgetting k <= 1 edge case.
```

Data Engineering connection:

```text
Count contiguous metric windows with product-like risk score below threshold.
```


## 62. Pattern: Time-Based Sliding Window

Use time-based sliding window when:

```text
events arrive sorted by timestamp
need events in last N seconds/minutes
need rate-limit count
need rolling time metric
```

State:

```text
left pointer or queue front
current right event
window contains events with timestamp >= current_time - window_size
```

Array version:

```python
left = 0

for right, event in enumerate(events):
    while events[left]["time"] < event["time"] - window_size:
        left += 1

    window_size_count = right - left + 1
```

Queue version:

```text
append current timestamp
popleft while expired
```

Critical assumption:

```text
events are sorted by timestamp
```

Data Engineering connection:

```text
Streaming metrics, request counters, event-time windows, watermark calculations.
```


## 63. Data Engineering Custom Problem: Count Events in Last N Seconds

Problem:

```text
Given events sorted by event_time, return count of events in the last window_seconds for each event.
Window is inclusive: [event_time - window_seconds, event_time].
```

Pattern:

```text
Time-based sliding window with left pointer
```

Code:

```python
def counts_in_recent_window(events, window_seconds):
    left = 0
    result = []

    for right, event in enumerate(events):
        current_time = event["event_time"]
        lower_bound = current_time - window_seconds

        while left <= right and events[left]["event_time"] < lower_bound:
            left += 1

        result.append(right - left + 1)

    return result
```

Complexity:

```text
Time: O(n)
Space: O(n) for result
```

Follow-ups:

```text
What if events are out of order?
What if window is half-open?
What if event_time is datetime?
```

Expected:

```text
Sort or buffer events first; define boundary rule; normalize timestamps.
```


## 64. Data Engineering Custom Problem: Longest High-Quality Data Window

Problem:

```text
Given non-negative data quality issue counts per partition, find longest contiguous window with total issues <= max_issues.
```

Pattern:

```text
Variable sliding window with non-negative values
```

Code:

```python
def longest_high_quality_window(issue_counts, max_issues):
    left = 0
    total_issues = 0
    best = 0

    for right, issues in enumerate(issue_counts):
        total_issues += issues

        while total_issues > max_issues:
            total_issues -= issue_counts[left]
            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Follow-ups:

```text
Return indices.
What if issue corrections can be negative?
What if partitions are dates with gaps?
```


## 65. Data Engineering Custom Problem: Source Target Sorted Diff

Problem:

```text
Given sorted source records and target records by primary key, return keys:
- only in source
- only in target
- in both
Assume unique keys.
```

Pattern:

```text
Two pointers over sorted lists
```

Code:

```python
def source_target_sorted_diff(source_keys, target_keys):
    i = 0
    j = 0
    only_source = []
    only_target = []
    both = []

    while i < len(source_keys) and j < len(target_keys):
        if source_keys[i] == target_keys[j]:
            both.append(source_keys[i])
            i += 1
            j += 1
        elif source_keys[i] < target_keys[j]:
            only_source.append(source_keys[i])
            i += 1
        else:
            only_target.append(target_keys[j])
            j += 1

    only_source.extend(source_keys[i:])
    only_target.extend(target_keys[j:])

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

Follow-ups:

```text
Handle duplicates.
Compare full rows when keys match.
Inputs too large for memory.
```

Expected:

```text
For large sorted files, stream both inputs and emit diff incrementally.
```


## 66. Pattern: Merge Two Sorted Arrays

Use two pointers from end when merging into first array in-place.

Why from end:

```text
Avoid overwriting unprocessed values in nums1.
```

Template:

```text
i = m - 1
j = n - 1
write = m + n - 1

place larger of nums1[i] and nums2[j] at nums1[write]
move pointer
```

Data Engineering connection:

```text
Merge sorted chunks or sorted exports, conceptually similar to merge phase of external sort.
```


## 67. Problem: Merge Sorted Array

LeetCode:

```text
88. Merge Sorted Array
Difficulty: Easy
Pattern: Two pointers from end
```

Code:

```python
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    write = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1

        write -= 1
```

Complexity:

```text
Time: O(m + n)
Space: O(1)
```

Common mistake:

```text
Merging from front and overwriting unprocessed values in nums1.
```

Data Engineering connection:

```text
Merge sorted in-memory chunks.
```


## 68. Pattern: Sessionization with Sliding Window

Sessionization often uses ordered events.

Common rule:

```text
A new session starts if gap between consecutive events is greater than threshold.
```

This is pointer/scan-based.

Sliding-window variation:

```text
Find longest event sequence where event_time[right] - event_time[left] <= session_limit.
```

Use when:

```text
events are sorted by user and time
need consecutive session windows
```

Data Engineering connection:

```text
User sessionization, event grouping, clickstream processing.
```


## 69. Data Engineering Custom Problem: Longest Session Duration Window

Problem:

```text
Given sorted event times for one user, find maximum number of events within any session_limit seconds.
Window condition:
event_times[right] - event_times[left] <= session_limit
```

Pattern:

```text
Variable sliding window over timestamps
```

Code:

```python
def max_events_within_session_limit(event_times, session_limit):
    left = 0
    best = 0

    for right, current_time in enumerate(event_times):
        while current_time - event_times[left] > session_limit:
            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Follow-ups:

```text
Handle multiple users.
Events not sorted.
Return actual window.
```

Expected:

```text
Group by user_id, sort each user's events by time, then apply sliding window per user.
```


## 70. Pattern Classification Drill

Classify each prompt.

```text
1. Pair sum in sorted array.
2. Longest substring without repeating characters.
3. Maximum average of K consecutive values.
4. Minimum subarray length with sum >= target, positive nums.
5. Count subarrays with sum K, nums may be negative.
6. Remove duplicates from sorted array in-place.
7. Move zeros to end preserving order.
8. Compare sorted source and target IDs.
9. Find all anagram start positions.
10. Find minimum window containing all required chars.
11. Longest session with at most K event types.
12. Sliding window maximum.
13. Top K frequent values.
14. Search insert position in sorted array.
15. Merge two sorted arrays in-place.
16. 3Sum unique triplets.
17. Container with most water.
18. Count event windows with exactly K event types.
19. Recent events in last N seconds, sorted timestamps.
20. Longest success streak allowing K failures.
```

Expected patterns:

```text
1. two pointers
2. sliding window + set/map
3. fixed-size sliding window
4. variable sliding window
5. prefix sum + hash map, not standard sliding window
6. read/write pointer
7. read/write pointer
8. two sorted list pointers
9. fixed window + frequency map
10. variable window + frequency map
11. at most K distinct sliding window
12. monotonic deque, not basic sliding window
13. heap/hash map, not two pointers
14. binary search
15. two pointers from end
16. sort + two pointers
17. two pointers
18. atMost(K) - atMost(K-1)
19. time-based sliding window
20. variable sliding window
```

Passing standard:

```text
18/20 correct before timed mocks.
```


## 71. High-ROI LeetCode List

Practice these first.

| No. | Title | Difficulty | Pattern |
|---:|---|---|---|
| 167 | Two Sum II | Medium | Sorted two pointers |
| 125 | Valid Palindrome | Easy | Two pointers |
| 680 | Valid Palindrome II | Easy | Two pointers with one deletion |
| 26 | Remove Duplicates from Sorted Array | Easy | Read/write pointer |
| 27 | Remove Element | Easy | Read/write pointer |
| 283 | Move Zeroes | Easy | Read/write pointer |
| 88 | Merge Sorted Array | Easy | Two pointers from end |
| 15 | 3Sum | Medium | Sort + two pointers |
| 16 | 3Sum Closest | Medium | Sort + two pointers |
| 11 | Container With Most Water | Medium | Two pointers |
| 42 | Trapping Rain Water | Hard | Two pointers |
| 643 | Maximum Average Subarray I | Easy | Fixed sliding window |
| 567 | Permutation in String | Medium | Fixed window + frequency |
| 438 | Find All Anagrams in a String | Medium | Fixed window + frequency |
| 3 | Longest Substring Without Repeating Characters | Medium | Variable window |
| 340 | Longest Substring with At Most K Distinct | Medium | Variable window + map |
| 904 | Fruit Into Baskets | Medium | At most 2 distinct |
| 209 | Minimum Size Subarray Sum | Medium | Variable window, positives |
| 76 | Minimum Window Substring | Hard | Variable window + counts |
| 992 | Subarrays with K Different Integers | Hard | exactly K via atMost |
| 1004 | Max Consecutive Ones III | Medium | Sliding window with flips |
| 424 | Longest Repeating Character Replacement | Medium | Sliding window + max freq |
| 713 | Subarray Product Less Than K | Medium | Sliding window product |
| 141 | Linked List Cycle | Easy | Fast/slow |
| 876 | Middle of the Linked List | Easy | Fast/slow |


## 72. Practice Ladder

### Level 1: Basic two pointers

```text
Valid Palindrome
Two Sum II
Remove Duplicates
Remove Element
Move Zeroes
Merge Sorted Array
```

Exit:

```text
Candidate can move pointers safely and explain O(n).
```

### Level 2: Sort + two pointers

```text
3Sum
3Sum Closest
Container With Most Water
Source-target sorted diff custom
```

Exit:

```text
Candidate handles duplicates and sorted pointer movement.
```

### Level 3: Fixed sliding window

```text
Maximum Average Subarray
Permutation in String
Find All Anagrams
Rolling K-run error sum custom
```

Exit:

```text
Candidate handles fixed size and frequency windows.
```

### Level 4: Variable sliding window

```text
Longest Substring Without Repeating
At Most K Distinct
Fruit Into Baskets
Minimum Size Subarray Sum
Max Consecutive Ones III
```

Exit:

```text
Candidate knows when to shrink and when to update answer.
```

### Level 5: Advanced sliding window

```text
Minimum Window Substring
Exactly K Distinct
Longest Repeating Character Replacement
Subarray Product Less Than K
Time-based event windows
```

Exit:

```text
Candidate handles frequency maps, exactly-K counting, and event-time logic.
```


## 73. 7-Day Two Pointers / Sliding Window Plan

### Day 1: Two pointer basics

Problems:

```text
Valid Palindrome
Two Sum II
Remove Duplicates
Move Zeroes
```

Focus:

```text
left/right movement
read/write compaction
edge cases
```

### Day 2: Sorted comparison

Problems:

```text
Merge Sorted Array
Intersection sorted variant
Reconcile sorted IDs custom
Source-target sorted diff custom
```

Focus:

```text
two sorted lists
merge-like scan
duplicates
```

### Day 3: Sort + pair/triplet

Problems:

```text
3Sum
3Sum Closest
Container With Most Water
```

Focus:

```text
duplicate skipping
pointer movement proof
```

### Day 4: Fixed windows

Problems:

```text
Maximum Average Subarray
Permutation in String
Find All Anagrams
Rolling K-run error sum custom
```

Focus:

```text
fixed window length
frequency map
window add/remove
```

### Day 5: Variable longest windows

Problems:

```text
Longest Substring Without Repeating
At Most K Distinct
Fruit Into Baskets
Max Consecutive Ones III
```

Focus:

```text
valid window invariant
frequency map cleanup
best length update
```

### Day 6: Variable shortest/counting windows

Problems:

```text
Minimum Size Subarray Sum
Minimum Window Substring
Exactly K Distinct
Subarray Product Less Than K
```

Focus:

```text
shrink while valid
atMost trick
positive-number assumption
```

### Day 7: Data Engineering mock and repair

Tasks:

```text
Run Mock Set 3.
Review mistakes.
Repair weakest pattern.
Update progress.
```


## 74. 30-Day Two Pointers / Sliding Window Plan

### Week 1: Basic pointer movement

Focus:

```text
palindrome
sorted pair sum
read/write pointer
merge sorted arrays
```

Problems:

```text
125, 167, 26, 27, 283, 88
```

Exit:

```text
Candidate can solve easy pointer problems under 15 minutes.
```

### Week 2: Sorting + two pointers

Focus:

```text
3Sum
duplicates
container proof
sorted reconciliation
```

Problems:

```text
15, 16, 11, 42, custom sorted diff
```

Exit:

```text
Candidate can justify pointer movement and duplicate skipping.
```

### Week 3: Sliding windows

Focus:

```text
fixed windows
variable windows
frequency maps
positive sums
```

Problems:

```text
643, 567, 438, 3, 340, 904, 209, 1004
```

Exit:

```text
Candidate can write add/shrink/update logic correctly.
```

### Week 4: Advanced windows and DE

Focus:

```text
minimum window
exactly K
time-based windows
session windows
mock interviews
```

Problems:

```text
76, 992, 424, 713, custom DE event/session/window problems
```

Exit:

```text
Average mock score >= 4/5.
```


## 75. Mock Set 1: Beginner

Problems:

```text
1. Valid Palindrome
2. Two Sum II
3. Remove Duplicates from Sorted Array
4. Move Zeroes
5. Maximum Average Subarray I
```

Expected skills:

```text
left/right pointers
read/write pointer
fixed-size window
O(n) scan
edge cases
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains pointer movement clearly.
```


## 76. Mock Set 2: Core Medium

Problems:

```text
1. 3Sum
2. Container With Most Water
3. Longest Substring Without Repeating Characters
4. Minimum Size Subarray Sum
5. Permutation in String
```

Expected skills:

```text
sort + two pointers
movement proof
variable window
fixed frequency window
positive-number sum logic
```

Passing standard:

```text
Average score >= 4/5.
Candidate handles duplicates and window boundaries.
```


## 77. Mock Set 3: Data Engineering Flavor

Problems:

```text
1. Reconcile sorted source and target IDs.
2. Longest session with at most K event types.
3. Shortest error window with total errors >= threshold.
4. Count events in last N seconds.
5. Smallest log segment with required event types.
```

Expected skills:

```text
sorted two-list scan
frequency window
positive sliding sum
time-based window
minimum window frequency map
Data Engineering boundary handling
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains sortedness, timestamp boundary, and invalid input risks.
```


## 78. Mock Set 4: Strong Candidate

Problems:

```text
1. Minimum Window Substring
2. Subarrays with K Different Integers
3. Trapping Rain Water
4. Longest Repeating Character Replacement
5. 3Sum Closest
```

Expected skills:

```text
advanced frequency windows
atMost trick
advanced two-pointer proof
max frequency window
duplicate and boundary discipline
```

Passing standard:

```text
Average score >= 4/5.
Candidate handles follow-ups under pressure.
```


## 79. Timed Drill Protocol

Use this timing protocol.

### Easy two-pointer/window problem

```text
10-15 minutes
```

### Medium two-pointer/window problem

```text
25-35 minutes
```

### Hard sliding-window problem

```text
40-45 minutes
```

Per problem:

```text
Minute 0-3:
Clarify sortedness, contiguity, and constraints.

Minute 3-6:
Choose pointer/window pattern.

Minute 6-9:
Define pointer meaning and movement/shrink condition.

Minute 9-25:
Code.

Minute 25-30:
Dry run edge case.

Minute 30-35:
Complexity and Data Engineering connection.
```

If candidate cannot explain pointer movement:

```text
Stop and switch to weakness-repair-mode.md.
```


## 80. Review Checklist

Review solutions using:

```text
1. Did candidate identify contiguous vs non-contiguous?
2. Did candidate identify sorted vs unsorted?
3. Did candidate choose correct pointer/window pattern?
4. Did candidate define what left and right mean?
5. Did candidate define state inside window?
6. Did candidate explain pointer movement safety?
7. Did candidate handle duplicates?
8. Did candidate handle k = 0 or k > n?
9. Did candidate update answer in correct place?
10. Did candidate shrink with while when needed?
11. Did candidate avoid sliding window when negatives break it?
12. Did candidate clean up zero counts in maps?
13. Did candidate handle timestamp boundaries for DE problems?
14. Did candidate explain time complexity?
15. Did candidate connect to Data Engineering?
```

Verdict examples:

```text
Correct idea but wrong answer update location.
Correct window but missing zero-count deletion.
Wrong use of sliding window because negatives are allowed.
Good LeetCode answer but weak timestamp boundary handling.
Correct two-pointer scan but duplicate handling missing.
Interview-ready.
Strong.
```


## 81. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Cannot choose two pointers vs hash map | Pattern classification drills |
| Moves wrong pointer | Sorted movement proof drills |
| Loses original index after sorting | Sort-with-index repair |
| Duplicate handling weak | 3Sum duplicate drills |
| Off-by-one window length | Fixed-window boundary drills |
| Shrink logic weak | Variable-window invariant drills |
| Uses if instead of while | Shrink-until-valid drills |
| Negative numbers issue | Positive vs negative sum drills |
| Frequency map zero-count bug | Window map cleanup drills |
| Exactly K confusion | atMost(K) - atMost(K-1) drills |
| Minimum window confusion | have/need drills |
| Time window boundary bug | Inclusive/exclusive event window drills |
| No DE connection | Sorted reconciliation/session/window custom drills |

If weakness repeats:

```text
Use weakness-repair-mode.md.
```


## 82. Communication Scripts

### Sorted two pointers script

```text
Because the array is sorted, if the current sum is too small I move the left pointer right to increase it. If the sum is too large I move the right pointer left to decrease it.
```

### Read/write pointer script

```text
The read pointer scans every element, and the write pointer marks where the next kept element should be placed.
```

### Fixed window script

```text
The window size is exactly K, so I add the new right element and remove the element that falls out when the window grows beyond K.
```

### Variable window script

```text
I expand the right pointer to include new items, and while the window is invalid, I shrink from the left until it becomes valid again.
```

### Minimum window script

```text
When the window becomes valid, I record the answer first, then shrink from the left to find a smaller valid window.
```

### Positive-sum warning script

```text
This sliding-window sum approach is valid because the values are non-negative. If negative values were allowed, I would switch to prefix-sum based techniques.
```

### Data Engineering script

```text
This maps to comparing sorted source-target IDs, finding session windows, counting recent events, or finding the smallest log segment containing required event types.
```


## 83. Candidate Self-Review Questions

After every problem, candidate should answer:

```text
1. Is this contiguous?
2. Is the input sorted?
3. Do I need to sort first?
4. Do I need original indices?
5. What do left and right mean?
6. What state is inside the window?
7. When do I expand?
8. When do I shrink?
9. When do I update the answer?
10. Are duplicates important?
11. Are negative numbers allowed?
12. What edge case can break this?
13. What is time complexity?
14. What is space complexity?
15. What Data Engineering scenario uses this pattern?
```

If candidate cannot answer these:

```text
The problem is not fully learned.
```


## 84. Maintenance Drills

After completing two pointers and sliding window, maintain skill with:

```text
1 two-pointer sorted problem per week
1 read/write pointer problem per week
1 fixed-size window problem per week
1 variable-size window problem per week
1 frequency-window problem every 2 weeks
1 Data Engineering custom window problem per week
1 mixed mock every 2 weeks
```

Maintenance rotation:

```text
Week 1: sorted two pointers + read/write
Week 2: fixed window + frequency window
Week 3: variable window + minimum window
Week 4: time-based DE window + mixed mock
```

If score drops below 4:

```text
Run weakness-repair-mode.md for failed pattern.
```


## 85. Progress Tracking Template

Use this progress format.

```text
# Two Pointers and Sliding Window Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Pattern | Difficulty | Score | Time | Mistake | Next Action

## Pattern Scores

Opposite two pointers:
Fast/slow pointers:
Read/write pointer:
Two sorted lists:
Sort + two pointers:
Duplicate handling:
Fixed-size window:
Variable longest window:
Variable shortest window:
Frequency window:
Minimum window:
Exactly K via atMost:
Time-based window:
Positive-sum window:
Data Engineering sorted reconciliation:
Data Engineering event/session windows:

## Repeated Mistakes

-

## Repair Items

-

## Next Practice

Today:
This week:
Next mock:
```


## 86. Final Exit Test

Candidate passes two pointers and sliding window when they can solve:

```text
1. Two Sum II
2. Valid Palindrome
3. Valid Palindrome II
4. Remove Duplicates from Sorted Array
5. Remove Element
6. Move Zeroes
7. Merge Sorted Array
8. 3Sum
9. 3Sum Closest
10. Container With Most Water
11. Trapping Rain Water
12. Maximum Average Subarray I
13. Permutation in String
14. Find All Anagrams in a String
15. Longest Substring Without Repeating Characters
16. At Most K Distinct
17. Minimum Size Subarray Sum
18. Minimum Window Substring
19. Subarrays with K Different Integers
20. Max Consecutive Ones III
21. Longest Repeating Character Replacement
22. Subarray Product Less Than K
23. Data Engineering: source-target sorted diff
24. Data Engineering: longest session with K event types
25. Data Engineering: shortest error window
26. Data Engineering: count events in last N seconds
27. Data Engineering: smallest log segment with required events
```

Passing standard:

```text
Average score >= 4/5.
No wrong pointer movement.
No duplicate handling miss on 3Sum.
No fixed/variable window confusion.
No sliding-window misuse with negative numbers.
No frequency map cleanup bug.
Can explain Data Engineering relevance.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles timestamp boundaries, exactly-K counting, and minimum-window follow-ups under pressure.
```


## 87. Final Summary

Two pointers and sliding window are essential for Data Engineering interviews.

They map directly to:

```text
sorted reconciliation
deduplication
source-target comparison
session analysis
event windows
rolling metrics
recent event counts
contiguous log segments
transaction windows
fixed-size rolling calculations
variable constraint windows
```

The candidate must master:

```text
opposite-direction two pointers
fast/slow pointers
read/write pointer
two sorted list comparison
sort + two pointers
duplicate skipping
fixed-size sliding window
variable-size sliding window
frequency maps in windows
minimum window substring
exactly K via atMost
time-based windows
positive-number limitations
Data Engineering custom applications
```

The mentor must be strict:

```text
No pointer movement explanation → not interview-ready.
No window invariant → not interview-ready.
Wrong shrink condition → not interview-ready.
Sliding window with invalid negative-number assumption → not interview-ready.
Only sample passes → not interview-ready.
```

The goal is not to memorize templates.

The goal is to understand how ordered pointer movement and incremental window state eliminate unnecessary nested loops.


## 88. Problem Card Appendix

### Card 1: Two Sum II

LeetCode:

```text
167. Two Sum II
Difficulty: Medium
```

Primary pattern:

```text
Sorted two pointers
```

Core idea:

```text
Move left/right based on sum.
```

Data Engineering connection:

```text
Match sorted reconciliation amounts.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Valid Palindrome

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
Compare normalized ends.
```

Data Engineering connection:

```text
Normalize and compare tokens.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Valid Palindrome II

LeetCode:

```text
680. Valid Palindrome II
Difficulty: Easy
```

Primary pattern:

```text
Two pointers with one deletion
```

Core idea:

```text
Try skipping either mismatch side.
```

Data Engineering connection:

```text
Tolerant string comparison.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Remove Duplicates from Sorted Array

LeetCode:

```text
26. Remove Duplicates from Sorted Array
Difficulty: Easy
```

Primary pattern:

```text
Read/write pointer
```

Core idea:

```text
Write unique values forward.
```

Data Engineering connection:

```text
Deduplicate sorted IDs.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Remove Element

LeetCode:

```text
27. Remove Element
Difficulty: Easy
```

Primary pattern:

```text
Read/write pointer
```

Core idea:

```text
Write kept values forward.
```

Data Engineering connection:

```text
Compact valid records.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Move Zeroes

LeetCode:

```text
283. Move Zeroes
Difficulty: Easy
```

Primary pattern:

```text
Read/write pointer
```

Core idea:

```text
Move non-zero values forward.
```

Data Engineering connection:

```text
Move valid metrics forward.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Merge Sorted Array

LeetCode:

```text
88. Merge Sorted Array
Difficulty: Easy
```

Primary pattern:

```text
Two pointers from end
```

Core idea:

```text
Merge without overwriting.
```

Data Engineering connection:

```text
Merge sorted chunks.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: 3Sum

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
Fix one value, find pair.
```

Data Engineering connection:

```text
Find transaction triplets.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: 3Sum Closest

LeetCode:

```text
16. 3Sum Closest
Difficulty: Medium
```

Primary pattern:

```text
Sort + two pointers
```

Core idea:

```text
Track closest sum.
```

Data Engineering connection:

```text
Closest reconciliation triplet.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Container With Most Water

LeetCode:

```text
11. Container With Most Water
Difficulty: Medium
```

Primary pattern:

```text
Two pointers
```

Core idea:

```text
Move smaller boundary.
```

Data Engineering connection:

```text
Pointer movement proof.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Trapping Rain Water

LeetCode:

```text
42. Trapping Rain Water
Difficulty: Hard
```

Primary pattern:

```text
Two pointers
```

Core idea:

```text
Use left/right max boundaries.
```

Data Engineering connection:

```text
Advanced boundary scan.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Maximum Average Subarray I

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
Rolling K-size sum.
```

Data Engineering connection:

```text
Max average latency over K runs.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Permutation in String

LeetCode:

```text
567. Permutation in String
Difficulty: Medium
```

Primary pattern:

```text
Fixed window + counts
```

Core idea:

```text
Compare pattern counts.
```

Data Engineering connection:

```text
Fixed event pattern match.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Find All Anagrams

LeetCode:

```text
438. Find All Anagrams
Difficulty: Medium
```

Primary pattern:

```text
Fixed window + counts
```

Core idea:

```text
Return all matching starts.
```

Data Engineering connection:

```text
Find event-pattern positions.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Longest Substring Without Repeating

LeetCode:

```text
3. Longest Substring Without Repeating
Difficulty: Medium
```

Primary pattern:

```text
Variable window
```

Core idea:

```text
Keep unique window.
```

Data Engineering connection:

```text
Longest sequence without repeated event type.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: At Most K Distinct

LeetCode:

```text
340. At Most K Distinct
Difficulty: Medium
```

Primary pattern:

```text
Variable window + map
```

Core idea:

```text
Shrink when distinct > K.
```

Data Engineering connection:

```text
Longest session with K event types.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Fruit Into Baskets

LeetCode:

```text
904. Fruit Into Baskets
Difficulty: Medium
```

Primary pattern:

```text
At most 2 distinct
```

Core idea:

```text
Same as K=2 distinct.
```

Data Engineering connection:

```text
At most two event categories.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
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
Shortest positive-sum window
```

Core idea:

```text
Shrink while sum >= target.
```

Data Engineering connection:

```text
Shortest error threshold window.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Minimum Window Substring

LeetCode:

```text
76. Minimum Window Substring
Difficulty: Hard
```

Primary pattern:

```text
Minimum frequency window
```

Core idea:

```text
have/need counts.
```

Data Engineering connection:

```text
Smallest log segment.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Subarrays with K Different Integers

LeetCode:

```text
992. Subarrays with K Different Integers
Difficulty: Hard
```

Primary pattern:

```text
exactly K via atMost
```

Core idea:

```text
atMost(K)-atMost(K-1).
```

Data Engineering connection:

```text
Count windows with exactly K event types.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 21: Max Consecutive Ones III

LeetCode:

```text
1004. Max Consecutive Ones III
Difficulty: Medium
```

Primary pattern:

```text
Window with flips
```

Core idea:

```text
Keep zeros <= K.
```

Data Engineering connection:

```text
Longest success streak with K failures.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 22: Longest Repeating Character Replacement

LeetCode:

```text
424. Longest Repeating Character Replacement
Difficulty: Medium
```

Primary pattern:

```text
Window + max frequency
```

Core idea:

```text
Window length - max_count <= K.
```

Data Engineering connection:

```text
Normalize event sequence.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 23: Subarray Product Less Than K

LeetCode:

```text
713. Subarray Product Less Than K
Difficulty: Medium
```

Primary pattern:

```text
Product window
```

Core idea:

```text
Positive product shrink.
```

Data Engineering connection:

```text
Risk-score product windows.
```

Candidate must be able to explain:

```text
1. Why two pointers or sliding window applies.
2. What each pointer means.
3. What state is tracked.
4. Pointer movement or shrink condition.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 89. Data Engineering Custom Problem Card Appendix

### Custom Card 1: Match Debit Credit Amounts

Pattern:

```text
two pointers across sorted arrays
```

Task:

```text
Find one pair matching reconciliation target.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 2: Reconcile Sorted IDs

Pattern:

```text
two sorted list comparison
```

Task:

```text
Find matched, missing, and extra IDs.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 3: Source Target Sorted Diff

Pattern:

```text
two sorted list comparison
```

Task:

```text
Find only-source, only-target, both.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 4: Compact Valid Records

Pattern:

```text
read/write pointer
```

Task:

```text
Move valid records to front in-place.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 5: Rolling K-Run Error Sum

Pattern:

```text
fixed-size sliding window
```

Task:

```text
Find max total errors over K runs.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 6: Longest Session with K Event Types

Pattern:

```text
at most K distinct
```

Task:

```text
Find longest session with limited event variety.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 7: Shortest Error Window

Pattern:

```text
positive-sum variable window
```

Task:

```text
Find shortest window reaching error threshold.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 8: Smallest Log Segment

Pattern:

```text
minimum window with counts
```

Task:

```text
Find smallest segment containing required events.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 9: Exactly K Event Types

Pattern:

```text
atMost(K)-atMost(K-1)
```

Task:

```text
Count windows with exact event-type count.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 10: Longest Success Streak

Pattern:

```text
window with K flips
```

Task:

```text
Allow K failed runs inside success streak.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 11: Count Events in Last N Seconds

Pattern:

```text
time-based sliding window
```

Task:

```text
Count recent events per event.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 12: Longest Session Duration Window

Pattern:

```text
timestamp window
```

Task:

```text
Max events within session duration.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 13: High-Quality Data Window

Pattern:

```text
non-negative sum window
```

Task:

```text
Longest window under issue limit.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 14: Recent Request Window

Pattern:

```text
queue/window
```

Task:

```text
Count requests in recent window.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 15: Fixed Event Pattern

Pattern:

```text
fixed frequency window
```

Task:

```text
Find required event multiset in fixed length.
```

Minimum expected answer:

```text
1. Define sortedness or contiguity.
2. Define pointer/window state.
3. Handle invalid or boundary cases.
4. Explain time and space complexity.
5. Explain production risk if ordering/window assumptions are wrong.
```

Passing score:

```text
4/5 or higher.
```


## 90. Drill Appendix

### Drill 1: Pointer Movement

Task:

```text
Dry run Two Sum II, Container With Most Water, and 3Sum pointer movement.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Read/Write Compaction

Task:

```text
Solve Remove Duplicates, Remove Element, Move Zeroes, and Compact Valid Records.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Sorted Reconciliation

Task:

```text
Compare sorted source and target IDs with and without duplicates.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Duplicate Skipping

Task:

```text
Solve 3Sum and explain every duplicate skip.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Fixed Window

Task:

```text
Solve Maximum Average, K-run error sum, and fixed event pattern.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: Frequency Fixed Window

Task:

```text
Solve Permutation in String and Find All Anagrams.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Variable Longest Window

Task:

```text
Solve Longest Substring, At Most K Distinct, and Max Consecutive Ones III.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Variable Shortest Window

Task:

```text
Solve Minimum Size Subarray Sum and Shortest Error Window.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Minimum Window

Task:

```text
Solve Minimum Window Substring and Smallest Log Segment.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Exactly K

Task:

```text
Solve Subarrays with K Different and exact K event types.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Time-Based Window

Task:

```text
Count events in last N seconds and session duration window.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Positive vs Negative

Task:

```text
Classify which sum-window problems break with negative numbers.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Data Engineering Mock

Task:

```text
Run sorted diff, session K types, shortest error window, smallest log segment.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Complexity Drill

Task:

```text
Explain why nested while sliding window is still O(n).
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Pattern Classification

Task:

```text
Classify 20 prompts before coding.
```

Minimum passing answer:

```text
1. State the pattern.
2. Define pointer/window state.
3. Explain pointer movement or shrink condition.
4. Write clean Python.
5. Dry run boundary cases.
6. Explain time and space complexity.
7. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 91. Quick Reference Cards

### Quick Card 1: Two pointers

Summary:

```text
Use when sorted order or symmetric scan allows safe pointer movement.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 2: Read/write pointer

Summary:

```text
Read scans all items; write stores kept items.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 3: Fixed window

Summary:

```text
Exactly K length; add right and remove item leaving window.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 4: Variable window

Summary:

```text
Expand right, shrink left until valid.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 5: Longest valid window

Summary:

```text
Shrink while invalid, then update best.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 6: Shortest valid window

Summary:

```text
While valid, update best then shrink.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 7: Frequency map

Summary:

```text
Delete zero-count keys when distinct count matters.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 8: Exactly K

Summary:

```text
Count atMost(K) minus atMost(K-1).
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 9: Positive sum window

Summary:

```text
Requires non-negative values for standard shrink logic.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 10: Minimum window

Summary:

```text
Track have/need and required counts.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 11: Sorted reconciliation

Summary:

```text
Advance pointer with smaller current key.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 12: 3Sum

Summary:

```text
Sort, fix one value, two-sum the rest, skip duplicates.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 13: Time window

Summary:

```text
Requires events sorted by timestamp.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 14: Data windows

Summary:

```text
Clarify inclusive/exclusive boundaries.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 15: Complexity

Summary:

```text
Each pointer moves forward at most n times, so O(n).
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```
