# Exercise 2: Explore a CSV Dataset

**Time:** ~30 minutes

---

## Goal

Load the sample orders dataset and produce a short data profile.

---

## Tasks

Create `curriculum/phase-01-foundations/exercises/my_work/02_explore_orders.py` (or a Jupyter notebook) that:

1. Loads `shared/datasets/orders.csv`
2. Prints: row count, column names, dtypes
3. Prints: count of nulls per column
4. Prints: value counts for `status`
5. Computes `revenue = quantity * unit_price` and prints total revenue for `status == 'completed'` only

---

## Expected skills

- `pd.read_csv()`
- `.shape`, `.dtypes`, `.isna().sum()`
- Boolean filtering

---

## Starter hint

```python
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
orders = pd.read_csv(ROOT / "shared/datasets/orders.csv")
```

---

## Verify

Compare logic with [solutions/02_explore_orders.py](solutions/02_explore_orders.py).

**Next:** [Exercise 3: First transform](03-first-transform.md)
