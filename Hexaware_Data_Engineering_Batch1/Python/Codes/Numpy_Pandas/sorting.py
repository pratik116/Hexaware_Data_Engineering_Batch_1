import pandas as pd

data=pd.read_csv("practice.csv")
dataframe=pd.DataFrame(data)
print(dataframe,"\n")

sorted_df=dataframe.sort_values(by='Name')
print("Ascending order:")
print(sorted_df,"\n")


sorted_df_desc=dataframe.sort_values(by='Name',ascending=False)


print("Descending order:")
print(sorted_df_desc)