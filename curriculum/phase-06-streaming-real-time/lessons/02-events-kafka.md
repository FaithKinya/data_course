# Lesson 2: Events & Kafka

**Time:** ~50 minutes

---

## Apache Kafka in one paragraph

Kafka is a **distributed log**: producers append messages to **topics**; consumers read at their own pace. Messages are retained (days/weeks), so you can replay history.

---

## Core concepts

| Term | Meaning |
|------|---------|
| **Topic** | Named channel (e.g. `clickstream`) |
| **Partition** | Ordered sub-log for parallelism |
| **Offset** | Position in partition |
| **Consumer group** | Cooperating consumers share work |
| **Broker** | Kafka server (our Docker container) |

---

## Producer (Python)

```python
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)
producer.send("clickstream", {"event": "page_view", "page": "/home"})
producer.flush()
```

---

## Consumer (Python)

```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "clickstream",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    group_id="click-aggregator",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)
for msg in consumer:
    print(msg.value)
```

---

## Delivery semantics

- **At-most-once** — may lose messages
- **At-least-once** — may duplicate (common default)
- **Exactly-once** — Kafka transactions + idempotent consumers (advanced)

Start with at-least-once + **idempotent sinks**.

---

## Schema discipline

Agree on JSON fields: `event`, `user_id`, `page`, `ts`. Breaking changes need new topic version (`clickstream.v2`) or schema registry (Avro/Protobuf).

---

## Local stack

`docker-compose.yml` runs Zookeeper + Kafka + Kafka UI at http://localhost:8081.

---

## Reflection

1. What happens if a consumer crashes before committing offset?
2. Why use `group_id`?

---

## Up next

[Lesson 3: Stream processing →](03-stream-processing.md)
