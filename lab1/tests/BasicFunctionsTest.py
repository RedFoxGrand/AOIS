import unittest
from sources.BasicFunctions import BasicFunctions


class BasicFunctionsTest(unittest.TestCase):
    def test_create_empty_bits_default(self):
        bits = BasicFunctions.create_empty_bits()
        self.assertEqual(len(bits), 32)
        self.assertTrue(all(b == 0 for b in bits))

    def test_create_empty_bits_custom(self):
        length = 10
        bits = BasicFunctions.create_empty_bits(length)
        self.assertEqual(len(bits), length)
        self.assertTrue(all(b == 0 for b in bits))

    def test_int_to_bits_zero(self):
        bits = BasicFunctions.int_to_bits(0, 8)
        self.assertEqual(bits, [0, 0, 0, 0, 0, 0, 0, 0])

    def test_int_to_bits_value(self):
        bits = BasicFunctions.int_to_bits(5, 4)
        self.assertEqual(bits, [0, 1, 0, 1])

    def test_int_to_bits_truncation(self):
        bits = BasicFunctions.int_to_bits(5, 2)
        self.assertEqual(bits, [0, 1])

    # Тесты для bin_to_int
    def test_bin_to_int_zero(self):
        val = BasicFunctions.bin_to_int([0, 0, 0, 0])
        self.assertEqual(val, 0)

    def test_bin_to_int_value(self):
        val = BasicFunctions.bin_to_int([0, 1, 0, 1])
        self.assertEqual(val, 5)

    def test_bin_to_int_empty(self):
        self.assertEqual(BasicFunctions.bin_to_int([]), 0)
