#A file conatins a word "Donkey" multiple times. You need to write a program
#which replace this word with ##### by updating the same file.

with open("statement.txt", "r") as f:
    text = f.read()

text = text.replace("Donkey", "#####")

with open("statement.txt", "w") as f:
    f.write(text)