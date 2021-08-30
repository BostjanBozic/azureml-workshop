library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")

datastore <- get_datastore(workspace = ws, datastore_name = "blob_storage")

datapath <- data_path(
  datastore = datastore,
  path_on_datastore = "*.parquet"
)

dataset <- create_file_dataset_from_files(path = datapath)

register_dataset(
  workspace = ws,
  dataset = dataset,
  name = "files",
  create_new_version = TRUE
)
