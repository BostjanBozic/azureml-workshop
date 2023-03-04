library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")
cluster_name <- "example-cluster"

cluster <- get_compute(workspace = ws, cluster_name = cluster_name)
if (is.null(cluster)) {
  cluster <- create_aml_compute(
    workspace = ws,
    cluster_name = cluster_name,
    vm_size = "STANDARD_DS3_V2",
    max_nodes = 4
  )

  wait_for_provisioning_completion(
    cluster = cluster,
    show_output = TRUE
  )
}
