from azureml.core import Workspace, Datastore

ws = Workspace.from_config(path="../../")
datastorage_name = "examplefileshare"

datastore = Datastore.register_azure_file_share(
  workspace=ws,
  datastore_name=datastorage_name,
  file_share_name="example-file-share",
  account_name="examplesa",
  account_key="<insert_account_key>",
  create_if_not_exists=True,
)
