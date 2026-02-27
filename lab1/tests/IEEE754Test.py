import unittest
from sources.IEEE754 import IEEE754
from sources.Verification import Verification


class IEEE754Test(unittest.TestCase):
    def test_convert_positive(self):
        res = IEEE754.converting_from_decimal_to_ieee754("22.15625")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, 22.15625)

    def test_convert_negative(self):
        res = IEEE754.converting_from_decimal_to_ieee754("-22.15625")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, -22.15625)

    def test_convert_small_number(self):
        res = IEEE754.converting_from_decimal_to_ieee754("0.0001")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, 0.0001, places=7)

    def test_convert_zero(self):
        res = IEEE754.converting_from_decimal_to_ieee754("0.0")
        val = Verification.ieee754_to_decimal(res)
        self.assertEqual(val, 0.0)

    def test_add_positive(self):
        res = IEEE754.add_in_ieee754("22.15625", "11.25")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, 33.40625)

    def test_add_positive_negative(self):
        res = IEEE754.add_in_ieee754("22.15625", "-27")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, -4.84375)

    def test_add_zero(self):
        res = IEEE754.add_in_ieee754("123.45", "0")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, 123.45, places=5)

    def test_subtract_positive(self):
        res = IEEE754.subtract_in_ieee754("22.15625", "1.1")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, 21.05625, places=5)

    def test_subtract_to_negative(self):
        res = IEEE754.subtract_in_ieee754("10.5", "20.5")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, -10.0)

    def test_multiply_positive(self):
        res = IEEE754.multiply_in_ieee754("22.15625", "2.0")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, 44.3125)

    def test_multiply_negative(self):
        res = IEEE754.multiply_in_ieee754("10.0", "-4.0")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, -40.0)

    def test_multiply_zero(self):
        res = IEEE754.multiply_in_ieee754("123.456", "0")
        val = Verification.ieee754_to_decimal(res)
        self.assertEqual(val, 0.0)

    def test_divide_positive(self):
        res = IEEE754.divide_in_ieee754("22.15625", "2.0")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, 11.078125)

    def test_divide_fractional_result(self):
        res = IEEE754.divide_in_ieee754("1.0", "4.0")
        val = Verification.ieee754_to_decimal(res)
        self.assertAlmostEqual(val, 0.25)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            IEEE754.divide_in_ieee754("10.0", "0.0")
