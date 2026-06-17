from lib.greet import *

def test_greets_person_of_given_name():
    result = greet ("Sita")
    assert result == "Hello, Sita!"
