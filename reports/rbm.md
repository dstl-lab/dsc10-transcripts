# AI Tutor Usage Report: student-rbm

## Overview

| Metric | Value |
|---|---|
| Total messages in conversation | 346 |
| Student messages | 196 |
| AI tutor responses | 150 |
| Conversation period | Jan 21 – Feb 5, 2026 |
| Number of conversations | 1 (single continuous session) |

student-rbm is the highest-volume user in the database, with 346 total messages — significantly more than the next most active student (264 messages).

## Topics and Assignments

student-rbm used the AI tutor to work through nearly every question across multiple homework and lab assignments. Topics covered include:

- **DataFrames and babypandas**: Filtering, groupby, merge, column access, `.shape`, `.assign()` (IMDB movies, Fortune 500, ArtPower events, Broadway, baby names, cereals, national parks)
- **Control flow and functions**: Implementing functions like `coffee_price`, `calculate_interest`, `monthly_payment`, `emojify` (Wordle game, Tritonmobile car calculator)
- **Probability**: Independent events, complementary probability (Dirty Birds food supply, Triton Spirit Night Lotto)
- **Plotting**: Line plots, scatter plots, seasonal variation analysis (Broadway ticket data, baby name popularity)
- **Data manipulation**: String processing, type conversion, arithmetic on columns (Fortune 500 revenue strings, population data)

## Interaction Patterns

### Message classification (of 196 student messages)

| Category | Count | Description |
|---|---|---|
| Generic help requests | 72 | Messages starting with "help with X.Y" |
| Question context pastes | 79 | Messages pasting the full question text with `[Context: ...]` |
| Error traceback pastes | 19 | Messages pasting Python tracebacks (NameError, AttributeError, TypeError) |
| Frustration / "it's wrong" | 21 | Messages like "still not working", "that's wrong", "your wrong again" |
| Direct answer requests | 12 | Messages like "just tell me what to write", "give me the answer" |

### Typical interaction flow

A recurring pattern across assignments:

1. **"help with X.Y"** — student requests help on a specific question number
2. AI tutor provides a scaffolded, step-by-step explanation
3. **Error paste** — student tries something, gets an error, pastes the traceback
4. AI tutor explains the error and suggests a fix
5. **"it's still wrong" / "that's wrong"** — student reports the fix didn't work
6. Cycle repeats, sometimes escalating to **"just tell me what to write"**

### Escalation examples

Several exchanges show a pattern of escalating frustration:

- Question 4.3 (IMDB averages): "help with 4.3" → "what do I do" → "tell me what to write" → "says its wrong" → "4.3.2 what do I fix"
- Question 3.5 (Fortune 500 sectors): "help with 3.5" → error paste → "still says that wrong just tell me what to write all within these box to make its right" → "its saying its not right" → re-pastes question text → another error
- Question 1.5 (ArtPower): "help with question 1.5" → "only tell me what to write instead of the elpses don't give me comments or nothing" → "that's wrong" → "your wrong again" → asked about 1.5 four more times
- Question 1.1 (later assignment): "help with 1.1" → "it doesn't work" → "give me the answer to 1.1" → "remember we are only in babypandas"

### Repeated questions

Several questions were asked about many times across the conversation, indicating sustained difficulty:

- **Question 3.1 (calculate_interest)**: Asked about 6 times across separate attempts
- **Question 3.2 (Triton discount)**: Asked about 6 times
- **Question 1.5 (ArtPower)**: Asked about 5 times
- **Question 1.3 (national parks species_category)**: Asked about 6 times
- **Question 2.6 (Broadway seasonal plot)**: Asked about 7 times

## Key Observations

1. **Question-by-question dependence**: student-rbm used the tutor for virtually every question in every assignment rather than selectively seeking help on difficult problems. This suggests reliance on the tutor as a primary problem-solving tool rather than a supplementary resource.

2. **Minimal conceptual engagement**: The vast majority of student messages are short requests for help on a question number, error pastes, or complaints that the answer is wrong. There are very few messages asking *why* something works, exploring concepts, or attempting to reason through a problem.

3. **Preference for direct answers over scaffolding**: When the tutor's guided approach didn't quickly resolve the issue, student-rbm frequently asked to be told exactly what to type ("just tell me what to write in the box", "only tell me what to write instead of the elpses don't give me comments or nothing").

4. **Debugging by re-asking**: Rather than reading error messages and attempting to debug, the student's pattern was to paste the traceback and ask the tutor to fix it, or simply say "it's wrong" without providing details about what went wrong.

5. **Single marathon session**: All 346 messages occurred in one continuous conversation, suggesting the student may have used the tutor as a constant companion while working through assignments rather than attempting problems independently first.
