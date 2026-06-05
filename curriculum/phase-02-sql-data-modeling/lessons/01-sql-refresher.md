# Lesson 1: SQL Refresher

**Time:** ~50 minutes

---

## Why SQL still matters

Python is great for glue code; **SQL is the language of data at scale**. Warehouses (Snowflake, BigQuery, DuckDB) push computation to the data. Every data engineer writes SQL daily.

---

## Core clauses (in logical order)

```sql
SELECT   customer_id, SUM(quantity * unit_price) AS revenue
FROM     orders
WHERE    status = 'completed'
GROUP BY customer_id
HAVING   SUM(quantity * unit_price) > 100
ORDER BY revenue DESC
LIMIT    10;
```

| Clause | Purpose |
|--------|---------|
| `WHERE` | Filter rows **before** aggregation |
| `GROUP BY` | Collapse rows into groups |
| `HAVING` | Filter groups **after** aggregation |
| `ORDER BY` | Sort result set |

---

## JOIN types you'll use most

- **INNER JOIN** — only matching keys on both sides
- **LEFT JOIN** — keep all left rows; NULLs where no match
- **CROSS JOIN** — Cartesian product (rare; watch row explosion)

```sql
SELECT o.order_id, c.name, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products  p ON o.product_id  = p.product_id;
```

---

## Aggregations

Common functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.

- `COUNT(*)` counts rows; `COUNT(col)` ignores NULLs
- Use `COUNT(DISTINCT col)` for unique values
- Always know your **grain**: one row per what?

---

## CTEs improve readability

```sql
WITH completed AS (
    SELECT *, quantity * unit_price AS revenue
    FROM orders
    WHERE status = 'completed'
)
SELECT customer_id, SUM(revenue) AS total_revenue
FROM completed
GROUP BY customer_id;
```

CTEs are not "faster" by default — they make complex logic maintainable.

---

## DuckDB tip

DuckDB reads CSVs directly:

```sql
SELECT * FROM read_csv_auto('shared/datasets/orders.csv') LIMIT 5;
```

Run via CLI: `duckdb` or Python `duckdb.connect().sql(...)`.

---

## Reflection

1. What's the difference between `WHERE status = 'completed'` and `HAVING status = 'completed'` after `GROUP BY`?
2. Write a query (on paper) for total revenue by `country` using orders + customers.

---

## Up next

[Lesson 2: Normalization →](02-normalization.md)
