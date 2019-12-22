from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Square import square
from Calculator.Squareroot import squareroot
from Calculator.Multiplication import multiplication


class Calculator:  # Class named 'Calculator'
    result = 0

    def __init__(self):  # Class constructor
        pass

    def add(self, a, b):  # Below are the Functions
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = squareroot(a)
        return self.result