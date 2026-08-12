#!/usr/bin/env python
"""Validate the repository skeleton without requiring scientific datasets."""

from pathlib import Path


REQUIRED = [
    "README.md",
    "configs/config.yaml",
    "docs/PROJECT_OVERVIEW.md",
    "docs/DATA_CATALOG.md",
    "docs/EXPERIMENT_MATRIX.md",
    "experiments/registry.csv",
    "workflows/Snakefile",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED if not (root / path).exists()]
    if missing:
        for path in missing:
            print(f"missing: {path}")
        return 1
    print("AtmosInv repository skeleton: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
