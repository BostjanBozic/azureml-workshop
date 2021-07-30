from azureml.core import Workspace, Experiment, ScriptRunConfig

ws = Workspace.from_config(path="../../")

exp = Experiment(
  workspace=ws,
  name="hello-world-experiment",
)

exp_config = ScriptRunConfig(
  source_directory="./src",
  script="hello.py",
  compute_target="rimi-cluster",
)

run = exp.submit(config=exp_config)
