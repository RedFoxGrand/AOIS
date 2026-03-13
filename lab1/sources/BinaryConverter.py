from sources.BasicFunctions import BasicFunctions
from sources.BasicFunctions import LENGTH_OF_BITS


class BinaryConverter:
    @staticmethod
    def converting_to_sign_magnitude(input_number: str) -> list[int]:
        number = int(input_number)
        bits = BasicFunctions.int_to_bits(abs(number), LENGTH_OF_BITS)
        if number < 0:
            bits[0] = 1
        return bits

    @staticmethod
    def converting_to_ones_complement(input_number: str) -> list[int]:
        number = int(input_number)
        bits = BasicFunctions.int_to_bits(abs(number), LENGTH_OF_BITS)
        if number < 0:
            for i in range(len(bits)):
                bits[i] = 1 if bits[i] == 0 else 0
        return bits

    @staticmethod
    def converting_to_twos_complement(input_number: str) -> list[int]:
        bits = BinaryConverter.converting_to_ones_complement(input_number)

        if int(input_number) >= 0:
            return bits

        carry = 1
        for i in range(LENGTH_OF_BITS - 1, -1, -1):
            sum = bits[i] + carry
            bits[i] = sum % 2
            carry = sum // 2

            if carry == 0:
                break

        return bits
