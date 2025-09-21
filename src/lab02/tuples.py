StudentRecord =tuple[str, str, float]

def format_record(rec:StudentRecord) -> str:
    fio = rec[0].strip()
    group=rec[1].strip()
    gpa=rec[2]

    names=fio.split()
    surname=names[0]
    initials=[name[0].upper()+ '.' for name in names[1:]]

    formatted_gpa=f"{gpa:.2f}"
    return f'{surname} {''.join(initials)}, гр. {group}, GPA {formatted_gpa}'

student=("Laurindo David Gonçalo", "BIVT-25", 4.6)
print(format_record(student))