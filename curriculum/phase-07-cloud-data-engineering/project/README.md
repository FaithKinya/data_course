# Phase 7 Project: Cloud-Native Batch Load

**Time:** 6–8 hours  
**Deliverable:** Local data lake with raw + curated zones, manifests, and partition-aware queries

---

## Scenario

ShopStream is migrating to AWS. Before cloud access, prototype the **lake layout** locally: ingest CSVs to hive-partitioned raw zone, promote to curated Parquet, register manifests for downstream Athena-style queries.

---

## Requirements

### 1. Lake layout

```
project/lake/
├── raw/
│   ├── orders/dt=YYYY-MM-DD/part-0000.parquet
│   ├── customers/snapshot=YYYY-MM-DD/part-0000.parquet
│   └── products/snapshot=YYYY-MM-DD/part-0000.parquet
├── curated/
│   └── orders_enriched/dt=YYYY-MM-DD/part-0000.parquet
└── manifests/
    └── load_{run_id}.json
```

### 2. Pipeline `project/lake_pipeline.py`

- CLI: `python lake_pipeline.py --run-date 2024-01-20`
- **Raw load:** copy/transform CSVs into partitioned paths (orders by `dt`, dims by snapshot date)
- **Curated load:** join orders + customers + products; add `revenue`; write partitioned curated
- **Manifest:** JSON with `run_id`, `partitions_written`, `row_counts`, `status`

### 3. Query module `project/query_lake.py`

- Function `query_partition(dt)` — reads only one `curated/.../dt=` folder via DuckDB
- Function `query_range(start, end)` — reads multiple partitions with hive_partitioning

### 4. Idempotency

Re-running same `--run-date` overwrites that date's partitions only.

---

## Step-by-step guide

### Step 1: Path utilities (1 hr)

Reuse Exercise 1 patterns; centralize in `paths.py`.

### Step 2: Raw zone (2 hr)

Partition orders; snapshot customers/products.

### Step 3: Curated zone (2 hr)

Enriched joins + revenue rules from prior phases.

### Step 4: Manifests + query (1.5 hr)

Write manifest; demonstrate partition pruning in `query_lake.py`.

### Step 5: Document (1 hr)

Map local paths to hypothetical `s3://shopstream-lake/...` URIs in README.

---

## Acceptance criteria

- [ ] `lake_pipeline.py` populates raw and curated zones
- [ ] Manifest written per run under `manifests/`
- [ ] `query_partition` reads single `dt` without scanning all history
- [ ] README includes S3 URI mapping table
- [ ] CHECKLIST.md complete

---

## What you learned

**Cloud-native layout** on your laptop — ready to swap local paths for S3 SDK calls.

**Next phase:** [Phase 8: Production & Pro Practices](../../phase-08-production-best-practices/README.md)
