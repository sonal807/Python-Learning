# Arithematic operators
a = 5
b = 2
c = a+b
d = a-b
e = a*b
f = a/b
print(c)
print(d)
print(e)
print(f)

# Assignment operators
g = 4-2 # Assign 4-2 in g
print(g)
h = 6 
h += 3 # Increment the value of h by 3 and then assign it to h
h -= 3 # Decrement the value of h by 3 and then assign it to h
h *= 3 # Multiply the value of h with 3 and then assign it to h
h /= 3 # devide the value of h with 3 and then assign it to h
print(h)

# Comparison operators (always return boolean values as result)
i = 10
j = 4
print(i>j)
print(i<j)
print(i>=j)
print(i<=j)
print(i != j)

# Logical operators (AND, OR, NOT, etc)
#Truth table of OR
print("True or False is:", True or False)
print("True or True is:", True or True)
print("False or True is:", False or True)
print("False or False is:", False or False)

#Truth table of AND
print("True and False is:", True and False)
print("True and True is:", True and True)
print("False and True is:", False and True)
print("False and False is:", False and False)

#NOT operator is used to inverse the boolean value
print(not(True)) #Reults False
print(not(False)) #Reults True