# Exercise 1: SELECT Practice

**Time:** ~30 minutes

---

## Goal

Practice filtering and aggregation on ShopStream orders using DuckDB.

---

## Setup

```bash
pip install duckdb
```

Create `curriculum/phase-02-sql-data-modeling/exercises/my_work/01_select_practice.py` or use the DuckDB CLI.

---

## Tasks

Using `shared/datasets/orders.csv`, write SQL that:

1. Returns row count and distinct `customer_id` count
2. Lists all `refunded` orders with computed `revenue = quantity * unit_price`
3. Finds the top 3 customers by total **completed** order revenue
4. Counts orders per `status` sorted by count descending

---

## Constraints

- Use `read_csv_auto('shared/datasets/orders.csv')` or load via Python with paths relative to project root
- Round revenue to 2 decimal places in output
- Exclude `cancelled` from task 3

---

## Verify

Compare with [solutions/01_select_practice.py](solutions/01_select_practice.py).

**Next:** [Exercise 2: JOINs & aggregations](02-joins-aggregations.md)
