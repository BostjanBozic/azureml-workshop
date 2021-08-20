from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment

ws = Workspace.from_config(path="../../../")

exp = Experiment(
  workspace=ws,
  name="cifar10-experiment",
)

env = ws.environments["AzureML-PyTorch-1.6-CPU"]

exp_config = ScriptRunConfig(
  source_directory="./src",
  script="train.py",
  compute_target="rimi-cluster",
  environment=env,
)

run = exp.submit(config=exp_config)
