import json
import os
from json import JSONDecodeError


def load_transaction_data(file_path):
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    try:
        try:
            if os.path.getsize(file_path) == 0:
                return []
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except JSONDecodeError:
            return []
        return data
    except FileNotFoundError:
        return []


# Необходимо указать абсолютный путь к файлу для корректной работы
print(load_transaction_data('C:/Users/Anastasiia/PycharmProjects/Nastya/data/operations.json'))
