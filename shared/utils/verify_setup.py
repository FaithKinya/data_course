#!/usr/bin/env python3
"""Quick sanity check that the learning environment is ready."""

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATASETS = ROOT / "shared" / "datasets"

REQUIRED_PACKAGES = [
    "pandas",
    "numpy",
    "duckdb",
    "yaml",
]

SAMPLE_FILES = [
    "orders.csv",
    "customers.csv",
    "products.csv",
]


def main() -> int:
    print("Checking Python packages...")
    ok = True
    for pkg in REQUIRED_PACKAGES:
        try:
            importlib.import_module(pkg if pkg != "yaml" else "yaml")
            print(f"  OK  {pkg}")
        except ImportError:
            print(f"  FAIL {pkg} — run: pip install -r requirements.txt")
            ok = False

    print("\nChecking sample datasets...")
    for name in SAMPLE_FILES:
        path = DATASETS / name
        status = "OK" if path.exists() else "MISSING"
        print(f"  {status}  {path}")
        if not path.exists():
            ok = False

    print(f"\nProject root: {ROOT}")
    if ok:
        print("\nSetup looks good. Open curriculum/phase-01-foundations/README.md")
    else:
        print("\nFix issues above before starting Phase 1.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
