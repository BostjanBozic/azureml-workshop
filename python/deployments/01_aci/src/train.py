from azureml.opendatasets import Diabetes
import joblib
from sklearn.linear_model import Ridge
# from azureml.core import Dataset, Datastore, Workspace
# from azureml.core import Run

# run = Run.get_context()
# ws = run.experiment.workspace
# datastore = Datastore.get(ws, "blob_storage")
# diabetes = Dataset.Tabular.from_delimited_files(path=(datastore, "diabetes.tab.txt"),separator="\t")

diabetes = Diabetes.get_tabular_dataset()

X = diabetes.drop_columns("Y")
y = diabetes.keep_columns("Y")
X_df = X.to_pandas_dataframe()
y_df = y.to_pandas_dataframe()
X_df.info()

model = Ridge().fit(X_df,y_df)
joblib.dump(model, 'outputs/diabetes.pkl')
