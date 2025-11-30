import json
from lab08.models import Student

# imports
def students_to_json(students: list[Student], path: str):
    #students.to_dict
    data = [s.to_dict() for s in students]
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Dados salvos com sucesso em '{path}'.")
    except ValueError as e:
        print(f"Erro ao escrever no arquivo {path}: {e}")

def students_from_json(path)-> list[Student]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data=json.load(f)
        if not isinstance(data, list):
            raise TypeError(f"Expected JSON list/array, but got {type(data).__name__}")
        students=[]
        for item in data:
            try:
                student=Student.from_dict(item)
                students.append(student)
            except:
                raise ValueError (f"Error processing student data from JSON: {item}")
        return students
    except:
        raise ValueError ("Error: File Not Found!!!")

# --- Tests ---
if __name__=="__main__":
    students_list=[
        Student("Silva Santos João", "2003-05-15", "БИВТ-6", 4.2),
        Student("David Gonçalo Laurindo", "2007-11-30", "A-50",4.0),
        Student("Petter Parker", "1998-11-30", "M-6",4.2)
    ]
    students_to_json(students_list, "data/lab08/students_output.json")
    loaded_students=students_from_json("data/lab08/students_input.json")
    print(f"Desserializado (str):\n {loaded_students}")
