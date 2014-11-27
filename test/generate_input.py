import random

class GenerateTestInput:
    
    @staticmethod
    def generate_test_input_from_word(word):
        length = len(word)
        GenerateTestInput.generate_random_case(word, length)
        GenerateTestInput.generate_vowel_mismatches(word, length)
        return GenerateTestInput.generate_char_repetitions(word, length)

    @staticmethod
    def generate_random_case(s, length):
        for i in range(length):
            if 0 == random.randint(0,2):
                s[i] = s[i].lower()
            else
                s[i] = s[i].upper()

    @staticmethod
    def generate_vowel_mismatches(s, length):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_set = set(vowels)
        num_of_vowels = len(vowels)
        for i in range(length):
            if s[i] in vowel_set:
                s[i] = vowels[random.randint(0, num_of_vowels)]

    @staticmethod
    def generate_char_repetitions(s, length):
        new_str = []
        for i in range(length):
            new_str.append([s[i]*random.randint(0, length)])

        
