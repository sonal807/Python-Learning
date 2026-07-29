#WAP to find the sum of first n natural numbers using while loop.

n = int(input("Enter a positive integer n: "))

i = 1
total_sum = 0

while (i <= n):
    total_sum += i
    i += 1

print(f"The sum of first {n} natural number is {total_sum}")