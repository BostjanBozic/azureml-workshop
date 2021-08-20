from azureml.core import Environment, Experiment, ScriptRunConfig, Workspace

ws = Workspace.from_config(path="../../../")

env = Environment.from_conda_specification(
  name="diabetes-sklearn",
  file_path="./conda.yml",
)

config = ScriptRunConfig(
  source_directory="./src",
  script="train.py",
  compute_target="rimi-cluster",
  environment=env,
)

exp = Experiment(
  workspace=ws,
  name="diabetes-sklearn",
)

run = exp.submit(config=config)
run.wait_for_completion(show_output=True)

model = run.register_model(
  model_name="diabetes-sklearn",
  model_path="outputs/diabetes.pkl"
)
