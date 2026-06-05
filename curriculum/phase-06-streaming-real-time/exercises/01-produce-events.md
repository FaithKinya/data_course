# Exercise 1: Produce Events

**Time:** ~45 minutes

---

## Goal

Publish simulated ShopStream clickstream events to Kafka.

---

## Prerequisites

```bash
cd curriculum/phase-06-streaming-real-time
docker compose up -d
pip install kafka-python
```

---

## Tasks

Create `exercises/my_work/01_producer.py`:

1. Connect to `localhost:9092`
2. Topic: `shopstream.clicks` (auto-created)
3. Publish 20 events with JSON schema:

```json
{
  "event": "page_view",
  "user_id": 1,
  "page": "/products/101",
  "ts": "2024-01-20T10:00:01Z"
}
```

4. Vary `user_id` (1–5), `page` (`/home`, `/products/101`, `/cart`), increment `ts` by 1 second
5. `flush()` and print confirmation

---

## Verify

- Kafka UI at http://localhost:8081 shows topic and messages
- Compare with [solutions/01_producer.py](solutions/01_producer.py)

**Next:** [Exercise 2: Consume & aggregate](02-consume-aggregate.md)
