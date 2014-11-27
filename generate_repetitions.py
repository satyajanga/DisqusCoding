from data import words
class GenerateRepetitions:
    candidates = []
    
    def __init__(self):
        self.candidates[:] = []

    def generatePossibleCandidates(self, s, b, length):
        if length < 2:
            candidate = ''.join([j for i,j in enumerate(s) if b[i] ])
            if candidate in words:  
                return candidate
            else:
                self.candidates.append(candidate)
                return None
        
        match = self.generatePossibleCandidates(s, b, length-1)
        if match != None:
            return match
        if s[length-1] == s[length-2]:
            b[length-1] = False
            match = self.generatePossibleCandidates(s, b, length-1)
            b[length-1] = True
        
        return match
    
    def generatePossibleCandidatesHelper(self, s):
        length = len(s)
        b = [True]*length
        return self.generatePossibleCandidates(s, b, length)


