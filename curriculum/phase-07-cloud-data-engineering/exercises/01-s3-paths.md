# Exercise 1: S3-Style Paths

**Time:** ~30 minutes

---

## Goal

Build a path helper that mirrors S3 key conventions on the local filesystem.

---

## Tasks

Create `exercises/my_work/01_s3_paths.py`:

1. Function `s3_uri(bucket, key) -> str` returning `s3://{bucket}/{key}`
2. Function `local_lake_path(root, layer, table, partition_col, partition_val) -> Path`
   - Example: `local_lake_path(ROOT, "raw", "orders", "dt", "2024-01-15")`
   - Returns `ROOT/lake/raw/orders/dt=2024-01-15/`
3. Function `partition_key(col, val) -> str` → `dt=2024-01-15`
4. Print URIs and local paths for orders partitions on 2024-01-15 and 2024-01-16

Use `ROOT = Path(__file__).resolve().parents[4]`.

---

## Verify

Compare with [solutions/01_s3_paths.py](solutions/01_s3_paths.py).

**Next:** [Exercise 2: Partitioned writes](02-partitioned-writes.md)
