f = open("student.txt", "w") #"w" made stands for write mode

f.write("Hello Sonal")
f.close()

#important point of "w" mode(overwriting existing file)
st = "Sonal Rai"

f = open("student.txt", "w") #if we write again something in the same file,
                             # the previous content willbw deleted as "w" does not add new content
                             # It replaces the old content
f.write(st)
f.close()

##Writing multiple lines 
#method- 1 (use the new line character(\n))
f = open("student.txt", "w")

f.write("Sonal\n")
f.write("Rahul\n")
f.write("Amit\n")

f.close()

#method- 2
f = open("student.txt", "w")

text = """Sonal
Rahul
Amit
Priya"""

f.write(text)

f.close()

#return value of write(): write() returns the number of characters written.
f = open("student.txt", "w")

characters = f.write("Python")

print(characters)

f.close()

#let us take an example to save the multiple names of the student using for loop in file student.txt
f = open("student.txt", "w")
n = int(input("How many names do you want to enter? "))

for i in range(n):
    name = input(f"Enter the name of {i+1} student:")
    f.write(name + "\n")
f.close()