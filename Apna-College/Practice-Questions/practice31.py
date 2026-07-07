# Create a new file "practice.txt" using python. Add following data in it:
#   Hi everyone
#   we are learning File I/O 
#   using java.
#   I like programing in java.

# WAF that replaces all occurences of java with "python" in above file.

# Search if the word "learning" exists in the file or not.

with open("Apna-College/Practice-Questions/practice31.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using java.\nI like programing in java.")

with open("Apna-College/Practice-Questions/practice31.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "Python")

with open("Apna-College/Practice-Questions/practice31.txt", "w") as f:
    f.write(new_data)

word = "learning"
with open("Apna-College/Practice-Questions/practice31.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

#WAF to find in which line of the file does the word "learning" occur first.
#print -1 if word not found

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("Apna-College/Practice-Questions/practice31.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        else:
            print("-1")
check_for_line()