import numpy as np
import pandas as pd

store=pd.read_csv("practice.csv")
data=pd.DataFrame(store)


print("Count of males:\n",(data.query("Gender == 'Male' and Age>25")).count())

