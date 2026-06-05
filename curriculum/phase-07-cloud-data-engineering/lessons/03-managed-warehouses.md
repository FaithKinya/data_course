# Lesson 3: Managed Warehouses

**Time:** ~50 minutes

---

## Warehouse vs query-on-lake

| Approach | Examples | Strength |
|----------|----------|----------|
| **External tables** | Athena, Hive | Cheap storage, pay per query |
| **Managed warehouse** | Snowflake, BigQuery | Performance, governance |
| **Lakehouse** | Databricks, Iceberg | Unified batch + stream |

Data engineers connect **ingestion → lake → warehouse → BI**.

---

## Snowflake (conceptual)

- Storage and compute **separate** — scale warehouses up/down
- Micro-partitions auto-optimize reads
- `COPY INTO` loads from S3 stages

---

## BigQuery (conceptual)

- Serverless — no cluster sizing
- Bills on **bytes scanned** — partitioning/clustering critical
- Native `LOAD` and federated queries over GCS

---

## DuckDB as local stand-in

```sql
SELECT *
FROM read_parquet('project/lake/raw/orders/dt=2024-01-15/*.parquet');
```

Or hive partitioning:

```sql
SELECT *
FROM read_parquet('project/lake/raw/orders/*/*.parquet', hive_partitioning=true);
```

Same SQL thinking transfers to Athena `MSCK REPAIR` and Snowflake external tables.

---

## External table workflow

1. Pipeline writes Parquet to `lake/raw/orders/dt=.../`
2. Catalog (Glue) registers partitions
3. Athena/Snowflake queries external table
4. dbt builds marts on top (Phase 5 pattern)

---

## Cost awareness preview

- **Listing** — `aws s3 ls` on 1M prefixes is slow and costly
- **Scanning** — BigQuery charges for full table scan without partition filter
- **Egress** — moving data out of cloud region costs money

Exercise 3 quantifies small-file impact locally.

---

## Reflection

1. Why would you keep raw Parquet in S3 *and* load to Snowflake?
2. How does partition pruning reduce cost?

---

## Up next

[Exercise 1: S3-style paths →](../exercises/01-s3-paths.md)
