#Write a recursive function to calculate the sum of first n natural numbers

def sum_natural_numbers(n):
    if (n == 1): #base case
        return n

    return (sum_natural_numbers(n-1) + n) #recursive case

n = int(input("Enter the number: "))

result = sum_natural_numbers(n)

print(f"The sum of first {n} natural numbers will be: {result}")