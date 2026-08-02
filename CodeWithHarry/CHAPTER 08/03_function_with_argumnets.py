'''A function with arguments is a function that accepts data from the caller.
   The values passed to the function are called arguments, and the variables that receive them are called parameters.

Syntax
def function_name(parameter1, parameter2):
    # code'''

#Functions with arguments
def goodDay(name, ending): #name, ending is as parameters
    print("GOOD DAY!", name)
    print(ending)

goodDay("Sonal", "Thank you") #Sonal, Thank you as arguments

#Default argument
def goodDay(name, ending = "Thank you"):
    print(f"GOOD DAY!, {name}")
    print(ending)

goodDay("Sonal")

#No arguments, no return value
def hello():
    print("HELLO!")

hello()

#Arguments, no return value
def greet(name):
    print(f"Hello! {name}")

greet("Sonal")

#No arguments, return value
def get_number():
    return 100

num = get_number()
print(num)

#Arguments, return value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)