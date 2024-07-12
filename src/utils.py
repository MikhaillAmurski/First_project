import json
import logging
import os.path
from typing import List, Dict

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(path: str) -> List[Dict]:
    """функция возвращает список словарей с данными о  транзакциях"""
    if not os.path.exists(path):
        return []
    logger.info('Начало работы функции...')
    try:
        logger.info("Открытие файла по указанному пути")
        with open(path, "r", encoding="utf-8") as file:
            logger.info('Получение информации из файла')
            transactions = []
            for line in json.load(file):
                if line != {}:
                    operation_dict = {
                        "id": line.get('id'),
                        "state": line.get('state'),
                        "date": line.get("date"),
                        "amount": line["operationAmount"].get("amount"),
                        "currency_name": line["operationAmount"]["currency"].get("name"),
                        "currency_code": line["operationAmount"]["currency"].get("code"),
                        "from": line.get("from"),
                        "to": line.get("to"),
                        "description": line.get("description")
                    }
                transactions.append(operation_dict)
            return transactions
    except json.JSONDecodeError as je:
        logger.error(f'Произошла ошибка: {je}')
        return transactions
    except FileNotFoundError as ex:
        logger.error(f'Произошла ошибка: {ex}')
        return transactions


if __name__ == "__main__":
    result = get_data_transactions("../data/operations.json")
    print(result)
