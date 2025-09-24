import logging
from typing import Union

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('C:/Users/Anastasiia/PycharmProjects/Nastya/logs/masks.log', encoding='utf-8',
                                   mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.
    То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками,
    номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:
    7000792289606361     # входной аргумент
    7000 79** **** 6361  # выход функции"""
    str_number = str(card_number)
    if len(str_number) == 16 and str_number.isdigit():
        logger.info("Выполняется маскировка номера карты")
        return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[12:]}"
    elif str_number == "":
        logger.error("Не был введен номер карты")
        return ""
    logger.error("Был введен некорректный номер карты")
    return "Ошибка ввода"


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску. Номер счета замаскирован
     и отображается в формате **XXXX, где X — это цифра номера. То есть видны только последние
      4 цифры номера, а перед ними — две звездочки. Пример работы функции:
      73654108430135874305  # входной аргумент
      **4305  # выход функции"""
    str_account_number = str(account_number)
    if len(str_account_number) == 20 and str_account_number.isdigit():
        logger.info("Выполняется маскировка номера счета")
        return "**" + str_account_number[-4:]
    elif str_account_number == "":
        logger.error("Не был введен номер карты")
        return ""
    logger.error("Был введен некорректный номер карты")
    return "Ошибка ввода"
