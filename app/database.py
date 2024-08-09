class Database:
    def __init__(self):
        self.accounts = {}

    def reset(self):
        self.accounts = {}

    def get_balance(self, account_id: str):
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account not found")
        return account['balance']

    def deposit(self, account_id: str, amount: float):
        if account_id not in self.accounts:
            self.accounts[account_id] = {'id': account_id, 'balance': 0}
        self.accounts[account_id]['balance'] += amount
        return self.accounts[account_id]

    def withdraw(self, account_id: str, amount: float):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        if self.accounts[account_id]['balance'] < amount:
            raise ValueError("Insufficient funds")
        self.accounts[account_id]['balance'] -= amount
        return self.accounts[account_id]

    def transfer(self, origin_id: str, destination_id: str, amount: float):
        origin_account = self.withdraw(origin_id, amount)
        if destination_id not in self.accounts:
            self.accounts[destination_id] = {'id': destination_id, 'balance': 0}
        destination_account = self.deposit(destination_id, amount)
        return origin_account, destination_account
