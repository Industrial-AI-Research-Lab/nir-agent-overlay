# Experiments in MLflow

- Every run: `mlflow.set_tracking_uri` from the settings, `mlflow.set_experiment("<repository>")`
  or `"<repository>/<task>"`, run name `<branch>-<short-description>`.
- Tags on every run: `stage` (baseline, ablation, final), `dataset`, `model_family`, `pr` (number);
  one paragraph of notes.
- Log params and final metrics explicitly; log the config file as an artifact; call
  `mlflow.autolog()` before training when the framework supports it.
- Run from a committed checkout so the commit is recorded; runs from notebooks get no commit.
- Local store by default, `sqlite:///mlflow.db`, with `mlruns/` and `mlartifacts/` ignored.
  A shared server only when the supervisor gives its address.
- A results row is commit, config path, seed, run id, metrics. Never write a number into a table
  or a PR without the run id behind it.
