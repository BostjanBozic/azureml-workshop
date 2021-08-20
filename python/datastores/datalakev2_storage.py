from azureml.core import Workspace, Datastore

ws = Workspace.from_config(path="../../")
datastorage_name = "rimidatalake"

datastore = Datastore.register_azure_data_lake_gen2(
  workspace=ws,
  datastore_name=datastorage_name,
  filesystem="rimi-workshop",
  account_name="rimibalticssa",
)
