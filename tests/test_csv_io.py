import csv
import io

import pytest

from football_standings.csv_io import CsvFormatError, read_matches, write_standings
from football_standings.standings import calculate_standings


def test_reads_input_csv_and_writes_conventional_table_csv():
    source = io.StringIO(
        "home_team,away_team,home_goals,away_goals\n"
        "Arsenal,Chelsea,2,1\n"
        "Chelsea,Everton,0,0\n"
    )

    matches = read_matches(source)
    table_output = io.StringIO()
    write_standings(table_output, calculate_standings(matches))

    table_output.seek(0)
    rows = list(csv.DictReader(table_output))
    assert rows[0] == {
        "position": "1",
        "team": "Arsenal",
        "played": "1",
        "wins": "1",
        "draws": "0",
        "losses": "0",
        "goals_for": "2",
        "goals_against": "1",
        "goal_average": "2.000",
        "points": "2",
    }
    assert rows[1]["team"] == "Everton"
    assert rows[2]["team"] == "Chelsea"


def test_rejects_missing_required_columns():
    with pytest.raises(CsvFormatError, match="missing required CSV columns"):
        read_matches(io.StringIO("team,goals\nArsenal,2\n"))


def test_rejects_negative_scores_with_line_number():
    with pytest.raises(CsvFormatError, match="line 2: home_goals must be non-negative"):
        read_matches(
            io.StringIO("home_team,away_team,home_goals,away_goals\nArsenal,Chelsea,-1,0\n")
        )


def test_rejects_non_integer_scores_with_line_number():
    with pytest.raises(CsvFormatError, match="line 2: home_goals must be an integer"):
        read_matches(
            io.StringIO("home_team,away_team,home_goals,away_goals\nArsenal,Chelsea,two,0\n")
        )


def test_rejects_team_playing_itself():
    with pytest.raises(
        CsvFormatError,
        match="a team cannot play itself",
    ):
        read_matches(
            io.StringIO(
                "home_team,away_team,home_goals,away_goals\n"
                "Arsenal,Arsenal,1,0\n"
            )
        )
