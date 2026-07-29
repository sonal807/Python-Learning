#WAP to calculate the factorial of a given number using for loop.

n = int(input("Enter the number to find the factorial of: "))

fact = 1

if (n < 0):
    print("Factorial doesn't exist.")

elif (n == 0):
    print("The factorial of 0 is 1")

else:
    for i in range(1, n+1):
         fact = fact * i
        
    print(f"The factorial of {n} is: {fact}")
   
