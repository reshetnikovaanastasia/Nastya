from typing import Iterable
import datetime


def filter_by_state(list_data_dictionaries: Iterable[list], state='EXECUTED') -> Iterable[list]:
    """ Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'). Функция возвращает
    новый список словарей, содержащий только те словари, у которых ключ 'state' соответствует указанному значению"""
    new_list_data = []
    for data_dictionary in list_data_dictionaries:
        if data_dictionary['state'] == state:
            new_list_data.append(data_dictionary)
    return new_list_data


def sort_by_date(list_data_dictionaries: Iterable[list], data_key="date", direction=True) -> Iterable[list]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция должна
    возвращать новый список, отсортированный по дате (date)"""
    return sorted(list_data_dictionaries, key=lambda x: datetime.datetime.strptime(x[data_key], '%Y-%m-%dT%H:%M:%S.%f'),
                  reverse=direction)
