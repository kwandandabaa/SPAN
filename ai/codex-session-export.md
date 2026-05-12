# AI Conversation Export

## User request summary

Build a lightweight, production-ready Python command-line application that calculates football league standings from CSV input/output.

The solution should:
- use the historical English First Division 1974/75 rules
- prioritise readability and separation of concerns
- remain dependency-minimal
- include automated tests
- include clear setup/run documentation
- generate standings for the league after week 10 of the 1974/75 season

During development, explore:
- sensible project structure
- historical ranking edge cases
- CSV validation behaviour
- reproducibility of the repository setup

## Development workflow summary

1. Reviewed the initial repository structure and clarified the historical league requirements.
2. Cross-checked the 1974/75 English First Division scoring and ranking rules, including the use of goal average rather than goal difference.
3. The implementation evolved into a small Python package under `src/football_standings` with separate modules for:
   - standings calculation
   - CSV parsing/writing
   - CLI execution
4. Added sample historical input/output CSV files under `data/`.
5. Added pytest coverage for:
   - standings calculation
   - CSV validation
   - CLI execution
   - historical ranking behaviour
6. Refined repository documentation and AI collaboration artefacts.
7. Validated the repository in a clean local Codex environment to confirm installation, test execution, and CLI behaviour.

## Key human/AI decision points

- Use historical 1974/75 rules:
  - 2 points for a win
  - goal average as the ranking tiebreaker
- Exclude fixtures postponed beyond 28 September 1974 from the week-10 dataset.
- Keep the implementation dependency-minimal and rely primarily on the Python standard library.
- Prioritise readability and separation of concerns over heavy abstraction/framework usage.
- Validate the repository in a clean environment before submission to confirm reproducibility.
