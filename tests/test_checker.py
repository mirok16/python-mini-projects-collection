from password_checker.checker import is_valid

def test_valid_password():
    assert is_valid("Password1")
