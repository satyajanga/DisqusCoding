import random

class TestInputGenerator:
    
    @staticmethod
    def generate_test_input_from_word(word):
        length = len(word)
        TestInputGenerator.generate_random_case(word, length)
        TestInputGenerator.generate_vowel_mismatches(word, length)
        return TestInputGenerator.generate_char_repetitions(word, length)

    @staticmethod
    def generate_random_case(s, length):
        for i in range(length):
            if random.randint(0,1) is 0:
                s[i] = s[i].lower()
            else:
                s[i] = s[i].upper()

    @staticmethod
    def generate_vowel_mismatches(s, length):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_set = set(vowels)
        num_of_vowels = len(vowels)
        for i in range(length):
            if s[i] in vowel_set:
                s[i] = vowels[random.randint(0, num_of_vowels-1)]

    @staticmethod
    def generate_char_repetitions(s, length):
        new_str = []
        for i in range(length):
            if random.randint(0,2) is 0:
                new_str += [s[i]]*random.randint(1, length)
            else:
                new_str+= [s[i]]

        return ''.join(new_str)
