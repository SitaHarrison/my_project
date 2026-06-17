import math 

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "" :
            raise Exception("Diary entries must have a title or contents")
        self._title = title 
        self._contents = contents
    
    def format(self):
      return f"{self._title }: {self._contents}"
        
    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        contents_word_count = len(self._contents.split())
        return math.ceil(contents_word_count / wpm)
    def reading_chunk(self, wpm, minutes):
        if not hasattr(self, "_reading_position"):
            self._reading_position = 0
            
        words = self._contents.split()
        words_to_read = wpm * minutes

        start = self._reading_position
        end = start + words_to_read

        chunk = words[start:end]

        self._reading_position = end

        if self._reading_position >= len(words):
            self._reading_position = 0

        return " ".join(chunk)