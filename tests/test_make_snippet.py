# Design:
# A function called make_snippet that takes a string 
# as an argument and returns the first five words and
# then a '...' if there are more than that.

from lib.make_snippet import *

# Given a string a fewer than 5 words 
# It returns the same string 

def test_returns_same_string_for_fewer_than_5_words():
    result = make_snippet("hello world")
    assert result == "hello world"

# Given a string with exactly 5 words 
# It returns the same string 

def test_returns_same_string_for_5_words():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

# Given a string with more than 5 words 
# It returns the first 5 words followed by "..."

def test_returns_snippet_for_more_than_5_words():
    result = make_snippet ("one two three four five six")
    assert result == "one two three four five..."

# Given an empty string
# It returns an empty string 

def test_returns_empty_string_for_empty_string():
    result = make_snippet("")
    assert result == ""
