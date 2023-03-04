from azureml.core import Dataset, Workspace, Experiment, ScriptRunConfig, Environment

ws = Workspace.from_config(path="../../../")

exp = Experiment(
  workspace=ws,
  name="cifar10-experiment",
)

env = ws.environments["AzureML-PyTorch-1.6-CPU"]

dataset_blob = Dataset.get_by_name(
  workspace=ws,
  name="cifar10",
)

exp_config = ScriptRunConfig(
  source_directory="./src",
  script="train.py",
  compute_target="example-cluster",
  environment=env,
  arguments=[
    "--data-path", dataset_blob.as_named_input("input").as_mount(),
    "--learning-rate", 0.005,
    "--momentum", 0.95,
  ]
)

run = exp.submit(config=exp_config)
