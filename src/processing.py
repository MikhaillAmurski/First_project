from src.widget import get_data


def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция фильтрации операций по ключу state"""
    new_list = list(filter(lambda x: x.get("state") == state, list_dict))
    return new_list


def sort_by_date(list_dict: list, user_rev: bool = True) -> list:
    """Функция сортировки операций по дате"""
    if user_rev is True:
        sorted_list = sorted(list_dict, key=lambda x: get_data(x["date"]))
        return sorted_list
    else:
        sorted_list = sorted(list_dict, key=lambda x: get_data(x["date"]), reverse=False)
        return sorted_list


r = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
    False,
)
print(r)
