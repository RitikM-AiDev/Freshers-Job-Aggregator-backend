from typing import TypedDict
import os
from langgraph.graph import StateGraph, END
from tools import create_csv


class JobState(TypedDict):
    file_path: str
    data: list
    output_file: str
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "jobs.csv")
def a2a(data_list : str):
    workflow = StateGraph(JobState)
    workflow.add_node("create_csv", create_csv)
    workflow.set_entry_point("create_csv")
    workflow.add_edge("create_csv", END)
    app = workflow.compile()
    result = app.invoke({
        "file_path": path,
        "data" : data_list,
        "output_file" : ""
    })

    print(result)
    print("CSV Created:", result["output_file"])
    return path