#SELF refers to the instance of class.
#It is automatically passed with a function call from an object.
#Self simply means "this current object".

class Employee:           
    salary = 20000   
    state = "UP"

    def getinfo(self):
        print(f"The salary is {self.salary} and the state of the employee is{self.state}.")

    @staticmethod     #static method doesn't need any object. It is marked as a decorator
    def greet():      #no need to use self here as it is termed as static method
        print("Hey! Good morning")

e1 = Employee()
e1.greet()
e1.getinfo()      
