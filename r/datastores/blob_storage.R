library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")
ds_name <- "blob_storage"

ds <- register_azure_blob_container_datastore(
  workspace = ws,
  datastore_name = ds_name,
  container_name = "example",
  account_name = "examplesa",
  account_key = "<add_key>",
  create_if_not_exists = TRUE
)
