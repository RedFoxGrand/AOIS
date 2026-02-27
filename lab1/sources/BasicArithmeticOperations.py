from sources.BasicFunctions import BasicFunctions
from sources.BinaryConverter import BinaryConverter


class BasicArithmeticOperations:
    @staticmethod
    def _add_lists(bits1: list[int], bits2: list[int]) -> list[int]:
        bits = BasicFunctions.create_empty_bits()
        carry = 0
        for i in range(len(bits1) - 1, -1, -1):
            total = bits1[i] + bits2[i] + carry
            bits[i] = total % 2
            carry = total // 2
        return bits

    @staticmethod
    def add_in_twos_complement(input_number1: str, input_number2: str) -> list[int]:
        number1 = BinaryConverter.converting_to_twos_complement(input_number1)
        number2 = BinaryConverter.converting_to_twos_complement(input_number2)
        return BasicArithmeticOperations._add_lists(number1, number2)

    @staticmethod
    def subtract_in_twos_complement(
        input_number1: str, input_number2: str
    ) -> list[int]:
        number1 = BinaryConverter.converting_to_twos_complement(input_number1)
        number2 = BinaryConverter.converting_to_twos_complement(input_number2)

        for i in range(len(number2)):
            number2[i] = 1 if number2[i] == 0 else 0

        one = BasicFunctions.create_empty_bits()
        one[-1] = 1
        number2_negated = BasicArithmeticOperations._add_lists(number2, one)

        return BasicArithmeticOperations._add_lists(number1, number2_negated)
