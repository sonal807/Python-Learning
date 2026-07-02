#WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#Start with an empty dictionary and add one by one.
#Use subject name as key and values and makrs as values.
marks = {}
x = input("Enter the marks for physics: ")
marks.update({"physics": x})
y = input("Enter the marks for chemistry: ")
marks.update({"chemistry": y})
z = input("Enter the marks for mathematics: ")
marks.update({"mathematics": z})

print(marks)