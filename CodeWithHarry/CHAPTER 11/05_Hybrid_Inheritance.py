#Hybrid Inheritance: Hybrid inheritance is a combination of two or more types of inheritance used together in the same class hierarchy.
#It can combine multiple, multilevel, hierarchical, or other inheritance patterns.

#Example-1 (Here we have used Hirarchical+Multiple)
class Vehicle:       # Base / Parent class
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):   # Car inherits from Vehicle
    def drive(self):
        print("Car is a type of vehicle")

class Bike(Vehicle):  # Bike also inherits from Vehicle
    def ride(self):
        print("Bike is a type of vehicle")

class ElectricVehicle(Car, Bike):  # ElectriVehicle inherits from both Car and Bike
    def hybrid_mode(self):
        print("Both Car and Bike comes in electric variant")

e = ElectricVehicle()

e.start()
e.drive()
e.ride()
e.hybrid_mode()

#Example-2 (Here we have used Hirarchical+Multiple)
class Employee:
    def work(self):
        print("Hello Employees!")

class Developer(Employee):
    def code(self):
        print("Hello! I am developer.")

class Manager(Employee):
    def manage(self):
        print("Hello! I am manager")

class TechLead(Developer, Manager):
    def lead(self):
        print("Hello! I'll guide developer and Manager")

t = TechLead()

t.work()
t.code()
t.manage()
t.lead()

#Example-3 (here we have use hierarchical+multilevel+multiple)
class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("Student is studying")

class Employee(Person):
    def work(self):
        print("Employee is working")

class CollegeStudent(Student):
    def attend_college(self):
        print("College Student is attending college")

class Teacher(Employee):
    def teach(self):
        print("Teacher is teaching")

class Researcher(CollegeStudent, Teacher):
    def research(self):
        print("Researcher is doing research")

r = Researcher()

r.introduce()
r.study()
r.work()
r.attend_college()
r.teach()
r.research()

#example-4 (here we have use hierarchical+multilevel+multiple)
class Device:
    def power_on(self):
        print("Device is poering on")

class Computer(Device):
    def run_program(self):
        print("Computer is running a program")

class Mobile(Device):
    def make_call(self):
        print("Making a call")

class Laptop(Computer):
    def carry(self):
        print("Laptop is easy to carry")

class Smartphone(Mobile):
    def use_app(self):
        print("Smartphone is running app")

class SmartDevice(Laptop, Smartphone):
    def connect_internet(self):
        print("Smart device is connected to the internet")

s = SmartDevice()

s.power_on()
s.run_program()
s.make_call()
s.carry()
s.use_app()
s.connect_internet()