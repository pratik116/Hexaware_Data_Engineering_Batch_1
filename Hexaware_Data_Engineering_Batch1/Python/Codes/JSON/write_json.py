import json

dictionary ={
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

with open("flag.json", "w") as outfile:
    json.dump(dictionary, outfile)
