#WAF to convert USD to INR

def converter(usd):
    inr = usd * 95.22
    print(usd, "USD =", inr, "INR")

usd =int(input("Enter the amount:"))
converter(usd)