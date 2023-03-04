from azureml.core import Workspace

ws = Workspace.create(
  name="example",
  subscription_id="<subscription_id>",
  resource_group="examplerg",
  location="westeurope",
  create_resource_group=False,
)

ws.write_config(path="../../", file_name="config.json")
