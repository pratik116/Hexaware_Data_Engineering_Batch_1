import csv
import pandas as pd
import numpy as np

# 1) reading data in csv using open and reader
rows=[]
with open("practice.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print("\n*******\n")
for i in rows:
    print(i)


# 2) reading data in csv using readlines
print("\n*******\n")
with open('practice.csv') as file:
    content = file.readlines()
header = content[:2]
rows = content[3:]
print(header)
print("\n*******\n")

print(rows)
print("\n*******\n")


# 3) reading file using pandas
data= pd.read_csv("practice.csv")
print(data)
print("\n**********\n")

#extracting the columns
print(data.columns)
print("\n**********\n")

#extracting specific column
print(data.Name)
print("\n**********\n")

# 4) reading data using DictReader
with open('practice.csv','r') as file:
    reader=csv.DictReader(file)

    for i in file:
        print(i)


#creating series
data=np.array(['P','R','A','T','I','K'])
series=pd.Series(data)
print("\n**********\n")
print("Pandas Series: ",series)
print("\n**********\n")



#creating dataframe using pandas
header=['Name','Age','Salary']
data=[['Pratik',21,'50000'],['Vikas',23,100000],['Rushi',22,120000]]
df=pd.DataFrame(data,columns=header)
print(df)

# 1) write using pandas: 

df.to_csv("student_salary_info.csv",index=False)

print("\n**********\n")
print(pd.read_csv('student_salary_info.csv'))
print("\n**********\n")

# 2) write in  csv file using DictReader

data=[{'Name':'Rudra','Age':25,'Salary':300000},
    {'Name':'Krushna','Age':24,'Salary':400000},
    {'Name':'Ram','Age':21,'Salary':20000}]

with open('test.csv', 'w', newline='') as file:
    field_names=['Name', 'Age', 'Salary']

    writer=csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader()

    writer.writerows(data)

# 3) write in  csv file using csv.writer

header=['Name','Score','Class']
data=[['Pratik',92,'A'], ['Rushi',80,'B'], ['Joey',93,'A']]

filename='Students_Data_write.csv'
with open(filename, 'w', newline="") as file:
    csvwriter= csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

# 4) write in  csv file using csv.writerlines
    
header=['Name','Score','Class']
data=[['Pratik',92,'A'], ['Rushi',80,'B'], ['Joey',93,'A']]
filename = 'Student_Data_writelines.csv'
with open(filename, 'w') as file:
    for header in header:
        file.write(str(header)+', ')
    file.write('n')
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('n')
