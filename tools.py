import json
import pandas as pd


def create_csv(state):

    data = state["data"]
    df = pd.DataFrame(data)

    output_file = "jobs.csv"

    df.to_csv(output_file, index=False)

    state["output_file"] = output_file

    return state