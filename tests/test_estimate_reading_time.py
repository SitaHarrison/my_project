from lib.estimate_reading_time import *

# Given a text containing 0 words
# It returns 0
def test_returns_0_for_empty_string():
    result = estimate_reading_time("")
    assert result == 0

# Given a text containing 200 words 
# It returns 1 

def test_returns_1_for_200_words():
    result = estimate_reading_time("word " * 200)
    assert result == 1

# Given a text containing 400 words 
# It returns 2 

def test_returns_2_for_400_words():
    result = estimate_reading_time("word " * 400)
    assert result == 2

# Given a text containing 199 words 
# It returns 1 

def test_returns_1_for_199_words():
    result = estimate_reading_time("word " * 199)
    assert result == 1

# Given a text containing 201 words 
# It returns 2 
def test_returns_2_for_201_words():
    result = estimate_reading_time("word " * 201)
    assert result == 2