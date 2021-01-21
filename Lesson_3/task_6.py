# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:43:28 2021

@author: Roman
"""
"""
6. В одномерном массиве найти сумму элементов, находящихся между 
минимальным и максимальным элементами. Сами минимальный и 
максимальный элементы в сумму не включать.
"""
import random as r

def minimax(n):
    nums = [r.randint(-99,99) for n in range(n)]
    low_num_i = 0
    large_num_i = 0
    # finding low and high indexes
    for i, n in enumerate(nums):
        if (n < nums[low_num_i]):
            low_num_i = i
        if (n > nums[large_num_i]):
            large_num_i = i
    # change indexes so low is start and high is end
    if (low_num_i > large_num_i):
        buff = low_num_i
        low_num_i = large_num_i
        large_num_i = buff
    summ = 0
    for n in nums[low_num_i + 1: large_num_i]:
        summ += n
    return summ


res = minimax(100)
print(res)
#print(f'Total sum is {summ}')
#print(f'Start index is {low_num_i}, end index is {large_num_i} with values {nums[low_num_i]} and {nums[large_num_i]}')