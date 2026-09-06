#Object oriented programming (OOP) is a programming paradigm where we create objects and classes.
# It helps organize code , makes it reusable and is widely used in python projects .

#CLASS: A class is a blueprint/template for creating objects.
#OBJECTS: An object is an actual instance created from a class.

class Employee: #class
    name = "Anuj"
    language = "Hindi"
    salary = 12000

info = Employee() #object
print(info.name, info.salary)
#Basic ways to create a class and object

class Employee: 
    language = "Hindi"#class attribute
    salary = 12000

anuj = Employee() 
anuj.name = "Anuj" #object attribute
print(anuj.name, anuj.language, anuj.salary)

rohan = Employee()
rohan.name = "Rohan" 
print(rohan.name, rohan.language, rohan.salary)