#Multiple Inheritance: A child class inherits directly from more than one parent class.
#This allows the child class to combine functionalities from multiple independent sources

#Example-1
class Employee:     #First Parent class
    company = "ITC"
    def show(self):
        print("\nHello There! I am the first parent class.")

class Coder:        #Second Parent class
    language = "Python"
    def printlanguage(self):
        print("\nHello There! I am the second parent class.")
        print(f"Language: {self.language}")

class Programmer(Employee, Coder):   #Child Class or inherited class which inherits all the functions and properties of both parent class.
    company = "Infotech"
    def showlanguage(self):
        print(f"\nThe company in which I work is {self.company} and I am master in {self.language}")

a = Employee()
b = Coder()
c = Programmer()

a.show()
b.printlanguage()

c.show()
c.printlanguage()
c.showlanguage()


#Example-2
class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def hobbies(self):
        print("Mother: Painting")

class Child(Father, Mother):
    def likes(self):
        print("Child: Bike")

c = Child()

c.skills()
c.hobbies()
c.likes()

#Example-3
class Teacher:
    def teach(self):
        print("Teacher is teaching")

class Sports:
    def play(self):
        print("Student is playing football")

class Student(Teacher, Sports):
    def study(self):
        print("Student is studying")

s = Student()

s.teach()
s.play()
s.study()