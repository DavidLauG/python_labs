# Задание 2 — Сумма и среднее
# Shows the Sum and average

a = float(input("a: "))  # Get the 1st number and convert it into float number
b = float(input("b: "))  # Get the 2nd number and convert it into float number

summa = a + b  # Sum
average = summa / 2  # Real division

print(
    "sum: {:.2}; avg: {:.2}".format(summa, average)
)  # do the same with vars "summa" e "averrage"
