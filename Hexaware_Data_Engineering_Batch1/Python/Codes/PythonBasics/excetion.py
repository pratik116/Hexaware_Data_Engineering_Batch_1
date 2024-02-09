try:
    a=int(input("Enter the a: "))
    b=int(input("Enter the b: "))
    result=a/b
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful.")
finally:
    print("This will always execute.")
