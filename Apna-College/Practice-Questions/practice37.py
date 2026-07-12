# Create a class Order which stores item and its price. 
# Use the __gt__() function to convey that:
#     order1>order2 if price of order1>price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, odr2):
        return self.price > odr2.price
        
odr1 = Order("Biscuits", 30)
odr2 = Order("Chips", 25)

print(odr1 > odr2)