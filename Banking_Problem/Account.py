class Account:
    def __init__(self, balance):
        self.balance = balance

    def getBalance(self):
        return 'Rp. '+ str(self.balance)

    def deposit(self, amt):
        self.balance = str(float(self.balance) + amt)
        print('You have deposit Rp. ' + str(amt))
        return self.balance

    def withdraw(self, amt):
        if float(self.balance) >= amt:
            self.balance = str(float(self.balance) - amt)
            print('You have withdraw Rp. '+ str(amt))
            return self.balance
        else:
            print('Sorry your balance is insufficient.')
