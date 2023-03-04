from azureml.core import Workspace
from azureml.core.compute import ComputeInstance
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.from_config(path="../../")
compute_name = "example-instance"

try:
  instance = ComputeInstance(
    workspace=ws,
    name=compute_name,
  )
except ComputeTargetException:
  compute_config = ComputeInstance.provisioning_configuration(
    vm_size="STANDARD_DS3_V2",
    ssh_public_access=False,
  )
  instance = ComputeInstance.create(
    workspace=ws,
    name=compute_name,
    provisioning_configuration=compute_config,
  )
  instance.wait_for_completion(show_output=True)
