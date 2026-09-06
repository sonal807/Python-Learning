#CLASS attributes: An attribute that belongs to the class then a particular object.
#INSTANCE attributes: An attributes the belongs to the instance(object).

class Employee:           
    salary = 20000      # class attributes
    state = "UP"


E1 = Employee()
E1.name = "Rohan"        #instance attribute
E1.state = "Bihar"        #state will now become bihar
print(E1.name,E1.salary,E1.state)

E2 = Employee()
E2.name = "Mohan"
E2.salary = 30000          # now salary will be 30000 at the palce of 20000 (instance attribute over class attribute)
print(E2.name,E2.state,E2.salary)

#Instance attributes, take preference over class atributes during asignment and retrieval.