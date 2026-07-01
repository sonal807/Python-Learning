#to check if a list contains a palindrome of elements
list = [1, 2, 2, 1]
list1 = list.copy()
print(list)
print(list1)
list2 = list1.reverse()
if(list1 == list):
    print("It is a palindrome")
else:
    print("It is not a palindrome")