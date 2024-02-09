print('Hello World!!')





# for loop
for i in range(0,10):
    print(i)





# if-elif-else and exception handling
    
try:
    age=int(input('Enter your age: '))
    if age<=0:
        raise ValueError
    elif(age>=18):
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")
except Exception:
    print("Not valid age")
else:
    print("Answer provided")







# while
count=1

while count< 5:
    print(count)
    count+=1
        





#function
from math import sqrt
def checkprime(number):
    flag=1
    if number>1:
        for i in range(2,int(sqrt(number))+1):
            if(number%i==0):
                flag=0
        if(flag==0):
            return False
        else: 
            return True

    else:
        return False
    
number=int(input("Enter the number: "))
if checkprime(number):
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")







#list
L=[1,2,3,4,5,6,7]
L.append(8)
print(L)
print(len(L))
L.reverse()
print(L)
print(L[0:4])
L.pop()
print(L)








# string
temp='pratik'
print(temp[:])
print(len(temp))
string='Wani'
print(temp+string)



#slicing
print(temp[0:3])

#-ve slicing
print(temp[-4:-1])







#dict
pratik={
    'name': "Pratik",
    'Age' : 13
}

print(pratik['name'])
print(pratik.get(1))
print(pratik.keys())
pratik.pop(1)








#sets
var = {"Pratik", "Arun", "Wani"}
type(var)








#oops
class Man:

    # class attribute
    clsattr="pratik"
    # Instance attribute
    def __init__(self,name):
        self.name = name

    #fucntion
    def age(self,age):
        print("My age is :"+ age)

# Driver code
# Object instantiation
V= Man("Vikas")
R= Man("Rushi")

# Accessing class attributes
print("The default name is: "+Man.clsattr)


# Accessing instance attributes
print(V.name)
print(R.name)


#inheritance
class family(Man):
    def __init__(self, name, salary):
        self.salary = salary
        # invoking the __init__ of the parent class
        Man.__init__(self, name)

a = family('Rahul', 886012)






#file handling
file=open(r"test.txt","w")
print(file)
l=[str(x) for x in range(0,10)]
file.writelines(l)
file.close()
f=open(r"test.txt","r")
print(f.readlines(19))



#break, continue, pass
for i in range(1, 5): 
    if(i%2==0):
        pass
    if(i==1):
        continue
    for j in range(2, 6): 
        if j%i == 0: 
            break
        print(i, " ", j)