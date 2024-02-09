import pandas as pd

#creating series
series=pd.Series(['P','R','A','T','I','K'])
print("Pandas Series:\n",series)
print("\n**********\n")

#creating dataframe using pandas
header=['Name','Age','Salary']
data=[['Pratik',21,'50000'],['Vikas',23,100000],['Rushi',22,120000]]
df=pd.DataFrame(data,columns=header)
print(df)