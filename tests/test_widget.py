import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 7158300734726758", "Visa Platinum 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_data():
    assert get_data("2018-07-11T02:26:18.671407") == "11.07.2018"
