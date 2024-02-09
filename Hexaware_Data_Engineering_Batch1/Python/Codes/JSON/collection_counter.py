
from collections import Counter
def unique(list1):
    print("the unique values from list is")
    print(*Counter(list1))

list1=[10,20,10,30,40,40]
unique(list1)

list2 = [1,2,1,1,3,4,3,3,5]
unique(list2)

