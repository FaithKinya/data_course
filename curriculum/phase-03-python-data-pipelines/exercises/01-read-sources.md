# Exercise 1: Read Multiple Sources

**Time:** ~30 minutes

---

## Goal

Load all three ShopStream datasets and produce a unified preview.

---

## Tasks

Create `curriculum/phase-03-python-data-pipelines/exercises/my_work/01_read_sources.py`:

1. Load `shared/datasets/orders.csv`, `customers.csv`, `products.csv`
2. Print shape and dtypes for each
3. Parse `order_date` and `signup_date` as datetimes
4. Inner-join orders → customers → products (first 5 rows)
5. Print total memory usage (`df.memory_usage(deep=True).sum()`)

---

## Constraints

- Use `Path(__file__).resolve().parents[4]` for project root
- Raise `FileNotFoundError` with path if any file missing
- Cast `order_id`, `customer_id`, `product_id` to consistent integer types

---

## Expected skills

- Multi-file ingest
- `pd.read_csv` options
- Chained merges

---

## Verify

Compare structure with [solutions/01_read_sources.py](solutions/01_read_sources.py).

**Next:** [Exercise 2: Clean & validate](02-clean-validate.md)
