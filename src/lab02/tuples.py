def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise ValueError("Sintax erro (fio, group, gpa)")
    fio = rec[0]  # Get the full name.
    group = rec[1]  # Get the goup.
    gpa = rec[2]  # Get gpa.
    if not isinstance(fio, str) or not isinstance(group, str):
        raise ValueError("They must be string")
    if not isinstance(gpa, float):
        raise ValueError("gpa must be a float number")

    fio = rec[0].strip().title()  # Get the full name and put the Initiasl in Capital.
    group = rec[1].strip()  # Get the goup.
    gpa = rec[2]  # Get gpa.

    names = fio.split()  # Create a list spliting the full name.
    initials = [
        name[0] + "." for name in names[1:]
    ]  # Get the initials and put a dot ".".

    if not fio or not group.strip():
        raise ValueError("fio and group cannot be empty")
    if len(names) < 2:
        raise ValueError(
            "The full name must contain at least the last name and first name."
        )

    formatted_gpa = f"{gpa:.2f}"  # As requested on the exercise.
    return f"{names[0]} {' '.join(initials)}, гр. {group}, GPA {formatted_gpa}"


# return: «Surname» «Init_name.Init_name»., гр. «group», GPA «GPA»
print(format_record(("laurindo david gonçalo", "BIVT-6", 4.6)))
