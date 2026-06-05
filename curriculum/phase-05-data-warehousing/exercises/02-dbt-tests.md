# Exercise 2: dbt Tests

**Time:** ~45 minutes

---

## Goal

Add generic and singular tests to catch bad data before marts.

---

## Tasks

In your exercise dbt project, create `models/staging/schema.yml`:

1. **Generic tests** on `stg_orders`:
   - `order_id` — `unique`, `not_null`
   - `status` — `accepted_values` in `completed`, `cancelled`, `refunded`
   - `customer_id` — `relationships` to `stg_customers`

2. **Singular test** `tests/assert_positive_quantity.sql`:

```sql
select order_id from {{ ref('stg_orders') }} where quantity <= 0
```

Should return 0 rows to pass.

3. Run `dbt test` — all green.

---

## Experiment

Temporarily add `where quantity = -1` logic to staging (or bad seed row). Confirm test fails. Revert.

---

## Verify

See [solutions/schema_staging.yml](solutions/schema_staging.yml).

**Next:** [Exercise 3: Documentation](03-documentation.md)
