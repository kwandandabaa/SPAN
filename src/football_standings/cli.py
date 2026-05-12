"""Command-line entry point for the football standings calculator."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import TextIO

from .csv_io import CsvFormatError, read_matches, write_standings
from .standings import calculate_standings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="football-standings",
        description="Calculate a football league table from match-result CSV data.",
    )
    parser.add_argument("input", nargs="?", help="input match CSV file; omit or use '-' for stdin")
    parser.add_argument("output", nargs="?", help="output table CSV file; omit or use '-' for stdout")
    parser.add_argument(
        "--points-for-win",
        type=int,
        default=2,
        choices=range(1, 4),
        metavar="N",
        help="points awarded for a win (default: 2 for English First Division 1974/75)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        with _input_handle(args.input) as input_handle:
            matches = read_matches(input_handle)
        table = calculate_standings(matches, points_for_win=args.points_for_win)
        with _output_handle(args.output) as output_handle:
            write_standings(output_handle, table)
    except (OSError, CsvFormatError) as exc:
        print(f"football-standings: {exc}", file=sys.stderr)
        return 2
    return 0


class _NonClosingTextIO:
    def __init__(self, handle: TextIO) -> None:
        self.handle = handle

    def __enter__(self) -> TextIO:
        return self.handle

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        return None


def _input_handle(filename: str | None):
    if filename in (None, "-"):
        return _NonClosingTextIO(sys.stdin)
    return Path(filename).open("r", newline="", encoding="utf-8")


def _output_handle(filename: str | None):
    if filename in (None, "-"):
        return _NonClosingTextIO(sys.stdout)
    return Path(filename).open("w", newline="", encoding="utf-8")


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
