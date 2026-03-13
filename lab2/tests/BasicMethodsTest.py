import unittest
from sources.BasicMethods import BasicMethods


class BasicMethodsTest(unittest.TestCase):
    def test_generate_combinations(self):
        expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.assertEqual(BasicMethods.generate_combinations(2), expected)

    def test_int_to_bits(self):
        self.assertEqual(BasicMethods.int_to_bits(0), "0")
        self.assertEqual(BasicMethods.int_to_bits(2), "10")
        self.assertEqual(BasicMethods.int_to_bits(5), "101")