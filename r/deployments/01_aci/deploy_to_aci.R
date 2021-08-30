library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../../")
model <- get_model(
  workspace = ws,
  name = "accidents-logistic",
  version = as.integer(1)
)

env <- r_environment(
  name = "r-environment",
  custom_docker_image = "9054a1a822d04d21a7a5f4e726da20cc.azurecr.io/r-azureml:latest" # nolint
)

inference_config <- inference_config(
  source_directory = "./src",
  entry_script = "score.R",
  environment = env
)

deployment_config <- aci_webservice_deployment_config(
  cpu_cores = 1,
  memory_gb = 1
)

deployment_name <- "accidents-aci"
current_deployment <- tryCatch({
    get_webservice(
    workspace = ws,
    name = deployment_name
  )
}, error = function(e) {
  current_deployment <- ""
})

if (current_deployment == "") {
  endpoint <- deploy_model(
    workspace = ws,
    name = deployment_name,
    models = list(model),
    inference_config = inference_config,
    deployment_config = deployment_config
  )

  wait_for_deployment(
    webservice = endpoint,
    show_output = TRUE
  )
} else {
  update_aci_webservice(
    webservice = current_deployment,
    models = list(model),
    inference_config = inference_config
  )

  wait_for_deployment(
    webservice = current_deployment,
    show_output = TRUE
  )
}
