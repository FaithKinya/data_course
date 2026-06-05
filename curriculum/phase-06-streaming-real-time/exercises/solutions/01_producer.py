"""Solution: Exercise 1 — Kafka clickstream producer."""

import json
from datetime import datetime, timedelta, timezone

from kafka import KafkaProducer

BOOTSTRAP = ["localhost:9092"]
TOPIC = "shopstream.clicks"
PAGES = ["/home", "/products/101", "/cart"]


def main() -> None:
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    base = datetime(2024, 1, 20, 10, 0, 0, tzinfo=timezone.utc)
    for i in range(20):
        event = {
            "event": "page_view",
            "user_id": (i % 5) + 1,
            "page": PAGES[i % len(PAGES)],
            "ts": (base + timedelta(seconds=i)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        producer.send(TOPIC, event)
        print("sent", event)

    producer.flush()
    print(f"Published 20 events to {TOPIC}")


if __name__ == "__main__":
    main()
