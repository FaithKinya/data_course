# Lesson 1: Batch vs Stream

**Time:** ~45 minutes

---

## Two processing modes

| | Batch | Streaming |
|---|-------|-----------|
| **Data** | Bounded (yesterday's files) | Unbounded (continuous events) |
| **Latency** | Minutes to hours | Seconds to milliseconds |
| **Correctness** | Easier — full snapshot | Harder — ordering, duplicates |
| **Tools** | Airflow, Spark batch | Kafka, Flink, Spark Streaming |
| **Cost** | Cheaper per TB | Higher infra complexity |

Most companies use **both**: batch for finance close, streams for fraud alerts.

---

## Lambda vs Kappa (preview)

- **Lambda** — batch layer + speed layer merged at query time
- **Kappa** — everything is a stream; reprocess history by replaying topic

Modern trend: **streaming-first** with batch compatibility.

---

## When streaming wins

- Fraud detection during checkout
- Live dashboard of active users
- IoT sensor anomaly alerts
- Inventory reservation across services

---

## When batch wins

- Monthly financial reports
- Training ML models on full history
- Backfills after schema changes
- Small teams without ops bandwidth for Kafka

---

## ShopStream example

| Use case | Mode |
|----------|------|
| Daily revenue mart | Batch (Phases 3–5) |
| Live product page views | Stream (this phase) |
| Annual tax filing | Batch |

---

## Event vs row

Batch thinks in **tables** (rows). Streaming thinks in **events** (facts that happened):

```json
{"event": "page_view", "user_id": 42, "page": "/products/101", "ts": "2024-01-20T10:00:00Z"}
```

---

## Reflection

1. Would you stream or batch ShopStream order exports? Why?
2. What latency does a "live sales ticker" need?

---

## Up next

[Lesson 2: Events & Kafka →](02-events-kafka.md)
