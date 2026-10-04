#!/usr/bin/env python3
"""Render GitHub's profile copy from the canonical root README."""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
expected = (root / 'README.md').read_text().replace('(assets/', '(../assets/')
target = root / 'profile/README.md'
if args.check:
    if target.read_text() != expected:
        raise SystemExit('Run python scripts/sync-profile.py before publishing.')
else:
    target.write_text(expected)
