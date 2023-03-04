library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../../")

exp <- experiment(
  workspace = ws,
  name = "iris-register-model"
)
env <- r_environment(
  name = "r-environment",
  custom_docker_image = "<acr_repository_name>.azurecr.io/r-azureml:latest" # nolint
)

config <- estimator(
  source_directory = "./src",
  entry_script = "train.R",
  compute_target = "example-cluster",
  environment = env
)

run <- submit_experiment(
  experiment = exp,
  config = config
)
wait_for_run_completion(run, show_output = TRUE)

download_file_from_run(
  run = run,
  name = "outputs/model.rds",
  output_file_path = "./model/model.rds"
)
register_model(
  workspace = ws,
  model_path = "./model/model.rds",
  model_name = "iris-R-local",
  description = "Model downloaded locally and then registered."
)

register_model_from_run(
  run = run,
  model_name = "iris-R-from-run",
  model_path = "outputs/model.rds",
  description = "Model registered from run."
)
