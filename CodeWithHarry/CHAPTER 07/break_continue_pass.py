#break statement-> The break statement terminates the loop prematurely. 
                # Execution jumps immediately to the first line of code outside the loop.

for i in range(100):
    if (i == 34):
        break #Exit the loop
    print(i)

for num in range(1,9):
    if (num == 6):
        break
    print(num)
print("Loop finished")


#continue statement-> The continue statement skips the rest of the current iteration
                    # and jumps directly to the start of the next iteration.

for j in range(20):
    if (j == 14):
        continue #Skip this iteration
    print(j)
                   
for new in range(1, 10):
    if (new == 7):
        continue
    print(new)
print("Loop finished")


#pass statement-> The pass statement is a null operation—nothing happens when it executes. 
                # It acts as a syntax placeholder when Python requires a statement block, 
                # but you aren't ready to write the code yet.

for i in range(100):
    pass #do nothing
i = 0
while(i<20):
    print(i)
    i += 2


#combines example of break , continue and pass
#Example 1
for i in range(1, 10):
    if (i % 2 == 0):
        continue
    elif (i == 5):
        pass #placeholder for future logic
    elif (i == 9):
        break
    print(f"Processing number: {i}")

#Example 2==> You have a list of item prices in a customer's shopping cart:
#prices = [10, 25, 0, 150, -5, 40]
# Here are the rules for processing the cart:
#1- Free promotional items (price == 0): 
    #Do nothing special right now (pass), just process them normally.
#2- Invalid prices (price < 0): 
   #Skip them completely because a price can't be negative (continue).
#3- Expensive items (price > 100): 
   #If an item costs more than 100, trigger a fraud alert and stop processing the cart immediately (break).

prices = [10, 25, 0, 150, -5, 40]

for price in prices:
    if (price < 0):
        continue

    elif (price == 0):
        pass #placeholder: free item, no tax applied.

    elif (price > 100):
        print(f"Price {price} exceeds limit! Stopping checkout.")
        break
    print(f"Item processed: ${price}")