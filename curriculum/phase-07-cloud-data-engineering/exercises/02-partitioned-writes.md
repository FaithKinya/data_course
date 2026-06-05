# Exercise 2: Partitioned Writes

**Time:** ~45 minutes

---

## Goal

Load ShopStream orders into hive-partitioned Parquet and query one partition with DuckDB.

---

## Tasks

Create `exercises/my_work/02_partitioned_writes.py`:

1. Read `shared/datasets/orders.csv`
2. Add `dt` column from `order_date` as `YYYY-MM-DD`
3. Write each date to:
   `exercises/my_work/lake/raw/orders/dt={date}/part-0000.parquet`
4. Write `exercises/my_work/lake/raw/orders/_manifest.json` listing partitions and row counts
5. Query one partition with DuckDB `read_parquet` and print row count

---

## Acceptance

- One folder per distinct `order_date`
- Re-run overwrites partition files (idempotent per `dt`)

---

## Verify

Compare with [solutions/02_partitioned_writes.py](solutions/02_partitioned_writes.py).

**Next:** [Exercise 3: Cost awareness](03-cost-awareness.md)
