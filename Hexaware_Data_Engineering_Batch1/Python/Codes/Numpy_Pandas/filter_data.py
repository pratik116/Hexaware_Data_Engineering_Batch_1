import pandas as pd

data=pd.read_csv("practice.csv")
store=pd.DataFrame(data)

filter_store=store.query("Gender == 'Male'")
print(filter_store)