# Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

from func_list import random_list_2
from func_list import give_int_2

num_list = give_int_2('Введите количество случайных чисел: ', min_num = 1, max_num = 1000)
ran_list = random_list_2(num_list)
ran_list = [i for i in enumerate(ran_list) if i[0] != i[1]]
print(ran_list, '\n')
sort_list = [i for i in ran_list if  not (i[0] + i[1]) % 5]
print(sort_list)