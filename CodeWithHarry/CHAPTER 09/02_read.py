#1- read()
f = open("file.txt", "r")

data = f.read() 
print(data)
f.close()

#2- read(n) can read only a specific number of characters.
f = open("file.txt", "r")

print(f.read(5))#Only the first 5 characters are read.
print(f.read(10))#here it will read and distpley the next 10 characters after first 5 characters(if written alone only the first 10 characters are read.)
f.close()

#Example-1
f = open("file.txt", "r")
print(f.read(7)) #OUTPUT: Hello e
f.close()

#Example-2
f = open("file.txt", "r")
print(f.read(5)) #OUTPUT: Hello
print(f.read(8)) #OUTPUT: _everyon
print(f.read(6)) #OUTPUT: e___Ho
f.close()

#3- readline() method reads only one line at a time.
f = open("file.txt", "r")

line = f.readline()
print(line)
f.close()

#Reading Multiple Lines
f = open("file.txt", "r")

print(f.readline()) #OUTPUT: Hello everyone...How are you ?
print(f.readline()) #OUTPUT: We are learning python file I/O
print(f.readline()) #OUTPUT: This is the third line.

f.close()

#4- readlines() method reads all the lines from a file and stores them in a list.
f = open("file.txt", "r")

lines = f.readlines()
print(lines)

f.close()

#Since readlines() returns a list, we can use indexing.
f = open("file.txt", "r")

lines = f.readlines()

print(lines[0]) #OUTPUT: Hello everyone...How are you ?(acess it from the returned list)
print(lines[1]) #OUTPUT: We are learning python file I/O(acess it from the returned list)

f.close()

#5- for line in file: Instead of using readlines(), Python programmers often use a for loop.
                    # which is best for large files.

f = open("file.txt", "r")

for line in f:
    print(line)

f.close()        

#6- readline() using while loop
file=open("file.txt","r")

line=file.readline()

while(line != ""):
    print(line)
    line=file.readline()

file.close()