import json
from json import JSONDecodeError


def load_transaction_data(file_path):
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        return []
    except FileNotFoundError:
        return []
