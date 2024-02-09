
def unique(l):
    l_set=set(l)
    new_list=list(l_set)
    print("the unique values from list is:")
    for i in new_list:
        print(i)

l1=[10,20,10,30,40,40,90,90,90]
unique(l1)


l2=[1,2,1,1,3,4,3,3,5]
unique(l2)

