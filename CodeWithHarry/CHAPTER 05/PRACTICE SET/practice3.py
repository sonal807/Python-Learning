#Create and empty dictionary.
#Allow four friends to enter their favourite language as value and use key as their names.
#Assume that the names are unique.

language = {}
for friends in range(4):
    name = input("Enter your name:")
    lang = input("Enter your favourite language:")
    language.update({name : lang})
print(language)