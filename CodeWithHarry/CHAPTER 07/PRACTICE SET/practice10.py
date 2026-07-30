#WAP to print multiplication table of n using for loop in reversed order

num = int(input("Enter the number to get the table: "))
print(f"Table of {num}")

for i in range(10, 0, -1):
    print(f"{num} * {i} = {num * i}")