# Phase 1: Foundations

**Goal:** Understand what data engineers do and build your first local data pipeline.

**Time:** ~1–2 weeks (8–12 hours)

**Prerequisites:** [Environment setup](../../docs/SETUP.md)

---

## What You'll Learn

- The data engineering role vs data science / analytics
- The data lifecycle: ingest → store → transform → serve
- Common file formats (CSV, JSON, Parquet)
- Your first Python transform script

---

## Learning Path

Complete in order:

| # | Type | Item | Time |
|---|------|------|------|
| 1 | Lesson | [What is Data Engineering?](lessons/01-what-is-data-engineering.md) | 45 min |
| 2 | Lesson | [Data Lifecycle](lessons/02-data-lifecycle.md) | 45 min |
| 3 | Lesson | [Data Formats & Storage](lessons/03-data-formats.md) | 45 min |
| 4 | Exercise | [Data lifecycle quiz](exercises/01-data-lifecycle-quiz.md) | 20 min |
| 5 | Exercise | [Explore a CSV dataset](exercises/02-explore-csv.md) | 30 min |
| 6 | Exercise | [Write your first transform](exercises/03-first-transform.md) | 45 min |
| 7 | **Project** | [**Local CSV Pipeline**](project/README.md) | 4–6 hrs |

---

## Phase Project Preview

You will build a pipeline that:

1. Reads raw order data from CSV
2. Cleans invalid rows and computes revenue
3. Writes a summary report and cleaned Parquet file

This pattern — **extract → transform → load** — repeats in every later phase.

---

## Success Criteria

Before moving to Phase 2, you should be able to:

- [ ] Explain ETL in your own words
- [ ] Load a CSV with pandas and inspect shape, dtypes, nulls
- [ ] Filter rows and create a new column
- [ ] Save output to a new file format (Parquet)
- [ ] Complete the phase project checklist

---

## Next Phase

[Phase 2: SQL & Data Modeling →](../phase-02-sql-data-modeling/README.md)
