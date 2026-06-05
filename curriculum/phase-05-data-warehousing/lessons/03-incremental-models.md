# Lesson 3: Incremental Models

**Time:** ~50 minutes

---

## When full rebuilds don't scale

A 500M-row fact table rebuilt nightly wastes time and money. **Incremental models** process only new/changed rows.

---

## Basic pattern

```sql
{{ config(materialized='incremental', unique_key='order_id') }}

select * from {{ ref('stg_orders') }}

{% if is_incremental() %}
  where order_date > (select max(order_date) from {{ this }})
{% endif %}
```

First run: full table. Later runs: filter to new dates only.

---

## Strategies

| Strategy | Config | Use when |
|----------|--------|----------|
| **Append** | no unique_key | Events immutable, no updates |
| **Merge** | `incremental_strategy='merge'` | Updates exist (DuckDB 0.9+) |
| **Delete+insert** | partition overwrite | Daily partitions |

ShopStream orders are small — use incremental for **learning**, not necessity.

---

## `is_incremental()` macro

Returns `true` only when target table already exists and run is incremental. Never use raw `if` on run flags — use dbt's macro.

---

## Testing incremental logic

1. `dbt run --full-refresh` — baseline
2. Add rows to source CSV
3. `dbt run` — only new rows processed
4. Compare counts

---

## Pitfalls

- **Late-arriving data** — watermark too aggressive misses rows
- **Schema changes** — need migration plan
- **Duplicates** — always set `unique_key` for merge

For ShopStream, `order_id` is a natural unique key.

---

## Snapshots (preview)

dbt **snapshots** capture SCD Type 2 history:

```bash
dbt snapshot
```

Use when dimension attributes change over time (customer city moves).

---

## Reflection

1. What column would you use as watermark for ShopStream orders?
2. When would you choose `--full-refresh`?

---

## Up next

[Exercise 1: Staging models →](../exercises/01-staging-models.md)
