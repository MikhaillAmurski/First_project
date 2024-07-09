import json
import logging


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(path):
    """функция возвращает список словарей с данными о  транзакциях"""
    logger.info('Начало работы функции...')
    json_data_transaction = []
    try:
        logger.info("Открытие файла по указанному пути")
        with open(path, "r", encoding="utf-8") as f:
            logger.info('Получение информации из файла')
            json_data_transaction = json.load(f)
            return json_data_transaction
    except json.JSONDecodeError as je:
        logger.error(f'Произошла ошибка: {je}')
        return json_data_transaction
    except FileNotFoundError as ex:
        logger.error(f'Произошла ошибка: {ex}')
        return json_data_transaction
