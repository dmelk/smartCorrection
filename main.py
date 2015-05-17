from Dictionary import *
from EnglishQwertyLetters import *

letter_operations = EnglishQwertyLetters()
dictionary = Dictionary('corncob_lowercase.txt', letter_operations)
dictionary.transform('input.txt', 0.3)
