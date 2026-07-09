#Create Account class with 2 attributes-balance and account no.
#Create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.balance)

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.balance)

    #printing balance
    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(5000)
print("Final balance=", acc1.get_balance())