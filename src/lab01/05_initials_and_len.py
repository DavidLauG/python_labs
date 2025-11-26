# Задание 5 — Инициалы и длина строки
# The user insert his fuulname. And the system shows him how many characteres he
# inserted, includding spaces but not the spaces in the beggining and end of the sentece

full_name = input("ФИО:")  # Getting the full name's user

# Removing the spaces in the beggining and finish of the name inserted
full_name = " ".join(full_name.split())

initials = ""  # Get the initials for user's name

# for eatch part of the full user's name, add the initials letters
# in var "initials. But 1st put these initials in CAPITAL letters"
for part in full_name.split():
    initials += part[0].upper()

# Calculate how many chars are in the name, includding spaces
length = len(full_name)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {length}")
