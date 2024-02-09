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
