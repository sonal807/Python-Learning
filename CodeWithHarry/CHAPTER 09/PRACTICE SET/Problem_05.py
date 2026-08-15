#Write a program to mine a log file and find out whether it contains 'python'.

with open("log.txt", "r") as f:
    text = f.read()

if "python" in text:
    print("Yes, python is present.")
else:
    print("No, python is not present.")

#Find out the line number where python is present

with open("log.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start = 1):
    if "python" in line:
        print("Python is present on line number", i)