# WAP to find the sum of first n natural numbers. (using while)

n = int(input("Enter a positive integer:"))

sum = 0
i = 1

while i <= n:
    sum += i
    i +=1

print("The sum of first", n, "numbers are:", sum)

#same question using for loop

n = int(input("Enter a positive integer:"))

sum = 0

for i in range(1, n+1):
    sum += i
print("The sum of first", n, "numbers are:", sum)