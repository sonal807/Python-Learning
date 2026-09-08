#Hierarchical_Inheritance: Hierarchical inheritance is a type of inheritance in which multiple child classes inherit from a single parent class.

#Example-1
class Animal:         #Parent class
    def sound(self):
        print("Animals makes sound.")

class Dog(Animal):    #First child class inherits parent class
    def bark(self):
        print("Dog Barks. Woof Woof!")

class Cat(Animal):    #Second child class also inherits parent class
    def meows(self):
        print("Cat Meows. Meow Meow!")

d = Dog()   #Obejct for first child class
c = Cat()   #Obejct for second child class

d.sound()
d.bark()

c.sound()
c.meows()

#Example-2
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("We drive a car")

class Bike(Vehicle):
    def ride(self):
        print("We ride a bike")

c = Car()
b = Bike()

c.start()
c.drive()

b.start()
b.ride()