# Lesson 3: Dimensional Modeling

**Time:** ~50 minutes

---

## Star schema in one picture

```
                    dim_customer
                         |
dim_date —— fact_orders —— dim_product
```

- **Fact table** — measurements (quantity, revenue); many rows; narrow + numeric
- **Dimension tables** — descriptive context (who, what, when); fewer rows; wide text

Analysts JOIN facts to dimensions — simple, fast mental model.

---

## Fact table design

`fact_orders` grain: **one row per order line** (or per order — pick one and document it).

Typical columns:

| Type | Examples |
|------|----------|
| Keys | `date_key`, `customer_key`, `product_key` |
| Degenerate dims | `order_id` (no separate dim table) |
| Measures | `quantity`, `unit_price`, `revenue` |
| Flags | `is_cancelled`, `is_refunded` |

Store **additive** measures (sum across rows). Don't store ratios in facts — compute in queries or marts.

---

## Dimension tables

**dim_customer:** `customer_key` (surrogate), `customer_id` (natural), `name`, `city`, `country`

**dim_product:** `product_key`, `product_id`, `product_name`, `category`

**dim_date:** `date_key` (YYYYMMDD int), `order_date`, `year`, `month`, `day_of_week`

Use **surrogate keys** (integer IDs you assign) so SCD Type 2 history is possible later.

---

## Star vs snowflake

- **Star** — dimensions are flat (category on `dim_product`)
- **Snowflake** — dimensions normalized (`dim_category` separate)

Stars win for simplicity; snowflakes save space but add JOINs. Most marts star.

---

## Slowly changing dimensions (preview)

If a customer moves cities:

- **Type 1** — overwrite (lose history)
- **Type 2** — new row with new `customer_key` (keep history)

Phase 5+ covers SCD in dbt; for now, Type 1 is fine.

---

## Building in DuckDB

```sql
CREATE TABLE dim_customer AS
SELECT
    ROW_NUMBER() OVER (ORDER BY customer_id) AS customer_key,
    customer_id, name, city, country
FROM read_csv_auto('shared/datasets/customers.csv');
```

Facts reference `customer_key`, not raw `customer_id`, in a full warehouse. For learning, either works — be consistent.

---

## Reflection

1. What is the grain of `fact_orders` for ShopStream?
2. Which dimension would you role-play as "time"?

---

## Up next

[Exercise 1: SELECT practice →](../exercises/01-select-practice.md)
