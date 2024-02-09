
import operator as op
def unique(list1):
    unique_list = []
    for x in list1:
        if op.countOf(unique_list, x) == 0:
            unique_list.append(x)
    print("the unique values from list is")
    for x in unique_list:
        print(x)


list1 = [10, 20, 10, 30, 40, 40]
unique(list1)

list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
unique(list2)

