#!/usr/bin/python
from generate_repetitions import RepetitionGenerator
from vowel_replacer import VowelReplacer
from data import words, VOWELS

class SpellSuggester:
    vowel_subs = VowelReplacer()
    
    def limit_chars_len_to_two(self, s):
        return ''.join([j for i,j in enumerate(s) if (i<2 or (j is not s[i-1] or j is not s[i-2])) or (i> 3 and j in VOWELS and s[i-3] is not j )])  

    def scan_input(self):
        return raw_input("> ").lower()
    
    def start(self):
        while True:
            input_str = self.scan_input()
            if input_str in words:
                print input_str
                continue
            
            input_str = self.limit_chars_len_to_two(input_str)    
            if input_str in words:
                print input_str
                continue
            print self.process_and_suggest_spelling(input_str)


    def scan_and_process_input(self):    
        while True:
            input_str = self.scan_input()
            if input_str in words:
                print input_str
                continue


    def process_and_suggest_spelling(self, input_str):
        repetitions = RepetitionGenerator()
        suggestion = repetitions.generate_possible_candidates_helper(input_str)
        if suggestion is None:
            for candidate in repetitions.candidates:
                suggestion = self.vowel_subs.match_vowel_substitutions(candidate)
                if suggestion != None:
                    return suggestion
        else:
            return suggestion

        return "NO SUGGESTION"
