library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")

datastore <- get_datastore(workspace = ws, datastore_name = "blob_storage")

datapath <- data_path(
  datastore = datastore,
  path_on_datastore = "*.parquet"
)

dataset <- create_tabular_dataset_from_parquet_files(path = datapath)

register_dataset(
  workspace = ws,
  dataset = dataset,
  name = "parquet-files",
  create_new_version = TRUE
)
