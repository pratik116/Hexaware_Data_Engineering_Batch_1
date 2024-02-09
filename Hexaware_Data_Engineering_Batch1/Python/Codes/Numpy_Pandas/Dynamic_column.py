import pandas as pd
import csv

data=pd.read_csv('practice.csv',usecols=['Name','Occupation'])
print(data)