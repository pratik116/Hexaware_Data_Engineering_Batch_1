import pandas as pd

data1= {'roll_no': [1, 2, 10, 12, 14],
    'name': ['Pratik', 'Vikas', 'Rushi', 'Ram','Rushi']}

dataframe1= pd.DataFrame(data1)



data2= {'roll_no': [1, 2, 10, 12, 14],
    'course': ['Math', 'Science', 'History', 'Science', 'Science']}

dataframe2= pd.DataFrame(data2)


result= pd.merge(dataframe1, dataframe2, on='roll_no', how='inner')
# print(result)


aggregated_result= result.groupby('name')['roll_no'].count()
print(aggregated_result)


