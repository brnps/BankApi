from app.database import Database
from app.models.account import Account

class AccountService:
    def __init__(self, db: Database):
        self.db = db

    def get_balance(self, account_id: str) -> float:
        try:
            return self.db.get_balance(account_id)
        except ValueError:
            return None

    def create_account(self, account_id: str, initial_balance: float):
        return self.db.deposit(account_id, initial_balance)

    def deposit(self, account_id: str, amount: float):
        return self.db.deposit(account_id, amount)

    def withdraw(self, account_id: str, amount: float):
        try:
            return self.db.withdraw(account_id, amount)
        except ValueError:
            return None

    def transfer(self, origin_id: str, destination_id: str, amount: float):
        try:
            return self.db.transfer(origin_id, destination_id, amount)
        except ValueError:
            return None
