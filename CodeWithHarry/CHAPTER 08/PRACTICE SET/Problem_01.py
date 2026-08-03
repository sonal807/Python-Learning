#WAP using functions to find greatest  of three numbers

#Method-1 (easy)
def great():
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    c = int(input("Enter the number:"))

    if(a >= b and a >= c):
        print(f"The greatest number is: {a}")

    elif(b >= a and b >= c):
        print(f"The greatest number is: {b}")

    else:
        print(f"The greatest number is: {c}")

great()

#Method-2 (preferable)

def greatest(a, b, c):
    if(a >= b and a >= c):
        return a

    elif(b >= a and b >= c):
        return b

    else:
        return c

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

result = greatest(a, b, c)

print(f"The greatest number is: {result}")