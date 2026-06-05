# Phase 2 Project: Star Schema Mini-Mart

**Time:** 5–7 hours  
**Deliverable:** DuckDB database + SQL queries + short README

---

## Scenario

ShopStream's analytics team is tired of slow spreadsheet joins. Your job: build a **star schema mini-mart** in DuckDB from the shared CSVs and expose five standard business queries.

---

## Requirements

### 1. Database setup

Create `curriculum/phase-02-sql-data-modeling/project/shopstream.duckdb` with:

| Table | Source | Notes |
|-------|--------|-------|
| `dim_customer` | `shared/datasets/customers.csv` | Surrogate `customer_key` |
| `dim_product` | `shared/datasets/products.csv` | Surrogate `product_key` |
| `dim_date` | derived from orders | `date_key` as `YYYYMMDD` int |
| `fact_orders` | `shared/datasets/orders.csv` | FKs to all dims; include `revenue` |

Grain: **one row per order** in `fact_orders`.

### 2. Business rules

- `revenue = quantity * unit_price`
- `cancelled` orders: `revenue = 0`, keep row with `is_cancelled = true`
- `refunded` orders: `revenue` negative
- `completed` orders: positive `revenue`

### 3. Required queries (`queries.sql`)

Save five queries:

1. Total revenue by month (`YYYY-MM`)
2. Top 5 products by revenue
3. Customer count and avg order value by country
4. Category mix (% of revenue per category)
5. Orders and revenue by day of week

### 4. Project structure

```
project/
├── README.md           # how to build DB and run queries
├── build_schema.py     # creates tables and loads data
├── queries.sql         # five business queries
├── CHECKLIST.md
└── shopstream.duckdb   # generated (gitignored)
```

---

## Step-by-step guide

### Step 1: Build dimensions (1.5 hr)

Write `build_schema.py` that creates `dim_customer`, `dim_product`, `dim_date` with surrogate keys.

### Step 2: Build fact table (1.5 hr)

Join orders to dimensions; compute `revenue` and flags; insert into `fact_orders`.

### Step 3: Validate (1 hr)

Row counts: fact rows = order rows. Spot-check one customer's total against raw CSV.

### Step 4: Write queries (1.5 hr)

Test each query in DuckDB CLI or Python; save to `queries.sql`.

### Step 5: Document (45 min)

README: prerequisites, `python build_schema.py`, how to run queries.

---

## Acceptance criteria

- [ ] `python build_schema.py` creates `shopstream.duckdb` idempotently (safe to re-run)
- [ ] Star schema has 1 fact + 3 dimensions
- [ ] All five queries return sensible results
- [ ] Cancelled/refunded rules applied correctly
- [ ] CHECKLIST.md complete

---

## What you learned

You turned normalized CSVs into an **analytics model** — the same pattern warehouses use before dbt marts.

**Next phase:** [Phase 3: Python Data Pipelines](../../phase-03-python-data-pipelines/README.md)
