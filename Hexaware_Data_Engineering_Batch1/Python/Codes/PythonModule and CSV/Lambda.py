numbers=[1,2,3,4]

squared_numbers=map(lambda x: x**2, numbers)

print(list(squared_numbers))


#map
L=['1','2','3']
new_L=list(map(int,L))

print(new_L[0]+new_L[1])
print("\n*********")  

#filter
odd_elements=list(filter(lambda x: x%2!=0,new_L))

print(odd_elements)
print("\n*********")  

#reduce
from functools import reduce
Sum=reduce(lambda x,y: x+y,new_L)

print(Sum)
print("\n*********")  
