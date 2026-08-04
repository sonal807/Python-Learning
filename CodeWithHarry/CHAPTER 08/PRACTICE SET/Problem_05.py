#Write a python program to print first n lines of the following pattern
# ***
# **
# *      

def pattern(n):
    for i in range(n):
        print("*" * (n - i))

n = int(input("Enter the value of n:"))

pattern(n)


##Method-2
def pattern(n):
    if (n == 0):
        return
    print("*" * n)
    pattern(n-1)

pattern(6)