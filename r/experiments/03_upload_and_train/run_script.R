library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../../")

datastore <- get_datastore(workspace = ws, datastore_name = "blob_storage")
upload_files_to_datastore(
  datastore = datastore,
  files = list("./data/iris.csv"),
  target_path = "irisdata"
)

exp <- experiment(
  workspace = ws,
  name = "iris-from-datastore"
)
env <- r_environment(
  name = "r-environment",
  custom_docker_image = "<acr_repository_name>.azurecr.io/r-azureml:latest" # nolint
)

config <- estimator(
  source_directory = "./src",
  entry_script = "train.R",
  compute_target = "example-cluster",
  environment = env,
  script_params = list("--data_folder" = datastore$path("irisdata"))
)

run <- submit_experiment(
  experiment = exp,
  config = config
)
