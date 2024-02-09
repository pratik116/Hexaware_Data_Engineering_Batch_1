my_set1={1, 2, 3, 3, 4, 5}

my_set2={3, 4, 5, 6}
print(my_set1)

#add
my_set1.add(6)
print(my_set1)

#update
my_set1.update([7, 8, 9])
print(my_set1)

#remove
my_set1.remove(3)
print(my_set1)

#union
new_uset=my_set1.union(my_set2)
print(new_uset)

#intersection
new_iset=my_set1.intersection(my_set2)
print(new_iset)