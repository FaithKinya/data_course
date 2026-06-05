# Phase 2: SQL & Data Modeling

**Goal:** Write analytical SQL, understand normalization, and build a star schema in DuckDB.

**Time:** ~1–2 weeks (10–14 hours)

**Prerequisites:** [Phase 1: Foundations](../phase-01-foundations/README.md)

---

## What You'll Learn

- SQL SELECT, JOIN, GROUP BY for analytics
- Normal forms and when to denormalize
- Dimensional modeling: facts, dimensions, star schema
- DuckDB as a local analytical engine

---

## Learning Path

Complete in order:

| # | Type | Item | Time |
|---|------|------|------|
| 1 | Lesson | [SQL Refresher](lessons/01-sql-refresher.md) | 50 min |
| 2 | Lesson | [Normalization](lessons/02-normalization.md) | 50 min |
| 3 | Lesson | [Dimensional Modeling](lessons/03-dimensional-modeling.md) | 50 min |
| 4 | Exercise | [SELECT practice](exercises/01-select-practice.md) | 30 min |
| 5 | Exercise | [JOINs & aggregations](exercises/02-joins-aggregations.md) | 45 min |
| 6 | Exercise | [Design a schema](exercises/03-schema-design.md) | 45 min |
| 7 | **Project** | [**Star Schema Mini-Mart**](project/README.md) | 5–7 hrs |

---

## Phase Project Preview

You will load ShopStream CSVs into DuckDB, model a star schema (`fact_orders`, dimension tables), and answer business questions with SQL.

---

## Success Criteria

Before moving to Phase 3, you should be able to:

- [ ] Write JOIN + GROUP BY queries without copying from a cheat sheet
- [ ] Explain 3NF in plain language
- [ ] Draw a star schema for orders/customers/products
- [ ] Run SQL in DuckDB against local CSV files
- [ ] Complete the phase project checklist

---

## Next Phase

[Phase 3: Python Data Pipelines →](../phase-03-python-data-pipelines/README.md)
