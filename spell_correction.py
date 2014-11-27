#!/usr/bin/python
import generate_repetitions as gr
import vowel_substitutions as vs
from data import words

def limit_chars_len_to_two(s):
     return ''.join([j for i,j in enumerate(s) if i<2 or (s[i-1] != s[i-2] or s[i-1] != j)])  

vowelSubs = vs.VowelSubstitutions()

while True:
    input_str = raw_input("> ").lower()
    if input_str in words:
        print input_str
        continue

    inputStr = limit_chars_len_to_two(input_str)    
    if input_str in words:
        print input_str
        continue

    repetetions = gr.GenerateRepetitions()
    suggestion = repetetions.generate_possible_candidates_helper(input_str)
    if suggestion == None:
        for candidate in repetetions.candidates:
            suggestion = vowelSubs.match_vowel_substitutions(candidate)
            if suggestion != None:
                break

            
    if suggestion == None:
        print "NO SUGGESTION"
    else:
        print suggestion
