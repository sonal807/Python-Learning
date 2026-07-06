#Write a recursive function to calculate the sum of first n natural numbers.

def cal(n):
    if (n==0):
        return 0
    return cal(n-1) + n

sum = cal(10)
print(sum)
    
