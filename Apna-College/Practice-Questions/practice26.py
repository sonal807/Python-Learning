#WAF to find the factorial of n.(n is the parameter)


def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*= i
    print(fact)

n = int(input("Enter the number to find factorial"))
cal_fact(n)
