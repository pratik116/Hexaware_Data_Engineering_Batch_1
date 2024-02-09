import pandas as pd

#first create dataframe
cc_data=pd.read_csv("codingchallenge.csv")
store=pd.DataFrame(cc_data)

#then we will use query method to apply different filters
filter_store1=store.query("Salary > 70000")
print(filter_store1,'\n')

filter_store2=store.query("Age == 33 or Age == 35")
print(filter_store2)