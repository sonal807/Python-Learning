#Inheritance in Python is a core pillar of Object-Oriented Programming (OOP) that allows a child class (derived class) to absorb all attributes and methods from a parent class (base class).
#It eliminates repetitive code, enforces structural organization, and mirrors real-world hierarchies.

class Employee:      #Parent class
    company = "ITC"
    def show(self):   #Parent class function which can be used by child class
        print("Hello! How are you?")

class Programmer(Employee):    #Child class(inherited class)
    company = "Infotech"       #If company was not mentioned here and we run b.company then the output will be ITC.
    def showlanguage(self):    #Child class function which can be use by only child class
        print("Namaste!")

a = Employee()
b = Programmer()
print(a.company, b.company)

a.show()
b.show()       #Parent class function can be used by child class
b.showlanguage()


#We take one more example to understand it.

class Animal:
    def speak(self):
        print("I can make a sound")

class Dog(Animal):
    def bark(self):
        print("Woof Woof")

d = Dog()
d.speak()
d.bark() 


#There are four types of inheritance:
#1- Single inheritance
#2- Multilevel Inheritance
#3- Multiple Inheritance
#4- Hierarchical Inheritance
#5- Hybrid Inheritance

#So here the examples we have used is a single inheritance
#where child class inherits from only one parent class. 