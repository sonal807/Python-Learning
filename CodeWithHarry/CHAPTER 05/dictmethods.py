# DICTIONARY METHODS
marks = {
    "Sonal" : 95,
    "Shivam" : 78,
    "Aditya" : 87,
    "Aman" : 89
}

print(marks.items()) #it returns the items of dictionary in list in the form of tuples

print(marks.keys()) #returns all the keys of the dictionary

print(marks.values()) #returns all the values of the dictionary

marks.update({"Sonal": 96}) # updates the dictionary with supplied key-value pairs
print(marks)

marks.update({"Sonal":89, "Sonali":90})#another way to update the dictionary which will update the existing key value and add the new item if it doent exist to dictionary
print(marks)

print(marks.get("Sonal")) #returns the value to the given key

clone = marks.copy() #Returns a shallow copy of the dictionary.
print(clone)

print(marks.popitem()) #Removes and returns the last inserted (key, value) pair as a tuple (LIFO order).

marks.clear() #removes all the items from the dictionary and make it empty
print(marks)