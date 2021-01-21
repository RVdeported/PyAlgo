# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:16:45 2021

@author: Roman
"""

"""
3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
"""
import random as r

nums = [r.randint(0,99) for n in range(10)]
print(nums)
low_num_i = 0
large_num_i = 0

for i, n in enumerate(nums):
    if (n < nums[low_num_i]):
        low_num_i = i
    if (n > nums[large_num_i]):
        large_num_i = i

buff = nums[low_num_i]
nums[low_num_i] = nums[large_num_i]
nums[large_num_i] = buff
print(nums)
print(f'Changed {low_num_i} and {large_num_i} indexes with values {nums[low_num_i]} and {nums[large_num_i]}')