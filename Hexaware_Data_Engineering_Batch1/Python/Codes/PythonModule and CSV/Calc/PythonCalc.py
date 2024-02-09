import math
class Calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def addition(self):
        return self.a+self.b

    def subtraction(self):
        return self.a-self.b

    def multiplication(self):
        return self.a*self.b

    def division(self):
        if self.b==0:
            return "B cannot be zero"
        else:
            return self.a / self.b
            
    def square_root(self, c):
        return math.sqrt(c)

    def power(self):
        return math.pow(self.a, self.b)


