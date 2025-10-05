from unittest.mock import MagicMock, mock_open, patch

from src.receiving import reading_csv, reading_excel


def test_reading_csv():
    mock_csv = """id;amount;date;description
1;100;2023-01-01;Transaction 1
2;200;2023-01-02;Transaction 2"""
    with patch("builtins.open", mock_open(read_data=mock_csv)):
        with patch('csv.DictReader') as mock_reader:
            mock_reader.return_value = [
                {"id": "1", "amount": "100", "date": "2023-01-01", "description": "Transaction 1"},
                {"id": "2", "amount": "200", "date": "2023-01-02", "description": "Transaction 2"}
            ]
            result = reading_csv("test.csv")

            assert len(result) == 2
            assert result[0]["id"] == "1"
            assert result[1]["amount"] == "200"


def test_empty_file_csv():
    with patch('builtins.open', mock_open(read_data="id;amount;date;description\n")):
        with patch('csv.DictReader') as mock_reader:
            mock_reader.return_value = []  # Пустой список

            result = reading_csv("empty.csv")

            assert result == []


def test_reading_excel():
    # Создаем мок DataFrame
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"id": 1, "amount": 100, "date": "2023-01-01"},
        {"id": 2, "amount": 200, "date": "2023-01-02"}
    ]

    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = mock_df

        result = reading_excel("test.xlsx")

        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[1]["amount"] == 200

        mock_read_excel.assert_called_once_with("test.xlsx")
        mock_df.to_dict.assert_called_once_with(orient="records")


def test_empty_file_reading_excel():
    mock_df = MagicMock()
    mock_df.to_dict.return_value = []

    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = mock_df

        result = reading_excel("empty.xlsx")

        assert result == []
        mock_read_excel.assert_called_once_with("empty.xlsx")
