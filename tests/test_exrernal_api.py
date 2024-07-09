import unittest
from unittest.mock import patch
from src.external_api import amount_transaction


@patch("requests.request")
def test_amount_transaction_rub(mock_request):
    """Проверяем, что транзакция в рублях корректно обрабатывается"""
    mock_request.return_value.json.return_value = {"result": 31957.58}
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
    }
    result = amount_transaction(transaction)
    assert result == "31957.58"


@patch("requests.request")
def test_amount_transaction_other_currency(mock_request):
    """Проверяем, что транзакция в других валютах корректно обрабатывается"""
    mock_request.return_value.json.return_value = {"result": 704216.961075}
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD.", "code": "USD"},
        },
    }
    result = amount_transaction(transaction)
    assert result == 704216.961075
