from sources.BasicFunctions import BasicFunctions


class IEEE754:
    @staticmethod
    def _get_components(bits: list[int]) -> tuple[int, int, int]:
        sign = bits[0]
        exp = BasicFunctions.bin_to_int(bits[1:9])
        mantissa_bits = bits[9:]
        if exp == 0:
            mantissa_value = BasicFunctions.bin_to_int(mantissa_bits)
        else:
            mantissa_value = (1 << 23) + BasicFunctions.bin_to_int(mantissa_bits)
        return sign, exp, mantissa_value

    @staticmethod
    def _normalize(sign: int, exp: int, mantissa_value: int) -> list[int]:
        if mantissa_value == 0:
            return [sign] + BasicFunctions.create_empty_bits(31)

        temp = mantissa_value
        pos = -1
        while temp > 0:
            temp //= 2
            pos += 1

        shift = 23 - pos

        if shift > 0:
            mantissa_value <<= shift
            exp -= shift
        elif shift < 0:
            mantissa_value >>= -shift
            exp += -shift

        if exp <= 0:
            return [sign] + BasicFunctions.create_empty_bits(31)
        if exp >= 255:
            return [sign] + [1] * 8 + BasicFunctions.create_empty_bits(23)

        mantissa_value = mantissa_value % (1 << 23)
        result = BasicFunctions.create_empty_bits()
        result[0] = sign
        result[1:9] = BasicFunctions.int_to_bits(exp, 8)
        result[9:] = BasicFunctions.int_to_bits(mantissa_value, 23)
        return result

    @staticmethod
    def _add_bits(bits1: list[int], bits2: list[int]) -> list[int]:
        s1, e1, m1 = IEEE754._get_components(bits1)
        s2, e2, m2 = IEEE754._get_components(bits2)

        if m1 == 0:
            return bits2
        if m2 == 0:
            return bits1

        if e1 > e2:
            shift = e1 - e2
            m2 >>= shift
            e_res = e1
        elif e2 > e1:
            shift = e2 - e1
            m1 >>= shift
            e_res = e2
        else:
            e_res = e1

        if s1 == s2:
            m_res = m1 + m2
            s_res = s1
        else:
            if m1 >= m2:
                m_res = m1 - m2
                s_res = s1
            else:
                m_res = m2 - m1
                s_res = s2

        return IEEE754._normalize(s_res, e_res, m_res)

    @staticmethod
    def converting_from_decimal_to_ieee754(input_number: str) -> list[int]:
        sign = 1 if input_number.startswith("-") else 0
        if input_number.startswith("-"):
            input_number = input_number[1:]

        if "." in input_number:
            parts = input_number.split(".")
            int_str = parts[0]
            frac_str = parts[1]
        else:
            int_str = input_number
            frac_str = "0"

        int_part = int(int_str)

        if frac_str == "0" or frac_str == "":
            frac_numerator = 0
            frac_denominator = 1
        else:
            frac_numerator = int(frac_str)
            frac_denominator = 10 ** len(frac_str)

        if int_part == 0 and frac_numerator == 0:
            result = BasicFunctions.create_empty_bits()
            result[0] = sign
            return result

        precision = 150
        full_mantissa = int_part << precision

        if frac_numerator > 0:
            full_mantissa += (frac_numerator << precision) // frac_denominator

        return IEEE754._normalize(sign, 0, full_mantissa)

    @staticmethod
    def add_in_ieee754(input_number1: str, input_number2: str) -> list[int]:
        bits1 = IEEE754.converting_from_decimal_to_ieee754(input_number1)
        bits2 = IEEE754.converting_from_decimal_to_ieee754(input_number2)
        return IEEE754._add_bits(bits1, bits2)

    @staticmethod
    def subtract_in_ieee754(input_number1: str, input_number2: str) -> list[int]:
        bits1 = IEEE754.converting_from_decimal_to_ieee754(input_number1)
        bits2 = IEEE754.converting_from_decimal_to_ieee754(input_number2)
        bits2[0] = 1 if bits2[0] == 0 else 0
        return IEEE754._add_bits(bits1, bits2)

    @staticmethod
    def multiply_in_ieee754(input_number1: str, input_number2: str) -> list[int]:
        bits1 = IEEE754.converting_from_decimal_to_ieee754(input_number1)
        bits2 = IEEE754.converting_from_decimal_to_ieee754(input_number2)
        s1, e1, m1 = IEEE754._get_components(bits1)
        s2, e2, m2 = IEEE754._get_components(bits2)

        if m1 == 0 or m2 == 0:
            return BasicFunctions.create_empty_bits()

        sign_res = 1 if s1 != s2 else 0
        return IEEE754._normalize(sign_res, e1 + e2 - 127 - 23, m1 * m2)

    @staticmethod
    def divide_in_ieee754(input_number1: str, input_number2: str) -> list[int]:
        bits1 = IEEE754.converting_from_decimal_to_ieee754(input_number1)
        bits2 = IEEE754.converting_from_decimal_to_ieee754(input_number2)
        s1, e1, m1 = IEEE754._get_components(bits1)
        s2, e2, m2 = IEEE754._get_components(bits2)

        if m2 == 0:
            raise ZeroDivisionError("Division by zero")
        if m1 == 0:
            return BasicFunctions.create_empty_bits()

        sign_res = 1 if s1 != s2 else 0
        return IEEE754._normalize(sign_res, e1 - e2 + 127, (m1 << 23) // m2)
