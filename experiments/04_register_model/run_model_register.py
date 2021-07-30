from azureml.core import Environment, Experiment, Workspace, ScriptRunConfig
from azureml.core.model import Model

ws = Workspace.from_config(path="../../")

env = Environment.from_conda_specification(
  name="sklearn-iris",
  file_path="./conda.yml"
)

config = ScriptRunConfig(
  source_directory="./src",
  script="train.py",
  compute_target="rimi-cluster",
  environment=env,
  arguments=[
    "--kernel", "linear",
    "--penalty", 2.0,
  ]
)

exp = Experiment(
  workspace=ws,
  name="iris-model-register",
)

run = exp.submit(config=config)
run.wait_for_completion(show_output=True)

# run.download_file(
#   name="outputs/model.joblib",
#   output_file_path="./model/model.joblib"
# )
# 
# model = Model.register(
#   workspace=ws,
#   model_path="./model/model.joblib",
#   model_name="iris-sklearn",
# )

model = run.register_model(
  model_name="iris-sklearn",
  model_path="outputs/model.joblib",
)
