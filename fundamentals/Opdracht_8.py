class BankAccount:

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("A withdrawal was made. ")
        return self.balance

    def withdraw(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            print("A withdrawal was made. ")
        else:
            print("You don't have enough money in your account!")
        return self.balance


balance = "Current balance is: "

account = BankAccount("Alex")
print(f"Owner of the account is: {account.owner}")
print(f"Starting account balance is: {account.balance}")
print(f"{balance}{account.deposit(10)}")
print(f"{balance}{account.withdraw(17)}")
