from Minimizer import Minimizer


class TaskRunner:
    @staticmethod
    def run_task1():
        print("\n1. ОДС-3 в (СКНФ)")

        S_values = []
        p_out_values = []

        print("Таблица истинности:")
        print("a b p_in | S p_out")
        print("-" * 18)

        for i in range(8):
            a, b, p_in = [int(x) for x in format(i, "03b")]
            S = a ^ b ^ p_in
            p_out = (a & b) | (a & p_in) | (b & p_in)

            print(f"{a} {b}  {p_in}   | {S}   {p_out}")

            S_values.append([a, b, p_in, S])
            p_out_values.append([a, b, p_in, p_out])

        vars_names = ["a", "b", "p_in"]

        minimizer_S = Minimizer(S_values, vars_names, is_sknf=True)
        minimizer_p_out = Minimizer(p_out_values, vars_names, is_sknf=True)

        print("Минимизированные функции (в СКНФ):")
        print(f"S = {minimizer_S.minimize()}")
        print(f"p_out = {minimizer_p_out.minimize()}")

    @staticmethod
    def run_task2():
        print("\n2. Преобразователь BCD 8421 + 1 (в СДНФ)")

        tables = {name: [] for name in ["P", "y4", "y3", "y2", "y1"]}

        print("Таблица истинности:")
        print("x4 x3 x2 x1 | P  y4 y3 y2 y1")
        print("-" * 28)

        for i in range(16):
            inputs = [int(x) for x in format(i, "04b")]
            inputs_str = "  ".join(map(str, inputs))

            if i <= 9:
                value = i + 1
                if value == 10:
                    outputs = [1, 0, 0, 0, 0]
                    outputs_str = "1  0  0  0  0"
                else:
                    y4, y3, y2, y1 = [int(x) for x in format(value, "04b")]
                    outputs = [0, y4, y3, y2, y1]
                    outputs_str = f"0  {y4}  {y3}  {y2}  {y1}"

                print(f"{inputs_str}  | {outputs_str}")
            else:
                outputs = [-1, -1, -1, -1, -1]
                print(f"{inputs_str}  | X  X  X  X  X")

            tables["P"].append(inputs + [outputs[0]])
            tables["y4"].append(inputs + [outputs[1]])
            tables["y3"].append(inputs + [outputs[2]])
            tables["y2"].append(inputs + [outputs[3]])
            tables["y1"].append(inputs + [outputs[4]])

        vars_names = ["x4", "x3", "x2", "x1"]

        print("Минимизированные функции (в СДНФ):")
        for name in tables:
            minimizer = Minimizer(tables[name], vars_names)
            print(f"{name} = {minimizer.minimize()}")

    @staticmethod
    def run_task3():
        print("\n3. Двоичный счётчик на Т-триггерах (в СДНФ)")

        tables = {name: [] for name in ["T2", "T1", "T0"]}
        print("Таблица переходов автомата:")
        print("Q - текущее сотояние\nN - следующее состояние\nT - входы Т-триггеров")
        print("Q2 Q1 Q0 | N2 N1 N0 | T2 T1 T0")
        print("-" * 30)

        for state in range(8):
            next_state = (state + 1) % 8

            Q2, Q1, Q0 = [int(x) for x in format(state, "03b")]
            N2, N1, N0 = [int(x) for x in format(next_state, "03b")]

            T2 = Q2 ^ N2
            T1 = Q1 ^ N1
            T0 = Q0 ^ N0

            print(f"{Q2}  {Q1}  {Q0}  | {N2}  {N1}  {N0}  | {T2}  {T1}  {T0}")

            tables["T2"].append([Q2, Q1, Q0, T2])
            tables["T1"].append([Q2, Q1, Q0, T1])
            tables["T0"].append([Q2, Q1, Q0, T0])

        vars_names = ["Q2", "Q1", "Q0"]

        print("Функции возбуждения Т-триггеров (в СДНФ):")
        for name in tables:
            minimizer = Minimizer(tables[name], vars_names)
            print(f"{name} = {minimizer.minimize()}")
