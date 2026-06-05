# Phase 8: Production & Pro Practices

**Goal:** Ship pipelines with data quality checks, structured logging, and data contracts.

**Time:** ~1–2 weeks (10–14 hours)

**Prerequisites:** [Phase 7: Cloud Data Engineering](../phase-07-cloud-data-engineering/README.md)

---

## What You'll Learn

- Data quality frameworks (Great Expectations)
- Observability: structured logging and run metadata
- Data contracts between producers and consumers
- CI/CD concepts for pipeline code

---

## Learning Path

Complete in order:

| # | Type | Item | Time |
|---|------|------|------|
| 1 | Lesson | [Data quality](lessons/01-data-quality.md) | 50 min |
| 2 | Lesson | [Observability](lessons/02-observability.md) | 50 min |
| 3 | Lesson | [CI/CD for pipelines](lessons/03-cicd-pipelines.md) | 50 min |
| 4 | Exercise | [Great Expectations intro](exercises/01-great-expectations.md) | 45 min |
| 5 | Exercise | [Pipeline logging](exercises/02-pipeline-logging.md) | 45 min |
| 6 | Exercise | [Data contracts](exercises/03-data-contracts.md) | 45 min |
| 7 | **Project** | [**Production-Ready Pipeline**](project/README.md) | 6–8 hrs |

---

## Phase Project Preview

Wrap ShopStream ETL with Great Expectations suites, JSON structured logs, a YAML data contract, and a failing-fast validation gate.

---

## Success Criteria

Before graduation, you should be able to:

- [ ] Define and run expectations on a dataset
- [ ] Emit structured JSON logs from a pipeline
- [ ] Author a data contract specifying schema and SLAs
- [ ] Block loads when validation fails
- [ ] Complete the phase project checklist

---

## Next

[Capstone A: E-commerce Analytics Platform →](../../capstones/capstone-01-ecommerce-analytics/README.md)
