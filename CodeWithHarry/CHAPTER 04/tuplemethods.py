# tuple in pyhton are immutable thats why they have only two builtin methods 
# 1- count()
# 2- index()

a = (1, 45, 34, 34.4, False, "Hello", "Sonal")
print(a)

b = (4, 5, 6)


no = a.count(45) #counts the number of time an element occured
print(no)

i = a.index(45) #returns the index of first occurence of an element
print(i)

#operations with tuple
#1- concatenation
result = a+b
print("Concatenation of tuple a and b will be:", result)

#2- repetition
print("repeat the tuple b two times", b*2)

#3- membership (checks if the item exists in tuple using in keyword)
print(3 in a)

#4- length
print(len(a))

#5- min max
d = (89, 75, 3, 45, 19, 4)
print(min(d))
print(max(d))

#6- slicing
print(d[1:5])
print(d[1:6:2])

#7- unpacking
my_tuple = ("Sonal", 25, "Lucknow")
name,age,city = my_tuple
print(name)
print(age)
print(city)

# 8-extneded unpacking       collects the remaining elements in to alist 
my_tuple_2=(1,2,3,3,3,4,5,6,7,8)
a,*b,c=my_tuple_2
print(a)
print(b)
print(c)

#9- sum(calculates the sum of numerical items)
sum = sum(d)
print("the sum of items in tuple d is:", sum)

#10- sorted(sorts the tuple)
sort = sorted(d)
print(sort)