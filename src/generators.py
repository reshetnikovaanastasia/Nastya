def filter_by_currency(transactions, selected_currency):
    """ Принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == selected_currency:
            yield transaction


def transaction_descriptions(transactions):
    """Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(beginning, end):
    """ Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
    start = str(beginning)
    for i in range(beginning, end + 1):
        yield f"{start.zfill(16)[:4]} {start.zfill(16)[4:8]} {start.zfill(16)[8:12]} {start.zfill(16)[12:]}"
        beginning += 1
        start = str(beginning)
