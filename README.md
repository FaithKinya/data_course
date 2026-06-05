# Learn Data Engineering

A **beginner-to-pro** learning system with clear phases, hands-on exercises, a mini-project in every phase, and two capstone projects at the end.

> **Never done data engineering before?** Start at [Phase 1](curriculum/phase-01-foundations/README.md). Do not skip ahead — each phase builds on the last.

---

## How This Course Works

| Component | What you get |
|-----------|--------------|
| **Lessons** | Short, focused concepts with real-world context |
| **Exercises** | Small drills to lock in skills (15–45 min each) |
| **Phase project** | One guided project per phase — your portfolio grows as you learn |
| **Capstones** | Two end-to-end projects that tie everything together |

### Recommended pace

- **Part-time (5–8 hrs/week):** ~6–9 months
- **Full-time (20+ hrs/week):** ~3–4 months

Copy [PROGRESS.md](PROGRESS.md) into your notes or check boxes directly in that file as you go.

---

## The Roadmap (8 Phases)

```
Phase 1  Foundations          →  Mini-project: Local CSV pipeline
Phase 2  SQL & Modeling       →  Mini-project: Design a star schema
Phase 3  Python Pipelines     →  Mini-project: Batch ETL with pandas
Phase 4  Orchestration        →  Mini-project: Scheduled Airflow DAG
Phase 5  Data Warehousing     →  Mini-project: dbt transformations
Phase 6  Streaming            →  Mini-project: Kafka event pipeline
Phase 7  Cloud DE             →  Mini-project: S3 + warehouse load
Phase 8  Production & Pro     →  Mini-project: Monitored pipeline

Capstone A  E-commerce Analytics Platform   (batch + warehouse + dbt)
Capstone B  Real-Time Event Pipeline        (streaming + cloud)
```

Full detail: [ROADMAP.md](ROADMAP.md)

---

## Where to Start (Day 1)

1. **Set up your environment** — follow [docs/SETUP.md](docs/SETUP.md) (~30 min)
2. **Read Phase 1 overview** — [curriculum/phase-01-foundations/README.md](curriculum/phase-01-foundations/README.md)
3. **Complete Lesson 1** — [What is Data Engineering?](curriculum/phase-01-foundations/lessons/01-what-is-data-engineering.md)
4. **Do Exercise 1** — [curriculum/phase-01-foundations/exercises/01-data-lifecycle-quiz.md](curriculum/phase-01-foundations/exercises/01-data-lifecycle-quiz.md)
5. **Mark progress** in [PROGRESS.md](PROGRESS.md)

---

## Project Structure

```
learn-data-engineering/
├── curriculum/          # 8 phases — lessons, exercises, projects
├── capstones/           # 2 end-to-end portfolio projects
├── shared/              # Sample datasets & helper scripts
├── docs/                # Setup & reference guides
├── tools/               # Progress checker CLI
└── PROGRESS.md          # Your checklist
```

---

## Capstone Projects (The Finish Line)

Complete **both** after Phase 8. They are designed as portfolio pieces you can show in interviews.

| Project | Skills demonstrated | Est. time |
|---------|---------------------|-----------|
| [E-commerce Analytics Platform](capstones/capstone-01-ecommerce-analytics/README.md) | Batch ETL, SQL modeling, dbt, orchestration, data quality | 2–3 weeks |
| [Real-Time Event Pipeline](capstones/capstone-02-real-time-events/README.md) | Streaming, Kafka, cloud storage, monitoring | 2–3 weeks |

You can do them in either order. Capstone A is more approachable if you want a gentler finale.

---

## Getting Unstuck

- Each exercise has a `solutions/` folder — **try on your own first**, then compare
- Phase projects include step-by-step guides and a `CHECKLIST.md`
- Stuck for 30+ minutes? Read the hint in the exercise, then peek at the solution structure (not the full answer)

---

## Quick Links

- [Full roadmap](ROADMAP.md)
- [Environment setup](docs/SETUP.md)
- [Glossary](docs/GLOSSARY.md)
- [Progress tracker](PROGRESS.md)
- [Check progress from terminal](tools/check_progress.py): `python tools/check_progress.py`
