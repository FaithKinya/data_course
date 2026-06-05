# Lesson 2: Object Storage Patterns

**Time:** ~50 minutes

---

## S3-style URIs

```
s3://shopstream-lake/raw/orders/dt=2024-01-15/part-0000.parquet
│    │              │   │      │              │
│    │              │   │      partition      file
│    │              │   table
│    │              layer (raw/curated)
│    bucket
scheme
```

Locally we use: `project/lake/raw/orders/dt=2024-01-15/part-0000.parquet`

---

## Hive-style partitioning

Directory names encode column values: `dt=2024-01-15`, `country=USA`.

**Benefits:**

- Query engines skip irrelevant folders (partition pruning)
- Easy incremental loads — add new `dt=` folder daily

**Rules:**

- Partition on columns you filter often (date, region)
- Avoid high-cardinality partitions (user_id) — millions of folders

---

## File sizing

Target **128 MB – 1 GB** per file in production.

| Problem | Symptom | Fix |
|---------|---------|-----|
| **Small files** | Slow listings, metadata overhead | Compact/coalesce |
| **Huge files** | Poor parallelism | Split by partition |

ShopStream exercises use tiny files — note the production guidance.

---

## Write patterns

1. **Append daily partition** — `dt={{ ds }}` idempotent overwrite
2. **Manifest file** — `_SUCCESS` or `manifest.json` signals completeness
3. **Versioning** — S3 versioning for accidental delete protection

```json
{"dataset": "orders", "partition": "dt=2024-01-15", "rows": 14, "files": 1}
```

---

## Python partitioned write

```python
for dt, group in df.groupby("order_date"):
    path = lake / f"raw/orders/dt={dt}/part-0000.parquet"
    path.parent.mkdir(parents=True, exist_ok=True)
    group.to_parquet(path, index=False)
```

---

## Reflection

1. Why partition by `order_date` not `order_id`?
2. What signals downstream that a partition is ready?

---

## Up next

[Lesson 3: Managed warehouses →](03-managed-warehouses.md)
