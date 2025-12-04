import csv
from pathlib import Path
from lab08.models import Student


class Group:
    HEADER=["fio","birthdate","group","gpa"]
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        if not self.path.exists():
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.HEADER)
                writer.writeheader()

    def _read_all(self)-> list[dict]:
        with open(self.path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)  # Read and save as a Dicty
        return list(reader)
    
    def _write_all(self, data: list[dict]):
        with open(self.path, "w", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
        return list(reader)

    def list(self) -> list[Student]:        
        rows=self._read_all()
        return [Student.from_dict(row) for row in rows]

    def add(self, student: Student):
        rows=self._read_all()
        rows.append(student.to_dict())
        self._al
    
    def find(self, substr: str):
        rows=self._read_all()
        return [r for r in rows if substr in r["fio"]]  


    """
    def remove(self, fio: str):
    # TODO: реализовать метод remove()
        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                break
    
    def update(self, fio: str, **fields):
    # TODO: реализовать метод update()
    """
if __name__=="__main__":
    caminho="data/lab09/students.csv"
    turma=Group(caminho)
    s1 = Student("Иванов Иван Иванович", "2000-01-15", "Группа А", 4.5)
    turma.add(s1)
    #Group()
    #print(tela)