import math

class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    
    def mulitply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y
    
    def square(self, x):
        return x ** 2  # or: return x * x

    def squareroot(self, x):
        return math.sqaureroot(x)

    def exp(self, x, y):
        return x ** y

    def inverse(self, x):
        return 1 / x

    def invert(self, x):
        return x * -1

    def sin(self, x):
        return (math.sin(x))
    
    def cos(self, x):
        return (math.cos(x))

    def tan(self, x):
        return (math.tan(x))
    


# add lots more methods to this calculator class.
