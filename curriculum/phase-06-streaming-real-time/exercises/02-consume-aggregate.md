# Exercise 2: Consume & Aggregate

**Time:** ~45 minutes

---

## Goal

Consume click events and maintain per-page view counts.

---

## Tasks

Create `exercises/my_work/02_consumer.py`:

1. Consumer group: `ex02-page-counts`
2. Subscribe to `shopstream.clicks`, `auto_offset_reset="earliest"`
3. Maintain `dict[page, count]` — print on every update
4. Stop after 20 messages (or Ctrl+C)
5. Write final counts to `exercises/my_work/output/page_counts.json`

Run producer (Exercise 1) first, then consumer.

---

## Verify

Compare with [solutions/02_consumer.py](solutions/02_consumer.py).

**Next:** [Exercise 3: Windowed counts](03-windowed-counts.md)
