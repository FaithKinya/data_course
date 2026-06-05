# Phase 4 Project: Scheduled Daily Pipeline

**Time:** 6–8 hours  
**Deliverable:** Airflow DAG orchestrating ShopStream batch ETL

---

## Scenario

ShopStream needs the Phase 3 ETL to run **daily at 6 AM UTC** with monitoring. Wrap your pipeline in Airflow with proper dependencies, a file sensor, and failure retries.

---

## Requirements

### 1. ETL code in `project/`

Copy or adapt Phase 3 modules into `curriculum/phase-04-etl-orchestration/project/`:

- `extract.py`, `validate.py`, `transform.py`, `load.py`, `pipeline.py`
- Output to `project/output/` (mounted in container as `/opt/airflow/project/output`)

Use container paths: `/opt/airflow/shared/datasets/`

### 2. DAG: `shopstream_daily_etl`

Create `dags/shopstream_daily_etl.py`:

| Task | Type | Purpose |
|------|------|---------|
| `wait_for_data` | FileSensor | Wait for orders.csv |
| `extract` | PythonOperator | Load all CSVs |
| `validate` | PythonOperator | Quarantine bad rows |
| `transform` | PythonOperator | Join + revenue |
| `load` | PythonOperator | Write Parquet marts |
| `emit_metadata` | PythonOperator | Log summary to XCom |

Dependencies: `wait_for_data` → `extract` → `validate` → `transform` → `load` → `emit_metadata`

### 3. DAG configuration

- `schedule="0 6 * * *"` (6 AM UTC daily)
- `catchup=False`
- `max_active_runs=1`
- `default_args`: `retries=2`, `retry_delay=5 min`, `email_on_failure=False`
- Meaningful `doc_md` with owner and data sources

### 4. Pass data between tasks

Use Airflow **XCom** for small metadata (row counts, paths) — not full DataFrames.

---

## Step-by-step guide

### Step 1: Docker up (30 min)

`docker compose up -d`; confirm UI and dataset mount.

### Step 2: Port ETL (2 hr)

Adapt paths for `/opt/airflow/...`; test `python pipeline.py` inside scheduler container:

```bash
docker compose exec airflow-scheduler python /opt/airflow/project/pipeline.py
```

### Step 3: Build DAG (2 hr)

Thin DAG file; `PythonOperator` callables import from `project/`.

### Step 4: Sensor + retries (1 hr)

Configure FileSensor; test manual trigger.

### Step 5: Document (1 hr)

README: start/stop Airflow, trigger DAG, where logs live.

---

## Acceptance criteria

- [ ] `shopstream_daily_etl` visible and unpaused in Airflow UI
- [ ] Manual run completes all tasks green
- [ ] Parquet outputs written under `project/output/marts/`
- [ ] XCom shows row counts from `emit_metadata`
- [ ] Re-triggering does not duplicate mart rows
- [ ] CHECKLIST.md complete

---

## What you learned

You separated **workflow** (Airflow) from **work** (Python ETL) — the standard pattern in data teams.

**Next phase:** [Phase 5: Data Warehousing](../../phase-05-data-warehousing/README.md)
