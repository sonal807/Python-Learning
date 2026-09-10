#Operator Overloading means defining how an operator behaves when it is used with objects of a class.
#Operators in python can be overloaded using dunder methods
#These methods are called when diven operator is used on the object

#__add__() overloading + operator: __add__() is a special method used to define 
#the behavior of the + operator for objects of a user-defined class.
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):    #__add__() is dunder method that define the behaviour of operator +
        return self.value + other.value

a = Number(10)
b = Number(20)

print(a+b)

#Example
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

n1 = Number(40)
n2 = Number(60)

print(n1 + n2)

#__sub__() overloading - operator:__sub__() is a special method used to define 
#the behavior of the - operator for objects of a user-defined class.
class Number:
    def __init__(self, n):
        self.n = n

    def __sub__(self, other):  #__sub__() define the behaviour of -
        return self.n - other.n

n1 = Number(25)
n2 = Number(5)

print(n1- n2)

#Example
class Number:
    def __init__(self, m):
        self.m = m

    def __sub__(self, other):
        return self.m - other.m

m1 = Number(100)
m2 = Number(35)

print(m1 - m2)

#__mul__() overloading * opertor: __mul__() is a special method used to define the 
#behavior of the * operator for objects of a user-defined class.
class Number:
    def __init__(self, m):
        self.m = m

    def __mul__(self, other):  #__mul__() define the behaviour of *
        return self.m * other.m

m1 = Number(15)
m2 = Number(5)

print(m1 * m2)

#Example
class Number:
    def __init__(self,f):
        self.f = f

    def __mul__(self, other):
        return self.f * other.f

f1 = Number(12)
f2 = Number(8)

print(f1 * f2) 

#__truediv__() overloading / operator: __truediv__() is a special method used to define
#the behavior of the / operator for objects of a user-defined class.
class Number:
    def __init__(self, d):
        self.d = d

    def __truediv__(self, other): #__truediv__() defines the behavoiur of / operator
        return self.d / other.d

d1 = Number(25)
d2 = Number(5)

print(d1 / d2)

#Example
class Number:
    def __init__(self, d):
        self.d = d

    def __truediv__(self, other):
        return self.d / other.d

d1 = Number(100)
d2 = Number(4)

print(d1 / d2)

#__eq__() overloading == operator: __eq__() is a special method used to define 
#how the == operator compares two objects.
class Number:
    def __init__(self,e):
        self.e = e

    def __eq__(self, value): #__eq__() defines the behaviour of == operator
        return self.e == value.e

e1 = Number(25)
e2 = Number(25)

print(e1 == e2)

#Example
class Number:
    def __init__(self,e):
        self.e = e

    def __eq__(self, value):
        return self.e == value.e

e1 = Number(22)
e2 = Number(33)

print(e1 == e2)

#__lt__() overloading < operator: __lt__() is a special method used to define the
#behavior of the < operator when comparing objects.
class Number:
    def __init__(self, l):
        self.l = l

    def __lt__(self, other):  #__lt__() defines the behaviour of < operator
        return self.l < other.l

l1 = Number(10)
l2 = Number(29)

print(l1 < l2)

#Example
class Number:
    def __init__(self, l):
        self.l = l

    def __lt__(self, other):
        return self.l < other.l

l1 = Number(33)
l2 = Number(9)

print(l1 < l2)

#__gt__() overloading > operator:__gt__() is a special method used to define the
#behavior of the > operator when comparing objects.
class Number:
    def __init__(self,g):
        self.g = g

    def __gt__(self, other): #__gt__() defines the behaviour of > operator
        return self.g > other.g

g1 = Number(87)
g2 = Number(67)

print(g1 > g2)

#Example
class Number:
    def __init__(self,g):
        self.g = g

    def __gt__(self, other):
        return self.g > other.g

g1 = Number(30)
g2 = Number(55)

print(g1 > g2)

#__le__() overloading <= operator: __le__() is a special method used to define the
# behavior of the <= operator when comparing objects.
class Number:
    def __init__(self, small):
        self.small = small

    def __le__(self, other):  #__le__() defines the behaviour of <= operator
        return self.small <= other.small

s1 = Number(20)
s2 = Number(20)

print(s1 <= s2)

#Example
class Number:
    def __init__(self, small):
        self.small = small

    def __le__(self, other):
        return self.small <= other.small

s1 = Number(25)
s2 = Number(30)

print(s1 <= s2)

#__ge__() overloading >= operator: __ge__() is a special method used to define the
#behavior of the >= operator when comparing objects.
class Number:
    def __init__(self,big):
        self.big = big

    def __ge__(self, other):  #__ge__() defines the behaviour of >= opeator
        return self.big >= other.big

b1 = Number(38)
b2 = Number(25)

print(b1 >= b2)

#Example
class Number:
    def __init__(self,big):
        self.big = big

    def __ge__(self, other):
        return self.big >= other.big

b1 = Number(10)
b2 = Number(10)

print(b1 >= b2)

#__ne__() overloading != operator: __ne__() is a special method used to define the
#behavior of the != operator when comparing objects
class Number:
    def __init__(self, n):
        self.n = n

    def __ne__(self, value): #__ne__() defines the behaviour of != operator
        return self.n != value.n

n1 = Number(23)
n2 = Number(99)

print(n1 != n2)

#Example
class Number:
    def __init__(self, n):
        self.n = n

    def __ne__(self, value):
        return self.n != value.n

n1 = Number(45)
n2 = Number(45)

print(n1 != n2)

#__floordiv__() overloading // operator: __floordiv__() is a special method used to define the
# behavior of the // (floor division) operator for objects.
class Number:
    def __init__(self, f):
        self.f = f

    def __floordiv__(self, other): #__floordiv__() defines the behaviour of // operator
        return self.f // other.f

f1 = Number(17)
f2 = Number(5)

print(f1 // f2)

#Example
class Number:
    def __init__(self, f):
        self.f = f

    def __floordiv__(self, other): 
        return self.f // other.f

f1 = Number(25)
f2 = Number(4)

print(f1 // f2)

#__str__(): __str__() is a special method used to define
# the human-readable string representation of an object.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #__str__() defines the human- readable string representation of object
        return f"Student name: {self.name}, Age: {self.age}"

s = Student("Scout", 28)
print(s)

#Example
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        return f"My name is {self.name} and I am doing {self.course}"

s = Student("Sonal", "BTech")
print(s)


#Example: Combining multiple concepts
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __eq__(self, value):
        return self.n == value.n

    def __str__(self):
        return f"{self.greet} {self.name}, Thanks for learning."

class Student:
    def __init__(self, greet, name):
        self.greet = greet
        self.name = name

    def __str__(self):
        return f"{self.greet} {self.name}, Thanks for learning."

n1 = Number(40)
n2 = Number(20)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 == n2)

s = Student("HELLO!", "Coder")
print(s)

#Uses of Operator Overloading: It makes operations on user-defined objects 
# more natural, readable, and intuitive.
# It is commonly used with mathematical objects, complex numbers, vectors, 
# matrices, money, dates, and other custom data types.