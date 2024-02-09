#using read_table

import pandas as pd
file=pd.read_table("practice.csv",delimiter =",")

print(file.head())
print("\n")

#using csv module
import csv

with open("practice.csv") as file:
    store=csv.reader(file)
    data=pd.DataFrame([store],index=None)

    for i in range(0,len(list(data))):
        for val in list(data[i]):
            print(val)

print("\n")
#using read_csv
            
import pandas as pd
data=pd.read_csv("practice.csv")

print(data.head())