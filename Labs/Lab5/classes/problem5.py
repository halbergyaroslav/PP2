class Account:
    def __init__(self, balance = 0):
        self.owner = input('Write your name please: ')
        self.balance = balance
        
    def withdraw(self, n):
        if n > self.balance: print('Withdraw is bigger than balance!')
        else: self.balance -= n
    
    def deposit(self, n):
        self.balance += n
        
    def __str__(self):
        return f'Owner: {self.owner}, Balance: {self.balance}'


account = Account()
print(account)
account.deposit(1000)
account.withdraw(500)
account.withdraw(600)
account.deposit(100)
print(account)