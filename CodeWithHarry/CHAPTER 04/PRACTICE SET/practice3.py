#Check that the tuple cannot be changed in python

a = (34, 32, "Sonal")
a[2] = "hello"
print(a)

# it will show an error that "tuple object doesnot support item assignment"
#it is verfied that tuple cant be changed, they are immutable 