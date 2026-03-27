from HashData import HashData


class HashTable:
    def __init__(self, H: int, B: int) -> None:
        self._H = H
        self._B = B
        self._table = [HashData() for _ in range(self._H)]
        self._alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    @property
    def table(self) -> list[HashData]:
        return self._table

    @property
    def H(self) -> int:
        return self._H

    @property
    def B(self) -> int:
        return self._B

    @property
    def alphabet(self) -> str:
        return self._alphabet

    def get_char_value(self, char: str) -> int:
        char = char.upper()
        return self._alphabet.index(char) if char in self._alphabet else 0

    def validate_key(self, key: str) -> bool:
        if len(key) < 2:
            print(f"Длина ключа '{key}' должна быть не менее 2 символов.")
            return False

        for char in key:
            if char.upper() not in self._alphabet:
                print(
                    f"Некорректный символ '{char}' в ключе '{key}'. Разрешены только русские буквы."
                )
                return False
        return True

    def hash_function(self, key: str) -> tuple[int, int]:
        V = self.get_char_value(key[0]) * 33 + self.get_char_value(key[1])
        h = (V % self._H) + self._B
        return V, h

    def get_chain_start_index(self, h: int) -> int:
        for step in range(self._H):
            index = (h + step) % self._H
            cell = self._table[index]
            if cell.U == 0:
                return -1
            _, current_h = self.hash_function(cell.ID)
            if current_h == h:
                return index
        return -1

    def create(self, key: str, data: str) -> bool:
        try:
            if not self.validate_key(key):
                return False
        except Exception as e:
            print(f"Ошибка валидации ключа '{key}': {e}")
            return False

        if self.read(key) is not None:
            print(f"Ключ '{key}' уже существует в таблице.")
            return False

        _, h = self.hash_function(key)
        last_chain_index = -1

        for step in range(self._H):
            index = (h + step) % self._H
            if self._table[index].U == 0 or self._table[index].D == 1:
                cell = self._table[index]
                cell.ID = key
                cell.Pi = data
                cell.U = 1
                cell.D = 0
                cell.C = 1 if step > 0 else 0
                cell.T = 1
                cell.P0 = -1

                if step > 0 and last_chain_index != -1:
                    self._table[last_chain_index].P0 = index
                    self._table[last_chain_index].T = 0
                return True
            else:
                _, current_h = self.hash_function(self._table[index].ID)
                if current_h == h:
                    last_chain_index = index

        print("Хеш-таблица заполнена.")
        return False

    def read(self, key: str) -> str | None:
        try:
            if not self.validate_key(key):
                return None
        except Exception as e:
            print(f"Ошибка валидации ключа '{key}': {e}")
            return None

        _, h = self.hash_function(key)

        start_index = self.get_chain_start_index(h)
        if start_index == -1:
            return None

        current_index = start_index
        while current_index != -1:
            cell = self._table[current_index]
            if cell.ID == key and cell.D == 0:
                return cell.Pi
            current_index = cell.P0

        return None

    def update(self, key: str, new_data: str) -> bool:
        try:
            if not self.validate_key(key):
                return False
        except Exception as e:
            print(f"Ошибка валидации ключа '{key}': {e}")
            return False

        _, h = self.hash_function(key)

        start_index = self.get_chain_start_index(h)
        if start_index == -1:
            return False

        current_index = start_index
        while current_index != -1:
            cell = self._table[current_index]
            if cell.ID == key and cell.D == 0:
                cell.Pi = new_data
                return True
            current_index = cell.P0

        return False

    def delete(self, key: str) -> bool:
        try:
            if not self.validate_key(key):
                return False
        except Exception as e:
            print(f"Ошибка валидации ключа '{key}': {e}")
            return False

        _, h = self.hash_function(key)

        start_index = self.get_chain_start_index(h)
        if start_index == -1:
            return False

        target_index = -1
        current_index = start_index
        while current_index != -1:
            cell = self._table[current_index]
            if cell.ID == key and cell.D == 0:
                target_index = current_index
                cell.D = 1
                break
            current_index = cell.P0

        if target_index == -1:
            return False

        cell = self._table[target_index]
        previous_index = -1
        for i in range(self._H):
            if self._table[i].U == 1 and self._table[i].P0 == target_index:
                previous_index = i
                break

        if cell.T == 1 and previous_index == -1:
            cell.reset()

        elif cell.T == 1 and previous_index != -1:
            cell.reset()
            self._table[previous_index].T = 1
            self._table[previous_index].P0 = -1

        elif cell.T == 0:
            next_index = cell.P0
            next_cell = self._table[next_index]
            cell.ID = next_cell.ID
            cell.Pi = next_cell.Pi
            cell.T = next_cell.T
            cell.P0 = next_cell.P0
            cell.C = 1 if cell.C == 1 else next_cell.C
            cell.D = 0
            next_cell.reset()

        return True
