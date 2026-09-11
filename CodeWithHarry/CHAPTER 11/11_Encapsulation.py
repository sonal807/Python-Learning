#Encapsulation:Encapsulation is the process of bundling data and the methods that operate on that data inside a single class, 
# while controlling how that data can be accessed or modified.
#Encapsulation = Data + Bunduling the methods in one class + Providing data access control

#Access Modifiers: Access modifiers are used to control the accessibility of attributes and methods within a class.
# In Python, they are mainly represented as Public, Protected, and Private.

#1- Public Access Modifiers: Public members are attributes and methods that can be accessed and modified directly from anywhere,
#both inside and outside the class.
#In pyhton the class attributes and methods are by default public.

class Car:
    def __init__(self):
        self.brand = "Toyota"

c = Car()
print(c.brand)

#Example-1
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Govind")

print(student.name) #self.name is public attribute so we can access it directly outside the class

student.name = "Rahul"
print(student.name) #we can also modify it

#Example-2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Satyam", 20000)

print(e1.name)
print(e1.salary)

#2- Protected Access Modifiers: Protected members are attributes and methods intended to be accessed within the class and its subclasses.
#In Python, it's just convention they are indicated by a single underscore (_) before the name.
class Vehicle:
    def __init__(self):
        self._engine = "Petrol"

class Bike(Vehicle):
    def show_engine(self):
        print("Engine type:", self._engine)

b = Bike()
b.show_engine()

print(b._engine)

#Important Concept First
#In python, self._engine is protected by convention
#⚠️That means - we are saying "pleasa don't access it from outside", but python won't stop you to access it from outside

#But in Java/C++:
#A protected variable cannot be accessed outside the class or subclass.

#Example: Accessing protected inside class
class Employee:
    def __init__(self, salary):
        self._salary = salary

    def show_salary(self):
        print(self._salary)

e1 = Employee(20000)

e1.show_salary()

#Example: Accessing protected in child class
class Employee:
    def __init__(self, salary):
        self._salary = salary

class Manager(Employee):
    def show_salary(self):
        print (self._salary)

m = Manager(50000)
m.show_salary()

#Example: Accessing protected outside class(convention, not strictly restriction)
class Employee:
    def __init__(self, salary):
        self._salary = salary

e1 = Employee(200000)
print(e1._salary) #accessing protected from out side (we should avoid to do that)

#Example
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

b1 = BankAccount(12345, 5000)

print(b1.account_number)
print(b1._balance) #generally we should avoid to do this


#3- Private Access Modifier:Private members are attributes and methods that are intended to be accessed only within the class.
#can only be accessed inside the class
#In Python, they are indicated by two underscores (__) before the name

class BankAccount:
    def __init__(self):
        self.__balance = 100000

    def get_balance(self):
        return self.__balance

acc = BankAccount()
print(acc.get_balance()) #If we use the private in method of same class then it will be accessed as the method doesn't know that the property is private
#print(acc.__balance)  #If we access private directly from out side it will show AttributeError

#Example:
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def show_salary(self):
        print(self.__salary)

e1 = Employee(2000)
e1.show_salary()

#print(e1.__salary)   #we can't access it outside class


#Private Variable: A private variable is a class variable whose name starts with two underscores (__).
#It is inteded to restrict direct access from outside the class and is mainly used to protect the internal data of an object.
class Employee:
    def __init__(self, salary):
        self.__salary = salary    #__salary is private variable

    def show_salary(self):
        print(self.__salary) #__salary is accessed here in same class

e1 = Employee(2000000)
e1.show_salary()


#Name Mangling: Name mangling is a mechanism in python that changes the name of a class member
#starting  with double underscores (__) by addin the class name as prefix.
#It's main purpose is to avoid the name clashes and to protect the double underscore members to be overrided/accessed accidently outside the class
class Employee:
    def __init__(self, salary):
        self.__salary = salary
        #Python will make internally self.__salary approximately to self._Employee__salary (this is called name mangling)

#⚠️ Name mangling is not actual security/private lock.
#If someone knows _Employee__salary so it can be technically accessed
class Employee:
    def __init__(self, salary):
        self.__salary = salary

e1 = Employee(2000000)
print(e1.__dict__)   #Output: {'_Employee__salary': 2000000}  we have written self.__salary = salary in class but python stores internally _Employee__salary (name mangling)
#print(e1.__salary)  #It will show error
print(e1._Employee__salary)   #It will give the output we want

#Example:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    def show_marks(self):
        print(f"Marks: {self.__marks}")

s1 = Student("Sunil", 67)
s1.show_marks()

## Getter and Setter
# Getter: A getter is a method used to access or retrieve the value of an attribute.
# It provides controlled access to an object's internal data.

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):   #Getter Method
        return self.__salary

e1 = Employee(200000)
print(e1.get_salary())

#Example
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s1 = Student("Sumit", 56)
print("Name:", s1.name)
print("Marks:", s1.get_marks())

#Setter: A setter is a method used to modify or update the value of an attribute.
# It provides controlled access to change an object's internal data.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):   #Getter method
        return self.__marks

    def set_marks(self, marks):  #Setter method
        self.__marks = marks

s1 = Student(56)
print(s1.get_marks())  #Used getter to read and access the value

s1.set_marks(80)
print(s1.get_marks())

#Setter with Validation: Setter validation is the process of checking whether a new value is valid before updating the attribute.
# It helps ensure that only acceptable values are assigned to an object's internal data.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):  #Setter doesn't only cahanges the value, it can also apply rules before changing
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

s1 = Student(67)
print(s1.get_marks())

s1.set_marks(89)
print(s1.get_marks())

s1.set_marks(159)
print(s1.get_marks())

#Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    #Getter
    def get_balance(self):
        return self.__balance

    #Setter
    def set_balance(self, amount):
        #Validation
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

acc = BankAccount(5000)
print("Current Balance:", acc.get_balance())

acc.set_balance(10000)
print("Updated balance:", acc.get_balance())

acc.set_balance(-2000)


#Encapsulation: Protecting data inside the class using private variables.

class BankAccount:
    def __init__(self):
        self.__balance = 0  #private

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(10000)
print(account.get_balance())  #safe access

#Property decorators and Encapsulation: Property decorators help implement Encapsulation 
#by providing controlled access to an object's internal data through properties. 
# They allow us to read, modify, or delete data while adding validation or other logic when required.
class Student:
    def __init__(self, name):
        self._name = name   #protected data

    @property               #it give controlled read access
    def name(self):
        return self._name
   
    @name.setter            #it gives controlled update access
    def name(self, value):
        self._name = value


#Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

account = BankAccount(5000)
print("Current Balance:", account.balance)

account.balance = 90000
print("Updated Balance:", account.balance)

account.balance = -5000
print("Final Balance:", account.balance)

#Encapsulation is the concept. 
# Private/internal variables, getters, setters, and property decorators are techniques used to 
# implement controlled access to that data.

#Example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Invalid Salary")

    def show_details(self):
        print(f"Employee name: {self.name} \nSalary: {self.salary}")

e1 = Employee("Rahul", 30000)

e1.show_details()
        
e1.salary = 40000
e1.show_details()

e1.salary = -20000
e1.show_details()