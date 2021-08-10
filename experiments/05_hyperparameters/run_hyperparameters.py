from azureml.core import Environment, Experiment, ScriptRunConfig, Workspace
from azureml.train.hyperdrive.runconfig import HyperDriveConfig
from azureml.train.hyperdrive.sampling import RandomParameterSampling
from azureml.train.hyperdrive.parameter_expressions import choice
from azureml.train.hyperdrive.run import PrimaryMetricGoal


ws = Workspace.from_config(path="../../")
env = Environment.from_conda_specification(
  name="hyperparameters",
  file_path="./conda.yml",
)

exp = Experiment(
  workspace=ws,
  name="hyperparameters-tuning",
)

config = ScriptRunConfig(
  source_directory="./src",
  script="train.py",
  compute_target="rimi-cluster",
  environment=env,
  arguments=[
    "--kernel", "linear",
    "--penalty", 0.9,
  ]
)

hyper_sampling = RandomParameterSampling({
    "--kernel": choice('linear', 'poly', 'rbf', 'sigmoid'),
    "--penalty": choice(0.5, 1.0, 1.5),
  }
)

hyper_config = HyperDriveConfig(
  run_config=config,
  hyperparameter_sampling=hyper_sampling,
  primary_metric_name="Accuracy",
  primary_metric_goal=PrimaryMetricGoal.MAXIMIZE,
  max_total_runs=12,
  max_concurrent_runs=4,
)

run = exp.submit(config=hyper_config)
run.wait_for_completion(show_output=True)

best_run = run.get_best_run_by_primary_metric()
model = best_run.register_model(
  model_name="iris-hyperparameters",
  model_path="outputs/model.joblib",
)
