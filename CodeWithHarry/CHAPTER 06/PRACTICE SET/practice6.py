#WAP which finds out whwther a given name is in a list or not.

avengers = ["Iron man", "Thor", "Captain", "Hulk", "Strange"]

name = input("Enter the name to search: ")

if (name in avengers):
    print("The name is present in list.")

else:
    print("The name is not present")