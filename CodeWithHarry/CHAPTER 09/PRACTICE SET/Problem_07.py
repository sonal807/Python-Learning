#Write a program to wipe out the content of a file using pyhton.

with open("this_copy.txt", "w") as f:
    pass

#Write a code to delete the file.
import os

os.remove("this_copy.txt")