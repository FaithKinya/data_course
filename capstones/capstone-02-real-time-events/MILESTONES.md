# Capstone B: Milestones

**Total duration:** 4–6 weeks  
**Recommended pace:** 8–12 hours per week

Mark each milestone complete before moving on. Weeks 1–3 are sequential (Kafka → validate → aggregate). Weeks 4–6 can partially overlap.

---

## Milestone 0: Kickoff (Day 1 — 2 hours)

**Goal:** Understand the streaming problem space, scaffold repo, draft architecture.

### Tasks
- [ ] Read [README.md](README.md) end-to-end
- [ ] Create folder structure from README scaffold
- [ ] Write `docs/architecture.md` with:
  - Event flow diagram
  - Topic list with partition counts
  - Delivery semantics choice (at-least-once recommended)
  - Latency SLA target (e.g. aggregates available within 90 seconds of event)
- [ ] Write `docs/event-catalog.md` skeleton with 4 event types
- [ ] Verify Docker Desktop running: `docker info`

### Exit criteria
- Architecture doc committed with Kafka diagram
- Event catalog lists all 4 event types with required fields
- Docker confirmed working

### Curriculum touchpoints
- **Phase 6:** [Batch vs stream](../../curriculum/phase-06-streaming-real-time/lessons/01-batch-vs-stream.md), [Events & Kafka](../../curriculum/phase-06-streaming-real-time/lessons/02-events-kafka.md)

---

## Milestone 1: Kafka Infrastructure & Event Production (Week 1 — 8–10 hours)

**Goal:** Kafka cluster running locally; realistic events flowing to `raw.events`.

### Tasks
- [ ] Create `docker/docker-compose.yml` with Zookeeper + Kafka (adapt from Phase 6)
- [ ] Write `docker/kafka/create-topics.sh`:
  - `raw.events` (6 partitions)
  - `validated.events` (6 partitions)
  - `dead.letter` (3 partitions)
- [ ] Define event schemas in `schemas/` (JSON Schema or Pydantic `registry.py`)
- [ ] Implement `producers/event_simulator.py`:
  - Configurable events/sec rate
  - Realistic `user_id` pool (1000 users)
  - Page catalog (20+ URLs)
  - Weighted event mix: 70% page_view, 20% click, 5% signup, 5% purchase
  - ISO 8601 timestamps
- [ ] Create `producers/simulator_config.yaml` for rate and mix tuning
- [ ] Implement `consumers/base_consumer.py` — shared connection, offset commit, graceful shutdown
- [ ] Write `consumers/debug_consumer.py` (temporary) — print events to verify flow
- [ ] Write `scripts/start_pipeline.sh` and `scripts/stop_pipeline.sh`

### Exit criteria
- `docker compose up -d` starts Kafka healthy
- `./kafka/create-topics.sh` creates all topics
- Simulator runs at 50 events/sec for 2 minutes without errors
- Debug consumer receives events; `kafka-console-consumer` confirms message count
- Ctrl+C on simulator commits cleanly (no zombie processes)

### Curriculum touchpoints
- **Phase 1:** [Data formats](../../curriculum/phase-01-foundations/lessons/03-data-formats.md) (JSON events)
- **Phase 3:** [Pipeline anatomy](../../curriculum/phase-03-python-data-pipelines/lessons/01-pipeline-anatomy.md)
- **Phase 6:** [Produce events](../../curriculum/phase-06-streaming-real-time/exercises/01-produce-events.md), [Phase 6 project](../../curriculum/phase-06-streaming-real-time/project/README.md)

---

## Milestone 2: Schema Validation & Dead Letter (Week 2 — 8–10 hours)

**Goal:** Invalid events quarantined; valid events forwarded to `validated.events`.

### Tasks
- [ ] Implement `consumers/schema_validator.py`:
  - Consume from `raw.events`
  - Validate against schemas (required fields, types, timestamp parseable)
  - Publish valid events to `validated.events` (preserve partition key)
  - Publish invalid events to `dead.letter` with `rejection_reason` and `original_payload`
- [ ] Add validation rules:
  - `timestamp` within last 24 hours (reject future timestamps > 5 min ahead)
  - `user_id` non-empty string
  - `purchase.amount` positive number
  - Unknown `event_type` → dead letter
- [ ] Write `tests/test_schemas.py` — valid and invalid payload cases
- [ ] Inject 5% malformed events in simulator (config flag `inject_errors: true`)
- [ ] Log validation stats: `valid_count`, `invalid_count`, `invalid_rate`
- [ ] Update `docs/event-catalog.md` with full JSON examples per event type

### Exit criteria
- Validator runs continuously alongside simulator
- Dead letter topic contains rejected events with reasons
- `validated.events` contains only schema-compliant events
- Unit tests pass: `pytest tests/test_schemas.py`
- Invalid rate metric logged every 30 seconds

### Curriculum touchpoints
- **Phase 8:** [Data contracts](../../curriculum/phase-08-production-best-practices/exercises/03-data-contracts.md), [data quality](../../curriculum/phase-08-production-best-practices/lessons/01-data-quality.md)
- **Phase 2:** [Grain](../../curriculum/phase-02-sql-data-modeling/lessons/03-dimensional-modeling.md) — event-level grain for raw, window grain for aggregates

---

## Milestone 3: Windowed Aggregations (Week 3 — 10–12 hours)

**Goal:** Compute tumbling window metrics from validated events.

### Tasks
- [ ] Implement `consumers/window_aggregator.py`:
  - Consume from `validated.events`
  - Maintain in-memory state per tumbling window
  - 1-minute windows: `page_views`, `unique_users`, `clicks` per `page_url`; `signups` and `revenue` global
  - Emit aggregate record on window close
- [ ] Handle window boundaries aligned to wall-clock (not processing time only — document choice)
- [ ] Track late events: events arriving > 30s after window close → `late_events` counter
- [ ] Implement 5-minute and 1-hour windows (separate tumbling or rollup — document in `docs/decisions.md`)
- [ ] Write `tests/test_aggregator.py`:
  - Known input events → expected counts for a 1-min window
  - Empty window produces zero-row or skip (document behavior)
- [ ] Add `scripts/produce_burst.py` — inject 500 events in 10 seconds for load test

### Exit criteria
- Aggregator runs for 10 minutes without memory leak (monitor process RSS)
- Manual verification: send 10 `page_view` events for `/home` in same minute → `page_views = 10`
- Unique users count correct for 3 events from 2 distinct `user_id`s
- Late event counter increments when injecting delayed timestamps
- Unit tests pass

### Curriculum touchpoints
- **Phase 6:** [Consume & aggregate](../../curriculum/phase-06-streaming-real-time/exercises/02-consume-aggregate.md), [windowed counts](../../curriculum/phase-06-streaming-real-time/exercises/03-windowed-counts.md), [stream processing](../../curriculum/phase-06-streaming-real-time/lessons/03-stream-processing.md)

---

## Milestone 4: Storage Sinks & Partitioning (Week 4 — 8–10 hours)

**Goal:** Aggregates and raw events land in partitioned Parquet with idempotent writes.

### Tasks
- [ ] Implement `sinks/path_builder.py`:
  - `aggregates/{window_size}/year=YYYY/month=MM/day=DD/hour=HH/`
  - `raw-events/year=YYYY/month=MM/day=DD/hour=HH/`
  - `dead-letter/year=YYYY/month=MM/day=DD/`
- [ ] Implement `sinks/parquet_writer.py`:
  - Deterministic filename: `{window_start}_{metric_type}.parquet`
  - Overwrite on re-run (idempotent)
  - Snappy compression
- [ ] Implement `consumers/raw_archiver.py` — write validated events to raw storage
- [ ] Wire aggregator output → `parquet_writer`
- [ ] Write `queries/realtime_dashboard.sql` — DuckDB query for last 5 minutes of 1-min aggregates
- [ ] Write `queries/daily_rollup.sql` — sum hourly aggregates for a day
- [ ] Write `tests/test_path_builder.py` — path correctness for edge cases (midnight, month boundary)

### Exit criteria
- 30 minutes of pipeline run produces Parquet files in correct partitions
- DuckDB query: `SELECT SUM(page_views) FROM 'storage/aggregates/1min/...'` returns sensible numbers
- Re-running aggregator for same window overwrites file (no duplicate rows on read)
- Path builder tests pass
- Storage size estimate documented in `docs/sla.md`

### Curriculum touchpoints
- **Phase 7:** [Object storage patterns](../../curriculum/phase-07-cloud-data-engineering/lessons/02-object-storage.md), [S3-style paths](../../curriculum/phase-07-cloud-data-engineering/exercises/01-s3-paths.md), [partitioned writes](../../curriculum/phase-07-cloud-data-engineering/exercises/02-partitioned-writes.md), [Phase 7 project](../../curriculum/phase-07-cloud-data-engineering/project/README.md)
- **Phase 3:** [Idempotent loads](../../curriculum/phase-03-python-data-pipelines/exercises/03-idempotent-load.md)

---

## Milestone 5: Monitoring & Alerting (Week 5 — 8–10 hours)

**Goal:** Operators can see pipeline health and get alerted on anomalies.

### Tasks
- [ ] Implement `monitoring/metrics.py`:
  - Counters: `events_consumed`, `events_produced`, `validation_errors`, `aggregate_rows_written`
  - Gauges: `consumer_lag` (messages behind latest offset), `window_close_latency_ms`
  - Export to `logs/metrics.jsonl` every 30 seconds
- [ ] Implement `monitoring/health_check.py`:
  - Check Kafka broker reachable
  - Check consumer groups have active members
  - Check metrics file updated within last 2 minutes
  - Return exit code 0 (healthy) or 1 (unhealthy)
- [ ] Implement `monitoring/alerts.py`:
  - Rule: `consumer_lag > 1000` → log ALERT
  - Rule: `validation_error_rate > 10%` → log ALERT
  - Rule: no metrics for 2 minutes → log ALERT
- [ ] Test alerts with `produce_burst.py` (lag spike) and `inject_errors: true` (error rate)
- [ ] Write `docs/sla.md` — latency target, availability, retention, alert thresholds
- [ ] Add structured JSON logging to all consumers: `level`, `timestamp`, `component`, `message`, `event_id`

### Exit criteria
- `metrics.jsonl` contains entries every 30 seconds during pipeline run
- `python monitoring/health_check.py` returns 0 when pipeline healthy, 1 when stopped
- Lag alert fires when burst injected (visible in logs)
- SLA doc committed with measurable targets

### Curriculum touchpoints
- **Phase 4:** [Retries & sensors](../../curriculum/phase-04-etl-orchestration/exercises/03-retries-sensors.md) (lag as operational signal)
- **Phase 8:** [Observability](../../curriculum/phase-08-production-best-practices/lessons/02-observability.md), [pipeline logging](../../curriculum/phase-08-production-best-practices/exercises/02-pipeline-logging.md), [Phase 8 project](../../curriculum/phase-08-production-best-practices/project/README.md)

---

## Milestone 6: Production Hardening & Portfolio (Week 6 — 8–10 hours)

**Goal:** Replay capability, documentation, interview-ready demo.

### Tasks
- [ ] Implement `scripts/replay_events.py`:
  - Read from `storage/raw-events/` for a date range
  - Re-publish to `raw.events` (or process directly)
  - Idempotent: re-aggregation produces same output files
- [ ] Implement graceful shutdown for all consumers (SIGTERM handler, commit offsets)
- [ ] Optional: `dbt_eventpulse/` mart on hourly aggregates
- [ ] Write project README: prerequisites, start/stop, sample queries, architecture summary
- [ ] Complete [CHECKLIST.md](CHECKLIST.md)
- [ ] Record or script 15-minute demo walkthrough
- [ ] Write `docs/decisions.md` ADRs:
  - Partition key choice
  - At-least-once vs exactly-once
  - Window alignment (event time vs processing time)
  - 5-min/1-hour rollup strategy
- [ ] `.gitignore`: `storage/`, `logs/`, `__pycache__/`, `.env`

### Exit criteria
- Replay script reprocesses one hour of raw events successfully
- Consumer restart after kill -9 resumes correctly (at-least-once, no crash loop)
- CHECKLIST.md ≥ 80% complete
- 15-minute walkthrough deliverable without notes
- Cross-reference to Capstone A documented (how batch + stream fit together)

### Curriculum touchpoints
- **Phase 1:** [Data lifecycle](../../curriculum/phase-01-foundations/lessons/02-data-lifecycle.md) — stream path vs batch path
- **Phase 5:** Optional dbt mart — [incremental models](../../curriculum/phase-05-data-warehousing/lessons/03-incremental-models.md)
- **Phase 8:** [CI/CD](../../curriculum/phase-08-production-best-practices/lessons/03-cicd-pipelines.md) — optional CI for `pytest tests/`

---

## Milestone Summary Table

| # | Week | Theme | Hours | Hard gate |
|---|------|-------|-------|-----------|
| 0 | Day 1 | Kickoff | 2 | Architecture + event catalog |
| 1 | 1 | Kafka + producers | 8–10 | 50 evt/sec sustained |
| 2 | 2 | Schema validation | 8–10 | Dead letter routing works |
| 3 | 3 | Window aggregations | 10–12 | Correct 1-min counts verified |
| 4 | 4 | Storage sinks | 8–10 | DuckDB query returns data |
| 5 | 5 | Monitoring + alerts | 8–10 | Lag alert tested |
| 6 | 6 | Hardening + portfolio | 8–10 | Replay + demo ready |

---

## If You Get Stuck

| Blocker | Try this |
|---------|----------|
| Kafka won't start | Check port 9092 not in use; `docker compose logs kafka` |
| Consumer not receiving | Verify topic name, `auto.offset.reset=earliest`, consumer group id |
| Window counts wrong | Print events in window before close; check timezone on timestamps |
| Memory growing | Flush window state on close; limit in-memory dict size; check for unbounded keys |
| Lag always high | Increase consumer instances (≤ partition count); reduce simulator rate |
| Parquet files empty | Check aggregator emit logic; verify sink path exists and is writable |

---

**Track daily progress in [CHECKLIST.md](CHECKLIST.md).**
