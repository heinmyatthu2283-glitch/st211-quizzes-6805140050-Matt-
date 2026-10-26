from bank import BankAccount

def test_deposit_increases_balance():
    account = BankAccount(balance=100)   # Arrange
    new_balance = account.deposit(50)    # Act
    assert new_balance == 150            # Assert