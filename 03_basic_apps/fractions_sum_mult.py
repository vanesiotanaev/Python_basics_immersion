# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions (без сокращений).

def input_fraction() -> list:

    fraction = input("Введите дробь в формате 'a/b': ")
    
    while not '/' in fraction:
        fraction = input("Ошибка! Введите дробь в формате 'a/b': ")
    
    numerator = fraction[:fraction.index('/')]
    denominator = fraction[fraction.index('/')+1:]

    if numerator.startswith('-'):
        while not numerator[1:].isdigit():
            fraction = input("Ошибка! Введите дробь в формате 'a/b': ")

    if denominator.startswith('-'):
        while not denominator[1:].isdigit():
            fraction = input("Ошибка! Введите дробь в формате 'a/b': ")
    
    return [int(numerator), int(denominator)]

def fractions_sum_mult(fraction_list_1: list, fraction_list_2: list) -> list:

    sum = [None, None]
    mult = [None, None]
    
    if not fraction_list_1[1] == fraction_list_2[1]:
        
        if fraction_list_1[1] % fraction_list_2[1] == 0:
            sum[1] = fraction_list_1[1]

        elif fraction_list_2[1] % fraction_list_1[1] == 0:
            sum[1] = fraction_list_2[1]

        else:
            sum[1] = fraction_list_1[1] * fraction_list_2[1]
        
        sum[0] = int((fraction_list_1[0] * sum[1] / fraction_list_1[1])\
                    + (fraction_list_2[0] * sum[1] / fraction_list_2[1])) 
        
        sum = '/'.join(map(str, sum))

    mult[0] = fraction_list_1[0] * fraction_list_2[0]
    mult[1] = fraction_list_1[1] * fraction_list_2[1]

    mult = '/'.join(map(str, mult))

    return [sum, mult]

user_fraction_a = input_fraction()
user_fraction_b = input_fraction()

result = fractions_sum_mult(user_fraction_a, user_fraction_b)

print(f"{user_fraction_a[0]}/{user_fraction_a[1]} + {user_fraction_b[0]}/{user_fraction_b[1]} = {result[0]}")
print(f"{user_fraction_a[0]}/{user_fraction_a[1]} * {user_fraction_b[0]}/{user_fraction_b[1]} = {result[1]}")