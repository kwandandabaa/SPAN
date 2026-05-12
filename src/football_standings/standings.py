"""Core football standings calculations."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Match:
    """A completed football match result."""

    home_team: str
    away_team: str
    home_goals: int
    away_goals: int


@dataclass
class TeamRecord:
    """Accumulated table record for one team."""

    team: str
    played: int = 0
    wins: int = 0
    draws: int = 0
    losses: int = 0
    goals_for: int = 0
    goals_against: int = 0
    points: int = 0

    @property
    def goal_average(self) -> Decimal | None:
        """Return historical goal average (GF / GA), or None when GA is zero."""

        if self.goals_against == 0:
            return None
        return Decimal(self.goals_for) / Decimal(self.goals_against)

    def record_result(self, goals_for: int, goals_against: int, points_for_win: int) -> None:
        self.played += 1
        self.goals_for += goals_for
        self.goals_against += goals_against
        if goals_for > goals_against:
            self.wins += 1
            self.points += points_for_win
        elif goals_for == goals_against:
            self.draws += 1
            self.points += 1
        else:
            self.losses += 1


def calculate_standings(matches: list[Match], points_for_win: int = 2) -> list[TeamRecord]:
    """Calculate and sort a league table from completed matches."""

    records: dict[str, TeamRecord] = {}
    for match in matches:
        home = records.setdefault(match.home_team, TeamRecord(match.home_team))
        away = records.setdefault(match.away_team, TeamRecord(match.away_team))
        home.record_result(match.home_goals, match.away_goals, points_for_win)
        away.record_result(match.away_goals, match.home_goals, points_for_win)

    return sorted(records.values(), key=_sort_key)


def _sort_key(record: TeamRecord) -> tuple[int, Decimal, int, str]:
    # English First Division 1974/75 sorted by points, then goal average.
    # Use a very large value for a side that has not conceded.
    goal_average = record.goal_average if record.goal_average is not None else Decimal("Infinity")
    return (-record.points, -goal_average, -record.goals_for, record.team.casefold())


def format_goal_average(record: TeamRecord, places: int = 3) -> str:
    """Format goal average for CSV output."""

    goal_average = record.goal_average
    if record.goal_average is None:
        return "inf"
    quant = Decimal(10) ** -places
    return str(goal_average.quantize(quant))
