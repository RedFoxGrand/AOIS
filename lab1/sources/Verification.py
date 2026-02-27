from sources.BasicFunctions import BasicFunctions
from sources.IEEE754 import IEEE754
from sources.BCD2421 import BCD2421


class Verification:
    @staticmethod
    def sign_magnitude_to_decimal(bits: list[int]) -> int:
        val = BasicFunctions.bin_to_int(bits[1:])
        return -val if bits[0] == 1 else val

    @staticmethod
    def ones_complement_to_decimal(bits: list[int]) -> int:
        if bits[0] == 0:
            return BasicFunctions.bin_to_int(bits)
        inverted = [1 if b == 0 else 0 for b in bits]
        val = BasicFunctions.bin_to_int(inverted)
        return -val

    @staticmethod
    def twos_complement_to_decimal(bits: list[int]) -> int:
        if bits[0] == 0:
            return BasicFunctions.bin_to_int(bits)
        inverted = [1 if b == 0 else 0 for b in bits]
        val = BasicFunctions.bin_to_int(inverted) + 1
        return -val

    @staticmethod
    def sign_magnitude_division_to_decimal(bits: list[int]) -> float:
        sign = bits[0]
        int_bits = bits[1:16]
        fract_bits = bits[16:]

        int_val = BasicFunctions.bin_to_int(int_bits)

        frac_val = 0.0
        for i, bit in enumerate(fract_bits):
            if bit == 1:
                frac_val += 1 / (1 << (i + 1))

        result = int_val + frac_val
        return -result if sign == 1 else result

    @staticmethod
    def ieee754_to_decimal(bits: list[int]) -> float:
        sign, exp, mant_val = IEEE754._get_components(bits)
        s = -1 if sign == 1 else 1

        if exp == 0:
            e = -126
        else:
            e = exp - 127

        m = mant_val / (1 << 23)

        if e >= 0:
            return s * m * (1 << e)
        else:
            return s * m / (1 << -e)

    @staticmethod
    def bcd2421_to_decimal(bits: list[int]) -> int:
        is_negative = bits[0] == 1
        current_bits = (
            list(bits) if not is_negative else [1 if b == 0 else 0 for b in bits]
        )
        res = 0
        for i in range(8):
            chunk = current_bits[i * 4 : (i + 1) * 4]
            digit = BCD2421._digit_from_2421_to_decimal(chunk)
            res = res * 10 + digit
        return -res if is_negative else res
