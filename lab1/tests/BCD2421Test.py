import unittest
from sources.BCD2421 import BCD2421
from sources.Verification import Verification


class BCD2421Test(unittest.TestCase):
    def test_convert_positive(self):
        res = BCD2421.decimal_number_to_2421("12")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, 12)

    def test_convert_negative(self):
        res = BCD2421.decimal_number_to_2421("-12")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, -12)

    def test_convert_zero(self):
        res = BCD2421.decimal_number_to_2421("0")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, 0)

    def test_convert_large_positive(self):
        res = BCD2421.decimal_number_to_2421("542")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, 542)

    def test_add_positive(self):
        res = BCD2421.add_in_bcd_2421("163", "379")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, 542)

    def test_add_positive_negative(self):
        res = BCD2421.add_in_bcd_2421("19", "-7")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, 12)

    def test_add_negative_positive(self):
        res = BCD2421.add_in_bcd_2421("-19", "7")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, -12)

    def test_add_negative_negative(self):
        res = BCD2421.add_in_bcd_2421("-5", "-17")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, -22)

    def test_add_with_zero(self):
        res = BCD2421.add_in_bcd_2421("30", "0")
        val = Verification.bcd2421_to_decimal(res)
        self.assertEqual(val, 30)
