#WAP to fill in altter template given below with name and date 
# letter='''
            #  Dear <name>,
            #  you are selected!
            #  <date>
            # '''

letter=''' Dear <name>,
           You are selected!
           <date> '''

print(letter.replace("<name>", "Sonal").replace("<date>", "22 July 2026")) #chaining of functions