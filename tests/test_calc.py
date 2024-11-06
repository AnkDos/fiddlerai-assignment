import pytest
from src import Spreadsheet


def test_basic_evaluation():
    spreadsheet = Spreadsheet(3, 2, ["A2", "4 5 *", "A1", "A1 B2 / 2 +", "3", "39 B1 B2 * /"])
    output = spreadsheet.evaluate()
    expected = ["20.00000", "20.00000", "20.00000", "8.66667", "3.00000", "1.50000"]
    assert output == expected


def test_increment_decrement():
    spreadsheet = Spreadsheet(2, 2, ["5 ++", "10 --", "A1 ++", "A2 --"])
    output = spreadsheet.evaluate()
    expected = ["6.00000", "9.00000", "7.00000", "8.00000"]
    assert output == expected


def test_cyclic_dependency():
    spreadsheet = Spreadsheet(2, 2, ["B1", "A1"])
    with pytest.raises(Exception):
        spreadsheet.evaluate()
