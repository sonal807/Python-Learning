#From a file containing numbers seperated by comma, print the count of even and odd numbers.

with open("Apna-College/Practice-Questions/practice32.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")

    even_count = 0
    odd_count = 0

    for val in nums:
        if int(val) % 2 == 0:
            even_count += 1
        else:
            odd_count +=1
    print("Count of even numbers:", even_count)
    print("Count of odd numbers:", odd_count)
