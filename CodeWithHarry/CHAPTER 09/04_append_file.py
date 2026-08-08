#Append is used when we want to add new data at the end of an existing file 
# without removing its previous contents.
#For this we use "a"(eppend) mode

# f = open("student.txt", "a")

# f.write("\nPawan") #if we don't use \n it will print in the same line
# f.close()

#We can also append using user input

name = input("Enter the name:")
f = open("student.txt", "a")

f.write(f"\n{name}")

#Just a simple program for showing vistors and their note
name = input("Enter visitor name: ")
note = input("Enter the note: ")

f = open("visitors.txt", "a") #if visitor.txt doesn't exist it will automatically create a file

f.write(f"\nThe visitor is: {name}\n{name}'s note:- {note}")

f.close()