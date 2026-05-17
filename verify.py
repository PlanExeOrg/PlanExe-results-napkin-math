#!/usr/bin/env python3
"""
Verify that every plan dir under ``snapshot/<n>/`` contains a ``meta.json``.

Walks each numbered snapshot directory and reports any plan dirs missing the
``meta.json`` sidecar. Exits non-zero if anything is missing.

Usage::

    python3 verify.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SNAPSHOT_ROOT = REPO_ROOT / "snapshot"


def main() -> int:
    if not SNAPSHOT_ROOT.is_dir():
        print(f"Missing snapshot dir: {SNAPSHOT_ROOT}", file=sys.stderr)
        return 1

    snapshots = sorted(p for p in SNAPSHOT_ROOT.iterdir() if p.is_dir())
    if not snapshots:
        print(f"No snapshot dirs found under {SNAPSHOT_ROOT}", file=sys.stderr)
        return 1

    missing: list[Path] = []
    checked = 0

    for snapshot in snapshots:
        plan_dirs = sorted(p for p in snapshot.iterdir() if p.is_dir())
        for plan_dir in plan_dirs:
            checked += 1
            if not (plan_dir / "meta.json").is_file():
                missing.append(plan_dir.relative_to(REPO_ROOT))

    if missing:
        print(f"Missing meta.json in {len(missing)} of {checked} plan dirs:")
        for path in missing:
            print(f"  {path}")
        return 1

    print(f"OK: all {checked} plan dirs have meta.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
