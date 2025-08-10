import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 12** **** 1234"


def test_get_mask_card_number_length():
    assert get_mask_card_number("1234") == "Ошибка ввода"
    assert get_mask_card_number("") == ""
    assert get_mask_card_number("254151532326263262632632") == "Ошибка ввода"
    assert get_mask_card_number("Nastya") == "Ошибка ввода"


@pytest.mark.parametrize("account, expected", [(12345678910111213145, "**3145"),
                                               (123, "Ошибка ввода"), ("123456789", "Ошибка ввода"), ("", "")])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
