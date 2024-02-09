import json

jsonString='''{
"name": "pratik wani",
"age": 21,
"city": "nashik",
"isStudent": false,
"grades": [85, 92, 78],
"address": {
    "street": "Ranapratap chaowk",
    "zipcode": "422009",
    "country": "India"
}
}'''

My_details=json.loads(jsonString)

print(My_details)
print("\n")

print(My_details['name'])


