from azureml.core import Workspace, Environment

ws = Workspace.from_config(path="../")

env = Environment(name="rimi-from-dockerfile")
env.docker.base_dockerfile = "./Dockerfile"
env.environment_variables["ENV_NAME"] = "your majesty"

env.register(ws)
env.build(ws)
