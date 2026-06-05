# Exercise 1: Staging Models

**Time:** ~45 minutes

---

## Goal

Initialize a dbt project and create staging models for ShopStream sources.

---

## Tasks

1. From `curriculum/phase-05-data-warehousing/exercises/my_work/`:

```bash
dbt init shopstream_ex01
cd shopstream_ex01
```

Configure `profiles.yml` (or `~/.dbt/profiles.yml`) for `dbt-duckdb` pointing at `ex01.duckdb`.

2. Define sources for `orders`, `customers`, `products` reading from `../../../../shared/datasets/*.csv` via DuckDB `read_csv_auto` in source definitions or seed copies.

3. Create models:
   - `models/staging/stg_orders.sql`
   - `models/staging/stg_customers.sql`
   - `models/staging/stg_products.sql`

4. Staging rules:
   - Lowercase `status` in orders
   - Cast dates properly
   - Rename nothing else — preserve column names

5. Run `dbt run --select staging` and confirm 3 views/tables built.

---

## Verify

Compare SQL patterns with [solutions/stg_orders.sql](solutions/stg_orders.sql).

**Next:** [Exercise 2: dbt tests](02-dbt-tests.md)
