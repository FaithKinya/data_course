# Phase 8 Project Checklist

- [ ] Data contracts exist for orders, customers, products
- [ ] Contract specifies version, owner, and SLA
- [ ] Validation runs before transform (fail-fast)
- [ ] Great Expectations or equivalent checks on key columns
- [ ] Failed validation writes quarantine file and exits 1
- [ ] JSON logs written to `logs/pipeline.jsonl`
- [ ] All log lines include `run_id` and `stage`
- [ ] `run_metadata.json` includes validation summary
- [ ] `--dry-run` validates without loading marts
- [ ] README documents contract versioning and run instructions
