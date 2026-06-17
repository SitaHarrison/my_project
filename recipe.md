# Single-Function Design Recipe

## 1. Describe the Problem

> As a user,
> so that I can manage my time, I want to see an estimate of reading time for a text
> assuming that I can read 200 words a minute.

> Clarifying notes: 
> Reading speed is assumed to be 200 words per minute.
> The function returns whole minutes as an integer.
> Partial minutes are rounded up to the nearest whole minute.


## 2. Design the Function Signature

```python
function: 
def estimate_reading_time(text):

parameters:
    text: a string 

returns:
    an integer representing the estimated reading time in mins

side effects: 
    None
```

## 3. Create Examples as Tests

```python

Given a text containing 0 words
It returns 0

def estimate_reading_time("") => 0

Given a text containing 200 words 
It returns 1 

def estimate_reading_time ("word word word...") => 1

Given a text containing 400 words 
It returns 2

def estimate_reading_time ("word word word...") => 2

Given a text containing 199 words 
It returns 1

def estimate_reading_time ("word word word...") => 1

Given a text containing 201 words 
It returns 2

def estimate_reading_time ("word word word...") => 2
```

## 4. Implement the Behaviour

```python

from lib.estimate_reading_time import *

Given a text containing 0 words
It returns 0

def test_returns_0_for_empty_string():
    result = estimate_reading_time("")
    assert result == 0

```

