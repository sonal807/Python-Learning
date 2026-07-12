#Define a Circle class To create a circle with radius r using the constructor.
#Define an Area() method of the class which calculates the area of the circle. 
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle. 

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print("The area of the circle:", c1.area())
print("The perimeter of the circle:", c1.perimeter())