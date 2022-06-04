from easy_equities_client.clients import EasyEquitiesClient
from dotenv import load_dotenv
import os

load_dotenv()

client = EasyEquitiesClient()
client.login(username=str(os.environ.get("EASY_USERNAME")), password=str(os.environ.get("EASY_PASSWORD")))

accounts = client.accounts.list()
accounts_empty_removed = []
for account in accounts:
    if account.name.find("Demo") == -1 and account.name.find("USD") == -1 and account.name.find("AUD") == -1 and account.name.find("Properties") == -1:
        accounts_empty_removed.append(account)

print("--------MY ACCOUNTS---------")
for account in accounts_empty_removed:
    print(account)

print("--------MY HOLDINGS---------")
for account in accounts_empty_removed:
    print(account.name)
    holdings = client.accounts.holdings(account.id)
    for holding in holdings:
        print(holding)
