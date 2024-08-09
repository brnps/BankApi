class Account:
    def __init__(self, account_id: str, balance: int = 0):
        self.account_id = account_id
        self.balance = balance

class Database:
    def __init__(self):
        self.accounts = {}

    def reset(self):
        self.accounts = {}

    def get_account(self, account_id: str):
        return self.accounts.get(account_id)

    def create_account(self, account_id: str, initial_balance: int):
        account = Account(account_id, initial_balance)
        self.accounts[account_id] = account
        return account

db = Database()
