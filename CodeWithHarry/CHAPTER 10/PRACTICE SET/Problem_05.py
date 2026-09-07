#Create a class train which has methods to book a ticket,
#get status(no of seats) and get fare information of train running under Indian railways.

class Train:
    
    def __init__(self, number, seats, fare):
        self.number = number
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats>0:
            print(f"Your ticket has been successfully booked")
            self.seats -= 1
            print(f"Seats left in {self.number} = {self.seats}")

        else:
            print("Sorry no seats avalable, The train is full.")

    def get_status(self):
        print(f"Train number: {self.number}")
        print(f"Seats available: {self.seats}")

    def get_fare(self):
        print(f"The fare of the ticket: {self.fare}")

train1 = Train(12345, 50, 900)

train1.get_status()
train1.book_ticket()
train1.get_status()
train1.get_fare()