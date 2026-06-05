# Capstone B: Acceptance Checklist

Use this as your definition of done. Check items as you complete them. Every section must be ≥ 80% complete before calling the capstone finished.

---

## Setup & Documentation

- [ ] Folder structure matches README scaffold
- [ ] `docs/architecture.md` with Kafka flow diagram committed
- [ ] `docs/event-catalog.md` with all 4 event types and JSON examples
- [ ] `docs/sla.md` with latency, retention, and alert thresholds
- [ ] `docs/decisions.md` covers partition key, delivery semantics, window alignment
- [ ] Project README: setup, start/stop commands, sample query output
- [ ] `.gitignore` excludes `storage/`, `logs/`, `__pycache__/`, `.env`

---

## Phase 1 Skills — Foundations

- [ ] Can explain stream-path data lifecycle: produce → validate → aggregate → sink → query
- [ ] Events stored as JSON in Kafka; aggregates stored as Parquet in object storage
- [ ] Run metadata or metrics file captures pipeline health every run/session
- [ ] Local dev workflow documented (Docker up → start consumers → start simulator)

---

## Phase 2 Skills — SQL & Data Modeling

- [ ] Raw event grain: one Kafka message = one user action
- [ ] Aggregate grain documented: one row = one metric per window per dimension (e.g. page_url)
- [ ] DuckDB queries on landed Parquet produce correct rollups
- [ ] `queries/realtime_dashboard.sql` answers "what happened in the last 5 minutes?"
- [ ] `queries/daily_rollup.sql` sums hourly aggregates for a full day

---

## Phase 3 Skills — Python Pipelines

- [ ] Producer, validator, aggregator, archiver are separate modules (not one script)
- [ ] Error handling: consumer crash logs exception and exits cleanly (no silent hang)
- [ ] Idempotent sink writes: re-run for same window produces same file
- [ ] Unit tests pass: `pytest tests/`
- [ ] Graceful shutdown: SIGTERM commits offsets before exit

---

## Phase 4 Skills — Orchestration

- [ ] `scripts/start_pipeline.sh` starts Kafka + all consumer processes
- [ ] `scripts/stop_pipeline.sh` stops consumers before Kafka
- [ ] Consumer restart resumes from last committed offset
- [ ] Documented deploy order: topics → consumers → producer
- [ ] Backpressure considered: simulator rate configurable when lag grows

---

## Phase 5 Skills — Data Warehousing (Optional Batch Layer)

- [ ] Documented how streaming aggregates feed batch/analytics (even if dbt not built)
- [ ] Optional: `dbt_eventpulse` mart on hourly aggregates
- [ ] Optional: incremental dbt model on landed aggregate Parquet
- [ ] Can explain how late-arriving events affect batch rollups vs stream windows

---

## Phase 6 Skills — Streaming

- [ ] Kafka topics created with documented partition counts
- [ ] Event simulator produces configurable rate (≥ 50 events/sec demonstrated)
- [ ] Partition key strategy documented and implemented
- [ ] Schema validator routes invalid events to `dead.letter`
- [ ] Valid events forwarded to `validated.events`
- [ ] 1-minute tumbling windows compute: `page_views`, `unique_users`, `clicks`, `signups`, `revenue`
- [ ] 5-minute and 1-hour windows implemented (or rollup documented)
- [ ] Late events tracked (counter or side output)
- [ ] At-least-once delivery with idempotent sinks documented

---

## Phase 7 Skills — Cloud Data Engineering

- [ ] Aggregate path: `aggregates/{window}/year=/month=/day=/hour=/`
- [ ] Raw archive path: `raw-events/year=/month=/day=/hour=/`
- [ ] Dead letter path: `dead-letter/year=/month=/day=/`
- [ ] Partition pruning works: queries filter on `year`, `month`, `day` columns or path
- [ ] Retention policy documented (raw 7 days, aggregates 30 days, or your choice)
- [ ] Storage size estimated for 24-hour run at target throughput

---

## Phase 8 Skills — Production Best Practices

- [ ] Event schemas defined (JSON Schema or Pydantic) — data contracts
- [ ] Schema validation rejects: missing fields, wrong types, unknown event types
- [ ] Structured JSON logging in all consumer processes
- [ ] Metrics exported: `events_consumed`, `validation_errors`, `consumer_lag`, `window_close_latency_ms`
- [ ] Alert rules: lag threshold, error rate threshold, stale metrics
- [ ] Alerts tested manually (burst script + error injection)
- [ ] `monitoring/health_check.py` returns pass/fail
- [ ] No secrets in Git; Kafka PLAINTEXT acceptable for local only (documented)

---

## Functional Gates

- [ ] Pipeline runs end-to-end for 30 minutes without manual intervention
- [ ] All 4 event types (`page_view`, `click`, `signup`, `purchase`) processed correctly
- [ ] Purchase `amount` summed correctly in revenue metric
- [ ] Dead letter contains rejected events with `rejection_reason`
- [ ] Raw archiver writes validated events to `storage/raw-events/`
- [ ] Aggregator writes to all 3 window sizes (1min, 5min, 1hour)

---

## Reliability Gates

- [ ] Consumer restart (stop → start) resumes processing without duplicate aggregates
- [ ] `scripts/replay_events.py` reprocesses at least 1 hour of raw events
- [ ] Replay produces identical aggregate files (idempotency verified)
- [ ] Simulator `inject_errors: true` does not crash validator
- [ ] `produce_burst.py` does not crash aggregator (lag recovers)

---

## Observability Gates

- [ ] `logs/metrics.jsonl` updated every 30 seconds during run
- [ ] Consumer lag visible in metrics
- [ ] Validation error rate visible in metrics
- [ ] Lag alert fires when burst injected (check logs)
- [ ] Error rate alert fires when `inject_errors` enabled (check logs)
- [ ] Health check returns 1 when consumers stopped

---

## Portfolio & Interview Readiness

- [ ] GitHub repo (or folder) with clean commit history
- [ ] 15-minute walkthrough rehearsed: architecture → live demo → trade-offs
- [ ] Can explain at-least-once vs exactly-once in 60 seconds
- [ ] Can explain partition key choice and hot-partition risk
- [ ] Can explain tumbling vs sliding windows and why you chose tumbling
- [ ] Can explain how this pipeline complements Capstone A (batch analytics)
- [ ] Can walk through one failure scenario and recovery steps
- [ ] Sample query output or screenshot in README

---

## Stretch Goals (Optional)

- [ ] HTTP ingest API (`producers/http_ingest.py`)
- [ ] Kafka UI in Docker Compose
- [ ] Grafana dashboard on metrics
- [ ] Faust or Spark Structured Streaming aggregator
- [ ] Exactly-once with Kafka transactions
- [ ] dbt mart with tests on hourly aggregates
- [ ] Integration: `purchase` events linked to ShopStream capstone

---

## Sign-off

| Item | Value |
|------|-------|
| **Completed date** | __________ |
| **Total hours spent** | __________ |
| **Sections complete** | ___ / 12 |
| **Stretch goals done** | __________ |
| **Ready for interview?** | Yes / Not yet |

When all core sections (Setup through Portfolio) are checked, update [PROGRESS.md](../../PROGRESS.md) Capstone B item.
