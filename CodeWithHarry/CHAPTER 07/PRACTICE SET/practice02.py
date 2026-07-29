#WAP to greet all the person names stored in a list l and which starts with S
#l=["HARRY", "SONAL", "RAHUL", "SOHAN", "SACHIN"]

#1st way- by using index number of every string in the list
l = ["HARRY", "SONAL", "RAHUL", "SOHAN", "SACHIN"]

for i in l:
    if (i[0] == "S"):
        print(f"HELLO! {i}")

#2nd way- by using function startwith()
l = ["HARRY", "SONAL", "RAHUL", "SOHAN", "SACHIN"]

for name in l:
    if (name.startswith("S")):
        print(f"Hello {name} !")
