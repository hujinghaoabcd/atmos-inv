#!/usr/bin/env python
"""Append a planned experiment to experiments/registry.csv.

This utility is intentionally small. It does not execute experiments and does not
replace versioned YAML manifests for formal experiment protocols.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


FIELDS = [
    "experiment_id",
    "family",
    "status",
    "title",
    "config",
    "teacher_version",
    "git_sha",
    "run_id",
    "primary_metric",
    "paper_target",
    "notes",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("experiment_id")
    parser.add_argument("family")
    parser.add_argument("title")
    parser.add_argument("--status", default="planned")
    parser.add_argument("--config", default="")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    registry = root / "experiments" / "registry.csv"
    rows = list(csv.DictReader(registry.open(encoding="utf-8")))
    if any(row["experiment_id"] == args.experiment_id for row in rows):
        raise SystemExit(f"experiment already exists: {args.experiment_id}")

    row = {field: "" for field in FIELDS}
    row.update(
        experiment_id=args.experiment_id,
        family=args.family,
        status=args.status,
        title=args.title,
        config=args.config,
        notes=args.notes,
    )
    with registry.open("a", newline="", encoding="utf-8") as handle:
        csv.DictWriter(handle, fieldnames=FIELDS).writerow(row)
    print(f"registered {args.experiment_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
