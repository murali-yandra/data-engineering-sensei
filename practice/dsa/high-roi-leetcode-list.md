# High-ROI LeetCode List for Data Engineering

Use this as the canonical DSA problem index for Data Engineering Sensei.

The mentor should assign problems based on weakness, target company, and timeline. Do not assign all problems blindly.

## Core List

| # | Problem | Difficulty | Pattern | Why it matters |
|---:|---|---|---|---|
| 1 | Two Sum | Easy | Hash map | Lookup and pair matching |
| 217 | Contains Duplicate | Easy | Set | Deduplication and membership |
| 242 | Valid Anagram | Easy | Frequency count | Counting and grouping |
| 49 | Group Anagrams | Medium | Hash map | Grouping records by derived key |
| 347 | Top K Frequent Elements | Medium | Heap or bucket count | Top-K analytics |
| 238 | Product of Array Except Self | Medium | Prefix/suffix | Derived values without nested loops |
| 3 | Longest Substring Without Repeating Characters | Medium | Sliding window | Contiguous-window reasoning |
| 424 | Longest Repeating Character Replacement | Medium | Sliding window | Window with constraint |
| 567 | Permutation in String | Medium | Sliding window + frequency | Window comparison |
| 125 | Valid Palindrome | Easy | Two pointers | Clean pointer movement |
| 167 | Two Sum II | Medium | Two pointers | Ordered input reasoning |
| 15 | 3Sum | Medium | Sorting + two pointers | Duplicate handling and ordered search |
| 704 | Binary Search | Easy | Binary search | Sorted search |
| 35 | Search Insert Position | Easy | Binary search | Boundary reasoning |
| 33 | Search in Rotated Sorted Array | Medium | Binary search | Conditional sorted halves |
| 20 | Valid Parentheses | Easy | Stack | Validation and parsing |
| 155 | Min Stack | Medium | Stack | Auxiliary state |
| 739 | Daily Temperatures | Medium | Monotonic stack | Next-greater pattern |
| 215 | Kth Largest Element in an Array | Medium | Heap or quickselect | Rank and top-K |
| 973 | K Closest Points to Origin | Medium | Heap | Top-K with custom key |
| 56 | Merge Intervals | Medium | Intervals | Overlap merging |
| 57 | Insert Interval | Medium | Intervals | Insert and merge ranges |
| 435 | Non-overlapping Intervals | Medium | Greedy intervals | Conflict removal |
| 200 | Number of Islands | Medium | BFS/DFS | Grid traversal |
| 994 | Rotting Oranges | Medium | BFS | Multi-source BFS |
| 207 | Course Schedule | Medium | Graph/topological sort | Dependency traversal |

## Assignment Rules

Use this order for most candidates:

1. Hash map and set.
2. Sorting and two pointers.
3. Sliding window.
4. Stack and queue.
5. Heap and top K.
6. Intervals.
7. BFS/DFS basics.
8. Binary search.

For short timelines, assign only:

```text
Two Sum
Contains Duplicate
Group Anagrams
Top K Frequent Elements
Longest Substring Without Repeating Characters
Valid Parentheses
Merge Intervals
Number of Islands
```

## Review Standard

A submitted solution must include:

- pattern
- approach
- code or precise pseudocode
- time complexity
- space complexity
- edge cases
- one follow-up variation

If the candidate cannot explain the pattern, do not mark the problem as complete.
