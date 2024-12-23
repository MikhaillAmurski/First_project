import pandas as pd
import pytest
from pandas import Timestamp


@pytest.fixture
def trans():
    return [
        {
            "Дата операции": "2020-05-26 13:29:09",
            "Дата платежа": "2020-05-28 00:00:00",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -45.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -45.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 0,
            "Категория": "Супермаркеты",
            "MCC": 5499.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 45.0,
        },
        {
            "Дата операции": "2020-05-26 13:23:32",
            "Дата платежа": "2020-05-28 00:00:00",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -86.6,
            "Валюта операции": "RUB",
            "Сумма платежа": -86.6,
            "Валюта платежа": "RUB",
            "Кэшбэк": 0,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Магнит",
            "Бонусы (включая кэшбэк)": 1,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 86.6,
        },
    ]


@pytest.fixture
def trans_for_services():
    return [
        {
            "Дата операции": "31.12.2021 16:44:00",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -160.89,
            "Валюта операции": "RUB",
            "Сумма платежа": -160.89,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 3.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 160.89,
        },
        {
            "Дата операции": "31.12.2021 16:42:04",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -64.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -64.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 1.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 64.0,
        },
        {
            "Дата операции": "31.12.2021 16:39:04",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -118.12,
            "Валюта операции": "RUB",
            "Сумма платежа": -118.12,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Магнит",
            "Бонусы (включая кэшбэк)": 2.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 118.12,
        },
        {
            "Дата операции": "31.12.2021 15:44:39",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -78.05,
            "Валюта операции": "RUB",
            "Сумма платежа": -78.05,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 1.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 78.05,
        },
        {
            "Дата операции": "31.12.2021 01:23:42",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*5091",
            "Статус": "OK",
            "Сумма операции": -564.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -564.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Различные товары",
            "MCC": 5399.0,
            "Описание": "Ozon.ru",
            "Бонусы (включая кэшбэк)": 5.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 564.0,
        },
        {
            "Дата операции": "31.12.2021 00:12:53",
            "Дата платежа": "31.12.2021",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -800.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -800.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Переводы",
            "MCC": None,
            "Описание": "Константин Л.",
            "Бонусы (включая кэшбэк)": 0.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 800.0,
        },
        {
            "Дата операции": "30.12.2021 22:22:03",
            "Дата платежа": "31.12.2021",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -20000.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -20000.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Переводы",
            "MCC": None,
            "Описание": "Константин Л.",
            "Бонусы (включая кэшбэк)": 0.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 20000.0,
        },
        {
            "Дата операции": "30.12.2021 19:18:22",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*5091",
            "Статус": "OK",
            "Сумма операции": -7.07,
            "Валюта операции": "RUB",
            "Сумма платежа": -7.07,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Каршеринг",
            "MCC": 7512.0,
            "Описание": "Ситидрайв",
            "Бонусы (включая кэшбэк)": 0.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 7.07,
        },
        {
            "Дата операции": "30.12.2021 19:06:39",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -1.32,
            "Валюта операции": "RUB",
            "Сумма платежа": -1.32,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Каршеринг",
            "MCC": 7512.0,
            "Описание": "Ситидрайв",
            "Бонусы (включая кэшбэк)": 0.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 1.32,
        },
        {
            "Дата операции": "30.12.2021 17:50:30",
            "Дата платежа": "30.12.2021",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": 5046.0,
            "Валюта операции": "RUB",
            "Сумма платежа": 5046.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Пополнения",
            "MCC": None,
            "Описание": "Пополнение через Газпромбанк",
            "Бонусы (включая кэшбэк)": 0.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 5046.0,
        },
    ]


@pytest.fixture
def return_value_for_investment_bank():
    return {
        "Thursday": -2774.18,
        "Wednesday": -1429.55,
        "Tuesday": -291.35,
        "Monday": -1404.81,
        "Sunday": -1373.39,
        "Saturday": -334.0,
        "Friday": -732.67,
    }


@pytest.fixture
def input_to_file():
    return {
        "greeting": "Доброй ночи",
        "cards": [
            {"last_digits": "7197", "total_spent": 20412.800000000003, "cashback": 204.12800000000001},
            {"last_digits": "4556", "total_spent": 1065.0, "cashback": 10.65},
        ],
        "top_transactions": [
            {
                "date": Timestamp("2020-05-02 00:00:00"),
                "amount": -9564.76,
                "category": "Другое",
                "description": "ГУП ВЦКП ЖХ",
            },
            {
                "date": Timestamp("2020-05-23 00:00:00"),
                "amount": -1851.0,
                "category": "Различные товары",
                "description": "МаксидоМ",
            },
            {
                "date": Timestamp("2020-05-18 00:00:00"),
                "amount": -815.0,
                "category": "Книги",
                "description": "Буквоед",
            },
            {
                "date": Timestamp("2020-05-27 00:00:00"),
                "amount": -572.0,
                "category": "Транспорт",
                "description": "Яндекс Такси",
            },
            {
                "date": Timestamp("2020-05-13 00:00:00"),
                "amount": -484.0,
                "category": "Различные товары",
                "description": "Улыбка радуги",
            },
        ],
        "currency_rates": [{"currency": "USD", "rate": 95.676332}, {"currency": "EUR", "rate": 104.753149}],
        "stock_prices": [
            {"stock": "S&P 500", "price": 4500.5},
            {"stock": "Dow Jones", "price": 34000.75},
            {"stock": "NASDAQ", "price": 15000.25},
        ],
    }


@pytest.fixture
def return_to_file():
    return {
        "greeting": "Доброй ночи",
        "cards": [
            {"last_digits": "7197", "total_spent": 20412.800000000003, "cashback": 204.12800000000001},
            {"last_digits": "4556", "total_spent": 1065.0, "cashback": 10.65},
        ],
        "top_transactions": [
            {"date": "2020-05-02T00:00:00", "amount": -9564.76, "category": "Другое", "description": "ГУП ВЦКП ЖХ"},
            {
                "date": "2020-05-23T00:00:00",
                "amount": -1851.0,
                "category": "Различные товары",
                "description": "МаксидоМ",
            },
            {"date": "2020-05-18T00:00:00", "amount": -815.0, "category": "Книги", "description": "Буквоед"},
            {"date": "2020-05-27T00:00:00", "amount": -572.0, "category": "Транспорт", "description": "Яндекс Такси"},
            {
                "date": "2020-05-13T00:00:00",
                "amount": -484.0,
                "category": "Различные товары",
                "description": "Улыбка радуги",
            },
        ],
        "currency_rates": [{"currency": "USD", "rate": 95.676332}, {"currency": "EUR", "rate": 104.753149}],
        "stock_prices": [
            {"stock": "S&P 500", "price": 4500.5},
            {"stock": "Dow Jones", "price": 34000.75},
            {"stock": "NASDAQ", "price": 15000.25},
        ],
    }


@pytest.fixture
def input_filter_operations_by_date_df():
    data = [
        {
            "Дата операции": "26.05.2020 13:29:09",
            "Дата платежа": "28.05.2020",
            "Номер карты": "*7197",
            "Сумма операции": -45.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -45.0,
            "Валюта платежа": "RUB",
        },
        {
            "Дата операции": "26.05.2020 13:23:32",
            "Дата платежа": "28.05.2020",
            "Номер карты": "*7197",
            "Сумма операции": -86.6,
            "Валюта операции": "RUB",
            "Сумма платежа": -86.6,
            "Валюта платежа": "RUB",
        },
    ]
    df_data = pd.DataFrame(data)
    return df_data


@pytest.fixture
def return_time_for_main():
    return "20-05-2020 13:26:36"

