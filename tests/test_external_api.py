from unittest.mock import patch, Mock

from src.external_api import get_transaction_amount_rub


@patch('src.external_api.requests.request')
def test_rub_transaction_returns_same_amount(mock_request):
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "RUB"
            }
        }
    }
    assert get_transaction_amount_rub(transaction) == 100.0
    mock_request.assert_not_called()

@patch('requests.request')
def test_external_api(mock_request):
    mock_response=Mock()
    mock_response.json.return_value={'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                                     'info': {'timestamp': 1757774827, 'rate': 83.75163},
                                     'date': '2025-09-13', 'result': 688553.138333}
    transaction = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    }
    assert get_transaction_amount_rub(transaction) == 1.0
