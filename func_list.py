from random import randint
from typing import Optional

def random_list(list_size: int) -> list:
    '''
    Фунция поиска случайного числа
    '''
    list_rand = list()
    for i in range(list_size):
        list_rand.append(randint(1, 50))
    return list_rand

def give_int(input_string: str,
            min_num: Optional[int] = None) -> int:
    '''
    Функция заполнения списка
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите число больше или равно: {min_num}')
                continue   
            return num
        except ValueError:
            print('Вы ввели не число')