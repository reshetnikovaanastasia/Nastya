import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY=os.getenv('API_KEY')
def get_transaction_amount_rub(transaction):
    url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
    amount=transaction["operationAmount"]["amount"]
    payload = {}
    headers = {"apikey": API_KEY}
    if transaction["operationAmount"]["currency"]["code"]=="RUB":
        return amount
    if transaction["operationAmount"]["currency"]["code"]=="USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
    if transaction["operationAmount"]["currency"]["code"]=="EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
    response = requests.request("GET", url, headers=headers, data=payload)
    data=response.json()
    status_code = response.status_code
    return data['result']

print(get_transaction_amount_rub({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "1",
      "currency": {
        "name": "EUR",
        "code": "EUR"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))
