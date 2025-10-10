import re
from collections import Counter


def process_bank_search(data_list: list[dict], search: str) -> list[dict]:
    """Функция, которая будет принимать список словарей с данными
        о банковских операциях и строку поиска, а возвращать список словарей,
        у которых в описании есть данная строка"""
    chosen_operations = []
    for operation in data_list:
        if re.search(search, operation["description"], re.IGNORECASE):
            chosen_operations.append(operation)
    return chosen_operations


def process_bank_operations(data_list: list[dict], categories: list) -> dict:
    """Функция, которая будет принимать список словарей с данными
    о банковских операциях и список категорий операций, а возвращать словарь,
    в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории."""
    categories_list = []
    for operation in data_list:
        if operation["description"] in categories:
            categories_list.append(operation["description"])
    counted = Counter(categories_list)
    result = {}
    for key, value in counted.items():
        result[key] = value
    return result
