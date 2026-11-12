# Encapsulation
# Keep data and methods together; use methods to control access to data.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Name-mangled (private by convention)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

account = BankAccount("Aarav", 1000)
account.deposit(500)
print("Current balance:", account.get_balance())
