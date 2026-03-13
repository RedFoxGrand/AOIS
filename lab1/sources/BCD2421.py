from sources.BasicFunctions import BasicFunctions


class BCD2421:
    @staticmethod
    def _digit_from_decimal_to_2421(digit: int) -> list[int]:
        if digit < 5:
            return BasicFunctions.int_to_bits(digit, 4)
        else:
            return BasicFunctions.int_to_bits(digit + 6, 4)

    @staticmethod
    def _digit_from_2421_to_decimal(bits: list[int]) -> int:
        val = BasicFunctions.bin_to_int(bits)
        return val - 6 if val >= 5 else val

    @staticmethod
    def decimal_number_to_2421(input_number: str) -> list[int]:
        result = []

        sign = 1 if input_number.startswith("-") else 0
        if sign == 1:
            input_number = input_number[1:]
            for i in input_number:
                result.extend(BCD2421._digit_from_decimal_to_2421(9 - int(i)))
        else:
            for i in input_number:
                result.extend(BCD2421._digit_from_decimal_to_2421(int(i)))

        padding = 32 - len(result)
        if padding > 0:
            result = [sign] * padding + result

        return result[-32:]

    @staticmethod
    def add_in_bcd_2421(input_number1: str, input_number2: str) -> list[int]:
        bits1 = BCD2421.decimal_number_to_2421(input_number1)
        bits2 = BCD2421.decimal_number_to_2421(input_number2)

        result = BasicFunctions.create_empty_bits()
        carry = 0

        for i in range(8):
            end = 32 - i * 4
            start = end - 4

            d1 = BCD2421._digit_from_2421_to_decimal(bits1[start:end])
            d2 = BCD2421._digit_from_2421_to_decimal(bits2[start:end])

            total = d1 + d2 + carry

            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0

            result[start:end] = BCD2421._digit_from_decimal_to_2421(total)

        if carry == 1:
            for i in range(8):
                end = 32 - i * 4
                start = end - 4

                d = BCD2421._digit_from_2421_to_decimal(result[start:end])
                d += carry

                if d >= 10:
                    d -= 10
                    carry = 1
                else:
                    carry = 0

                result[start:end] = BCD2421._digit_from_decimal_to_2421(d)
                
                if carry == 0:
                    break

        return result
