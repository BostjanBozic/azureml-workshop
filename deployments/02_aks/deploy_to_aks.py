from azureml.core import Environment, Model, Workspace
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AksWebservice

ws = Workspace.from_config(path="../../")
model = Model(
  workspace=ws,
  name="diabetes-sklearn",
  version=1,
)

env = Environment.from_conda_specification(
  name="diabetes-sklearn-aks",
  file_path="./conda.yml",
)

config = InferenceConfig(
  source_directory="./src",
  entry_script="score.py",
  environment=env,
)

aks_config = AksWebservice.deploy_configuration(
  cpu_cores=1,
  memory_gb=2,
  compute_target_name="rimi-aks-cluster",
  auth_enabled=False,
)

endpoint = Model.deploy(
  workspace=ws,
  name="diabetes-aks-deploy",
  models=[model],
  inference_config=config,
  deployment_config=aks_config,
  overwrite=True,
)

endpoint.wait_for_deployment(show_output=True)
print(endpoint.state)
