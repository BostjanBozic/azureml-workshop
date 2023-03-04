library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")
ds_name <- "file_share"

ds <- register_azure_file_share_datastore(
  workspace = ws,
  datastore_name = ds_name,
  file_share_name = "example",
  account_name = "examplesa",
  account_key = "<add_key>",
  create_if_not_exists = TRUE
)
