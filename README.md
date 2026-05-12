# Football Standings Calculator

A production-ready Python command-line application that calculates a football (soccer) league table from match-result CSV input.

The included sample data calculates the English First Division table after the 10th week / round of the 1974/75 season. That season used the historical English league rules of **2 points for a win, 1 for a draw, and ranking tied teams by goal average** (`goals_for / goals_against`) rather than goal difference.

## Requirements

- Python 3.10+
- `pytest` for running the test suite

The application itself uses only the Python standard library.

## Input CSV format

Input files must have a header row with these columns:

```csv
home_team,away_team,home_goals,away_goals
Arsenal,Chelsea,2,1
```

Additional columns are ignored, so richer source files can be used as long as the required columns are present.

## Output CSV format

The program writes a conventional table with these columns:

```csv
position,team,played,wins,draws,losses,goals_for,goals_against,goal_average,points
```

Goal average is emitted to three decimal places. A team with zero goals conceded is emitted as `inf`.

## Run from source

Use stdin/stdout:

```bash
PYTHONPATH=src python -m football_standings.cli < data/english_first_division_1974_75_week10_results.csv
```

Use filenames:

```bash
PYTHONPATH=src python -m football_standings.cli \
  data/english_first_division_1974_75_week10_results.csv \
  data/english_first_division_1974_75_week10_table.csv
```

## Install as a command

```bash
python -m pip install -e .
football-standings data/english_first_division_1974_75_week10_results.csv
```

## Run tests

```bash
python -m pytest
```

## Data notes

The sample result file contains completed English First Division matches through 28 September 1974, corresponding to the 10th listed round/week in the 1974/75 fixture list. Matches listed in earlier rounds but postponed until December 1974 or April 1975 are intentionally excluded because they had not been played by the end of week 10.

Sources consulted while preparing the sample data and historical rules:

- BDFutbol `First Division 1974-75` result list for rounds 1-10.
- Historical Lineups `1974-75 Week 11` PDF for a cross-check of the following week's table and confirmation that the table used `P W D L Pts GF GA GR`.
- RSSSF / season summaries for final-table convention and season context.

## Repository AI collaboration artefacts

This repository includes the required AI collaboration artefacts:

- `CLAUDE.md` — project instructions for AI assistants.
- `.claude/` — session-data placeholder and notes.
- `ai/` — exported conversation-history equivalent for this Codex session.
- `AI_REFLECTION.md` — reflection on AI collaboration decisions.
