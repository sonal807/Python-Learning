#Create a class "Programmer" for storing information of few programmers working at Microsoft.

class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, country):
        self.name = name
        self.salary = salary
        self.country = country

        print(f"The information of {self.name}-")

p1 = programmer("Daniel", 120000, "USA")
print(f"Company = {p1.company} \nName = {p1.name}\nSalary ={p1.salary}\nCountry = {p1.country}\n")
p2 = programmer("Rohan", 150000, "India")
print(f"Company = {p2.company} \nName = {p2.name}\nSalary ={p2.salary}\nCountry = {p2.country}\n")
p3 = programmer("Diljeet", 100000, "Canada")
print(f"Company = {p3.company} \nName = {p3.name}\nSalary ={p3.salary}\nCountry = {p3.country}\n")