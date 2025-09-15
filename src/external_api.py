import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_transaction_amount_rub(transaction):
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float. Если транзакция была в USD или EUR, происходит обращение
    к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""
    url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
    amount = transaction["operationAmount"]["amount"]
    payload = {}
    headers = {"apikey": API_KEY}
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(amount)
    if transaction["operationAmount"]["currency"]["code"] == "USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
    if transaction["operationAmount"]["currency"]["code"] == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    status_code = response.status_code
    return float(data['result'])
