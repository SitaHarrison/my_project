from lib.string_builder import *

"""
Initially the output is an empty string
"""

def test_initially_output_is_an_empty_string ():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

"""
When we add a single string
The output is now that string 
"""

def test_adding_a_string_outputs_that_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"

"""
When we add a single string 
The size reflects the size of that string 
"""
def test_adding_a_string_sets_size_to_that_strings_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.size() == 5

"""
When we add multiple strings 
The output is those strings concatenated 
"""
def test_adding_multiple_strings_outputs_concatenated_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.output() == "hello world"

"""
When we add multiple strings 
The size is the size of all the strings added 
"""

def test_adding_multiple_strings_has_total_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.size() == 11