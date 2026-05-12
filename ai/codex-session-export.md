# AI Conversation Export

## User request summary

Build a production-ready Python command-line app that calculates football league standings from CSV input/output, demonstrate it with English First Division week 10 of the 1974/75 season, include automated tests, README, and AI collaboration artefacts.

## Assistant workflow summary

1. Inspected the repository and found only an initial README.
2. Researched historical 1974/75 English First Division results and table rules.
3. Implemented a Python package under `src/football_standings` with separate calculation, CSV I/O, and CLI modules.
4. Created sample input and output CSV files under `data/`.
5. Added pytest tests for core ranking rules, CSV validation, and command-line execution.
6. Added `CLAUDE.md`, `.claude/`, `ai/`, `AI_REFLECTION.md`, and expanded `README.md`.

## Key human/AI decision points

- Use goal average rather than goal difference for 1974/75.
- Exclude fixtures postponed beyond 28 September 1974 from the week-10 sample input.
- Keep dependencies minimal and avoid committing installed packages.
