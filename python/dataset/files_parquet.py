from azureml.core import Dataset, Datastore, Workspace

ws = Workspace.from_config(path="../../")

datastore = Datastore.get(
  workspace=ws,
  datastore_name="rimiblobstorage",
)

dataset = Dataset.File.from_files(path=(datastore, "*.parquet"))

dataset.register(
  workspace=ws,
  name="blob-parquet-non-tabular",
  create_new_version=True,
)
