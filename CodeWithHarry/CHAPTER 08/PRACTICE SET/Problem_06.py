#Write a python function which converts inches to cms.

def inch_to_cm(i):
    cm = i * 2.54
    return cm

i = float(input("Enter the inches to convert:"))

result = inch_to_cm(i)

print(f"{i} inch in cm will be: {result}")