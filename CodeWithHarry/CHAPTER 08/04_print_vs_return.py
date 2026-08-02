#print() displays output on the screen but does not send it back to the caller.
# If a function has no return, Python automatically returns None.
def add(a, b):
    print(a + b)

result = add(10, 20) # This will print 30 but result will be None
print(result)

#return sends a value back to the caller and immediately ends the function.
# The returned value can be stored in a variable, printed, or used in further calculations.
def add(c, d):
    return c + d

result = add(10, 20)
print(result)