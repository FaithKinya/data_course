# Capstone A: Milestones

**Total duration:** 4–6 weeks  
**Recommended pace:** 8–12 hours per week

Mark each milestone complete before moving on. If you fall behind, compress Weeks 5–6 (orchestration + hardening) rather than skipping data modeling.

---

## Milestone 0: Kickoff (Day 1 — 2 hours)

**Goal:** Align on scope, set up repo, write your architecture doc skeleton.

### Tasks
- [ ] Read [README.md](README.md) end-to-end
- [ ] Create folder structure from README scaffold
- [ ] Initialize Git repo (or dedicated branch) for capstone work
- [ ] Write `docs/architecture.md` with:
  - Problem statement (1 paragraph)
  - Architecture diagram (Mermaid or draw.io export)
  - List of source systems and target marts
  - Open questions (grain, incremental strategy, SCD choices)
- [ ] Run `python shared/utils/verify_setup.py` — fix any environment issues

### Exit criteria
- Architecture doc committed with diagram
- Empty folder scaffold in place
- DuckDB and dbt CLI working locally

### Curriculum touchpoints
- **Phase 1:** Review [data lifecycle](../../curriculum/phase-01-foundations/lessons/02-data-lifecycle.md)
- **Phase 2:** Skim [dimensional modeling](../../curriculum/phase-02-sql-data-modeling/lessons/03-dimensional-modeling.md) before locking grain

---

## Milestone 1: Bronze Ingestion (Week 1 — 8–10 hours)

**Goal:** Land raw source data in a partitioned bronze layer with run metadata.

### Tasks
- [ ] Implement `ingestion/extractors/orders.py` — read CSV, return DataFrame + metadata
- [ ] Implement extractors for `customers.csv` and `products.csv`
- [ ] Create `scripts/generate_sample_data.py` for `inventory_snapshots` (JSON) and `marketing_campaigns` (CSV)
- [ ] Implement `ingestion/loaders/bronze_writer.py`:
  - Write Parquet to `storage/bronze/{source}/year=YYYY/month=MM/day=DD/`
  - Append-only (never overwrite bronze)
  - Return partition path and row count
- [ ] Write `ingestion/validators/schemas.py` — define expected columns and types per source (data contract draft)
- [ ] Create `scripts/run_pipeline.sh` (or `.py`) that runs bronze ingest only
- [ ] Log to `storage/gold/run_metadata.json`: `run_id`, `source`, `rows_ingested`, `partition_path`, `status`, `timestamp`

### Exit criteria
- `python scripts/run_pipeline.sh --layer bronze --date 2024-01-15` lands all 5 sources
- Bronze partitions inspectable: `SELECT * FROM 'storage/bronze/orders/year=2024/month=01/day=15/*.parquet'`
- Re-running same date is idempotent (no duplicate files or duplicate rows in partition)
- Validator rejects file with missing required column (test with a broken CSV)

### Curriculum touchpoints
- **Phase 1:** [Data formats](../../curriculum/phase-01-foundations/lessons/03-data-formats.md), [Phase 1 project](../../curriculum/phase-01-foundations/project/README.md)
- **Phase 3:** [Ingestion patterns](../../curriculum/phase-03-python-data-pipelines/lessons/02-ingestion.md), [idempotent loads](../../curriculum/phase-03-python-data-pipelines/exercises/03-idempotent-load.md)
- **Phase 7:** [Object storage paths](../../curriculum/phase-07-cloud-data-engineering/lessons/02-object-storage.md), [partitioned writes](../../curriculum/phase-07-cloud-data-engineering/exercises/02-partitioned-writes.md)
- **Phase 8:** [Data contracts](../../curriculum/phase-08-production-best-practices/lessons/03-cicd-pipelines.md) (schema draft)

---

## Milestone 2: Silver Transforms (Week 2 — 8–10 hours)

**Goal:** Clean, validate, and type-cast bronze data into silver Parquet.

### Tasks
- [ ] Implement `transforms/clean_orders.py`:
  - Exclude cancelled orders from revenue path (flag, don't drop — keep for cancelled metric)
  - Negative revenue for refunds
  - Parse dates, coerce numeric types
  - Deduplicate on `order_id` + `line_id` (keep latest by `updated_at` if present)
- [ ] Implement `transforms/clean_customers.py` and `transforms/clean_products.py`
- [ ] Wire silver writer with same partition pattern: `storage/silver/{entity}/year=.../`
- [ ] Add row-count reconciliation: log `bronze_rows`, `silver_rows`, `rejected_rows`, `rejection_reasons`
- [ ] Write unit tests in `tests/test_clean_orders.py` (cancelled, refund, dedup cases)
- [ ] Update `docs/data-dictionary.md` with silver column definitions
- [ ] Finalize data contracts in `ingestion/validators/schemas.py`

### Exit criteria
- Silver orders pass manual spot-check: cancelled excluded from `line_revenue`, refunds negative
- Unit tests pass: `pytest tests/`
- Reconciliation log shows expected rejection rate (< 1% on clean sample data)
- Data dictionary covers all silver tables

### Curriculum touchpoints
- **Phase 1:** [Exercise 3: first transform](../../curriculum/phase-01-foundations/exercises/03-first-transform.md)
- **Phase 3:** [Clean & validate](../../curriculum/phase-03-python-data-pipelines/exercises/02-clean-validate.md), [Phase 3 project](../../curriculum/phase-03-python-data-pipelines/project/README.md)
- **Phase 8:** [Data quality](../../curriculum/phase-08-production-best-practices/lessons/01-data-quality.md), [Great Expectations intro](../../curriculum/phase-08-production-best-practices/exercises/01-great-expectations.md) (optional)

---

## Milestone 3: Dimensional Model & dbt Staging (Week 3 — 10–12 hours)

**Goal:** Load silver into DuckDB and build dbt staging + core dimension/fact models.

### Tasks
- [ ] Initialize dbt project: `dbt init dbt_shopstream` (or copy from Phase 5 project)
- [ ] Configure `profiles.yml` for DuckDB target
- [ ] Create external table sources or copy silver Parquet into DuckDB on each run
- [ ] Build staging models:
  - `stg_orders.sql` — rename, cast, basic filters
  - `stg_customers.sql`
  - `stg_products.sql`
- [ ] Create `seeds/dim_dates.csv` (or generate via macro) — 5 years of dates
- [ ] Build core dimensions:
  - `dim_customers.sql` — surrogate key `customer_key`
  - `dim_products.sql` — surrogate key `product_key`
  - `dim_dates.sql`
- [ ] Build `fct_orders.sql` at order-line grain with foreign keys to dimensions
- [ ] Build `int_order_lines_enriched.sql` — join staging tables before fact load
- [ ] Document grain in `docs/decisions.md` (ADR format)
- [ ] Run `dbt build --select staging+` successfully

### Exit criteria
- `dbt run` builds staging + dimensions + fact without errors
- `fct_orders` grain is one row per order line (verify with `COUNT(*) vs COUNT(DISTINCT order_line_id)`)
- Surrogate keys populated; no orphan foreign keys
- `docs/decisions.md` explains grain and key choices

### Curriculum touchpoints
- **Phase 2:** [Dimensional modeling](../../curriculum/phase-02-sql-data-modeling/lessons/03-dimensional-modeling.md), [Phase 2 project](../../curriculum/phase-02-sql-data-modeling/project/README.md)
- **Phase 5:** [Staging models](../../curriculum/phase-05-data-warehousing/exercises/01-staging-models.md), [intro to dbt](../../curriculum/phase-05-data-warehousing/lessons/02-intro-dbt.md)

---

## Milestone 4: dbt Marts, Tests & Docs (Week 4 — 10–12 hours)

**Goal:** Deliver business metrics with tested, documented mart models.

### Tasks
- [ ] Build mart models:
  - `mart_daily_revenue.sql` — revenue, order count, AOV by date
  - `mart_category_performance.sql` — revenue and units by category over time
  - `mart_customer_cohorts.sql` — retention by signup month (stretch: 3-month retention)
- [ ] Add dbt tests:
  - `not_null` + `unique` on primary keys
  - `relationships` from `fct_orders` to dimensions
  - Custom test `assert_positive_revenue` (non-refund rows)
- [ ] Configure incremental model on `fct_orders` (merge strategy for late-arriving data)
- [ ] Add `schema.yml` descriptions for all models and key columns
- [ ] Run `dbt docs generate` and review lineage graph
- [ ] Write `reports/sample_queries.sql` — 5 stakeholder-facing queries with comments

### Exit criteria
- `dbt test` passes all tests
- Mart models answer finance + marketing + product questions from README
- Incremental run processes only new order lines (verify with row count before/after)
- dbt docs site viewable locally

### Curriculum touchpoints
- **Phase 5:** [dbt tests](../../curriculum/phase-05-data-warehousing/exercises/02-dbt-tests.md), [documentation](../../curriculum/phase-05-data-warehousing/exercises/03-documentation.md), [incremental models](../../curriculum/phase-05-data-warehousing/lessons/03-incremental-models.md), [Phase 5 project](../../curriculum/phase-05-data-warehousing/project/README.md)

---

## Milestone 5: Airflow Orchestration (Week 5 — 8–10 hours)

**Goal:** Schedule and monitor the full pipeline with Airflow.

### Tasks
- [ ] Create `orchestration/docker-compose.yml` (adapt from Phase 4)
- [ ] Build `orchestration/dags/shopstream_daily.py`:
  - Task 1: `bronze_ingest` (all sources)
  - Task 2: `silver_transform` (depends on bronze)
  - Task 3: `load_warehouse` (copy Parquet → DuckDB or external tables)
  - Task 4: `dbt_run` (depends on load)
  - Task 5: `dbt_test` (depends on dbt_run)
  - Task 6: `write_metadata` (always runs — success or failure summary)
- [ ] Configure retries (3x, exponential backoff) on ingest and dbt tasks
- [ ] Add `execution_date` templating for partition paths
- [ ] Implement `scripts/backfill.py` — trigger DAG for a date range
- [ ] Test manual trigger and verify all tasks green
- [ ] Document DAG in `docs/architecture.md` (update with orchestration section)

### Exit criteria
- DAG runs end-to-end from Airflow UI with all tasks successful
- Forced failure in bronze task triggers retry, then fails DAG with visible log
- Backfill for 3 historical dates produces correct partitions
- `run_metadata.json` updated after every DAG run

### Curriculum touchpoints
- **Phase 4:** [Airflow concepts](../../curriculum/phase-04-etl-orchestration/lessons/02-airflow-concepts.md), [DAG best practices](../../curriculum/phase-04-etl-orchestration/lessons/03-dag-best-practices.md), [retries & sensors](../../curriculum/phase-04-etl-orchestration/exercises/03-retries-sensors.md), [Phase 4 project](../../curriculum/phase-04-etl-orchestration/project/README.md)

---

## Milestone 6: Production Hardening & Portfolio (Week 6 — 8–10 hours)

**Goal:** Make the project interview-ready and production-defensible.

### Tasks
- [ ] Add structured logging throughout Python code (JSON or key=value format)
- [ ] Implement failure alerting (log file threshold, email stub, or Slack webhook placeholder)
- [ ] Add pre-commit or CI workflow: `dbt parse && dbt test` on push (`.github/workflows/dbt_ci.yml`)
- [ ] Write capstone README section: setup, env vars, how to run, architecture summary
- [ ] Record or script a 15-minute demo walkthrough
- [ ] Complete [CHECKLIST.md](CHECKLIST.md) — every item checked or explicitly deferred with reason
- [ ] Clean up: `.gitignore` for `storage/`, `logs/`, `target/`, `.env`
- [ ] Optional: connect Metabase/Evidence to DuckDB for one dashboard screenshot

### Exit criteria
- New clone can run pipeline following README instructions alone
- CI passes (or documented why skipped)
- CHECKLIST.md 100% complete (or stretch items marked N/A)
- You can deliver 15-min walkthrough without reading slides

### Curriculum touchpoints
- **Phase 6:** Write 1 paragraph in `docs/decisions.md` on where streaming would fit (batch/stream boundary)
- **Phase 7:** Review [cost awareness](../../curriculum/phase-07-cloud-data-engineering/exercises/03-cost-awareness.md) — document partition strategy rationale
- **Phase 8:** [Observability](../../curriculum/phase-08-production-best-practices/lessons/02-observability.md), [pipeline logging](../../curriculum/phase-08-production-best-practices/exercises/02-pipeline-logging.md), [CI/CD](../../curriculum/phase-08-production-best-practices/lessons/03-cicd-pipelines.md), [Phase 8 project](../../curriculum/phase-08-production-best-practices/project/README.md)

---

## Milestone Summary Table

| # | Week | Theme | Hours | Hard gate |
|---|------|-------|-------|-----------|
| 0 | Day 1 | Kickoff | 2 | Architecture doc |
| 1 | 1 | Bronze ingest | 8–10 | Partitioned Parquet landing |
| 2 | 2 | Silver transforms | 8–10 | Tests + data contracts |
| 3 | 3 | dbt staging + star schema | 10–12 | Fact grain verified |
| 4 | 4 | Marts + tests + docs | 10–12 | `dbt test` green |
| 5 | 5 | Airflow DAG | 8–10 | End-to-end scheduled run |
| 6 | 6 | Production + portfolio | 8–10 | Demo-ready README |

---

## If You Get Stuck

| Blocker | Try this |
|---------|----------|
| Grain confusion | Write one English sentence: "One row in fct_orders represents ___" |
| dbt can't find sources | Use `dbt debug`, check `profiles.yml` path and DuckDB file location |
| Airflow task import errors | Mount `ingestion/` into Docker volume; check `PYTHONPATH` |
| Incremental duplicates | Add unique key test; switch merge strategy to `delete+insert` |
| Partition path bugs | Print resolved path in logs; test with `execution_date='2024-01-15'` |

---

**Track daily progress in [CHECKLIST.md](CHECKLIST.md).**
