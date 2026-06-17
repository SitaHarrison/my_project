import pytest 
from lib.present import *

# Unwrapping an empty present raises an error
def test_unwrapping_without_contents_raises_an_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


# Wrapping and unwrapping returns the contents
def test_wrap_and_unwrap_returns_the_contents():
    present = Present()
    present.wrap("Book")
    assert present.unwrap() == "Book"


# Wrapping an already wrapped present raises an error
def test_wrapping_twice_raises_an_error():
    present = Present()
    present.wrap("Book")
    with pytest.raises(Exception) as e:
        present.wrap("Chocolate")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."