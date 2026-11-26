from access import check_access


def test_active_admin_is_granted_access():
    assert check_access("admin", True) == "granted"


def test_inactive_admin_is_denied_access():
    assert check_access("admin", False) == "denied"


def test_active_user_is_denied_access():
    assert check_access("user", True) == "denied"


def test_inactive_user_is_denied_access():
    assert check_access("user", False) == "denied"