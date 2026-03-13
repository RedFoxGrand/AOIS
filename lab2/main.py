from sources.LogicalFunctions import LogicalFunctions
from sources.minimization.CalculatedMinimizer import CalculatedMinimizer
from sources.minimization.TableMinimizer import TableMinimizer
from sources.minimization.KarnaughMinimizer import KarnaughMinimizer


if __name__ == "__main__":
    function = input("Введите логическое выражение: ")
    print(f"Выражение: {function}")
    try:
        processor = LogicalFunctions(function)
        processor.build_truth_table()
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)

    print(f"СДНФ: {processor.build_sdnf()}")
    print(f"СКНФ: {processor.build_sknf()}")

    sdnf_numeric_form, sknf_numeric_form = processor.get_numeric_forms_sdnf_and_sknf()
    print(f"Числовая форма СДНФ: {sdnf_numeric_form}")
    print(f"Числовая форма СКНФ: {sknf_numeric_form}")

    print(f"Индексная форма: {processor.get_index_form()}")

    print(f"\nПолином Жегалкина: {processor.build_zhegalkin_polynomial()}")

    classes = processor.get_post_classes()
    vector_str = " ".join("+" if val else "-" for val in classes.values())
    print(f"Принадлежность к классам Поста (T0, T1, S, M, L): ({vector_str})")

    dummies = processor.get_dummy_variables()
    print(f"Фиктивные переменные: {', '.join(dummies) if dummies else 'Нет'}")

    print("\nПроизводные:")
    df_da = processor.get_derivative(["a"])
    print(f"df/da = {df_da}")
    df_db = processor.get_derivative(["b"])
    print(f"df/db = {df_db}")
    df_da_dc = processor.get_derivative(["a", "c"])
    print(f"d^2f/(da dc) = {df_da_dc}")

    print("\nРасчётный метод минимизации")
    alg_minimizer_sdnf = CalculatedMinimizer(
        processor.truth_table, processor.variables, is_sknf=False
    )
    print(f"ДНФ: {alg_minimizer_sdnf.minimize()}")
    alg_minimizer_sknf = CalculatedMinimizer(
        processor.truth_table, processor.variables, is_sknf=True
    )
    print(f"КНФ: {alg_minimizer_sknf.minimize()}")

    print("\nРасчётно-табличный метод")
    tab_minimizer_sdnf = TableMinimizer(
        processor.truth_table, processor.variables, is_sknf=False
    )
    print(f"ДНФ: {tab_minimizer_sdnf.minimize()}")
    tab_minimizer_sknf = TableMinimizer(
        processor.truth_table, processor.variables, is_sknf=True
    )
    print(f"КНФ: {tab_minimizer_sknf.minimize()}")

    print("\nМетод Карт Карно")
    kmap_minimizer_sdnf = KarnaughMinimizer(
        processor.truth_table, processor.variables, is_sknf=False
    )
    print(f"ДНФ: {kmap_minimizer_sdnf.minimize()}")
    kmap_minimizer_sknf = KarnaughMinimizer(
        processor.truth_table, processor.variables, is_sknf=True
    )
    print(f"КНФ: {kmap_minimizer_sknf.minimize()}")
