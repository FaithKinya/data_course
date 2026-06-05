# Exercise 2: Task Dependencies

**Time:** ~45 minutes

---

## Goal

Build a DAG that reads ShopStream CSV row counts using `PythonOperator`.

---

## Tasks

Create `dags/ex02_row_counts_dag.py`:

1. DAG `ex02_row_counts`, schedule `None` (manual only)
2. Three parallel `PythonOperator` tasks:
   - `count_orders` — rows in `/opt/airflow/shared/datasets/orders.csv`
   - `count_customers` — customers CSV
   - `count_products` — products CSV
3. One downstream `PythonOperator` `report_totals` that logs all three counts
4. Dependencies: all count tasks → `report_totals`

Use `pandas.read_csv` inside callables, not at DAG parse time.

---

## Expected log output

```
orders=14 customers=10 products=8
```

(Counts match current shared datasets.)

---

## Verify

Compare with [solutions/ex02_row_counts_dag.py](solutions/ex02_row_counts_dag.py).

**Next:** [Exercise 3: Retries & sensors](03-retries-sensors.md)
