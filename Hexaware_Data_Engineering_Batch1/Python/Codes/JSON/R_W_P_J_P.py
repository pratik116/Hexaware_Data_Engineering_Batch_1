import json

student='{"id":"1", "name":"pratik", "class":"A", "Grade":30}'


student_dict=json.loads(student)
print(student_dict)

print(student_dict['name'])
