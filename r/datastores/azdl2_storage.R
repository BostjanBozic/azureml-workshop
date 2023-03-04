library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")
ds_name <- "datalake_gen2"

ds <- register_azure_data_lake_gen2_datastore(
  workspace = ws,
  datastore_name = ds_name,
  filesystem = "example",
  account_name = "examplesa"
)
