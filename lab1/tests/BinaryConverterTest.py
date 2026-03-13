import unittest
from sources.BinaryConverter import BinaryConverter


class BinaryConverterTest(unittest.TestCase):
    def test_sign_magnitude_positive(self):
        res = BinaryConverter.converting_to_sign_magnitude("5")
        expected = [0] * 32
        expected[-3:] = [1, 0, 1]
        self.assertEqual(res, expected)

    def test_sign_magnitude_negative(self):
        res = BinaryConverter.converting_to_sign_magnitude("-5")
        expected = [0] * 32
        expected[0] = 1
        expected[-3:] = [1, 0, 1]
        self.assertEqual(res, expected)

    def test_ones_complement_positive(self):
        res = BinaryConverter.converting_to_ones_complement("5")
        expected = [0] * 32
        expected[-3:] = [1, 0, 1]
        self.assertEqual(res, expected)

    def test_ones_complement_negative(self):
        res = BinaryConverter.converting_to_ones_complement("-5")
        expected = [1] * 32
        expected[-3:] = [0, 1, 0]
        self.assertEqual(res, expected)

    def test_twos_complement_positive(self):
        res = BinaryConverter.converting_to_twos_complement("5")
        expected = [0] * 32
        expected[-3:] = [1, 0, 1]
        self.assertEqual(res, expected)

    def test_twos_complement_negative(self):
        res = BinaryConverter.converting_to_twos_complement("-5")
        expected = [1] * 32
        expected[-3:] = [0, 1, 1]
        self.assertEqual(res, expected)
