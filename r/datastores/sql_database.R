library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")
ds_name <- "sql_database"

ds <- register_azure_sql_database_datastore(
  workspace = ws,
  datastore_name = ds_name,
  server_name = "example",
  endpoint = "database.windows.net",
  database_name = "example-db"
)
