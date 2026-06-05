# Lesson 1: Cloud DE Landscape

**Time:** ~45 minutes

---

## Why cloud for data?

On-prem clusters require capital expense and ops headcount. Cloud offers:

- **Object storage** — cheap, durable blobs (S3, GCS, ADLS)
- **Managed warehouses** — Snowflake, BigQuery, Redshift
- **Elastic compute** — Spark on EMR/Dataproc, Lambda
- **Pay for use** — but bills surprise teams who don't monitor

---

## Reference architecture (AWS-flavored)

```
Apps/DBs → Kinesis/Kafka → S3 (raw) → Glue/Spark (clean) → S3 (curated) → Athena/Snowflake → BI
                              ↑
                         Airflow MWAA
```

Names change per cloud; **patterns** repeat.

---

## IAM and security (must know)

- Least-privilege roles for pipelines
- Encryption at rest (SSE-S3, KMS)
- No public buckets — ever
- Secrets in Parameter Store / Secrets Manager, not git

---

## Data lake vs warehouse

| | Lake | Warehouse |
|---|------|-------------|
| **Format** | Files (Parquet, JSON) | Tables (columnar) |
| **Schema** | Schema-on-read | Schema-on-write |
| **Cost** | Storage cheap | Compute + storage |
| **Users** | Engineers, ML | Analysts, BI |

Modern stacks **blend**: lakehouse (Delta, Iceberg, Hudi).

---

## Local simulation in this phase

We mirror cloud paths on disk:

```
project/lake/
└── raw/
    └── orders/
        └── dt=2024-01-15/
            └── part-0000.parquet
```

DuckDB reads `lake/raw/orders/dt=2024-01-15/*.parquet` — same as Athena partition pruning.

---

## Reflection

1. Why land raw data in object storage before transforming?
2. What does "schema-on-read" mean?

---

## Up next

[Lesson 2: Object storage patterns →](02-object-storage.md)
