#Abstraction:Abstraction is an OOP concept that hides unnecessary implementation details and exposes only the essential features of an object.
# It focuses on what an object does rather than how it does it.
#Show only essential feature and hide complex details.

#Abstraction = What to do, not How it is done.
#Encapsulation mainly controls access to data/implementation,
#while Abstraction hides unnecessary complexity and exposes only essential functionality.


#Abstract class: An abstract class is a class that is designed to be used as a blueprint for other classes.
#  It can define common methods and structure that child classes are expected to follow, 
# but it is generally not used to create objects directly.
#Abstract Class = Blueprint that defines what child classes should provide.

#ABC(Abstract Base Class):ABC stands for Abstract Base Class.
# It is a base class provided by Python's abc module that is used to create abstract classes.
# A class that inherits from ABC can define abstract methods that must be implemented by its child classes.
#ABC = Python ko batana ki “ye class ek Abstract Base Class hai.”

#Example
from abc import ABC  #Import ABC

class Shape(ABC): #Shape class is inheriting from ABC, which will make the Shape class defined as abstract base class
    pass

#@abstractmethod: @abstractmethod is a decorator used to declare a method as abstract inside an abstract class. 
# An abstract method defines a method that child classes are required to implement,
# while the abstract class itself does not provide the complete implementation.

#Example
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):  #Any class that inherits by shape class, has to provide/implement area()
        pass


#Example
from abc import ABC, abstractmethod

class Shape(ABC): #Can't create the object of abstract class

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Calculating Circle area")

c = Circle()
c.area()

#Example
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        print("Complex data")

class Car(Vehicle):
    def start(self):
        print("Car started")

v = Car()
v.start()

#Rule-1 Abstract class = blueprint, not a directly usable object (when it has abstract methods).
#Rule-2 If a child class does not implement all inherited abstract methods, it also remains abstract and cannot be instantiated.
#Rule-3 Abstract class will have abstract method(compulsary), but if we want we can also define normal methods

#Rule-4 Abstract class can have __init__() constructor
#Example
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    def display(self):
        print(f"Shape: {self.name}")

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        print("Calculating Circle area")


c = Circle("Circle", 5)

c.display()
c.area()


#Example
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Payment of₹{amount} made through UPI")

class Card(Payment):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made through Card")

upi = UPI()
card = Card()

upi.pay(5000)
card.pay(10000)

#Example
from abc import ABC, abstractmethod


class AIModel(ABC):

    def __init__(self, model_name):
        self.model_name = model_name

    @abstractmethod
    def predict(self, data):
        # Each child class must provide its own prediction logic.
        raise NotImplementedError

    def show_model(self):
        print(f"Model: {self.model_name}")


class ImageModel(AIModel):

    def predict(self, data):
        print(f"Image model is predicting for: {data}")


class TextModel(AIModel):

    def predict(self, data):
        print(f"Text model is predicting for: {data}")


class SpeechModel(AIModel):

    def predict(self, data):
        print(f"Speech model is predicting for: {data}")


image_model = ImageModel("ResNet")
text_model = TextModel("BERT")
speech_model = SpeechModel("Whisper")


image_model.show_model()
image_model.predict("cat image")

print()

text_model.show_model()
text_model.predict("Hello, how are you?")

print()

speech_model.show_model()
speech_model.predict("audio file")


#Example
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        raise NotImplementedError

    def show_name(self):
        print(f"Name: {self.name}")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team")

m = Manager("Rahul")

m.show_name()
m.work()

#Example
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, recipient):
        self.recipient = recipient

    @abstractmethod
    def send(self):
        raise NotImplementedError

    def show_recipient(self):
        print(f"Recipient: {self.recipient}")

class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending Notification through SMS")

email = EmailNotification("rahul@gmail.com")
sms = SMSNotification("9876543210")

email.show_recipient()
email.send()

sms.show_recipient()
sms.send()