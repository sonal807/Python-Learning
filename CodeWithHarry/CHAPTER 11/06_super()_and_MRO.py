#super() method: super() method is used to access the method of a super class in the derived class.
#super() is a built-in Python function that allows us to access methods and attributes of the next class in the Method Resolution Order (MRO),
#without explicitly referring to the parent class by name.
#super() is used in a child class to access the next class's methods or constructor without explicitly referring to the class name.

class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method")
        super().show()  #If we dont use this line here the parent class method will be completely overrided(happens when both have same named method)
        #So for using both the parent's and child's method we used here super()
obj = Child()
obj.show()

#super() is importantly used with constructore __init__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)   #it calls the parent constructor, so the the attributes of parent also get initialized in child object
        self.course = course

s = Student("Sonal", 20, "Python")
print(s.name)
print(s.age)
print(s.course)

#Let' take one more example
class School:
    def __init__(self):
        print("Constructor of school")

class Class(School):
    def __init__(self):
        super().__init__()
        print("Constructor of class")

class Student(Class):
    def __init__(self):
        super().__init__()
        print("Constructor of student")

s = Student()

#We can call parent's method directly by name and by super() too(We prefer super()), both will have same output
class Parent:
    def show(self):
        print("Parent method")


class Child(Parent):
    def show(self):
        Parent.show(self)      # Directly parent class
        super().show()         # Using super()
        print("Child method")

c = Child()
c.show()


##MRO (Method Resolution Order): It is the order in which python searches when looking for a method or attribute.
#MRO decides the order. super() follows that order and moves to the next class.

class Person:
    def show(self):
        print("Person")

class Student(Person):
    def show(self):
        print("Student")

class CollegeStudent(Student):
    pass

student = CollegeStudent()
student.show()  #since show() is not present in CollegeStudent, the according to MRO it will go to student and it gets show() then it will execute there and will not go to person.

print(CollegeStudent.mro()) #It is used to see the MRO 

#MRO gets intresting and important in multiple inheritance
class Teacher:
    def show(self):
        print("Teacher")

class Sports:
    def show(self):
        print("Sports")

class Student(Teacher, Sports):  #If we write here (Sports, Teacher) then the sports show will be called.
    pass

std = Student()

std.show()

print(Student.mro())


#Let's take one more example
class Person:
    def identity(self):
        print("I am a person")

class Teacher(Person):
    def work(self):
        print("I teach students")

class Sports:
    def play(self):
        print("I play football")

class Student(Teacher, Sports):
    def study(self):
        print("I study Python")

s = Student()

s.identity()
s.work()
s.play()
s.study()

print(Student.mro())

##We will now understand the concept of super() + MRO
#MRO decides the route
#super() calls the next class in the route
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show() # here the super() will acess the next class after current class in MRO

obj = D()
obj.show()

print(D.mro())

#Let's Take one more example
class Railway:
    def show(self):
        print("Railway system")


class Passenger(Railway):
    def show(self):
        print("Passenger service")
        super().show()


class Booking(Railway):
    def show(self):
        print("Booking service")
        super().show()


class Train(Passenger, Booking):
    def show(self):
        print("Train service")
        super().show()


t = Train()

t.show()

print(Train.mro())
