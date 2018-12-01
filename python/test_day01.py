from unittest import TestCase

from day01 import calculate, find_reached_twice


class Day01TestCase(TestCase):

    def test_calculate_example_1(self):
        input_ = "+1, +1, +1"
        self.assertEqual(calculate(input_), 3)

    def test_calculate_example_2(self):
        input_ = "+1, +1, -2"
        self.assertEqual(calculate(input_), 0)

    def test_calculate_example_3(self):
        input_ = "-1, -2, -3"
        self.assertEqual(calculate(input_), -6)

    def test_find_reached_twice_example_1(self):
        input_ = "+1, -1"
        self.assertEqual(find_reached_twice(input_), 0)

    def test_find_reached_twice_example_2(self):
        input_ = "+3, +3, +4, -2, -4"
        self.assertEqual(find_reached_twice(input_), 10)

    def test_find_reached_twice_example_3(self):
        input_ = "-6, +3, +8, +5, -6"
        self.assertEqual(find_reached_twice(input_), 5)

    def test_find_reached_twice_example_4(self):
        input_ = "+7, +7, -2, -7, -4"
        self.assertEqual(find_reached_twice(input_), 14)
