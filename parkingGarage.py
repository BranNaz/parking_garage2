



# Start Your Code here

class parkingGarage():
    
    # updated to intialize w/o any parameters- the parking spaces/tickets are a set number
    def __init__(self):
        self.tickets = 5
        self.parkingSpaces = [
            {0: 'open', 'paid' : False}, 
            {1: 'open', 'paid' : False}, 
            {2: 'open', 'paid' : False}, 
            {3: 'open', 'paid' : False}, 
            {4: 'open', 'paid' : False}
        ]
        
        #just throwing this in to maybe have some fun with a print statement later; "Look at all the money our parking garage has made!"
        self.bank = 0
        
    def serveSpace(self):
        for x in range(len(self.parkingSpaces)):
            if self.parkingSpaces[x][x] == 'open':
                return x
            elif self.parkingSpaces[x][x] == 'full':
                continue
            return False

    def takeTicket(self):
        a = self.serveSpace()
        if a:
           self.tickets -= 1
           self.parkingSpaces[a][a] = 'full'
           print(f'Please proceed to spot {a}.  This is your ticket, don\'t forget {a} or you\'re stuck here forever. . . ')
        else:
            print("We're full!  Sorry, better keep looking for a spot to park.")
    


    def payForParking(self):
        pay = input('Please enter your ticket #.')
        z = input("Enter an amount of $35 foo! ")
        if z == '35':
            self.parkingSpaces[pay]['paid'] = True
            self.bank += z
        else:
            oth = input("Let's try this again, gimme what you got.")
            self.parkingSpaces[pay]['paid'] = True
            self.bank += oth
        print("Thank you for paying. You get 15mins tops.  Get outta here! ")



    def leaveGarage(self):
        tic = input("What's your ticket number?")
        # if paid- we let them loose and reset
        if self.parkingSpaces[tic]['paid'] == True:
            self.parkingSpaces[tic]['paid'] = False
            self.parkingSpaces[tic][tic] = 'open'
            print('Thank You, Have a wonderful life!')
        # Else we're gonna get that money
        elif self.currentTicket == False:
            x = input('Gimme all your money, how much you got???')
            if isinstance(x, int):
                self.parkingSpaces[tic][tic] = 'open'
                self.tickets += 1
                self.bank += x
                print('That works, have a great day!')
            else:
                # Just trying to have some fun with error handling
                y = input("Don't make me bust a kneecap, give me a number. . . ")
                self.parkingSpaces[tic][tic] = 'open'
                self.tickets += 1
                self.bank += y
                print('That works, have a great day!')
                print('That works, have a great day!')
    
    def run(self):
        print("Welcome to Tony's yard/event parking!")
        menu = input('p to park, pay to pay, l to leave, done to quit')
        while menu != 'done':
            if menu == 'p':
                # The framework is in, finish it off!
                pass
            elif menu == 'pay':
                # The framework is in, finish it off!
                pass
            elif menu == 'l':
                # The framework is in, finish it off!
                pass
        print(f"\n\nHey Tony!  We made ${self.bank} today.")
        
        
t = parkingGarage()
t.run()