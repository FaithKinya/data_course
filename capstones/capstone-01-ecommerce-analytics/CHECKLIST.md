# Capstone A: Acceptance Checklist

Use this as your definition of done. Check items as you complete them. Every section must be ≥ 80% complete before calling the capstone finished.

---

## Setup & Documentation

- [ ] Folder structure matches README scaffold
- [ ] `docs/architecture.md` with diagram committed
- [ ] `docs/data-dictionary.md` covers bronze, silver, and mart columns
- [ ] `docs/decisions.md` documents grain, incremental strategy, and batch/stream boundary
- [ ] Project README: setup, run commands, sample output
- [ ] `.gitignore` excludes `storage/`, `logs/`, `target/`, `.env`, `__pycache__/`

---

## Phase 1 Skills — Foundations

- [ ] Understand and can explain data lifecycle (ingest → transform → serve) for this project
- [ ] Bronze layer stores immutable raw data in Parquet
- [ ] Silver layer stores cleaned, analytics-ready Parquet
- [ ] Gold layer (dbt marts) serves business metrics
- [ ] `run_metadata.json` written every pipeline run with timestamp, row counts, status
- [ ] Can articulate why Parquet over CSV for intermediate storage

---

## Phase 2 Skills — SQL & Data Modeling

- [ ] Star schema designed with fact + dimension tables
- [ ] `fct_orders` grain documented: one row per order line
- [ ] Surrogate keys (`customer_key`, `product_key`, `date_key`) used in fact table
- [ ] `dim_dates` supports role-playing (order date, ship date if applicable)
- [ ] No fan-out joins: fact row count stable after dimension joins
- [ ] Conformed dimensions reusable across marts

---

## Phase 3 Skills — Python Pipelines

- [ ] Ingestion code separated into extractors, validators, loaders (not one monolith)
- [ ] Multi-source ingest: orders, customers, products (+ generated sources)
- [ ] Validation rejects malformed input with clear error message
- [ ] Idempotent loads: re-running same date produces same result
- [ ] Structured error handling: failures don't silently produce empty partitions
- [ ] Unit tests for core transform logic (`pytest tests/` passes)

---

## Phase 4 Skills — Orchestration

- [ ] Airflow DAG orchestrates bronze → silver → warehouse → dbt
- [ ] Task dependencies reflect true data dependencies (no premature dbt run)
- [ ] Retries configured on transient-failure tasks (≥ 2 retries)
- [ ] `execution_date` drives partition paths correctly
- [ ] Backfill script or documented process for historical dates
- [ ] DAG failure visible in Airflow UI with actionable log message

---

## Phase 5 Skills — Data Warehousing (dbt)

- [ ] dbt project with `staging` → `intermediate` → `marts` layers
- [ ] `dbt run` completes without errors
- [ ] `dbt test` passes: `not_null`, `unique`, `relationships` on key columns
- [ ] Custom test for business rule (e.g. positive revenue on non-refund rows)
- [ ] Incremental model on `fct_orders` (or documented why full-refresh)
- [ ] `schema.yml` descriptions on all mart models
- [ ] `dbt docs generate` produces lineage graph

---

## Phase 6 Skills — Streaming (Conceptual)

- [ ] `docs/decisions.md` explains what would move to Kafka/streaming (e.g. clickstream, real-time inventory)
- [ ] Can articulate batch vs stream trade-off for ShopStream's use cases
- [ ] Event schema drafted for one hypothetical real-time source (optional stretch)

---

## Phase 7 Skills — Cloud Data Engineering

- [ ] Bronze/silver paths follow `source/year=YYYY/month=MM/day=DD/` convention
- [ ] Partition strategy documented (why date partitioning, expected query patterns)
- [ ] Queries use partition pruning (no full-table scan on date-filtered queries)
- [ ] Cost awareness note: estimated data volume and retention policy documented

---

## Phase 8 Skills — Production Best Practices

- [ ] Data contracts defined per source (columns, types, freshness SLA)
- [ ] Row-count reconciliation logged: bronze → silver → staging
- [ ] Structured logging in Python pipeline code
- [ ] Alert or escalation path on pipeline failure (log, email stub, or CI notification)
- [ ] CI workflow runs `dbt parse` and/or `dbt test` on push (or documented skip)
- [ ] No secrets committed to Git

---

## Business Metrics (Functional)

- [ ] `mart_daily_revenue` — daily revenue, order count, average order value
- [ ] `mart_category_performance` — revenue and units by category over time
- [ ] `mart_customer_cohorts` — cohort retention or revenue by signup month
- [ ] Cancelled orders tracked separately from revenue metrics
- [ ] Refund orders reflected as negative revenue in net calculations
- [ ] `reports/sample_queries.sql` with 5 documented stakeholder queries

---

## Data Quality Gates

- [ ] Validator catches missing required column (tested manually)
- [ ] Validator catches type mismatch (tested manually)
- [ ] dbt relationship test: no orphan `customer_key` or `product_key` in facts
- [ ] Row counts within expected bounds (reconciliation log reviewed)
- [ ] Spot-check 3 order lines end-to-end: source → bronze → silver → fact → mart

---

## Operations Gates

- [ ] Full pipeline runs via single command or Airflow trigger
- [ ] Pipeline completes in reasonable time on sample data (< 5 min local)
- [ ] Failed run leaves system in recoverable state (no corrupt partitions)
- [ ] `run_metadata.json` reflects failure status when pipeline fails
- [ ] Fresh clone setup works following README alone (ask a friend or future-you to verify)

---

## Portfolio & Interview Readiness

- [ ] GitHub repo (or folder) with clean commit history
- [ ] 15-minute walkthrough rehearsed (architecture → demo → trade-offs)
- [ ] Can explain grain choice in 2 sentences without hesitation
- [ ] Can explain one bug you fixed and how you diagnosed it
- [ ] Can explain what you'd change at 10x data volume
- [ ] Screenshot or sample output table in README

---

## Stretch Goals (Optional)

- [ ] SCD Type 2 on `dim_customers`
- [ ] Great Expectations validation suite
- [ ] GitHub Actions CI fully green
- [ ] Live dashboard (Metabase, Evidence, or similar)
- [ ] `fct_inventory_daily` fact table with daily snapshots
- [ ] `dim_campaigns` with marketing attribution mart

---

## Sign-off

| Item | Value |
|------|-------|
| **Completed date** | __________ |
| **Total hours spent** | __________ |
| **Sections complete** | ___ / 12 |
| **Stretch goals done** | __________ |
| **Ready for interview?** | Yes / Not yet |

When all core sections (Setup through Portfolio) are checked, update [PROGRESS.md](../../PROGRESS.md) Capstone A item.
