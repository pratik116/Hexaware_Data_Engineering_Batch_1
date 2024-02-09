import pandas as pd

data={
    "name": ["Pratik","Vikas","Rushi"],
    "age": [21,23,25],
    "city": ["nashik","pune","nagpur"]                                                                                                                                                                                                                          
    }
df=pd.DataFrame(data)
print(df)


df.to_json("student_salary.json",orient='records')

print("\n**********\n")
