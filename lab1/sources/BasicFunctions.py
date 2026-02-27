class BasicFunctions:
    @staticmethod
    def create_empty_bits(length: int = 32) -> list[int]:
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