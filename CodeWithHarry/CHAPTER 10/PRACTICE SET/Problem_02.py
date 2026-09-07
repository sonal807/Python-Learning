#Write a class "calculator" capable of finding square, cube and square root of a number.

import math
class calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number) #we can also write (self.number ** 1/2) but we have imported math module so we simply use sqrt.

number = float(input("Enter the number:"))

calculator = calculator(number)

print("Square:", calculator.square())
print("Cube:", calculator.cube())
print("Square Root:", calculator.square_root())