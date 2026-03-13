import unittest
from sources.BasicArithmeticOperations import BasicArithmeticOperations
from sources.BasicFunctions import BasicFunctions


class BasicArithmeticOperationsTest(unittest.TestCase):
    def test_add_in_twos_complement_positive(self):
        res = BasicArithmeticOperations.add_in_twos_complement("5", "5")
        expected = BasicFunctions.int_to_bits(10, 32)
        self.assertEqual(res, expected)

    def test_add_in_twos_complement_positive_negative(self):
        res = BasicArithmeticOperations.add_in_twos_complement("10", "-5")
        expected = BasicFunctions.int_to_bits(5, 32)
        self.assertEqual(res, expected)

    def test_add_in_twos_complement_negative(self):
        res = BasicArithmeticOperations.add_in_twos_complement("-5", "-5")
        expected = [1] * 32
        expected[-4:] = [0, 1, 1, 0]
        self.assertEqual(res, expected)

    def test_subtract_in_twos_complement_positive(self):
        res = BasicArithmeticOperations.subtract_in_twos_complement("10", "5")
        expected = BasicFunctions.int_to_bits(5, 32)
        self.assertEqual(res, expected)

    def test_subtract_in_twos_complement_negative_result(self):
        res = BasicArithmeticOperations.subtract_in_twos_complement("5", "10")
        expected = [1] * 32
        expected[-3:] = [0, 1, 1]
        self.assertEqual(res, expected)

    def test_subtract_in_twos_complement_with_negative(self):
        res = BasicArithmeticOperations.subtract_in_twos_complement("5", "-5")
        expected = BasicFunctions.int_to_bits(10, 32)
        self.assertEqual(res, expected)
