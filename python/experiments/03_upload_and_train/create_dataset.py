from azureml.core import Dataset, Datastore, Workspace

ws = Workspace.from_config(path="../../../")

datastore = Datastore.get(ws, "exampleblobstorage")

dataset = Dataset.File.from_files(path=(datastore, "datasets/cifar10"))

dataset.register(
  workspace=ws,
  name="cifar10",
  create_new_version=True,
)
