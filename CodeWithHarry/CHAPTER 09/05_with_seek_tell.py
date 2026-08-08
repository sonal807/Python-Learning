#As we know we were using f.close() for closing the file after finishing the work.
#But there is a problem if an error occurs and the program crashes before
#reaching f.close() so the file may remain open.
#Python provide the better solution for it that is 'with' statement

#1- 'with' statement: automatically manages the file we don't need to use f.close()
#Python automatically closes the file when the with block finishes.
#And it is also the cleaner safer and easy to read version.

#'with' with "r" mode
with open("student.txt", "r") as f:
    data = f.read()
    print(data)

#'with' with "a" mode
with open("student.txt", "a") as f:
    f.write("\nRohan")

#=>tell() method:The file pointer tells Python where it currently is inside the file.
#                The tell() method tells us the current position of the pointer.

with open("student.txt", "r") as f:
    print(f.tell())

#tell() After Reading
with open("student.txt", "r") as f:

    print(f.tell()) #initially 0

    data = f.read(5)
    print(data) #output will be Sonal

    print(f.tell()) #it will give


#=>seek() method: tell() tells us where the pointer is.
#                 seek() allows us to move the pointer.
with open("student.txt", "r") as f:

    print(f.read(5))

    f.seek(0)

    print(f.read(5))