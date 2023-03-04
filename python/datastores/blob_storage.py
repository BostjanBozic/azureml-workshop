from azureml.core import Workspace, Datastore

ws = Workspace.from_config(path="../../")
datastorage_name = "exampleblobstorage"

datastore = Datastore.register_azure_blob_container(
  workspace=ws,
  datastore_name=datastorage_name,
  container_name="example",
  account_name="examplesa",
  account_key="<insert_account_key>",
  create_if_not_exists=True,
)
