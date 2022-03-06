class User:	
    def __init__(self, name, email, checkingBalance, savingBalance):
        self.name = name
        self.email = email
        self.checkingBalance = checkingBalance
        self.savingBalance = savingBalance
        self.checking = BankAccount(0.02, checkingBalance)
        self.saving = BankAccount(0.02, savingBalance)

    def make_deposit(self, amount, account):	
        
        if account == "checking":
            self.checking.deposit(amount)
        elif account == "saving":
            self.saving.deposit(amount)

        return self
  
    def make_withdrawal(self, amount, account): 
        if account == "checking":
            self.checking.withdrawal(amount)
        elif account == "saving":
            self.saving.withdrawal(amount)

        return self    
      
    def display_user_balance(self): 
        print("User: {}, Checking: {}\nUser: {}, Balance: {}".format(self.name, self.checking.balance, self.name, self.saving.balance)) 
       


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

chelsa = User("Chelsa Kays", "chelsakays@yahoo.com", 4000, 6000)
chelsa.make_deposit(2000, "checking").make_withdrawal(500, "checking").make_deposit(600, "saving").make_withdrawal(1200, "saving").display_user_balance()