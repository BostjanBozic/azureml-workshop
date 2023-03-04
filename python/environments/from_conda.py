from azureml.core import Workspace, Environment
from azureml.core.conda_dependencies import CondaDependencies

ws = Workspace.from_config(path="../../")

conda = CondaDependencies()

conda.add_channel("conda-forge")
conda.add_conda_package("python==3.8")
conda.add_conda_package("pip==20.0.2")
conda.add_conda_package("matplotlib")
conda.add_conda_package("numpy")

conda.add_pip_package("pandas")

env = Environment(name="example-conda")
env.python.conda_dependencies = conda

env.register(workspace=ws)
env.build(workspace=ws)
