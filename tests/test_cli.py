import os
import csv
import subprocess
import sys
from pathlib import Path


def test_cli_accepts_filenames_and_writes_csv(tmp_path: Path):
    input_file = tmp_path / "matches.csv"
    output_file = tmp_path / "table.csv"
    input_file.write_text(
        "home_team,away_team,home_goals,away_goals\nArsenal,Chelsea,2,1\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, "-m", "football_standings.cli", str(input_file), str(output_file)],
        check=False,
        env={**os.environ, "PYTHONPATH": "src"},
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    with output_file.open(newline="", encoding="utf-8") as handle:
        assert next(csv.DictReader(handle))["team"] == "Arsenal"


def test_cli_reports_csv_errors_without_traceback(tmp_path: Path):
    input_file = tmp_path / "bad_matches.csv"
    input_file.write_text(
        "home_team,away_team,home_goals,away_goals\nArsenal,Chelsea,two,1\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, "-m", "football_standings.cli", str(input_file)],
        check=False,
        env={**os.environ, "PYTHONPATH": "src"},
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "football-standings: line 2: home_goals must be an integer" in result.stderr
    assert "Traceback" not in result.stderr
