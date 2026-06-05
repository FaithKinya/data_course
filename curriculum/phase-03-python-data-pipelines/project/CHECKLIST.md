# Phase 3 Project Checklist

- [ ] Code split into extract, validate, transform, load modules
- [ ] Reads from `shared/datasets/` with clear errors if missing
- [ ] Invalid orders quarantined to `output/rejects/`
- [ ] Revenue rules: completed positive, refunded negative, cancelled zero
- [ ] `orders_enriched` includes customer and product fields
- [ ] `daily_revenue_summary` aggregated by date and category
- [ ] Parquet loads use atomic write pattern
- [ ] Second pipeline run produces same output row counts
- [ ] `run_metadata.json` written every run with `status`
- [ ] `pipeline.py` exits with code 1 on failure
