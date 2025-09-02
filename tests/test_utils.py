from unittest.mock import mock_open, patch
from src.utils import load_transaction_data


def test_load_transaction_data():
    with patch("builtins.open",mock_open(read_data='{"1":"2"}')):
        assert load_transaction_data("")=={"1":"2"}

    with patch("builtins.open",mock_open(read_data='{"1":"2"')):
        assert load_transaction_data("")==[]
    assert load_transaction_data("")==[]

