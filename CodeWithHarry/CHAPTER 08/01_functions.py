'''Functions in pyhton are blocks of reusable code that perform a specific task 
Instead of writing the same code again and again ,you can write it once inside a function and call it whenever needed
When program gets bigger in size we use functions'''

#Basic function to greet with functions without parameters
def greet(): #Defining a function
    print("HELLO!")

greet() #function call

#Functions without parameters
def greet(name):
    print("HELLO!", name)

greet("Sonal")
greet("Ishika")

#Returning values
def add(a,b):
    return a + b

result = add(55, 100)
print("Result", result)

#Taking input inside function
def avg(): #Function to find the average of three numbers
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = int(input("Enter the third number:"))

    average =(a + b + c)/3
    print(average)

avg()
print("Thank you")

#Quick quiz to greet with have a good day
def goodDay():
    print("Good day!")

goodDay()