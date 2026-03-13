LENGTH_OF_BITS = 32
LENGTH_OF_INT_PART = 16
EXPONENT_LENGTH = 8
MANTISSA_LENGTH = 23
EXPONENT_BIAS = 127
PRECISION = 150


class BasicFunctions:
    @staticmethod
    def create_empty_bits(length: int = LENGTH_OF_BITS) -> list[int]:
        return [0] * length

    @staticmethod
    def int_to_bits(val: int, length: int) -> list[int]:
        bits = [0] * length
        for i in range(length):
            bits[length - 1 - i] = val % 2
            val //= 2
        return bits

    @staticmethod
    def bin_to_int(bits: list[int]) -> int:
        val = 0
        for b in bits:
            val = val * 2 + b
        return val
