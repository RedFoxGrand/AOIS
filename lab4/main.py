from HashTable import HashTable


def display(ht: HashTable) -> None:
    print("\n" + "-" * 89)
    print(
        "| №  |  V   | h  | ID              | C | U | T | L | D | P0 | Данные                    |"
    )
    print("-" * 89)
    occupied = 0
    for i, cell in enumerate(ht.table):
        V_str, h_str = "", ""
        if cell.ID:
            v, h = ht.hash_function(cell.ID)
            V_str = str(v)
            h_str = str(h)

        if cell.U == 1:
            occupied += 1

        print(f"| {i:2} | {V_str:4} | {h_str:2} | {cell} |")
    print("-" * 89)
    print(f"Коэффициент заполнения: {occupied / ht.H:.2f}\n")


if __name__ == "__main__":
    while True:
        try:
            H = int(input("Введите размер хеш-таблицы: "))
            B = int(input("Введите смещение: "))
            break
        except ValueError:
            print(
                "Некорректное значение, введите целые числа.\n"
            )

    ht = HashTable(H, B)

    while True:
        print("\nМеню: ")
        print("1. Добавить новую запись")
        print("2. Найти запись по ключу")
        print("3. Обновить существующую запись")
        print("4. Удалить запись")
        print("5. Вывести хеш-таблицу на экран")
        print("6. Создание тестовых данных")
        print("7. Выход")

        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            key = input("Введите ключ для добавления: ").strip()
            data = input("Введите данные: ").strip()
            if key and data:
                if ht.create(key, data):
                    print(f"Запись '{key}' добавлена.")
            else:
                print("Ключ и данные не могут быть пустыми.")

        elif choice == "2":
            key = input("Введите ключ для поиска: ").strip()
            if result := ht.read(key):
                print(f"Найдено: {key} — {result}")
            else:
                print(f"Ключ '{key}' не найден в таблице.")

        elif choice == "3":
            key = input("Введите ключ для обновления: ").strip()
            new_data = input("Введите новые данные: ").strip()
            if key and new_data:
                if ht.update(key, new_data):
                    print(f"Данные для ключа '{key}' успешно обновлены.")
                else:
                    print(f"Ключ '{key}' не найден в таблице.")
            else:
                print("Ввод не может быть пустым.")

        elif choice == "4":
            key = input("Введите ключ для удаления: ").strip()
            if key:
                if ht.delete(key):
                    print(f"Запись '{key}' удалена.")
                else:
                    print(f"Ключ '{key}' не найден в таблице.")
            else:
                print("Ключ не может быть пустым.")

        elif choice == "5":
            display(ht)

        elif choice == "6":
            ht.create("Анализ", "Разбор данных")
            ht.create("Аналог", "Подобие объекта")
            ht.create("Анкета", "Опросный лист")
            ht.create("Анамнез", "Опрос пациента")

            ht.create("Индекс", "Показатель")
            ht.create("Интеграл", "Сумма элементов")

            ht.create("База", "Основа системы")
            ht.create("Вектор", "Направление")
            ht.create("График", "Схема зависимости")
            ht.create("Данные", "Сведения или факты")
            ht.create("Журнал", "Сборник записей")
            print("Тестовые данные успешно добавлены.")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Введите цифру от 1 до 7.")
