from src.description import description_transaction
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_data_transactions
from src.csv_excel_reader import func_for_read_csv, func_for_read_excel
from src.widget import get_data, mask_account_card
from src.masks import account_number_hider, card_number_hider


def greeting_user():
    """ Приветстсвие и выбор файла с транзакциями """
    print("""Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")
    user_choice = input("Введите цифру: ")
    match user_choice:
        case "1":
            print("Программа: Для обработки выбран JSON-файл.")
            return get_data_transactions("../data/operations.json")
        case "2":
            print("Программа: Для обработки выбран CSV-файл.")
            return func_for_read_csv("../data/transaction.csv")
        case "3":
            print("Программа: Для обработки выбран XLSX-файл.")
            return func_for_read_excel("../data/transactions_excel.xlsx")
        case _:
            print("Ошибка ввода. Введите цифру от 1 до 3")
            return greeting_user()


def choice_user_status(operations):
    """ Выбор статуса и фильтрация по нему """
    print("""Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    user_choice = input("Введите статус: ").upper()
    if user_choice in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Программа: Операции отфильтрованы по статусу "{user_choice}"\n')
        return filter_by_state(operations, user_choice)
    print(f"Программа: Статус операции {user_choice} недоступен.")
    return choice_user_status(operations)


def user_settings(operations: list[dict]) -> list[dict]:
    """Выбор настроек фильтрации"""

    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет")
        user_answer = input("Пользователь: ").lower()
        if user_answer == "да":
            while True:
                print("\nПрограмма: Отсортировать по возрастанию или по убыванию? ")
                user_answer = "по убыванию"
                if user_answer == "по возрастанию":
                    operations_processing = sort_by_date(operations, False)
                    break
                elif user_answer == "по убыванию":
                    operations_processing = sort_by_date(operations, True)
                    break
                else:
                    print("\nОшибка ввода - повторите, пожалуйста\n")
            break
        elif user_answer == "нет":
            operations_processing = operations
            break
        else:
            print("\nОшибка ввода - повторите, пожалуйста\n")

    while True:
        print("\nПрограмма: Выводить только рублевые тразакции? Да/Нет ")
        user_answer = input("Пользователь: ").lower()
        if user_answer == "да":
            operations_processing = [tr for tr in filter_by_currency(operations_processing, "RUB")]
            break
        elif user_answer == "нет":
            break
        else:
            print("\nОшибка ввода - повторите, пожалуйста\n")

    while True:
        print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
        user_answer = input("Пользователь: ").lower()
        if user_answer == "да":
            print("\nПрограмма: введите слово для фильтрации")
            filter_input = input("Пользователь: ")
            operations_processing = description_transaction(operations_processing, filter_input)
            break
        elif user_answer == "нет":
            break
        else:
            print("\nОшибка ввода - повторите, пожалуйста\n")

    return operations_processing


def result_printing(operations: list[dict]) -> None:
    """Вывод результатов"""

    print("Программа: Распечатываю итоговый список транзакций...\n")
    if len(operations) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Программа: Всего банковских операций в выборке: {len(operations)}")

        for operation in operations:
            print(f'\n{get_data(operation["date"])} {operation["description"]}')
            if (
                (operation.get("from", 0) == 0)
                or (operation.get("from", 0) is None)
                or (operation.get("from", 0) == "NaN")
            ):
                print(mask_account_card(operation["to"]))
            else:
                print(f'{mask_account_card(operation["from"])} -> {mask_account_card(operation["to"])}')

            print(f"Сумма {operation['operationAmount']['amount']} {operation["operationAmount"]["currency"]["code"]}")


def main() -> None:
    operations_from_file = greeting_user()
    operations_by_state = choice_user_status(operations_from_file)
    operations_for_print = user_settings(operations_by_state)
    result_printing(operations_for_print)


if __name__ == "__main__":
    main()
