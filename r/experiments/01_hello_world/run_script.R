library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../../")

exp <- experiment(
  workspace = ws,
  name = "hello-world-r"
)
env <- r_environment(
  name = "r-environment",
  custom_docker_image = "<acr_repository_name>.azurecr.io/r-azureml:latest" # nolint
)

config <- estimator(
  source_directory = "./src",
  entry_script = "hello.R",
  compute_target = "example-cluster",
  environment = env
)

run <- submit_experiment(
  experiment = exp,
  config = config
)
