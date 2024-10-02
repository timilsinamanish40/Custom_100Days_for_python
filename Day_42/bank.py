class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Account holder's name
        self.balance = balance  # Initial balance, defaults to 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. Remaining balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

# Example usage:
account = BankAccount("John Doe", 1000)

account.deposit(500)  # Deposited 500. New balance: 1500
account.withdraw(200)  # Withdrew 200. Remaining balance: 1300
account.withdraw(2000)  # Insufficient balance
