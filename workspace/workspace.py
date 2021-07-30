from azureml.core import Workspace

ws = Workspace.create(
  name="rimi-workshop",
  subscription_id="32dff789-bcd1-41d0-8899-b06bf1c4a8c7",
  resource_group="rimi-architecture-ws-rg",
  location="westeurope",
  create_resource_group=False,
)

ws.write_config(path="../", file_name="config.json")
