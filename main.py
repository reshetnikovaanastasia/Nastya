import os

# import requests
from dotenv import load_dotenv

from src.masks import get_mask_account, get_mask_card_number
# from src.external_api import get_transaction_amount_rub
from src.utils import load_transaction_data

load_dotenv()
API_KEY = os.getenv('API_KEY')

if __name__ == "__main__":
    # print(get_transaction_amount_rub({
    #     "id": 939719570,
    #     "state": "EXECUTED",
    #     "date": "2018-06-30T02:08:58.425572",
    #     "operationAmount": {
    #         "amount": "8221.37",
    #         "currency": {
    #             "name": "USD",
    #             "code": "USD"
    #         }
    #     }
    # }))

    print(load_transaction_data(r'С:\Users\Anastasiia\PycharmProjects\Nastya\data\operations.json'))

    print(get_mask_card_number("7000792289606361"))
    print(get_mask_card_number(""))
    print(get_mask_account("73654108430135874305"))
    print(get_mask_account("ghjhgjh"))
