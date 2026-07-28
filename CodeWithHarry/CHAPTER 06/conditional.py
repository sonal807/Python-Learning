# a conditional expression is used to make a decision in a program based on whether the condition is true or false 
#if...else anf if..elif..else are types of conditional expressions

#if...else statement
a = int(input("Enter your age:"))

if (a >= 18):
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")


#if...elif....else statement
age = int(input("Enter your age: "))

if (age >= 18):
    print("You are eligible to vote")

elif(age == 0):
    print("You have just borned, can't vote now")

elif(age<0):
    print("You have entered invalid age")

else:
    print("You are not eligible to vote")


##nested if statement- A nested if statement occurs when you place an if, elif, or else block inside another if, elif, or else block
b = int(input("Enter your age:"))
income = int(input("Enter your Income:"))

if (b >= 18):
    print("Age requirement met.")

    if (income >= 30000):
        print("Loan approved.")

    else:
        print("Loan denied: Income below 30000")

else:
    print("Loan denied: Must be atleast 18 years old.")


#Single line statement
num = int(input("Enter the number:"))

result = "Even" if num % 2 == 0 else "Odd"
print(result)