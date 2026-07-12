#Define an employee class with attributes:
# - Role
# - Department
# - Salary  #This class also has a showDetails() method.
# Create an Engineer class that inherits from Employee and has additional attributes:
# - name
# - age.  

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "Rs. 60000")


eng1 = Engineer("Sonal Rai", 24)
eng1.showDetails()
        
