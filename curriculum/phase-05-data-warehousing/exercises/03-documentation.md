# Exercise 3: Documentation

**Time:** ~30 minutes

---

## Goal

Document models and publish dbt docs site.

---

## Tasks

1. Add descriptions to all staging models in `schema.yml` (model + column level for key fields)
2. Add one mart model `marts/dim_customers.sql` — select from `stg_customers` with doc block
3. Run:

```bash
dbt run --select marts
dbt docs generate
dbt docs serve
```

4. Open http://localhost:8080 (dbt default) and verify lineage graph shows staging → marts

---

## Deliverable

Screenshot or note: which models appear upstream of `dim_customers`?

---

## Verify

Compare with [solutions/dim_customers.sql](solutions/dim_customers.sql).

**Next:** [Phase project →](../project/README.md)
