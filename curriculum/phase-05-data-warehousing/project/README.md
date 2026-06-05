# Phase 5 Project: dbt Analytics Project

**Time:** 6–8 hours  
**Deliverable:** Full dbt project with staging, marts, tests, and docs

---

## Scenario

ShopStream analysts need trusted metrics in a warehouse. Build a **dbt project** on DuckDB that transforms shared CSVs into documented, tested marts.

---

## Requirements

### 1. Project layout

```
project/shopstream_dbt/
├── dbt_project.yml
├── profiles.yml.example
├── models/
│   ├── staging/
│   │   ├── stg_orders.sql
│   │   ├── stg_customers.sql
│   │   ├── stg_products.sql
│   │   └── schema.yml
│   └── marts/
│       ├── dim_customers.sql
│       ├── dim_products.sql
│       ├── fct_orders.sql
│       └── fct_revenue_daily.sql
├── tests/
│   └── assert_revenue_not_null_completed.sql
└── shopstream.duckdb
```

Set `vars.datasets_path` to `../../../shared/datasets` (relative to dbt project).

### 2. Staging layer

- Read CSVs via `read_csv_auto` and `var('datasets_path')`
- Standardize types and lowercase `status`

### 3. Marts layer

| Model | Grain | Key columns |
|-------|-------|-------------|
| `dim_customers` | customer | customer_id, name, country |
| `dim_products` | product | product_id, category, unit_cost |
| `fct_orders` | order | order_id, revenue, flags |
| `fct_revenue_daily` | date + category | revenue, order_count |

Revenue rules match prior phases.

### 4. Tests (minimum)

- `unique` + `not_null` on all mart primary keys
- `relationships` from fct_orders to dims
- Singular test: completed orders have non-null revenue

### 5. Documentation

- Model descriptions for all marts
- `dbt docs generate` produces lineage

---

## Step-by-step guide

### Step 1: Init project (1 hr)

`dbt init`, configure duckdb profile, set `datasets_path` var.

### Step 2: Staging (1.5 hr)

Three staging models + source/schema YAML.

### Step 3: Marts (2 hr)

`fct_orders` joins dims; `fct_revenue_daily` aggregates.

### Step 4: Tests (1.5 hr)

Generic + singular; `dbt test` all pass.

### Step 5: Docs + README (1 hr)

Document how to run; add profile example.

---

## Acceptance criteria

- [ ] `dbt run` builds all models without error
- [ ] `dbt test` passes
- [ ] `fct_revenue_daily` matches manual spot-check for one date
- [ ] Docs site shows staging → marts lineage
- [ ] CHECKLIST.md complete

---

## What you learned

**ELT with dbt** — the industry-standard way to own warehouse transformations in git.

**Next phase:** [Phase 6: Streaming & Real-Time](../../phase-06-streaming-real-time/README.md)
