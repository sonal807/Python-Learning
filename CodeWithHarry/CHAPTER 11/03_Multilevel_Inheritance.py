#Multilevel Inheritance:Multilevel inheritance is a type of inheritance in which a class inherits from another class,
#which itself inherits from another class, forming a chain of inheritance.

# Base / Grandparent class
class Animal:     
    def eat(self):
        print("Animal is eating")

# Dog inherits from Animal
# Animal → Parent class of Dog
# Dog → Child class of Animal
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Puppy inherits from Dog
# Dog → Parent class of Puppy
# Puppy → Child class of Dog
# Puppy also gets the methods of Animal through Dog
class Puppy(Dog):
    def play(self):
        print("Puppy is playing")

# Creating an object of the last/child class
p = Puppy()

# Inherited from Animal (Grandparent class)
p.eat()
# Inherited from Dog (Parent class)
p.bark()
# Defined directly inside Puppy
p.play()

#Example-2
class School:
    school_name = "CPS School"
    def greet(self):
        print("Hello!")

class Class(School):
    Class = "10th"
    def show_school(self):
        print(f"\nMy School name is {self.school_name}\nAnd my class is {self.Class}")

class Student(Class):
    def show(self, name):
        self.name = name
        print(f"My name is {self.name}")

c = Class()
c.greet()
c.show_school()

s = Student()
s.greet()
s.show_school()
s.show("Puneet")

#Example-3
class Train:
    train_name = "Vandey Bharat"
    def show_train(self):
        print(f"This is a {self.train_name}")

class ExpressTrain(Train):
    def book_ticket(self):
        print("Ticket Booked")

class TrainSpeed(ExpressTrain):
    def show_speed(self):
        print("Speed of this train is 200 km/h.")

train = TrainSpeed()

train.show_train()
train.book_ticket()
train.show_speed()

#Example-4
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class SportCar(Car):
    def race(self):
        print("Sports car is racing")

s = SportCar()
s.start()
s.drive()
s.race()