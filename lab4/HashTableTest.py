import unittest
from HashTable import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(H=10, B=0)

    def test_initialization(self):
        self.assertEqual(self.ht.H, 10)
        self.assertEqual(self.ht.B, 0)
        self.assertEqual(len(self.ht.table), 10)

    def test_validate_key(self):
        self.assertTrue(self.ht.validate_key("Тест"))
        self.assertFalse(self.ht.validate_key("А"))
        self.assertFalse(self.ht.validate_key("Test"))
        self.assertFalse(self.ht.validate_key("Тест1"))

    def test_create_and_read(self):
        self.assertTrue(self.ht.create("Яблоко", "Красное"))
        self.assertEqual(self.ht.read("Яблоко"), "Красное")
        self.assertFalse(self.ht.create("Яблоко", "Зеленое"))

    def test_read_non_existent(self):
        self.assertIsNone(self.ht.read("Груша"))

    def test_update(self):
        self.ht.create("Яблоко", "Красное")
        self.assertTrue(self.ht.update("Яблоко", "Зеленое"))
        self.assertEqual(self.ht.read("Яблоко"), "Зеленое")
        self.assertFalse(self.ht.update("Груша", "Желтая"))

    def test_delete_simple(self):
        self.ht.create("Яблоко", "Красное")
        self.assertTrue(self.ht.delete("Яблоко"))
        self.assertIsNone(self.ht.read("Яблоко"))
        self.assertFalse(self.ht.delete("Яблоко"))

    def test_collisions_and_chaining(self):
        self.assertTrue(self.ht.create("Анализ", "Данные 1"))
        self.assertTrue(self.ht.create("Аналог", "Данные 2"))
        self.assertTrue(self.ht.create("Анкета", "Данные 3"))

        self.assertEqual(self.ht.read("Анализ"), "Данные 1")
        self.assertEqual(self.ht.read("Аналог"), "Данные 2")
        self.assertEqual(self.ht.read("Анкета"), "Данные 3")

    def test_delete_with_shift(self):
        self.ht.create("Анализ", "Данные 1")
        self.ht.create("Аналог", "Данные 2")
        self.ht.create("Анкета", "Данные 3")

        self.assertTrue(self.ht.delete("Аналог"))
        self.assertEqual(self.ht.read("Анкета"), "Данные 3")
        self.assertIsNone(self.ht.read("Аналог"))

    def test_table_full(self):
        ht_small = HashTable(H=2, B=0)
        self.assertTrue(ht_small.create("Один", "1"))
        self.assertTrue(ht_small.create("Два", "2"))
        self.assertFalse(ht_small.create("Три", "3"))

    def test_exceptions_in_operations(self):
        self.assertFalse(self.ht.create(123, "Data"))
        self.assertIsNone(self.ht.read(123))
        self.assertFalse(self.ht.update(123, "Data"))
        self.assertFalse(self.ht.delete(123))

    def test_hashing_and_char_values(self):
        self.assertEqual(self.ht.get_char_value("А"), 0)
        self.assertEqual(self.ht.get_char_value("Б"), 1)
        self.assertEqual(self.ht.get_char_value("1"), 0)

        V, h = self.ht.hash_function("АБ")
        self.assertEqual(V, 1)
        self.assertEqual(h, 1)

    def test_delete_last_in_chain(self):
        self.ht.create("Анализ", "Данные 1")
        self.ht.create("Аналог", "Данные 2")
        self.assertTrue(self.ht.delete("Аналог"))
        self.assertIsNone(self.ht.read("Аналог"))
        self.assertEqual(self.ht.read("Анализ"), "Данные 1")

    def test_update_and_delete_non_existent_in_chain(self):
        self.ht.create("Анализ", "Данные 1")
        self.assertFalse(self.ht.update("Аналог", "Данные 2"))
        self.assertFalse(self.ht.delete("Аналог"))


if __name__ == "__main__":
    unittest.main()
