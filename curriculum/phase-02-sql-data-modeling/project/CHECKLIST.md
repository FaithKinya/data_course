# Phase 2 Project Checklist

- [ ] `build_schema.py` uses paths relative to project root (`shared/datasets/`)
- [ ] `dim_customer`, `dim_product`, `dim_date` created with surrogate keys
- [ ] `fact_orders` grain is one row per order
- [ ] Revenue rules: cancelled=0, refunded=negative, completed=positive
- [ ] Fact row count matches `orders.csv` row count
- [ ] `queries.sql` contains all 5 required queries
- [ ] Monthly revenue query returns expected 2024 months
- [ ] Top products query has exactly 5 rows
- [ ] Re-running `build_schema.py` does not duplicate data
- [ ] README documents build and query steps
