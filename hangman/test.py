import string
import unittest

from utils import is_word_guessed

class TestIsWordGuessed(unittest.TestCase):
    secret_word = "qwer"

    def test_all(self):
        guesses = list(string.ascii_lowercase)

        self.assertTrue(is_word_guessed(self.secret_word, guesses))

    def test_correct_guesses(self):
        guesses = ["q","w","e","r"]

        self.assertTrue(is_word_guessed(self.secret_word, guesses))

    def test_incomplete_guesses(self):
        guesses = ["q","w","e"]

        self.assertFalse(is_word_guessed(self.secret_word, guesses))

    def test_incorrect_guesses(self):
        guesses = ["a","s","d","f"]

        self.assertFalse(is_word_guessed(self.secret_word, guesses))

if __name__ == '__main__':
    unittest.main(verbosity=2)
