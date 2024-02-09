# main.py

import Calc.PythonCalc as C 

calc=C.Calculator(84,4)

print("Addition:", calc.addition())
print("Subtraction:", calc.subtraction())
print("Multiplication:", calc.multiplication())
print("Division:", calc.division())
print("Square Root:", calc.square_root(9))
print("Power:", calc.power())

