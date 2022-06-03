from easy_equities_client.clients import EasyEquitiesClient
from dotenv import load_dotenv
import os

load_dotenv()

client = EasyEquitiesClient()
client.login(username=str(os.environ.get("EASY_USERNAME")), password=str(os.environ.get("USER_PASSWORD")))

accounts = client.accounts.list()
print(accounts)