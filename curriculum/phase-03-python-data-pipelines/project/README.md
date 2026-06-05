# Phase 3 Project: Batch ETL Pipeline

**Time:** 5–7 hours  
**Deliverable:** Modular Python ETL with validation, idempotent loads, and metadata

---

## Scenario

ShopStream IT delivers three CSV exports nightly. Build a **batch ETL pipeline** that ingests, validates, transforms, and loads analytics-ready Parquet — safe to re-run after failures.

---

## Requirements

### 1. Module structure

```
project/
├── pipeline.py       # entry point
├── extract.py        # read CSVs
├── validate.py       # schema + business rules
├── transform.py      # joins, revenue, enrichments
├── load.py           # atomic Parquet writes
├── README.md
├── CHECKLIST.md
└── output/           # generated (gitignored)
    ├── staging/
    ├── marts/
    ├── rejects/
    └── run_metadata.json
```

### 2. Extract

Read from `shared/datasets/`:
- `orders.csv`, `customers.csv`, `products.csv`

### 3. Validate

- Required columns present on each table
- Orders: `quantity > 0`, valid `status`, non-null IDs
- Write invalid order rows to `output/rejects/orders_{run_id}.csv`

### 4. Transform

- Join orders + customers + products
- Compute `revenue` (same rules as Phase 1/3 exercises)
- Add `order_month` (`YYYY-MM`)
- Build mart: `orders_enriched` (row-level) and `daily_revenue_summary` (by date + category)

### 5. Load (idempotent)

- `output/staging/orders.parquet` — overwrite each run
- `output/marts/orders_enriched.parquet` — overwrite
- `output/marts/daily_revenue_summary.parquet` — overwrite
- Use atomic write (temp + rename)

### 6. Metadata

`output/run_metadata.json` every run:

```json
{
  "run_id": "...",
  "status": "success",
  "duration_seconds": 1.2,
  "tables": { "orders_enriched": 14, "daily_revenue_summary": 5 },
  "rejected_rows": 0
}
```

---

## Step-by-step guide

### Step 1: Scaffold modules (1 hr)

Empty functions with type hints; `pipeline.py` calls them in order.

### Step 2: Extract + validate (1.5 hr)

Fail fast on missing columns; quarantine bad rows.

### Step 3: Transform + load (2 hr)

Joins and aggregations; atomic Parquet writes.

### Step 4: Metadata + logging (1 hr)

`logging` module; duration timer; non-zero exit on failure.

### Step 5: Test idempotency (30 min)

Run twice; checksums or row counts must match.

---

## Acceptance criteria

- [ ] `python pipeline.py` from `project/` succeeds
- [ ] Re-run produces identical mart row counts
- [ ] Rejects file created when you inject a bad row (test manually)
- [ ] All paths relative to repo root for shared data
- [ ] CHECKLIST.md complete

---

## What you learned

A **modular, idempotent batch pipeline** — the unit of work Airflow will schedule in Phase 4.

**Next phase:** [Phase 4: ETL Orchestration](../../phase-04-etl-orchestration/README.md)
