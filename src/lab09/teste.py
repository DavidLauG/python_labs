import csv
from pathlib import Path
from lab08.models import Student

class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Creates a header file if it does not already exist or is empty."""
        if not self.path.exists() or self.path.stat().st_size == 0:
            with open(self.path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.HEADER)
                writer.writeheader()

    def _read_all_dicts(self) -> list[dict]:
        """Read all lines from CSV as a list of dictionaries."""
        with open(self.path, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != self.HEADER:
                raise ValueError(f"Invalid CSV header. Expected {self.HEADER}")
            return list(reader)

    def _write_all_dicts(self, data: list[dict]):
        """Записать все строки (словари) обратно в CSV."""
        with open(self.path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(data)

    def list(self) -> list[Student]:
        """Вернуть всех студентов в виде списка Student."""
        rows = self._read_all_dicts()
        # Преобразование словарей в объекты Student с валидацией типов
        return [Student.from_dict(row) for row in rows]

    def add(self, student: Student):
        """Добавить нового студента в CSV."""
        rows = self._read_all_dicts()
        # Простая проверка на дублирование (опционально)
        if any(r['fio'] == student.fio for r in rows):
            print(f"Студент с ФИО '{student.fio}' уже существует.")
            return

        rows.append(student.to_dict())
        self._write_all_dicts(rows)

    def find(self, substr: str) -> list[Student]:
        """Найти студентов по подстроке в fio."""
        rows = self._read_all_dicts()
        found_dicts = [r for r in rows if substr.lower() in r["fio"].lower()]
        return [Student.from_dict(d) for d in found_dicts]

    def remove(self, fio: str):
        """Удалить запись(и) с данным fio."""
        rows = self._read_all_dicts()
        # Фильтруем все строки, оставляя только те, где FIO не совпадает
        initial_count = len(rows)
        updated_rows = [r for r in rows if r["fio"] != fio]
        
        if len(updated_rows) < initial_count:
            self._write_all_dicts(updated_rows)
            print(f"Записи для '{fio}' удалены.")
        else:
            print(f"Студент с ФИО '{fio}' не найден.")

    def update(self, fio: str, **fields):
        """Обновить поля существующего студента."""
        rows = self._read_all_dicts()
        updated = False
        
        for row in rows:
            if row["fio"] == fio:
                # Обновляем поля в словаре, при этом ключи должны быть валидными (fio, birthdate, group, gpa)
                for key, value in fields.items():
                    if key in self.HEADER:
                        # Важно: gpa должно храниться в CSV как строка, поэтому приводим к str
                        row[key] = str(value) 
                        updated = True
                    else:
                        print(f"Предупреждение: Неизвестное поле для обновления: {key}")
                # Прерываем цикл, если предполагается обновление только первой записи
                # Если нужно обновить все записи с таким FIO, уберите 'break'
                break 

        if updated:
            self._write_all_dicts(rows)
            print(f"Записи для '{fio}' обновлены.")
        else:
            print(f"Студент с ФИО '{fio}' не найден или поля не изменились.")

