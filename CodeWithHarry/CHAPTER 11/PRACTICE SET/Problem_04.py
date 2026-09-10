#Write a class 'Complex' to represent complex numbers, along with
#overloaded operators '+' and '*' which adds and multiplies them.
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary

        )
    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imaginary * other .imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def show(self):
        print(f"{self.real} + {self.imaginary}i")

c1 = Complex(2, 3)
c2 = Complex(4, 6)

print("First complex number : ")
c1.show()

print("\nSecond complex number : ")
c2.show()

print("\nAddition of both numbers : ")
result1 = c1 + c2
result1.show()

print("\nMultiplication of both numbers : ")
result2 = c1 * c2
result2.show()