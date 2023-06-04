# Написать программу, которая будет выводить в консоль ёлочку заданной высоты.

SPIKE = '*'
SPACE = ' '

spike_quantity = 1
min_part = 3
user_numb = int(input("Введите числовое значение, соответствующее высоте ёлочки: "))
max_part = user_numb + 2

while min_part <= max_part:
    space_size = max_part - 1 
    
    for i in range(min_part):
        print((space_size * SPACE) + (SPIKE * spike_quantity) + (space_size * SPACE))
        spike_quantity += 2
        space_size -= 1
    
    min_part += 1
    spike_quantity = 1