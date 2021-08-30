library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")

git_package <- github_package(repository = "Azure/azureml-sdk-for-r")

env <- r_environment(
  name = "github-environment",
  r_version = "3.6.0",
  github_packages = list(git_package)
)

register_environment(
  environment = env,
  workspace = ws
)
