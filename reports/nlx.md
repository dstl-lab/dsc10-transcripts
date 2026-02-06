# AI Tutor Usage Report: student-nlx

## Overview

| Metric | Value |
|---|---|
| Total messages in conversation | 246 |
| Student messages | 152 |
| AI tutor responses | 94 |
| Conversation period | Jan 28 – Feb 5, 2026 |
| Number of conversations | 1 (single continuous session) |

student-nlx is the 4th most active user in the database by total message count.

## Topics and Assignments

student-nlx used the AI tutor across multiple assignments covering core DSC 10 topics:

- **DataFrames and babypandas**: Groupby, merge, filtering, column selection, `.assign()` (Fortune 500, ArtPower events, Broadway, baby names, cereals, national parks)
- **Control flow and functions**: Implementing `calculate_interest`, `monthly_payment`, `emojify` (Tritonmobile car calculator, Wordle)
- **Iteration and for-loops**: String iteration vs list iteration, building arrays with loops (Great Gatsby word analysis)
- **Probability**: Independent events, complementary probability (Dirty Birds, Triton Spirit Night Lotto)
- **Plotting and visualization**: Line plots, histograms, `figsize` parameters (baby name popularity, flight delays)

## Interaction Patterns

### Message classification (of 152 student messages)

| Category | Count | Description |
|---|---|---|
| "How" questions | 17 | "how should I approach...", "how do I...", "how can I..." |
| "Why" questions | 39 | "why is there an error", "why does this...", "why is this wrong" |
| Assistance requests | 25 | "can you assist me", "can you guide me through...", "can you help me with..." |
| Error / failure reports | 18 | Messages mentioning errors, tracebacks, or error messages |
| Wrong / not passing | 27 | "why is this wrong", "test not passing", "still wrong", "test fail" |
| Question context pastes | 79 | Messages pasting the full question text with `[Context: ...]` |
| Conceptual questions | 5 | "what is the difference between...", "what is the function of..." |
| Responsiveness pings | 7 | "hello?" messages when tutor seemed unresponsive |

### Comparison with student-rbm

student-nlx's usage pattern differs from the highest-volume user (student-rbm) in several notable ways:

| Behavior | student-rbm | student-nlx |
|---|---|---|
| Direct answer demands | 12 ("just tell me what to write") | 0 |
| "Why" questions | Very few | 39 (25% of messages) |
| "How should I approach" | Rare | 17 (11% of messages) |
| Conceptual questions | Nearly none | 5 |
| Frustration expressions | Frequent ("your wrong again") | Moderate, more measured |

student-nlx asked *why* things weren't working rather than simply demanding answers, and frequently asked *how to approach* a problem before diving in — indicating more engagement with the learning process.

### Typical interaction flow

student-nlx's interactions generally followed this pattern:

1. **"how should I approach X.Y"** — asks for strategy before attempting
2. AI tutor provides a guided explanation
3. Student attempts the problem, encounters an error
4. **"why is there an error" / "why is this wrong"** — asks for explanation of the failure
5. AI tutor explains; student iterates

When stuck for extended periods, the pattern shifted to repeated "can you assist me?" and "hello?" pings, suggesting frustration with either the tutor's responsiveness or the clarity of its guidance.

### Notable struggles

Several questions required many attempts:

- **Question 1.1 (national parks species_counts)**: 7 messages — struggled with groupby output format, asked "why does my code not work", "how do I drop other columns", "why does get([]) return a dataframe"
- **Question 1.3 (species_category)**: 6 messages — repeated "why is there an error" messages, indicating persistent confusion about groupby aggregation
- **Question 2.2 (cereal merge understanding)**: 6 messages — "why is the test not passing" asked 3 times, "this is not correct", "the test is still not passing"
- **Questions 5.2–5.3 (Lotto probability)**: 6 messages — "why did the test case fail for 5.2" repeated, "this is still wrong", "why are 5.2 and 5.3 not passing"
- **Question 3.2 (calculate_principal)**: 6 messages — "why did this calculate principal function" asked 4 times across different context windows
- **Broadway questions 2.3–2.10**: Asked to be guided through all of them in sequence, with multiple "hello?" pings suggesting the tutor was not responding or the student was losing patience

### Responsiveness concerns

student-nlx sent 7 "hello?" messages throughout the conversation, sometimes multiple in a row:
- "hello?" → "can you assist me?" → "hello? can you assist me?"
- "hello?" appearing before several sections of questions

This suggests the student experienced delays or perceived unresponsiveness from the tutor, which may have contributed to frustration.

## Key Observations

1. **More inquiry-oriented than answer-seeking**: Unlike some high-volume users, student-nlx never demanded direct answers. Their messages consistently asked "why" and "how to approach," showing an attempt to understand the material rather than just get through the assignment.

2. **Persistent debugging struggles**: Despite asking good questions, student-nlx frequently got stuck in loops on the same question — particularly around groupby operations, merge behavior, and probability calculations. The tutor's explanations may not have been effectively addressing the student's specific misconceptions.

3. **Broad coverage, question-by-question**: Like other high-volume users, student-nlx worked through assignments question by question with the tutor, covering homework and lab assignments on DataFrames, functions, iteration, and probability.

4. **Tutor responsiveness issues**: The repeated "hello?" messages suggest a friction point in the interaction — either technical latency or the student feeling that the tutor's responses weren't addressing their questions, prompting them to re-engage.

5. **Conceptual curiosity present but limited**: The student asked a few genuinely conceptual questions (e.g., "why does iteration over a string print out a column while iteration over a list print out a normal row", "what is the difference between..."), indicating some intellectual curiosity, though most messages remained task-focused.

6. **Single continuous session**: All 246 messages occurred in one conversation over about 8 days, similar to other high-volume users.
