# File Generation Log

This file tracks generated and pending files for the public reusable skill.

## Status Values

```text
generated
needs_review
empty_filled
pending
deprecated
```

## Canonical Files

| File | Status | Notes |
|---|---|---|
| `SKILL.md` | needs_review | Main router and operating instructions |
| `README.md` | needs_review | Public usage and structure docs |
| `CONTRIBUTING.md` | needs_review | Contribution standards |
| `CHANGELOG.md` | needs_review | History and status |
| `docs/dsa-for-data-engineering.md` | empty_filled | Canonical DSA guide |
| `docs/warehouse-cloud-guide.md` | empty_filled | Canonical warehouse/cloud bridge |
| `docs/project-deep-dive-guide.md` | empty_filled | Canonical project explanation guide |
| `practice/sql/sql-drills.md` | empty_filled | SQL drill index |
| `practice/python/python-drills.md` | empty_filled | Python drill index |
| `practice/dsa/high-roi-leetcode-list.md` | empty_filled | DSA problem index |
| `practice/system-design/system-design-prompts.md` | empty_filled | System design prompt index |
| `practice/mixed-interviews/mixed-interview-sets.md` | empty_filled | Mixed mock sets |
| `progress/*.md` | empty_filled | Public reusable progress templates |
| `templates/answer-frameworks/*.md` | empty_filled | Answer frameworks |
| `templates/interview-feedback/mock-interview-feedback-template.md` | empty_filled | Mock feedback template |
| `templates/progress/session-summary-template.md` | empty_filled | Session summary template |

## Maintenance Rule

Do not mark a file as complete if it is only a placeholder. If a file contains candidate-specific content, mark it `needs_review`.
