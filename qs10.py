# 10.Write a Python program that simulates a banking system. Implement a class called BankAccount with methods to initialize an account with a
# starting balance, withdraw funds, and handle a custom exception called NegativeBalanceError when the account balance goes below zero.

class NegativeBalanceError(Exception):
    def __init__(self, balance):
        self.balance = balance
        super().__init__(f"Error: Account balance cannot be negative ({balance})")

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < 0:
            raise NegativeBalanceError(self.balance)
        self.balance -= amount
        print(f"Withdrew {amount}. Current balance: {self.balance}")

try:
    balance = float(input("Enter the balance: "))
    account = BankAccount(balance)
    withdraw = float(input("Enter the withdrawal amount: "))
    if withdraw < 0:
        raise ValueError("Withdrawal amount must be positive.")
    account.withdraw(withdraw)
except NegativeBalanceError as e:
    print(e)
except ValueError as e:
    print(e)
