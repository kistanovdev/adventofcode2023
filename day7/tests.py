# test_my_functions.py

import unittest
from solution import custom_eval


class TestCustomEval(unittest.TestCase):
    def test_5_of_kind(self):
        self.assertEqual(custom_eval("AAAAA"), 0)

    def test_4_of_kind(self):
        self.assertEqual(
            custom_eval(
                "AA8AA",
            ),
            1,
        )

    def test_full_house(self):
        self.assertEqual(custom_eval("23332"), 2)

    def test_3_of_kind(self):
        self.assertEqual(custom_eval("QQQJA"), 3)
        self.assertEqual(custom_eval("TTT98"), 3)
        self.assertEqual(custom_eval("T55J5"), 3)

    def test_two_pair(self):
        self.assertEqual(custom_eval("23432"), 4)

    def test_one_pair(self):
        self.assertEqual(custom_eval("A23A4"), 5)

    def test_add(self):
        self.assertEqual(custom_eval("23456"), 6)
