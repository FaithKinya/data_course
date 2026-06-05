# Lesson 2: Intro to dbt

**Time:** ~50 minutes

---

## What dbt does

**dbt (data build tool)** runs SQL `SELECT` statements and materializes results as tables/views in your warehouse. It adds:

- **Refactoring** — `{{ ref('stg_orders') }}` builds dependency graph
- **Tests** — `unique`, `not_null`, relationships
- **Docs** — auto-generated lineage site
- **Jinja** — macros and loops in SQL

No extract/load — dbt is **transform-only** (the T in ELT).

---

## Project structure

```
shopstream_dbt/
├── dbt_project.yml
├── models/
│   ├── staging/
│   │   └── stg_orders.sql
│   └── marts/
│       └── fct_revenue_daily.sql
├── seeds/          # optional CSV copies
└── schema.yml      # tests + descriptions
```

---

## Staging models

One staging model per source table. Light cleaning only:

```sql
-- models/staging/stg_orders.sql
select
    order_id,
    customer_id,
    product_id,
    cast(order_date as date) as order_date,
    quantity,
    unit_price,
    lower(status) as status
from {{ source('shopstream', 'orders') }}
```

Define sources in `schema.yml`:

```yaml
sources:
  - name: shopstream
    tables:
      - name: orders
```

---

## Marts

Business-facing models join staging tables:

```sql
-- models/marts/fct_revenue_daily.sql
select
    o.order_date,
    p.category,
    sum(case when o.status = 'completed' then o.quantity * o.unit_price else 0 end) as revenue
from {{ ref('stg_orders') }} o
join {{ ref('stg_products') }} p on o.product_id = p.product_id
group by 1, 2
```

---

## Core commands

```bash
dbt debug          # test connection
dbt run            # build models
dbt test           # run tests
dbt docs generate && dbt docs serve
```

---

## Materializations

| Type | Behavior |
|------|----------|
| `view` | Default; always fresh |
| `table` | Full rebuild each run |
| `incremental` | Append/merge new rows only |

Staging → usually `view`. Large facts → `incremental`.

---

## Reflection

1. Why keep heavy business logic out of staging models?
2. What does `ref()` give you that raw table names don't?

---

## Up next

[Lesson 3: Incremental models →](03-incremental-models.md)
