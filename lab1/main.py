from sources.BinaryConverter import BinaryConverter
from sources.BasicArithmeticOperations import BasicArithmeticOperations
from sources.AdvancedArithmeticOperations import AdvancedArithmeticOperations
from sources.IEEE754 import IEEE754
from sources.BCD2421 import BCD2421
from sources.Verification import Verification


def print_info(bits: list[int], text: str, converter=None) -> None:
    val = converter(bits) if converter else None
    if converter == Verification.sign_magnitude_division_to_decimal:
        val_str = f" ({val:.5f})" if val is not None else ""
        s = "".join(map(str, bits))
        print(f"{text}: {s[:16]}.{s[16:]}{val_str}")
    else:
        if isinstance(val, float):
            val_str = f" ({val:.5f})" if val is not None else ""
        else:
            val_str = f" ({val})" if val is not None else ""
        print(f"{text}: {''.join(map(str, bits))}{val_str}")


def main():
    while True:
        print("Меню:")
        print("1. Перевод числа в двоичные коды (прямой, обратный, дополнительный)")
        print("2. Сложение/вычитание в дополнительном коде")
        print("3. Умножение/деление в прямом коде")
        print("4. Операции в IEEE 754")
        print("5. Операции в BCD 2421")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "0":
            break
        elif choice == "1":
            num = input("Введите число: ")
            try:
                print_info(
                    BinaryConverter.converting_to_sign_magnitude(num),
                    "Прямой код",
                    Verification.sign_magnitude_to_decimal,
                )
                print_info(
                    BinaryConverter.converting_to_ones_complement(num),
                    "Обратный код",
                    Verification.ones_complement_to_decimal,
                )
                print_info(
                    BinaryConverter.converting_to_twos_complement(num),
                    "Дополнительный код",
                    Verification.twos_complement_to_decimal,
                )
            except Exception as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            num1 = input("Введите первое число: ")
            num2 = input("Введите второе число: ")
            print("Операция:")
            print("1. Сложение")
            print("2. Вычитание")
            operation = input("Выбор: ")
            try:
                if operation == "1":
                    print_info(
                        BasicArithmeticOperations.add_in_twos_complement(num1, num2),
                        f"Сумма {num1} и {num2}",
                        Verification.twos_complement_to_decimal,
                    )
                elif operation == "2":
                    print_info(
                        BasicArithmeticOperations.subtract_in_twos_complement(
                            num1, num2
                        ),
                        f"Разность {num1} и {num2}",
                        Verification.twos_complement_to_decimal,
                    )
                else:
                    print("Неверная операция")
            except Exception as e:
                print(f"Ошибка: {e}")
        elif choice == "3":
            num1 = input("Введите первое число: ")
            num2 = input("Введите второе число: ")
            print("Операция:")
            print("1. Умножение")
            print("2. Деление")
            operation = input("Выбор: ")
            try:
                if operation == "1":
                    print_info(
                        AdvancedArithmeticOperations.multiply_in_sign_magnitude(
                            num1, num2
                        ),
                        f"Произведение {num1} и {num2}",
                        Verification.sign_magnitude_to_decimal,
                    )
                elif operation == "2":
                    print_info(
                        AdvancedArithmeticOperations.divide_in_sign_magnitude(
                            num1, num2
                        ),
                        f"Частное {num1} и {num2}",
                        Verification.sign_magnitude_division_to_decimal,
                    )
                else:
                    print("Неверная операция")
            except Exception as e:
                print(f"Ошибка: {e}")
        elif choice == "4":
            print("1. Перевод числа в IEEE754")
            print("2. Сложение")
            print("3. Вычитание")
            print("4. Умножение")
            print("5. Деление")
            operation = input("Выбор: ")
            try:
                if operation == "1":
                    num = input("Введите число: ")
                    print_info(
                        IEEE754.converting_from_decimal_to_ieee754(num),
                        f"{num} в IEEE754",
                        Verification.ieee754_to_decimal,
                    )
                elif operation in ("2", "3", "4", "5"):
                    num1 = input("Введите первое число: ")
                    num2 = input("Введите второе число: ")
                    if operation == "2":
                        print_info(
                            IEEE754.add_in_ieee754(num1, num2),
                            f"Сумма {num1} и {num2}",
                            Verification.ieee754_to_decimal,
                        )
                    elif operation == "3":
                        print_info(
                            IEEE754.subtract_in_ieee754(num1, num2),
                            f"Разность {num1} и {num2}",
                            Verification.ieee754_to_decimal,
                        )
                    elif operation == "4":
                        print_info(
                            IEEE754.multiply_in_ieee754(num1, num2),
                            f"Произведение {num1} и {num2}",
                            Verification.ieee754_to_decimal,
                        )
                    elif operation == "5":
                        print_info(
                            IEEE754.divide_in_ieee754(num1, num2),
                            f"Частное {num1} и {num2}",
                            Verification.ieee754_to_decimal,
                        )
                else:
                    print("Неверная операция")
            except Exception as e:
                print(f"Ошибка: {e}")
        elif choice == "5":
            print("1. Первеод в числа 2421 BCD")
            print("2. Сложение")
            operation = input("Выбор: ")
            try:
                if operation == "1":
                    num = input("Введите число: ")
                    print_info(
                        BCD2421.decimal_number_to_2421(num),
                        f"{num} в BCD2421",
                        Verification.bcd2421_to_decimal,
                    )
                elif operation == "2":
                    num1 = input("Введите первое число: ")
                    num2 = input("Введите второе число: ")
                    print_info(
                        BCD2421.add_in_bcd_2421(num1, num2),
                        f"Сумма {num1} и {num2}",
                        Verification.bcd2421_to_decimal,
                    )
                else:
                    print("Неверная операция")
            except Exception as e:
                print(f"Ошибка: {e}")
        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()
