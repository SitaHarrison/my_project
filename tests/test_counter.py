from lib.counter import *

"""
Initially reports a count of zero
"""

def test_counter_starts_at_zero():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."
    
    """
    When we add a single number to the counter
    it is reflected in the count 
    """

def test_counter_adds_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."
"""
When we add multiple numbers to the counter 
the sum of those numbers is the final count
"""

def test_counter_adds_multiple_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 8 so far."