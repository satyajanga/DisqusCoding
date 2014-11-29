from test_input_generator import TestInputGenerator

import sys
sys.path.append("../")
from data import words

for word in words:
    print TestInputGenerator.generate_test_input_from_word(list(word))


