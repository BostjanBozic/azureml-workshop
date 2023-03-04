from azureml.core import Dataset, Datastore, Workspace

ws = Workspace.from_config(path="../../")

datastore = Datastore.get(
  workspace=ws,
  datastore_name="exampleblobstorage",
)

dataset = Dataset.Tabular.from_parquet_files(path=(datastore, "*.parquet"))

dataset.register(
  workspace=ws,
  name="blob-parquet-files",
  create_new_version=True,
)
