from utils import get_data_transactions
from collections import Counter, defaultdict
from description import description_transaction


def get_count_operations_by_category(operations: list[dict], list_of_category: list) -> dict:
    """

    Функция принимает список словарей с данными о банковских операциях и список категорий операций
    и возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории

    """
    result = Counter(
        [operation["description"] for operation in operations if operation["description"] in list_of_category]
    )

    return dict(result)


if __name__ == '__main__':
    path = "../data/operations.json"
    test_try = get_data_transactions(path)
    my_list = ["Перевод организации", "Открытие вклада"]

    result = get_count_operations_by_category(test_try, my_list)
    print(result)
