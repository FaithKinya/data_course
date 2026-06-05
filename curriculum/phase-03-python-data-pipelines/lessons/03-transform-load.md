# Lesson 3: Transform & Load

**Time:** ~50 minutes

---

## Transform: where business logic lives

Reuse Phase 1 rules:

- Drop or flag invalid rows (`quantity <= 0`)
- Exclude `cancelled` from revenue reports
- Treat `refunded` as negative revenue
- Join dimensions (customers, products)

Keep transforms **pure functions**: `DataFrame in → DataFrame out`.

---

## Validation before load

```python
def validate_orders(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    valid_mask = (df["quantity"] > 0) & df["order_id"].notna()
    valid = df[valid_mask].copy()
    rejects = df[~valid_mask].copy()
    return valid, rejects
```

Write rejects to `output/rejects/orders_{run_id}.csv` for investigation.

---

## Idempotent loads

**Problem:** Pipeline runs twice → duplicate rows in warehouse.

**Strategies:**

1. **Full partition overwrite** — `output/orders/dt=2024-01-20/` replaced each run
2. **Merge by key** — upsert on `order_id`
3. **Append + dedupe** — load then `DROP DUPLICATES` (slowest)

For local Parquet:

```python
def load_parquet(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".parquet.tmp")
    df.to_parquet(tmp, index=False)
    tmp.replace(path)  # atomic on same filesystem
```

---

## Load formats

| Format | Use case |
|--------|----------|
| **Parquet** | Analytics default — columnar, compressed |
| **CSV** | Human-readable reports |
| **JSON** | Metadata, small config payloads |

One Parquet file per table per run is fine for learning; production uses partitioned folders.

---

## Logging

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("shopstream_etl")
log.info("Loaded %d orders", len(df))
```

Structured logs (JSON) come in Phase 8.

---

## End-to-end checklist per run

1. Generate `run_id` (UTC timestamp)
2. Extract all sources
3. Validate → split valid/rejects
4. Transform valid rows
5. Load to staging + marts
6. Write `run_metadata.json`
7. Exit non-zero on failure (for orchestrators in Phase 4)

---

## Reflection

1. Which idempotency strategy fits ShopStream daily CSV drops?
2. What would you put in `run_metadata.json` beyond row counts?

---

## Up next

[Exercise 1: Read multiple sources →](../exercises/01-read-sources.md)
