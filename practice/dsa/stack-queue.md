# Stack and Queue Practice Guide

Generated: 2026-06-06

This practice guide is part of **Data Engineering Sensei**.

Path:

```text
data-engineering-sensei/practice/dsa/stack-queue.md
```

This guide teaches and drills **stack, queue, deque, monotonic stack, and monotonic queue patterns for Data Engineering interviews**.

This is not a generic data-structures document. It is an interview-focused guide for Data Engineering candidates who need to solve parsing, validation, ordering, buffering, streaming, undo/rollback, scheduling, and sliding-window problems.

Stack and queue patterns are high-ROI because they appear in:

- coding interviews
- log parsing
- path normalization
- expression evaluation
- bracket validation
- nested string decoding
- undo/rollback logic
- parsing nested JSON-like structures
- monotonic next-greater/next-smaller problems
- sliding-window maximum/minimum
- streaming request counters
- fixed-size event buffers
- job scheduling queues
- retry queues
- producer-consumer systems
- BFS traversal
- topological ordering
- task dependency processing
- pipeline rollback stacks
- batch processing queues
- stack-based error handling
- queue-based event ingestion
- latency-window monitoring

Use this guide with:

- `docs/dsa-for-data-engineers.md`
- `docs/python-interview-guide.md`
- `docs/leetcode-practice-map.md`
- `docs/data-engineering-fundamentals.md`
- `docs/etl-elt-pipelines-guide.md`
- `docs/orchestration-airflow-guide.md`
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
- `practice/dsa/bfs-dfs-basics.md`
- `practice/dsa/heap-top-k.md`
- `practice/dsa/intervals.md`
- `practice/dsa/sorting-binary-search.md`
- `progress/CANDIDATE_PROFILE.md`
- `progress/CURRENT_STATE.md`
- `progress/ROADMAP_PROGRESS.md`
- `progress/NEXT_STEPS.md`

Default interview standard if target companies are not provided:

```text
FAANG-style Data Engineering coding standard, scaled by candidate experience.
```


## 1. Purpose

The purpose of this guide is to make the candidate strong at stack and queue patterns.

The candidate should learn to answer:

```text
When should I use a stack?
When should I use a queue?
When should I use deque?
When do I need monotonic stack?
When do I need monotonic queue?
How do I validate nested structures?
How do I parse expressions?
How do I simulate undo/rollback?
How do I process events in FIFO order?
How do I maintain a sliding-window maximum?
How do I handle streaming request counts?
How do I implement queue using stacks?
How do I implement stack using queues?
How do I explain time and space complexity?
How does this map to Data Engineering work?
```

A candidate is interview-ready only when they can:

```text
identify stack/queue trigger clues
choose stack vs queue vs deque correctly
write clean Python list-stack code
write clean collections.deque queue code
avoid list.pop(0)
handle empty-stack and empty-queue cases
explain LIFO and FIFO
solve validation/parsing problems
solve monotonic stack problems
solve monotonic queue problems
solve streaming queue problems
dry run state changes
explain complexity
connect the pattern to Data Engineering scenarios
```


## 2. Why Stack and Queue Matter for Data Engineers

Stack and queue patterns are not only for software engineering roles.

Data Engineering examples:

```text
Validate parentheses in generated SQL or expression strings.
Normalize file paths from object storage.
Parse nested config expressions.
Evaluate postfix expressions in rule engines.
Decode encoded strings in metadata fields.
Track undo steps in pipeline rollback.
Maintain current active path while traversing directories.
Process events in FIFO ingestion order.
Buffer recent events in a sliding time window.
Maintain maximum latency in the last K events.
Track request count in the last 3000 ms.
Schedule jobs in queue order.
Use BFS queue for graph/data-lineage traversal.
Use stack for DFS/nested JSON traversal.
Use monotonic queue for rolling maximum.
Use monotonic stack for next greater metric analysis.
Use stack to resolve collisions/conflicts.
Use queue to model producer-consumer pipelines.
```

Interviewers ask stack/queue questions because they test whether the candidate can manage state carefully and process data in the correct order.


## 3. Core Mental Model: Stack

A stack is **Last In, First Out**.

```text
LIFO
```

The last item added is the first item removed.

Operations:

```text
push → add to top
pop → remove from top
peek/top → read top without removing
```

Python stack:

```python
stack = []
stack.append(value)   # push
value = stack.pop()   # pop
top = stack[-1]       # peek
```

Use stack when:

```text
need to remember previous items
need to match opening/closing symbols
need to undo last operation
need to process nested structures
need to backtrack
need next greater/smaller element
need maintain monotonic order
need resolve collisions with previous item
```

Interview line:

```text
A stack fits because the most recent unmatched item is the first one that should be resolved.
```


## 4. Core Mental Model: Queue

A queue is **First In, First Out**.

```text
FIFO
```

The first item added is the first item removed.

Use Python `collections.deque`.

```python
from collections import deque

queue = deque()
queue.append(value)      # enqueue
value = queue.popleft()  # dequeue
front = queue[0]         # peek front
```

Use queue when:

```text
process items in arrival order
BFS level-order traversal
task scheduling in FIFO order
event ingestion buffer
recent request counter
producer-consumer workflow
stream processing
```

Do not use:

```python
queue.pop(0)
```

Why:

```text
list.pop(0) is O(n)
deque.popleft() is O(1)
```

Interview line:

```text
A queue fits because items must be processed in the same order they arrive.
```


## 5. Core Mental Model: Deque

A deque is a double-ended queue.

It supports efficient operations at both ends:

```text
append right: O(1)
append left: O(1)
pop right: O(1)
pop left: O(1)
```

Python:

```python
from collections import deque

dq = deque()
dq.append(1)
dq.appendleft(0)
dq.pop()
dq.popleft()
```

Use deque when:

```text
need queue behavior
need sliding window
need monotonic queue
need add/remove from both ends
need recent events by time
```

Data Engineering examples:

```text
maintain recent request timestamps
maintain max latency in last K events
store active events in a time window
BFS over lineage graph
```

Interview line:

```text
I use deque because I need O(1) operations from both ends.
```


## 6. Stack vs Queue vs Deque Decision Table

| Requirement | Data Structure |
|---|---|
| Last added item should be handled first | Stack |
| First added item should be handled first | Queue |
| Need add/remove at both ends | Deque |
| Validate nested brackets | Stack |
| Undo last operation | Stack |
| BFS / level order | Queue |
| DFS iterative | Stack |
| Sliding window maximum | Monotonic deque |
| Next greater element | Monotonic stack |
| Recent request counter | Queue/deque |
| Normalize path | Stack |
| Parse nested expression | Stack |
| Process jobs in arrival order | Queue |
| Priority-based scheduling | Heap, not normal queue |
| Need top K | Heap, not stack/queue |
| Need sorted lookup | Binary search, not stack/queue |

Strict rule:

```text
Do not force stack/queue where hash map, heap, or binary search is the real pattern.
```


## 7. Standard Answer Framework

Use this framework for every stack/queue problem:

```text
1. Restate the problem.
2. Clarify input and output.
3. Identify order requirement:
   - LIFO
   - FIFO
   - both ends
   - monotonic order
4. Choose data structure:
   - stack
   - queue
   - deque
   - monotonic stack
   - monotonic queue
5. Explain why that structure fits.
6. Define what each element in the structure stores.
7. Define push/pop conditions.
8. Write code.
9. Dry run state changes.
10. Explain edge cases.
11. Explain time complexity.
12. Explain space complexity.
13. Connect to Data Engineering scenario.
```

Short version:

```text
Structure:
Stores:
Push rule:
Pop rule:
Result:
Complexity:
```

Strict rule:

```text
No stack/queue code before explaining what the structure stores.
```


## 8. Scoring Rubric

Score each stack/queue attempt from 0 to 5.

### Score 0

No meaningful attempt.

### Score 1

Does not understand LIFO/FIFO or uses wrong structure.

### Score 2

Partial logic but missing empty checks, wrong order, or major edge cases.

### Score 3

Works for simple cases but weak on edge cases, state explanation, or complexity.

### Score 4

Interview-ready. Correct structure, clean code, edge cases, and complexity.

### Score 5

Strong. Handles follow-ups, monotonic variants, streaming cases, and Data Engineering connections.

Do not give 4+ if:

```text
candidate uses list.pop(0) for queue
candidate cannot explain stack vs queue
candidate forgets empty-stack check
candidate does not define what stack stores
candidate cannot dry run state
candidate confuses monotonic increasing/decreasing
candidate returns heap-like or sorted behavior from queue
candidate code only passes sample
candidate cannot explain O(n)
```


## 9. Complexity Rules

Common complexities:

```text
stack push/pop/peek: O(1)
queue append/popleft with deque: O(1)
deque append/pop both ends: O(1)
monotonic stack scan: O(n)
monotonic queue sliding window: O(n)
valid parentheses: O(n)
path simplification: O(n)
RPN evaluation: O(n)
BFS with queue: O(V + E)
```

Why monotonic stack/queue is O(n):

```text
Each element is pushed at most once and popped at most once.
```

Bad queue complexity:

```text
list.pop(0) is O(n)
```

Interview wording:

```text
Time is O(n) because every character/item is processed once, and each stack operation is O(1).
```

Space wording:

```text
Space is O(n) in the worst case when all items are stored in the stack/queue.
```


## 10. Edge Case Checklist

Stack edge cases:

```text
empty input
single item
empty stack pop
unmatched closing bracket
leftover opening bracket
nested structures
invalid token
negative numbers
multi-digit numbers
spaces
path with multiple slashes
path with ..
path going above root
very deep nesting
```

Queue edge cases:

```text
empty queue
one item
long stream
all events expired
time boundary exactly equals window limit
fixed-size window smaller than input
k = 0
k = 1
k > n
duplicate values
same priority/order
```

Monotonic edge cases:

```text
strict vs non-strict comparison
duplicates
all increasing
all decreasing
all equal
window expiration
returning values vs indices
circular array
```

Data Engineering-specific edge cases:

```text
invalid log line
malformed path
bad expression
missing event_time
out-of-order events
late event
duplicate event timestamp
empty batch
retry queue with no jobs
pipeline rollback with no completed steps
window boundary inclusive/exclusive
```


## 11. Pattern Map

Stack and queue patterns:

```text
1. Basic stack simulation
2. Bracket validation
3. Path simplification
4. Expression evaluation
5. Nested string decoding
6. Undo/rollback stack
7. Collision resolution
8. Monotonic stack: next greater
9. Monotonic stack: next smaller
10. Monotonic stack: histogram area
11. Min stack / auxiliary stack
12. Queue simulation
13. Moving average queue
14. Recent counter queue
15. Circular queue
16. Queue using stacks
17. Stack using queues
18. Monotonic queue: sliding window max
19. BFS queue
20. Producer-consumer queue
21. Topological queue
22. Time-window event buffer
23. Fixed-size buffer
24. Retry FIFO queue
25. Data pipeline rollback stack
```

Pattern selection:

```text
Need most recent unresolved item → stack.
Need arrival order → queue.
Need both ends / sliding window → deque.
Need next greater/smaller → monotonic stack.
Need max/min in sliding window → monotonic queue.
Need shortest steps / levels → BFS queue.
```


## 12. Common Mistakes

Common stack mistakes:

```text
Popping without checking stack is non-empty.
Not checking leftover stack at end.
Using stack when queue is required.
Forgetting to convert string number tokens to int.
Handling '-' incorrectly in RPN.
Not preserving nested state.
Not restoring previous state after decoding.
Wrong order after popping stack.
```

Common queue mistakes:

```text
Using list.pop(0).
Not removing expired events.
Using queue when priority queue is needed.
Not tracking window boundaries.
Not handling empty queue.
Not using indices in sliding-window maximum.
```

Common monotonic mistakes:

```text
Wrong comparison direction.
Forgetting each element can be popped only once.
Using values instead of indices when window expiration matters.
Not handling duplicates consistently.
Returning heap-like sorted result.
```

Strict feedback:

```text
This is not interview-ready. You used a list as a queue with pop(0), which changes the intended O(n) solution into O(n²).
```


## 13. Python Stack and Queue Tools

### Stack with list

```python
stack = []
stack.append(value)
value = stack.pop()
top = stack[-1]
```

### Queue with deque

```python
from collections import deque

queue = deque()
queue.append(value)
value = queue.popleft()
front = queue[0]
```

### Deque for sliding window

```python
from collections import deque

dq = deque()
dq.append(index)
dq.popleft()
dq[-1]
dq[0]
```

### Avoid

```python
list.pop(0)
```

### Why

```text
list.pop(0) shifts all remaining elements and costs O(n).
```

Interview line:

```text
In Python, list is fine for stack, but deque is the right tool for queue.
```


## 14. Pattern: Bracket Validation

Use stack when matching opening and closing symbols.

Trigger phrases:

```text
valid parentheses
balanced brackets
matching tags
nested delimiters
syntax validation
```

Algorithm:

```text
1. Push opening brackets.
2. On closing bracket:
   - stack must not be empty
   - top must match closing bracket
   - pop top
3. At end, stack must be empty.
```

Why stack:

```text
The most recent opening bracket must be closed first.
```

Data Engineering connection:

```text
Validate generated SQL fragments, JSON-like expressions, config templates, or formula strings.
```

Interview line:

```text
Stack works because nested structures must close in reverse order of opening.
```


## 15. Problem: Valid Parentheses

LeetCode:

```text
20. Valid Parentheses
Difficulty: Easy
Pattern: Stack
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

Edge cases:

```text
empty string
only opening brackets
only closing brackets
mismatched type
nested valid brackets
```

Data Engineering connection:

```text
Validate generated expressions or SQL-like syntax before execution.
```

Common mistake:

```text
Returning True before checking leftover opening brackets.
```


## 16. Data Engineering Custom Problem: Validate SQL Parentheses

Problem:

```text
Given a SQL expression string, validate only parentheses balance.
Ignore all non-parenthesis characters.
```

Pattern:

```text
Stack
```

Code:

```python
def validate_sql_parentheses(expression):
    stack = []

    for char in expression:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Follow-ups:

```text
Validate brackets [] and braces {} too.
Ignore parentheses inside quoted strings.
Return index of first error.
```

Expected:

```text
For quoted strings, track quote state before applying stack logic.
```


## 17. Pattern: Path Simplification

Use stack when normalizing paths.

Rules for Unix-style path:

```text
"." means current directory
".." means parent directory
empty parts from multiple slashes are ignored
normal directory names are pushed
```

Algorithm:

```text
1. Split by slash.
2. For each token:
   - ignore "" and "."
   - if "..", pop if possible
   - else push directory
3. Join stack with slashes.
```

Why stack:

```text
The last valid directory is the one removed by ..
```

Data Engineering connection:

```text
Normalize object storage paths or file paths before deduplication and processing.
```


## 18. Problem: Simplify Path

LeetCode:

```text
71. Simplify Path
Difficulty: Medium
Pattern: Stack
```

Code:

```python
def simplify_path(path):
    stack = []

    for part in path.split("/"):
        if part == "" or part == ".":
            continue

        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Edge cases:

```text
multiple slashes
path ending with slash
path going above root
current directory tokens
hidden file names like .config
```

Data Engineering connection:

```text
Normalize S3/GCS/ADLS-style paths before comparing file manifests.
```

Common mistake:

```text
Treating names like "...", ".config", or "file..txt" as special. Only exact "." and ".." are special.
```


## 19. Data Engineering Custom Problem: Normalize Object Storage Path

Problem:

```text
Normalize object storage paths by:
- removing duplicate slashes
- resolving .
- resolving ..
- preserving bucket prefix if provided
```

Simplified path-only code:

```python
def normalize_storage_path(path):
    stack = []

    for part in path.split("/"):
        if part == "" or part == ".":
            continue

        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/".join(stack)
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Follow-ups:

```text
How do you handle s3://bucket/path?
How do you prevent going above bucket root?
Should paths be case-sensitive?
```

Expected:

```text
Parse scheme/bucket separately, then normalize only the key/path portion.
```


## 20. Pattern: Expression Evaluation

Use stack when evaluating postfix or nested expressions.

Trigger phrases:

```text
reverse polish notation
postfix expression
evaluate tokens
operator applies to previous operands
calculator
```

Reverse Polish Notation:

```text
["2", "1", "+", "3", "*"]
means (2 + 1) * 3
```

Algorithm:

```text
1. Push numbers.
2. When operator appears, pop right operand then left operand.
3. Apply operator.
4. Push result.
5. Final stack top is answer.
```

Important:

```text
Order matters for subtraction and division.
```

Data Engineering connection:

```text
Evaluate simple rule-engine expressions or derived metric formulas.
```


## 21. Problem: Evaluate Reverse Polish Notation

LeetCode:

```text
150. Evaluate Reverse Polish Notation
Difficulty: Medium
Pattern: Stack
```

Code:

```python
def eval_rpn(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
            continue

        right = stack.pop()
        left = stack.pop()

        if token == "+":
            stack.append(left + right)
        elif token == "-":
            stack.append(left - right)
        elif token == "*":
            stack.append(left * right)
        else:
            stack.append(int(left / right))

    return stack[-1]
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Important:

```text
LeetCode division truncates toward zero. int(left / right) handles that in Python for this context.
```

Data Engineering connection:

```text
Evaluate metric expressions stored as postfix tokens in a lightweight rule engine.
```

Common mistakes:

```text
Popping operands in wrong order.
Using // for negative division, which floors instead of truncating toward zero.
```


## 22. Data Engineering Custom Problem: Evaluate Metric Formula

Problem:

```text
Given postfix tokens for a simple metric formula, evaluate it.
Tokens may include integers and + - * /.
Return None if formula is invalid.
```

Pattern:

```text
Stack expression evaluation
```

Code:

```python
def evaluate_metric_formula(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token not in operators:
            try:
                stack.append(int(token))
            except ValueError:
                return None
            continue

        if len(stack) < 2:
            return None

        right = stack.pop()
        left = stack.pop()

        if token == "+":
            stack.append(left + right)
        elif token == "-":
            stack.append(left - right)
        elif token == "*":
            stack.append(left * right)
        else:
            if right == 0:
                return None
            stack.append(int(left / right))

    if len(stack) != 1:
        return None

    return stack[0]
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Follow-ups:

```text
Support variables.
Support decimals.
Support infix expressions.
Return detailed error reason.
```


## 23. Pattern: Decode Nested String

Use stack for nested encoded strings.

Example:

```text
3[a2[c]] → accaccacc
```

State:

```text
current_number
current_string
stack of previous_string and repeat_count
```

Algorithm:

```text
When digit: build number.
When '[': push current string and repeat count; reset both.
When letter: append to current string.
When ']': pop previous state and combine.
```

Why stack:

```text
Nested encodings must resolve inside-out.
```

Data Engineering connection:

```text
Decode compact metadata strings or nested template expressions.
```


## 24. Problem: Decode String

LeetCode:

```text
394. Decode String
Difficulty: Medium
Pattern: Stack
```

Code:

```python
def decode_string(s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == "[":
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0
        elif char == "]":
            previous_string, repeat_count = stack.pop()
            current_string = previous_string + current_string * repeat_count
        else:
            current_string += char

    return current_string
```

Complexity:

```text
Time: O(output length)
Space: O(output length + nesting depth)
```

Edge cases:

```text
multi-digit repeat counts
nested brackets
plain characters
empty encoded section
```

Data Engineering connection:

```text
Decode compact field expressions or template metadata.
```

Common mistake:

```text
Not resetting current_number after '['.
```


## 25. Pattern: Min Stack / Auxiliary Stack

Use auxiliary stack when a stack must return minimum in O(1).

State:

```text
main stack stores values
min stack stores current minimum at each level or only new minima
```

Simpler robust version:

```text
Push value to main stack.
Push min(value, current_min) to min stack.
Pop both together.
```

Why:

```text
Each stack depth knows the minimum up to that depth.
```

Data Engineering connection:

```text
Maintain minimum metric in an undoable stack of operations or nested processing context.
```


## 26. Problem: Min Stack

LeetCode:

```text
155. Min Stack
Difficulty: Medium
Pattern: Stack + auxiliary min stack
```

Code:

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

Complexity:

```text
push: O(1)
pop: O(1)
top: O(1)
getMin: O(1)
space: O(n)
```

Common mistakes:

```text
Only storing one global minimum.
Not updating min when popping the minimum.
```

Data Engineering connection:

```text
Track minimum metric across nested processing states while allowing rollback.
```


## 27. Pattern: Collision Resolution with Stack

Use stack when current item may interact with the most recent unresolved previous item.

Trigger phrases:

```text
collisions
remove adjacent conflicts
resolve previous item
current cancels previous
```

Algorithm:

```text
For each item:
  while stack top conflicts with current:
    resolve conflict
  push current if it survives
```

Data Engineering examples:

```text
resolve add/delete operations
cancel adjacent inverse operations
resolve event corrections
collapse conflicting status transitions
```

Interview line:

```text
A stack works because only the most recent unresolved item can collide with the current item first.
```


## 28. Problem: Asteroid Collision

LeetCode:

```text
735. Asteroid Collision
Difficulty: Medium
Pattern: Stack collision resolution
```

Code:

```python
def asteroid_collision(asteroids):
    stack = []

    for asteroid in asteroids:
        alive = True

        while alive and asteroid < 0 and stack and stack[-1] > 0:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()

            alive = False

        if alive:
            stack.append(asteroid)

    return stack
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Resolve conflicting operations where the latest item can cancel or replace the previous unresolved operation.
```

Common mistake:

```text
Colliding asteroids only happen when previous moves right and current moves left.
```


## 29. Data Engineering Custom Problem: Resolve File Operations

Problem:

```text
Given operations for a file stream:
CREATE file
DELETE file

If a CREATE is immediately followed by DELETE for the same file before any other operation for that file, cancel both.
Return unresolved operations in order.
```

Pattern:

```text
Stack conflict resolution
```

Code:

```python
def resolve_file_operations(operations):
    stack = []

    for operation in operations:
        op_type = operation.get("op")
        file_name = operation.get("file")

        if (
            op_type == "DELETE"
            and stack
            and stack[-1].get("op") == "CREATE"
            and stack[-1].get("file") == file_name
        ):
            stack.pop()
        else:
            stack.append(operation)

    return stack
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Follow-ups:

```text
What if operations are not adjacent?
What if UPDATE is included?
What if same file has many operations?
```

Expected:

```text
For non-adjacent operations, use hash map state instead of only stack.
```


## 30. Pattern: Monotonic Stack

A monotonic stack keeps values in increasing or decreasing order.

Use it for:

```text
next greater element
next smaller element
previous greater element
previous smaller element
daily temperatures
stock span
largest rectangle in histogram
remove K digits
```

Two common forms:

### Monotonic decreasing stack

```text
Stack values decrease from bottom to top.
Useful for finding next greater element.
```

When current is greater than stack top:

```text
current is next greater for popped elements.
```

### Monotonic increasing stack

```text
Stack values increase from bottom to top.
Useful for finding next smaller element.
```

When current is smaller than stack top:

```text
current is next smaller for popped elements.
```

Interview line:

```text
The stack stores unresolved indices whose next greater/smaller answer has not been found yet.
```


## 31. Monotonic Stack Template: Next Greater

Template:

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # stores indices

    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            previous_index = stack.pop()
            result[previous_index] = value

        stack.append(i)

    return result
```

Why indices?

```text
Need to write answer at original position.
Need values for comparison.
Need support duplicates and positions.
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Why O(n):

```text
Each index is pushed once and popped once.
```

Data Engineering connection:

```text
For each day's metric, find next future day with higher value.
```


## 32. Problem: Next Greater Element I

LeetCode:

```text
496. Next Greater Element I
Difficulty: Easy
Pattern: Monotonic stack + hash map
```

Approach:

```text
Compute next greater for nums2.
Map value → next greater.
Return answers for nums1.
```

Code:

```python
def next_greater_element(nums1, nums2):
    next_greater = {}
    stack = []

    for value in nums2:
        while stack and stack[-1] < value:
            smaller = stack.pop()
            next_greater[smaller] = value

        stack.append(value)

    for value in stack:
        next_greater[value] = -1

    return [next_greater[value] for value in nums1]
```

Complexity:

```text
Time: O(n + m)
Space: O(n)
```

Data Engineering connection:

```text
For selected metrics, find next later metric value that exceeds current value.
```

Common mistake:

```text
Using nested loops and getting O(n²).
```


## 33. Problem: Next Greater Element II

LeetCode:

```text
503. Next Greater Element II
Difficulty: Medium
Pattern: Circular monotonic stack
```

Problem:

```text
Array is circular. Find next greater element for each position.
```

Code:

```python
def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        index = i % n

        while stack and nums[stack[-1]] < nums[index]:
            previous_index = stack.pop()
            result[previous_index] = nums[index]

        if i < n:
            stack.append(index)

    return result
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Analyze cyclic schedules or rotating metric windows.
```

Common mistake:

```text
Pushing indices during the second pass and creating duplicates.
```


## 34. Problem: Daily Temperatures

LeetCode:

```text
739. Daily Temperatures
Difficulty: Medium
Pattern: Monotonic decreasing stack
```

Problem:

```text
For each day, return number of days until a warmer temperature.
```

Code:

```python
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # indices with unresolved warmer day

    for i, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            previous_index = stack.pop()
            result[previous_index] = i - previous_index

        stack.append(i)

    return result
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
For each pipeline run, find how many runs until latency becomes higher, lower, or crosses a threshold.
```

Common mistake:

```text
Storing values instead of indices when distance is required.
```


## 35. Data Engineering Custom Problem: Next Higher Latency

Problem:

```text
Given pipeline run latencies in order, for each run return how many runs until a higher latency appears.
If none, return 0.
```

Pattern:

```text
Daily Temperatures-style monotonic stack
```

Code:

```python
def runs_until_higher_latency(latencies):
    result = [0] * len(latencies)
    stack = []

    for i, latency in enumerate(latencies):
        while stack and latencies[stack[-1]] < latency:
            previous = stack.pop()
            result[previous] = i - previous

        stack.append(i)

    return result
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Follow-ups:

```text
Find next lower latency.
Find next latency above threshold.
Return timestamp difference instead of index difference.
```


## 36. Pattern: Stock Span

Stock span asks:

```text
For each price, how many consecutive previous days have price <= current price?
```

Pattern:

```text
Monotonic decreasing stack storing (price, span).
```

When current price is greater than or equal to stack top:

```text
merge that previous span into current span
```

Data Engineering connection:

```text
For each metric value, count how many consecutive previous events were less than or equal to current metric.
```


## 37. Problem: Online Stock Span

LeetCode:

```text
901. Online Stock Span
Difficulty: Medium
Pattern: Monotonic stack
```

Code:

```python
class StockSpanner:
    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price):
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            previous_price, previous_span = self.stack.pop()
            span += previous_span

        self.stack.append((price, span))
        return span
```

Complexity:

```text
Amortized O(1) per next call
Space: O(n)
```

Why amortized O(1):

```text
Each price is pushed once and popped once across all calls.
```

Data Engineering connection:

```text
Streaming metric span: count consecutive previous runs with latency <= current latency.
```


## 38. Pattern: Largest Rectangle / Next Smaller

Largest rectangle in histogram uses monotonic increasing stack.

Core idea:

```text
When current height is smaller than stack top, current index is the right boundary for popped height.
Previous stack top after popping is the left boundary.
```

Use sentinel:

```text
append height 0 to flush stack
```

Data Engineering connection:

```text
Analyze widest continuous period where a metric stayed above a certain level.
```

Interview line:

```text
The stack stores bars in increasing height order. When a lower bar appears, it determines the right boundary for taller bars.
```


## 39. Problem: Largest Rectangle in Histogram

LeetCode:

```text
84. Largest Rectangle in Histogram
Difficulty: Hard
Pattern: Monotonic increasing stack
```

Code:

```python
def largest_rectangle_area(heights):
    stack = []  # indices
    best = 0
    extended = heights + [0]

    for i, height in enumerate(extended):
        while stack and extended[stack[-1]] > height:
            popped_index = stack.pop()
            popped_height = extended[popped_index]

            left_boundary = stack[-1] if stack else -1
            width = i - left_boundary - 1
            best = max(best, popped_height * width)

        stack.append(i)

    return best
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Find largest continuous workload block where minimum capacity/metric supports area-like score.
```

Common mistakes:

```text
wrong width calculation
forgetting sentinel 0
using values instead of indices
```


## 40. Pattern: Remove K Digits

This is a monotonic increasing stack problem.

Goal:

```text
Remove k digits to make smallest possible number.
```

Greedy idea:

```text
When current digit is smaller than previous digit, remove previous digit if removals remain.
```

Stack maintains:

```text
digits in increasing order as much as possible
```

Data Engineering analogy:

```text
Greedily remove high-cost earlier items when a lower-cost later item can improve ordered sequence.
```


## 41. Problem: Remove K Digits

LeetCode:

```text
402. Remove K Digits
Difficulty: Medium
Pattern: Monotonic stack
```

Code:

```python
def remove_kdigits(num, k):
    stack = []

    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    result = "".join(stack).lstrip("0")

    return result if result else "0"
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Common mistakes:

```text
not removing remaining k digits
not stripping leading zeros
returning empty string instead of "0"
```

Data Engineering connection:

```text
Greedy stack optimization over ordered tokens.
```


## 42. Pattern: Basic Queue Simulation

Use queue when processing in arrival order.

Trigger phrases:

```text
first come first served
process in order
recent requests
moving average
streaming window
FIFO buffer
```

Python:

```python
from collections import deque
```

Template:

```python
from collections import deque

queue = deque()

for item in items:
    queue.append(item)

    while should_remove(queue[0]):
        queue.popleft()
```

Data Engineering examples:

```text
process ingestion events in arrival order
track recent requests
maintain fixed-size rolling average
process retry queue FIFO
```

Interview line:

```text
Queue fits because the oldest item is the first one that should be removed or processed.
```


## 43. Problem: Number of Recent Calls

LeetCode:

```text
933. Number of Recent Calls
Difficulty: Easy
Pattern: Queue / sliding time window
```

Problem:

```text
Return number of pings in last 3000 ms.
```

Code:

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)

        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)
```

Complexity:

```text
Amortized O(1) per ping
Space: O(w), requests in active window
```

Data Engineering connection:

```text
Track number of requests/events in a recent time window.
```

Boundary:

```text
Window is [t - 3000, t], inclusive in this problem.
```

Common mistake:

```text
Removing t - 3000 itself even though it should be included.
```


## 44. Data Engineering Custom Problem: Recent Event Counter

Problem:

```text
Events arrive in non-decreasing event_time order.
For each event_time, return number of events in last window_ms milliseconds.
Window is inclusive: [event_time - window_ms, event_time].
```

Pattern:

```text
Queue / deque time window
```

Code:

```python
from collections import deque

class RecentEventCounter:
    def __init__(self, window_ms):
        self.window_ms = window_ms
        self.events = deque()

    def add_event(self, event_time):
        self.events.append(event_time)

        lower_bound = event_time - self.window_ms

        while self.events and self.events[0] < lower_bound:
            self.events.popleft()

        return len(self.events)
```

Complexity:

```text
Amortized O(1) per event
Space: O(active window size)
```

Follow-ups:

```text
What if events arrive out of order?
What if timestamps are not monotonic?
What if window is half-open?
```

Expected:

```text
This queue approach depends on non-decreasing timestamps. Out-of-order events need sorting, watermarking, or a different data structure.
```


## 45. Pattern: Moving Average Queue

Use queue for fixed-size rolling averages.

State:

```text
queue of recent values
running_sum
max_size
```

Algorithm:

```text
add new value
add to running sum
if queue too large, pop oldest and subtract
average = running_sum / len(queue)
```

Data Engineering connection:

```text
Rolling average latency, rows processed, error rate, or throughput over last N events.
```

Interview line:

```text
A queue is useful because when the window exceeds size K, the oldest value is the one to remove.
```


## 46. Problem: Moving Average from Data Stream

LeetCode:

```text
346. Moving Average from Data Stream
Difficulty: Easy
Pattern: Queue + running sum
```

Code:

```python
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.values = deque()
        self.total = 0

    def next(self, val):
        self.values.append(val)
        self.total += val

        if len(self.values) > self.size:
            removed = self.values.popleft()
            self.total -= removed

        return self.total / len(self.values)
```

Complexity:

```text
next: O(1)
space: O(size)
```

Data Engineering connection:

```text
Maintain moving average of pipeline latency over recent N runs.
```

Common mistake:

```text
Recomputing sum over the queue every time, causing O(k) per call.
```


## 47. Data Engineering Custom Problem: Rolling Average Latency

Problem:

```text
Build a class that tracks average latency over the last K pipeline runs.
```

Code:

```python
from collections import deque

class RollingAverageLatency:
    def __init__(self, k):
        self.k = k
        self.latencies = deque()
        self.total = 0.0

    def add_latency(self, latency):
        self.latencies.append(latency)
        self.total += latency

        if len(self.latencies) > self.k:
            removed = self.latencies.popleft()
            self.total -= removed

        return self.total / len(self.latencies)
```

Complexity:

```text
add_latency: O(1)
space: O(k)
```

Follow-ups:

```text
Ignore invalid latency.
Track p95 instead of average.
Track time-based window instead of count-based window.
```

Expected:

```text
p95 needs a different data structure or approximate streaming algorithm.
```


## 48. Pattern: Monotonic Queue

A monotonic queue is a deque that keeps candidates in sorted order.

Use for:

```text
sliding window maximum
sliding window minimum
max/min in recent K items
rolling max latency
```

For sliding maximum:

```text
deque stores indices
values at indices are decreasing
front is max candidate
```

Algorithm for each index i:

```text
1. Remove indices that are outside window.
2. Remove indices from back while their value <= current value.
3. Append current index.
4. Front is max for current window.
```

Why store indices:

```text
Need to know if an item expired from the window.
```

Complexity:

```text
O(n)
```

Because:

```text
Each index is added once and removed once.
```


## 49. Problem: Sliding Window Maximum

LeetCode:

```text
239. Sliding Window Maximum
Difficulty: Hard
Pattern: Monotonic deque
```

Code:

```python
from collections import deque

def max_sliding_window(nums, k):
    if not nums or k <= 0:
        return []

    dq = deque()
    result = []

    for i, value in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= value:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Data Engineering connection:

```text
Track maximum latency or error count over the last K events.
```

Common mistakes:

```text
using values instead of indices
forgetting to remove expired indices
wrong comparison direction
```


## 50. Data Engineering Custom Problem: Rolling Max Latency

Problem:

```text
Given latencies and window size k, return maximum latency for each window.
```

Pattern:

```text
Monotonic queue
```

Code:

```python
from collections import deque

def rolling_max_latency(latencies, k):
    if k <= 0:
        return []

    dq = deque()
    result = []

    for i, latency in enumerate(latencies):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and latencies[dq[-1]] <= latency:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(latencies[dq[0]])

    return result
```

Complexity:

```text
Time: O(n)
Space: O(k)
```

Follow-ups:

```text
Return rolling minimum.
Use time-based window instead of count-based window.
Handle out-of-order events.
```

Expected:

```text
For time-based monotonic queue, store (timestamp, value) and expire by timestamp.
```


## 51. Pattern: Time-Based Monotonic Queue

Use when events have timestamps and you need max/min over recent time window.

Assumption:

```text
events arrive in non-decreasing timestamp order
```

For max:

```text
deque stores (timestamp, value)
values decrease from front to back
front is max
```

Algorithm:

```text
1. Expire old events from front by timestamp.
2. Remove smaller/equal values from back.
3. Append current event.
4. Front is max.
```

Data Engineering connection:

```text
Maximum error count, latency, or batch size in last N minutes.
```

Warning:

```text
Out-of-order events break simple deque logic.
```


## 52. Data Engineering Custom Problem: Max Error Count in Recent Window

Problem:

```text
Events arrive as (timestamp, error_count), timestamp non-decreasing.
Return max error_count in the last window_seconds after each event.
Window is [timestamp - window_seconds, timestamp].
```

Code:

```python
from collections import deque

class RecentMaxErrorCounter:
    def __init__(self, window_seconds):
        self.window_seconds = window_seconds
        self.dq = deque()

    def add(self, timestamp, error_count):
        lower_bound = timestamp - self.window_seconds

        while self.dq and self.dq[0][0] < lower_bound:
            self.dq.popleft()

        while self.dq and self.dq[-1][1] <= error_count:
            self.dq.pop()

        self.dq.append((timestamp, error_count))

        return self.dq[0][1]
```

Complexity:

```text
Amortized O(1) per event
Space: O(active window size)
```

Follow-ups:

```text
What if timestamps are out of order?
What if window is half-open?
What if you need average and max?
```

Expected:

```text
Out-of-order events require buffering/sorting/watermarking or a different structure.
```


## 53. Pattern: Queue Using Stacks

This tests understanding of stack and queue behavior.

Goal:

```text
Implement FIFO queue using LIFO stacks.
```

Use two stacks:

```text
input_stack for pushes
output_stack for pops/peeks
```

When output_stack is empty:

```text
move all items from input_stack to output_stack
```

This reverses order and exposes oldest item on top.

Amortized complexity:

```text
push: O(1)
pop: amortized O(1)
peek: amortized O(1)
```

Why amortized O(1):

```text
Each element moves from input_stack to output_stack at most once.
```


## 54. Problem: Implement Queue using Stacks

LeetCode:

```text
232. Implement Queue using Stacks
Difficulty: Easy
Pattern: Two stacks
```

Code:

```python
class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        self.input_stack.append(x)

    def _move_if_needed(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

    def pop(self):
        self._move_if_needed()
        return self.output_stack.pop()

    def peek(self):
        self._move_if_needed()
        return self.output_stack[-1]

    def empty(self):
        return not self.input_stack and not self.output_stack
```

Complexity:

```text
push: O(1)
pop: amortized O(1)
peek: amortized O(1)
empty: O(1)
space: O(n)
```

Data Engineering connection:

```text
Understand how buffering layers can reverse/reorder data when transferred between structures.
```

Common mistake:

```text
Moving elements on every push, causing unnecessary O(n) operations.
```


## 55. Pattern: Stack Using Queues

Goal:

```text
Implement LIFO stack using FIFO queues.
```

One common method:

```text
Use one queue.
On push, append new item, then rotate previous items behind it.
```

Then:

```text
front of queue is stack top
```

Complexity:

```text
push: O(n)
pop: O(1)
top: O(1)
```

Alternative:

```text
Use two queues.
```

Interview line:

```text
To simulate stack behavior with queue, I need to make the newest item come to the front.
```


## 56. Problem: Implement Stack using Queues

LeetCode:

```text
225. Implement Stack using Queues
Difficulty: Easy
Pattern: Queue rotation
```

Code:

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0
```

Complexity:

```text
push: O(n)
pop: O(1)
top: O(1)
empty: O(1)
space: O(n)
```

Data Engineering connection:

```text
Understand order transformations when using FIFO systems to simulate LIFO behavior.
```


## 57. Pattern: Circular Queue

Circular queue uses fixed-size storage and wraps around.

Use when:

```text
fixed capacity buffer
streaming ring buffer
memory-limited queue
recent N items
```

State:

```text
array
front index
size
capacity
```

Rear index:

```text
(front + size) % capacity
```

Operations:

```text
enQueue
deQueue
Front
Rear
isEmpty
isFull
```

Data Engineering connection:

```text
Fixed-size in-memory event buffer or recent batch cache.
```


## 58. Problem: Design Circular Queue

LeetCode:

```text
622. Design Circular Queue
Difficulty: Medium
Pattern: Circular buffer
```

Code:

```python
class MyCircularQueue:
    def __init__(self, k):
        self.data = [0] * k
        self.capacity = k
        self.front_index = 0
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False

        rear_index = (self.front_index + self.size) % self.capacity
        self.data[rear_index] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.front_index = (self.front_index + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1

        return self.data[self.front_index]

    def Rear(self):
        if self.isEmpty():
            return -1

        rear_index = (self.front_index + self.size - 1) % self.capacity
        return self.data[rear_index]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
```

Complexity:

```text
All operations: O(1)
Space: O(k)
```

Data Engineering connection:

```text
Fixed-capacity event buffer for recent records.
```

Common mistakes:

```text
wrong rear index
not wrapping with modulo
confusing empty and full states
```


## 59. Data Engineering Custom Problem: Fixed-Size Event Buffer

Problem:

```text
Design a fixed-size buffer that keeps the last K event IDs.
When full, adding a new event evicts the oldest.
```

Pattern:

```text
Circular buffer or deque with maxlen
```

Simple Python code:

```python
from collections import deque

class FixedEventBuffer:
    def __init__(self, k):
        self.events = deque(maxlen=k)

    def add(self, event_id):
        self.events.append(event_id)

    def get_events(self):
        return list(self.events)
```

Manual circular-buffer discussion:

```text
Use array + front + size if interviewer wants implementation without deque maxlen.
```

Complexity:

```text
add: O(1)
get_events: O(k)
space: O(k)
```

Follow-ups:

```text
Return events in newest-first order.
Track event payload too.
Reject duplicates.
```


## 60. Pattern: BFS Queue

BFS uses queue.

This is covered deeply in `practice/dsa/bfs-dfs-basics.md`, but queue basics matter here.

BFS template:

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited
```

Why queue:

```text
BFS processes nodes level by level in discovery order.
```

Data Engineering connection:

```text
Traverse downstream lineage level by level or compute shortest hops in dependency graph.
```


## 61. Data Engineering Custom Problem: Process Jobs FIFO

Problem:

```text
Given jobs in arrival order, process them FIFO.
Return processing order.
Skip invalid jobs missing job_id.
```

Pattern:

```text
Queue
```

Code:

```python
from collections import deque

def process_jobs_fifo(jobs):
    queue = deque()
    invalid_count = 0

    for job in jobs:
        if job.get("job_id") is None:
            invalid_count += 1
            continue

        queue.append(job)

    order = []

    while queue:
        job = queue.popleft()
        order.append(job["job_id"])

    return {
        "processing_order": order,
        "invalid_count": invalid_count,
    }
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Follow-up:

```text
What if jobs have priority?
```

Expected:

```text
Use heap/priority queue, not FIFO queue.
```


## 62. Pattern: Undo / Rollback Stack

Use stack when actions must be undone in reverse order.

Examples:

```text
pipeline rollback
transaction rollback
directory traversal
browser history
undo edit operations
nested processing context
```

Algorithm:

```text
When action succeeds, push rollback action.
If failure occurs, pop and execute rollback actions.
```

Data Engineering connection:

```text
If pipeline step 4 fails, rollback steps 3, 2, 1 in reverse order.
```

Interview line:

```text
Rollback is naturally LIFO because the most recent successful operation should be undone first.
```


## 63. Data Engineering Custom Problem: Pipeline Rollback Order

Problem:

```text
Given completed pipeline steps in execution order, return rollback order.
```

Pattern:

```text
Stack
```

Code:

```python
def rollback_order(completed_steps):
    stack = []

    for step in completed_steps:
        stack.append(step)

    order = []

    while stack:
        order.append(stack.pop())

    return order
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Follow-ups:

```text
What if some steps are not rollbackable?
What if rollback can fail?
What if dependencies are not linear?
```

Expected:

```text
For dependency graphs, use topological order/reverse topological order instead of simple stack.
```


## 64. Pattern: Browser History / Navigation Stack

Browser history uses stacks.

Typical design:

```text
back_stack
forward_stack
current_page
```

When visiting new page:

```text
push current to back_stack
clear forward_stack
set current
```

When back:

```text
push current to forward_stack
pop from back_stack into current
```

When forward:

```text
push current to back_stack
pop from forward_stack into current
```

Data Engineering connection:

```text
Navigation through lineage exploration or UI state history.
```


## 65. Problem: Design Browser History

LeetCode:

```text
1472. Design Browser History
Difficulty: Medium
Pattern: Two stacks or list with pointer
```

Two-stack code:

```python
class BrowserHistory:
    def __init__(self, homepage):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self, steps):
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1

        return self.current

    def forward(self, steps):
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1

        return self.current
```

Complexity:

```text
visit: O(1)
back: O(steps)
forward: O(steps)
space: O(n)
```

Data Engineering connection:

```text
Track user navigation through lineage graph or dashboard drilldowns.
```


## 66. Pattern: Backspace / Edit Simulation

Use stack to simulate edits.

Trigger phrases:

```text
backspace
undo character
remove previous
process edit stream
```

Algorithm:

```text
For each char:
  if normal char: push
  if backspace: pop if possible
```

Data Engineering connection:

```text
Process correction markers in streamed text fields or command logs.
```


## 67. Problem: Backspace String Compare

LeetCode:

```text
844. Backspace String Compare
Difficulty: Easy
Pattern: Stack or two pointers
```

Stack code:

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

Data Engineering connection:

```text
Compare corrected field values after applying delete markers.
```

Follow-up:

```text
Can you do O(1) extra space?
```

Expected:

```text
Use reverse two-pointer simulation.
```


## 68. Pattern: Remove Adjacent Duplicates

Use stack when adjacent items cancel.

Trigger phrases:

```text
remove adjacent duplicates
collapse repeated adjacent characters
cancel pairs
```

Algorithm:

```text
For each char:
  if stack top equals char: pop
  else: push char
```

Data Engineering connection:

```text
Collapse repeated status toggles or adjacent duplicate tokens.
```


## 69. Problem: Remove All Adjacent Duplicates In String

LeetCode:

```text
1047. Remove All Adjacent Duplicates In String
Difficulty: Easy
Pattern: Stack
```

Code:

```python
def remove_duplicates(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Collapse adjacent duplicate markers in a cleaned string field.
```


## 70. Problem: Remove All Adjacent Duplicates in String II

LeetCode:

```text
1209. Remove All Adjacent Duplicates in String II
Difficulty: Medium
Pattern: Stack with counts
```

Code:

```python
def remove_duplicates(s, k):
    stack = []  # [char, count]

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])

        if stack[-1][1] == k:
            stack.pop()

    result = []

    for char, count in stack:
        result.append(char * count)

    return "".join(result)
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

Data Engineering connection:

```text
Remove repeated adjacent tokens when a threshold count is reached.
```

Common mistake:

```text
Using repeated string replacement, causing inefficient behavior and missed cascading removals.
```


## 71. Pattern Classification Drill

Classify each prompt.

```text
1. Validate balanced parentheses.
2. Normalize /a/./b/../c path.
3. Evaluate postfix expression tokens.
4. Decode 3[a2[c]].
5. Return minimum from stack in O(1).
6. Resolve asteroid collisions.
7. Find next greater value for each element.
8. Find days until warmer temperature.
9. Find largest rectangle in histogram.
10. Track recent requests in last 3000 ms.
11. Maintain moving average of last K values.
12. Return max of every sliding window of size K.
13. Implement queue using two stacks.
14. Implement stack using one queue.
15. Design circular fixed-size event buffer.
16. Process jobs in arrival order.
17. Rollback completed pipeline steps.
18. Compare strings with backspace markers.
19. Remove adjacent duplicates.
20. Traverse graph level by level.
```

Expected patterns:

```text
1. stack
2. stack
3. stack
4. stack
5. auxiliary stack
6. stack collision
7. monotonic stack
8. monotonic stack
9. monotonic increasing stack
10. queue/deque time window
11. queue + running sum
12. monotonic queue/deque
13. two stacks
14. queue rotation
15. circular queue / deque maxlen
16. FIFO queue
17. rollback stack
18. stack or two pointers
19. stack
20. BFS queue
```

Passing standard:

```text
18/20 correct before timed stack/queue mocks.
```


## 72. High-ROI LeetCode List

Practice these first.

| No. | Title | Difficulty | Pattern |
|---:|---|---|---|
| 20 | Valid Parentheses | Easy | Stack |
| 71 | Simplify Path | Medium | Stack |
| 150 | Evaluate Reverse Polish Notation | Medium | Stack |
| 394 | Decode String | Medium | Stack |
| 155 | Min Stack | Medium | Auxiliary stack |
| 735 | Asteroid Collision | Medium | Stack collision |
| 496 | Next Greater Element I | Easy | Monotonic stack |
| 503 | Next Greater Element II | Medium | Circular monotonic stack |
| 739 | Daily Temperatures | Medium | Monotonic stack |
| 901 | Online Stock Span | Medium | Monotonic stack |
| 84 | Largest Rectangle in Histogram | Hard | Monotonic stack |
| 402 | Remove K Digits | Medium | Monotonic stack |
| 933 | Number of Recent Calls | Easy | Queue |
| 346 | Moving Average from Data Stream | Easy | Queue + running sum |
| 239 | Sliding Window Maximum | Hard | Monotonic deque |
| 232 | Implement Queue using Stacks | Easy | Two stacks |
| 225 | Implement Stack using Queues | Easy | Queue rotation |
| 622 | Design Circular Queue | Medium | Circular queue |
| 1472 | Design Browser History | Medium | Two stacks |
| 844 | Backspace String Compare | Easy | Stack |
| 1047 | Remove Adjacent Duplicates | Easy | Stack |
| 1209 | Remove Adjacent Duplicates II | Medium | Stack with counts |


## 73. Practice Ladder

### Level 1: Basic stack

```text
Valid Parentheses
Backspace String Compare
Remove Adjacent Duplicates
Simplify Path
```

Exit:

```text
Candidate can push/pop safely and handle empty stack.
```

### Level 2: Stack parsing and design

```text
Evaluate Reverse Polish Notation
Decode String
Min Stack
Browser History
```

Exit:

```text
Candidate can manage stack state and design stack-backed APIs.
```

### Level 3: Queue and deque basics

```text
Recent Counter
Moving Average
Implement Queue using Stacks
Implement Stack using Queues
Design Circular Queue
```

Exit:

```text
Candidate uses deque correctly and avoids pop(0).
```

### Level 4: Monotonic stack

```text
Next Greater Element
Daily Temperatures
Online Stock Span
Asteroid Collision
Remove K Digits
```

Exit:

```text
Candidate can explain unresolved candidates and amortized O(n).
```

### Level 5: Monotonic queue and advanced

```text
Sliding Window Maximum
Largest Rectangle in Histogram
Rolling Max Latency custom
Time-Based Monotonic Queue custom
Pipeline rollback custom
```

Exit:

```text
Candidate handles indices, expiration, and advanced stack boundaries.
```


## 74. 7-Day Stack/Queue Plan

### Day 1: Stack fundamentals

Problems:

```text
Valid Parentheses
Backspace String Compare
Remove Adjacent Duplicates
Validate SQL Parentheses custom
```

Focus:

```text
push/pop
empty checks
leftover stack
```

### Day 2: Stack parsing

Problems:

```text
Simplify Path
Evaluate RPN
Decode String
Normalize Object Storage Path custom
```

Focus:

```text
nested state
token processing
path stack
```

### Day 3: Queue basics

Problems:

```text
Recent Counter
Moving Average
Process Jobs FIFO custom
Fixed Event Buffer custom
```

Focus:

```text
deque
popleft
running sum
time window
```

### Day 4: Stack/queue design

Problems:

```text
Min Stack
Queue using Stacks
Stack using Queues
Circular Queue
Browser History
```

Focus:

```text
API design
amortized complexity
state invariants
```

### Day 5: Monotonic stack

Problems:

```text
Next Greater Element I
Next Greater Element II
Daily Temperatures
Online Stock Span
```

Focus:

```text
unresolved indices
next greater
amortized O(n)
```

### Day 6: Advanced stack/deque

Problems:

```text
Asteroid Collision
Remove K Digits
Largest Rectangle in Histogram
Sliding Window Maximum
```

Focus:

```text
collision resolution
monotonic direction
width calculation
window expiration
```

### Day 7: Mock and repair

Tasks:

```text
Run Mock Set 2 or 3.
Review mistakes.
Repair weakest stack/queue pattern.
Update progress.
```


## 75. 30-Day Stack/Queue Plan

### Week 1: Basic stack and queue

Focus:

```text
LIFO
FIFO
deque
empty checks
path/expression basics
```

Problems:

```text
20, 71, 150, 933, 346, 844, 1047
```

Exit:

```text
Candidate can solve simple stack/queue problems under 15 minutes.
```

### Week 2: Design and parsing

Focus:

```text
Min Stack
queue using stacks
stack using queues
circular queue
decode string
browser history
```

Problems:

```text
155, 232, 225, 622, 394, 1472
```

Exit:

```text
Candidate explains amortized behavior and state design.
```

### Week 3: Monotonic stack

Focus:

```text
next greater
daily temperatures
stock span
collisions
remove K digits
histogram
```

Problems:

```text
496, 503, 739, 901, 735, 402, 84
```

Exit:

```text
Candidate can explain monotonic stack direction and O(n).
```

### Week 4: Monotonic queue and Data Engineering

Focus:

```text
sliding window maximum
recent event windows
rolling max metrics
pipeline rollback
job queues
mock interviews
```

Problems:

```text
239, custom rolling max, recent event counter, pipeline rollback, FIFO jobs
```

Exit:

```text
Average mock score >= 4/5.
```


## 76. Mock Set 1: Beginner

Problems:

```text
1. Valid Parentheses
2. Simplify Path
3. Backspace String Compare
4. Recent Counter
5. Moving Average from Data Stream
```

Expected skills:

```text
basic stack
path stack
edit simulation
queue time window
running sum
```

Passing standard:

```text
Average score >= 4/5.
No missing empty-stack checks.
No list.pop(0).
```


## 77. Mock Set 2: Core Medium

Problems:

```text
1. Evaluate Reverse Polish Notation
2. Decode String
3. Min Stack
4. Daily Temperatures
5. Queue using Stacks
```

Expected skills:

```text
expression stack
nested state
auxiliary stack
monotonic stack
amortized queue design
```

Passing standard:

```text
Average score >= 4/5.
Candidate explains stack state clearly.
```


## 78. Mock Set 3: Data Engineering Flavor

Problems:

```text
1. Validate SQL parentheses.
2. Normalize object storage path.
3. Recent event counter.
4. Rolling max latency.
5. Pipeline rollback order.
```

Expected skills:

```text
stack validation
path stack
time-window queue
monotonic queue
rollback stack
DE edge-case explanation
```

Passing standard:

```text
Average score >= 4/5.
Candidate connects each solution to practical pipeline behavior.
```


## 79. Mock Set 4: Strong Candidate

Problems:

```text
1. Sliding Window Maximum
2. Largest Rectangle in Histogram
3. Remove K Digits
4. Asteroid Collision
5. Online Stock Span
```

Expected skills:

```text
monotonic queue
monotonic stack
greedy stack
collision resolution
amortized analysis
```

Passing standard:

```text
Average score >= 4/5.
Candidate handles follow-ups and dry-runs advanced state changes.
```


## 80. Timed Drill Protocol

Use this timing protocol.

### Easy stack/queue problem

```text
10-15 minutes
```

### Medium stack/queue problem

```text
25-35 minutes
```

### Hard monotonic stack/queue problem

```text
35-45 minutes
```

Per problem:

```text
Minute 0-3:
Clarify input, output, and order requirement.

Minute 3-6:
Choose stack, queue, deque, monotonic stack, or monotonic queue.

Minute 6-9:
Define what the structure stores and pop condition.

Minute 9-25:
Code.

Minute 25-30:
Dry run state changes.

Minute 30-35:
Complexity and Data Engineering connection.
```

If candidate cannot explain what the stack/deque stores:

```text
Stop and switch to modes/weakness-repair-mode.md.
```


## 81. Review Checklist

Review stack/queue solutions using:

```text
1. Did candidate identify LIFO/FIFO/deque requirement?
2. Did candidate choose correct structure?
3. Did candidate define what the structure stores?
4. Did candidate define push condition?
5. Did candidate define pop condition?
6. Did candidate check empty structure before pop/peek?
7. Did candidate avoid list.pop(0)?
8. Did candidate handle duplicates if monotonic?
9. Did candidate store indices when needed?
10. Did candidate expire old window indices/events?
11. Did candidate explain amortized O(n) when relevant?
12. Did candidate handle edge cases?
13. Did candidate dry run state?
14. Did candidate explain time complexity?
15. Did candidate connect to Data Engineering?
```

Verdict examples:

```text
Correct stack but missing leftover check.
Correct queue idea but inefficient pop(0).
Correct monotonic direction but stores values instead of indices.
Works on sample but fails duplicates.
Good LeetCode answer but weak DE boundary handling.
Interview-ready.
Strong.
```


## 82. Weakness Repair Map

Use this map when candidate fails.

| Weakness | Repair |
|---|---|
| Confuses stack and queue | LIFO/FIFO classification drills |
| Pops empty stack | Empty-state guard drills |
| Uses list.pop(0) | deque queue drills |
| Cannot parse nested state | Decode String dry-run drills |
| RPN operand order wrong | Expression evaluation drills |
| Path simplification weak | Token-based path stack drills |
| Monotonic direction wrong | Next greater vs next smaller contrast drills |
| Uses values instead of indices | Daily temperatures/window max drills |
| Window expiration bug | Monotonic queue index drills |
| Cannot explain amortized O(n) | Push-once-pop-once drills |
| Circular queue index bug | Modulo index drills |
| Queue using stacks confusion | Transfer-on-demand drills |
| No DE connection | Recent events/rollback/path custom drills |

If weakness repeats:

```text
Use modes/weakness-repair-mode.md.
```


## 83. Communication Scripts

### Stack script

```text
I use a stack because the most recent unresolved item must be handled first. I push opening/state items and pop when the matching closing/resolution appears.
```

### Queue script

```text
I use a queue because items must be processed in arrival order. In Python I use deque for O(1) popleft.
```

### Deque script

```text
I use deque because I need efficient operations at both ends, especially for sliding-window expiration and candidate maintenance.
```

### Monotonic stack script

```text
The stack stores unresolved indices. When the current value is greater than the value at the stack top, the current value becomes the next greater answer for that popped index.
```

### Monotonic queue script

```text
The deque stores indices of candidates in decreasing value order. The front is always the maximum for the current window, and expired indices are removed from the front.
```

### Data Engineering script

```text
This pattern maps to validating generated expressions, normalizing storage paths, tracking recent events, rolling max latency, or rolling back pipeline steps in reverse order.
```


## 84. Candidate Self-Review Questions

After every stack/queue problem, candidate should answer:

```text
1. Why stack, queue, or deque?
2. What does the structure store?
3. When do I push?
4. When do I pop?
5. What happens if structure is empty?
6. Do I need values or indices?
7. Is the order LIFO or FIFO?
8. If monotonic, increasing or decreasing?
9. If sliding window, how do I expire old items?
10. What is time complexity?
11. What is space complexity?
12. Why is amortized complexity O(n), if relevant?
13. What Data Engineering scenario uses this pattern?
```

If candidate cannot answer these:

```text
The problem is not fully learned.
```


## 85. Maintenance Drills

After completing stack/queue, maintain skill with:

```text
1 basic stack problem per week
1 queue/deque problem per week
1 monotonic stack problem per week
1 monotonic queue problem every 2 weeks
1 Data Engineering custom stack/queue problem per week
1 mixed mock every 2 weeks
```

Maintenance rotation:

```text
Week 1: validation + path stack
Week 2: queue windows + moving average
Week 3: monotonic stack + next greater
Week 4: monotonic queue + DE mock
```

If score drops below 4:

```text
Run modes/weakness-repair-mode.md for failed pattern.
```


## 86. Progress Tracking Template

Use this progress format.

```text
# Stack and Queue Progress

Last Updated:

## Current Level

Beginner / Intermediate / Advanced:

## Completed Problems

Date | Problem | Pattern | Difficulty | Score | Time | Mistake | Next Action

## Pattern Scores

Basic stack:
Bracket validation:
Path simplification:
Expression evaluation:
Nested decoding:
Min stack:
Collision stack:
Monotonic stack:
Histogram stack:
Basic queue:
Recent counter:
Moving average:
Queue using stacks:
Stack using queues:
Circular queue:
Monotonic queue:
Sliding window maximum:
Rollback stack:
Data Engineering custom:

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

Candidate passes stack/queue when they can solve:

```text
1. Valid Parentheses
2. Simplify Path
3. Evaluate Reverse Polish Notation
4. Decode String
5. Min Stack
6. Asteroid Collision
7. Next Greater Element I
8. Next Greater Element II
9. Daily Temperatures
10. Online Stock Span
11. Largest Rectangle in Histogram
12. Remove K Digits
13. Number of Recent Calls
14. Moving Average from Data Stream
15. Sliding Window Maximum
16. Implement Queue using Stacks
17. Implement Stack using Queues
18. Design Circular Queue
19. Data Engineering: validate SQL parentheses
20. Data Engineering: normalize object storage path
21. Data Engineering: recent event counter
22. Data Engineering: rolling max latency
23. Data Engineering: pipeline rollback order
```

Passing standard:

```text
Average score >= 4/5.
No stack/queue confusion.
No missing empty checks.
No list.pop(0).
No monotonic direction confusion.
No missing index usage for sliding windows.
Can explain Data Engineering relevance.
```

Strong standard:

```text
Average score >= 4.5/5.
Candidate handles advanced monotonic stack/queue follow-ups under pressure.
```


## 88. Final Summary

Stack and queue patterns are essential for Data Engineering interviews.

They map directly to:

```text
validation
parsing
path normalization
undo/rollback
stream buffers
event windows
moving averages
rolling maximums
FIFO processing
BFS traversal
dependency processing
pipeline rollback
recent request counts
```

The candidate must master:

```text
stack with list
queue with deque
deque for both ends
empty-state checks
LIFO vs FIFO
bracket validation
path stack
expression stack
nested decoding
auxiliary min stack
monotonic stack
monotonic queue
queue design
circular queue
streaming windows
amortized complexity
Data Engineering custom applications
```

The mentor must be strict:

```text
No structure explanation → not interview-ready.
No empty check → not interview-ready.
Using pop(0) for queue → not interview-ready.
Wrong monotonic direction → not interview-ready.
Only sample passes → not interview-ready.
```

The goal is not to memorize stack and queue syntax.

The goal is to understand order, state, and when the most recent or oldest item must be processed first.


## 89. Problem Card Appendix

### Card 1: Valid Parentheses

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
Validate generated expressions.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 2: Simplify Path

LeetCode:

```text
71. Simplify Path
Difficulty: Medium
```

Primary pattern:

```text
Stack
```

Core idea:

```text
Use stack of path parts.
```

Data Engineering connection:

```text
Normalize storage paths.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 3: Evaluate Reverse Polish Notation

LeetCode:

```text
150. Evaluate Reverse Polish Notation
Difficulty: Medium
```

Primary pattern:

```text
Stack
```

Core idea:

```text
Operators consume previous operands.
```

Data Engineering connection:

```text
Evaluate metric formulas.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 4: Decode String

LeetCode:

```text
394. Decode String
Difficulty: Medium
```

Primary pattern:

```text
Stack
```

Core idea:

```text
Store previous string and repeat count.
```

Data Engineering connection:

```text
Decode metadata templates.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 5: Min Stack

LeetCode:

```text
155. Min Stack
Difficulty: Medium
```

Primary pattern:

```text
Auxiliary stack
```

Core idea:

```text
Track current minimum at each depth.
```

Data Engineering connection:

```text
Track min metric in rollback context.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 6: Asteroid Collision

LeetCode:

```text
735. Asteroid Collision
Difficulty: Medium
```

Primary pattern:

```text
Collision stack
```

Core idea:

```text
Current item collides with previous unresolved item.
```

Data Engineering connection:

```text
Resolve operation conflicts.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 7: Next Greater Element I

LeetCode:

```text
496. Next Greater Element I
Difficulty: Easy
```

Primary pattern:

```text
Monotonic stack
```

Core idea:

```text
Map each value to next greater value.
```

Data Engineering connection:

```text
Next higher metric.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 8: Next Greater Element II

LeetCode:

```text
503. Next Greater Element II
Difficulty: Medium
```

Primary pattern:

```text
Circular monotonic stack
```

Core idea:

```text
Two-pass circular scan.
```

Data Engineering connection:

```text
Cyclic schedule metrics.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 9: Daily Temperatures

LeetCode:

```text
739. Daily Temperatures
Difficulty: Medium
```

Primary pattern:

```text
Monotonic stack
```

Core idea:

```text
Store unresolved indices.
```

Data Engineering connection:

```text
Runs until higher latency.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 10: Online Stock Span

LeetCode:

```text
901. Online Stock Span
Difficulty: Medium
```

Primary pattern:

```text
Monotonic stack
```

Core idea:

```text
Merge spans while previous <= current.
```

Data Engineering connection:

```text
Consecutive metric span.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 11: Largest Rectangle in Histogram

LeetCode:

```text
84. Largest Rectangle in Histogram
Difficulty: Hard
```

Primary pattern:

```text
Monotonic stack
```

Core idea:

```text
Lower bar determines right boundary.
```

Data Engineering connection:

```text
Largest continuous metric block.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 12: Remove K Digits

LeetCode:

```text
402. Remove K Digits
Difficulty: Medium
```

Primary pattern:

```text
Monotonic stack
```

Core idea:

```text
Remove larger previous digits greedily.
```

Data Engineering connection:

```text
Ordered greedy optimization.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 13: Number of Recent Calls

LeetCode:

```text
933. Number of Recent Calls
Difficulty: Easy
```

Primary pattern:

```text
Queue
```

Core idea:

```text
Keep timestamps in recent window.
```

Data Engineering connection:

```text
Recent event counter.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 14: Moving Average

LeetCode:

```text
346. Moving Average
Difficulty: Easy
```

Primary pattern:

```text
Queue + running sum
```

Core idea:

```text
Remove oldest when size exceeds K.
```

Data Engineering connection:

```text
Rolling average latency.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 15: Sliding Window Maximum

LeetCode:

```text
239. Sliding Window Maximum
Difficulty: Hard
```

Primary pattern:

```text
Monotonic deque
```

Core idea:

```text
Deque stores max candidates by index.
```

Data Engineering connection:

```text
Rolling max latency.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 16: Queue using Stacks

LeetCode:

```text
232. Queue using Stacks
Difficulty: Easy
```

Primary pattern:

```text
Two stacks
```

Core idea:

```text
Transfer only when output stack empty.
```

Data Engineering connection:

```text
Understand buffering order.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 17: Stack using Queues

LeetCode:

```text
225. Stack using Queues
Difficulty: Easy
```

Primary pattern:

```text
Queue rotation
```

Core idea:

```text
Rotate newest item to front.
```

Data Engineering connection:

```text
Order simulation.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 18: Design Circular Queue

LeetCode:

```text
622. Design Circular Queue
Difficulty: Medium
```

Primary pattern:

```text
Circular buffer
```

Core idea:

```text
Fixed-capacity queue with modulo.
```

Data Engineering connection:

```text
Fixed event buffer.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 19: Browser History

LeetCode:

```text
1472. Browser History
Difficulty: Medium
```

Primary pattern:

```text
Two stacks
```

Core idea:

```text
Back and forward stacks.
```

Data Engineering connection:

```text
Lineage navigation history.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 20: Backspace String Compare

LeetCode:

```text
844. Backspace String Compare
Difficulty: Easy
```

Primary pattern:

```text
Stack
```

Core idea:

```text
Apply delete markers.
```

Data Engineering connection:

```text
Corrected field comparison.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 21: Remove Adjacent Duplicates

LeetCode:

```text
1047. Remove Adjacent Duplicates
Difficulty: Easy
```

Primary pattern:

```text
Stack
```

Core idea:

```text
Adjacent equal items cancel.
```

Data Engineering connection:

```text
Collapse duplicate tokens.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```

### Card 22: Remove Adjacent Duplicates II

LeetCode:

```text
1209. Remove Adjacent Duplicates II
Difficulty: Medium
```

Primary pattern:

```text
Stack with counts
```

Core idea:

```text
Remove when count reaches K.
```

Data Engineering connection:

```text
Threshold duplicate cleanup.
```

Candidate must be able to explain:

```text
1. Why stack/queue/deque applies.
2. What the structure stores.
3. Push/enqueue rule.
4. Pop/dequeue rule.
5. Edge cases.
6. Time complexity.
7. Space complexity.
8. One Data Engineering variation.
```

Passing score:

```text
4/5 or higher without major hints.
```


## 90. Data Engineering Custom Problem Card Appendix

### Custom Card 1: Validate SQL Parentheses

Pattern:

```text
stack
```

Task:

```text
Validate generated SQL parentheses.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 2: Normalize Object Storage Path

Pattern:

```text
stack
```

Task:

```text
Normalize paths with ., .., and duplicate slashes.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 3: Evaluate Metric Formula

Pattern:

```text
stack
```

Task:

```text
Evaluate postfix metric expression safely.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 4: Resolve File Operations

Pattern:

```text
collision stack
```

Task:

```text
Cancel adjacent create/delete conflicts.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 5: Next Higher Latency

Pattern:

```text
monotonic stack
```

Task:

```text
Find runs until higher latency appears.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 6: Recent Event Counter

Pattern:

```text
queue/deque
```

Task:

```text
Count events in recent time window.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 7: Rolling Average Latency

Pattern:

```text
queue + running sum
```

Task:

```text
Average of last K latencies.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 8: Rolling Max Latency

Pattern:

```text
monotonic deque
```

Task:

```text
Max of each K-run latency window.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 9: Recent Max Error Counter

Pattern:

```text
time-based monotonic deque
```

Task:

```text
Max error count in recent time window.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 10: Process Jobs FIFO

Pattern:

```text
queue
```

Task:

```text
Process valid jobs in arrival order.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 11: Pipeline Rollback Order

Pattern:

```text
stack
```

Task:

```text
Rollback completed steps in reverse order.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 12: Fixed Event Buffer

Pattern:

```text
circular queue/deque
```

Task:

```text
Keep last K event IDs.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 13: Retry FIFO Queue

Pattern:

```text
queue
```

Task:

```text
Process retries in arrival order.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 14: Lineage BFS Queue

Pattern:

```text
queue
```

Task:

```text
Traverse downstream dependencies level by level.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```

### Custom Card 15: Nested JSON DFS Stack

Pattern:

```text
stack
```

Task:

```text
Iteratively traverse nested JSON structures.
```

Minimum expected answer:

```text
1. Define order requirement.
2. Define what structure stores.
3. Handle invalid input.
4. Explain edge cases.
5. Explain time and space complexity.
6. Explain production risk if order/window handling is wrong.
```

Passing score:

```text
4/5 or higher.
```


## 91. Drill Appendix

### Drill 1: LIFO vs FIFO Classification

Task:

```text
Classify 20 prompts as stack, queue, deque, heap, or hash map.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 2: Basic Stack

Task:

```text
Solve Valid Parentheses, Backspace Compare, and Adjacent Duplicates.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 3: Path Stack

Task:

```text
Solve Simplify Path and object storage normalization.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 4: Expression Stack

Task:

```text
Solve RPN and metric formula validation.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 5: Nested Decode

Task:

```text
Solve Decode String with dry run.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 6: Auxiliary Stack

Task:

```text
Implement Min Stack and explain current minimum.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 7: Collision Stack

Task:

```text
Solve Asteroid Collision and file operation conflict.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 8: Monotonic Stack

Task:

```text
Solve Next Greater, Daily Temperatures, and Stock Span.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 9: Histogram Stack

Task:

```text
Solve Largest Rectangle and explain width calculation.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 10: Basic Queue

Task:

```text
Solve Recent Counter, FIFO jobs, and Moving Average.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 11: Queue Design

Task:

```text
Implement Queue using Stacks and Stack using Queues.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 12: Circular Queue

Task:

```text
Implement circular queue and fixed event buffer.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 13: Monotonic Queue

Task:

```text
Solve Sliding Window Maximum and rolling max latency.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 14: Time Window Queue

Task:

```text
Recent event counter and recent max error counter.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 15: Rollback Stack

Task:

```text
Pipeline rollback order and failure handling discussion.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 16: Complexity Drill

Task:

```text
Explain amortized O(n) for monotonic stack/queue.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```

### Drill 17: Timed Mock

Task:

```text
Run 5 stack/queue problems in 90 minutes and review.
```

Minimum passing answer:

```text
1. State the data structure.
2. Explain why order requirement fits.
3. Define stored item.
4. Define push/pop or enqueue/dequeue rule.
5. Write clean Python.
6. Dry run state changes.
7. Explain time and space complexity.
8. Connect to Data Engineering when relevant.
```

Repair trigger:

```text
If score is below 4/5, repeat with two variations before moving on.
```


## 92. Quick Reference Cards

### Quick Card 1: Stack

Summary:

```text
LIFO; use list append/pop.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 2: Queue

Summary:

```text
FIFO; use deque append/popleft.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 3: Deque

Summary:

```text
O(1) both ends; useful for windows.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 4: Bracket validation

Summary:

```text
Push openings, pop matching closings, stack empty at end.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 5: Path simplification

Summary:

```text
Push directories, pop on .., ignore . and empty.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 6: RPN

Summary:

```text
Pop right then left operand for operators.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 7: Min Stack

Summary:

```text
Maintain auxiliary min stack.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 8: Monotonic stack

Summary:

```text
Stores unresolved indices for next greater/smaller.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 9: Monotonic queue

Summary:

```text
Stores window candidate indices in value order.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 10: Sliding max

Summary:

```text
Expire old indices, pop smaller from back, front is max.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 11: Recent counter

Summary:

```text
Queue timestamps and remove old events.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 12: Moving average

Summary:

```text
Queue + running sum avoids O(k) recompute.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 13: Queue using stacks

Summary:

```text
Use input/output stacks, transfer on demand.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 14: Circular queue

Summary:

```text
Use modulo with front and size.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```

### Quick Card 15: Rollback

Summary:

```text
Undo completed steps in reverse order with stack.
```

Interview check:

```text
Give one LeetCode example and one Data Engineering example where this applies.
```
