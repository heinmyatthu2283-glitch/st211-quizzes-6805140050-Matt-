import pytest

from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150


def test_deposit_another_amount(account):
    account.deposit(100)
    assert account.balance == 200


def test_multiple_deposits(account):
    account.deposit(50)
    account.deposit(25)
    assert account.balance == 175