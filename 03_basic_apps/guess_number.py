# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

import random

def guess_number():
    
    MIN_VALUE = 0
    MAX_VALUE = 1000

    hidden_number = random.randint(MIN_VALUE, MAX_VALUE)
    attempts = 10

    print(f'Компьютер загадал число от {MIN_VALUE} до {MAX_VALUE}.')

    while attempts > 0:
        user_number = int(input(f'Угадайте, что это за число (Кол-во попыток - {attempts}): '))

        if user_number > hidden_number:
            attempts -= 1
            print(f'Загаданное компьютером число меньше!')

        elif user_number < hidden_number:
            attempts -= 1
            print(f'Загаданное компьютером число больше!')
        
        else:
            print(f'Поздравляем! Вы отгадали число {hidden_number} c попытки №{11 - attempts}!')
            break
    else:
        print('У Вас не осталось попыток! Игра окончена!')
        
guess_number()