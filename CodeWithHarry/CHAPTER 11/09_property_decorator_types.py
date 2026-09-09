#Types of @property decorator

#1- @property(Getter): A getter is a method used to access or retrieve the value of an attribute.
#In Python, the @property decorator is commonly used to create a getter.

class Student:
    def __init__(self, name):
        self._name = name

    @property    #It is used for getter also
    def name(self):
        return self._name

s = Student("Rahul")
print(s.name)

#2- <property>.setter: A setter is a method used to modify or update the value of a property.
#In Python, a setter is defined using the @property_name.setter decorator.
#Getter reads the value and Setter changes or updates the value.

class Rectangle:
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

r = Rectangle(10)
print(r.length)

r.length = 20
print(r.length)

#Very useful feature of setter is that we can check or validate the value before setting it
class Rectangle:
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            print("Length must be positive")

r = Rectangle(10)
print(r.length)

r.length = 20
print(r.length)

r.length = -5
print(r.length)


#3- <property>.deleter: A deleter is a method used to define what happens when a property is deleted using the del statement.
# A deleter is used to define the behavior of a property when it is deleted using the del statement.
# It is defined using the @property_name.deleter decorator.
# Getter → Read
# Setter → Update
# Deleter → Delete

class Student:
    def __init__(self, name):
        self._name = name

    @property         #Read getter value
    def name(self):
        return self._name

    @name.deleter     #Defines what to do if property gets deleted
    def name(self):
        del self._name   #Delets actual stored value

s = Student("Rohan")
print(s.name)

del s.name  #It triggers the deleter
#print(s.name)  #If we try to print it will show AttributeError

#Example (Getter + Setter + Deleter)
class Train:

    def __init__(self, train_name):
        self._train_name = train_name

    # Getter
    @property
    def train_name(self):
        return self._train_name

    # Setter
    @train_name.setter
    def train_name(self, new_name):
        if new_name:
            self._train_name = new_name
        else:
            print("Train name cannot be empty")

    # Deleter
    @train_name.deleter
    def train_name(self):
        del self._train_name


t = Train("Vande Bharat")

# Getter
print(t.train_name)

# Setter
t.train_name = "Rajdhani Express"
print(t.train_name)

# Deleter
del t.train_name


## NOTE: Property decorators are commonly used in Encapsulation to provide controlled access to an object's internal data.
#They allow us to read, modify, or delete data while adding validation or other logic when needed. 
#They let you validate or compute values while allowing users of your class to use simple attribute syntax (obj.attribute) 
#instead of method calls (obj.get_attribute()).
#The detailed concept of Encapsulation will be covered separately.