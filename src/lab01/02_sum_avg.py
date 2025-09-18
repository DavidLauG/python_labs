#Задание 2 — Сумма и среднее
#Shows the Sum and average

a = float(input('Write the 1st REAL number: '))
b = float(input('Write the 2nd one: '))

summa = a+b
average = summa/2

print(f'a: {a:.2}') #print the 1st num just with 2 decimal point
print(f'b: {b:.2}')  #do de same as in line 7
print('sum: {:.2}; avg: {:.2}'.format(summa, average)) #do the same with vars "summa" e "averrage"
