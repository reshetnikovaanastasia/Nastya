def filter_by_state(list_data_dictionaries: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'). Функция
    возвращает новый список словарей, содержащий только те словари, у которых ключ 'state' соответствует
    указанному значению"""
    new_list_data = []
    for data_dictionary in list_data_dictionaries:
        if data_dictionary['state'] == state:
            new_list_data.append(data_dictionary)
    return new_list_data


def sort_by_date(list_data_dictionaries: list[dict], sorting: bool = True) -> list[dict]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)"""
    sorted_state = sorted(list_data_dictionaries, key=lambda x: x["date"], reverse=sorting)
    return sorted_state
