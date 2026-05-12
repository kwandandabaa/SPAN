# CLAUDE.md

## Project goal

Build and maintain a production-ready Python CLI that calculates football league standings from CSV match results. The target demonstration is the English First Division table after week 10 of the 1974/75 season.

## Domain rules

- Default to English First Division 1974/75 rules:
  - 2 points for a win.
  - 1 point for a draw.
  - 0 points for a loss.
  - Sort by points, then historical goal average (`goals_for / goals_against`), not modern goal difference.
- Preserve deterministic output by using goals scored and then team name as final tie-breakers.
- Treat postponed fixtures as absent until their actual played date.

## Engineering guidelines

- Use Python standard library for application code unless a dependency is clearly justified.
- Keep input and output as text CSV.
- Support both stdin/stdout and filename arguments.
- Validate CSV input with actionable error messages.
- Keep core calculation logic independent from CLI and file I/O.
- Add or update automated tests for every behavior change.

## Useful commands

```bash
PYTHONPATH=src python -m football_standings.cli data/english_first_division_1974_75_week10_results.csv
python -m pytest
```
