"""CSV input and output helpers for football standings."""

from __future__ import annotations

import csv
from collections.abc import Iterable
from typing import TextIO

from .standings import Match, TeamRecord, format_goal_average

INPUT_COLUMNS = ("home_team", "away_team", "home_goals", "away_goals")
OUTPUT_COLUMNS = (
    "position",
    "team",
    "played",
    "wins",
    "draws",
    "losses",
    "goals_for",
    "goals_against",
    "goal_average",
    "points",
)


class CsvFormatError(ValueError):
    """Raised when input CSV cannot be parsed as match results."""


def read_matches(handle: TextIO) -> list[Match]:
    """Read match results from CSV with a header row."""

    reader = csv.DictReader(handle)
    if reader.fieldnames is None:
        return []
    missing = [column for column in INPUT_COLUMNS if column not in reader.fieldnames]
    if missing:
        raise CsvFormatError(f"missing required CSV columns: {', '.join(missing)}")

    matches: list[Match] = []
    for line_number, row in enumerate(reader, start=2):
        try:
            home_team = _required_text(row, "home_team")
            away_team = _required_text(row, "away_team")
            home_goals = _required_non_negative_int(row, "home_goals")
            away_goals = _required_non_negative_int(row, "away_goals")
        except CsvFormatError as exc:
            raise CsvFormatError(f"line {line_number}: {exc}") from exc
        if home_team == away_team:
            raise CsvFormatError(f"line {line_number}: a team cannot play itself")
        matches.append(Match(home_team, away_team, home_goals, away_goals))
    return matches


def write_standings(handle: TextIO, records: Iterable[TeamRecord]) -> None:
    """Write a league table to CSV."""

    writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
    writer.writeheader()
    for position, record in enumerate(records, start=1):
        writer.writerow(
            {
                "position": position,
                "team": record.team,
                "played": record.played,
                "wins": record.wins,
                "draws": record.draws,
                "losses": record.losses,
                "goals_for": record.goals_for,
                "goals_against": record.goals_against,
                "goal_average": format_goal_average(record),
                "points": record.points,
            }
        )


def _required_text(row: dict[str, str | None], column: str) -> str:
    value = (row.get(column) or "").strip()
    if not value:
        raise CsvFormatError(f"{column} is required")
    return value


def _required_non_negative_int(row: dict[str, str | None], column: str) -> int:
    raw_value = (row.get(column) or "").strip()
    if not raw_value:
        raise CsvFormatError(f"{column} is required")
    try:
        value = int(raw_value)
    except ValueError as exc:
        raise CsvFormatError(f"{column} must be an integer") from exc
    if value < 0:
        raise CsvFormatError(f"{column} must be non-negative")
    return value
