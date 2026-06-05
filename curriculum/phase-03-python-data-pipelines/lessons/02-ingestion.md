# Lesson 2: Ingestion Patterns

**Time:** ~50 minutes

---

## Ingestion = getting data into your control

Sources you'll see:

- **Files** — CSV, JSON, Parquet drops in S3/FTP
- **APIs** — paginated REST, rate limits
- **Databases** — CDC, timestamp-based incremental queries
- **Streams** — Kafka (Phase 6)

This phase focuses on **file-based batch** ingestion.

---

## Full vs incremental loads

| Pattern | When | Risk |
|---------|------|------|
| **Full snapshot** | Small tables, daily exports | Overwrites; simple |
| **Incremental** | Large fact tables | Missed rows if watermark wrong |
| **CDC** | OLTP replication | Complex; most accurate |

ShopStream CSVs are daily full snapshots — replace or merge by primary key.

---

## Reading multiple files with pandas

```python
import pandas as pd
from pathlib import Path

def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing source: {path}")
    return pd.read_csv(path, parse_dates=["order_date"])
```

Always set `parse_dates` explicitly for date columns.

---

## Schema drift

Sources add columns without telling you. Defensive ingestion:

```python
REQUIRED = {"order_id", "customer_id", "product_id", "order_date", "quantity", "unit_price", "status"}
missing = REQUIRED - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {missing}")
```

Log **extra** columns instead of failing — they might be useful later.

---

## Encoding and parsing pitfalls

- UTF-8 BOM in CSV → use `encoding="utf-8-sig"`
- Mixed date formats → `pd.to_datetime(..., errors="coerce")` then count nulls
- Implicit type inference → pass `dtype=` for IDs (avoid `1001` → float)

---

## Landing zone pattern

```
landing/     raw copies (immutable audit)
staging/     parsed DataFrames / Parquet
marts/       business-ready tables
```

Never mutate `landing/` files. Reprocessing starts from landing.

---

## Reflection

1. Why parse `order_id` as string or int consistently?
2. What watermark column would you use for incremental orders?

---

## Up next

[Lesson 3: Transform & load →](03-transform-load.md)
