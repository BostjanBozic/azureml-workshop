import os
from azureml.core.model import InferenceConfig, Model
from azureml.core import Run, Environment
from azureml.core.webservice import AciWebservice

run = Run.get_context()
ws = run.experiment.workspace

run.log("Deploy start time", str(datetime.datetime.now()))

model = Model(
  workspace=ws,
  name="diabetes-logistic-regression",
)

env = Environment.from_conda_specification(
  name="diabetes-logistic-regression",
  file_path="./conda.yml",
)

inference_config = InferenceConfig(
  source_directory="./",
  entry_script="score.py",
  environment=env,
)

deployment_config = AciWebservice.deploy_configuration(
  cpu_cores=1,
  memory_gb=1,
)

endpoint = Model.deploy(
  workspace=ws,
  name="diabetes-logistic-regression",
  models=[model],
  inference_config=inference_config,
  deployment_config=deployment_config,
  overwrite=True,
)

run.log("Deploy end time", str(datetime.datetime.now()))

run.complete()
