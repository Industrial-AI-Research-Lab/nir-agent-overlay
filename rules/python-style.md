---
paths:
  - "**/*.py"
---
# Python style

- Python >= 3.12; `uv` for environments and running: `uv run ...`, never `pip install`.
- ruff formats and lints, mypy checks types in strict mode on `src` and `tests`; the config lives
  in pyproject.toml. Type every function signature.
- Reusable code lives in `src/<package>/`; notebooks import it, never the other way round.
- Configuration comes from a typed settings class read from the environment; no hard-coded paths,
  endpoints or keys.
- Randomness goes through one seeded generator passed explicitly; no hidden global state.
- Tests in `tests/`, at least one smoke test that runs the main pipeline on a tiny input in seconds.
- A comment explains why, in one to three lines; it never restates the code.
