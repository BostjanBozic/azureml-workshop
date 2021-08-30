library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")

aks_rg <- "rimi"
aks_name <- "rimi-aks"

aks_target <- attach_aks_compute(
  workspace = ws,
  resource_group = aks_rg,
  cluster_name = aks_name,
  cluster_purpose = "DevTest"
)
