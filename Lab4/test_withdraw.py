import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70

def test_overdraft(account):
    with pytest.raises(ValueError):
        account.withdraw(150)