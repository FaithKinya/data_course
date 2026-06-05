# Exercise 1: Great Expectations Intro

**Time:** ~45 minutes

---

## Goal

Validate `shared/datasets/orders.csv` with Great Expectations.

---

## Prerequisites

```bash
pip install great-expectations pandas
```

---

## Tasks

Create `exercises/my_work/01_great_expectations.py`:

1. Load orders CSV with pandas
2. Create GX validator on the DataFrame
3. Add expectations:
   - `order_id` not null and unique
   - `quantity` > 0
   - `status` in allowed set
   - `unit_price` >= 0
4. Run `validate()`; print success/failure summary
5. Exit code 1 if any expectation fails

---

## Experiment

Temporarily filter to invalid rows in memory and confirm validation fails.

---

## Verify

Compare with [solutions/01_great_expectations.py](solutions/01_great_expectations.py).

**Next:** [Exercise 2: Pipeline logging](02-pipeline-logging.md)
