# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# number = int(input('Введите чило: '))

# def list_order(num):
#     '''
#     Функция формирования последовательности
#     (порядковое умножение на -3)  
#     '''
#     num_list = [1]
#     for i in range(1, num):
#         i = (-3)**i
#         num_list.append(i)   
#     return num_list

# result = list_order(number)
# print(result)

from typing import Optional

def give_int(input_number:  str,
            min_num: Optional[int] = 1) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = int(input(input_number)) 
            if min_num and num < min_num:
                print(f'Введите число больше или равно {min_num}')
                continue   
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

list_order = [(-3)**i for i in range(give_int('Введите число: '))]
print(list_order)