# Lesson 3: Data Formats & Storage

**Time:** ~45 minutes

---

## Common formats

| Format | Best for | Pros | Cons |
|--------|----------|------|------|
| **CSV** | Small files, human-readable | Universal | No schema, slow at scale |
| **JSON** | Semi-structured, APIs | Flexible nesting | Verbose, inconsistent keys |
| **Parquet** | Analytics, big data | Columnar, compressed, typed | Not human-readable |
| **Avro** | Streaming schemas | Schema evolution | Less common in pandas workflows |

**Rule of thumb:** CSV/JSON at the edges; Parquet (or similar) in the warehouse/lake.

---

## Row vs column storage

- **Row-oriented (CSV, Postgres rows):** Fast for reading one record
- **Column-oriented (Parquet, warehouses):** Fast for aggregations (`SUM`, `AVG` on one column)

Analytics workloads almost always prefer columnar.

---

## Local practice in this course

You'll use:

- `shared/datasets/*.csv` — sample inputs
- `output/` folders — your pipeline outputs (gitignored)
- **DuckDB** — query CSV/Parquet with SQL locally (Phase 2+)

---

## Try it now (5 min)

```python
import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parents[3]  # adjust if running from elsewhere
orders = pd.read_csv(root / "shared/datasets/orders.csv")
print(orders.dtypes)
print(orders.head())
```

---

## Compression & partitioning (preview)

At scale, files are:

- **Compressed** (snappy, gzip) — less storage & network cost
- **Partitioned** by date (`year=2024/month=01/`) — query only relevant folders

Phase 7 covers this hands-on.

---

## Up next

Start [Exercise 1](../exercises/01-data-lifecycle-quiz.md)
