# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:45:29 2021

@author: Roman
"""

"""
1. В диапазоне натуральных чисел от 2 до 99 определить, 
сколько из них кратны каждому из чисел в диапазоне от 2 до 9. 
Примечание: 8 разных ответов.
"""

import sys

def original(n):
    res = [0] * 8
    for j in range(2, 10):
        for i in range(2, n+1):
            if i % j == 0:
                res[j-2] += 1
    #---------memo evaluation-----------
    occupied_items = [res, j, i] + [i for i in res]
    occupied_memo = 0
    for t in occupied_items:
        occupied_memo += sys.getsizeof(t)
    #-----------------------------------
    return res, occupied_memo

def useless_recursion(n, start = 2, memo = 0):
    #-----------------------------------
    memo += sys.getsizeof(n) + sys.getsizeof(start)
    #-----------------------------------
    if (start > 9):
        return [], memo
    count = 0
    for i in range(2, n + 1):
        if (i % start == 0):
            count += 1
    res = [count]
    #--------memo evaluation------------
    occupied_items = [res, i, count] + [u for u in res]
    for t in occupied_items:
        memo += sys.getsizeof(t)
    #-----------------------------------
    temp = useless_recursion(n, start + 1, memo)
    res += temp[0]
    
    memo += temp[1]
    
    return res, memo

def cheated(n):
    res = [0] * 8
    for t in range(2,10):
        res[t-2] = n // t
    
    occupied_items = [res, t] + [i for i in res]
    occupied_memo = 0
    for u in occupied_items:
        occupied_memo += sys.getsizeof(u)
    return res, occupied_memo

print("Results of the three algorithms:")
print(f'original: {original(99)[1]}')
print(f'recursion: {useless_recursion(99)[1]}')
print(f'cheated: {cheated(99)[1]}')

"""
python v 3.6.5 (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
win32

Первый алгоритм требует для выполнения лист и несколько переменных, что достаточно эффективно по выделнию памяти.
На моей машине получилось 408 байт.

Рекурсивный алгоритм ожидаемо занял заметно больше места - 9384 байт. Однако, стоит заметить, что это выделение памяти в момент
последнего рекурсивного обхода, когда алгоритм развораяивается полностью. Одна итерация же занимает около 212 байт, что дает
некий потенциал существенно сократить занимающую память (например, передавая в рекурсии один и тот же лит res)

Наиболее эффективным ожидаемо оказался алгоритм деления за счет того, что использует на одну переменную меньше - 380 байт
"""



