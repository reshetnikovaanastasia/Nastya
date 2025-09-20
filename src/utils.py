import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('C:/Users/Anastasiia/PycharmProjects/Nastya/logs/utils.log', encoding='utf-8',
                                   mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transaction_data(file_path):
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Чтение JSON-файла")
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        logger.error("Ошибка чтения JSON-файла")
        return []
    except FileNotFoundError:
        logger.error("Программа не может найти JSON-файл")
        return []
