import json
json_data = '''
{
"students": [
    {
        "name": "Alice",
        "age": 20,
        "grades": [85, 90, 95],
        "isgoodstudent":true
    },
    {
        "name": "Bob",
        "age": 22,
        "grades": [75, 80, 85],
        "isgoodstudent": false
    }
    ]
}
'''
py_data=json.loads(json_data)
print(json.dumps(py_data,indent=4))
print(type(py_data))
print(py_data)
print((py_data['students'][0]['grades']))
for i in range(len(py_data['students'])):
    if (py_data['students'][i]['name']) == 'Bob':
        print('Bob Grades: ',py_data['students'][i]['grades'])

with open("sample.json") as file:
    py_data_from_file=json.load(file)
    print(json.dumps(py_data_from_file,indent=2))


