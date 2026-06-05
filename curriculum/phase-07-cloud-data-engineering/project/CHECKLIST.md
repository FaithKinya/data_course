# Phase 7 Project Checklist

- [ ] `lake/raw/orders` uses `dt=` hive partitions
- [ ] Customers and products written as snapshot partitions
- [ ] `lake/curated/orders_enriched` joined with revenue logic
- [ ] Manifest JSON lists partitions and row counts per run
- [ ] Re-run for same date overwrites without duplicates
- [ ] `query_partition` scans only one `dt` folder
- [ ] `query_range` uses hive partition filtering
- [ ] README maps local paths to `s3://` URIs
- [ ] Paths to shared data use project-root-relative references
