#Write a program to generate multiplication tables form 2 to 20 and write it to the different files.
#Place these file in a folder for a 13 year old

import os

def generate_table(n, f):
    for i in range(1, 11):
        f.write(f"{n} X {i} = {n * i}\n")

#Create a folder
os.makedirs("TABLE", exist_ok = True)

#Generates the table from 2 to 20
for n in range(2, 21):

    filename = f"TABLE/table_of_{n}.txt"

    with open(filename, "w") as f:
        generate_table(n, f)