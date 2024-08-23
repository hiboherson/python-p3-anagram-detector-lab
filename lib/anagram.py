# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        sorted_word = ''.join(sorted(self.word.lower()))
        return [word for word in possible_anagrams if ''.join(sorted(word.lower())) == sorted_word]
