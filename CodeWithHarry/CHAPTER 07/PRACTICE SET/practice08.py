#WAP to print following type star pattern
# *
# **
# ***

n = int(input("Enter the number: "))

for i in range (1, n+1):
    for j in range (i):
        print("*", end ="")
    print()

#2nd way
for i in range(1, n+1):
    print("*"*i, end = "")
    print("")

#for pattern
# ***
# **
# *
for i in range (n, 0, -1):
    for j in range (i):
        print("*", end ="")
    print()