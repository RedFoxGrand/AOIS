import unittest
from sources.AdvancedArithmeticOperations import AdvancedArithmeticOperations


class AdvancedArithmeticOperationsTest(unittest.TestCase):
    def test_multiply_positive(self):
        res = AdvancedArithmeticOperations.multiply_in_sign_magnitude("5", "5")
        expected = [0] * 32
        expected[-5:] = [1, 1, 0, 0, 1]
        self.assertEqual(res, expected)

    def test_multiply_negative(self):
        res = AdvancedArithmeticOperations.multiply_in_sign_magnitude("-5", "5")
        expected = [0] * 32
        expected[0] = 1
        expected[-5:] = [1, 1, 0, 0, 1]
        self.assertEqual(res, expected)

    def test_multiply_zero(self):
        res = AdvancedArithmeticOperations.multiply_in_sign_magnitude("10", "0")
        expected = [0] * 32
        self.assertEqual(res, expected)

    def test_divide_integer_result(self):
        res = AdvancedArithmeticOperations.divide_in_sign_magnitude("10", "2")
        expected = [0] * 32
        expected[13:16] = [1, 0, 1]
        self.assertEqual(res, expected)

    def test_divide_fractional_result(self):
        res = AdvancedArithmeticOperations.divide_in_sign_magnitude("5", "2")
        expected = [0] * 32
        expected[14:16] = [1, 0]
        expected[16] = 1
        self.assertEqual(res, expected)

    def test_divide_negative(self):
        res = AdvancedArithmeticOperations.divide_in_sign_magnitude("-10", "2")
        expected = [0] * 32
        expected[0] = 1
        expected[13:16] = [1, 0, 1]
        self.assertEqual(res, expected)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            AdvancedArithmeticOperations.divide_in_sign_magnitude("10", "0")
