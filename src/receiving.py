import pandas as pd
import csv


def reading_csv(path):
    '''Функция для считывания финансовых операций из CSV принимает путь к файлу CSV
    в качестве аргумента, выдает список словарей с транзакциями.'''
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=";")
        result = []
        for row in reader:
            result.append(row)
        return result


# print(reading_csv(r'C:\Users\Anastasiia\PycharmProjects\Nastya\data\transactions.csv'))

def reading_excel(path):
    '''Функция для считывания финансовых операций из Excel принимает путь к файлу Excel
        в качестве аргумента, выдает список словарей с транзакциями.'''
    df = pd.read_excel(path)
    return df.to_dict(orient="records")


# print(reading_excel(r'C:\Users\Anastasiia\PycharmProjects\Nastya\data\transactions_excel.xlsx'))
