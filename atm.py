class Atm(object):
    def __init__(self, name, cardNumber, pin, currentBalance): 
        self.name = name
        self.cardNumber = cardNumber
        self.pin = pin
        self.currentBalance = currentBalance

    def cashWithdrawal(self):
        withdraw = input("How much money would you like to withdraw? ")
        print("Money Successfully Withdrawn")

    def  balanceInquiry(self):
        print(self.currentBalance)
    
    def accessCard(self):
        putPin = input("Input Pin to access card: ")

        if putPin == self.pin:
            print("Pin successfully inputted")

        if not putPin == self.pin:
            print("Incorrect Pin")
    
Kai = Atm("Kai", "1234567890", "1234", "$234.56")
Kai.balanceInquiry()

#Quick Note for Ms. Charan: I don't really understand how ATMs work, so I made up a function. I hope that's ok!