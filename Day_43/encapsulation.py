class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance  # Accessor method to get private balance

# Example usage
account = BankAccount("John", 500)
account.deposit(200)
account.withdraw(100)
print(account.get_balance())  # Output: 600
