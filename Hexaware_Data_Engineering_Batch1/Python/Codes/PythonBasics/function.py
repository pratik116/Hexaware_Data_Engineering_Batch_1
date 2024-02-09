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