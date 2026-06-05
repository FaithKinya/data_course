# Exercise 3: Design a Schema

**Time:** ~45 minutes

---

## Goal

Design a star schema for ShopStream analytics before building it in the phase project.

---

## Tasks

### Part A — Diagram (paper or draw.io)

Draw tables and relationships:

- `fact_orders`
- `dim_customer`, `dim_product`, `dim_date`

Label:

- Primary keys (surrogate `*_key`)
- Foreign keys on the fact table
- Grain of the fact table (one row per ___)

### Part B — DDL sketch

Write `CREATE TABLE` statements (DuckDB SQL) for all four tables. Include column types.

### Part C — Load plan

List the steps to populate dimensions from CSVs, then facts. Which table loads first? Why?

### Part D — Business query

Write one SQL query against your star schema:

> Monthly revenue by category for completed orders in 2024

---

## Deliverable

Save your work as:

`curriculum/phase-02-sql-data-modeling/exercises/my_work/03_schema_design.md`

Include diagram (image or ASCII), DDL, load order, and sample query.

---

## Check yourself

- [ ] Fact grain is documented
- [ ] No descriptive text duplicated on fact rows (except degenerate dims)
- [ ] `dim_date` has `year` and `month` columns
- [ ] Cancelled orders excluded from revenue measures (flag or filter)

**Next:** [Phase project →](../project/README.md)
