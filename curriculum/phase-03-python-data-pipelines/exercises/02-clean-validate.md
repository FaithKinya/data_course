# Exercise 2: Clean & Validate

**Time:** ~45 minutes

---

## Goal

Implement validation that splits valid orders from rejects and applies business rules.

---

## Tasks

Create `curriculum/phase-03-python-data-pipelines/exercises/my_work/02_clean_validate.py`:

1. Load orders from `shared/datasets/orders.csv`
2. Validate:
   - `order_id`, `customer_id`, `product_id` not null
   - `quantity > 0`
   - `unit_price >= 0`
   - `status` in `completed`, `cancelled`, `refunded`
3. Split into `valid_df` and `rejects_df`; print counts
4. On `valid_df`, add `revenue` column:
   - `completed` → `quantity * unit_price`
   - `refunded` → `-quantity * unit_price`
   - `cancelled` → `0`
5. Write `rejects_df` to `exercises/my_work/rejects.csv` if non-empty

---

## Verify

Compare with [solutions/02_clean_validate.py](solutions/02_clean_validate.py).

**Next:** [Exercise 3: Idempotent loads](03-idempotent-load.md)
