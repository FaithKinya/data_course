# Lesson 2: Observability

**Time:** ~50 minutes

---

## Operators need answers fast

When Finance pings "numbers look wrong," you need:

1. Did the pipeline run?
2. Which task failed?
3. How many rows were loaded?
4. What changed since yesterday?

**Observability** = logs + metrics + traces for data systems.

---

## Structured logging

Plain text logs are hard to query. Use JSON:

```python
import json
import logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "ts": self.formatTime(record),
            "level": record.levelname,
            "msg": record.getMessage(),
            "pipeline": "shopstream_etl",
        })

log = logging.getLogger("shopstream")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
log.addHandler(handler)
log.info("extract_complete", extra={"rows": 14})
```

Ship to CloudWatch, Datadog, ELK — JSON parses cleanly.

---

## Correlation IDs

Generate `run_id` at pipeline start; include in every log line and metadata file. Trace one run end-to-end across Airflow tasks.

---

## Metrics worth tracking

| Metric | Type |
|--------|------|
| `pipeline_duration_seconds` | histogram |
| `rows_ingested` | counter |
| `validation_failures` | counter |
| `last_success_timestamp` | gauge |

Even a JSON metadata file per run is a start.

---

## Alerting rules

- Pipeline failed → page on-call
- Success but 0 rows → warn (sensor bug or empty source)
- Revenue ±50% vs yesterday → investigate before publishing

Avoid alert fatigue — actionable alerts only.

---

## Data lineage (preview)

OpenLineage, dbt docs, and Marquez show upstream/downstream. When a mart breaks, lineage finds which ingest changed.

---

## Reflection

1. What would you search in logs given only an `order_id`?
2. Why log row counts per stage?

---

## Up next

[Lesson 3: CI/CD for pipelines →](03-cicd-pipelines.md)
