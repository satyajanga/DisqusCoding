from data import words
from collections import defaultdict

class VowelSubstitutions:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonents_word_map = defaultdict(list)
    def __init__(self):
        self.generate_consonent_word_map()

    def remove_vowels_from_word(self, word):
        return ''.join([j for i,j in enumerate(word) if word[i] not in self.vowels])

    def generate_consonent_word_map(self):
        for word in words:
            self.consonents_word_map[self.remove_vowels_from_word(word)].append(word)


    def match_word_to_input(self, input_str, word, length):
        for i in range(length):
            if input_str[i] != word[i] and (input_str[i] not in self.vowels or word[i] not in self.vowels):
                return False

        return True

    def match_vowel_substitutions(self, input_str):
        consonent_word = self.remove_vowels_from_word(input_str)
        if consonent_word == '':
            return None
        candidates = self.consonents_word_map[consonent_word]
        input_word_len = len(input_str)
        for word in candidates:
            if input_word_len == len(word) and self.match_word_to_input(input_str, word, input_word_len):
                return word

        return None
