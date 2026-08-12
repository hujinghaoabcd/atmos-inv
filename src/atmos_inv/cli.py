"""Lightweight repository utilities.

Production scientific commands will be added only after their data contracts and
validation protocols are frozen. This CLI is intentionally conservative.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path


REQUIRED_ROOTS = ("ATMOSINV_DATA_ROOT", "ATMOSINV_SCRATCH_ROOT", "ATMOSINV_RUN_ROOT")


def _doctor() -> int:
    print("AtmosInv bootstrap doctor")
    missing = []
    for name in REQUIRED_ROOTS:
        value = os.environ.get(name)
        if not value:
            missing.append(name)
            print(f"[missing] {name}")
        else:
            path = Path(value).expanduser()
            print(f"[set]     {name}={path}")
    if missing:
        print("\nLarge-scale workflows remain disabled until storage roots are configured.")
        return 1
    print("\nStorage path contract is configured.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="AtmosInv repository utilities")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("doctor", help="check external storage environment variables")
    args = parser.parse_args()
    if args.command == "doctor":
        raise SystemExit(_doctor())
    parser.print_help()


if __name__ == "__main__":
    main()
