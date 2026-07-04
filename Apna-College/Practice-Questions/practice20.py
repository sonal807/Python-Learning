#Q1- print elements of the following list using for loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in lst:
    print(i)

#Q2- search for a number x in this tuple using for loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tup = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter the number to search:"))
idx = 0
for i in tup:
    if(x == i):
        print("Number found at index:", idx)
        break
    idx += 1
else:
    print("Not found")    

