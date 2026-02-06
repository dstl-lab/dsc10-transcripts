# Student-AI Conversation Statistics

**Data range:** Jan 20, 2026 -- Feb 6, 2026 (~17 days)

## Overview

| Metric | Value |
|---|---|
| Assignments | 2 |
| Unique students | 162 |
| Total conversations | 162 (1 per student) |
| Total messages | 6,869 |
| Avg messages/conversation | 42.4 |

## Message Patterns by Role

| Role | Messages | Avg Length (chars) | Max Length |
|---|---|---|---|
| STUDENT | 3,966 (58%) | 174 | 30,059 |
| AI_TUTOR | 2,903 (42%) | 2,150 | 4,966 |

Students send ~1.4x more messages than the AI, but AI responses are ~12x longer on average. The 30K-char max student message likely indicates pasted code/output.

## Conversation Depth Distribution

| Depth | Count | % |
|---|---|---|
| Single message (abandoned) | 12 | 7.4% |
| Quick (2-5 msgs) | 39 | 24.1% |
| Medium (6-20 msgs) | 39 | 24.1% |
| Extended (21-50 msgs) | 24 | 14.8% |
| Deep (50+ msgs) | 48 | 29.6% |

Nearly 30% of students had deep conversations (50+ messages), suggesting substantial engagement. One conversation reached 346 messages.

## Student Message Length

| Bucket | Count |
|---|---|
| 1-50 chars | 1,587 (40%) |
| 51-200 chars | 1,489 (38%) |
| 201-500 chars | 678 (17%) |
| 500+ chars | 212 (5%) |

78% of student messages are under 200 characters -- mostly short questions and follow-ups.

## Temporal Patterns (UTC)

| Hour (UTC) | Conversations |
|---|---|
| 00:00 | 6 |
| 01:00 | 12 |
| 02:00 | 10 |
| 03:00 | 6 |
| 04:00 | 9 |
| 05:00 | 13 |
| 06:00 | 27 |
| 07:00 | 9 |
| 08:00 | 5 |
| 09:00 | 2 |
| 10:00 | 2 |
| 13:00 | 1 |
| 16:00 | 1 |
| 18:00 | 5 |
| 19:00 | 3 |
| 20:00 | 20 |
| 21:00 | 11 |
| 22:00 | 9 |
| 23:00 | 11 |

Peak activity at 06:00 UTC (27 convos) and 20:00 UTC (20 convos) -- likely corresponding to late evening and afternoon in Pacific time for UCSD students.

## Assignment Breakdown

| Assignment | Students | Avg msgs/convo |
|---|---|---|
| Assignment 1 (0695ea16-733f...) | 159 | 41.5 |
| Assignment 2 (0695ea16-df80...) | 3 | 89.3 |

Assignment 2 has only 3 students but with much deeper engagement (89 avg messages).

## Key Takeaways

- **Bimodal engagement**: Students either had short interactions (<=5 msgs, 31%) or very deep ones (50+ msgs, 30%).
- **Students ask, AI explains**: The ratio of short student queries to long AI responses is consistent with a tutoring dynamic.
- **High per-student engagement**: Average of 24.5 student turns per conversation shows this is not a one-question tool for most users.
