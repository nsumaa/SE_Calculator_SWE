# test_bitwise.py
import unittest
from calculator import Calculator

class TestBitwise(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_bitwise_and(self):
        self.assertEqual(self.calc.calculate("12 & 10"), 8)

    def test_bitwise_or(self):
        self.assertEqual(self.calc.calculate("12 | 10"), 14)

    def test_bitwise_lshift(self):
        self.assertEqual(self.calc.calculate("3 << 2"), 12)

    def test_bitwise_not(self):
        self.assertEqual(self.calc.calculate("~0"), -1)

    def test_mixed_expression(self):
        self.assertEqual(self.calc.calculate("2 + (1 << 3)"), 10)

if __name__ == "__main__":
    unittest.main()