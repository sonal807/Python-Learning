'''Recursion is a technique where a function calls itself to solve a problem.

Instead of using loops (for or while),
a recursive function repeatedly calls itself with a smaller version of the problem
until it reaches a stopping condition
Every recursive function must have a Base Case, without a base case,
the function will keep calling itself forever and cause an recurssionerror.

Every recursive function has two essential parts:

A. Base Case (Stopping Condition)

This tells Python when to stop calling the function.

B. Recursive Case

This is where the function calls itself with a smaller problem.'''

#Factorial of a number
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number:"))

print(f"The factorial of {n} is: {factorial(n)}")

#Fibonacci series
def fib(n):
    if(n <= 1):
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter the number:"))

print(f"Fibonacci of {n} is: {fib(n)}")

#Recursive function for sum of first n natural numbers
def sum_natural(n):
    if(n == 1):
        return n
    return sum(n-1) + n

n = int(input("Enter the number:"))

print(f"The sum of first {n} natural numbers will be: {sum_natural(n)}")

#Recursive function for couting the number of digits in a number
def count_digit(n):
    if (n < 10):
        return 1

    return 1 + count_digit(n // 10)

n = int(input("Enter the number:"))
print(f"The total number of digits in {n} is: {count_digit(n)}")

#Recursive function to find whether the string is palindrome or not
def palin(s):
    if (len(s) <= 1):
        return True
    if s[0] != s[-1]:
        return False
    return palin(s[1:-1])

word = input("Enter a string: ")

if palin(word):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Recursive function to reverse the string
def reverse(s):
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("Sonal"))