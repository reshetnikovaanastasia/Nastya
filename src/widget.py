from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_type_and_number: str) -> str:
    """Обработка информации о картах и счетах"""
    if card_type_and_number[:4] == "Счет":
        masks_number = get_mask_account(card_type_and_number[5:])
        return "Счет " + masks_number
    else:
        numbers = "".join([i for i in card_type_and_number if i.isdigit()])
        numbers_mask = get_mask_card_number(numbers)
        return card_type_and_number.replace(numbers, "") + numbers_mask


def get_date(date: str) -> str:
    """Возвращает строку с датой"""
    return date[8:10] + "." + date[5:7] + "." + date[:4]
