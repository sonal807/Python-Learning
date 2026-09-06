# 📘 Chapter 10 - OOP Basics (Object-Oriented Programming)

## 🎯 Objective

The objective of this chapter is to understand the **fundamentals of Object-Oriented Programming (OOP)** in Python.

In this chapter, we learn how Python allows us to organize programs using **classes and objects**.

The main concepts covered are:

- Object-Oriented Programming
- Classes
- Objects
- Attributes
- Instance Attributes
- Class Attributes
- Methods
- Instance Methods
- `self`
- Static Methods
- `@staticmethod` Decorator
- Constructors
- `__init__()` Method
- Creating and initializing objects
- Difference between class and object
- Difference between instance and class attributes
- Basic OOP structure
- Real-life applications of OOP
- Best practices and common beginner mistakes

---

# 📌 Topics Covered

1. What is OOP?
2. Why do we need OOP?
3. Procedural Programming vs OOP
4. What is a Class?
5. What is an Object?
6. Class as a Blueprint
7. Creating a Class
8. Creating Objects
9. Accessing Class Members
10. Attributes
11. Instance Attributes
12. Class Attributes
13. Instance Methods
14. `self`
15. Constructors
16. `__init__()` Method
17. Static Methods
18. `@staticmethod` Decorator
19. Instance Attributes vs Class Attributes
20. Class vs Object
21. Methods vs Attributes
22. Object Creation Process
23. Multiple Objects
24. Real-Life Applications
25. Common Beginner Mistakes
26. Best Practices
27. Quick Revision Tables
28. Key Takeaways
29. Summary

---

# 🧠 What is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a programming approach in which programs are designed around **objects and classes**.

Instead of writing a program only as a collection of functions and statements, OOP allows us to combine:

- Data
- Functions that operate on that data

inside objects.

For example, consider a student.

A student may have:

```text
Name
Roll Number
Age
Course
```

These are the student's **data/attributes**.

The student may also perform actions such as:

```text
Study
Attend Class
Take Exam
Display Details
```

These can be represented using **methods**.

OOP allows us to model such real-world entities in our programs.

---

# ❓ Why Do We Need OOP?

As programs become larger, managing everything using simple variables and functions can become difficult.

For example, suppose we want to store information about 100 students.

Without OOP, we may end up creating many separate variables:

```python
student1_name = "Aarav"
student1_roll = 101

student2_name = "Meera"
student2_roll = 102

student3_name = "Kabir"
student3_roll = 103
```

This approach becomes difficult to manage as the program grows.

With OOP, we can create one `Student` class and then create multiple student objects.

```python
class Student:
    pass
```

Then:

```python
student1 = Student()
student2 = Student()
student3 = Student()
```

Each object can represent a different student.

This makes the program more organized and easier to maintain.

---

# ⭐ Advantages of OOP

Object-Oriented Programming provides several advantages.

### 1. Organization

Related data and behavior can be grouped together.

### 2. Reusability

A class can be used to create many objects.

### 3. Maintainability

Large programs become easier to understand and modify.

### 4. Modularity

Different classes can represent different parts of a system.

### 5. Real-World Modeling

Real-world entities can be represented naturally using objects.

### 6. Scalability

OOP provides a structured foundation for developing larger applications.

---

# 🆚 Procedural Programming vs OOP

### Procedural Programming

Procedural programming mainly focuses on:

```text
Functions
↓
Statements
↓
Data
```

Example:

```python
name = "Aarav"
age = 20

def display():
    print(name)
    print(age)

display()
```

---

### Object-Oriented Programming

OOP focuses on:

```text
Class
 ↓
Objects
 ↓
Attributes + Methods
```

Example:

```python
class Student:

    def display(self):
        print("Student details")


student = Student()

student.display()
```

---

# 📦 What is a Class?

A **class** is a blueprint or template used to create objects.

A class defines what an object should contain and what it should be able to do.

For example:

```python
class Student:
    pass
```

Here:

```text
Student
```

is the name of the class.

The class itself does not represent one particular student.

It provides a structure from which student objects can be created.

---

# 🏠 Class as a Blueprint

A useful real-life analogy is a **house blueprint**.

Suppose an architect creates a blueprint containing:

```text
Number of rooms
Doors
Windows
Kitchen
Bathroom
```

The blueprint itself is not an actual house.

It describes how a house should be built.

Similarly:

```python
class Student:
    pass
```

is a blueprint for creating student objects.

Objects are the actual instances created from that class.

---

# 🧱 Creating a Class

The basic syntax is:

```python
class ClassName:
    # class body
    pass
```

Example:

```python
class Student:
    pass
```

### Important Points

- The `class` keyword is used to define a class.
- `Student` is the class name.
- The class body contains attributes and methods.
- `pass` can be used when the class body is empty.

---

# 📦 What is an Object?

An **object** is an instance of a class.

If a class is a blueprint, an object is an actual entity created using that blueprint.

Example:

```python
class Student:
    pass

student1 = Student()
```

Here:

```text
Student → Class
student1 → Object
```

The object `student1` is an instance of the `Student` class.

---

# 🔨 Creating an Object

The general syntax is:

```python
object_name = ClassName()
```

Example:

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

Here:

```text
Student → Class
student1 → Object
student2 → Object
```

Both objects are created from the same class.

---

# 🔗 Class and Object Relationship

The relationship can be visualized as:

```text
              CLASS
          ┌─────────────┐
          │   Student   │
          └──────┬──────┘
                 │
        ┌────────┴────────┐
        ↓                 ↓
    student1           student2
     Object              Object
```

One class can be used to create many objects.

---

# 🏷 What are Attributes?

**Attributes** are variables associated with a class or object.

They represent the **data or characteristics** of an object.

For example, a student may have:

```text
Name
Age
Roll Number
Course
```

These can be represented as attributes.

Example:

```python
class Student:

    name = "Aarav"
    age = 20
```

Here:

```text
name → Attribute
age  → Attribute
```

---

# 👤 Instance Attributes

An **instance attribute** belongs to a particular object.

Different objects can have different values for their instance attributes.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now create two objects:

```python
student1 = Student("Aarav", 20)
student2 = Student("Meera", 21)
```

Here:

```text
student1.name → Aarav
student1.age  → 20

student2.name → Meera
student2.age  → 21
```

The values are different for different objects.

Therefore:

```text
self.name
self.age
```

are instance attributes.

---

# 🏷 Class Attributes

A **class attribute** is an attribute that belongs to the class itself and is generally shared by all instances.

Example:

```python
class Student:

    college = "ABC University"
```

Now:

```python
student1 = Student()
student2 = Student()
```

Both objects can access:

```python
print(student1.college)
print(student2.college)
```

Output:

```text
ABC University
ABC University
```

The `college` attribute is defined at the class level.

---

# 🔄 Instance Attributes vs Class Attributes

Consider:

```python
class Student:

    college = "ABC University"

    def __init__(self, name):
        self.name = name
```

Here:

```text
college → Class Attribute
name    → Instance Attribute
```

`college` is common to students, while `name` is specific to each student.

---

# 📊 Instance Attribute vs Class Attribute

| Feature | Instance Attribute | Class Attribute |
|---|---|---|
| Belongs to | Object/instance | Class |
| Usually created | Inside methods such as `__init__()` | Directly inside class |
| Value | Can differ between objects | Common/shared by instances unless overridden |
| Access | `object.attribute` | `Class.attribute` or often `object.attribute` |
| Example | `self.name` | `college` |

---

# 🔍 Accessing Class Attributes

A class attribute can be accessed through the class:

```python
class Student:

    college = "ABC University"

print(Student.college)
```

Output:

```text
ABC University
```

It can also generally be accessed through an object:

```python
student1 = Student()

print(student1.college)
```

Output:

```text
ABC University
```

---

# 🔍 Accessing Instance Attributes

Instance attributes are accessed through an object.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Aarav")

print(student1.name)
```

Output:

```text
Aarav
```

---

# 🧩 What is a Method?

A **method** is a function defined inside a class.

Methods describe the **behavior or actions** associated with objects.

Example:

```python
class Student:

    def study(self):
        print("Student is studying.")
```

Now create an object:

```python
student1 = Student()

student1.study()
```

Output:

```text
Student is studying.
```

Here:

```text
study() → Method
student1 → Object
```

---

# 👤 Instance Methods

An **instance method** is a method that works with a particular object.

It normally receives `self` as its first parameter.

Example:

```python
class Student:

    def display(self):
        print("Student details")


student1 = Student()

student1.display()
```

Here:

```python
def display(self):
```

is an instance method.

---

# 🔑 What is `self`?

`self` refers to the **current object/instance**.

It allows an instance method to access the attributes and methods belonging to that particular object.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

Create an object:

```python
student1 = Student("Aarav")

student1.display()
```

Output:

```text
Aarav
```

Here:

```python
self.name
```

refers to the `name` attribute of the current object.

---

# 🧠 Understanding `self` with Multiple Objects

Consider:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

Now:

```python
student1 = Student("Aarav")
student2 = Student("Meera")

student1.display()
student2.display()
```

Output:

```text
Aarav
Meera
```

When:

```python
student1.display()
```

is called, `self` refers to `student1`.

When:

```python
student2.display()
```

is called, `self` refers to `student2`.

Therefore:

```text
student1 → self
student2 → self
```

depending on which object calls the method.

---

# 📌 Important Rule About `self`

`self` is not a special Python keyword.

It is a conventional name used for the current instance.

However, following the convention is strongly recommended.

Prefer:

```python
def display(self):
```

rather than using another name.

---

# 🏗 What is a Constructor?

A **constructor** is a special method that is used to initialize an object when it is created.

In Python, the commonly used constructor method is:

```python
__init__()
```

It runs automatically when an object is created.

---

# ⚙️ `__init__()` Method

The `__init__()` method is used to initialize instance attributes.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

When we create an object:

```python
student1 = Student("Aarav", 20)
```

Python automatically calls:

```python
__init__()
```

with the supplied arguments.

---

# 🔄 How `__init__()` Works

Consider:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Creating:

```python
student1 = Student("Aarav", 20)
```

initializes:

```text
student1.name = "Aarav"
student1.age = 20
```

Therefore, we can later access:

```python
print(student1.name)
print(student1.age)
```

Output:

```text
Aarav
20
```

---

# 🧱 Constructor Without Parameters

A constructor can also be written without additional parameters.

Example:

```python
class Student:

    def __init__(self):
        self.name = "Aarav"
        self.age = 20
```

Now:

```python
student1 = Student()

print(student1.name)
print(student1.age)
```

Output:

```text
Aarav
20
```

---

# 🧑‍🎓 Constructor with Parameters

A more flexible approach is to accept values while creating the object.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now:

```python
student1 = Student("Aarav", 20)
student2 = Student("Meera", 21)
```

Each object receives its own values.

---

# 📊 Constructor Example

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Rahul", 30000)
employee2 = Employee("Priya", 40000)

print(employee1.name)
print(employee1.salary)

print(employee2.name)
print(employee2.salary)
```

Output:

```text
Rahul
30000
Priya
40000
```

---

# ⚡ Constructor vs Normal Method

| Feature | `__init__()` | Normal Method |
|---|---|---|
| Purpose | Initialize object | Perform an action |
| Called automatically during normal object creation | ✅ | ❌ |
| Commonly used for | Initializing attributes | Object behavior |
| Example | `__init__()` | `display()` |

---

# 🧠 Important Note About `__init__()`

`__init__()` is commonly called the constructor in beginner-level Python explanations because it initializes newly created objects.

Technically, object creation and initialization are separate stages in Python, but for practical beginner OOP learning, it is appropriate to understand `__init__()` as the method used to initialize an object's state.

---

# 🧮 Static Methods

A **static method** is a method that does not need access to a particular object or instance.

It is defined using the:

```python
@staticmethod
```

decorator.

Example:

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
```

It can be called using the class:

```python
print(Calculator.add(10, 20))
```

Output:

```text
30
```

---

# 🏷 `@staticmethod` Decorator

`@staticmethod` tells Python that the method should behave as a static method.

Example:

```python
class Calculator:

    @staticmethod
    def multiply(a, b):
        return a * b
```

Calling it:

```python
result = Calculator.multiply(5, 4)

print(result)
```

Output:

```text
20
```

---

# 🔍 Static Method and `self`

A static method does **not require `self`**.

Instance method:

```python
class Student:

    def display(self):
        print("Student")
```

Static method:

```python
class Student:

    @staticmethod
    def message():
        print("Welcome to the course")
```

Notice that the static method does not have `self`.

---

# 🆚 Instance Method vs Static Method

| Feature | Instance Method | Static Method |
|---|---|---|
| Uses `self` | Usually yes | No |
| Works with object state | Yes | Not inherently |
| Decorator | Not required | `@staticmethod` |
| Called using object | Yes | Possible |
| Called using class | Possible but instance methods need an instance | Yes |
| Best use | Object-specific behavior | Utility/helper behavior related to the class |

---

# 💡 When Should We Use a Static Method?

A static method is useful when a function is logically related to a class but does not need information from a particular object.

Example:

```python
class MathOperations:

    @staticmethod
    def square(number):
        return number * number
```

The method does not need:

```python
self
```

because it does not depend on any object's attributes.

We can simply use:

```python
print(MathOperations.square(5))
```

Output:

```text
25
```

---

# 🧩 Complete OOP Example

The following example combines several concepts learned in this chapter:

```python
class Student:

    college = "ABC University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", self.college)

    @staticmethod
    def welcome():
        print("Welcome to the Student Management System")


student1 = Student("Aarav", 20)

student1.display()

Student.welcome()
```

Output:

```text
Name: Aarav
Age: 20
College: ABC University
Welcome to the Student Management System
```

### Concepts used:

```text
Student
   ↓
Class

student1
   ↓
Object

college
   ↓
Class Attribute

name, age
   ↓
Instance Attributes

display()
   ↓
Instance Method

self
   ↓
Current Object

__init__()
   ↓
Object Initialization

welcome()
   ↓
Static Method
```

---

# 🔄 Creating Multiple Objects

One of the major benefits of classes is that we can create multiple objects using the same class.

Example:

```python
class Student:

    college = "ABC University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age, self.college)


student1 = Student("Aarav", 20)
student2 = Student("Meera", 21)
student3 = Student("Kabir", 19)

student1.display()
student2.display()
student3.display()
```

Each object has its own instance data.

---

# 🧠 Object State

The **state of an object** refers to the values stored in its attributes at a particular time.

For example:

```python
student1 = Student("Aarav", 20)
```

The object's state includes information such as:

```text
name = Aarav
age = 20
```

Another object may have:

```text
name = Meera
age = 21
```

Therefore, different objects created from the same class can have different states.

---

# ⚙️ Object Behavior

The **behavior of an object** is represented by its methods.

For example:

```python
class Student:

    def study(self):
        print("Student is studying.")

    def attend_class(self):
        print("Student is attending class.")
```

Here:

```text
study()         → Behavior
attend_class()  → Behavior
```

Therefore:

```text
Attributes → State / Data

Methods → Behavior / Actions
```

---

# 📊 Class vs Object

| Feature | Class | Object |
|---|---|---|
| Meaning | Blueprint/template | Instance of a class |
| Represents | General structure | Specific entity |
| Created using | `class` keyword | `ClassName()` |
| Contains | Attributes and methods | Actual object state |
| Example | `Student` | `student1` |

Easy way to remember:

```text
Class  → Blueprint
Object → Actual instance
```

---

# 📊 Attributes vs Methods

| Feature | Attributes | Methods |
|---|---|---|
| Represents | Data/state | Behavior/action |
| Usually | Variables | Functions inside class |
| Example | `name`, `age` | `display()` |
| Access | `student.name` | `student.display()` |

---

# 📊 Instance vs Class Members

| Member | Instance | Class |
|---|---|---|
| Attribute | `self.name` | `college` |
| Belongs to | Particular object | Class |
| Can vary per object | ✅ | Usually shared |
| Example | Student name | College name |

---

# 🔄 Object Creation Process

When we write:

```python
student1 = Student("Aarav", 20)
```

conceptually, the process involves:

```text
Student class
      ↓
Object is created
      ↓
__init__() is called
      ↓
Arguments are passed
      ↓
Instance attributes are initialized
      ↓
student1 becomes a reference to the object
```

The object can then be used through:

```python
student1
```

---

# 🧠 Important Concept: Class Attribute Lookup

Suppose:

```python
class Student:

    college = "ABC University"
```

and:

```python
student1 = Student()
```

When we write:

```python
student1.college
```

Python can find `college` on the class if it is not found as an instance attribute.

This is why an object can access a class attribute.

---

# ⚠️ Changing a Class Attribute

Consider:

```python
class Student:

    college = "ABC University"
```

If we change the attribute through the class:

```python
Student.college = "XYZ University"
```

then instances that rely on the class attribute can observe the new class-level value.

Example:

```python
student1 = Student()
student2 = Student()

Student.college = "XYZ University"

print(student1.college)
print(student2.college)
```

Output:

```text
XYZ University
XYZ University
```

---

# ⚠️ Instance Attribute Can Shadow a Class Attribute

Consider:

```python
class Student:

    college = "ABC University"
```

Now:

```python
student1 = Student()

student1.college = "XYZ University"
```

Here, an instance attribute named `college` is created for `student1`.

Therefore:

```python
print(student1.college)
```

gives:

```text
XYZ University
```

while another object that does not have its own `college` attribute can still use the class attribute.

Example:

```python
student2 = Student()

print(student2.college)
```

Output:

```text
ABC University
```

This demonstrates that an instance attribute can **shadow** a class attribute with the same name.

---

# 🌍 Real-Life Applications of OOP

OOP is used extensively in software development.

### 🎓 1. Student Management System

Classes:

```text
Student
Teacher
Course
Exam
```

Objects can represent individual students, teachers, and courses.

---

### 🏦 2. Banking System

Classes:

```text
BankAccount
Customer
Transaction
Loan
```

Objects can represent individual accounts and customers.

---

### 🛒 3. E-Commerce System

Classes:

```text
Product
Customer
Cart
Order
Payment
```

---

### 🚗 4. Vehicle Management

Classes:

```text
Car
Bike
Truck
Driver
```

Objects can represent individual vehicles.

---

### 🎮 5. Games

Classes:

```text
Player
Enemy
Weapon
Game
Score
```

---

### 🤖 6. AI and Machine Learning Software

OOP is also widely used in Python libraries and frameworks.

Classes can represent:

```text
Models
Datasets
Layers
Optimizers
Configurations
```

---

### 🏥 7. Hospital Management System

Classes:

```text
Patient
Doctor
Appointment
Medicine
Hospital
```

---

# 💡 Best Practices

## 1. Use Meaningful Class Names

Prefer:

```python
class Student:
    pass
```

instead of:

```python
class S:
    pass
```

Use names that clearly describe what the class represents.

---

## 2. Follow Class Naming Conventions

Python convention generally uses **PascalCase** for class names.

Examples:

```python
class Student:
    pass

class BankAccount:
    pass

class EmployeeRecord:
    pass
```

---

## 3. Use `self` Consistently

For instance methods, use:

```python
def display(self):
```

and access instance attributes using:

```python
self.name
```

---

## 4. Initialize Object Data in `__init__()`

When an attribute is part of the object's initial state, initialize it clearly inside `__init__()`.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## 5. Use Class Attributes for Shared Information

If a value is conceptually common to the class, a class attribute may be appropriate.

Example:

```python
class Student:

    college = "ABC University"
```

---

## 6. Use Instance Attributes for Object-Specific Data

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Each student can have a different name.

---

## 7. Use Static Methods for Independent Utility Behavior

If a method does not need `self` or object state, consider whether `@staticmethod` is appropriate.

Example:

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
```

---

## 8. Keep Classes Focused

A class should represent a meaningful concept and avoid becoming responsible for unrelated tasks.

For example:

```text
Student → Student-related data and behavior
BankAccount → Banking-related data and behavior
```

---

# ⚠️ Common Beginner Mistakes

## 1. Confusing Class and Object

Incorrect understanding:

```text
Student = Object
```

Correct:

```text
Student → Class
student1 → Object
```

---

## 2. Forgetting `self`

Incorrect:

```python
class Student:

    def display():
        print("Hello")
```

Correct:

```python
class Student:

    def display(self):
        print("Hello")
```

---

## 3. Forgetting `self.` for Instance Attributes

Incorrect:

```python
class Student:

    def __init__(self, name):
        name = name
```

Correct:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Here:

```text
name       → Parameter
self.name  → Instance Attribute
```

---

## 4. Forgetting Parentheses When Creating an Object

Correct:

```python
student1 = Student()
```

Incorrect:

```python
student1 = Student
```

The second statement refers to the class itself rather than creating a new instance.

---

## 5. Using Instance Data in a Static Method

A static method does not automatically receive `self`.

Incorrect concept:

```python
class Student:

    @staticmethod
    def display():
        print(self.name)
```

There is no `self` parameter available here.

---

## 6. Confusing Class and Instance Attributes

Remember:

```python
class Student:

    college = "ABC University"
```

is a class attribute.

While:

```python
self.name = name
```

is an instance attribute.

---

## 7. Giving `__init__()` the Wrong Name

Correct:

```python
def __init__(self):
```

Incorrect:

```python
def init(self):
```

The double underscores are important.

---

## 8. Incorrect Indentation

Python uses indentation to define blocks.

Correct:

```python
class Student:

    def display(self):
        print("Hello")
```

---

# 🔎 Important OOP Terminology

| Term | Meaning |
|---|---|
| Class | Blueprint/template for objects |
| Object | Instance of a class |
| Instance | A specific object created from a class |
| Attribute | Data associated with a class/object |
| Instance Attribute | Attribute belonging to a particular object |
| Class Attribute | Attribute associated with the class |
| Method | Function defined inside a class |
| `self` | Reference to the current instance |
| Constructor | Common beginner term for `__init__()` |
| `__init__()` | Initializes an object's state |
| Static Method | Method that does not require instance state |
| `@staticmethod` | Decorator used to define a static method |

---

# 📊 Quick Revision Tables

## 🧱 Basic OOP Structure

```text
Class
 ↓
Objects
 ↓
Attributes + Methods
```

---

## 📦 Class and Object

| Concept | Example |
|---|---|
| Class | `Student` |
| Object | `student1` |
| Class Attribute | `college` |
| Instance Attribute | `self.name` |
| Instance Method | `display()` |
| Static Method | `welcome()` |
| Constructor/Initializer | `__init__()` |

---

## 👤 `self`

```text
self
 ↓
Current Object
 ↓
Access instance data
 ↓
self.name
self.age
```

---

## 🏗 `__init__()`

```text
Object Creation
      ↓
__init__()
      ↓
Initialize Attributes
      ↓
Object Ready
```

---

## 🧮 Static Method

```text
@staticmethod
      ↓
No self
      ↓
No automatic access to instance state
      ↓
Useful for class-related utility behavior
```

---

# 🧪 Complete Example

```python
class Employee:

    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)

    @staticmethod
    def company_info():
        print("This is a technology company.")


employee1 = Employee("Aarav", 30000)
employee2 = Employee("Meera", 40000)

employee1.display()
print()

employee2.display()
print()

Employee.company_info()
```

### Concepts demonstrated:

```text
Employee
    ↓
Class

employee1, employee2
    ↓
Objects

company
    ↓
Class Attribute

name, salary
    ↓
Instance Attributes

display()
    ↓
Instance Method

self
    ↓
Current Object

__init__()
    ↓
Object Initialization

company_info()
    ↓
Static Method
```

---

# 🧠 Mental Model for OOP

A simple way to remember the concepts is:

```text
CLASS
  │
  │ Blueprint
  ↓
OBJECT
  │
  ├── Attributes → Data
  │
  └── Methods → Behavior
```

For example:

```text
Student Class
      │
      ├── name
      ├── age
      ├── college
      │
      ├── study()
      └── display()
```

Here:

```text
name, age
    ↓
Instance Data

college
    ↓
Class Data

study(), display()
    ↓
Behavior
```

---

# 🌟 Why OOP is Important for Python

OOP is one of the most important programming concepts to understand because many real-world Python programs and libraries are designed using classes and objects.

Once the basic concepts are clear, more advanced OOP concepts can be learned later, such as:

```text
Inheritance
Encapsulation
Polymorphism
Abstraction
Method Overriding
Multiple Inheritance
```

These concepts build on the foundation learned in this chapter.

---

# ⭐ Key Points

- OOP stands for **Object-Oriented Programming**.
- OOP organizes programs around objects and classes.
- A class is a blueprint/template.
- An object is an instance of a class.
- One class can create multiple objects.
- Attributes represent data or state.
- Methods represent behavior or actions.
- Instance attributes belong to individual objects.
- Class attributes belong to the class and can be shared by instances.
- `self` refers to the current instance.
- Instance methods normally receive `self`.
- `__init__()` is used to initialize an object's state.
- `__init__()` is automatically called during normal object initialization.
- `@staticmethod` is used to define static methods.
- Static methods do not automatically receive `self`.
- Static methods are useful when behavior is related to a class but does not depend on instance state.
- The same class can be used to create many objects with different states.
- OOP makes programs more organized, reusable, modular, and maintainable.
- Understanding classes and objects is essential before moving to advanced OOP concepts.

---

# 🚀 Summary

In this chapter, I learned the **basics of Object-Oriented Programming (OOP) in Python**.

The major concepts covered were:

### Object-Oriented Programming

OOP is a programming paradigm that organizes programs around objects and classes.

### Classes

A class is a blueprint or template used to create objects.

```python
class Student:
    pass
```

### Objects

An object is an instance of a class.

```python
student1 = Student()
```

### Attributes

Attributes represent data associated with a class or object.

### Instance Attributes

Instance attributes belong to individual objects.

```python
self.name
self.age
```

### Class Attributes

Class attributes belong to the class and can provide values shared by instances.

```python
class Student:
    college = "ABC University"
```

### Methods

Methods are functions defined inside a class and generally represent object behavior.

### `self`

`self` refers to the current instance and allows instance methods to access that object's attributes.

### `__init__()`

`__init__()` is used to initialize an object's attributes when the object is created.

```python
def __init__(self, name):
    self.name = name
```

### Static Methods

Static methods are methods that do not automatically receive an instance reference.

They are created using:

```python
@staticmethod
```

Example:

```python
@staticmethod
def add(a, b):
    return a + b
```

Overall, this chapter provided the foundation required to understand how Python programs can be designed using **classes, objects, attributes, and methods**.

---

# 📚 Course Information

**Course:** CodeWithHarry Python Course

**Chapter:** 10 - OOP Basics

**Language:** Python

**Topic:** Object-Oriented Programming Fundamentals

**Main Concepts:** Classes, Objects, Attributes, Methods, `self`, `__init__()`, Class Attributes, Instance Attributes, Static Methods

---

# 👨‍💻 Author

**Sonal Rai**