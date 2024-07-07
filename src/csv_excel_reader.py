import csv
import json
import pandas as pd


def func_for_read_csv(filename: str) -> list[dict]:
    """Функция для считывания данных в формате CSV и возврата в виде списка словорей"""
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = dict()
            for i, item in enumerate(header):
                row_dict[item] = row[i]
            result.append(row_dict)
    return result


def func_for_read_excel(filename: str) -> list[dict]:
    """Функция для считывания данных в формате EXCEL и возврата в виде списка словарей"""
    result = pd.read_excel(filename).to_json()
    return json.loads(result)


if __name__ == "__main__":
    test = func_for_read_csv("transaction.csv")
    print(test)
    test2 = func_for_read_excel("transactions_excel.xlsx")
    print(test2)
