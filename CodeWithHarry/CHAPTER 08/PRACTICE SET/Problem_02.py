#Write a python program using function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(c):
    f = (1.8 * c) + 32
    return f

celsius = float(input("Enter the temperature in celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"Temperature in Fahrenheit is: {fahrenheit}")

#Program to convert Fahrenheit to Celsius

def fahrenheit_to_celsius(f):
    c = (5/9) * (f - 32)
    return c

fahrenheit = float(input("Enter the temperature in fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print(f"Temperature in Fahrenheit is: {celsius}")