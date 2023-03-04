from azureml.core import Dataset, Datastore, Workspace

ws = Workspace.from_config(path="../../")

datastore = Datastore.get(
  workspace=ws,
  datastore_name="exampleblobstorage",
)

dataset = Dataset.Tabular.from_delimited_files(path=(datastore, "*.csv"))

dataset.register(
  workspace=ws,
  name="blob-csv-files",
  create_new_version=True,
)
