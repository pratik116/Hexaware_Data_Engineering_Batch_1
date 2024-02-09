import json

coding_challeng='''{
"name": "pratik wani",
"age": 21,
"city": "nashik",
"isStudent": "Yes",
"grades": [85, 92, 78],
"address": {
    "street": "Ranapratap chaowk",
    "zipcode": "422009",
    "country": "India"
}
}'''

My_details=json.loads(coding_challeng)

print("Name: ",My_details['name'])
print("Age: ",My_details['age'])
print("City: ",My_details['city'])
print("Status: ",My_details['isStudent'])
print("Grades: ",My_details['grades'])
for i in My_details['address'].items():
    print(i[0],": ",i[1])


