# A simple class
# Class body
class Account:
    account_type = "Basic"
    def __init__(self,name,balance):
        "Initialize a new Account instances"
        self.name = name
        self.balance = balance
    def deposit(self, amt):
        "Add to the balance"
        self.balance = self.balance+amt
    def withdraw(self,amt):
        "Subtract from the balance"
        self.balance = self.balance - amt
    def inquiry(self):
        "Return the current balance"
        return self.balance

#create few accounts
a = Account('AB',1000)
a.deposit(100)
print (a.inquiry())