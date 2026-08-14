#Write a program to reda the text from a given file 'poems.txt' and
#find out whether it contains the word 'twinkle'

with open("poems.txt", "r") as f:
    poem = f.read()
    print(poem)

if "Twinkle" in poem:
    print("The word Twinkle is present.")

else:
    print("The word twinkle is not present.")
