# Exercise 3: Windowed Counts

**Time:** ~45 minutes

---

## Goal

Aggregate events into 1-minute tumbling windows per page.

---

## Tasks

Create `exercises/my_work/03_windowed_consumer.py`:

1. Consume from `shopstream.clicks`
2. Bucket `ts` into 1-minute windows (floor seconds)
3. Key: `(window_start, page)` → count
4. Print only when a window key **changes** (new minute detected)
5. Save final state to `exercises/my_work/output/windowed_counts.json`

Tip: use `datetime.fromisoformat` with UTC.

---

## Test data

Re-run producer with `ts` spanning at least 2 distinct minutes (adjust producer timestamps if needed).

---

## Verify

Compare with [solutions/03_windowed_consumer.py](solutions/03_windowed_consumer.py).

**Next:** [Phase project →](../project/README.md)
