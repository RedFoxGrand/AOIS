import unittest
from sources.Verification import Verification


class VerificationTest(unittest.TestCase):
    def test_sign_magnitude_positive(self):
        bits = [0] * 32
        bits[-3:] = [1, 0, 1]
        self.assertEqual(Verification.sign_magnitude_to_decimal(bits), 5)

    def test_sign_magnitude_negative(self):
        bits = [0] * 32
        bits[0] = 1
        bits[-3:] = [1, 0, 1]
        self.assertEqual(Verification.sign_magnitude_to_decimal(bits), -5)

    def test_ones_complement_positive(self):
        bits = [0] * 32
        bits[-3:] = [1, 0, 1]
        self.assertEqual(Verification.ones_complement_to_decimal(bits), 5)

    def test_ones_complement_negative(self):
        bits = [1] * 32
        bits[-3:] = [0, 1, 0]
        self.assertEqual(Verification.ones_complement_to_decimal(bits), -5)

    def test_twos_complement_positive(self):
        bits = [0] * 32
        bits[-3:] = [1, 0, 1]  # 5
        self.assertEqual(Verification.twos_complement_to_decimal(bits), 5)

    def test_twos_complement_negative(self):
        bits = [1] * 32
        bits[-3:] = [0, 1, 1]
        self.assertEqual(Verification.twos_complement_to_decimal(bits), -5)

    def test_division_integer(self):
        bits = [0] * 32
        bits[13:16] = [1, 0, 1]
        self.assertEqual(Verification.sign_magnitude_division_to_decimal(bits), 5.0)

    def test_division_fractional(self):
        bits = [0] * 32
        bits[14:16] = [1, 0]
        bits[16] = 1
        self.assertEqual(Verification.sign_magnitude_division_to_decimal(bits), 2.5)

    def test_division_negative(self):
        bits = [0] * 32
        bits[0] = 1
        bits[14:16] = [1, 0]
        bits[16] = 1
        self.assertEqual(Verification.sign_magnitude_division_to_decimal(bits), -2.5)

    def test_ieee754_one(self):
        bits = [0] * 32
        bits[1:9] = [0, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(Verification.ieee754_to_decimal(bits), 1.0)

    def test_bcd2421_positive(self):
        bits = [0] * 32
        bits[-8:-4] = [0, 0, 0, 1]
        bits[-4:] = [0, 0, 1, 0]
        self.assertEqual(Verification.bcd2421_to_decimal(bits), 12)

    def test_bcd2421_negative(self):
        bits = [1] * 32
        bits[-8:-4] = [1, 1, 1, 0]
        bits[-4:] = [1, 1, 0, 1]
        self.assertEqual(Verification.bcd2421_to_decimal(bits), -12)
