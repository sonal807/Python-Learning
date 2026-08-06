'''
a = "a very long string with emails"

email = []
3 seconds
'''

f = open("file.txt", "r") #open() opens the file
data = f.read() #read() reads the whole file  and The result is stored in data.
print(data) #print() displays the contents.
f.close() #close() closes the file.


'''
MODES OF OPENING FILE:
r- open for reading
w- open for writing
a- open for appending
+- open for updating
'rb'- will open for read in binary mode
'rt'- will open for read in text mode
'''