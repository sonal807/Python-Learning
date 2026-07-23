#WAP to print the content of a directorty using the os module.
#Search online for the function which does that
import os

#Specify the directory you want to list
path = "/"

#List all files and directories in the specified path
contents = os.listdir(path)

#print each file and directory name
for item in contents:
    print(item)