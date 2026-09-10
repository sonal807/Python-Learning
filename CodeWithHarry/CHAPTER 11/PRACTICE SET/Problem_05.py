#Write a class vector representing a vector of n dimensions.
#Overload the + and * operator ehich calculates the sum and dot(.) product of them 

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y +self.z * other.z

    def show(self):
        print(f"({self.x} , {self.y} , {self.z})")

c1 = Vector(2,3,4)
c2 = Vector(4,6,7)

print("First Vector : ")
c1.show()

print("\nSecond Vector  : ")
c2.show()

print("\nAddition of both vectors: ")
result1 = c1 + c2
result1.show()

print("\nDot product of both vectors : " , c1*c2)
# Dot product of two vectors produces a scalar quantity(a single number)