# Exercise 2: JOINs & Aggregations

**Time:** ~45 minutes

---

## Goal

Join orders to customers and products; produce analytics-ready summaries.

---

## Tasks

Write SQL (DuckDB) that answers:

1. **Revenue by country** — total revenue for `completed` orders, joined via `customers`
2. **Revenue by product category** — join `products`, group by `category`
3. **Top customer per country** — customer with highest completed revenue in each country (hint: window function `ROW_NUMBER()`)
4. **Daily order trend** — order count and revenue by `order_date`

---

## Expected output shapes

| Query | Columns (minimum) |
|-------|-------------------|
| 1 | `country`, `total_revenue` |
| 2 | `category`, `order_count`, `total_revenue` |
| 3 | `country`, `name`, `total_revenue` |
| 4 | `order_date`, `order_count`, `total_revenue` |

---

## Hints

```sql
WITH base AS (
    SELECT o.*, c.country, p.category,
           o.quantity * o.unit_price AS revenue
    FROM read_csv_auto('shared/datasets/orders.csv') o
    JOIN read_csv_auto('shared/datasets/customers.csv') c
      ON o.customer_id = c.customer_id
    JOIN read_csv_auto('shared/datasets/products.csv') p
      ON o.product_id = p.product_id
    WHERE o.status = 'completed'
)
SELECT ...
```

---

## Verify

Compare with [solutions/02_joins_aggregations.py](solutions/02_joins_aggregations.py).

**Next:** [Exercise 3: Design a schema](03-schema-design.md)
