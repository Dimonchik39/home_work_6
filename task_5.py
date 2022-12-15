# Есть список случайных чисел в промежутке от 1 до 200, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

from func_list import random_list_2
from func_list import give_int_2


num_list = give_int_2('Введите количество случайных чисел: ', min_num = 1, max_num = 1000)
ran_list = random_list_2(num_list)
ran_list = [i for i in enumerate(ran_list) if i[0] != i[1]]
print(ran_list)
