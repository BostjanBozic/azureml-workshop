from azureml.core import Workspace, Experiment, Environment,ScriptRunConfig
from azureml.core.compute import ComputeTarget
from azureml.core.runconfig import RunConfiguration

ws = Workspace.from_config(path="../../../")
compute_cluster = "rimi-cluster"

ray_env = Environment.from_conda_specification(
    name = "RayEnv",
    file_path = "./conda.yml"
)

ray_cluster = ComputeTarget(
    workspace=ws,
    name=compute_cluster
)

aml_run_config_ml = RunConfiguration(communicator='OpenMpi')
aml_run_config_ml.target = ray_cluster
aml_run_config_ml.node_count = 6
aml_run_config_ml.environment = ray_env

src = ScriptRunConfig(
    source_directory='./src',
    script='proc.py',
    run_config = aml_run_config_ml,
)

run = Experiment(ws, "rl_on_aml_job").submit(src)
