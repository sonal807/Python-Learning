#WAP to print multiplication table of a given number using while loop.

num = int(input("Enter the number to get the table: "))
print(f"Table of {num}")

i = 1
while (i < 11):
    print(f"{num} * {i} = {num * i}")
    i += 1