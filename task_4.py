# Дан список случайных чисел. Оставьте только те, 
# сумма цифр которых четна

from func_list import random_list
from func_list import give_int

def even_num(lst):
    if (lst % 2) == 0:
        return True
    else:
        return False

num_input = give_int('Введите число: ', min_num = 1)
ran_list = random_list(num_input)
even_list = filter(even_num, ran_list)
print(ran_list)
print (list(even_list))