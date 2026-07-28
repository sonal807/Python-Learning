#A spam comment is defines as a text containing following keywords:
#"make a lot of money", "buy now", "subscribe this", "click this".
#WAP to detect these spams.

s1 = "make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

message = input("Enter your comment: ")

if((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message)):
    print("Spam comment detected.\nAttention!")

else:
    print("Comment is safe.\nGo ahead!")