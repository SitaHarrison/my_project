import pytest
from lib.password_checker import *

def test_returns_true_for_a_valid_password_of_8_chars():
    password_checker = PasswordChecker()
    result = password_checker.check("password")
    assert result == True


def test_raises_an_error_for_a_short_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("cat")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
