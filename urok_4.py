# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:12:28 2021

@author: KaiJax

Урок №4
"""

import numpy as np
import pandas as pd

np.sum([x for x in range(10)])


import time
# или можно импортировать только sleep или time:
from time import sleep

sleep(5) # пауза выполнения кода на 5 секунд





s = 'sum fig sum hgi'
v = s.split() # создает список
v = list(set(v)) # удаляет повторяющиеся значения
s1 = ' '.join(v) # делает из списка строку



my_list = [2, 4, 6]
print(f"Исходный список: {my_list}")

new_list = []
for el in my_list:
    new_list.append(el + 10)
print(f"Новый список: {new_list}")

# Более короткий вариант кода:
new_list = [x+10 for x in my_list]


# для открытия файла и соххранения его по строчно
lines = [line.strip() for line in open('test.txt')]
print(lines)


my_list = [10, 25, 30, 45, 50]
print(my_list)
# вывод только четных чисел
new_list = [el for el in my_list if el % 2 ==0]
print(new_list)


my_list = [10, 25, 30, 45, 50]
my_list2 = [5, 25, 30, 15, 50]
print(my_list)
# вывод элемента если он совпадает из my_list2
new_list = [el for el in my_list if el in my_list2]
print(new_list)

# то же самое но короче:
list(set(my_list) & set(my_list2))

# Создать dict с индексом как число int
my_dict = {el: el*2 for el in range(10, 20)}
print(my_dict[10])

# Создать dict с индексом как строка str
my_dict = {str(el): el*2 for el in range(10, 20)}
print(my_dict['10'])


my_set = {el**3 for el in range(5, 10)}
print(my_set)


# yield используется временно ооднажды обычно в функции или цикле
# чnобы не занимало оперативную память
def generator():
    for el in (10, 20, 30):
        yield el

g = generator()
print(g)

for el in g:
    print(el)


from functools import reduce # reduce используется для суммирования сумм

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элеент
    return prev_el + el

v = [x*10 for x in range(1, 4)]
print(reduce(my_func, v))



from functools import partial

def my_func(param_1, param_2):
    return param_1 ** param_2

new_my_func = partial(my_func, 2)
print(new_my_func)

# 2 возводим в 4-ую степень
print(new_my_func(4))



from itertools import count

for el in count(7):
    if el > 15:
        break
    else:
        print(el)


from itertools import cycle

c = 0
for el in cycle("ABC"):
    if c > 10:
        break
    print(el)
    c += 1










