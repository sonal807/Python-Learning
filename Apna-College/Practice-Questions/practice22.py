# print multiplication table of a number n using for and range.

n = int(input("Enter the number for multiplication table:"))

for i in range(1, 11):
    print(n, "X", i, "=", n*i)