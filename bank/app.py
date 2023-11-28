class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            return True
        else:
            return False

    def get_balance(self, account_number):
        return self.accounts.get(account_number, "Account not found")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            return True
        else:
            return False

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number] >= amount:
            self.accounts[account_number] -= amount
            return True
        else:
            return False


# Example usage:
bank = Bank()

# Create accounts
bank.create_account("12345", 1000)
bank.create_account("67890", 500)

# Deposit and withdraw
bank.deposit("12345", 200)
bank.withdraw("67890", 100)

# Display account balances
print("Account 12345 Balance:", bank.get_balance("12345"))
print("Account 67890 Balance:", bank.get_balance("67890"))
