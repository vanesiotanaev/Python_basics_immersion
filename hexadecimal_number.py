# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def convert_to_hex(user_value) -> str:
    HEX_DIVIDER = 16

    hex_value = ''

    while user_value > 0:

        if user_value % HEX_DIVIDER == 10:
            hex_value += 'A'

        elif user_value % HEX_DIVIDER == 11:
            hex_value += 'B'
        
        elif user_value % HEX_DIVIDER == 12:
            hex_value += 'C'

        elif user_value % HEX_DIVIDER == 13:
            hex_value += 'D'
        
        elif user_value % HEX_DIVIDER == 14:
            hex_value += 'E'
        
        elif user_value % HEX_DIVIDER == 15:
            hex_value += 'F'
        
        else:
            hex_value += str(user_value % HEX_DIVIDER)
        
        user_value = user_value // HEX_DIVIDER

    return hex_value[::-1]
    
print(convert_to_hex(100000))