#!/usr/bin/python
import generate_repetitions as gr
import vowel_substitutions as vs
from data import words

def setCharsLenToTwo(s):
     return ''.join([j for i,j in enumerate(s) if i<2 or (s[i-1] != s[i-2] or s[i-1] != j)])  

vowelSubs = vs.VowelSubstitutions()

while True:
    inputStr = raw_input("> ").lower()
    if inputStr in words:
        print inputStr
        continue

    inputStr = setCharsLenToTwo(inputStr)    
    if inputStr in words:
        print inputStr
        continue

    repetetions = gr.GenerateRepetitions()
    suggestion = repetetions.generatePossibleCandidatesHelper(inputStr)
    if suggestion == None:
        for candidate in repetetions.candidates:
            suggestion = vowelSubs.matchVowelSubstitutions(candidate)
            if suggestion != None:
                break

            
    if suggestion == None:
        print "NO SUGGESTION"
    else:
        print suggestion
