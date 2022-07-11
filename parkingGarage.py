


# Start Your Code here

class parkingGarage():
    
    # updated to intialize w/o any parameters- the parking spaces/tickets are a set number
    def __init__(self):
        self.tickets = [20]
        self.parkingSpaces = [20]
        self.currentTicket = {'paid' : False}
        #just throwing this in to maybe have some fun with a print statement later; "Look at all the money our parking garage has made!"
        self.bank = 0
        
        

    def takeTicket(self):
        if self.currentTicket == True:
           self.tickets[0] -= 1
           self.parkingSpaces[0] -= 1
    


    def payForParking(self):
        z = input("Enter an amount of $35 foo! ")
        if input == '35':
            self.currentTicket['paid'] = True
        print("Thank you for paying. You get 15mins tops. ")



    def leaveGarage(self):
        # if paid- we let them loose and reset
        if self.currentTicket == True:
            self.currentTicket = False
            print('Thank You, Have a wonderful life!')
        # Else we're gonna get that money
        elif self.currentTicket == False:
            x = input('Gimme all your money, how much you got???')
            if isinstance(x, int):
                self.currentTicket['paid'] = False
                self.parkingSpaces[0] += 1
                self.tickets[0] += 1
                self.bank += x
                print('That works, have a great day!')
            else:
                # Just trying to have some fun with error handling
                y = input("Don't make me bust a kneecap, give me a number. . . ")
                self.currentTicket['paid'] = False
                self.parkingSpaces[0] += 1
                self.tickets[0] += 1
                self.bank += y
                print('That works, have a great day!')



parking = parkingGarage()
print(parking.__dict__)
print(parking.payForParking())