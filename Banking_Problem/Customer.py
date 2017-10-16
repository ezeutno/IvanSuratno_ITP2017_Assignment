from Jude_Assignment.Banking_Problem.Account import Account
import random
class Customer(Account):
    def __init__(self, firstname, lastname, account, balance):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__account = account
        self.balance = balance
        Account.__init__(self, self.balance)

    def getFirstName(self):
        return self.__firstname
    def getLastName(self):
        return self.__lastname
    def getAccount(self):
        return self.__account
    def setAccount(self,acc,amt):
        self.__account = acc
        Account.deposit(self,amt)
    def newAccount(self,acc,data):
        acc_data = acc+str(random.randint(0,999))
        data.append([acc_data,'0'])
        return acc_data



