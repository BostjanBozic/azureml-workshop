library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../../")

exp <- experiment(
  workspace = ws,
  name = "accidents-logistic-regression"
)
env <- r_environment(
  name = "r-environment",
  custom_docker_image = "9054a1a822d04d21a7a5f4e726da20cc.azurecr.io/r-azureml:latest" # nolint
)

config <- estimator(
  source_directory = "./src",
  entry_script = "train.R",
  compute_target = "rimi-cluster",
  environment = env
)

run <- submit_experiment(
  experiment = exp,
  config = config
)

wait_for_run_completion(run, show_output = TRUE)

register_model_from_run(
  run = run,
  model_name = "accidents-logistic",
  model_path = "outputs/model.rds"
)
