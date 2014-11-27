from data import words
from collections import defaultdict

class VowelSubstitutions:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonentsWordMap = defaultdict(list)
    def __init__(self):
        self.generateConsonentWordMap()

    def removeVowelsFromWord(self, word):
        return ''.join([j for i,j in enumerate(word) if word[i] not in self.vowels])

    def generateConsonentWordMap(self):
        for word in words:
            self.consonentsWordMap[self.removeVowelsFromWord(word)].append(word)


    def matchWordToInput(self, inputStr, word, length):
        for i in range(length):
            if inputStr[i] != word[i] and (inputStr[i] not in self.vowels or word[i] not in self.vowels):
                return False

        return True

    def matchVowelSubstitutions(self, inputStr):
        consonentWord = self.removeVowelsFromWord(inputStr)
        if consonentWord == '':
            return None
        candidates = self.consonentsWordMap[consonentWord]
        inputWordLen = len(inputStr)
        for word in candidates:
            if inputWordLen == len(word) and self.matchWordToInput(inputStr, word, inputWordLen):
                return word

        return None
                 

    def generateVowelSubstitutionHelper(self, s):
        length = len(s)
        return self.generateVowelSubstitutions(list(s), 0, length)

    def generateVowelSubstitutions(self, s, index, length):
        currentStr = ''.join(s)
        if currentStr in words:
            return currentStr
        while(index < length and (s[index] not in self.vowels)):
            index+=1
        
        if(index >= length):
            return None
        
        for v in self.vowels:
            s[index] = v
            match = self.generateVowelSubstitutions(s, index+1, length)
            if match != None:
                return match

        return None


            
        
                        
        
