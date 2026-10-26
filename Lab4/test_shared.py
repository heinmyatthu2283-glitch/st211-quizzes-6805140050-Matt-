def test_funded_account_balance(funded_account):
    assert funded_account.balance == 1000


def test_funded_account_after_withdrawal(funded_account):
    funded_account.withdraw(200)
    assert funded_account.balance == 800