import pytest 
from lib.diary_entry import *

# Given an empty title and contents 
# Raises an error 

def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry ("", "")
    
    assert str(err.value) == "Diary entries must have a title or contents"


# Given a title and contents 
# format returns a formatted entry, like:
# "My Title: These are the contents"

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry ("My Title" , "Some contents")
    result= diary_entry.format()
    assert result == "My Title: Some contents"

# Given a title and contents 
# count_words returns the number of words 
# in the title and contents 

def test_counts_words_in_both_title_and_contents():
    diary_entry = DiaryEntry ("My Title" , "Some contents")
    result = diary_entry.count_words()
    assert result == 4                            

# Given a wpm of 2
# And a text with 2 words 
# reading_time returns 1 minute 

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry ("My Title" , "one two")
    result = diary_entry.reading_time(2)
    assert result == 1 

# Given a wpm of 2
# And a text with 4 words 
# reading_time returns 2 minutes

def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntry ("My Title" , " one two three four")
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_chunk_returns_first_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"


def test_reading_chunk_returns_next_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four")
    diary_entry.reading_chunk(2, 1)
    result = diary_entry.reading_chunk(2, 1)
    assert result == "three four"


def test_reading_chunk_restarts_after_finishing():
    diary_entry = DiaryEntry("My Title", "one two three four")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"
