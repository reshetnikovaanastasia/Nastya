from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Принимает на вход номер карты и возвращает её маску"""
    str_number = str(card_number)
    count = 0
    mask = ""
    for i in range(len(str_number)):
        count += 1
        if 5 < i < 12:
            mask += "*"
        else:
            mask += str_number[i]
        if count == 4:
            count = 0
            mask += " "
    return mask


def get_mask_account(account_number: Union[str, int]) -> str:
    """Принимает на вход номер счёта и возвращает его маску"""
    str_account_number = str(account_number)
    return "**" + str_account_number[-4:]
