from azureml.core import Workspace
from azureml.core import Environment

ws = Workspace.from_config(path="../")

cust_envir = Environment.from_pip_requirements(
  name="rimi-from-pip",
  file_path="./requirements.txt",
)

cust_envir.register(ws)
cust_envir.build(ws)
