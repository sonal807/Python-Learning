#Create a class 'Employee' and add salary and increment properties to it.
#Write a method 'salaryAfterIncrement' method @property decorator with a setter
#which changes the value of the increment based on salary.

class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + ((self.salary * self.increment)/ 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary - self.salary)/ self.salary)* 100

    def show(self):
        print(f"\nSalary : {self.salary}\nIncrement : {self.increment}%")
        print(f"Salary After Increment : {self.salaryAfterIncrement}")

e = Employee(50000, 20)
# print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 60000

# print(e.increment)
e.show()