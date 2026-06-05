# Lesson 1: Data Quality

**Time:** ~50 minutes

---

## Bad data is expensive

- Dashboard shows 2× revenue → wrong budget decisions
- ML model trained on duplicates → bad recommendations
- Compliance report missing rows → regulatory risk

**Data quality** is not optional in production pipelines.

---

## Dimensions of quality

| Dimension | Question |
|-----------|----------|
| **Accuracy** | Does it match reality? |
| **Completeness** | Are rows/columns missing? |
| **Consistency** | Same rules everywhere? |
| **Timeliness** | Arrived on schedule? |
| **Uniqueness** | Duplicate keys? |
| **Validity** | Values in allowed set/range? |

---

## Where to test

1. **Source** — reject bad ingests early
2. **Staging** — dbt tests (Phase 5)
3. **Pre-load gate** — block poisoned data
4. **Post-load monitor** — anomaly detection on metrics

Shift left: cheapest to fix at ingestion.

---

## Great Expectations (GX)

Define **expectations** on DataFrames or SQL:

```python
import great_expectations as gx

context = gx.get_context()
validator = context.sources.pandas_default.read_dataframe(orders_df)
validator.expect_column_values_to_not_be_null("order_id")
validator.expect_column_values_to_be_in_set("status", ["completed", "cancelled", "refunded"])
results = validator.validate()
```

Failed expectations → alert, quarantine, or halt pipeline.

---

## dbt tests vs GX

| Tool | Layer | Best for |
|------|-------|----------|
| **dbt tests** | Warehouse SQL models | Analyst-owned mart rules |
| **GX** | Python pipelines, files | Ingestion validation |

Use both — they complement.

---

## Anomaly checks (lightweight)

Track daily row count and revenue totals. Alert if > 3σ from 7-day mean. No ML required to start.

---

## Reflection

1. Which quality dimension does `unique(order_id)` test?
2. Should bad rows fail the whole pipeline or quarantine?

---

## Up next

[Lesson 2: Observability →](02-observability.md)
