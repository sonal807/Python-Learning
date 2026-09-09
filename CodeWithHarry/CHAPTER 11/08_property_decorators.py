# @property decorator: The @property decorator allows a method to be accessed like an attribute, without explicitly calling it with parentheses ().
# It is commonly used to control or calculate the value of an attribute while keeping a simple attribute-like interface.
# It is especially useful when we want that any calculated or controlled value looks like an attribute

#without @property
class Student:
    def get_name(self):
        return "Anil"

s = Student()
print(s.get_name()) #Method call

#With @property
class Student:
    @property
    def name(self):
        return "Amit"

s = Student()
print(s.name) #We have just accessed the method as an attribute


##Let's take one more example
#without @property
class Employee:
    def get_salary(self):
        return 200000

e = Employee()
print(e.get_salary())   #Method call

#with @property
class Employee:
    @property
    def get_salary(self):
        return 200000

e = Employee()
print(e.get_salary) #accessed the method like an attribute


#Example
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

s = Student("Sonal", "Rai")
print(s.full_name)

#Example
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

r = Rectangle(10, 5)
print(r.area)