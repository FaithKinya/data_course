# Phase 3: Python Data Pipelines

**Goal:** Build reliable batch pipelines with ingestion, validation, and idempotent loads.

**Time:** ~1–2 weeks (10–14 hours)

**Prerequisites:** [Phase 2: SQL & Data Modeling](../phase-02-sql-data-modeling/README.md)

---

## What You'll Learn

- Pipeline structure: extract → validate → transform → load
- Reading multiple sources and handling schema drift
- Data validation patterns (not just hope-and-pray)
- Idempotent loads so re-runs don't duplicate data

---

## Learning Path

Complete in order:

| # | Type | Item | Time |
|---|------|------|------|
| 1 | Lesson | [Pipeline anatomy](lessons/01-pipeline-anatomy.md) | 50 min |
| 2 | Lesson | [Ingestion patterns](lessons/02-ingestion.md) | 50 min |
| 3 | Lesson | [Transform & load](lessons/03-transform-load.md) | 50 min |
| 4 | Exercise | [Read multiple sources](exercises/01-read-sources.md) | 30 min |
| 5 | Exercise | [Clean & validate](exercises/02-clean-validate.md) | 45 min |
| 6 | Exercise | [Idempotent loads](exercises/03-idempotent-load.md) | 45 min |
| 7 | **Project** | [**Batch ETL Pipeline**](project/README.md) | 5–7 hrs |

---

## Phase Project Preview

A production-style Python ETL that ingests all three ShopStream CSVs, validates rows, and loads Parquet datasets with run metadata — safe to re-run.

---

## Success Criteria

Before moving to Phase 4, you should be able to:

- [ ] Structure pipeline code into testable functions/modules
- [ ] Validate dtypes, nulls, and business rules before load
- [ ] Implement upsert or overwrite strategies for idempotency
- [ ] Write run metadata JSON on every execution
- [ ] Complete the phase project checklist

---

## Next Phase

[Phase 4: ETL Orchestration →](../phase-04-etl-orchestration/README.md)
