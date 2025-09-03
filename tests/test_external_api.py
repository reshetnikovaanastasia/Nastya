from unittest.mock import patch

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
    assert get_transaction_amount_rub(transaction) == "100.0"
    mock_request.assert_not_called()
