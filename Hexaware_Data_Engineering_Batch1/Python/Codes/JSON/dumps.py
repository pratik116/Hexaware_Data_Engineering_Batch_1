import json

my_data = {
    "name": "pratik wani",
    "age": 21,
    "city": "nashik",
    "isStudent": False,
    "grades": [85, 92, 78],
    "address": {
        "street": "Ranapratap chaowk",
        "zipcode": "422009",
        "country": "India"
    }
    }

json_object=json.dumps(my_data,indent=4)
print(json_object)