#WAP to print the following star pattern:
#   *
#  ***
# ***** for n = 3

n = int(input("Enter the value of n: "))

for i in range (1, n+1):
    spaces = n - i
    for j in range(spaces):
        print(" ", end = "")
    for k in range(2 * i - 1):
        print("*", end = "")
    print()