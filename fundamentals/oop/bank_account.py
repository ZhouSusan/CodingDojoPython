import math

class BankAccount:

    #class sttribute
    all_accounts_info = []

    def __init__(self, interestRate, balance) :
        self.interestRate = interestRate
        self.balance = balance
        BankAccount.all_accounts_info.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    def display_account_info(self):
        print("Balance: {}".format(self.balance))

    def yield_interest(self):
        if (self.balance > 0):
            self.balance = (math.ceil(self.balance * self.interestRate * 100)/ 100) + self.balance
            return self

    # class method to print all instances of a Bank Account's info
    @classmethod
    def print_all_info(cls): #cls refers to the class
        for account in cls.all_accounts_info:
            account.display_account_info()
            

mike = BankAccount(.10, 5000)
kyle = BankAccount(.05, 10000)

mike.deposit(200).deposit(700).deposit(100).withdrawal(50).yield_interest().display_account_info()
kyle.deposit(1000).deposit(1200).withdrawal(3500).withdrawal(2800).withdrawal(800.50).withdrawal(9000).yield_interest().display_account_info()
BankAccount.print_all_info()