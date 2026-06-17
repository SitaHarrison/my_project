import math 

WORDS_PER_MINUTE = 200 

def estimate_reading_time(text):
    word_count = len(text.split())
    return math.ceil(word_count / WORDS_PER_MINUTE)
