name = "sonal rai"

print(len(name)) #gives length of the string
print(name.endswith("ai")) #checks whether the string end with the given characters and gives True or False as result
print(name.startswith("son")) #checks whether the string starts with the given characters and gives True or False as result
print(name.capitalize()) #it capitalize the very first letter of the string
print(name.lower()) #changes the whole string in lower case
print(name.upper()) #changes the whole string in upper case
print(name.title()) #it capitalize the first letter of every word in string
print(name.find("sonal")) #it gives the index of the word at wich it first occured
print(name.replace("sonal","SONAL")) #it replaces the old word with new word
print(name.count("i")) #it counts the number of times a letter or a word occured
print(name.strip())
print(name.split()) #it splits every word of string and store it in a list