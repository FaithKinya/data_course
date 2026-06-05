# Phase 6 Project Checklist

- [ ] `docker compose up -d` starts Kafka and UI
- [ ] Producer publishes to `shopstream.clicks` with valid JSON schema
- [ ] Consumer uses dedicated `group_id`
- [ ] Per-page totals increment correctly
- [ ] 5-minute window buckets appear in output
- [ ] `aggregates.json` flushes every 30 seconds
- [ ] Product enrichment works for `/products/{id}` pages
- [ ] Offset commit allows resume after consumer restart
- [ ] README has start/run/stop instructions
