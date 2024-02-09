
import json

with open('data.json') as json_file:
    data=json.load(json_file)

    print("\nPrinting nested dictionary as a key-value pair\n")

    for i in data.items():
        print(i)

