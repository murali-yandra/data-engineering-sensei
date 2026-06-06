# Contributing to Data Engineering Sensei 🛠️

Thank you for contributing to **Data Engineering Sensei**.

This project is a strict, interview-focused AI mentor for Data Engineering interview preparation. It trains candidates in SQL, Python, high-ROI DSA, Data Engineering fundamentals, data modeling, ETL/ELT, Spark/PySpark, cloud data platforms, orchestration, system design, project explanation, and mock interviews.

This repository is mostly a **Markdown-based AI skill/prompt system**. Contributions should improve the mentor’s behavior, accuracy, structure, interview realism, and usefulness.

---

## 1. Project Mission

The mission of Data Engineering Sensei is:

> Help candidates crack Data Engineering interviews through strict assessment, personalized roadmaps, realistic practice, honest feedback, and interview-ready explanation training.

This project is not trying to become:

- a generic Data Engineering course
- a cloud certification guide
- a competitive programming repository
- a soft motivational chatbot
- a random collection of interview questions
- a direct-answer machine that prevents learning

Every contribution should support interview readiness.

---

## 2. Contribution Philosophy

A good contribution should make the mentor better at one or more of these:

1. Assessing a candidate’s current level.
2. Identifying weak areas.
3. Creating personalized interview roadmaps.
4. Teaching SQL, Python, DSA, DE fundamentals, modeling, and system design clearly.
5. Giving strict, realistic feedback.
6. Simulating real Data Engineering interviews.
7. Helping candidates explain projects with ownership and depth.
8. Reducing hallucination and vague advice.
9. Improving practice quality.
10. Improving progress tracking.

If a contribution does not improve interview performance, question whether it belongs here.

---

## 3. Expected Mentor Standard

The mentor should behave like a serious senior Data Engineer / interviewer.

It should be:

- strict
- direct
- realistic
- practical
- structured
- no-sugarcoating
- interview-focused

It should not be:

- rude
- insulting
- blindly motivational
- vague
- overcomplicated
- tool-obsessed
- memorization-focused
- unrealistic about timelines

### Good Mentor Behavior

```text
Your answer defines CDC, but it does not explain why CDC matters in a pipeline.
In an interview, that is too shallow. Add source change tracking, incremental ingestion,
failure handling, and downstream consistency.
```

### Bad Mentor Behavior

```text
Nice answer! Keep practicing!
```

This is too vague and does not help the candidate improve.

---

## 4. Repository Structure

Expected structure:

```text
data-engineering-sensei/
├── SKILL.md
├── README.md
├── CONTRIBUTING.md
├── modes/
│   ├── tutor-mode.md
│   ├── hint-mode.md
│   ├── review-mode.md
│   ├── interview-mode.md
│   ├── pattern-mapper-mode.md
│   ├── profile-assessment-mode.md
│   ├── roadmap-mode.md
│   ├── sql-drill-mode.md
│   ├── python-drill-mode.md
│   ├── dsa-drill-mode.md
│   ├── system-design-mode.md
│   ├── project-deep-dive-mode.md
│   └── weakness-repair-mode.md
├── docs/
│   ├── data-engineering-interview-roadmap.md
│   ├── sql-interview-guide.md
│   ├── python-interview-guide.md
│   ├── dsa-for-data-engineering.md
│   ├── data-modeling-guide.md
│   ├── data-engineering-fundamentals.md
│   ├── spark-pyspark-guide.md
│   ├── warehouse-cloud-guide.md
│   ├── orchestration-airflow-guide.md
│   ├── system-design-guide.md
│   ├── project-deep-dive-guide.md
│   └── assessment-rubric.md
├── templates/
│   ├── answer-frameworks/
│   ├── interview-feedback/
│   ├── roadmaps/
│   └── progress/
├── practice/
│   ├── sql/
│   ├── python/
│   ├── dsa/
│   ├── system-design/
│   └── mixed-interviews/
├── progress/
├── assets/
├── scripts/
└── tests/
```

---

## 5. High-Priority Contributions

The most valuable contributions are:

### 5.1 SQL Interview Improvements

High-priority SQL improvements include:

- realistic business-style SQL questions
- window function drills
- deduplication patterns
- cohort and retention queries
- gaps and islands examples
- query review checklists
- SQL anti-pattern examples
- performance reasoning prompts
- dialect notes for PostgreSQL, SQL Server, BigQuery, and Snowflake

SQL is one of the highest-signal areas for Data Engineering interviews, so SQL content must be strong.

### 5.2 Python Interview Improvements

Useful Python contributions include:

- data transformation exercises
- dictionary/set/list drills
- JSON parsing tasks
- CSV/file-style questions
- API response processing tasks
- malformed record handling
- memory-conscious processing examples
- Python code review rubrics
- complexity explanations for Python operations

Python should be taught for interview coding and practical Data Engineering scripts, not abstract syntax memorization.

### 5.3 High-ROI DSA Improvements

DSA contributions should focus on role-relevant patterns:

- arrays
- strings
- hash maps
- sets
- sorting
- binary search
- two pointers
- sliding window
- stack
- queue
- heap basics
- intervals
- BFS/DFS basics
- prefix sums
- top K problems

Avoid turning this project into a competitive programming trainer.

### 5.4 Data Engineering Fundamentals

Valuable additions include better explanations and drills for:

- ETL vs ELT
- batch vs streaming
- CDC
- full load vs incremental load
- idempotency
- backfills
- retries
- schema evolution
- partitioning
- file formats
- data quality
- monitoring
- SLAs
- lineage

### 5.5 Data Engineering System Design

Useful system design contributions include:

- batch ingestion designs
- CDC pipeline designs
- streaming pipeline designs
- data warehouse designs
- data lakehouse designs
- data quality frameworks
- reporting pipelines
- customer 360 pipelines
- log analytics pipelines
- monitoring and alerting systems
- backfill/reprocessing strategies

Every design should include requirements, data volume, latency, failure handling, quality checks, monitoring, cost, and trade-offs.

### 5.6 Project Deep Dive Improvements

Useful additions include:

- project explanation frameworks
- follow-up questions
- ownership clarification prompts
- weak vs strong project answer examples
- architecture explanation templates
- impact statement examples
- production issue discussion prompts

### 5.7 Assessment and Progress Tracking

Useful contributions include:

- better candidate intake questions
- assessment rubrics
- readiness scoring
- progress tracking templates
- session summary formats
- roadmap checkpoint formats
- weakness repair loops

---

## 6. Medium-Priority Contributions

Medium-priority contributions include:

- more mock interview sets
- more mixed interview rounds
- better behavioral interview prompts
- better markdown formatting
- better diagrams
- better examples for different experience levels
- additional cloud examples
- improvements to README clarity
- documentation cleanup

---

## 7. Low-Priority Contributions

Low-priority contributions include:

- decorative changes
- extra emojis
- purely visual changes
- unnecessary renaming
- broad generic tutorial content
- advanced topics that rarely appear in DE interviews

These are not forbidden, but they should not distract from the core mission.

---

## 8. What Not to Contribute

Do not contribute content that:

1. Gives fake company-specific claims.
2. Invents interview questions and labels them as real.
3. Fabricates LeetCode problem numbers or links.
4. Encourages memorization without understanding.
5. Gives direct answers without explanation.
6. Over-focuses on competitive programming.
7. Over-focuses on cloud certification trivia.
8. Makes unrealistic promises.
9. Uses a soft tone that hides weak performance.
10. Includes copyrighted material copied from paid platforms.
11. Includes private company interview content from NDAs.
12. Includes user personal data.
13. Includes secrets, tokens, credentials, or private keys.

---

## 9. Accuracy Rules

Accuracy matters because this project trains candidates for interviews.

### 9.1 Do Not Fabricate

Never fabricate:

- LeetCode titles
- LeetCode numbers
- company interview processes
- company-specific hiring standards
- tool behavior
- benchmark numbers
- salary data
- current trends
- links

If unsure, write content in a way that avoids unsupported claims.

Bad:

```text
Google always asks this exact SQL question.
```

Good:

```text
This is a common style of SQL question in product analytics and Data Engineering interviews.
```

### 9.2 LeetCode Problem References

When adding LeetCode practice problems, include:

```text
LeetCode number:
Problem title:
Difficulty:
Pattern:
Link if known:
Why it matters for Data Engineering interviews:
```

Use only real, well-known problems.

If you are unsure of the URL slug, include the number and title only.

### 9.3 SQL Dialect Notes

Default to ANSI-style SQL.

Add dialect notes only when helpful:

- PostgreSQL
- SQL Server
- BigQuery
- Snowflake

Do not write one dialect-specific solution and imply it works everywhere.

### 9.4 Tool-Specific Claims

For Spark, Airflow, BigQuery, Snowflake, Redshift, AWS, GCP, and Azure:

- prefer conceptual explanations
- avoid outdated claims
- avoid unsupported version-specific behavior
- mention assumptions when needed

---

## 10. Writing Style Guide

### 10.1 General Style

Use clear, direct language.

Preferred:

```text
This answer is not interview-ready because it does not explain failure handling.
```

Avoid:

```text
Maybe you can improve this a little bit.
```

### 10.2 Formatting

Use:

- clear headings
- numbered steps
- tables where useful
- code blocks for examples
- checklists for reviews
- explicit rubrics for scoring

Avoid:

- long unstructured paragraphs
- vague motivational text
- too many emojis
- dense jargon without explanation

### 10.3 Tone

Tone should be strict but useful.

Allowed:

```text
This is weak for your experience level.
```

Not allowed:

```text
You clearly do not know anything.
```

The mentor should challenge the candidate, not insult them.

### 10.4 Interview-Focused Language

Every guide should answer:

- Why does this matter in interviews?
- What does a weak answer look like?
- What does a strong answer look like?
- What follow-ups can be asked?
- How should the candidate explain this clearly?

---

## 11. Markdown Standards

All Markdown files should follow these rules:

1. Use `#` for the title.
2. Use `##` for main sections.
3. Use `###` for subsections.
4. Use fenced code blocks for code or templates.
5. Use tables only when they improve clarity.
6. Keep examples realistic.
7. Prefer numbered steps for processes.
8. Avoid excessive emojis.
9. Avoid unexplained abbreviations.
10. Make each file useful on its own.

### Example Section Pattern

```md
## Concept Name

### Plain-English Explanation

### Why Interviewers Ask This

### Weak Answer

### Strong Answer

### Common Mistakes

### Follow-Up Questions

### Mini Drill
```

---

## 12. Mode File Standards

Every file in `modes/` should include:

1. Purpose of the mode
2. When to trigger it
3. When not to trigger it
4. Required behavior
5. Output format
6. Strict feedback rules
7. Error scenarios
8. Example interactions
9. Scoring or review rules when relevant
10. Next-step behavior

### Required Mode Behavior

Mode files should be very clear about how the mentor behaves.

Bad:

```md
Help the user with SQL.
```

Good:

```md
When the user asks for SQL practice, provide a schema and business question.
Do not provide the solution immediately. First ask the user to explain the output grain,
base table, join strategy, aggregation level, and edge cases.
```

---

## 13. Documentation File Standards

Files in `docs/` should be detailed guides.

Each guide should include:

1. What the topic is
2. Why it matters in interviews
3. Core concepts
4. Interview explanation frameworks
5. Weak vs strong answers
6. Practice questions
7. Common mistakes
8. Follow-up questions
9. Minimum passing standard
10. Advanced expectations for experienced candidates

---

## 14. Practice File Standards

Files in `practice/` should contain interview-quality practice.

Each practice problem should include:

```text
Problem title:
Round type:
Difficulty:
Expected time:
Skills tested:
Prompt:
Input/schema:
Expected output:
What candidate should explain:
Hints:
Common mistakes:
Review criteria:
Follow-up variation:
```

For SQL problems, include:

- schema
- table grain
- sample rows when useful
- expected output grain
- edge cases

For Python problems, include:

- input shape
- output shape
- malformed data cases
- expected complexity
- edge cases

For DSA problems, include:

- LeetCode number/title/difficulty
- pattern
- why it matters for DE
- expected approach
- common traps

For system design problems, include:

- requirements to clarify
- data volume assumptions
- latency expectations
- architecture expectations
- quality and monitoring expectations
- follow-up questions

---

## 15. Template File Standards

Files in `templates/` should provide reusable answer formats.

Templates should be:

- specific
- structured
- easy to copy
- interview-focused
- strict about quality

A good template should tell the candidate exactly how to organize an answer under interview pressure.

---

## 16. Progress File Standards

Files in `progress/` should help the AI or candidate continue from where they left off.

Progress files should be simple and structured.

### 16.1 `CURRENT_STATE.md`

Should track:

```text
Current focus:
Current module:
Current difficulty:
Current weak area:
Last completed task:
Last failed task:
Next task:
Blocked by:
```

### 16.2 `REQUIREMENTS.md`

Should track:

```text
Project goal:
Scope:
Out of scope:
Mentor tone:
Core modules:
Default interview standard:
File generation rules:
User decisions:
```

### 16.3 `DECISION_LOG.md`

Should track:

```text
Decision:
Reason:
Impact:
Date/order:
```

### 16.4 `FILE_GENERATION_LOG.md`

Should track:

```text
Generated files:
Pending files:
Partially generated files:
Next recommended file:
```

### 16.5 `CANDIDATE_PROFILE.md`

Should track:

```text
Experience:
Current role:
Timeline:
Target companies/countries:
Skill ratings:
Weakest areas:
Study hours:
Readiness verdict:
```

### 16.6 `ROADMAP_PROGRESS.md`

Should track:

```text
Roadmap start:
Roadmap target:
Completed modules:
Current module:
Drill scores:
Mock interview scores:
Weakness repair tasks:
Next checkpoint:
```

---

## 17. Branch Workflow

Use a branch for every contribution.

### Branch Naming

Use descriptive names:

```bash
feature/sql-window-drills
feature/project-deep-dive-mode
fix/readme-typos
docs/system-design-guide
practice/python-json-drills
```

Avoid vague branch names:

```bash
changes
updates
new-stuff
final
```

### Recommended Workflow

```bash
git checkout main
git pull origin main
git checkout -b feature/your-change-name
```

Make your changes.

Then:

```bash
git status
git add .
git commit -m "Add SQL window function drill guide"
git push origin feature/your-change-name
```

Open a pull request.

---

## 18. Commit Message Guidelines

Use clear commit messages.

Recommended prefixes:

```text
Add:
Update:
Fix:
Refactor:
Docs:
Practice:
Template:
Mode:
Progress:
```

Examples:

```text
Add: SQL drill mode with window function review rules
Update: README with progress folder workflow
Fix: typo in Python drill template
Practice: Add high-ROI DSA problem list
Mode: Add project deep dive strict follow-up rules
Docs: Add system design guide outline
```

Avoid:

```text
update
done
final version
fixed stuff
```

---

## 19. Pull Request Guidelines

Every PR should include:

```text
## What changed?

## Why this matters for Data Engineering interviews?

## Files changed

## How to test/review

## Any risks or open questions?
```

### PR Checklist

Before opening a PR:

- [ ] The change is interview-focused.
- [ ] The tone is strict but not rude.
- [ ] The content is accurate.
- [ ] No fake company-specific claims were added.
- [ ] No fabricated LeetCode references were added.
- [ ] Markdown formatting is clean.
- [ ] Examples are realistic.
- [ ] Weak vs strong answer examples are included where useful.
- [ ] Follow-up questions are included where useful.
- [ ] Progress files are updated if relevant.
- [ ] README or file generation log is updated if structure changed.

---

## 20. Issue Guidelines

Open an issue for:

- bug in instructions
- unclear mode behavior
- weak or vague content
- inaccurate technical explanation
- missing interview topic
- missing practice problem type
- broken link
- file structure problem
- roadmap gap
- hallucination risk
- improvement idea

### Good Issue Format

```text
## Problem

## Why it matters

## Suggested fix

## Affected file

## Example
```

### Example Issue

```text
## Problem

SQL Drill Mode does not force the candidate to identify output grain.

## Why it matters

Many SQL interview failures happen because the candidate aggregates at the wrong level.

## Suggested fix

Add a mandatory step asking:
- What is the output grain?
- What is the base table?
- Can joins create duplicate rows?

## Affected file

modes/sql-drill-mode.md
```

---

## 21. Testing Contributions

This repository is mostly Markdown, but changes still need review.

### 21.1 Manual Testing

For any mode file, test with example prompts.

Example for SQL Drill Mode:

```text
Give me a medium SQL question on deduplication.
```

Expected behavior:

- mentor gives schema
- asks for approach
- does not reveal solution immediately
- reviews output grain and ROW_NUMBER logic

### 21.2 Review Testing

For Review Mode, test with a weak answer.

Example:

```text
Review this project explanation:
"We created ETL pipelines using Spark and loaded data to warehouse."
```

Expected behavior:

- mentor flags vague ownership
- asks for architecture
- asks what the candidate personally did
- asks for data volume, SLA, failure handling, and impact

### 21.3 Interview Testing

For Interview Mode, test:

```text
Take my Data Engineering system design interview.
```

Expected behavior:

- mentor asks a realistic design question
- forces requirements
- asks follow-ups
- scores strictly
- gives next tasks

### 21.4 Regression Testing

After changing `SKILL.md`, test that the mentor still routes correctly for:

- roadmap request
- SQL practice request
- Python practice request
- DSA practice request
- system design request
- project deep dive request
- mock interview request
- review request
- hint request

---

## 22. Technical Accuracy Review Checklist

Before submitting technical content, check:

### SQL

- [ ] Is the query logically correct?
- [ ] Is the output grain clear?
- [ ] Are joins correct?
- [ ] Could joins create duplicate rows?
- [ ] Is GROUP BY used correctly?
- [ ] Are NULLs handled?
- [ ] Are date boundaries clear?
- [ ] Are window partitions and orderings correct?
- [ ] Is the dialect clear?

### Python

- [ ] Is the code correct?
- [ ] Is it readable?
- [ ] Are edge cases handled?
- [ ] Is complexity explained?
- [ ] Are variable names clear?
- [ ] Is input shape clear?
- [ ] Does it avoid unnecessary nested loops?
- [ ] Is pandas used only when appropriate?

### DSA

- [ ] Is the problem real?
- [ ] Is the pattern correct?
- [ ] Is difficulty accurate?
- [ ] Is the DE relevance explained?
- [ ] Are common traps included?

### Data Engineering Concepts

- [ ] Is the definition accurate?
- [ ] Is the practical example realistic?
- [ ] Is the interview relevance clear?
- [ ] Are trade-offs included?
- [ ] Are common mistakes included?

### System Design

- [ ] Are requirements clarified?
- [ ] Is data volume discussed?
- [ ] Is latency discussed?
- [ ] Is failure handling included?
- [ ] Is data quality included?
- [ ] Is monitoring included?
- [ ] Is backfill/reprocessing included?
- [ ] Are cost trade-offs included?
- [ ] Is security/governance mentioned where relevant?

---

## 23. Content Depth Expectations

The user specifically expects detailed files, even if they are lengthy.

A generated file should not be shallow.

### Minimum Good Depth

Each major guide or mode file should include:

- purpose
- scope
- triggers
- behavior
- examples
- error handling
- weak vs strong examples
- review criteria
- next-step behavior

### Avoid Shallow Sections

Bad:

```md
## SQL

Teach joins and windows.
```

Good:

```md
## SQL

When teaching joins, force the candidate to identify:
1. base table
2. output grain
3. join key
4. join type
5. duplicate risk
6. NULL behavior
7. whether aggregation should happen before or after the join
```

---

## 24. Candidate Experience-Level Rules

Content should adapt by candidate level.

### Beginner Candidate

Focus on:

- basic SQL
- simple Python
- core DE concepts
- project explanation basics
- easy DSA

Do not expect senior-level system design.

### Junior Candidate

Focus on:

- SQL medium questions
- Python transformations
- basic DSA
- ETL concepts
- project clarity

### Mid-Level Candidate

Focus on:

- advanced SQL
- pipeline trade-offs
- Spark basics
- system design
- ownership
- optimization

### Experienced Candidate

Focus on:

- architecture depth
- failure handling
- scalability
- data quality
- cost
- mentoring/ownership examples
- tough follow-ups

### Senior Candidate

Focus on:

- ambiguous requirements
- cross-team trade-offs
- platform thinking
- governance
- reliability
- design leadership
- deep project defense

---

## 25. Error Scenario Coverage

When contributing mode behavior, include how to handle:

1. User gives incomplete information.
2. User asks for full solution without trying.
3. User has unrealistic timeline.
4. User avoids weak areas.
5. User gives a memorized answer.
6. User gives a vague project explanation.
7. User writes SQL that returns duplicates.
8. User writes Python without edge cases.
9. User gives system design without requirements.
10. User wants advanced topics before basics.
11. User gets frustrated.
12. User asks for company-specific claims.
13. User asks for outdated or current hiring trends.
14. User asks for non-interview content.

---

## 26. Security and Privacy

Do not commit:

- API keys
- access tokens
- database credentials
- private resumes
- private interview transcripts
- proprietary company documents
- personal user data
- confidential business data
- screenshots with sensitive information

If examples require data, use fake data.

---

## 27. Copyright and Content Safety

Do not copy:

- paid course content
- paid interview question banks
- proprietary company interview materials
- copyrighted explanations from other sites
- content under restrictive licenses

It is fine to create original explanations inspired by common public interview topics.

---

## 28. Accessibility and Readability

Make content easy to use for candidates.

Use:

- simple language
- clear definitions
- practical examples
- structured checklists
- progressive difficulty
- short code examples
- realistic scenarios

Avoid:

- unnecessary academic language
- overly long code without explanation
- walls of text without headings
- unexplained abbreviations

---

## 29. Adding New Files

When adding a new file:

1. Confirm it fits the project scope.
2. Put it in the correct folder.
3. Add a clear title.
4. Include purpose and usage.
5. Link or mention it in README if important.
6. Update `progress/FILE_GENERATION_LOG.md` if using the generation workflow.
7. Update `progress/NEXT_STEPS.md` if it changes generation order.

### New Mode File Checklist

- [ ] Purpose
- [ ] Trigger conditions
- [ ] Non-trigger conditions
- [ ] Required behavior
- [ ] Output template
- [ ] Strict feedback rules
- [ ] Error scenarios
- [ ] Example prompts
- [ ] Example responses
- [ ] Next action behavior

### New Guide File Checklist

- [ ] Topic overview
- [ ] Interview relevance
- [ ] Core concepts
- [ ] Examples
- [ ] Weak vs strong answers
- [ ] Common mistakes
- [ ] Practice tasks
- [ ] Follow-up questions
- [ ] Passing standard

### New Practice File Checklist

- [ ] Difficulty labels
- [ ] Skills tested
- [ ] Realistic prompts
- [ ] Expected explanation
- [ ] Hints
- [ ] Review criteria
- [ ] Follow-up variations

---

## 30. Updating Existing Files

When updating existing files:

1. Preserve the strict mentor identity.
2. Preserve interview-only focus.
3. Do not remove DSA completely.
4. Keep DSA high-ROI and DE-relevant.
5. Keep SQL as a top priority.
6. Keep target companies optional.
7. Keep FAANG-level as default when no target is provided.
8. Keep current tech stack non-mandatory in intake.
9. Keep progress tracking support.
10. Keep detailed error scenario behavior.

---

## 31. Review Standards by File Type

### `SKILL.md`

Review for:

- correct identity
- correct routing
- candidate intake behavior
- strict tone
- full curriculum scope
- error handling
- progress support
- no contradictions

### `README.md`

Review for:

- clear project purpose
- installation
- usage examples
- file structure
- modes
- progress workflow
- contribution workflow
- accurate expectations

### `CONTRIBUTING.md`

Review for:

- contribution process
- style guide
- technical accuracy rules
- PR/issue process
- content standards
- safety and copyright rules

### `modes/*.md`

Review for:

- mode triggers
- behavior
- output templates
- examples
- error handling
- strictness
- interview focus

### `docs/*.md`

Review for:

- conceptual accuracy
- interview relevance
- detailed examples
- weak/strong answers
- follow-up questions
- passing standards

### `practice/*.md`

Review for:

- realistic prompts
- clear difficulty
- expected approach
- review criteria
- follow-up variations

### `progress/*.md`

Review for:

- continuity
- current state clarity
- generated file tracking
- decision tracking
- next steps

---

## 32. Example Good Contribution

### Contribution

Add a SQL deduplication drill.

### Why It Is Good

It improves SQL interview readiness by training a common Data Engineering pattern.

### Expected Content

```md
## SQL Drill: Deduplicate Latest Event Per User

Difficulty: Medium
Skills tested: ROW_NUMBER, PARTITION BY, ORDER BY, CTE, output grain

### Schema

events(user_id, event_id, event_type, event_time, updated_at)

### Question

For each user, return their latest event by event_time. If two events have the same event_time,
use updated_at as the tie-breaker.

### What Candidate Should Explain

1. Output grain is one row per user.
2. Need ROW_NUMBER partitioned by user_id.
3. Order by event_time DESC, updated_at DESC.
4. Filter row_number = 1.
5. Handle ties deterministically.
```

---

## 33. Example Poor Contribution

### Contribution

Add a generic list of 100 SQL questions with no schema, answer expectation, or review criteria.

### Why It Is Poor

It does not train interview performance. It creates volume without structure.

### How to Fix

For each question, add:

- schema
- difficulty
- skills tested
- expected approach
- hints
- common mistakes
- review criteria
- follow-up variation

---

## 34. Maintaining the No-Sugarcoating Standard

Strict does not mean negative.

The mentor should:

- expose gaps
- explain consequences
- give next actions
- track improvement

The mentor should not:

- shame the candidate
- mock the candidate
- make personal comments
- use aggressive language
- demotivate without a repair plan

### Good Strict Feedback

```text
This is not interview-ready yet. Your definition is correct, but you cannot explain
how it behaves in a real pipeline. Fix that by adding an example with incremental load,
failure retry, and downstream consistency.
```

### Bad Strict Feedback

```text
This is terrible.
```

The second version gives no path forward and should not be used.

---

## 35. Roadmap Contribution Rules

Roadmaps must be realistic.

A good roadmap includes:

- timeline
- weekly focus
- daily drills
- weak-area priority
- mock interview checkpoints
- exit criteria
- revision blocks
- expected outcomes

Do not create unrealistic roadmaps like:

```text
Become FAANG-ready in 7 days from beginner level.
```

Instead, say:

```text
With 7 days and beginner-level SQL, the realistic goal is not full FAANG readiness.
The goal is to maximize interview survival by focusing on joins, aggregation,
ROW_NUMBER, project explanation, and one basic pipeline design.
```

---

## 36. Mock Interview Contribution Rules

Mock interview content should be realistic.

Each mock interview set should include:

1. Round type
2. Candidate level
3. Difficulty
4. Time limit
5. Question
6. Expected clarifying questions
7. Expected approach
8. Follow-up questions
9. Scoring rubric
10. Common failure patterns
11. Improvement assignment

---

## 37. Behavioral Interview Contribution Rules

Behavioral content should be technical and role-relevant.

Good behavioral topics:

- production incident
- missed deadline
- unclear requirements
- stakeholder conflict
- data quality issue
- learning new tool
- owning a pipeline
- optimizing a slow job
- debugging failure
- explaining technical trade-offs

Use STAR, but add technical depth:

```text
Situation:
Task:
Action:
Technical decision:
Result:
Learning:
```

---

## 38. Keeping the Project Cohesive

Before adding a new concept, ask:

1. Is this useful for Data Engineering interviews?
2. Is it common or high-impact?
3. Does it help SQL, Python, DSA, DE concepts, system design, or project explanation?
4. Does it improve mentor behavior?
5. Does it help candidates explain better?
6. Does it fit the strict interview-prep identity?

If the answer is no, do not add it.

---

## 39. Local Review Before Submitting

Before submitting, read the changed file as if you are a candidate.

Ask:

- Would this help me answer better in an interview?
- Does this tell the mentor exactly how to behave?
- Is the feedback style clear?
- Are there enough examples?
- Are weak answers called out?
- Are next actions specific?
- Is anything vague?
- Is anything inaccurate?
- Is anything too broad?

---

## 40. Maintainer Review Criteria

Maintainers should review PRs using these criteria:

| Category | Question |
|---|---|
| Mission fit | Does it improve DE interview prep? |
| Accuracy | Is the technical content correct? |
| Specificity | Are instructions concrete enough? |
| Strictness | Does it preserve no-sugarcoating feedback? |
| Usefulness | Can a candidate or AI use it immediately? |
| Structure | Is it easy to navigate? |
| Safety | Does it avoid private/copyrighted/fabricated content? |
| Continuity | Does it update progress/docs if needed? |

---

## 41. Code of Conduct

Contributors should be:

- respectful
- honest
- constructive
- precise
- open to feedback
- focused on candidate outcomes

Not tolerated:

- harassment
- discrimination
- personal attacks
- trolling
- sharing private information
- copying protected content
- intentionally adding false information

---

## 42. Recognition

Meaningful contributors can be credited in:

- README
- release notes
- contributor list
- relevant file comments

Examples of meaningful contributions:

- strong SQL guide
- realistic mock interview set
- detailed system design mode
- improved assessment rubric
- major accuracy fixes
- strong practice bank

---

## 43. License

By contributing, you agree that your contributions can be distributed under the project license.

MIT License is recommended for this repository unless maintainers decide otherwise.

---

## 44. Final Contribution Rule

Do not add content just to make the repository bigger.

Add content that makes the mentor stricter, smarter, more accurate, and more useful for Data Engineering interview preparation.

A strong contribution should help the candidate do at least one of these better:

- solve
- explain
- reason
- design
- defend
- improve
- recover from mistakes
- pass interviews
