# Design
# A function called count_words that takes a string 
# as an argument and 
# returns the number of words in that string.

"""
examples:
- 1 word -> returns 1 
- 2 words _> returns 2
- empty string -> returns 0 
- multiple words -> returns correct count 
"""

from lib.count_words import *

# Given a string with one word 
# It returns 1 

def test_returns_1_for_1_word():
    result = count_words("hello")
    assert result == 1

# Given a string with 2 words 
# It returns 2 

def test_returns_2_for_2_words():
    result = count_words("hello world")
    assert result == 2

# Given an empty string
# It returns 0 

def test_returns_0_for_empty_string():
    result = count_words("")
    assert result == 0

# Given a string with many words 
# It returns the correct count 

def test_returns_5_for_5_words():
    result = count_words ("one two three four five")
    assert result == 5