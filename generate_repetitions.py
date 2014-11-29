from data import words
class RepetitionGenerator:
    candidates = []
    
    def __init__(self):
        self.candidates[:] = []

    def generate_possible_candidates(self, s, b, length):
        if length < 2:
            candidate = ''.join([j for i,j in enumerate(s) if b[i] ])
            if candidate in words:  
                return candidate
            else:
                self.candidates.append(candidate)
                return None
        
        match = self.generate_possible_candidates(s, b, length-1)
        if match is not None:
            return match
        if s[length-1] is s[length-2]:
            b[length-1] = False
            match = self.generate_possible_candidates(s, b, length-1)
            b[length-1] = True
        
        return match
    
    def generate_possible_candidates_helper(self, s):
        length = len(s)
        b = [True]*length
        return self.generate_possible_candidates(s, b, length)


