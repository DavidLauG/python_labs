#Задание 4 — Минуты → ЧЧ:ММ
#Asks to user to insert the total amount of minutes and then converts it in HH:MM

total_minutes=int(input('Insert the total minutes: '))

hours=total_minutes//60
minutes=total_minutes%60

print(f'Минуты: {total_minutes}')
print(f'{hours}:{minutes}')