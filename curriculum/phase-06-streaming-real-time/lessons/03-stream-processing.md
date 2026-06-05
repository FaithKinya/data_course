# Lesson 3: Stream Processing

**Time:** ~50 minutes

---

## Processing patterns

1. **Stateless map** — enrich each event (add geo from IP)
2. **Aggregation** — count views per page
3. **Windowing** — counts per 5-minute window
4. **Join** — stream-stream or stream-table join

This phase covers 1–3 in plain Python consumers.

---

## Running counts

```python
counts: dict[str, int] = {}
for msg in consumer:
    page = msg.value["page"]
    counts[page] = counts.get(page, 0) + 1
    print(counts)
```

State lives in memory — lost on restart unless you persist to RocksDB/DB (Flink/ksqlDB do this for you).

---

## Tumbling windows (manual)

Bucket events by floored timestamp:

```python
from datetime import datetime, timezone

def window_key(ts_iso: str, minutes: int = 5) -> str:
    ts = datetime.fromisoformat(ts_iso.replace("Z", "+00:00"))
    bucket_min = (ts.minute // minutes) * minutes
    floored = ts.replace(minute=bucket_min, second=0, microsecond=0)
    return floored.isoformat()
```

Count per `(window_key, page)` tuple.

---

## Watermarks & late data (concept)

Real streams have **late events**. Production frameworks drop or side-output events past a watermark. For learning, assume events arrive in order.

---

## Sink options

| Sink | Use |
|------|-----|
| stdout | Learning |
| JSON file | Demo persistence |
| DuckDB/Postgres | Micro-aggregation store |
| S3 | Archive (Phase 7) |

Flush aggregates every N seconds for dashboards.

---

## Backpressure

If producer outpaces consumer, lag grows. Monitor **consumer lag** (offset behind latest). Scale consumers up to partition count.

---

## Reflection

1. Why is in-memory state risky for production?
2. How would you persist counts without Flink?

---

## Up next

[Exercise 1: Produce events →](../exercises/01-produce-events.md)
