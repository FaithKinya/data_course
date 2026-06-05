# Exercise 3: Data Contracts

**Time:** ~45 minutes

---

## Goal

Author a YAML data contract and validate a CSV against it.

---

## Tasks

1. Create `exercises/my_work/contracts/orders_v1.yaml`:

```yaml
dataset: orders
version: v1
owner: data-engineering
sla:
  freshness_hours: 24
schema:
  - name: order_id
    type: integer
    required: true
    unique: true
  - name: status
    type: string
    allowed_values: [completed, cancelled, refunded]
```

(Include all columns from `orders.csv`.)

2. Create `exercises/my_work/03_validate_contract.py`:
   - Load contract YAML
   - Load `shared/datasets/orders.csv`
   - Check required columns, types, allowed values, uniqueness
   - Print human-readable report; exit 1 on violation

---

## Deliverable

Contract file + validator script. No external contract tools required — pure Python + PyYAML.

---

## Verify

Compare with [solutions/orders_v1.yaml](solutions/orders_v1.yaml) and [solutions/03_validate_contract.py](solutions/03_validate_contract.py).

**Next:** [Phase project →](../project/README.md)
