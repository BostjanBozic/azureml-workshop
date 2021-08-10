from azureml.core import Environment, Model, Workspace
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice

ws = Workspace.from_config(path="../../")
model = Model(
  workspace=ws,
  name="diabetes-sklearn",
  version=1,
)

env = Environment.from_conda_specification(
  name="diabetes-sklearn-aci",
  file_path="./conda.yml",
)

# env.register(workspace=ws)
# env.build(workspace=ws)

config = InferenceConfig(
  source_directory="./src",
  entry_script="score.py",
  environment=env,
)

aci_config = AciWebservice.deploy_configuration(
  cpu_cores=1,
  memory_gb=2,
)

endpoint = Model.deploy(
  workspace=ws,
  name="diabetes-aci-deploy",
  models=[model],
  inference_config=config,
  deployment_config=aci_config,
  overwrite=True,
)

endpoint.wait_for_deployment(show_output=True)
print(endpoint.state)
