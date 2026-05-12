# Football Standings Calculator


A Python command-line application that calculates a football league standings table from CSV match results.
The included sample dataset calculates the English First Division standings after the 10th round/week of the 1974/75 season using the historical rules in effect at the time:
* 2 points for a win
* 1 point for a draw
* teams ranked by goal average (goals_for / goals_against) rather than goal difference
The project was intentionally kept lightweight and dependency-minimal. The application itself uses only the Python standard library, with pytest used for automated testing.

## Requirements

* Python 3.10+
* pip

Optional development dependencies (including pytest) can be installed using the dev extras group.

## Project Structure

```text
.
├── data/                      # Sample input and generated output CSV files
├── src/football_standings/    # Application source code
├── tests/                     # Automated test suite
├── .claude/                   # AI collaboration notes/session artefacts
├── ai/                        # Exported AI interaction history
├── AI_REFLECTION.md           # Reflection on AI-assisted development
├── CLAUDE.md                  # AI collaboration instructions/context
├── README.md
└── pyproject.toml
```

## Input CSV format

Input files must contain the following columns:

home_team,away_team,home_goals,away_goals

Arsenal,Chelsea,2,1


Additional columns are ignored, allowing richer historical datasets to be used as long as the required columns are present.
Each row represents a completed match.

## Output CSV format

The generated standings table contains the following columns:

```csv
position,team,played,wins,draws,losses,goals_for,goals_against,goal_average,points
```

Goal average is emitted to three decimal places. A team with zero goals conceded is emitted as `inf`.


## Setup

Ensure `python` resolves to Python 3.10 or newer.

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the project and development dependencies:

```bash
pip install -e ".[dev]"
```

## Running the Application

### Using filenames

```bash
football-standings \
  data/english_first_division_1974_75_week10_results.csv \
  data/english_first_division_1974_75_week10_table.csv
```

### Using stdin/stdout

```bash
PYTHONPATH=src python -m football_standings.cli \
  < data/english_first_division_1974_75_week10_results.csv
```

## Running Tests

Run the automated test suite:

```bash
pytest
```

The test suite validates:
- standings calculation
- points allocation
- goal-average ranking behaviour
- CSV parsing/writing
- CLI execution flow
 
## Historical Data Notes
The sample input file contains completed English First Division matches through 28 September 1974, corresponding to the 10th listed round/week of the 1974/75 fixture schedule.
Matches originally scheduled in earlier rounds but postponed until later in the season were intentionally excluded, since they had not yet been played by the end of week 10.
Historical rules and fixtures were cross-checked using publicly available historical football references and season summaries, including:
* BDFutbol season results
* Historical Lineups weekly tables
* RSSSF season summaries
 
⸻
 
## Engineering Notes
The implementation intentionally separates:
* CSV input/output handling
* standings calculation logic
* command-line orchestration
The application was designed to remain small and readable rather than heavily abstracted or framework-driven.

The focus of the exercise was correctness, reproducibility, testability, clear handling of the historical league rules, and deterministic ordering of fully tied teams.

Operational metadata such as generation timestamps or processing identifiers were intentionally excluded from the output schema to keep the standings table deterministic and focused on domain data. In a production environment, these concerns would typically be handled through orchestration metadata, logging, or partitioned output conventions.

The implementation intentionally avoids external runtime dependencies because the problem scope could be solved cleanly using the Python standard library.

The CSV parser is intentionally strict about required columns and score validity, while remaining tolerant of additional columns to support richer historical datasets without changing the core application contract.

Sources consulted while preparing the sample data and historical rules:

- BDFutbol `First Division 1974-75` result list for rounds 1-10.
- Historical Lineups `1974-75 Week 11` PDF for a cross-check of the following week's table and confirmation that the table used `P W D L Pts GF GA GR`.
- RSSSF / season summaries for final-table convention and season context.

## Repository AI collaboration artefacts

This repository includes the required AI collaboration artefacts:

- `CLAUDE.md` — project instructions for AI assistants.
- `.claude/` — session-data placeholder and notes.
- `ai/` — exported conversation history and workflow summary for this Codex session.
  - `ai/codex-conversation-history.md` contains the transcript-style conversation history.
  - `ai/codex-session-export.md` contains a concise workflow summary.
- `AI_REFLECTION.md` — reflection on AI collaboration decisions.

