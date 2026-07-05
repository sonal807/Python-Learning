# WAF to print length of a list.(list is the parameter)

cities = ["Noida", "Pune", "Lucknow", "Gurgaon", "Greater Noida"]
heroes = ["Captain america", "Strange", "spiderman", "Iron man", "Thor", "Hulk"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#WAF to print the elements of a list in a single line(list is the parameter)

heroes = ["Captain america", "Strange", "spiderman", "Iron man", "Thor", "Hulk"]
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heroes)     
