#Class method: It is a method which is bound to the class and not the object of the class.
# A class method is a method that works with the class itself rather than a particular object.
# It is defined using the @classmethod decorator and takes cls as its first parameter.

class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()   #Here we didn't created object and called method directly from class.
                        #Because class method is bind with class, not with object


#let's take example
class Employee:
    a = 1
    def show(self):
        print(f"The class sttribute of a is {self.a}")

e = Employee()
e.a = 45

e.show() #IT will show 45, as self access the current instance attribute, if not mentioned then class method

#so if want to access our class attribute whether the instance attribute is given or not given we use @class method
class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class sttribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show() #Both will give same output
Employee.show() #but we should use this one as it reduces the line of code

#self vs cls
#self -> current object
#cls -> current class
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def show_student(self):
        print(self.name)

    @classmethod
    def show_school(cls):
        print(cls.school)

s1 = Student("Happy") 
s1.show_student()  #Object involved

Student.show_school() #Class is directly incolved


#Modification of class attribute with class method
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

print(Student.school)

Student.change_school("CPS School")
print(Student.school)

##Example
class Train:
    railway_name = "Indian Railways"

    @classmethod
    def change_railway_name(cls, new_name):
        cls.railway_name = new_name

print(Train.railway_name)

Train.change_railway_name("Northern Railways")
print(Train.railway_name)

#Alternative constructor: We create object using class method
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


s = Student.from_string("Sonal-20")

print(s.name)
print(s.age)