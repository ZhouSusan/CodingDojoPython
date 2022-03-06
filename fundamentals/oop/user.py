class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

     # adding the withdrawal method
    def make_withdrawal(self, amount): #takes an argument that is the amount of the withdrawal
        self.account_balance -= amount #decrease the user's balance by the amount specified

    def display_user_balance(self): 
        print("User: {}, Balance: {}".format(self.name, self.account_balance))

    def transfer_money(self, other_user, amount) :
        self.other_user = other_user
        self.account_balance -= amount
        other_user.make_deposit(amount)

david = User("David Martinez", "dem@gmail.com")
susan = User("Susan Zhou", "szhou089@gmail.com")
eva = User("Eva Strobeck", "evastrobek@gmail.com") 

david.make_deposit(100)
david.make_deposit(500)
david.make_deposit(1000)
david.make_withdrawal(200)
david.display_user_balance()

susan.make_deposit(50)
susan.make_deposit(200)
susan.make_withdrawal(20)
susan.make_withdrawal(80)
susan.display_user_balance()

eva.make_deposit(5000)
eva.make_withdrawal(3000)
eva.make_withdrawal(700)
eva.make_withdrawal(600)
eva.display_user_balance()

david.transfer_money(susan, 300)
david.display_user_balance()
susan.display_user_balance()