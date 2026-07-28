#WAP to find whether a given username contains less than 10 character or not.

user = input("Enter the username:")

size = len(user)

if (size >= 10):
    print("Valid user name!\nContains 10 characters")

else:
    print("Invalid user name!\nContains less than 10 characters.")