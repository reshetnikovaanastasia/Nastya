from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.receiving import reading_csv, reading_excel
from src.refunctions import process_bank_search
from src.utils import load_transaction_data
from src.widget import mask_account_card, get_date
from src.masks import get_mask_account, get_mask_card_number


def main():
    """Основная логика проекта и связывает функциональности между собой"""
    selected_action = int(input("Привет! Добро пожаловать в программу работы "
                                "с банковскими транзакциями.\nВыберите необходимый пункт меню:\n1. Получить "
                                "информацию о транзакциях из JSON - файла\n2. Получить информацию о "
                                "транзакциях из CSV - файла\n3. Получить информацию о транзакциях из "
                                "XLSX - файла\n"))
    if selected_action == 1:
        processed_list = load_transaction_data("C:/Users/Anastasiia/PycharmProjects/Nastya/data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif selected_action == 2:
        processed_list = reading_csv("C:/Users/Anastasiia/PycharmProjects/Nastya/data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif selected_action == 3:
        processed_list = reading_excel("C:/Users/Anastasiia/PycharmProjects/Nastya/data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Выбран неверный номер")
    while True:
        status = str(input("Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные "
                           "для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")).upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            sort_list = filter_by_state(processed_list, status)
            break
        else:
            print(f'Статус операции {status} недоступен')
    question1 = str(input("Отсортировать операции по дате? Да/Нет\n"))
    if question1.lower == "да":
        question2 = str(input("Отсортировать по возрастанию или по убыванию?\n"))
        if question2.lower() == "по возрастанию":
            date_sort_list = sort_by_date(sort_list, False)
        else:
            date_sort_list = sort_by_date(sort_list, True)
    else:
        date_sort_list = sort_list
    question3 = str(input("Выводить только рублевые транзакции? Да/Нет\n"))
    if question3.lower() == "да":
        rub_date_sort_list = filter_by_currency(date_sort_list, "RUB")
    else:
        rub_date_sort_list = date_sort_list
    question4 = str(input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"))
    if question4.lower() == "да":
        word = str(input("Введите слово"))
        word_sort_list = process_bank_search(rub_date_sort_list, word)
    else:
        word_sort_list = rub_date_sort_list
    print("Распечатываю итоговый список транзакций...")
    if len(word_sort_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(word_sort_list)}")
        for i in word_sort_list:
            date = get_date(i['date'])
            print(f"{date} {i['description']}")
            mask_from = mask_account_card(i['from'])
            mask_to = mask_account_card(i["to"])
            print(f"{mask_from} -> {mask_to}")
            print(f"Сумма {i['amount']} {i['currency_code']}")
            print("")


print(main())
