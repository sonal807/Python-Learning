#Write a program to make a copy of a text file "this.txt".

with open("this.txt", "r") as f:
    text = f.read()

with open("this_copy.txt", "w") as f:
    f.write(text)

#Write a program to find out whether a file is identical and matches the content of another file.
with open("this.txt", "r") as f:
    text1 = f.read()

with open("this.txt", "r") as f:
    text2 = f.read()

if text1 == text2:
    print("Files are identical")
else:
    print("Files are not identical")