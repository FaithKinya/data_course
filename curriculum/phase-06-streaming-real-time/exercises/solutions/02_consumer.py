"""Solution: Exercise 2 — Per-page aggregate consumer."""

import json
from pathlib import Path

from kafka import KafkaConsumer

BOOTSTRAP = ["localhost:9092"]
TOPIC = "shopstream.clicks"
GROUP = "ex02-page-counts"
OUTPUT = Path(__file__).resolve().parent.parent / "my_work/output/page_counts.json"


def main() -> None:
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        auto_offset_reset="earliest",
        group_id=GROUP,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        consumer_timeout_ms=5000,
    )

    counts: dict[str, int] = {}
    processed = 0
    for msg in consumer:
        page = msg.value["page"]
        counts[page] = counts.get(page, 0) + 1
        print(counts)
        processed += 1
        if processed >= 20:
            break

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(counts, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
