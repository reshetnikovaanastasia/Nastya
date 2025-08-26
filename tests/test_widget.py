import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("account_card, expected", [("Visa Platinum 7000792289606361",
                                                     "Visa Platinum 7000 79** **** 6361"),
                                                    ("Счет 73654108430135874305", "Счет **4305"),
                                                    ("Счет 7365410843013587430", "Ошибка ввода"),
                                                    ("MasterCard 1234123412341234",
                                                     "MasterCard 1234 12** **** 1234"),
                                                    ("MasterCard 123412341234123", "Ошибка ввода"),
                                                    ("MasterCard 123412341234ihiui", "Ошибка ввода"),
                                                    ("Счет 7365410каыуя35874305", "Ошибка ввода")])
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("fgyguhu") == "Некорректный формат времени"
    assert get_date("03-2024-12") == "Некорректный формат времени"
    assert get_date("") == "Некорректный формат времени"
