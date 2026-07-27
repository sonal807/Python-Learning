#WAP to creste a hindi of hindi word with values as their english translation
#Provide user with an option to look it up! 

meaning = {
    "Khana" : "Food",
    "Sona" : "Gold",
    "Madad" : "Help",
    "Kursi" : "Chair",
    "Chashma" : "Spectacles"
}

word = input("Enter the word you want meaning of:")

if word in meaning:
    print(meaning[word])
else:
    print("This word is not in our meaning.")