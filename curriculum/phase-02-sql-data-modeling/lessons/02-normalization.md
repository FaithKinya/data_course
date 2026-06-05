# Lesson 2: Normalization

**Time:** ~50 minutes

---

## The problem normalization solves

Operational databases (OLTP) store **transactions**: place order, update inventory, change address. If customer name is duplicated on every order row, an address change requires updating thousands of rows — and inconsistencies creep in.

**Normalization** splits data into related tables so each fact is stored once.

---

## First normal form (1NF)

- Atomic columns (no lists in a cell)
- Unique row identifier

Bad: `tags = 'electronics,gadget'`. Good: separate `product_tags` table or one tag per row.

---

## Second normal form (2NF)

- 1NF + every non-key column depends on the **whole** primary key

If order line items use composite key `(order_id, line_num)`, `product_name` must not depend only on `product_id` — it belongs in `products`.

---

## Third normal form (3NF)

- 2NF + no **transitive** dependencies (non-key → non-key)

Example violation: `orders` stores `customer_city` when `customer_id` → `customers.city` already defines it.

```
orders(order_id, customer_id, product_id, quantity, ...)
customers(customer_id, name, city, country, ...)
products(product_id, product_name, category, ...)
```

This is the shape of our ShopStream CSVs — already normalized for OLTP.

---

## When to denormalize

Analytics workloads (OLAP) favor **wide, pre-joined** tables for scan speed. Data warehouses often:

1. Ingest normalized OLTP data
2. Transform into **star schemas** or wide marts
3. Accept redundancy in facts/dimensions for query simplicity

Normalization is for **writes**; dimensional models are for **reads**.

---

## Functional dependency shorthand

Write: `customer_id → name, email, city`

Meaning: knowing `customer_id` uniquely determines those attributes.

Design exercise: list dependencies in `shared/datasets/orders.csv`. Which columns belong elsewhere?

---

## Practical rule for DE

- **Source systems:** keep normalized; don't fight the DBA
- **Warehouse layer:** model for analytics (star/snowflake)
- **Document** where business rules change between layers

---

## Reflection

1. Why is `product_name` in `orders` a normalization problem?
2. Name one column in `orders.csv` that is correctly a foreign key.

---

## Up next

[Lesson 3: Dimensional Modeling →](03-dimensional-modeling.md)
