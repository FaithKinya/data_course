# Phase 5: Data Warehousing

**Goal:** Transform raw data into analytics marts with dbt and DuckDB.

**Time:** ~1–2 weeks (10–14 hours)

**Prerequisites:** [Phase 4: ETL Orchestration](../phase-04-etl-orchestration/README.md)

---

## What You'll Learn

- OLTP vs OLAP and the modern warehouse stack
- dbt projects: staging → intermediate → marts
- Tests, documentation, and incremental models
- DuckDB as a local warehouse target

---

## Learning Path

Complete in order:

| # | Type | Item | Time |
|---|------|------|------|
| 1 | Lesson | [OLTP vs OLAP](lessons/01-oltp-vs-olap.md) | 45 min |
| 2 | Lesson | [Intro to dbt](lessons/02-intro-dbt.md) | 50 min |
| 3 | Lesson | [Incremental models](lessons/03-incremental-models.md) | 50 min |
| 4 | Exercise | [Staging models](exercises/01-staging-models.md) | 45 min |
| 5 | Exercise | [dbt tests](exercises/02-dbt-tests.md) | 45 min |
| 6 | Exercise | [Documentation](exercises/03-documentation.md) | 30 min |
| 7 | **Project** | [**dbt Analytics Project**](project/README.md) | 6–8 hrs |

---

## Setup note

Install dbt with DuckDB adapter:

```bash
pip install dbt-duckdb
```

---

## Phase Project Preview

A full dbt project loading ShopStream CSVs into DuckDB, with staging models, revenue marts, tests, and generated docs.

---

## Success Criteria

Before moving to Phase 6, you should be able to:

- [ ] Explain staging vs marts layer purposes
- [ ] Run `dbt run` and `dbt test` successfully
- [ ] Write a `schema.yml` with tests and descriptions
- [ ] Build at least one mart model joining facts and dimensions
- [ ] Complete the phase project checklist

---

## Next Phase

[Phase 6: Streaming & Real-Time →](../phase-06-streaming-real-time/README.md)
