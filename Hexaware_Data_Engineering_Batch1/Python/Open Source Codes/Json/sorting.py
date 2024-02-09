import json
with open("test.json") as file:
    py_data=json.load(file)
    sorted_py_data=sorted(py_data["students"],key=lambda x:x["age"])
    print(json.dumps(sorted_py_data,indent=2))