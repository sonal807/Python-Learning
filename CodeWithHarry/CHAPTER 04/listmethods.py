friends = ["Apple", "Orange", 6, 345.06, False, "aaksh", "Rohan"]
print(friends)

friends.append("Sonal") #adds element at the end of the list
print(friends)

l1 = [1, 34, 62, 2, 8, 76, 98]
l1.sort() #sort the list in ascending order
print(l1)

l1.reverse() #reverse the whole list
print(l1)

friends.insert(2, "banana") #insert the item to the given index(index, item)
print(friends)

l1.pop(3) #delete the element from the list from given index and if we print it will return the popped value
print(l1)

l1.remove(62) #it removes the given element from the list
print(l1)

l1.clear() #removes all the items from the list
print(l1)