"""Solution: Exercise 2 — Structured JSON pipeline logging."""

import argparse
import json
import logging
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUTPUT = Path(__file__).resolve().parent.parent / "my_work/output/run_log.jsonl"


class JsonFormatter(logging.Formatter):
    def __init__(self, run_id: str):
        super().__init__()
        self.run_id = run_id

    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "run_id": self.run_id,
            "msg": record.getMessage(),
        }
        for key in ("stage", "duration_ms", "row_count", "status"):
            if hasattr(record, key):
                payload[key] = getattr(record, key)
        return json.dumps(payload)


def log_stage(log: logging.Logger, stage: str, row_count: int, fail: bool = False) -> None:
    start = time.perf_counter()
    time.sleep(0.05)
    if fail:
        raise ValueError(f"{stage} failed")
    duration_ms = round((time.perf_counter() - start) * 1000, 2)
    log.info(
        f"{stage}_complete",
        extra={"stage": stage, "duration_ms": duration_ms, "row_count": row_count},
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fail-validate", action="store_true")
    args = parser.parse_args()

    run_id = str(uuid.uuid4())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    log = logging.getLogger("shopstream")
    log.handlers.clear()
    log.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(JsonFormatter(run_id))
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler(OUTPUT, encoding="utf-8")
    file_handler.setFormatter(JsonFormatter(run_id))
    log.addHandler(file_handler)

    status = "success"
    try:
        log_stage(log, "extract", row_count=14)
        log_stage(log, "validate", row_count=14, fail=args.fail_validate)
        log_stage(log, "load", row_count=14)
    except Exception as exc:
        status = "failed"
        log.error(str(exc), extra={"stage": "validate", "status": status})
        raise SystemExit(1) from exc
    finally:
        log.info("pipeline_finished", extra={"status": status})


if __name__ == "__main__":
    main()
