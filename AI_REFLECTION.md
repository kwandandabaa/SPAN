# AI Collaboration Reflection

The most important collaboration decision was clarifying what “10th week” should mean for a historical football table. A naive implementation could have loaded every fixture assigned to a nominal round, including matches that were postponed and played months later. I used the assistant to cross-check historical fixture listings and then made the product decision to include only matches actually completed by 28 September 1974, while documenting that assumption in the README.

Another point where the AI workflow needed correction was around the ranking rule. Modern football tables normally use goal difference, but the 1974/75 English First Division used goal average. I explicitly steered the implementation toward goal average and added tests that would fail if a future change accidentally sorted by goal difference.

The assistant was most useful for accelerating implementation of scaffolding the CLI,validation scenarios, and repository documentation. I kept the final design deliberately small: standard-library Python, separated modules for calculation and CSV I/O, and a fixture CSV that can be inspected or replaced without changing code.
