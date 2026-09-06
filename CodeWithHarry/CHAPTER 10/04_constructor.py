#__int__() constructor: It is a dpecial method which is first run as soon as the object is created.
#It is also known as a constructor.
#It takes self argument and also can take further arguments.

class Employee:           
    salary = 20000   
    state = "UP"

    def __init__(self, name, city):    #A dunder method hich is automatically called
        self.name = name
        self.city = city
        print(f"Nmae of the employee is {self.name}, and he is from {self.city}")

    def getinfo(self, salary, state):
            print(f"The salary is {self.salary} and the state of the employee is {self.state}.")

e1 = Employee("Aman", "Noida")
e1.getinfo()
