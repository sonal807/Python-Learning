#Create a class 'Pets' from a class 'Animal' and further create a class 'Dog' from 'Pets'.
#Add a method 'bark' to class 'Dog'.

class Animal:
    def __init__(self):
        print("Hi I am animal")

class Pets(Animal):
    def view(self):
        print("Some animals are pet animals")

class Dog(Pets):
    def bark(self):
        print("Woof woof")

d = Dog()
d.bark()

#2nd way
class Animal:
    def __init__(self):
        print("Hi I am animal")

class Pets(Animal):
    def __init__(self):
        super().__init__()
        print("Some animals are pet animals")

class Dog(Pets):
    def __init__(self):
        super().__init__()
        print("I am a Dog")

    def bark(self):
        print("Woof woof")

d = Dog()
d.bark()