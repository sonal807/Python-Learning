#search for a number x in this tuple using while loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number to search:"))
i = 0
while i < len(tup):
    if tup[i] == x:
        print("Number founded at index:", i)
        break
    else:
        print("finding....")
    i += 1

  
