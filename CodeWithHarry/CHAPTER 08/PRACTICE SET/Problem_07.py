#Write a python function to remove a given word from a list and strip it at the same time.

def remove_and_strip(list, word):
    new_list = []

    for item in list:
        if item.strip() != word:
            new_list.append(item.strip())

    return new_list

list = [" Sonal ", "Mohan", " Gaurav", "after", "  Hello  "]

word = input("Enter the word to remove:")

print(remove_and_strip(list, word))