#WAP to print multiplication table of a given number using for loop.

num = int(input("Enter the number to get the table: "))
print(f"Table of {num}")

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")