import pytest
from bank import BankAccount


@pytest.fixture
def tracked_account():
    print("[setup]")
    account = BankAccount(100)
    yield account
    print("[teardown]")


def test_deposit_with_tracking(tracked_account):
    tracked_account.deposit(50)
    assert tracked_account.balance == 150


def test_withdraw_with_tracking(tracked_account):
    tracked_account.withdraw(40)
    assert tracked_account.balance == 60