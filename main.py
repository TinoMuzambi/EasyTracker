from easy_equities_client.accounts.parsers import HoldingFieldNotFoundException
from easy_equities_client.clients import EasyEquitiesClient
from dotenv import load_dotenv
import os


class EasyTracker:
    def __init__(self):
        super().__init__()
        load_dotenv()

    @staticmethod
    def login(username, password):
        client = EasyEquitiesClient()
        client.login(username=username, password=password)
        return client

    @staticmethod
    def get_accounts(client):
        accounts = client.accounts.list()
        return accounts

    @staticmethod
    def print_accounts(accounts):
        print("--------MY ACCOUNTS---------")
        for account in accounts:
            print(account)

    @staticmethod
    def get_holdings(client, account):
        holdings = client.accounts.holdings(account.id)
        return holdings

    @staticmethod
    def print_holdings(holdings):
        for holding in holdings:
            print(holding)

    @staticmethod
    def print_account_holdings(accounts, tracker, client):
        print("--------MY HOLDINGS---------")
        for account in accounts:
            print(account.name)
            try:
                holdings = tracker.get_holdings(client, account)
                tracker.print_holdings(holdings)
            except HoldingFieldNotFoundException:
                pass

def main():
    tracker = EasyTracker()
    client = tracker.login(str(os.environ.get("EASY_USERNAME")), str(os.environ.get("EASY_PASSWORD")))

    accounts = tracker.get_accounts(client)
    tracker.print_accounts(accounts)

    tracker.print_account_holdings(accounts, tracker, client)


if __name__ == "__main__":
    main()
