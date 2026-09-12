#Polymorphism: Polymorphism is an OOP concept that allows the same method, function, or operator to
# perform different behaviors depending on the object or data it is used with.
#Polymorphism = "one thing, many forms"

#Simple Idea
class Dog:
    def speak(self):    #speak() method
        print("Bark")

class Cat:
    def speak(self):   #same speak method()
        print("Meow")

dog = Dog()
cat = Cat()

dog.speak() #it will give output bark
cat.speak() #it will give output meow (Same method name but different behaviour)

#Polymorphism = Same interface, different behaviour

#Example
class UPI:
    def pay(self):
        print("Payment through UPI")

class Card:
    def pay(self):
        print("Payment through Card")

class Cash:
    def pay(self):
        print("Payment through cash")

upi = UPI()
card = Card()
cash = Cash()

upi.pay()
card.pay()
cash.pay()
#methods are same but different object and behaviour are different

#Method Overriding: Method overriding is an OOP concept in which a child class provides its own
#implementation of a method that is already defined in its parent class.
#Method Overriding = Child class parent ke existing method ko same name se apne behavior ke according redefine karti hai.

class Animal:
    def speak(self):   #same method in child
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  #same method from parent
        print("Dog Barks")

d = Dog()
d.speak() #Method of parent is overrided by child

#Example:
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):  #method overiding
        print("Car is starting")

class Bike(Vehicle):
    def start(self):  #method overiding
        print("Bike is starting")

v = Vehicle()
c = Car()
b = Bike()

v.start()
c.start()
b.start()
#same method but for different obect it's showing different behaviour
#So, Method Overiding is an important way to achieve Polymorphism

#Example-2
class Animal:
    def sound(self):
        print("Animal Makes Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

d = Dog()
c = Cat()

d.sound()
c.sound()

#Method Overriding + super(): super() can be used in a child class to call the overridden method of its parent class 
#while still allowing the child class to provide its own behavior.

#Simple example
class Animal:
    def sound(self):  #same method
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):   #same method overided
        print("Dog barks")
        super().sound()  #It will call parent class method also

d = Dog()
d.sound()
#Child overrides own behaviour, by using super() it also reuse parent's behaviour.

#🦆Duck Typing: Duck typing is a Python concept where the type or class of an object
#is less important than the methods or behavior it provides.
#This means that if an object provides the required behavior, we can work with it without checking its exact type.

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

def make_sound(animal):  
    animal.sound()   #function doesn't need to check that animal is cat or dog

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
#Behviour is more important tha object type

#Duck Typing- real world example
class UPI:
    def pay(self):
        print("Paymnet made using UPI")

class Card:
    def pay(self):
        print("Payment made using card")

def make_payment(payment_method):
    payment_method.pay()

upi = UPI()
card  = Card()

make_payment(upi)
make_payment(card)
#function doesn't need to check that payment_method is UPI or Card, if object has pay() method then it will work with it

#Example
class Car:
    def start(self):
        print("Car is starting")

class Bike:
    def start(self):
        print("Bike is starting")

def start_vehicle(vehicle):
    vehicle.start()

car = Car()
bike = Bike()

start_vehicle(car)
start_vehicle(bike)

#Method Overloading: Method Overloading is an OOP concept in which multiple methods have the same name but different parameters,
# allowing the same method name to perform different tasks depending on the arguments provided.

# 🧠 Important Python Point
# Languages like Java/C++ directly support traditional method overloading:
# add(int, int)
# add(int, int, int)

# But Python does not support traditional method overloading.

# If you define the same method multiple times inside a class, the latest definition replaces the previous one.

# Instead, Python achieves similar behavior using techniques such as:
# Default arguments
# *args
# **kwargs

#Default Arguments and Method Overloading in Python:
#Python does not support traditional method overloading, where multiple methods with the same name can be defined with different parameters.
# However, we can achieve similar behavior using default arguments. 
# A default argument is a parameter that is assigned a default value when no value is provided during the function or method call.
# This allows the same method to work with different numbers of arguments.
class Calculator:
    def add(self, a, b=0): #a -> required argument, b=0 -> optional argument
        return a + b

c = Calculator()

print(c.add(5))  #b is not given so b= 0; 5+0
print(c.add(5, 10)) #a and b both are given; 5+10

#Example
class Calculator:
    def multiply(self, a, b=1):    #b has a default value of 1
        return a * b

c = Calculator()

print(c.multiply(2))  #b is not provided, Python uses the default value
print(c.multiply(2,20))  #provides a value for b, so Python uses 20

#*args and Method Overloading in Python:
#*args allows a Python function or method to accept a variable number of positional arguments. 
# It collects all the extra positional arguments into a tuple, allowing a single method to handle different numbers of arguments. 
# This can be used to achieve behavior similar to method overloading in Python

#Simply *args ka main purpose hai ki method ko pata na ho ki kitne positional arguments milenge, 
# phir bhi woh unhe accept kar sake.
class Calculator:
    def add(self, *args):
        return sum(args)

c = Calculator()

print(c.add(4))
print(c.add(12, 18))
print(c.add(10, 5, 25))

#Example with strings
class Message:
    def combine(self, *args):
        return " ".join(args)

m = Message()

print(m.combine("Hello"))
print(m.combine("Hello", "World!"))
print(m.combine("Python", "Is", "Easy"))

#Example
class Student:
    def show_subjects(self, *args):
        for subject in args:
            print(f"Subject: {subject}")

s = Student()

s.show_subjects("Python")
s.show_subjects("Python", "SQL")
s.show_subjects("Python", "SQL", "AI", "IoT")

#Example
class ShoppingCart:
    def calculate_total(self, *prices):
        total = sum(prices)
        print(" + ".join(map(str, prices)), "=", total)
        if total >= 5000:
            discount = total * 10 / 100
            discounted_price = total - discount

            print(f"10% discount = {discount:g}")
            print(f"Final amount = {discounted_price:g}")
        else:
            print(f"No discount → {total:g}")

cart = ShoppingCart()

cart.calculate_total(1200, 800)
print()

cart.calculate_total(2000, 1500, 1000)
print()

cart.calculate_total(3000, 2500, 1000)


#**kwargs and Method Overloading in Python:
#**kwargs allows a Python function or method to accept a variable number of keyword arguments.
# It collects all the keyword arguments into a dictionary, allowing a single method to handle different numbers of named arguments.
#  This can be used to achieve behavior similar to method overloading in Python.

#*args → positional arguments → tuple
#**kwargs → keyword arguments → dictionary

class Student:
    def show_details(self, **kwrgs):
        print(kwrgs)   #store the items in list
        print(type(kwrgs))   #show that the kwrgs is of dict type

s = Student()

s.show_details(name = "Sonal", age = 24) #OUTPUT: {'name': 'Sonal', 'age': 24}

#**kwrgs stores arguments in list. So, we can access the value like we do in dictionary
class Student:
    def show_details(self, **kwargs):
        for key, value in kwargs.items(): #kwargs gives result in form of key-value pair, so this for loop acess key and it's value one by one in 
            print(f"{key}: {value}")

s = Student()

s.show_details(name= "Sonal", age = 34, course = "python") #**kwargs collects these arguments in list


#Example
class Employee:
    def show_details(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

e = Employee()

e.show_details(name="Rahul", age=25, salary=30000)

e.show_details(name="Aman", department="IT")

e.show_details(name="Priya", age=22, department="AI", city="Lucknow")

#Example
class Employee:
    def calculate_salary(self, **kwargs):

        salary = kwargs.get("salary", 0)
        bonus = kwargs.get("bonus", 0)
        tax = kwargs.get("tax", 0) 

        gross_salary = salary + bonus

        tax_amount = gross_salary * tax / 100

        final_salary = gross_salary + tax_amount

        print(f"Basic Salary: {salary:g}")
        print(f"Bonus: {bonus:g}")
        print(f"Gross Salary: {gross_salary:g}")
        print(f"Tax: {tax_amount:g}")
        print(f"Final Salary: {final_salary:g}")

e = Employee()

e.calculate_salary(
    salary=30000,
    bonus=5000,
    tax=10
)

print()

e.calculate_salary(
    salary=40000,
    bonus=8000
)

print()

e.calculate_salary(
    salary=25000,
    tax=5
)

#Example:
class Student:
    def show_details(self, **kwargs):

        name = kwargs.get("name")
        age = kwargs.get("age")
        course = kwargs.get("course", "Not specified")

        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Course: {course}")


s = Student()

s.show_details(name="Rahul", age=20, course="Python")

s.show_details(name="Aman", age=22)


#Defining same method multiple times:
#In Python, defining multiple methods with the same name inside a class does not create traditional method overloading.
#The latest method definition replaces the previous one, so only the last definition remains available.

class Calculator:
    def add(self, a, b):  #first method
        return a + b

    def add(selff, a, b, c):  #Second method; it will replace the first method
        return a + b + c

c = Calculator()

# print(c.add(4, 6))   #It will give error as its on first method and will show positional argument c as its been replaced by seconf method
print(c.add(6, 7, 9))  #This will run successfully

#Example
class Employee:
    def show_info(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"Name: {self.name}, Salary: {self.salary}")

    def show_info(self, name , salary, department):
        self.name = name
        self.salary = salary
        self.department = department

        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

e = Employee()

# e.show_info("Rahul", 30000) #error
e.show_info("Rahul", 30000, "IT")


#Polymoephism with Built-in functions: Polymorphism with built-in functions means that the same built-in function can perform
#different operations depending on the type of object or data it is used with.
#Same built-in function → different objects → different behavior

#Example: len() with user-defined objects
class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)

s = Student("Rahul", ["Python", "SQL", "AI"])

print(len(s.name))   #it will get the length of "Python"
print(len(s.subjects)) #It will get the length of ["Python", "SQL", "AI"]
print(len(s))  #and it will return len(self.subjects) passed in method.

#Example
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages


b = Book("Python Programming", 350)

print(len(b))

#Example: built-in function sum()
# The sum() built-in function can work with different iterable objects containing numeric values and calculate their total.
# Its behavior depends on the type and structure of the data provided to it.

class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices

    def total(self):
        return sum(self.prices)

cart1 = ShoppingCart([100, 200, 300])  #passed list
cart2 = ShoppingCart((500, 1000, 1500))  #passed tuple
 
print(cart1.total())
print(cart2.total()) 
#Same function → different types of data → appropriate behavior

#print() + __str__() and Polymorphism:
# The __str__() method defines the human-readable string representation of an object. 
# When an object is passed to the built-in print() function, Python uses __str__() to determine what should be displayed. 
# This allows print() to behave appropriately for user-defined objects.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}"


s1 = Student("Rahul", 20, "Python")
s2 = Student("Priya", 22, "AI")

print(s1)
print(s2)
#Same print() function → different types of objects → appropriate representation

#Example:
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Category: {self.category}"

p1 = Product("Laptop", 55000, "Electronics")
p2 = Product("Shoes", 2500, "Fashion")

print(p1)
print(p2)


#Final polymorphism practice
class UPI:
    def pay(self):
        print("Paymnet made using UPI")

class Card:
    def pay(self):
        print("Payment made using card")

class Cash:
    def pay(self):
        print("Payment made using cash")

def make_payment(payment_method):
    payment_method.pay()

upi = UPI()
card  = Card()
cash = Cash()

make_payment(upi)
make_payment(card)
make_payment(cash)


#Example
class Notification:
    def send(self, message):
        print("Sending notification")

class EmailNotification(Notification):
    def send(self, message):
        super().send(message)
        print(f"Email: {message}")

class SmsNotification(Notification):
    def send(self, message):
        super().send(message)
        print(f"SMS: {message}")

class PushNotification(Notification):
    def send(self, message):
        super().send(message)
        print(f"Push Notification: {message}")

def send_notification(notification, message):
    notification.send(message)


email = EmailNotification()
sms = SmsNotification()
push = PushNotification()

send_notification(email, "Your order has been shipped")
send_notification(sms, "Your order has been shipped")
send_notification(push, "Your order has been shipped")

#In this we have used:
# - Inhertance
# - Method Overloading()
# - super()
# - Duck typing
# - Polymorphism