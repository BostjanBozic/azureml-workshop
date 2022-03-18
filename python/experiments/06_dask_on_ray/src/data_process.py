import datetime
import json
import pandas as pd
import numpy as np
import dask
import dask.dataframe as dd
from ray.util.dask import ray_dask_get
from ray_on_aml.core import Ray_On_AML


dask.config.set(scheduler=ray_dask_get)
ray_on_aml =Ray_On_AML()
ray = ray_on_aml.getRay()

def prepare_data(sales_data):
    sales_data["date"] = dd.to_datetime(sales_data["date"])
    df_groups = dd.from_pandas(pd.DataFrame({"something": list("abcaddbe" * 300), "testString": "this is it"}), npartitions = 5)
    sales_data = sales_data.merge(
        df_groups,
        left_on="b",
        right_on="something"
    )
    
    return sales_data


if ray:
    print("Main node")
    df_list_dask = dd.from_pandas(pd.DataFrame(), npartitions=10)
    current_time = datetime.datetime.now()
    df1 = dd.from_pandas(pd.DataFrame({"date": current_time, "a": np.arange(270000), "b": list("abcadbefg" * 30000), "c": "TEST", "d": "1572"}), npartitions=10)
    df2 = dd.from_pandas(pd.DataFrame({"date": current_time, "a": np.arange(270000), "b": list("abcadbefg" * 30000), "c": "TEST", "d": "1220"}), npartitions=10)
    df3 = dd.from_pandas(pd.DataFrame({"date": current_time, "a": np.arange(270000), "b": list("abcadbefg" * 30000), "c": "SOMETHING", "d": "1007"}), npartitions=10)
    df4 = dd.from_pandas(pd.DataFrame({"date": current_time, "a": np.arange(270000), "b": list("abcadbefg" * 30000), "c": "SOMETHING", "d": "1234"}), npartitions=10)
    ddf = dd.concat([df1, df2, df3, df4])

    categories = json.load(open("mapping.json"))

    for key, value in categories.items():
        for i in value:
            ddf_filtered = ddf[((ddf.c == key) & (ddf.d == i))]
            ddf_prep = prepare_data(sales_data=ddf_filtered)

            df_list_dask = dd.concat([df_list_dask, ddf_prep])
    
    df_list_dask.compute().to_csv("./outputs/output.csv")

else:
    print("Worker node")
