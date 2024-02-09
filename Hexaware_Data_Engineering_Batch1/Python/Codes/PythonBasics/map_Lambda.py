#map

L=['1','2','3']

new_L=list(map(int,L))

print(new_L[0]+new_L[1])

print("\n*********")    


#lambda


numbers=[1,2,3,4]

squared_numbers=map(lambda x: x**2, numbers)

print(list(squared_numbers))

