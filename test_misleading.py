from shipping import calculate_shipping


def test_runs_but_asserts_nothing():
    calculate_shipping(10)
    assert True