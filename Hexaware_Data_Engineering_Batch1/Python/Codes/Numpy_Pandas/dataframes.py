import csv
import pandas as pd

store=pd.read_csv("practice.csv")
print(store)

print("\n")
dataframe_store=pd.DataFrame(store)
print(dataframe_store)
