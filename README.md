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
Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate
Install the project and development dependencies:
pip install -e ".[dev]"
 
⸻
 
## Running the Application
#### Using filenames:

football-standings \
  data/english_first_division_1974_75_week10_results.csv \
  data/english_first_division_1974_75_week10_table.csv

#### Using stdin/stdout:

PYTHONPATH=src python -m football_standings.cli \
  < data/english_first_division_1974_75_week10_results.csv
 
⸻
 
## Running Tests
#### pytest

The test suite validates:
* standings calculation
* points allocation
* goal-average ranking behaviour
* CSV parsing/writing
* CLI execution flow
 
⸻
 
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
 
⸻
 
## AI Collaboration
This repository was developed using AI-assisted tooling, primarily OpenAI Codex.
AI assistance was used for:
* implementation scaffolding
* iteration on project structure
* validation of historical-rule edge cases
* test generation/refinement
* documentation refinement
Architectural decisions, historical-rule verification, validation behaviour, and final implementation decisions were reviewed and adjusted manually during development.
The repository includes the required collaboration artefacts:
* CLAUDE.md
* .claude/
* ai/ (includes `ai/codex-session-export.md` and `ai/codex-conversation-history.md`)
* AI_REFLECTION.md
