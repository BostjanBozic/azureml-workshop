import os
from azureml.core.model import Model
from azureml.core import Run

parser = argparse.ArgumentParser("register")
 
parser.add_argument("--model", type=str, help="model")
 
args = parser.parse_args()
run = Run.get_context()
ws = run.experiment.workspace

run.log("Register start time", str(datetime.datetime.now()))

model = Model.register(
  workspace=ws,
  model_path=(args.model + "/model.joblib"),
  model_name="diabetes-logistic-regression",
)

run.log("Register end time", str(datetime.datetime.now()))

run.complete()
