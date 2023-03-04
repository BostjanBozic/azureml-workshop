library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../../")

exp <- experiment(
  workspace = ws,
  name = "keras-hyperparameters"
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

hyper_sampling <- random_parameter_sampling(list(
  batch_size = choice(c(16, 32, 64)),
  epochs = choice(c(200, 500)),
  lr = normal(0.0001, 0.005),
  decay = uniform(1e-6, 3e-6)
))

hyperdrive_config <- hyperdrive_config(
  estimator = config,
  hyperparameter_sampling = hyper_sampling,
  primary_metric_name = "Loss",
  primary_metric_goal("MINIMIZE"),
  max_total_runs = 12,
  max_concurrent_runs = 4
)

run <- submit_experiment(
  experiment = exp,
  config = hyperdrive_config
)
wait_for_run_completion(run, show_output = TRUE)

best_run <- get_best_run_by_primary_metric(run)
register_model_from_run(
  run = best_run,
  model_name = "keras-hyperparameter",
  model_path = "outputs/model.rds"
)
