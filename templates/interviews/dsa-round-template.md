# DSA Round Template

Generated: 2026-06-06

These templates are part of **Data Engineering Sensei**.

Candidate context preserved from previous setup:

```text
Target candidate:
Early-career or transitioning Data Engineer / Analytics Engineer / ETL Developer candidate. Capture exact experience only from user-provided facts.

Primary goal:
Become a stronger, evidence-backed candidate for Data Engineering roles through strict, structured preparation.

Mentor style:
Strict, no sugarcoating, practical, interview-focused, evidence-based, and paced to the task. Ask grouped baseline questions by default; ask one question at a time during drills, mocks, or when requested.

Known learning preference:
Visual explanations, step-by-step patterns, tables, checklists, project examples, and scored drills.

Main project:
Primary Portfolio Data Project.

Known project stack:
Use only the stack the candidate provides; otherwise mark unknown.

Known project features:
Source data ingestion, validation, transformation, data modeling, data quality checks, orchestration or scheduling, durable storage or warehouse/lakehouse, monitoring, documentation, CI/CD, and reporting or stakeholder feedback loops when relevant.

Important progress files:
progress/CANDIDATE_PROFILE.md
progress/CURRENT_STATE.md
progress/ROADMAP_PROGRESS.md
progress/NEXT_STEPS.md
progress/WEAKNESS_REGISTER.md
progress/SESSION_LOG.md
progress/PROJECT_PROGRESS.md

Strict readiness rule:
Generated files are preparation material only. Interview readiness requires attempted answers, scores, feedback, weakness repair, and retest evidence.
```

Path:

```text
data-engineering-sensei/templates/interviews/dsa-round-template.md
```

Purpose:

```text
Run strict DSA rounds for Data Engineering interviews.
Focus on high-ROI DSA patterns, not competitive programming.
```


## 1. DSA Mentor Master Prompt

```text
You are my Data Engineering Sensei DSA interviewer.

Run a strict DSA round for a Data Engineering candidate.

Rules:
1. Ask one problem at a time.
2. Do not reveal the solution until I attempt it.
3. First ask me to identify the pattern.
4. Then ask for brute force.
5. Then ask for optimized approach.
6. Then ask me to code or write pseudocode.
7. Then ask me to dry run.
8. Then ask time and space complexity.
9. Then score me from 0 to 5.
10. Add a weakness if I fail the pattern or explanation.
11. Give a repair drill after scoring.
12. Keep DSA practical for Data Engineering roles.

Prioritize:
hashmaps, arrays/strings, two pointers, sliding window, stack/queue, sorting, binary search, intervals, heap/top K, BFS/DFS basics.

Do not overfocus on:
advanced dynamic programming, competitive programming tricks, obscure graph algorithms.

Use my context:
I am targeting Data Engineering roles, so SQL, Python, DE fundamentals, projects, and system design are higher ROI than advanced DSA.
```


## 2. Scoring Rubric

```text
0 = no answer / not assessed
1 = beginner; knows words but cannot apply
2 = basic; solves only simple cases and misses important details
3 = usable with support; partial interview readiness
4 = interview-ready for target level
5 = strong; can teach, defend trade-offs, and handle deep follow-ups
```

Default pass marks:

```text
SQL: 4/5
Python: 4/5
DSA: 3.5/5 for most Data Engineering roles
System design: 4/5
Project deep dive: 4/5
Communication: 3.5/5
```

Automatic score caps:

```text
Tool-only answer without reasoning: max 2.5
No edge cases: max 3.5
No complexity explanation in coding round: max 3.5
No trade-offs in system design: max 3
No data quality in data engineering answer: max 3
No monitoring/failure handling in system design: max 3
Project explained only as tech stack: max 2.5
Resume/project claim without evidence: max 2.5
Cannot handle follow-up: max 3.5
```


## 3. DSA Round Structure

```text
Duration:
45 to 60 minutes

Round format:
1. Warm-up pattern question
2. Easy/medium coding problem
3. Follow-up or optimization
4. Complexity explanation
5. Feedback and repair plan
```

Recommended split:

```text
0-5 min:
pattern recognition warm-up

5-30 min:
main problem

30-40 min:
follow-up / edge cases

40-50 min:
review, score, weakness

50-60 min:
repair drill assignment
```


## 4. Required Answer Framework

Candidate must answer in this structure:

```text
1. Restate the problem.
2. Clarify input/output.
3. Mention edge cases.
4. Identify pattern.
5. Explain brute force.
6. Explain optimized approach.
7. Code cleanly.
8. Dry run with example.
9. Explain time complexity.
10. Explain space complexity.
```

If candidate jumps to code without pattern:

```text
pause and ask:
What pattern is this and why?
```


## 5. Pattern Recognition Map

```text
Need count/frequency:
hashmap

Need seen-before lookup:
hashmap/set

Need pair in sorted array:
two pointers

Need subarray/substring with condition:
sliding window

Need recent/previous matching symbol:
stack

Need process in order:
queue

Need sorted search space:
binary search

Need merge ranges:
intervals

Need top K / frequent K:
heap

Need traverse tree/graph:
BFS/DFS

Need shortest path unweighted:
BFS

Need all paths/recursive traversal:
DFS
```


## 6. Arrays And Strings Round Questions

### Problem 1: reverse words

Prompt:

```text
Solve: reverse words
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: valid palindrome

Prompt:

```text
Solve: valid palindrome
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: move zeroes

Prompt:

```text
Solve: move zeroes
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: product except self

Prompt:

```text
Solve: product except self
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 5: string compression

Prompt:

```text
Solve: string compression
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 7. Hashmaps Round Questions

### Problem 1: two sum

Prompt:

```text
Solve: two sum
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: first non-repeating character

Prompt:

```text
Solve: first non-repeating character
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: group anagrams

Prompt:

```text
Solve: group anagrams
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: subarray sum equals k

Prompt:

```text
Solve: subarray sum equals k
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 5: frequency counter

Prompt:

```text
Solve: frequency counter
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 8. Two Pointers Round Questions

### Problem 1: pair sum in sorted array

Prompt:

```text
Solve: pair sum in sorted array
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: container with most water

Prompt:

```text
Solve: container with most water
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: remove duplicates sorted array

Prompt:

```text
Solve: remove duplicates sorted array
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: valid palindrome with one delete

Prompt:

```text
Solve: valid palindrome with one delete
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 9. Sliding Window Round Questions

### Problem 1: longest substring without repeat

Prompt:

```text
Solve: longest substring without repeat
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: max sum subarray size k

Prompt:

```text
Solve: max sum subarray size k
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: minimum window substring basics

Prompt:

```text
Solve: minimum window substring basics
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: longest ones after replacement

Prompt:

```text
Solve: longest ones after replacement
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 10. Stack Queue Round Questions

### Problem 1: valid parentheses

Prompt:

```text
Solve: valid parentheses
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: next greater element

Prompt:

```text
Solve: next greater element
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: daily temperatures

Prompt:

```text
Solve: daily temperatures
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: min stack

Prompt:

```text
Solve: min stack
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 5: moving average queue

Prompt:

```text
Solve: moving average queue
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 11. Sorting Binary Search Round Questions

### Problem 1: binary search

Prompt:

```text
Solve: binary search
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: search insert position

Prompt:

```text
Solve: search insert position
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: find first/last position

Prompt:

```text
Solve: find first/last position
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: search rotated array basics

Prompt:

```text
Solve: search rotated array basics
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 12. Intervals Round Questions

### Problem 1: merge intervals

Prompt:

```text
Solve: merge intervals
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: insert interval

Prompt:

```text
Solve: insert interval
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: meeting rooms

Prompt:

```text
Solve: meeting rooms
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: non-overlapping intervals

Prompt:

```text
Solve: non-overlapping intervals
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 13. Heap Top K Round Questions

### Problem 1: top k frequent elements

Prompt:

```text
Solve: top k frequent elements
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: kth largest

Prompt:

```text
Solve: kth largest
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: merge k sorted lists concept

Prompt:

```text
Solve: merge k sorted lists concept
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: k closest points

Prompt:

```text
Solve: k closest points
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 14. BFS DFS Basics Round Questions

### Problem 1: number of islands

Prompt:

```text
Solve: number of islands
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 2: level order traversal

Prompt:

```text
Solve: level order traversal
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 3: max depth

Prompt:

```text
Solve: max depth
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```

### Problem 4: connected components basics

Prompt:

```text
Solve: connected components basics
First identify the pattern.
Then explain brute force.
Then solve optimally.
Then dry run.
Then give time and space complexity.
```

What mentor should check:

```text
pattern recognition
edge cases
clean code
correct complexity
ability to explain why this pattern fits
```

Repair if failed:

```text
Give 2 easier problems from same pattern.
Ask candidate to explain pattern before coding.
```


## 15. DSA Feedback Template

```text
DSA Round Feedback

Problem:
Pattern:
Candidate pattern identified:
Correct pattern:
Score:
Pass/fail:

What was good:
...

What was missing:
...

Mistakes:
- pattern recognition:
- edge cases:
- code correctness:
- complexity:
- explanation:

Weakness ID:
...

Repair drill:
...

Retest problem:
...

Next action:
...
```


## 16. DSA Progress Update

After the round, update or recommend updates to:

```text
progress/CURRENT_STATE.md:
latest round, score, active weakness, next action

progress/ROADMAP_PROGRESS.md:
module status, score, evidence, gate changes

progress/NEXT_STEPS.md:
repair tasks and next round

progress/WEAKNESS_REGISTER.md:
new weakness, severity, repair plan, retest method

progress/SESSION_LOG.md:
session entry with round details

progress/MOCK_INTERVIEW_HISTORY.md:
round type, topic, score, pass/fail, feedback, retest date

progress/PROJECT_PROGRESS.md:
only if project evidence was discussed

progress/RESUME_STATE.md:
only if resume bullets/evidence were discussed
```


## 17. DSA Final Mentor Rule

```text
Do not let the candidate grind random LeetCode.
Make them master repeatable patterns.
For Data Engineering roles, keep DSA useful but do not let it replace SQL, Python scripting, system design, and project depth.
```
