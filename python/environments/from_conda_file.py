from azureml.core import Workspace
from azureml.core import Environment

ws = Workspace.from_config(path="../../")

cust_envir = Environment.from_conda_specification(
  name="example-from-condafile",
  file_path="./conda.yml",
)

cust_envir.register(ws)
cust_envir.build(ws)
