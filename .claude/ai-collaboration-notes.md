This directory contains AI collaboration notes and supporting artefacts produced during development of the football standings calculator.

The project was primarily developed using OpenAI Codex / GPT-5.5-assisted workflows rather than Claude Code specifically. This directory provides the equivalent session context and implementation notes requested in the coding challenge brief.

Key development decisions and outcomes:

- Selected Python to prioritise readability, portability, and rapid iteration.
- Kept the implementation dependency-minimal, using only the Python standard library for the application itself.
- Implemented the historical English First Division 1974/75 rules:
  - 2 points for a win
  - goal average as the ranking tiebreaker
- Separated CSV handling, standings calculation, and CLI orchestration into distinct modules.
- Added automated pytest coverage for:
  - standings calculation
  - CSV parsing/writing
  - CLI execution flow
  - historical ranking behaviour
- Validated the repository in a clean local Codex environment to confirm:
  - installation
  - CLI execution
  - generated output
  - passing tests

Additional AI interaction history and exported collaboration artefacts are included in the `ai/` directory.
