import pandas as pd

header=['Name','Age','Salary']
data=[['Pratik',21,'50000'],['Vikas',23,100000],['Rushi',22,120000]]
df=pd.DataFrame(data,columns=header)
print(df)


df.to_csv("student_salary_info.csv",index=False)

print("\n**********\n")
print(pd.read_csv('student_salary_info.csv'))
print("\n**********\n")