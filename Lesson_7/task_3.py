# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:26:17 2021

@author: Roman
"""

"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в 
другой — не больше медианы.
"""

import random


def median(arr):
    leng = len(arr)
    for i in range(leng):
        pivot = arr[i]
        Lcount = 0
        Rcount = 0
        Mcount = 0
        for t in arr:
            if (t > pivot):
                Lcount += 1
            elif (t < pivot):
                Rcount += 1
            else: Mcount += 1
        if (Rcount == Lcount):
            return i
        """
        В случае большого количества чисел равных медиане, идеальной медианы никогда не выйдет:
        по левую и правую сторону буду числа равные медиане.
        Для выявления таких медиан привдеена проверка ниже:
        """
        if (Rcount <= leng // 2 and 
            Lcount <= leng // 2 and
            (
            Rcount + Mcount > leng // 2 or
            Lcount + Mcount > leng // 2
            )):
            return i
    return None

m = 100
arr = [random.randint(0,100) for i in range(2*m + 1)]
print(f'initial arr:\n{arr}')
median = median(arr)
print(f'Median: {arr[median]}')
left = [i for i in arr if i < arr[median]]
mid = [i for i in arr if i == arr[median]]
right = [i for i in arr if i > arr[median]]
print(f'left side of median:\n{left}')
print(f'equal to median elements:\n{mid}')
print(f'right side of median:\n{right}')
print(f'lengh of left side {len(left)}')
print(f'lengh of right side {len(right)}')