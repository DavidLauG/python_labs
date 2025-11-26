# Задание 4 — Минуты → ЧЧ:ММ
# Asks to user to insert the total amount of minutes and then converts it in HH:MM

minutes = int(input("Минуты: "))  # Get the full time in minutes

hours = minutes // 60  # Calculate the hour of thew full time
minutes = minutes % 60  # Calculate the rest of time from the previous calculus

print(f"{hours}:{minutes}")
