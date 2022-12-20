class Bank_account:
    def __init__(self, no):
        self.balance=0
        self.bank_account_no=no

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient funds on the account")

    def display(self):
        print(f"Bank Account No: {self.bank_account_no}")
        print(f"Balance: PLN {self.balance}")

account=Bank_account("12 3456 5555 9090 1111 0000 7722")
account.display()
account.deposit(25.30)
account.display()
account.withdraw(31.70)
account.display()
account.withdraw(14)
account.display()