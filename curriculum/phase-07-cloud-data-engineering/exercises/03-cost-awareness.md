# Exercise 3: Cost Awareness

**Time:** ~30 minutes

---

## Goal

Measure the "small files" problem and partition pruning benefit locally.

---

## Tasks

Create `exercises/my_work/03_cost_awareness.py`:

1. **Small files test:** Write orders as 14 single-row Parquet files under `lake/bad/orders/dt=2024-01-15/row-{order_id}.parquet`. Time directory listing + DuckDB read of all files.

2. **Good layout test:** Write same data as one `part-0000.parquet` under `lake/good/orders/dt=2024-01-15/`. Time the same operations.

3. **Partition pruning:** Use DuckDB to read only `dt=2024-01-16` from good layout vs reading all `dt=*` folders. Compare row counts and explain which query would be cheaper in Athena/BigQuery.

4. Print a 3-line summary comparing approaches.

---

## Deliverable

Console output with timings (use `time.perf_counter()`).

---

## Verify

Compare approach with [solutions/03_cost_awareness.py](solutions/03_cost_awareness.py).

**Next:** [Phase project →](../project/README.md)
