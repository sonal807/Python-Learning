#Create a class with class attribute a;
#create an object from it and set 'a' directly using object.a = 0.
#Does this change the class sttribute?

class something:
    a = "Hello"

s1 = something()
s1.a = "Hii"
print(s1.a)

#No the class sttribute doesn't get changed but,
#during execution class attribute gets changed as the object attribute take over class attribute.