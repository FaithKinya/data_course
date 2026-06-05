# Exercise 3: Write Your First Transform

**Time:** ~45 minutes

---

## Goal

Write a function that cleans order data according to business rules.

---

## Business rules

1. Drop rows where `quantity <= 0` or `unit_price <= 0` (none in sample, but handle generically)
2. Keep only `status` in `completed`, `refunded` (exclude `cancelled`)
3. Add column `revenue = quantity * unit_price`
4. For `refunded` orders, multiply revenue by `-1`
5. Add `order_month` as `YYYY-MM` from `order_date`

---

## Tasks

Create `exercises/my_work/03_clean_orders.py` with:

```python
def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    ...
```

Run it on `orders.csv` and print the first 5 rows.

---

## Stretch

Write output to `curriculum/phase-01-foundations/exercises/my_work/output/clean_orders.parquet`

---

## Solution

[solutions/03_clean_orders.py](solutions/03_clean_orders.py)

**Next:** [Phase 1 Project](../project/README.md)
