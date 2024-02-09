import pandas as pd


with open("codingchallenge.csv") as file:
    cc_data=pd.read_csv(file)
    dataframe=pd.DataFrame(cc_data)
    print(dataframe)