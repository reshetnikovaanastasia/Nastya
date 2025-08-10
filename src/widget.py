from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_type_and_number: str) -> str:
    """Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Аргументом может быть строка типа Visa Platinum 7000792289606361, или
    Maestro 7000792289606361, или Счет 73654108430135874305.
    Возвращает строку с замаскированным номером."""
    differentiation = card_type_and_number.rfind(" ")
    if card_type_and_number[:differentiation] == "Счет":
        if card_type_and_number[-20:].isdigit():
            masks_number = get_mask_account(card_type_and_number[differentiation + 1:])
            return "Счет " + masks_number
        else:
            return "Ошибка ввода"
    elif card_type_and_number[-16:].isdigit():
        numbers_mask = get_mask_card_number(card_type_and_number[differentiation + 1:])
        return card_type_and_number[: differentiation + 1] + numbers_mask
    else:
        return "Ошибка ввода"


def get_date(date: str) -> str:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    if date[8:10].isdigit() and date[5:7].isdigit() and date[:4].isdigit():
        return date[8:10] + "." + date[5:7] + "." + date[:4]
    else:
        return "Некорректный формат времени"
