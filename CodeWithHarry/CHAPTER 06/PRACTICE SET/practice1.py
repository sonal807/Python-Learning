#WAP to find greatest of four numbers entered by user

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourth number:"))

if(a > b and a > c and a > d):
    print("First number is the largest number, which is:", a)

if(b > a and b > c and b > d):
    print("Second number is the largest number, which is:", b)

if(c > b and c > a and c > d):
    print("Third number is the largest number, which is:", c)

else:
    print("Fourth number is the largest number, which is:", d)
