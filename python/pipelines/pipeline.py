from azureml.core import Dataset, Datastore, Environment, Experiment, RunConfiguration, Workspace
from azureml.core.compute import AmlCompute
from azureml.pipeline.steps import PythonScriptStep
from azureml.pipeline.core import PipelineData, Pipeline


ws = Workspace.from_config(path="../../")
env = Environment.from_conda_specification("diabetes-environment", "./conda.yml")
compute = AmlCompute(
  workspace=ws,
  name="rimi-cluster",
)

run_config = RunConfiguration()
run_config.target = compute
run_config.environment = env

datastore = Datastore.get(
  workspace=ws,
  datastore_name="rimiblobstorage",
)

datastore.upload_files(
  files=["./data/pima-indians-diabetes.csv"],
  target_path="pipelines-data",
  overwrite=True,
)

diabetes_data = Dataset.Tabular.from_delimited_files(path=datastore.path("./pipelines-data/pima-indians-diabetes.csv"))
diabetes_data.register(
  workspace=ws,
  name="diabetes-data",
  create_new_version=True,
)

raw_data = diabetes_data.as_named_input("raw_data")
train_data = PipelineData("train_data", datastore=datastore).as_dataset()
test_data = PipelineData("test_data", datastore=datastore).as_dataset()
scaler_file = PipelineData("scaler_file", datastore=datastore)
model_file = PipelineData("model_file", datastore=datastore)
register_deploy_dep = PipelineData("dependency", datastore=datastore)


step1 = PythonScriptStep(
  name="Data preparation",
  source_directory="./prep",
  script_name="prep.py",
  arguments=[
    "--train", train_data,
    "--test", test_data,
    "--scaler", scaler_file,
  ],
  compute_target=compute,
  runconfig=run_config,
  allow_reuse=False,
  inputs=[raw_data],
  outputs=[
    train_data,
    test_data,
    scaler_file,
  ],
)

step2 = PythonScriptStep(
  name="Train the model",
  source_directory="./train",
  script_name="train.py",
  arguments=[
    "--train", train_data,
    "--test", test_data,
    "--model", model_file,
  ],
  compute_target=compute,
  runconfig=run_config,
  allow_reuse=False,
  inputs=[
    train_data,
    test_data,
  ],
  outputs=[model_file],
)

step3 = PythonScriptStep(
  name="Register the model",
  source_directory="./register",
  script_name="register.py",
  arguments=["--model", model_file],
  inputs=[model_file],
  outputs=[register_deploy_dep],
  compute_target=compute,
  runconfig=run_config,
  allow_reuse=True,
)

step4 = PythonScriptStep(
  name="Deploy the model",
  source_directory="./deploy",
  script_name="deploy.py",
  inputs=[register_deploy_dep],
  compute_target=compute,
  runconfig=run_config,
  allow_reuse=True,
)

pipeline_steps = [step1]

pipeline = Pipeline(workspace=ws, steps=pipeline_steps)
pipeline_run = Experiment(ws, "diabetes-pipeline").submit(pipeline, regenerate_outputs=False)
