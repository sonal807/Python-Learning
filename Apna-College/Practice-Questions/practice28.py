#WAF to the number entered by user is odd or even ehich is taken as input by user
num = int(input("Enter the number:"))

def check_odd_even(num):
    if num%2 == 0:
        print("The entered number is even")
    else:
        print("The entered number is odd")

check_odd_even(num)