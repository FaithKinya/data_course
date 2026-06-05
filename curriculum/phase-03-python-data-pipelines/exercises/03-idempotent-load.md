# Exercise 3: Idempotent Loads

**Time:** ~45 minutes

---

## Goal

Write Parquet output that produces identical results when the pipeline runs twice.

---

## Tasks

Create `curriculum/phase-03-python-data-pipelines/exercises/my_work/03_idempotent_load.py`:

1. Reuse validation/revenue logic from Exercise 2
2. Load to `exercises/my_work/output/orders.parquet` using **atomic write** (temp file + rename)
3. Write `exercises/my_work/output/run_metadata.json` with:
   - `run_id` (ISO timestamp)
   - `input_rows`, `valid_rows`, `reject_rows`
   - `output_path`
   - `checksum` (md5 of parquet file bytes)
4. Run the script **twice**; confirm row count and checksum match

---

## Acceptance

- Second run does not duplicate or corrupt parquet
- Metadata updated with new `run_id` but same `checksum` (same input data)

---

## Verify

Compare with [solutions/03_idempotent_load.py](solutions/03_idempotent_load.py).

**Next:** [Phase project →](../project/README.md)
