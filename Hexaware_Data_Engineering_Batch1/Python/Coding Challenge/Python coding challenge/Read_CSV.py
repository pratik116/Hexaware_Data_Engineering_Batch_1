import pandas as pd

#reading file using pandas
cc_data= pd.read_csv("codingchallenge.csv")
print(cc_data,'\n')


#extracting the columns
print(cc_data.columns,'\n')


#extracting specific column
print(cc_data.Name,'\n')
