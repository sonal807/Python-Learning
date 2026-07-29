#WAP to find whether a given number is prime or not.
num = int(input("Enter the number: "))
print(f"Check {num} is prime or not")

if num > 1:
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(f"{num} IS a prime number")
else:
    print(f"{num} is NOT a prime number.")

#WAP to print all prime numbers within a given range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            print(num)