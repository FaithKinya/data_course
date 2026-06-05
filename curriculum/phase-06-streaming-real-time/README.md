# Phase 6: Streaming & Real-Time

**Goal:** Produce and consume events with Kafka; compare batch vs stream processing.

**Time:** ~1–2 weeks (10–14 hours)

**Prerequisites:** [Phase 5: Data Warehousing](../phase-05-data-warehousing/README.md)

---

## What You'll Learn

- Batch vs streaming tradeoffs
- Kafka topics, producers, consumers
- Event schemas and at-least-once delivery
- Simple stream aggregations (counts, windows)

---

## Learning Path

Complete in order:

| # | Type | Item | Time |
|---|------|------|------|
| 1 | Lesson | [Batch vs stream](lessons/01-batch-vs-stream.md) | 45 min |
| 2 | Lesson | [Events & Kafka](lessons/02-events-kafka.md) | 50 min |
| 3 | Lesson | [Stream processing](lessons/03-stream-processing.md) | 50 min |
| 4 | Exercise | [Produce events](exercises/01-produce-events.md) | 45 min |
| 5 | Exercise | [Consume & aggregate](exercises/02-consume-aggregate.md) | 45 min |
| 6 | Exercise | [Windowed counts](exercises/03-windowed-counts.md) | 45 min |
| 7 | **Project** | [**Clickstream Aggregator**](project/README.md) | 6–8 hrs |

---

## Local Kafka setup

```bash
cd curriculum/phase-06-streaming-real-time
docker compose up -d
```

Broker: `localhost:9092`. See [docker-compose.yml](docker-compose.yml).

---

## Phase Project Preview

Simulate ShopStream clickstream events to Kafka, aggregate page views in real time, and write rolling counts to a local sink.

---

## Success Criteria

Before moving to Phase 7, you should be able to:

- [ ] Start Kafka with Docker Compose
- [ ] Write a Python producer and consumer with `kafka-python`
- [ ] Explain at-least-once vs exactly-once at a high level
- [ ] Compute running aggregates from a topic
- [ ] Complete the phase project checklist

---

## Next Phase

[Phase 7: Cloud Data Engineering →](../phase-07-cloud-data-engineering/README.md)
