def format_record(rec:tuple[str, str, float]) -> str:
    fio = rec[0].strip() #Get the full name.
    group=rec[1].strip() #Get the goup.
    gpa=rec[2] #Get gpa.

    names=fio.split() # Create a list spliting the full name.
    surname=names[0].capitalize() #Put the 1st letter in capital and Get it.
    initials=[name[0].upper()+ '.' for name in names[1:]] #Get the initials and put a dot ".".

    formatted_gpa=f"{gpa:.2f}" #As requested on the exercise.
    return f'{surname} {''.join(initials)}, гр. {group}, GPA {formatted_gpa}'
#return: «Surname» «Init_name.Init_name»., гр. «group», GPA «GPA»

student=("laurindo david ", "BIVT-25", 4.6)
print(format_record(student))