# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_VALUE = 0
MAX_VALUE = 100000

number_chosen = int(input('Введите положительное число (не более 100 000): '))
number_status = None

while number_chosen < MIN_VALUE or number_chosen > MAX_VALUE:
    number_chosen = int(input('Вы ввели недопустимое число! Введите положительное число (не более 100 000): '))

if number_chosen == 0 or number_chosen == 1:
    print(f'Число {number_chosen} не является ни простым, ни составным!')

for i in range(2, number_chosen+1):
    if number_chosen % i == 0 and i != number_chosen:
        print(f'Число {number_chosen} также делится нацело, по крайней мере, на {i}, а значит {number_chosen} - составное число!')
        number_status = True
        break

if number_status == None:    
    print(f'{number_chosen} - простое число!')

