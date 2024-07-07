import requests
import os
from src.utils import get_data_transactions
from dotenv import load_dotenv


load_dotenv("..\\.env")

path = "..\\data\\operations.json"


def amount_transaction(transaction_by_id):
    """функция возвращает сумму транзакции в рублях"""

    trans_amount = transaction_by_id["operationAmount"]["amount"]
    trans_code = transaction_by_id["operationAmount"]["currency"]["code"]
    API_KEY = os.getenv("API_KEY")
    headers_api = {"apikey": API_KEY}
    if trans_code == "RUB":
        return trans_amount
    else:
        try:

            url = f"https://api.apilayer.com/fixer/convert?to=RUB&from={trans_code}&amount={trans_amount}"

            response = requests.request("GET", url, headers=headers_api)
            my_result = response.json()
            return my_result["result"]
        except Exception as e:
            print(e)