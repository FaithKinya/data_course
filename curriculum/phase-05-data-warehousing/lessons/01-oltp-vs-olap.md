# Lesson 1: OLTP vs OLAP

**Time:** ~45 minutes

---

## Two database workloads

| | OLTP | OLAP |
|---|------|------|
| **Purpose** | Run the business (orders, payments) | Analyze the business |
| **Queries** | Short, indexed lookups | Large scans, aggregations |
| **Schema** | Normalized (3NF) | Star/snowflake, wide marts |
| **Users** | Applications | Analysts, BI tools, ML |
| **Examples** | Postgres, MySQL | Snowflake, BigQuery, DuckDB |

Data engineers **replicate** OLTP → transform → **serve** OLAP.

---

## The modern warehouse stack

```
Sources → Ingestion (Airflow/Fivetran) → Raw/Landing → dbt → Marts → BI
```

- **Ingestion** lands data cheaply and fast
- **dbt** applies business logic in SQL (version controlled)
- **Marts** are the "official" metrics layer

---

## Why not query OLTP directly?

- Heavy analytics slow down checkout
- Historical changes lost (overwrites)
- Joins across systems don't exist in one DB

Replication to a warehouse decouples **operations** from **analytics**.

---

## DuckDB in this course

DuckDB is an in-process OLAP engine — perfect for learning:

- Reads CSV/Parquet natively
- SQL dialect close to Postgres/BigQuery
- dbt-duckdb adapter for local dev

Production might use Snowflake; dbt models port with minor edits.

---

## Medallion architecture

| Layer | Contents |
|-------|----------|
| **Bronze** | Raw ingested data |
| **Silver** | Cleaned, conformed (dbt staging) |
| **Gold** | Business marts (dbt marts) |

Your Phase 3 `staging/` ≈ silver; `marts/` ≈ gold.

---

## Reflection

1. Why shouldn't analysts run heavy JOINs on the production orders DB?
2. Where does dbt sit in the stack diagram above?

---

## Up next

[Lesson 2: Intro to dbt →](02-intro-dbt.md)
