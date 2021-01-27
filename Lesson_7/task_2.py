# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:58:44 2021

@author: Roman
"""

"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и 
отсортированный массивы.
"""

import random

def mergesort(arr):
    if len(arr) > 2:
        pivot = len(arr) // 2
        arr = mergesort(arr[:pivot]) + mergesort(arr[pivot:]) 
        arr_1 = []
        i = 0
        t = pivot
        while (len(arr_1) < len(arr)):
            if (arr[i] > arr[t]):
                arr_1.append(arr[t])
                t += 1
            else:
                arr_1.append(arr[i])
                i += 1
            if (i >= pivot or t >= len(arr)):
                arr_1 += arr[i:pivot] + arr[t:]
                break
        arr = arr_1
    elif len(arr) == 2:
        if (arr[0] > arr[1]):
            return [arr[1], arr[0]]
    return arr


arr = [random.randint(0,50) for i in range(100)]

true_arr = sorted(arr)
print(f'initial arr:\n{arr}')
arr = mergesort(arr)
print(f'sorted arr:\n{arr}')
print(f'arr sorted correctly: {arr == true_arr}')