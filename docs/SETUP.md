# Environment Setup

Complete this once before Phase 1. Budget **30–45 minutes**.

---

## 1. Install Python 3.11+

**Windows:** Download from [python.org](https://www.python.org/downloads/) and check **"Add Python to PATH"**.

Verify:

```powershell
python --version
pip --version
```

---

## 2. Create a virtual environment

From the project root:

```powershell
cd C:\Users\Administrator\learn-data-engineering
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 3. Install Git

Download from [git-scm.com](https://git-scm.com/). Verify:

```powershell
git --version
```

---

## 4. Install Docker Desktop (Phases 4 & 6)

Download [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/).

Needed for:
- Apache Airflow (Phase 4)
- Apache Kafka (Phase 6)

You can complete Phases 1–3 without Docker.

---

## 5. Install a SQL client (optional)

- **DBeaver** (free, recommended): [dbeaver.io](https://dbeaver.io/)
- Or use Python + DuckDB from the command line (included in requirements)

---

## 6. Verify your setup

```powershell
python tools/check_progress.py
python shared/utils/verify_setup.py
```

You should see Python packages OK and sample data paths listed.

---

## IDE recommendations

- **Cursor / VS Code** with Python extension
- Jupyter extension for notebook-style exploration in early phases

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `python` not found | Reinstall Python with PATH checked, or use `py` launcher |
| pip SSL errors | `pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt` |
| Docker won't start | Enable WSL 2 / virtualization in BIOS (Windows) |
| Airflow port in use | Change port in `curriculum/phase-04-etl-orchestration/docker-compose.yml` |
