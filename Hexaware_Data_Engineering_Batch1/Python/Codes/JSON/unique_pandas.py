import pandas as pd

def unique(l):
    unique_list=pd.Series(l).drop_duplicates().tolist()
    print("the unique values from list is")
    for i in unique_list:
        print(i)

l1=[10,20,10,30,40,40,80]
unique(l1)

l2=[1,2,1,1,3,4,3,3,5]
unique(l2)
