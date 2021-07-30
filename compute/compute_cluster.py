from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.from_config(path="../")
cluster_name = "rimi-cluster"

try:
  cluster = ComputeTarget(
    workspace=ws,
    name=cluster_name,
  )
except ComputeTargetException:
  cluster_config = AmlCompute.provisioning_configuration(
    vm_size="STANDARD_DS3_V2",
    max_nodes=5,
    identity_type="SystemAssigned",
  )
  cluster = ComputeTarget.create(
    workspace=ws,
    name=cluster_name,
    provisioning_configuration=cluster_config,
  )
  
  cluster.wait_for_completion(show_output=True)
