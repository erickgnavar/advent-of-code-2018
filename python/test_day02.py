from unittest import TestCase

from day02 import count_letters


class Day02TestCase(TestCase):

    def test_count_letters_example_1(self):
        input_ = "abcdef"
        self.assertEqual(count_letters(input_), (False, False))

    def test_count_letters_example_2(self):
        input_ = "bababc"
        self.assertEqual(count_letters(input_), (True, True))

    def test_count_letters_example_3(self):
        input_ = "abbcde"
        self.assertEqual(count_letters(input_), (True, False))

    def test_count_letters_example_4(self):
        input_ = "abcccd"
        self.assertEqual(count_letters(input_), (False, True))

    def test_count_letters_example_5(self):
        input_ = "aabcdd"
        self.assertEqual(count_letters(input_), (True, False))

    def test_count_letters_example_6(self):
        input_ = "abcdee"
        self.assertEqual(count_letters(input_), (True, False))

    def test_count_letters_example_7(self):
        input_ = "ababab"
        self.assertEqual(count_letters(input_), (False, True))
