import re
from utils import get_data_transactions
import random


def description_transaction(transactions: list[dict], my_string: str) -> list[dict] | str:
    """
    Функция, которая будет принимать список словарей с данными
    о банковских операциях и строку поиска, а возвращать список словарей,
    у которых в описании есть данная строка.

    """
    pattern = re.compile(f"{re.escape(my_string)}")
    my_transactions = []
    for transaction in transactions:
        try:
            if pattern.search(transaction["description"]):
                my_transactions.append(transaction)
        finally:
            continue
    if my_transactions:
        return my_transactions
    else:
        return []


if __name__ == "__main__":
    path = "../data/operations.json"
    list_trans = get_data_transactions(path)
    my_string = random.choice(["Перевод со счета на счет",
                               "Перевод организации",
                               "Перевод с карты на карту",
                               "Открытие вклада",
                               "error"
                               ])
    print(*description_transaction(list_trans, my_string), sep="\n")
