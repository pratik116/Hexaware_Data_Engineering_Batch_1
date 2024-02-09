
from functools import reduce

def unique(list1):
    ans=reduce(lambda re,x: re+[x] if x not in re else re, list1, [])
    print("the unique values from 1st list is")
    print(ans)


list1=[10,10,10,20,20,30]
unique(list1)

list2=[1,2,1,1,3,4,3,3,5]
unique(list2)

