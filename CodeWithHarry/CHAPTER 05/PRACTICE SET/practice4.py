#Can you change the value inside a list which is contained in set
# s={8,7,12,"harry",[1,2]} 

s={8,7,12,"harry",[1,2]} 
print(s) ## it will raise an type error
# can't use list as a set element because lists are mutable (changeable) but set elements are immutable (unchangeable)

# in case of tuple ...a set can contain tuple as its element becuase they are all immutable but also you can't modify the tuple after creation