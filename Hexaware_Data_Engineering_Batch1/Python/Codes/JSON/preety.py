import json

employee = '{"id":"01", "name": "Pratik", "department":"IT","age":21}'
employee_dict=json.loads(employee)

print(json.dumps(employee_dict,indent=4,sort_keys=True))
