"""Solution: Exercise 3 — 1-minute tumbling window counts."""

import json
from datetime import datetime, timezone
from pathlib import Path

from kafka import KafkaConsumer

BOOTSTRAP = ["localhost:9092"]
TOPIC = "shopstream.clicks"
GROUP = "ex03-windowed-counts"
OUTPUT = Path(__file__).resolve().parent.parent / "my_work/output/windowed_counts.json"


def floor_minute(ts_iso: str) -> str:
    ts = datetime.fromisoformat(ts_iso.replace("Z", "+00:00"))
    floored = ts.replace(second=0, microsecond=0)
    return floored.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


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
    last_window: str | None = None
    processed = 0

    for msg in consumer:
        page = msg.value["page"]
        window = floor_minute(msg.value["ts"])
        key = f"{window}|{page}"

        if last_window and window != last_window:
            print(f"--- window closed: {last_window} ---")
            snapshot = {k: v for k, v in counts.items() if k.startswith(last_window)}
            print(snapshot)

        counts[key] = counts.get(key, 0) + 1
        last_window = window
        processed += 1
        if processed >= 20:
            break

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(counts, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
