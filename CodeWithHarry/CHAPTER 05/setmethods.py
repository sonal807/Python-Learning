s = {1, 3, 5, 7, 9, 11}
s.add(13) #adds new item to the set
print(s)

s.remove(1) #Removes the specified element. Raises a KeyError if the element is not in the set.
print(s)

s.discard(11) #Removes the specified element safely without raising an error if it doesn't exist.
print(s)

s.pop()
print(s) #Removes and returns an arbitrary element from the set (since sets are unordered). Raises KeyError if the set is empty.

a = s.copy() # returns a shallow copy of the set
print(a)

print(len(s)) #length of set

s.clear() #removes all the elements and make it empty
print(s)


#SET OPERATIONS
A = {1, 2, 3, 4, 5, 6, 7, 8}
B = {2, 4, 6, 8, 10, 12}

# 1- Union(|)
print(A.union(B))
print(A | B)

# 2- Intersection(&)
print(A.intersection(B))
print(A & B)

# 3- Difference(-) RETURNS THE ELEMENT THAT ARE IN A BUT NOT IN B
print(A.difference(B))
print(A - B)

# 4- Symmetric difference(^) RETURNS THE ELEMENT THAT ARE IN EITHER SET BUT NOT IN BOTH 
print(A.symmetric_difference(B))
print(A ^ B)

# 4- Subset(issubset / <=)
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
print(a <= b)

# 5- Superset(issuperset / >=)
c = {1, 2, 3, 4}
d = {1, 2}
print(c.issuperset(d))
print(c >= d)

# 6- Proper subset(<)
e = {1, 2}
f = {1, 2, 3}
g = {1, 2}

print(e < f)
print(e < g)

# 7- Proper superset(>)
h = {1, 2, 3}
i = {1, 2}

print(h > i)

# 8- Disjoint(isdisjoint) Two sets are disjoint if their intersection is empty
j = {1, 2}
k = {3, 4}
l = {2, 3}

print(j.isdisjoint(k))
print(j.isdisjoint(l))